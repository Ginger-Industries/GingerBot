import time, math, string, random



CONSTANTS = {
  "↹": "PyPOL APOL interpreter v0.1.5 by Ginger Industries 2021",
  "T": True, 
  "F": False, 
  "X": None,
  "ĥ": "Hello, World!", 
  "ô": 100,
  "õ": 1000,
  "ö": 10000,
  "ø": 100000,
  "ó": 1000000,
  "ò": 1000000000,
  "π": math.pi,
  "ε": math.e,
  "Ⓠ": "qwertyuiop",
  "Ⓔ": "aeiou",
  "⒬": list("qwertyuiop"),
  "Ⓐ": string.ascii_letters,
  "⒜": list(string.ascii_letters),
  "ⓛ": string.ascii_lowercase,
  "Ⓛ": string.ascii_uppercase,
  "①": "".join([str(_) for _ in list(range(10))]),
  "⑴": list(range(10)),
  "⑩": list(range(1, 100)),
  "⑽": "".join([str(_) for _ in list(range(1, 100))]),
  "⑨": list(range(100)),
  "⑼": "".join([str(_) for _ in list(range(100))]),
  "⒈": 16,
  "⒉": 32,
  "⒊": 64,
  "⒋": 128,
  "⒌": 256,
  "⒍": 512,
  "⒎": 1024,
  "⒏": 2048,
  "⒐": 4096,
  "⒑": 8192,
  "⒒": 16384,
  "⒓": 32768,
  "⒔": 65536,
  "⒕": 2147483648,
  "⒖": 4294967296
}



class Instruction():
  def __init__(self, interpreter):
    self.interpreter = interpreter
class ConstantInstruction(Instruction):
  def __init__(self, constant):
    self.constant = constant
  def execute(self):
    return self.constant

class PrintInstruction(Instruction):
  def __init__(self, interpreter, output, end="\n"):
    self.output = output
    self.end = end
  def execute(self):
    o = None
    try:
      o = self.output.execute()
    except AttributeError:
      o = self.output
    try:
      e = self.end.execute()
    except AttributeError:
      e = self.end
    if type(o) == float:
      #print(o - int(0))
      if o - int(o) == 0:
        o = int(o)
    print(o, end=e)
class StringSplitInstruction(Instruction):
  def __init__(self, interpreter, string, sep=" "):
    self.string = string
    self.sep = sep
  def execute(self):
    o = None
    try:
      o = self.string.execute()
    except AttributeError:
      o = self.string
    try:
      e = self.sep.execute()
    except AttributeError:
      e = self.sep
    return o.split(e)
class InputInstruction(Instruction):
  def __init__(self, interpreter, prompt=""):
    self.prompt = prompt
  def execute(self):
    try:
      prompt = self.prompt.execute()
    except AttributeError:
      prompt = self.prompt
    return input(prompt)
class FloatInputInstruction(Instruction):
  def __init__(self, interpreter, prompt=""):
    self.prompt = prompt
  def execute(self):
    try:
      prompt = self.prompt.execute()
    except AttributeError:
      prompt = self.prompt
    try:
      return float(input(prompt))
    except ValueError:
      return None
class IntInputInstruction(Instruction):
  def __init__(self, interpreter, prompt=""):
    self.prompt = prompt
  def execute(self):
    try:
      prompt = self.prompt.execute()
    except AttributeError:
      prompt = self.prompt
    try:
      return int(float(input(prompt)))
    except ValueError:
      return None

class AdditionInstruction(Instruction):
  def __init__(self, interpreter, n1, n2):
    self.n1 = n1
    self.n2 = n2
  def execute(self):
    try:
      n1 = self.n1.execute()
    except AttributeError:
      n1 = self.n1
    try:
      n2 = self.n2.execute()
    except AttributeError:
      n2 = self.n2
    return n1 + n2
class SubtractionInstruction(Instruction):
  def __init__(self, interpreter, n1, n2):
    self.n1 = n1
    self.n2 = n2
  def execute(self):
    try:
      n1 = self.n1.execute()
    except AttributeError:
      n1 = self.n1
    try:
      n2 = self.n2.execute()
    except AttributeError:
      n2 = self.n2
    return n1 - n2
