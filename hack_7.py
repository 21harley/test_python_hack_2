"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [] output => [0] 
"""


def fn_hack_7(result):
    new_list=[]
    if len(result)>1:
        for i in range(0,len(result)):
            if i%2==0:
                new_list.append(str(i+1))
            else:
                new_list.append(i+1)
    else:
        new_list.append(int('0'))
    return new_list

