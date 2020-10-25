#Say "Hello, World!" With Python
Greetings= 'Hello, World!'
print(Greetings)

#Python If-Else

# !/bin/python3
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    #n in range(1, 101)
    if n % 2 == 1 or n % 2 == 0 and n in range(6, 21):
        print('Weird')
    elif n % 2 == 0 and (n in range(2, 6) or n > 20):
        print('Not Weird')

#Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    if 1<=a<=10**10 and 1<=b<=10**10:
        print(a+b)
        print(a-b)
        print(a*b)

#Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    intDivision = int(a/b)
    floatDivision = float (a/b)
    print(intDivision)
    print(floatDivision)


#Loops
if __name__ == '__main__':
    n = int(input())
    if n in range(1,21):
        for i in (range(0,n)):
            print(i*i)


#Write a function
def is_leap(year):
    leap = False
    # Write your logic here
    if year % 4 == 0:
        leap = True
        if year%100==0:
            leap = False
            if year % 400 == 0:
                leap=True
    return leap


#Print Function
if __name__ == '__main__':
    n = int(input())


def PrintFunction(n):
    l = []
    if n in range(1, 151):
        while n > 0:
            i = n
            l.append(i)
            n = n - 1
    l.sort()
    return l


for y in PrintFunction(n):
    print(y, end="")



#List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    permutations = [[i, j, k] for i in range(0, x + 1) for j in range(0, y + 1) for k in range(0, z + 1) if
                    i + j + k != n]
    # not <> in py3/// nb: use [] for operation part of List Comp. to have the right output!
    print(permutations)

#Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    score=list(set(arr)) #elimina doppioni
    score.sort() #ordina elementi cresc
    runner_up=score[-2] #penultimo elemento
    if n in range(2,11):
        print(runner_up)


#Nested Lists
if __name__ == '__main__':
    people = []
    scores=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores.append(score)
        scores.sort()


        for num in scores:  #....
            if scores.count(num)>1:
                scores.remove(num)

        people.append([name,score])
        people.sort()

    second_score=scores[1]
    for i in people:
        if i[1]==second_score:
            print(i[0])


#Finding the percentage
import statistics

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    mediael= statistics.mean(student_marks[query_name])

    print(format(mediael, '.2f'))


#Lists
if __name__ == '__main__':
    N = int(input())
    c = []
    for el in range(0,N):
        righe = input().split()

        if righe[0] == 'insert':
            c.insert(int(righe[1]), int(righe[2]))
        elif righe[0] == 'remove':
            c.remove(int(righe[1]))
        elif righe[0] == 'append':
            c.append(int(righe[1]))
        elif righe[0] == 'sort':
            c=sorted(c)
        elif righe[0] == 'pop':
            c.pop()
        elif righe[0] == 'reverse':
            c.reverse()
        elif righe[0] == 'print':
            print(c)


#Tuples
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))



#sWAP cASE
def swap_case(s):
    swap= ""

    for l in s:
        if l==l.upper():
            swap = swap + l.lower()
        else:
            swap = swap + l.upper()
    return swap

#String Split and Join
def split_and_join(line):
    newline=line.split(" ") #slpit sullo spazio
    joinline="-".join(newline)
    return joinline



#What's Your Name?
def print_full_name(a, b):
    fn=a
    ln=b
    print("Hello "+ fn + " " + ln + "! You just delved into python.")

#Mutations
def mutate_string(string, position, character):
    newstring = list(string)
    newstring[position]= character
    newstring2= ''.join(newstring)
    return newstring2


#Find a string
def count_substring(string, sub_string):
    c1=0
    lenss=len(sub_string)

    if 1 <= len(string) <= 200:  #constraints
        if sub_string in string:
            i=string.find(sub_string) #indice posizione elemento con cui inizia la substring nella string
            rimanente=string[i:] #inizio a contare da qui quante volte c'è la substring

            while len(rimanente)>0:
                i = rimanente.find(sub_string)
                if i==0 and (rimanente[0:lenss]==sub_string[0:]):
                    c1+=1
                    rimanente=rimanente[1:]
                elif i>0 and (rimanente[i:lenss]==sub_string[0:]):
                    c1+=1
                    rimanente=rimanente[i:]
                else:
                    rimanente = rimanente[1:]

    return c1