class MultiplicationInstruction(Instruction):
  def __init__(self, interpreter, n1, n2):
    self.n1 = n1
    self.n2 = n2
  def execute(self):
    try:
      n1 = self.n1.execute()
    except AttributeError:
      n1 = self.n1
    try:
      n2 = self.n2.execute()
    except AttributeError:
      n2 = self.n2
    if type(n1) == float or type(n1) == int:
      return n1 * n2
    else:
      return n1 * int(n2)
class DivisionInstruction(Instruction):
  def __init__(self, interpreter, n1, n2):
    self.n1 = n1
    self.n2 = n2
  def execute(self):
    try:
      n1 = self.n1.execute()
    except AttributeError:
      n1 = self.n1
    try:
      n2 = self.n2.execute()
    except AttributeError:
      n2 = self.n2
    return n1 / n2
class FloorDivisionInstruction(Instruction):
  def __init__(self, interpreter, n1, n2):
    self.n1 = n1
    self.n2 = n2
  def execute(self):
    try:
      n1 = self.n1.execute()
    except AttributeError:
      n1 = self.n1
    try:
      n2 = self.n2.execute()
    except AttributeError:
      n2 = self.n2
    return n1 // n2
class ModuloInstruction(Instruction):
  def __init__(self, interpreter, n1, n2):
    self.n1 = n1
    self.n2 = n2
  def execute(self):
    try:
      n1 = self.n1.execute()
    except AttributeError:
      n1 = self.n1
    try:
      n2 = self.n2.execute()
    except AttributeError:
      n2 = self.n2
    return n1 % n2
class ExponentInstruction(Instruction):
  def __init__(self, interpreter, n1, n2=2):
    self.n1 = n1
    self.n2 = n2
  def execute(self):
    try:
      n1 = self.n1.execute()
    except AttributeError:
      n1 = self.n1
    try:
      n2 = self.n2.execute()
    except AttributeError:
      n2 = self.n2
    return n1 ** n2

class ExecuteAsAPOLInstruction(Instruction):
  def __init__(self, interpreter, code):
    self.code = code
    self.interpreter = interpreter
  def execute(self):
    return self.interpreter.interpret(self.code)[0].execute()
class ExecuteAsPythonInstruction(Instruction):
  def __init__(self, interpreter, code):
    self.code = code
    self.interpreter = interpreter
  def execute(self):
    return eval(self.code)

class ListAppendInstruction(Instruction):
  def __init__(self, interpreter, address, data):
    self.address = address
    self.data = data
    self.interpreter = interpreter
  def execute(self):
    try:
      address = self.address.execute()
    except AttributeError:
      address = self.address
    try:
      data = self.data.execute()
    except AttributeError:
      data = self.data
    if type(self.interpreter.memory.get(address)) == list:
      self.interpreter.memory.get(address).append(data)
    else:
      raise ValueError("Value at cell index " + str(address) + " isn't a list!")
class ListSumInstruction(Instruction):
  def __init__(self, interpreter, data):
    self.data = data
    self.interpreter = interpreter
  def execute(self):
    try:
      data = self.data.execute()
    except AttributeError:
      data = self.data
    if type(data) == list:
      return sum(data)
    elif type(data) == float or type(data) == int:
      return sum(int(x) for x in list(str(int(data))))
    else:
      raise ValueError("Unable to interpret \'" + str(data) + "\' as list or number!")
class ListGetInstruction(Instruction):
  def __init__(self, interpreter, list_, index=0):
    self.index = index
    self.list_ = list_
  def execute(self):
    try:
      index = self.index.execute()
    except AttributeError:
      index = self.index
    try:
      l = self.list_.execute()
    except AttributeError:
      l = self.list_
    return l[int(index)]
class ListSetInstruction(Instruction):
  def __init__(self, interpreter, list_, value, index=0):
    self.index = index
    self.list_ = list_
    self.value = value
  def execute(self):
    try:
      index = self.index.execute()
    except AttributeError:
      index = self.index
    try:
      l = self.list_.execute()
    except AttributeError:
      l = self.list_
    try:
      v = self.value.execute()
    except AttributeError:
      v = self.value
    l[int(index)] = v
    return l
