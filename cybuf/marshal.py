# defaultEncoding = "utf-8"
marshal_sep = " "

def _marshal(obj, tab_count, with_indent):
    cybuf_str = "{"
    if with_indent:
        cybuf_str += "\n"
    tabs = ""
    if with_indent:
        tabs = "\t" * tab_count
        
    if type(obj) == dict:
        for (k, v) in obj.items():
            cybuf_str += tabs
            cybuf_str += str(k)
            cybuf_str += ":"
            if with_indent:
                cybuf_str += " "
                
            value_str = ""
            print(type(v))
            if type(v) == int:
                value_str = str(v)
            elif type(v) == float:
                value_str = str(v)
            elif type(v) == None:
                value_str += "nil"
            elif type(v) == bool:
                value_str += str(v)
            elif type(v) == str:
                value_str += "\"" + v + "\""
            cybuf_str += value_str
            if with_indent:
                cybuf_str += "\n"
            else:
                if type(v)!=str:
                    cybuf_str += marshal_sep
        if with_indent:
            cybuf_str += tabs[1:]
        if cybuf_str.endswith(marshal_sep):
            cybuf_str = cybuf_str[: len(cybuf_str) - len(marshal_sep)]
        cybuf_str += "}"
    return cybuf_str

if __name__ == "__main__":
    print("test mode, marshal.py")