#String Validators
if __name__ == '__main__':
    s = input()
    #metodo any() per vedere se uno dei valori corrisponde a quanto cerchiamo, altrimenti isXXX() mi dice se tutti lo sono. Restituisce true di default
    num   = any(el.isalnum() for el in s)
    alpha = any(el.isalpha() for el in s)
    digit = any(el.isdigit() for el in s)
    lower = any(el.islower() for el in s)
    upper = any(el.isupper() for el in s)

    print(num)
    print(alpha)
    print(digit)
    print(lower)
    print(upper)


#Text Alignement
thickness = int(input()) #This must be an odd number

c = 'H'
if 0 < thickness < 50 and thickness % 2 == 1:  #condizioni di lunghezza e num dispari
    #Top Cone
    for i in range(thickness):
        print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

    #Top Pillars
    for i in range(thickness+1):
        print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

    #Middle Belt
    for i in range((thickness+1)//2):
        print((c*thickness*5).center(thickness*6))

    #Bottom Pillars
    for i in range(thickness+1):
        print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

    #Bottom Cone
    for i in range(thickness):
        print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

#Text Wrap
def wrap(string, max_width):
    if 0<len(string)<100 and 0<max_width<len(string):
        wrapped=textwrap.wrap(string,max_width)
        return "\n".join(wrapped)

#Designer Door Mat

N,M= map(int,(input().split()))


if 5< N < 101 and N % 2 ==1 and (M == 3*N):
    middleM = int((M-3)/2)
    middleN = int((N-3)/2)
    mN= int((N-1)/2)
    mM = int ((M-1)/2)
    mat_center = "WELCOME"
    p1 = "-"
    p2 = ".|."

    for i in range(mN):
        print( (p2+2*p2*i).center(M, p1))
    print(mat_center.center(M, p1))

    for i in range(mN-1,-1,-1): #all'inverso
        print((p2+2*p2*i).center(M, p1))

#String Formatting

def print_formatted(number):
    if number in range(0, 100):
        # Ogni valore deve essere riempito di spazio per corrispondere alla larghezza del valore binario di n ---> try print(f'{s:>5}')
        w4 = len(bin(number)[2:])
        for i in range(1, number + 1):
            # decimale
            dec = str(i)
            # ottale
            octal = str(oct(i)[2:])
            # esadecimale
            hexa = str((hex(i)[2:]).upper())
            # binario
            binary = str((bin(i)[2:]))

            print((dec.rjust(w4) + " " + octal.rjust(w4) + " " + hexa.rjust(w4) + " " + binary.rjust(w4)))




#Alphabet Rangoli
def print_rangoli(size):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for i in range(size - 1, 0, -1):  # 0 è per togliere la riga doppia di base
        metalph = str(alphabet[i:size])
        k1 = ("-".join(metalph))  # .ljust(size, "-")
        p1 = ("-".join(metalph[::-1])[
              :-1])  # .rjust(size, "-") metalph[::-1])[:-1]  #reverse della stringa e tolgo lettera già presente
        r = p1 + k1
        print((r).center(4 * size - 3, "-"))  # 3*size-3 è il pattern ricorrente

    for i in range(size):
        metalph = str(alphabet[i:size])
        k1 = ("-".join(metalph))  # .ljust(size, "-")
        p1 = ("-".join(metalph[::-1])[
              :-1])  # .rjust(size, "-") metalph[::-1])[:-1]  #reverse della stringa e tolgo lettera già presente
        r = p1 + k1
        print((r).center(4 * size - 3, "-"))  # 3*size-3 è il pattern ricorrente

#Capitalize!
# Complete the solve function below.
def solve(s):
    lista1 = s.split(" ")
    r = ""
    for el in lista1:
        p = el.capitalize()

        r += p + " "
    return r


#The Minion Game
def minion_game(string):
    if 0<len(string)<=10**6: #constraint
        check = 'AEIOU'

        K = 0
        S = 0
        for i in range(len(string)):
            if s[i] in check:
                K += (len(string)-i)
            else:
                S += (len(string)-i)

        if K > S:
            print ("Kevin", K)
        elif K < S:
            print ("Stuart", S)
        else:
            print ("Draw")

#Merge the Tools!
def merge_the_tools(string, k):
    n = len(string)
    f = k / n

    if 1 <= n <= 10 ** 4 and 1 <= k <= n:
        for t in range(0, n, k):
            new_s = string[t:t + k]  # stringa di k elementi
            g = ""
            for l in new_s:
                if l not in g:
                    g += l
            print(g)




#Introduction to Sets
def average(array):
    a = set(array)
    b = sum(a)
    c = len(a)
    return (b / c)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)


