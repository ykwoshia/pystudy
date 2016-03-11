#!/usr/bin/python
#  from random import randint
#  from random import choice
import random




#  ## part1
#  name = "Crossin"
#  myVar = 123
#  price = 5.99
#  visible = True

#  print name
#  print myVar
#  print price
#  print visible

#  pprint 2 < 5

#  ##  part 2

#  num = randint(1,100)
#  print "guess"
#  answer = input()
#  while answer != num :
    #  if answer < num :
        #  print '%d is too small' % answer
        #  answer = input()
    #  if answer > num :
        #  print '%d is too big' %answer
        #  answer = input()
#  print 'equal'

## part3 sum
#  a = 1
 #  sum = 0
  #  while a <= 100 :
 #  sum += a
    #  a += 1 

#  print sum
#  sum = 0
#  for a in range(1, 101):
    #  sum += a

#  print sum


## part 4 function
#  #  def sayhello(a):
    #  #  print "hello %s" % a
#  #  def plus(a,b):
    #  #  print a+b
#  #  sayhello("Moto");
#  #  plus(3,2)

#  def isEqual(num1, num2):
    #  if num1<num2:
        #  print 'too small'
        #  return False
    #  elif num1>num2:
        #  print 'too big'
        #  return False
    #  else:
        #  print 'bingo'
        #  return True

#  num = randint(1, 10000)
#  print 'Guess what I think?'
#  bingo = False
#  while bingo == False:
   #  answer = input()
   #  bingo = isEqual(answer, num)


### part5 list 

#  l = [1,2,3,4,5,6,7]
#  l.append(8)
#  print l
#  del l[0]
#  print l

#  l = [365, 'everyday', 0.618, True]
#  m = l[1:3]
#  print m

#  print 'chose one side to shoot:'
#  print 'left, center, right'
#  you = raw_input()
#  print 'You kicked ' + you
#  direction = ['left', 'center', 'right']
#  com = choice(direction)
#  print 'Computer saved ' + com
#  if you != com:
    #  print 'Goal!'
#  else:
    #  print 'Oops...'



#  score = [0, 0]
#  direction = ['left', 'center', 'right']

#  def kick():
   #  print '==== You Kick! ===='
   #  print 'Choose one side to shoot:'
   #  print 'left, center, right'
   #  you = raw_input()
   #  print 'You kicked ' + you
   #  com = choice(direction)
   #  print 'Computer saved ' + com
   #  if you != com:
       #  print 'Goal!'
       #  score[0] += 1
   #  else:
       #  print 'Oops...'
   #  print 'Score: %d(you) - %d(com)\n' % (score[0], score[1])

   #  print '==== You Save! ===='
   #  print 'Choose one side to save:'
   #  print 'left, center, right'
   #  you = raw_input()
   #  print 'You saved ' + you
   #  com = choice(direction)
   #  print 'Computer kicked ' + com
   #  if you == com:
       #  print 'Saved!'
   #  else:
       #  print 'Oops...'
       #  score[1] += 1
   #  print 'Score: %d(you) - %d(com)\n' % (score[0], score[1])

#  for i in range(1):
   #  print '==== Round %d ====' % (i+1)
   #  kick()

#  while(score[0] == score[1]):
   #  i += 1
   #  print '==== Round %d ====' % (i+1)
   #  kick()

#  if score[0] > score[1]:
   #  print 'You Win!'
#  else:
   #  print 'You Lose.'


#  a = 'hello world how are you '
#  b = a.split()
#  print b
#  s = '-'

#  c = '~'.join(b)
#  print c
#  for d in c:
    #  print d

#  print c[0]
#  print  c[4:]

#  IFH = file("p60.txt")
#  data = IFH.read()
#  IFH.close()

#  data = input()
#  OFH = file("p60_bak.txt", "w")
#  OFH.write(data)
#  OFH.close

#  i = 0
#  while i < 5:
    #  i += 1
    #  for j in range(3):
        #  print "j=",j
        #  if j == 2:
            #  break
    #  for k in range(3):
        #  if k == 2:
            #  continue
        #  print "k=",k
    #  if i > 3:
        #  break
    #  print "i=",i

#  score = {'b':2,'a':1,'c':3}
#  for key in score:
    #  print score[key]
#  try:
    #  f = file('nonexist.txt')
    #  print 'File opened!'
    #  f.close
#  except:
    #  print 'File not exist.'
#  print 'Done'
#  d = {1:'a',2:'b',4:'c'}
#  print d[1]
#  print d[2]
#  print d[4]
#  dir(random)
from math import pi
print pi
