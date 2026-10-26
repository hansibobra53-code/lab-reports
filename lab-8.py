

#lab:8

#project:1
s = input()

v = c = d = sp = o = 0

for x in s:
    if x in "aeiouAEIOU":
        v += 1
    elif x.isalpha():
        c += 1
    elif x.isdigit():
        d += 1
    elif x == " ":
        sp += 1
    else:
        o += 1

print("Vowels:", v)
print("Consonants:", c)
print("Digits:", d)
print("Spaces:", sp)
print("Others:", o)


#project:2
s = input()
a = ""

for i in range(len(s)):
    if i % 2 == 0:
        a += s[i].upper()
    else:
        a += s[i].lower()

print(a)



#project:3
s = input()

u = l = d = sp = 0

for x in s:
    if x.isupper():
        u = 1
    elif x.islower():
        l = 1
    elif x.isdigit():
        d = 1
    elif x != " ":
        sp = 1

n = u + l + d + sp

if len(s) < 8:
    print("WEAK")
elif n == 4:
    print("STRONG")
elif n >= 2:
    print("MODERATE")
else:
    print("WEAK")


#project:4
s = input()
ch = input()

count = 0

for i in range(len(s)):
    if s[i] == ch:
        print(i, end=" ")
        count += 1

if count == 0:
    print(-1)

print()
print("Count:", count)


#project:5
s = input()

for x in s.split():
    print(len(x), end=" ")



#project:6
s = input()

if len(s) == 10 and s[:2] == "RJ" and s[2:4].isdigit() and s[4:6].isalpha() and s[4:6].isupper() and s[6:].isdigit():
    print(True)
else:
    print(False)


#project:7
s = input()
count = 0

for i in range(len(s) // 2):
    if s[i] != s[-i-1]:
        count += 1

print("Changes needed:", count)



#project:8
s = input()
a = ""

for x in s:
    if x not in a:
        a += x

print(a)



#project:9
s = input()
k = int(input())

abc = "abcdefghijklmnopqrstuvwxyz"
a = ""

for x in s:
    if x == " ":
        a += " "
    else:
        i = abc.index(x)
        a += abc[(i + k) % 26]

print(a)



#project:10
s = input()

count = 1
max_count = 1
ch = s[0]

for i in range(1, len(s)):
    if s[i] == s[i-1]:
        count = count + 1
    else:
        count = 1

    if count > max_count:
        max_count = count
        ch = s[i]

print(ch, max_count)