#Symmetric Difference
# Enter your code here. Read input from STDIN. Print output to STDOUT
m=list(map(int,input().split()))
l1=list(map(int,input().split()))
n=list(map(int,input().split()))
l2=list(map(int,input().split()))

a=set(l1)
b=set(l2)
c=a.difference(b)
d=b.difference(a)
e=list(c.union(d))
f=sorted(e)
for i in f:
    print(i)


#No Idea!
n, m = map(int,input().split())
arr= input().split()
A=set(input().split())
B=set(input().split())

if 1<=n<=10**5 and 1<=m<=10**5:#constraints
    c=0
    c1=0
    c2=0
    for i in arr:
        if i in A :
            c1+=1
        if i in B:
            c2+=1
    print(c1-c2)


#Set .add()
n = input()
country = set()
for i in range(int(n)):
    a=input()
    country.add(a)
print(len(country))

#Set .discard(), .remove() & .pop()
n = input()
s = set(map(int, input().split()))
M=int(input())

for el in range(M):
    cmd = input().split()
    if cmd[0] == "discard":
        s.discard(int(cmd[1]))
    elif cmd[0] == "remove":
        s.remove(int(cmd[1]))
    elif cmd[0] == "pop":
        s.pop()

c=0
for i in s:
    c=c+i
print(c)

#Set .union() Operation
n = int(input())
s1= set(map(int,input().split()))
M=int(input())
s2= set(map(int,input().split()))
inter=s1.union(s2)

print(len(inter))


#Set .intersection() Operation
n = int(input())
s1= set(map(int,input().split()))
M=int(input())
s2= set(map(int,input().split()))
inter=s1.intersection(s2)

print(len(inter))



#Set .difference() Operation
n = int(input())
s1= set(map(int,input().split()))
M=int(input())
s2= set(map(int,input().split()))
inter=s1.difference(s2)

print(len(inter))


#Set .symmetric_difference() Operation
n = int(input())
s1= set(map(int,input().split()))
M=int(input())
s2= set(map(int,input().split()))
inter=s1.symmetric_difference(s2)

print(len(inter))

#Set Mutations
n = int(input())
s= set(map(int,input().split()))
M=int(input())

for el in range(M):
    cmd = list(input().split())
    s1= set(map(int,input().split()))

    if cmd[0] == 'intersection_update':
        s.intersection_update(s1)
    elif cmd[0] == 'update':
        s.update(s1)
    elif cmd[0] == 'symmetric_difference_update':
        s.symmetric_difference_update(s1)
    elif cmd[0] == 'difference_update':
        s.difference_update(s1)

print(sum(s))

#The Captain's Room
n = int(input())
s1= (map(int,input().split()))
s3=set()
s4=set()

for i in s1:
    if i in s4:
        s3.add(i)
    else:
        s4.add(i)
s2=list(s4.difference(s3))
print(s2[0])

#Check Subset
n= int(input())


for el in range(n):
    if 0<n<21 : #constraints
        n1,s1 = int(input()),set(input().split()) #input lunghezza e set
        n2,s2 = int(input()),set(input().split()) #input lunghezza e set
        if 0 < len(list(s1)) < 1001 and 0< len(list(s2))<1001: #constraints
            diff=s1.intersection(s2) #per vedere elementi comuni e poi se sono uguali al set-->quindi è subset
            if diff==s1:
                print("True")
            else:
                print("False")

