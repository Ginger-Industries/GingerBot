from .instructions import *
import sys

codepage = "abcdefghijklmnopqrstuvwxyzABCDE FGHIGKLMNOPQRSTUVWXYZ+-*/%^?:<>=&!|\"\'()0123456789[]⁰¹²³⁴⁵⁶⁷⁸⁹ĿĽ⭳@#$_\,;{}`~⌬⌕↶↷⊕ⅎƒḟ∈∋¿⋔⍭≤≥≠≬∆∇≐∓⌿∿≀≖⧤⧣∸⋒\n\0\0\0\0\0\0\0\0↹ĥôõöøóòπε\0\0\0\0\0\0Ⓠ⒬Ⓐ⒜ⓛⓁ①⑴⑩⑽⑨⑼Ⓔ↑↓\0⒈⒉⒊⒋⒌⒍⒎⒏⒐⒑⒒⒓⒔⒕⒖"

conversionTable = {
  "p": PrintInstruction,
  "i": InputInstruction,
  "⧤": FloatInputInstruction,
  "⧣": IntInputInstruction,

  "+": AdditionInstruction,
  "-": SubtractionInstruction,
  "*": MultiplicationInstruction,
  "x": MultiplicationInstruction,
  "/": DivisionInstruction,
  "^": ExponentInstruction,
  "%": ModuloInstruction,
  "∸": FloorDivisionInstruction,

  "v": MemoryWriteInstruction,
  "@": DynamicReadInstruction,

  "I": CastToNumberInstruction,
  "t": CastToStringInstruction,
  "L": CastToListInstruction,
  "Ŀ": CastToIntListInstruction,
  "⌬": ReverseInstruction,
  "~": SortInstruction,
  "l": StringLengthInstruction,
  "⌕": StringFindInstruction,
  "c": StringContainsInstruction,
  "C": CountInstruction,
  "s": StringSplitInstruction,
  "j": StringJoinInstruction,
  "V": SubstringInstruction,
  "R": StringReplaceInstruction,
  "↑": StringUppercaseInstruction,
  "↓": StringLowercaseInstruction,

  "↶": Char2CodepointInstruction,
  "↷": Codepoint2CharInstruction,
  "b": Num2BinaryInstruction,
  "B": Binary2NumInstruction,

  "A": ExecuteAsAPOLInstruction,
  #"y": ExecuteAsPythonInstruction,

  "a": ListAppendInstruction,
  "⊕": ListSumInstruction,
  "g": ListGetInstruction,
  "S": ListSetInstruction,
  "P": ListPopInstruction,
  "r": ListRemoveInstruction,
  "⭳": ListFlattenInstruction,
  "u": UnduplicateListInstruction,

  "w": WhileLoopInstruction,
  "W": PrecheckWhileLoopInstruction,
  "f": ForLoopInstruction,
  "ⅎ": OneForLoopInstruction,
  "ƒ": ListBuilderForLoopInstruction,
  "ḟ": StartEndForLoopInstruction, 
  "∈": LoopCounterInstruction,
  "∋": LoopItemInstruction,
  "⋒": ForIteratorInstruction,
  "?": IfInstruction,
  "¿": ReturningIfInstruction,
  "⋔": IfItemInstruction,
  ":": FunctionInstruction,
  "⍭": DelayInstruction,

  "<": LessThanComparison,
  ">": GreaterThanComparison,
  "≤": LessThanOrEqualToComparison,
  "≥": GreaterThanOrEqualToComparison,
  "=": EqualComparison,
  "≠": UnequalComparison,
  "≬": BetweenInstruction,

  "!": NotInstruction,
  "&": AndInstruction,
  "|": OrInstruction,

  "∆": IncreaseInstruction,
  "∇": DecreaseInstruction,
  #"±": SetSignInstruction,
  "≐": GetEvenInstruction,
  "∓": GetSignInstruction,
  "⌿": AbsoluteValueInstruction,
  "∿": RandomNumberInstruction,
  "≀": RandomFloatInstruction,
  "≖": RoundInstruction,
}

altNames = {
  "print": "p",
  "floatinput": "⧤",
  "intinput": "⧣",
  "input": "i",
  "listflatten": "⭳",
  "add": "+",
  "subtract": "-",
  "multiply": "*",
  "divide": "/",
  "exponent": "^",
  "modulo": "%",
  "floordiv": "∸",
  "dynamicread": "@",
  "write": "v",
  "castnumber": "I",
  "caststring": "t",
  "castlist": "L",
  "castfloatlist": "Ľ",
  "castintlist": "Ŀ",
  "tobinary": "b",
  "frombinary": "B",
  "reverse": "⌬",
  "length": "l",
  "substring": "V",
  "stringfind": "⌕",
  "stringcontains": "c",
  "stringsplit": "s",
  "stringjoin": "j",
  "stringreplace": "R",
  "uppercase": "↑",
  "lowercase": "↓",
  "tocodepoint": "↶",
  "tochar": "↷",
  "precheckwhile": "W",
  "while": "w",
  "apolexec": "A",
  "foriterator": "⋒",
  "loopcounter": "∈",
  "count": "C",
  "loopitem": "∋",
  "ifitem": "⋔",
  "onefor": "ⅎ",
  "startendfor": "ḟ",
  "listfor": "ƒ",
  "for": "f",
  "delay": "⍭",
  "lessthan": "<",
  "greaterthan": ">",
  "lessorequal": "≤",
  "greaterorequal": "≥",
  "unequal": "≠",
  "equal": "=",
  "between": "≬",
  "increase": "∆",
  "decrease": "∇",
  "geteven": "≐",
  "getsign": "∓",
  "abs": "⌿",
  "append": "a",
  "sum": "⊕",
  "listget": "g",
  "listset": "S",
  "listpop": "P",
  "listremove": "r",  
  "returnif": "¿",
  "if": "?",
  "function": ":",
  "randnum": "∿",
  "randfloat": "≀",
  "roundnum": "≖",
  "logicand": "&",
  "logicor": "|",
  "logicnot": "!"
}

