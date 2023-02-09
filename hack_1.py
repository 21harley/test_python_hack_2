"""
generic script

text: "fooziman" output => "fOozIman" 
text: "qux" output => "qUx" 
text: "eq" output => "eq" 
"""


def fn_hack_1(result:str):
    new_cadena=''
    array_c=['i','o','u']
    for i in range(0,len(result)):
        ban=0
        try:
            if array_c.index(result[i])!=-1:
                ban=1
                array_c.remove(result[i])
        except:
            None
        new_cadena+=(result[i].upper() if ban==1 else result[i])
    return new_cadena
