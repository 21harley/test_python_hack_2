"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(result):
    new_list=[]
    aux=len(result)
    if aux%2!=0:
        cont=0
        aux_list=result[::-1]
        while(aux>=0):
            if cont>=len(aux_list): break
            new_list.append(str(aux_list[cont])+'-'+str(aux))
            aux-=1
            cont+=1
    else:
        while(aux>0):
            new_list.append(str(aux))
            aux-=1
    return new_list