class ListPopInstruction(Instruction):
  def __init__(self, interpreter, list_, index=0):
    self.index = index
    self.list_ = list_
  def execute(self):
    try:
      index = self.index.execute()
    except AttributeError:
      index = self.index
    try:
      l = self.list_.execute()
    except AttributeError:
      l = self.list_
    l.pop(int(index))
    return l
class ListRemoveInstruction(Instruction):
  def __init__(self, interpreter, list_, value):
    self.list_ = list_
    self.value = value
  def execute(self):
    try:
      l = self.list_.execute()
    except AttributeError:
      l = self.list_
    try:
      v = self.value.execute()
    except AttributeError:
      v = self.value
    l.remove(v)
    return l
class ListFlattenInstruction(Instruction):
  def __init__(self, interpreter, string):
    # too lazy to change string to list
    self.string = string
  def execute(self):
    try:
      s = self.string.execute()
    except AttributeError:
      s = self.string
    flat_list = []
    # Iterate through the outer list
    for element in s:
      if type(element) is list:
        # If the element is of type list, iterate through the sublist
        for item in element:
            flat_list.append(item)
      else:
        flat_list.append(element)
    return flat_list
class UnduplicateListInstruction(Instruction):
  def __init__(self, interpreter, string):
    # too lazy to change string to list
    self.string = string
  def execute(self):
    try:
      s = self.string.execute()
    except AttributeError:
      s = self.string
    return list(dict.fromkeys(s))

class MemoryWriteInstruction(Instruction):
  def __init__(self, interpreter, address, data=0):
    self.address = address
    self.data = data
    self.interpreter = interpreter
  def execute(self):
    try:
      address = self.address.execute()
    except AttributeError:
      address = self.address
    try:
      data = self.data.execute()
    except AttributeError:
      data = self.data
    self.interpreter.memory[int(address)] = data
class DynamicReadInstruction(Instruction):
  def __init__(self, interpreter, address, data=0):
    self.address = address
    self.interpreter = interpreter
  def execute(self):
    try:
      address = self.address.execute()
    except AttributeError:
      address = self.address
    return MemoryReadInstruction(self.interpreter, int(address)).execute()
class MemoryReadInstruction(Instruction):
  # This class is not meant to be created directly, use the superscript numbers instead
  def __init__(self, interpreter, address):
    self.address = int(address)
    self.interpreter = interpreter
  def execute(self):
    return self.interpreter.memory.get(self.address)
class ReverseInstruction(Instruction):
  def __init__(self, interpreter, string):
    self.string = string
  def execute(self):
    try:
      s = self.string.execute()
    except AttributeError:
      s = self.string
    if type(s) == list:
      return list(reversed(s))
    return s[::-1]
class SortInstruction(Instruction):
  def __init__(self, interpreter, string):
    self.string = string
  def execute(self):
    try:
      s = self.string.execute()
    except AttributeError:
      s = self.string
    return sorted(s)
class StringLengthInstruction(Instruction):
  def __init__(self, interpreter, string):
    self.string = string
  def execute(self):
    try:
      s = self.string.execute()
    except AttributeError:
      s = self.string
    return len(s)
class StringFindInstruction(Instruction):
  def __init__(self, interpreter, string, toFind):
    self.string = string
    self.toFind = toFind
  def execute(self):
    try:
      s = self.string.execute()
    except AttributeError:
      s = self.string
    try:
      f = self.toFind.execute()
    except AttributeError:
      f = self.toFind
    return s.find(f)
class StringContainsInstruction(Instruction):
  def __init__(self, interpreter, string, toFind):
    self.string = string
    self.toFind = toFind
  def execute(self):
    try:
      s = self.string.execute()
    except AttributeError:
      s = self.string
    try:
      f = self.toFind.execute()
    except AttributeError:
      f = self.toFind
    return f in s
class StringReplaceInstruction(Instruction):
  def __init__(self, interpreter, string, toFind, replaceWith):
    self.string = string
    self.toFind = toFind
    self.replaceWith = replaceWith
  def execute(self):
    try:
      s = self.string.execute()
    except AttributeError:
      s = self.string
    try:
      f = self.toFind.execute()
    except AttributeError:
      f = self.toFind
    try:
      r = self.replaceWith.execute()
    except AttributeError:
      r = self.replaceWith
    return s.replace(f, r)
