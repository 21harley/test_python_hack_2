"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(result):
    #result = [{"a":"b"},{"c","d"},{"e":"f"}]
    new_lis=[]
    cont=0
    for k in range(0,len(result)):
        if k%2==0:
            new_lis.append({str(cont+1):str(cont+2)})
        else:
            new_lis.append({str(cont+1),str(cont+2)})
        cont+=2
    return new_lis

print(fn_hack_10([{"a":"b"},{"c","d"},{"e":"f"}]))