#Check Strict Superset
s=set(input().split())
n= int(input())
a = ""
for el in range(n):
    s2 = set(input().split())  # set
    if 0<n<21 and 0 < len(list(s)) <  501 and 0< len(list(s2))<101: #constraints
        unione=s.union(s2) #se superset l'unione deve dare lui
        if s == s2 or unione !=s:
            print("False")
            exit()
        else:
            a="True"
print(a)




#collections.Counter()
from collections import Counter

ns=int(input())
sizes=Counter(map(int,input().split()))
nc=int(input())
tot=0

for el in range(nc):
    shoe,prezzo=map(int,input().split())
    if sizes[shoe]>0:
        tot+=prezzo
        sizes[shoe]-=1


#DefaultDict Tutorial
from collections import defaultdict

n,m=list(map(int,input().split()))
dic=defaultdict(list)
l=[]


for el in range(1,n+1):
    w_n=input()
    dic[w_n].append(el)

words_m = []

for el2 in range(m):
    w_m=input()
    words_m.append(w_m)

stdout_list = []

for word in words_m:
    if word in dic:
        stdout_list.append(" ".join(map(str, dic[word])))
    else:
        stdout_list.append("-1")

for line in stdout_list:
    print(line)


#Collections.namedtuple()
from collections import namedtuple

n_students = int(input())
columns = input().split()
student = namedtuple('Student', columns)
sum = 0

for i in range(n_students):
    columns_i = input().split()
    student_i = student(*columns_i)
    sum += int(student_i.MARKS)

print('{:.2f}'.format(sum/n_students))



#Collections.OrderedDict()
from collections import OrderedDict

items_length = int(input())
dict = OrderedDict()

for i in range(items_length):

    item = input().split()
    name = " ".join(item[0:-1])
    prezzo = int(item[-1])
    dict[name] = dict.get(name, 0) + prezzo

for name, price in dict.items():
    print(name, price)

#Word Order
from collections import Counter

n = int(input())
words = []

for i in range(n):
    word = input()
    words.append(word)

ordered_words = Counter(words)
print(str(len(ordered_words.keys())))
values = list(ordered_words.values())
print(' '.join(str(x) for x in values))


#Collections.deque()
from collections import deque

d = deque()
number = int(input())

for i in range(number):
    stdin = input().split()
    method = str(stdin[0])

    if len(stdin) > 1:
        value = int(stdin[1])
    if method == 'append':
        d.append(value)
    elif method == 'appendleft':
        d.appendleft(value)
    elif method == 'pop':
        d.pop()
    elif method == 'popleft':
        d.popleft()
    elif method == 'clear':
        d.clear()
    elif method == 'extend':
        d.extend(value)
    elif method == 'extendleft':
        d.extendleft(value)
    elif method == 'count':
        d.count(value)

print(" ".join([str(x) for x in d]))

#Company Logo
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    s = input()
    c = Counter(s)
    ordered = sorted(c.items(), key = lambda x:(-x[1], x[0]))[:3]
    for key, value in ordered:
        print(key, value)

#Piling Up!
from collections import deque

number = int(input())
for i in range(number):
    n_cubes = int(input())
    d = deque(map(int, input().split()))
    pile = []

    for n in range(n_cubes):
        if len(pile) == 0:
            if len(d) == 1:
                print("Yes")
                break
            if d[0] > d[-1]:
                pile.append(d.popleft())
            else:
                pile.append(d.pop())
        else:
            if len(d) == 1 and d[0] <= pile[-1]:
                print("Yes")
                break

            if d[0] >= d[-1] and d[0] <= pile[-1]:
                pile.append(d.popleft())

            elif d[-1] >= d[0] and d[-1] <= pile[-1]:
                pile.append(d.pop())

            else:
                print("No")
                break


#Calendar Module
import calendar
m,d,y = map(int,input().split())
c=calendar.weekday(y, m, d) #documentation--> per avere giorno
week_days={0: "MONDAY", 1: "TURSDAY", 2:"WEDNESDAY",3:"THURSDAY",4:"FRIDAY",5:"SATURDAY",6:"SUNDAY"}
print(week_days[c])

