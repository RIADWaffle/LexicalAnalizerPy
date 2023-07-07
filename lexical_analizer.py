import string
from os import remove

#flush the files
try:
  remove("data.txt")
  remove("tokens.txt")
  remove("errors.txt")
except:
  print("files not created already")

#create the data txt
txt = """1234
1.234
$yono.
$hola
/
=
==
|
||
&
&&
!
!=
+
-
*
/
{
  [1234]
}
(1234)
[]
"""

#create the data.txt with the code
with open("data.txt", 'a') as archivo:
  archivo.write(txt + '\n')

#read the txt file with the data
name = "data.txt"
with open(name, "r") as archivo:
    array = archivo.read().splitlines()


#adding lists to make easy the transitions
lowercase = list(string.ascii_lowercase)
uppercase = list(string.ascii_uppercase)
numbers = ['0','1','2','3','4','5','6','7','8','9']


#//////////////////////////////////////////////////
#////////////////AUTOMATA STARTS///////////////////
#//////////////////////////////////////////////////
#making the automata to follow the steps.
automata = {
    #first state of the automata
    'initialState': '0',

    #all final states on the automata
    'finalState': ['enter','tab','space','2', '3', '5', '7', '8', '11', '12', '13', '14', '15', '16',
                   '17', '19', '20', '21', '22', '24', '26', '27', '28', '29', '30', '31', '32', '33',
                   '34'],

    #all the movements/transitions the automata can do, also has the type of the token at every point
    'transitions': [
        {
            'state': '0',
            'symbol': ['$'],
            'nextState': '1',
            'type': 'id'
        },
        {
            'state': '0',
            'symbol': numbers,
            'nextState': '3',
            'type': 'num'
        },
        {
            'state': '0',
            'symbol': ["'"],
            'nextState': '6',
            'type': 'string'
        },
        {
            'state': '0',
            'symbol': ['/'],
            'nextState': '8',
            'type': 'arithmetic'
        },
        {
            'state': '0',
            'symbol': ["="],
            'nextState': '12',
            'type': 'asignation'
        },
        {
            'state': '0',
            'symbol': ['>'],
            'nextState': '14',
            'type': 'relacional'
        },
        {
            'state': '0',
            'symbol': ["<"],
            'nextState': '16',
            'type': 'relacional'
        },
        {
            'state': '0',
            'symbol': ['!'],
            'nextState': '18',
            'type': 'logic'
        },
        {
            'state': '0',
            'symbol': ["+"],
            'nextState': '20',
            'type': 'arithmetic'
        },
        {
            'state': '0',
            'symbol': ['-'],
            'nextState': '21',
            'type': 'arithmetic'
        },
        {
            'state': '0',
            'symbol': ["*"],
            'nextState': '22',
            'type': 'arithmetic'
        },
        {
            'state': '0',
            'symbol': ['|'],
            'nextState': '23',
            'type': 'logic'
        },
        {
            'state': '0',
            'symbol': ['&'],
            'nextState': '25',
            'type': 'logic'
        },
        {
            'state': '0',
            'symbol': ['{'],
            'nextState': '27',
            'type': 'delimiter'
        },
        {
            'state': '0',
            'symbol': ['}'],
            'nextState': '27',
            'type': 'delimiter'
        },
        {
            'state': '0',
            'symbol': ['('],
            'nextState': '29',
            'type': 'delimiter'
        },
        {
            'state': '0',
            'symbol': [')'],
            'nextState': '30',
            'type': 'delimiter'
        },
        {
            'state': '0',
            'symbol': ['['],
            'nextState': '31',
            'type': 'delimiter'
        },
        {
            'state': '0',
            'symbol': [']'],
            'nextState': '32',
            'type': 'delimiter'
        },
        {
            'state': '0',
            'symbol': [':'],
            'nextState': '34',
            'type': 'delimiter'
        },
        {
            'state': '0',
            'symbol': [';'],
            'nextState': '33',
            'type': 'delimiter'
        },
        {
            'state': '0',
            'symbol': [' '],
            'nextState': 'space',
            'type': 'Indentation'
        },
        {
            'state': '0',
            'symbol': ['\t'],
            'nextState': 'tab',
            'type': 'Indentation'
        },
        {
            'state': '0',
            'symbol': ['\n'],
            'nextState': 'enter',
            'type': 'Indentation'
        },
        {
            'state': '1',
            'symbol': numbers,
            'nextState': '2',
            'type': 'id'
        },
        {
            'state': '1',
            'symbol': lowercase,
            'nextState': '2',
            'type': 'id'
        },
        {
            'state': '1',
            'symbol': uppercase,
            'nextState': '2',
            'type': 'id'
        },
        {
            'state': '3',
            'symbol': numbers,
            'nextState': '3',
            'type': 'num'
        },
        {
            'state': '2',
            'symbol': numbers,
            'nextState': '2',
            'type': 'id'
        },
        {
            'state': '2',
            'symbol': lowercase,
            'nextState': '2',
            'type': 'id'
        },
        {
            'state': '2',
            'symbol': uppercase,
            'nextState': '2',
            'type': 'id'
        },
        {
            'state': '3',
            'symbol': ['.'],
            'nextState': '4',
            'type': 'decimal'
        },
        {
            'state': '4',
            'symbol': numbers,
            'nextState': '5',
            'type': 'decimal'
        },
        {
            'state': '5',
            'symbol': numbers,
            'nextState': '5',
            'type': 'decimal'
        },
        {
            'state': '6',
            'symbol': numbers,
            'nextState': '6',
            'type': 'string'
        },
        {
            'state': '6',
            'symbol': lowercase,
            'nextState': '6',
            'type': 'string'
        },
        {
            'state': '6',
            'symbol': uppercase,
            'nextState': '6',
            'type': 'string'
        },
        {
            'state': '6',
            'symbol': ["'"],
            'nextState': '7',
            'type': 'string'
        },
        {
            'state': '8',
            'symbol': ['*'],
            'nextState': '9',
            'type': 'comment'
        },
        {
            'state': '9',
            'symbol': numbers,
            'nextState': '9',
            'type': 'comment'
        },
        {
            'state': '9',
            'symbol': lowercase,
            'nextState': '9',
            'type': 'comment'
        },
        {
            'state': '9',
            'symbol': [' '],
            'nextState': '9',
            'type': 'comment'
        },
        {
            'state': '9',
            'symbol': uppercase,
            'nextState': '9',
            'type': 'comment'
        },
        {
            'state': '9',
            'symbol': ['*'],
            'nextState': '10',
            'type': 'comment'
        },
        {
            'state': '10',
            'symbol': ['/'],
            'nextState': '11',
            'type': 'comment'
        },
        {
            'state': '12',
            'symbol': ['='],
            'nextState': '13',
            'type': 'relational'
        },
        {
            'state': '14',
            'symbol': ['='],
            'nextState': '15',
            'type': 'relational'
        },
        {
            'state': '16',
            'symbol': ['='],
            'nextState': '17',
            'type': 'relational'
        },
        {
            'state': '18',
            'symbol': ['='],
            'nextState': '19',
            'type': 'relational'
        },
        {
            'state': '23',
            'symbol': ['|'],
            'nextState': '24',
            'type': 'logic'
        },
        {
            'state': '25',
            'symbol': ['&'],
            'nextState': '26',
            'type': 'logic'
        }
      ],
    }