class CountInstruction(Instruction):
  def __init__(self, interpreter, string, toFind):
    self.string = string
    self.toFind = toFind
  def execute(self):
    try:
      s = self.string.execute()
    except AttributeError:
      s = self.string
    try:
      f = self.toFind.execute()
    except AttributeError:
      f = self.toFind
    if type(s) == str:
      return s.count(f)
    elif type(s) == list:
      return sum([1 if x == f else 0 for x in s])
class StringJoinInstruction(Instruction):
  def __init__(self, interpreter, list_, sep=""):
    self.string = list_
    self.sep = sep
  def execute(self):
    try:
      s = self.string.execute()
    except AttributeError:
      s = self.string
    try:
      f = self.sep.execute()
    except AttributeError:
      f = self.sep
    return f.join([str(i) for i in s])
class SubstringInstruction(Instruction):
  def __init__(self, interpreter, instr, start, end=None):
    self.instr = instr
    if end == -1:
      self.end = start
      self.start = 0
    else:
      self.start = start
      self.end = end
    
  def execute(self):
    try:
      t = self.instr.execute()
    except AttributeError:
      t = self.instr
    try:
      s = self.start.execute()
    except AttributeError:
      s = self.start
    try:
      e = self.end.execute()
    except AttributeError:
      e = self.end
    return t[s:e]
class StringUppercaseInstruction(Instruction):
  def __init__(self, interpreter, string):
    self.string = string
  def execute(self):
    try:
      s = self.string.execute()
    except AttributeError:
      s = self.string
    return s.upper()
class StringLowercaseInstruction(Instruction):
  def __init__(self, interpreter, string):
    self.string = string
  def execute(self):
    try:
      s = self.string.execute()
    except AttributeError:
      s = self.string
    return s.lower()

class Char2CodepointInstruction(Instruction):
  def __init__(self, interpreter, string):
    self.string = string
  def execute(self):
    try:
      s = self.string.execute()
    except AttributeError:
      s = self.string
    return ord(s[0])
class Codepoint2CharInstruction(Instruction):
  def __init__(self, interpreter, string):
    self.string = string
  def execute(self):
    try:
      s = self.string.execute()
    except AttributeError:
      s = self.string
    return chr(s)
class Num2BinaryInstruction(Instruction):
  def __init__(self, interpreter, string):
    self.string = string
  def execute(self):
    try:
      s = self.string.execute()
    except AttributeError:
      s = self.string
    return bin(s)[2:]
class Binary2NumInstruction(Instruction):
  def __init__(self, interpreter, string):
    self.string = string
  def execute(self):
    try:
      s = self.string.execute()
    except AttributeError:
      s = self.string
    return int(s, 2)

class CastToNumberInstruction(Instruction):
  def __init__(self, interpreter, value):
    self.value = value
  def execute(self):
    try:
      value = self.value.execute()
    except AttributeError:
      value = self.value
    try:
      return int(value)
    except ValueError:
      try:
        return float(value)
      except ValueError:
        return None
class CastToListInstruction(Instruction):
  def __init__(self, interpreter, value):
    self.value = value
  def execute(self):
    try:
      value = self.value.execute()
    except AttributeError:
      value = self.value
    try:
      return list(value)
    except ValueError:
      return None
class CastToIntListInstruction(Instruction):
  def __init__(self, interpreter, value):
    self.value = value
  def execute(self):
    try:
      value = self.value.execute()
    except AttributeError:
      value = self.value
    try:
      return [int(i) for i in value]
    except ValueError:
      return None
class CastToStringInstruction(Instruction):
  def __init__(self, interpreter, value):
    self.value = value
  def execute(self):
    try:
      value = self.value.execute()
    except AttributeError:
      value = self.value
    try:
      if type(value) == float:
        if value - int(value) == 0:
          return str(int(value))
      return str(value)
    except ValueError:
      return None

class LessThanComparison(Instruction):
  def __init__(self, interpreter, n1, n2):
    self.n1 = n1
    self.n2 = n2
  def execute(self):
    try:
      n1 = self.n1.execute()
    except AttributeError:
      n1 = self.n1
    try:
      n2 = self.n2.execute()
    except AttributeError:
      n2 = self.n2
    return n1 < n2