#Time Delta
#!/bin/python3

import math
import os
import random
import re
import sys

from datetime import datetime
# Complete the time_delta function below.

def time_delta(t1, t2):
    t3=datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z') #string to datetime object + formato
    t4=datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z') #string to datetime object + formato
    diff = (abs(t3-t4)).total_seconds() #to have secs
    return str(int(diff)) #intero + stringa (unsupport altrimenti)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()

#Exceptions
n=int(input())

for num in range(n):
    try:
        n,m = map(int,input().split())
        print(n//m)
    except ZeroDivisionError as e:
        print ("Error Code:",e)
    except ValueError as e2:
        print ("Error Code:",e2)


#Zipped!
n,x=(map(int,input().split()))  #n students and x subjects

l=[]
for i in range(x):
    scores=(map(float,input().split()))
    l.append(scores)
zipped=list(zip(*l))

for score in zipped:
    s=sum(score)
    #print(s)
    average=s/x
    print(average)


#Athlete Sort

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
#####sopra obbligatorio di Hackerrank

    sortlist=sorted(arr, key=lambda x: x[k]) #vedi doc per lambda, sort by parametro k

    #print(arr)
    #print(sortlist)
    for athlete in sortlist:
        print(*athlete) #star operator, come es zip



#ginortS
s=str(input())
lower=[]
upper=[]
odd=[] #dispari
even=[]
for i in s:
    if i.isupper()==True:
        upper.append(i)

    elif i.islower()==True:
        lower.append(i)
    elif int(i)%2==1:
        odd.append(i)
    elif int(i)%2==0:
        even.append(i)
stdout_list=[]
stdout_list.append("".join(sorted(lower)+sorted(upper)+sorted(odd)+sorted(even)))
for l in stdout_list:
    print(l)



#Map and Lambda Function
cube = lambda x: x**3 # complete the lambda function

def fibonacci(n):
    # return a list of fibonacci numbers
    fiblist=[]
    for i in range(n):
        if i == 0:
            fiblist.append(0)
        if i == 1:
            fiblist.append(1)
        if i > 1:
            fiblist.append(fiblist[i - 1] + fiblist[i - 2])
    return fiblist



#Detect Floating Point Number
import re

t=int(input())

for num in range(t):
    number=input()
    print(bool(re.search(r"^[+-]?\d*\.\d+$", number)))  #^ inizio, []

#Re.split()
regex_pattern = r"[.,]"	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))



#Group(), Groups() & Groupdict()
import re

s=input()
regex_pattern = r".*?([a-zA-Z0-9])\1" #carattere alfanumerico-->\1 the first group
n=re.match(regex_pattern, s)
if n:
    print(n.group(1))  # The first parenthesized subgroup.
else:
    print(-1)



#Re.findall() & Re.finditer()
import re

vocali='AEIOUaeiou'
consonanti='QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm '

s=input()
#due o più vocali in mezzo a due consonanti. devono contenere solo vocali
regex_pattern = r'(?<=[' + consonanti + '])([' + vocali + ']{2,})[' + consonanti + ']'
n=re.findall(regex_pattern, s)

if n:
    print(*n, sep='\n')  #star operator e stampa a capo
else:
    print(-1)

#Re.start() & Re.end()
import re


#Your task is to find the indices of the start and end of string k in s .
s=input()
k=input()
regex_pattern = r'(?=('+k+'))'
r1=re.finditer(regex_pattern,s)
r2=re.search(regex_pattern,s)
if r2:
    for m in r1:
        print((m.start(1), m.end(1)-1))
else:
    print((-1,-1))


#Regex Substitution
import re

n=int(input())
regex_pattern1=r"(?<= )(&&)(?= )"
regex_pattern2=r"(?<= )(\|\|)(?= )"

for i in range (n):
    testo= str(input())
    if testo in ' && ' or ' || ':
         r1=(re.sub(regex_pattern1,'and',testo))
         r2=(re.sub(regex_pattern2,'or',r1))
         print(r2)


#Validating Roman Numerals
regex_pattern = r"^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"    # Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))

#Validating phone numbers
import re
n=int(input())

