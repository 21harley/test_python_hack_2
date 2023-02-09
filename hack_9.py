"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(result):
    new_dict={}
    aux_dict=result.copy()
    for k in aux_dict.keys():
        if k=='foo':
            new_dict.setdefault('foo'.capitalize(),aux_dict[k].capitalize().replace('k', ''))
    return new_dict
