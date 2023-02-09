"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""


def fn_hack_4(result):
    result=result.lower()
    return result[1:len(result)-1] if len(result)>3 else result