class GreaterThanComparison(Instruction):
  def __init__(self, interpreter, n1, n2):
    self.n1 = n1
    self.n2 = n2
  def execute(self):
    try:
      n1 = self.n1.execute()
    except AttributeError:
      n1 = self.n1
    try:
      n2 = self.n2.execute()
    except AttributeError:
      n2 = self.n2
    return n1 > n2
class LessThanOrEqualToComparison(Instruction):
  def __init__(self, interpreter, n1, n2):
    self.n1 = n1
    self.n2 = n2
  def execute(self):
    try:
      n1 = self.n1.execute()
    except AttributeError:
      n1 = self.n1
    try:
      n2 = self.n2.execute()
    except AttributeError:
      n2 = self.n2
    return n1 <= n2
class GreaterThanOrEqualToComparison(Instruction):
  def __init__(self, interpreter, n1, n2):
    self.n1 = n1
    self.n2 = n2
  def execute(self):
    try:
      n1 = self.n1.execute()
    except AttributeError:
      n1 = self.n1
    try:
      n2 = self.n2.execute()
    except AttributeError:
      n2 = self.n2
    return n1 >= n2
class EqualComparison(Instruction):
  def __init__(self, interpreter, n1, n2):
    self.n1 = n1
    self.n2 = n2
  def execute(self):
    try:
      n1 = self.n1.execute()
    except AttributeError:
      n1 = self.n1
    try:
      n2 = self.n2.execute()
    except AttributeError:
      n2 = self.n2
    return n1 == n2
class UnequalComparison(Instruction):
  def __init__(self, interpreter, n1, n2):
    self.n1 = n1
    self.n2 = n2
  def execute(self):
    try:
      n1 = self.n1.execute()
    except AttributeError:
      n1 = self.n1
    try:
      n2 = self.n2.execute()
    except AttributeError:
      n2 = self.n2
    return n1 != n2
class BetweenInstruction(Instruction):
  def __init__(self, interpreter, n1, n2, n3):
    self.n1 = n1
    self.n2 = n2
    self.n3 = n3
  def execute(self):
    try:
      n1 = self.n1.execute()
    except AttributeError:
      n1 = self.n1
    try:
      n2 = self.n2.execute()
    except AttributeError:
      n2 = self.n2
    try:
      n3 = self.n3.execute()
    except AttributeError:
      n3 = self.n3
    return n1 < n2 < n3

class AndInstruction(Instruction):
  def __init__(self, interpreter, i1, i2):
    self.i1 = i1
    self.i2 = i2
  def execute(self):
    try:
      i1 = self.i1.execute()
    except AttributeError:
      i1 = self.i1
    try:
      i2 = self.i2.execute()
    except AttributeError:
      i2 = self.i2
    
    return i1 and i2
class OrInstruction(Instruction):
  def __init__(self, interpreter, i1, i2):
    self.i1 = i1
    self.i2 = i2
  def execute(self):
    try:
      i1 = self.i1.execute()
    except AttributeError:
      i1 = self.i1
    try:
      i2 = self.i2.execute()
    except AttributeError:
      i2 = self.i2
    
    return i1 or i2
class NotInstruction(Instruction):
  def __init__(self, interpreter, i1):
    self.i1 = i1
  def execute(self):
    try:
      i1 = self.i1.execute()
    except AttributeError:
      i1 = self.i1
    
    return not i1

class IncreaseInstruction(Instruction):
  def __init__(self, interpreter, address, amount=1):
    self.interpreter = interpreter
    self.address = address
    self.amount = amount
  def execute(self):
    try:
      a = self.address.execute()
    except AttributeError:
      a = self.address
    try:
      i = self.amount.execute()
    except AttributeError:
      i = self.amount
    self.interpreter.memory[a] += i
class DecreaseInstruction(Instruction):
  def __init__(self, interpreter, address, amount=1):
    self.interpreter = interpreter
    self.address = address
    self.amount = amount
  def execute(self):
    try:
      a = self.address.execute()
    except AttributeError:
      a = self.address
    try:
      i = self.amount.execute()
    except AttributeError:
      i = self.amount
    self.interpreter.memory[a] -= i
