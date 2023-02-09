"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(result):
    new_list=[]
    if len(result)>0:
        for i in range(0,len(result)):
            if i%2==0:
                new_list.append(str(i+1))
            else:
                new_list.append('-')
    elif len(result)==0:
        new_list.append('0')
    return new_list