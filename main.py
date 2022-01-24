from LyxaLib import Chatbot
from bs4 import BeautifulSoup, Tag
from pypol.interpreter import Interpreter
import sys
import traceback
from capture import Capturing
from multiprocessing import Process, Queue
import re
import mistletoe
from markdownify import markdownify as md
from github import Github #upm package(PyGithub)
import os
import schedule
import time

PARTS = {
  "pre": "Prefixes and Suffixes",
  "suf": "Prefixes and Suffixes",
  "n": "Nouns",
  "noun": "Nouns",
  "v": "Verbs",
  "adj": "Adjectives",
  "a": "Adjectives",
  "pron": "Pronouns",
  "pro": "Pronouns",
  "adv": "Adverbs",
  "part": "Case Particles",
  "par": "Case Particles",
  "int": "Interjections",
  "intj": "Interjections",
  "conj": "Conjunctions",
  "othr": "Other",
  "other": "Other",
  "misc": "Other"
}

ADMINS = [347075, 533049]

wordCache = []

def run(code, q):
  with Capturing() as out:
    try:
      r = interpreter.run(code)
    except Exception as e:
      q.put(interpreter.lastError[1])
      return
    else:
      if not out:
        out = []
      print(r, out)
      q.put([r] + out)

def buildResults(data):
  data = [str(x) for x in data]
  if len(data) > 5:
    return "\n".join(data[:5]) + "\n(" + str(len(data)-5) + " more hidden)"
  else:
    return "\n".join(data)

def execute(msg, data):
  soup = BeautifulSoup(msg, 'html.parser')
  code = str(soup.code.string)
  id_ = room.sendMessage("Processing: `" + code + "`")
  print(code)
  interpreter.restart()
  q = Queue()
  t = Process(target=run, args=(code, q))
  t.start()
  t.join(10)
  if t.is_alive():
    print("Timeout reached")
    t.terminate()
    t.join()
    print("EFF")
    room.editMessage(":" + str(data["e"][0]["message_id"]) + " Error: Timeout reached. Make sure your code wasn't an infinite loop!", id_)
  else:
    out = q.get()
    if type(out) == list:
      print(out, buildResults(out))
      room.editMessage(":" + str(data["e"][0]["message_id"]) + " Results: " + buildResults(out), id_)
    else:
      print('err', repr(out))
      room.editMessage(":" + str(data["e"][0]["message_id"]) + " Error executing program: `" + repr(out) + "')`", id_)

def messageHandler(data):
  msg = data["e"][0]["content"]
  if msg.startswith("@<code>"):
    execute(msg, data)
    

def dumpCache():
  try:
    global wordCache
    if not len(wordCache):
        return
    repo = g.get_repo("katlani/katlani")
    contents = repo.get_contents("vocab.md")
    mdDoc = BeautifulSoup(mistletoe.markdown(contents.decoded_content.decode("utf-8")), 'html.parser')
    #print(mdDoc)
    for word, part, definition, _, __ in wordCache:
      #print(word, part, definition)
      header = [i  for i in mdDoc.find_all("h2") if i.string == PARTS[part]][0]
      lst = header.find_next_sibling("ul")
      dupe = False
      for c, i in enumerate(lst.find_all(True)):
        if type(i) == Tag:
          if i.name == "li":
            if str(i.code.string).lower() == word.lower():
              dupe = True
              break
      if dupe:
        continue
    
      newItem = mdDoc.new_tag("li")
      code = mdDoc.new_tag("code")
      code.string = word
      newItem.append(code)
      newItem.append(" - " + definition)
      pos = 0
      for c, i in enumerate(lst.find_all(True)):
        if type(i) == Tag:
          if i.name == "li":
            #print(str(i.code.string), word)
            if str(i.code.string) > word:
              pos = c
      lst.insert(pos, newItem)
    repo.update_file(contents.path, "Added " + str(len(wordCache)) + " new words", md(str(mdDoc)), contents.sha)
    langRoom.sendMessage("Push complete, successfully added " + str(len(wordCache)) + " new words!")
    wordCache = []
  except Exception as e:
    langRoom.sendMessage("Something's gone horribly wrong!" + repr(e))
    print("An error occured!", repr(e), traceback.format_exc())
  
  
def langHandler(data):
  global wordCache
  print(data)
  if data["e"][0]["event_type"] == 1:
    msg = data["e"][0]["content"]
    if msg == "@PUSH" and data["e"][0]["user_id"] == 533049:
      try:
        dumpCache()
      except Exception as e:
        traceback.print_exc()
    if msg == "@HALT" and data["e"][0]["user_id"] == 533049:
      langRoom.sendMessage("Halting")
      bot.leaveAllRooms()
      sys.exit()
    if msg == "@LIST":
      queue = ""
      for word, part, defi, user_id, _ in wordCache:
        queue += "\n"
        if user_id == data["e"][0]["user_id"]:
          queue += "* "
        queue += f"{word} ({part}): {defi}"
      langRoom.sendMessage(f":{data["e"][0]["message_id"]} {queue}")
      return
    if msg.startswith("@REMOVE"):
      processed_msg = msg[8:]
      if processed_msg.endswith("."):
        processed_msg = processed_msg[:-1]
      for ind, (word, _, _, user_name, _) in wordCache.copy():
         if processed_msg == word and (user_name==data["e"]["user_name"] or user_name in ADMINS):
           wordCache.pop(ind)
    if msg.startswith("<b>WR: "):
      processed_msg = re.sub("<\/?code>", "", re.sub("</?b>", "", msg))
      word, part, definition = re.fullmatch("^WR: ([\w ]+) \(([\w.]+)\): (.*)$", processed_msg).groups()
      if part.endswith("."):
        part = part[:-1]
      invalid_letters = [letter for letter in "cejqwx" if letter in word]
      if invalid_letters:
        langRoom.sendMessage(f":{data["e"][0]["message_id"]} Word contains illegal letters: {invalid_letters}!")
        return
      if part not in PARTS:
        langRoom.sendMessage(f":{data["e"][0]["message_id"]} Invalid part of speech!")
        return
      if word[-1] == "i":
        langRoom.sendMessage(f":{data["e"][0]["message_id"]} Word ends in -i!")
        return
      id_ = langRoom.sendMessage(":" + str(data["e"][0]["message_id"]) + " Word " + word + " added to queue.")
      wordCache.append((word, part, definition, data["e"]["user_id"], id_))
  elif data["e"][0]["event_type"] == 18:
    e = data["e"]
    for word in wordCache:
      if word[4] == e["parent_id"]:
        if word[3] == e["user_id"] or e["user_id"] in ADMINS:
          pass


interpreter = Interpreter()
g = Github("TOKEN")
schedule.every(30).minutes.do(dumpCache)

bot = Chatbot()
bot.login()
room = bot.joinRoom(133058, messageHandler)
langRoom = bot.joinRoom(133067, langHandler)
try:
  while True:
    schedule.run_pending()
    time.sleep(1)
except:
  bot.leaveAllRooms()
  bot.logout()
  raise