class GetSignInstruction(Instruction):
  def __init__(self, interpreter, n1):
    self.n1 = n1
  def execute(self):
    try:
      n1 = self.n1.execute()
    except AttributeError:
      n1 = self.n1
    return n1 >= 0
class GetEvenInstruction(Instruction):
  def __init__(self, interpreter, n1):
    self.n1 = n1
  def execute(self):
    try:
      n1 = self.n1.execute()
    except AttributeError:
      n1 = self.n1
    return not bool(n1 % 2)
class AbsoluteValueInstruction(Instruction):
  def __init__(self, interpreter, n1):
    self.n1 = n1
  def execute(self):
    try:
      n1 = self.n1.execute()
    except AttributeError:
      n1 = self.n1
    return abs(n1)
class RoundInstruction(Instruction):
  def __init__(self, interpreter, n):
    self.n = n
  def execute(self):
    try:
      n = self.n.execute()
    except AttributeError:
      n = self.n
    return round(n)
class RandomNumberInstruction(Instruction):
  def __init__(self, interpreter, n1, n2=None):
    if not n2:
      self.n2 = n1
      self.n1 = 0
    else:
      self.n1 = n1
      self.n2 = n2
  def execute(self):
    try:
      n1 = self.n1.execute()
    except AttributeError:
      n1 = self.n1
    try:
      n2 = self.n2.execute()
    except AttributeError:
      n2 = self.n2
    return random.randint(n1, n2)
class RandomFloatInstruction(Instruction):
  def execute(self):
    return random.random()

class WhileLoopInstruction(Instruction):
  def __init__(self, interpreter, comparison, *args):
    self.interpreter = interpreter
    self.comparison = comparison
    self.instructions = args
  def execute(self):
    v = True
    c = 0
    while v:
      self.interpreter._forLoopCounter = c
      self.interpreter._forLoopItem = v
      try:
        v = self.comparison.execute()
      except AttributeError:
        v = self.comparison
      for i in self.instructions:
        try:
          i.execute()
        except AttributeError:
          pass
      c += 1
class PrecheckWhileLoopInstruction(Instruction):
  def __init__(self, interpreter, comparison, *args):
    self.interpreter = interpreter
    self.comparison = comparison
    self.instructions = args
  def execute(self):
    try:
      v = self.comparison.execute()
    except AttributeError:
      v = self.comparison
    c = 0
    while v:
      self.interpreter._forLoopCounter = c
      self.interpreter._forLoopItem = v
      try:
        v = self.comparison.execute()
      except AttributeError:
        v = self.comparison
      for i in self.instructions:
        try:
          i.execute()
        except AttributeError:
          pass
class ForLoopInstruction(Instruction):
  def __init__(self, interpreter, iterations, *args):
    self.interpreter = interpreter
    self.iterations = iterations
    self.instructions = args
  def execute(self):
    try:
      i = self.iterations.execute()
    except AttributeError:
      i = self.iterations
    if type(i) == float or type(i) == int:
      self.interpreter._forLoopIterator = i
      i = range(int(i))
    else:
      self.interpreter._forLoopIterator = i
    for c, x in enumerate(i):
      self.interpreter._forLoopCounter = c
      self.interpreter._forLoopItem = x
      for l in self.instructions:
        try:
          l.execute()
        except AttributeError:
          pass
    self.interpreter._forLoopCounter = None
    self.interpreter._forLoopItem = None
    self.interpreter._forLoopIterator = None
class StartEndForLoopInstruction(Instruction):
  def __init__(self, interpreter, start, end, *args):
    self.interpreter = interpreter
    self.start = start
    self.end = end
    self.instructions = args
  def execute(self):
    try:
      s = self.start.execute()
    except AttributeError:
      s = self.start
    try:
      e = self.end.execute()
    except AttributeError:
      e = self.end
    self.interpreter._forLoopIterator = e
    for c, x in enumerate(range(s, e)):
      self.interpreter._forLoopCounter = c
      self.interpreter._forLoopItem = x
      for l in self.instructions:
        try:
          l.execute()
        except AttributeError:
          pass
    self.interpreter._forLoopCounter = None
    self.interpreter._forLoopItem = None
    self.interpreter._forLoopIterator = None
