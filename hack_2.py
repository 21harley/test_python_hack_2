"""
generic script

text: "fooziman" output => "fzmn" 
text: "barziman" output => "brzmn" 
text: "qux" output => "qx" 
"""


def fn_hack_2(result):
    result=result.lower()
    transTable = result.maketrans("","", "aeiou")
    return result.translate(transTable)

print(fn_hack_2("fooziman"))