for num in range(n):
    s=input()
    regex_pattern = r"^[789]\d{9}$"
    b = bool(re.match(regex_pattern, str(s)))
    if b==True:
        print('YES')
    else:
        print('NO')

#Validating and Parsing Email Addresses
import email.utils
import re
n = int(input())

for em in range(n):
    indmail=input()
    email_address = email.utils.parseaddr(indmail)
    regex_pattern = r"^[a-zA-Z][a-zA-Z0-9-_.]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$"
    b=re.match(regex_pattern, email_address[1])
    to_print=email.utils.formataddr(email_address)
    if b:
        print(to_print)

#Hex Color Code
import re

n=int(input())

for col in range(n):
    l=input()
    regex_pattern=r"(?<=.)#[0-9A-Fa-f]{3}\b|#[0-9A-Fa-f]{6}\b"
    f=re.findall(regex_pattern,l)
    for i in f:
        print(i)


#HTML Parser - Part 1
from html.parser import HTMLParser

n=int(input())

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print ("Start :", tag)
        for a in attrs:
            print("->", a[0], ">", a[1])
    def handle_endtag(self, tag):
        print ("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print ("Empty :", tag)
        for a in attrs:
            print("->", a[0], ">", a[1])


parser = MyHTMLParser()
for l in range(n):
    tag = input().rstrip()
    parser.feed(str(tag))

#HTML Parser - Part 2
from html.parser import HTMLParser

n=int(input())

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if '\n' not in data: #ver a capo
            print('>>> Single-line Comment')
            print(data)
        else:
            print('>>> Multi-line Comment')
            print(data)

    def handle_data(self, data):
        if '\n' not in data: # Do not print data if data == '\n'.
            print(">>> Data")
            print(data)

parser = MyHTMLParser()
cod = ''
for i in range(n):
    cod += input().rstrip() +'\n'
parser.feed(cod)

#Detect HTML Tags, Attributes and Attribute Values

from html.parser import HTMLParser

n=int(input())
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for a in attrs:
            print("->", a[0], ">", a[1])


parser = MyHTMLParser()
for l in range(n):
    tag = input().rstrip()
    parser.feed(str(tag))


#Validating UID
import re

n=input()

for num in range(int(n)):
    s=input().strip()
    regex_pattern = r"^(?!.*(.).*\1)(?=(?:.*[A-Z]){2,})(?=(?:.*[0-9]){3,})[a-zA-Z0-9]{10}$"  #(?!.*(.).*\1) no rep.
    b=re.match(regex_pattern, s)
    if b:
        print('Valid')
    else:
        print('Invalid')

#Validating Credit Card Numbers
import re

n=input()
regex_pattern1 = r"^[456][0-9]{15}$"
regex_pattern2 = r"(^[456][0-9]{3}-)([0-9]{4}-){2}([0-9]{4})$"
nofour=r"(?!.*([0-9])\1{3})"

for num in range(int(n)):
    s=input().strip()
    b=re.match(regex_pattern1, s)
    c=re.match(regex_pattern2, s)

    if c:
        s1 = s.replace("-", "")
        d = re.match(nofour, s1)
        if d:
            print("Valid")
        else:
            print("Invalid")
    else:
        if b:
            print('Valid')
        else:
            print("Invalid")




#Validating Postal Codes
regex_integer_in_range = r"^[1-9][0-9]{5}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(?=([0-9])[0-9]\1)"	# Do not delete 'r'.

import re
P = input()

print (bool(re.match(regex_integer_in_range, P))
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)




#Matrix Script

#!/bin/python3

import math
import os
import random
import re
import sys



first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []

for i in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
#print(matrix)
###########################
to_print = ''
for i in range(m):
    for j in range(n):
        to_print = to_print + matrix[j][i]
#print(to_print)

regex_pattern=r"(?<=([a-zA-Z0-9]))[\s$#%&]+(?=[a-zA-Z0-9])"
f=re.sub(regex_pattern," ",to_print)
print(f)


#XML 1 - Find the Score
import sys
import xml.etree.ElementTree as etree


def get_attr_number(node):
    # your code goes here
    count = 0
    for el in node.iter():  #iterator for the given object
        count+=len(el.attrib)  #pydoc
    return count


if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))


