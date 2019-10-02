out = {}
import copy 

def checkType(obj):
    if type(obj) == type(dict()):
        return "dict"
    elif type(obj) == type(list()) or type(obj) == type(tuple()):
        return "list"
    else:
        return "other"

def loop_dict(d, ret, key_word):
    for key in d:
        # print("Testing ", key, ": ", d[key], key_word)
        if str(key) == str(key_word):
            return d[key]
        else:
            # if type(d[key]) == type(str()) and "ok: [10.42.0.200]" in d[key]:
                # print("!-"*25)
            new_key = copy.deepcopy(d[key])
            try:
                # if type(new_key) == type(str()) and "ok: [10.42.0.200]" in d[key]:
                    # print("flag 1")
                if type(new_key) == type(str()):
                    new_key = new_key.replace("\n", "")
                    if "=>" in new_key:
                        new_key = new_key.split("=>")[1]
                while "  " in new_key:
                    new_key = new_key.replace("  ", " ")
                # if type(new_key) == type(str()) and "ok: [10.42.0.200]" in d[key]:
                    # print("flag 2", new_key) 
                new_key = eval(new_key)
            except:
                pass
            finally:
                d[key] = new_key
            if checkType(d[key]) == "list":
                ret = ret or loop_list(d[key], ret, key_word)
            elif checkType(d[key]) == "dict":
                ret = ret or loop_dict(d[key], ret, key_word)
    return ret
    
def loop_list(l, ret, key_word):
    for item in l:
        if checkType(item) == "list":
            ret = ret or loop_list(item, ret, key_word)
        elif checkType(item) == "dict":
            ret = ret or loop_dict(item, ret, key_word)
    return ret

def find(obj, key):
    if checkType(obj) == "list":
        return loop_list(obj, None, key)
    elif checkType(obj) == "dict":
        return loop_dict(obj, None, key)
    return "Not of proper type"

print(find(out, 'text'))
print(find(out, 'name'))