class Interpreter():
  @classmethod
  def compile(self, program):
    out = b""
    for c in program:
      if c in codepage:
        out += (codepage.find(c).to_bytes(1, "big"))
    return out
  def decompile(self, bytecode):
    out = ""
    for byte in bytecode:
      out += codepage[byte]
    return out
  @classmethod
  def prepare(self, program):
    program = program.replace("\n", ";")
    for altName in altNames:
      program = program.replace(altName, altNames[altName])
    return program.split(";")
  def __init__(self):
    self.memory = {}
    self.lastError = None
    self._forLoopCounter = None
    self._forLoopItem = None
    self._forLoopIterator = None
    self._ifItem = None
  
  def interpret(self, program):
    instructions = []
    def parseInstruction(instruction):
      if instruction[0] in CONSTANTS:
        return ConstantInstruction(CONSTANTS[instruction[0]])
      if instruction[0] in "⁰¹²³⁴⁵⁶⁷⁸⁹":
        try:
            return MemoryReadInstruction(self, int("".join([str("⁰¹²³⁴⁵⁶⁷⁸⁹".find(c)) for c in instruction])))
        except ValueError:
          raise ValueError("Error processing cell id: " + arg + " Make sure you're not using superscript numbers to refer to cells, or that you mistyped an instruction.") from None
      try:
        t = conversionTable[instruction[0]]
      except KeyError:
        raise SyntaxError("Invalid instruction: " + instruction[0])
      argStr = instruction[1:].split("(", 1)[-1]
      if not len(argStr):
        try:
          return t(self)
        except TypeError as e:
          raise TypeError(str(e) + " in instruction " + instruction) from None
      args = []
      i = ""
      l = []
      ignore = 0
      inString = ""
      inList = False
      class String():
        def __init__(self, r):
          self.r = r
        
      for c, char in enumerate(argStr):
        if (char == '"' or char == "'") and argStr[c-1] != "\\" and ignore == 0:
          if char == inString:
            inString = ""
            continue
          elif not inString:
            inString = char
            continue
        if char == "(" and argStr[c-1] != "\\":
          ignore += 1
        elif char == ")" and argStr[c-1] != "\\":
          ignore -= 1
        if ((char == " " and ignore == 0) or (c == len(argStr)-1)) and (not inString):
          if argStr[c-1] == "'" or argStr[c-1] == '"' or argStr[c-len(i)] == "\\":
            if inList:
              if i.lstrip() != "":
                l.append(i.lstrip())
            else:
              args.append(String(i[1:]) if argStr[c-len(i)] == "\\" else String(i))
          else:
            if inList:
              try:
                l.append(int(i.lstrip()))
              except ValueError:
                try:
                  l.append(float(i.lstrip()))
                except ValueError:
                  if i.lstrip() != "":
                    l.append(i.lstrip())
            else:
              args.append(i.lstrip())
          i = ""
          continue
        if char == "[" and argStr[c-1] != "\\":
          inList = True
          continue
        elif char == "]" and argStr[c-1] != "\\":
          inList = False
          if argStr[c-1] == "'" or argStr[c-1] == '"':
            l.append(i.lstrip())
          else:
            try:
              l.append(int(i.lstrip()))
            except ValueError:
              try:
                l.append(float(i.lstrip()))
              except ValueError:
                if i.lstrip() != "":
                  l.append(i.lstrip())
          args.append(l)
          l = []
          i = ""
          continue
        if not (char == "\\" and argStr[c+1] in ["(", ")", "'", '"']):
          i += char
      args = [c for c in args if c != ""]
      if inList:
        raise SyntaxError("Unclosed list")
      if ignore > 0:
        raise SyntaxError("Unclosed parenthesis")
      if inString:
        raise SyntaxError("Unclosed string")
      parsedArgs = []
      for arg in [i for i in args if i != '']:
        if type(arg) == list:
          parsedArgs.append(arg)
        elif type(arg) == String:
          parsedArgs.append(arg.r.replace("\\n", "\n"))
        elif arg[0] in CONSTANTS:
          parsedArgs.append(ConstantInstruction(CONSTANTS[arg[0]]))
        elif all([c in "-1234567890." for c in arg]):
          try:
            parsedArgs.append(int(arg))
          except ValueError:
            parsedArgs.append(float(arg))
        elif arg[0] in conversionTable:
          parsedArgs.append(parseInstruction(arg))
        elif any(c in "⁰¹²³⁴⁵⁶⁷⁸⁹" for c in arg):
          try:
            parsedArgs.append(MemoryReadInstruction(self, int("".join([str("⁰¹²³⁴⁵⁶⁷⁸⁹".find(c)) for c in arg]))))
          except ValueError:
            raise ValueError("Error processing cell id: " + arg + " Make sure you're not using superscript numbers to refer to cells, or that you mistyped an instruction.") from None
        else:
          #It's a command I guess
          parsedArgs.append(arg)
      try:
        return t(self, *parsedArgs)
      except TypeError as e:
        raise TypeError(str(e) + " in instruction " + instruction) from None
    for instruction in program:
      instructions.append(parseInstruction(instruction))
    return instructions
  
  def run(self, program, implicitPrint = True):
    _ = None
    try:
      instructions = self.interpret(self.prepare(program))
      for instruction in instructions:
        _ = instruction.execute()
    except:
      self.lastError = sys.exc_info()
      raise
    if implicitPrint and _ != None:
      print(_)
    return _
  def restart(self):
    self.memory = {}