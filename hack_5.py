"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""


def fn_hack_5(result):
    new_cadena=''
    letras='aeiou'
    ban=0
    cont1=0
    if len(result)>3:
        cont=0
        for i in range(0,len(result)):
            cont+=1
            if cont!=3:
                new_cadena+=result[i]
            else:
                if ban==0:    
                   new_cadena+='-'
                else:
                   new_cadena+=('-'+result[i])
                cont=0
                if letras.find(result[i])>=0 and cont1==0:
                    ban=1
                    cont1=1
        if ban==1:
            new_cadena=new_cadena[:len(new_cadena)-1]+'-'
    elif len(result)==3:
        new_cadena=result[:len(result)-1]+'-'
    else:
        new_cadena=result
    return new_cadena