class OneForLoopInstruction(Instruction):
  def __init__(self, interpreter, iterations, *args):
    self.interpreter = interpreter
    self.iterations = iterations
    self.instructions = args
  def execute(self):
    try:
      i = self.iterations.execute()
    except AttributeError:
      i = self.iterations
    if type(i) == float or type(i) == int:
      self.interpreter._forLoopIterator = i
      i = range(int(i))
    else:
      self.interpreter._forLoopIterator = i

    for c, x in enumerate(i):
      self.interpreter._forLoopCounter = c+1
      self.interpreter._forLoopItem = x
      for l in self.instructions:
        try:
          l.execute()
        except AttributeError:
          pass
    self.interpreter._forLoopCounter = None
    self.interpreter._forLoopItem = None
    self.interpreter._forLoopIterator = None
class ListBuilderForLoopInstruction(Instruction):
  def __init__(self, interpreter, iterations, instruction):
    self.interpreter = interpreter
    self.iterations = iterations
    self.instruction = instruction
  def execute(self):
    try:
      i = self.iterations.execute()
    except AttributeError:
      i = self.iterations
    if type(i) == float or type(i) == int:
      self.interpreter._forLoopIterator = i
      i = range(int(i))
    else:
      self.interpreter._forLoopIterator = i
      
    r = []
    for c, x in enumerate(i):
      self.interpreter._forLoopCounter = c
      self.interpreter._forLoopItem = x
      try:
        r.append(self.instruction.execute())
      except AttributeError:
        pass
    self.interpreter._forLoopCounter = None
    self.interpreter._forLoopItem = None
    self.interpreter._forLoopIterator = None
    return r
class LoopCounterInstruction(Instruction):
  def __init__(self, interpreter):
    self.interpreter = interpreter
  def execute(self):
    if self.interpreter._forLoopCounter != None:
      return self.interpreter._forLoopCounter
    else:
      raise ValueError("Cannot use this instruction outside of a for loop!")
class ForIteratorInstruction(Instruction):
  def __init__(self, interpreter):
    self.interpreter = interpreter
  def execute(self):
    if self.interpreter._forLoopIterator != None:
      return self.interpreter._forLoopIterator
    else:
      raise ValueError("Cannot use this instruction outside of a for loop!")
class LoopItemInstruction(Instruction):
  def __init__(self, interpreter):
    self.interpreter = interpreter
  def execute(self):
    if self.interpreter._forLoopItem != None:
      return self.interpreter._forLoopItem
    else:
      raise ValueError("Cannot use this instruction outside of a for loop!")
class FunctionInstruction(Instruction):
  def __init__(self, interpreter, *args):
    self.instructions = args
  def execute(self):
    for l in self.instructions:
      try:
        l.execute()
      except AttributeError:
        pass
class IfInstruction(Instruction):
  def __init__(self, interpreter, condition, true, false=None):
    self.interpreter = interpreter
    self.condition = condition
    self.true = true
    self.false = false
  def execute(self):
    try:
      c = self.condition.execute()
    except AttributeError:
      c = self.condition
    self.interpreter._ifItem = c
    if bool(c):
      try:
        r = self.true.execute()
      except AttributeError:
        r = self.true
    else:
      try:
        r = self.false.execute()
      except AttributeError:
        r = self.false
    self.interpreter._ifItem = None
class ReturningIfInstruction(Instruction):
  def __init__(self, interpreter, condition, true, false=None):
    self.interpreter = interpreter
    self.condition = condition
    self.true = true
    self.false = false
  def execute(self):
    try:
      c = self.condition.execute()
    except AttributeError:
      c = self.condition
    self.interpreter._ifItem = c
    if bool(c):
      try:
        r = self.true.execute()
      except AttributeError:
        r = self.true
    else:
      try:
        r = self.false.execute()
      except AttributeError:
        r = self.false
    self.interpreter._ifItem = None
    return r
class IfItemInstruction(Instruction):
  def execute(self):
    if not self.interpreter._ifItem:
      raise ValueError("Cannot use this instruction outside of an if statement!")
    return self.interpreter._ifItem

class DelayInstruction(Instruction):
  def __init__(self, interpreter, duration=1):
    self.duration = duration
  def execute(self):
    try:
      d = self.duration.execute()
    except AttributeError:
      d = self.duration
    time.sleep(d)
