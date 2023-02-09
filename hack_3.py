"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""


def fn_hack_3(result):
    result=result.lower()
    transTable = result.maketrans("aeiou","@3¡0v", "")
    result = result.translate(transTable)
    if result[0].isnumeric():
       result=result[0:len(result)-1]+result[len(result)-1:len(result)].upper()
    else:
        if len(result)>2:    
            result=result[0].capitalize()+result[1:len(result)-1]+result[len(result)-1:len(result)].upper()
        else:
            result=result[0].capitalize()+result[1:len(result)]
    return result