#Define the tokens table
tTable = {
          '2' : '200 ID',
          '3' : '201 Natural num',
          '5' : '202 Decimal num',
          '7' : '100 String',
          '8' : '23 Division',
          '11' : '101 Commentary',
          '12' : '10 Asignation',
          '13' : '11 Relational ==',
          '14' : '12 Relational >',
          '15' : '13 Relational >=',
          '16' : '14 Relational <',
          '17' : '15 Relational <=',
          '19' : '16 Relational !=',
          '20' : '20 Arithmetic +',
          '21' : '21 Arithmetic -',
          '22' : '22 Arithmetic *',
          '24' : '40 Logical ||',
          '26' : '41 Logical &&',
          '27' : '34 Delimiter {',
          '28' : '35 Delimiter }',
          '29' : '30 Delimiter (',
          '30' : '31 Delimiter )',
          '31' : '32 Delimiter [',
          '32' : '33 Delimiter ]',
          '33' : '50 Delimiter :',
          '34' : '51 Delimiter ;',
          'space':'identation',
          'tab':'identation',
          'enter':'identation'
         }

#//////////////////////////////////////////////////
#/////////////////AUTOMATA ENDS////////////////////
#//////////////////////////////////////////////////




# ---------- Function were magic happens -----------------------
def validateWords(array):
  scReaded = array
  currentState = automata['initialState']
  lastState = automata['initialState']
  word = ""
  pastTransition = False
  transition = False
  lastType = ""
  currentType = ""

  counter = 0



  #read the .txt file in separated Chars
  for ch in array:
    counter = 0
    #Checking for transitions
    for t in automata['transitions']:
      counter += 1
      if(ch in t['symbol'] and currentState == t['state']):
        transition, pastTransition = True, transition
        lastState = currentState
        lastType = currentType
        currentType = t['type']
        currentState = t['nextState']
        word += ch
        break

      #is a valid word
      if(counter == len(automata['transitions'])):
        transition = False
        if(currentState in automata['finalState']):
          if(word in [' ','\n']):
            for l in word:
              scReaded.remove(l)
            return scReaded
          with open('tokens.txt','a') as code:
            code.write(word + ' - ' + tTable[currentState] + '\n')
          code.close()
          for l in word:
            scReaded.remove(l)
          return scReaded

        # Is an error
        else:
          word += ch
          if currentType == '':
            with open('errors.txt','a') as code:
              code.write(word + ' - syntaxis error'  + '\n')
            code.close()
            for l in word:
              scReaded.remove(l)
          else:
            with open('errors.txt','a') as code:
              code.write(word + ' - ' + currentType + ' error' '\n')
            code.close()
            for l in word:
              scReaded.remove(l)
          return scReaded


    if((not transition) and (pastTransition) and (currentState in automata['finalState'])):
      with open('tokens.txt','a') as code:
        code.write(word + ' - ' + tTable[currentState] + '\n')
      code.close()
      for l in word:
            scReaded.remove(l)
      currentState = automata['initialState']
      lastState = automata['initialState']
      word = ""
      pastTransition = False
      transition = False
  if(word != ""):
    with open('tokens.txt','a') as code:
      code.write(word + ' - ' + tTable[currentState] + '\n')
    code.close()
    for l in word:
            scReaded.remove(l)
    print('Function ends')
    return scReaded



#//////////////////////////////////////////
print("Generating tokens/errors files...")
#creating the tokens list
with open('tokens.txt','w') as tokens:
  tokens.write('                tokens list\n--------------------------------------------\n')
tokens.close()

#opening the data file
file = open("data.txt","r")
contenido = file.read()
sc = list(contenido)
file.close()

#creating the errors list
with open('errors.txt','w') as code:
  code.write("                errors list\n--------------------------------------------\n")
code.close()

#using the function to validate
print("Validating tokens in the data.txt")
repeat = validateWords(sc)

while(len(repeat) > 0):
  repeat = validateWords(sc)

print("Files generated!")