#XML2 - Find the Maximum Depth
import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    # your code goes here-->vedi dfs(?)
    if maxdepth==level:
        maxdepth+=1
    elif level >= maxdepth:
        maxdepth = level
    for el in elem:
        depth(el, level+1) #test ricorsione
    return maxdepth


if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)

#Standardize Mobile Number Using Decorators
def wrapper(f):
    def fun(l):
        # complete the function
        p1 = "0"
        p2 = "9"
        p3 = "1"

        to_print = []
        for el in l:
            el2 = list(el)
            if len(el) == 11:
                if el2[0] == p1:
                    to_print.append("+91 " + el[1:6] + " " + el[6:11])
            elif len(el) == 12:
                if el2[0] == p2 and el2[1] == p3:
                    to_print.append("+91 " + el[2:7] + " " + el[7:12])
            elif len(el) == 10:
                if el[0] == p2:
                    to_print.append("+91 " + el[0:5] + " " + el[5:10])
                else:
                    to_print.append("+91 " + el[0:5] + " " + el[5:10])
            elif len(el)==13:
                to_print.append(el[0:3]+ " " +el[3:8] + " " + el[8:13])

        d = sorted(to_print)
        for n in d:
            print(n)

    @wrapper
    def sort_phone(l):
        print(*sorted(l), sep='\n')

    if __name__ == '__main__':
        l = [input() for _ in range(int(input()))]
        sort_phone(l)


#Decorators 2 - Name Directory
def person_lister(f):
    def inner(people):
        # complete the function
        #to_print=[]
        sorted_by_third = sorted(people, key=lambda l: int(l[2]))
        return (f(person) for person in sorted_by_third)

    return inner
@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')



#Arrays
import numpy
def arrays(arr):
    new_a=list(reversed(arr))
    return numpy.array(new_a,float)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

#Shape and Reshape
import numpy


arr = list(map(int,input().split()))
new_a=numpy.array((arr))
shape_a=numpy.reshape(new_a,(3,3))
print(shape_a)

#Transpose and Flatten
import numpy

n,m=input().split() # n rows m colonne
l=[]

for el in range(int(n)):
    arr = list(map(int, input().split()))
    l.append(arr)
new_a = numpy.array((l))
#print(new_a)
print(new_a.transpose())
print(new_a.flatten())


#Concatenate
import numpy

n,m,p=input().split()
l = []
ll = []
for el in range(int(n)):

    arr = list(map(int, input().split()))
    l.append(arr)

new_a = numpy.array((l))
#print(new_a)
for el in range(int(m)):

    arr = list(map(int, input().split()))
    ll.append(arr)

new_b = numpy.array((ll))
#print(new_b)
print(numpy.concatenate((new_a,new_b),axis=0))

#Zeros and Ones
import numpy

inp=list(map(int, input().split(" ")))

print (numpy.zeros((inp),dtype = numpy.int))
print (numpy.ones((inp),dtype = numpy.int))


#Eye and Identity
import numpy

n,m=list(map(int, input().split(" ")))
numpy.set_printoptions(sign=' ')
print ((numpy.eye(n,m, k = 0)))

#Array Mathematics
import numpy
n,m=input().split(" ")

l = []
ll = []
for el in range(int(n)):
    arr = list(map(int, input().split()))
    l.append(arr)

int_a = numpy.array((l))

for el in range(int(n)):
    arr = list(map(int, input().split()))
    ll.append(arr)

int_b = numpy.array((ll))


    #add
print (numpy.add(int_a, int_b))
    #sub
print(numpy.subtract(int_a, int_b))
    #mul
print(numpy.multiply(int_a, int_b))
    #div
print(numpy.floor_divide(int_a, int_b))
    #mod
print(numpy.mod(int_a, int_b))
    #pow
print(numpy.power(int_a, int_b))

#Floor, Ceil and Rint
import numpy

inp=input().split(" ")
new_arr=numpy.array(inp,float)
numpy.set_printoptions(sign=' ')

