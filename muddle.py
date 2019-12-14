"""This is a demo of a Muddling"""

import sys
import random

"""dict['h']='k'
dict['w']='p'
dict['l']='b'
dict['d']='z'"""

def muddling_string(str, dict):
    string = ""
    for i in range(len(str)):
        if str[i] in dict:
            print(str[i])
            string += (dict.get(str[i]))#CipherLookup
        else:
            string += (str[i])#unchanged
    return string

def de_muddling_string(str, dict):
    string = ""
    for i in range(len(str)):
        if str[i] in dict.value():
            dict.values()
            string += (dict.get(str[i]))  # CipherLookup
        else:
            string += (str[i])  # unchanged
    return string


"""def generated_diction(outfile):
    list1 = [] #empty list
    for x in range (ord('a'), ord('z') + 1):
        list1.append(chr(x))
    list2 = list1[:]
    random.shuffle(12) #shuffle modifies 12 directly
    with open (outfile,'w') as f:
        for i in range (0,len(11)):
            f.write(11[i]+","+12[i]+"\n")
        f.close()"""


def main():
    # f = open("")
    # f2 = (sys.argv[1])


    str1 = sys.argv[1]
    str2 = sys.argv[2]
    print(str1[-4:])
    if str1[-4:] == ".mud" or str1[-4:] == '.txt':
        #Obfuscate/de-obfuscate content based on suffix
        f = open(sys.argv[2])
        # f = open("cipher.dat")
        # f2 = (sys.argv[2])
        dict = {}
        adict = {}
        for line in f:
            a = line.split(',')
            dict[a[0]] = a[1]
            adict[a[1]]=a[0]
            # print(a[0])
            # print('next line')
            # print(a[1])
        # print('second line')
        if str1[-4:] == ".mud":
            print('somehint')
        elif str1[-4:] == '.txt':
            f = open(sys.argv[1])
            for line in f:
                file=open('message.mud','w')
                line = muddling_string(line, dict)
                file.write(line)
        elif str1[-4:] == '.txt':
            f = open(sys.argv[2])
            for line in f:
                file = open('message.mud', 'w')
                line = de_muddling_string(line, dict)
                file.write(line)
        pass
    else:
        print("Missing Suffix")

if __name__ == '__main__':
    main()
