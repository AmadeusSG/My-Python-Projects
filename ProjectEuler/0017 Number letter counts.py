# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then
# there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
# how many letters would be used?
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
# contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of
# "and" when writing out numbers is in compliance with British usage.
#
# Answer: 21124

def numberinletters(number):
    n = list(str(number))[::-1]
    word = list(str(number))[::-1]

    for i in range(len(n)):
        word[i] = ''
        if len(n)==1:
            if n[i] == '0': word[i] += 'zero'
        if (i!=1 or (i !=1 and len(n)>1 and n[1]!='1')):
            if n[i]=='1': word[i]= 'one'
            elif n[i]=='2': word[i]= 'two'
            elif n[i]=='3': word[i]= 'three'
            elif n[i]=='4': word[i]= 'four'
            elif n[i]=='5': word[i]= 'five'
            elif n[i]=='6': word[i]= 'six'
            elif n[i]=='7': word[i]= 'seven'
            elif n[i]=='8': word[i]= 'eight'
            elif n[i]=='9': word[i]= 'nine'
        elif (i==1 and n[i]!='1'):
            if n[i] == '2': word[i] = 'twenty'
            elif n[i] == '3': word[i] = 'thirty'
            elif n[i] == '4': word[i] = 'forty'
            elif n[i] == '5': word[i] = 'fifty'
            elif n[i] == '6': word[i] = 'sixty'
            elif n[i] == '7': word[i] = 'seventy'
            elif n[i] == '8': word[i] = 'eighty'
            elif n[i] == '9': word[i] = 'ninety'
        elif (i==1 and n[i]=='1'):
            word[i-1]=''
            if n[0] == '0': word[i] = 'ten'
            elif n[0] == '1': word[i] = 'eleven'
            elif n[0] == '2': word[i] = 'twelve'
            elif n[0] == '3': word[i] = 'thirteen'
            elif n[0] == '4': word[i] = 'fourteen'
            elif n[0] == '5': word[i] = 'fifteen'
            elif n[0] == '6': word[i] = 'sixteen'
            elif n[0] == '7': word[i] = 'seventeen'
            elif n[0] == '8': word[i] = 'eighteen'
            elif n[0] == '9': word[i] = 'nineteen'

        if (i==2):
            if (n[i]!='0'): word[i]+=' hundred'
            if (n[0]!='0' or n[1]!='0'): word[i]+=' and'
        if (i==3):
            word[i]+=' thousand'
    for j in range(len(word)-1,-1,-1):
        if word[j]=='': del word[j]

    return ' '.join(word[::-1])

def count_letters(word):
    return len(word) - word.count(' ')

def count(lownumber,highnumber):
    total=0
    for i in range(lownumber,highnumber+1):
        total+=count_letters(numberinletters(i))
    return total

print(count(1,1000))

'''
Alist=[]
for j in range(100):
    for i in range(1+j*10,10+j*10):
        Alist.append(numberinletters(i))
    print(Alist)
    Alist=[]
'''