print(numpy.floor(new_arr))
print(numpy.ceil(new_arr))
print(numpy.rint(new_arr))

#Sum and Prod
import numpy
n,m=input().split(" ")

l = []

for el in range(int(n)):
    arr = list(map(int, input().split()))
    l.append(arr)

a = numpy.array((l))
#print the product of that sum.
print( numpy.prod(numpy.sum(a, axis = 0)))


#Min and Max
import numpy
n,m=input().split(" ")
l = []

for el in range(int(n)):
    arr = list(map(int, input().split()))
    l.append(arr)

a = numpy.array((l))
print( numpy.max(numpy.min(a, axis = 1)))  #max of min

#Mean, Var, and Std
import numpy
n,m=input().split(" ")
l = []

for el in range(int(n)):
    arr = list(map(int, input().split()))
    l.append(arr)
a = numpy.array((l))

numpy.set_printoptions(sign=' ', legacy='1.13') #opz stampa

print( numpy.mean(a, axis = 1))#mean
print( (numpy.var(a, axis = 0).round(decimals=12)))#var
print( numpy.std(a, axis = None))#std

#Dot and Cross
import numpy
n=input()

l = []
ll = []
for el in range(int(n)):
    arr = list(map(int, input().split()))
    l.append(arr)

int_a = numpy.array((l))

for el in range(int(n)):
    arr = list(map(int, input().split()))
    ll.append(arr)

int_b = numpy.array((ll))


print(numpy.dot(int_a,int_b)) #matrix prod

#Inner and Outer
import numpy


arr_a = numpy.array(input().split(),int)
arr_b = numpy.array(input().split(),int)

print(numpy.inner(arr_a,arr_b))
print(numpy.outer(arr_a,arr_b))


#Polynomials
import  numpy

arr_a = numpy.array(input().split(),float)
x=int(input())

print(numpy.polyval(arr_a,x))

#Linear Algebra
import numpy
n=input()

l = []
for el in range(int(n)):
    arr = list(map(float, input().split()))
    l.append(arr)
arr_a = numpy.array((l))

numpy.set_printoptions(legacy='1.13')
print (numpy.linalg.det(arr_a))




#Birthday Cake Candles
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here
    max_c = max(candles)
    count = 0
    for c in candles:
        if c == max_c:
            count += 1
    return(count)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()


#Number Line Jumps
# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    res = ""
    if x1 > x2 and v1 > v2:  # never
        res = ("NO")
    if x1 < x2 and v1 == v2:  # never
        res = ("NO")
    elif x1 < x2 and v1 < v2:  # never
        res = ("NO")
    elif x1 == x2:  # same pos
        res = ("YES")
    elif x1 > x2 and v1 < v2:
        while x1 > x2:
            x1 += v1
            x2 += v2
        if x1 == x2:  # same pos
            res = ("YES")
        else:
            res = ("NO")
    elif x1 < x2 and v1 > v2:
        while x1 < x2:
            x1 += v1
            x2 += v2
        if x1 == x2:  # same pos
            res = ("YES")
        else:
            res = ("NO")

    return res
    ##############


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()


#Viral Advertising

#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    cum = 0
    shared = 5
    for i in range(n):

        like = int(shared // 2)
        cum += like
        shared=like*3
    return(cum)

########
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()

#Recursive Digit Sum
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superDigit function below.
def superDigit(n, k):
    if int(n) < 10:
        return n
    sum = 0
    for i in n:
        sum += int(i)
    tot = sum * k
    return superDigit(str(tot),1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()


#Insertion Sort - Part 1
# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the insertionSort1 function below.


def insertionSort1(n, arr):
    i = n - 1
    val = arr[i]
    # j = i - 1
    while (i > 0 and val < arr[i - 1]):
        arr[i] = arr[i - 1]
        print(*arr)
        i -= 1
    arr[i] = val
    print(*arr)


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

#Insertion Sort - Part 2
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort2 function below.
def insertionSort2(n, arr):
    #definizione classica

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:

            arr[j + 1] = arr[j]
            j -= 1
            arr[j + 1] = key
        print(*arr)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)


