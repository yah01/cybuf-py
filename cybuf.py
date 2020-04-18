defaultEncoding = "utf-8"
MarshalSep = b" "

def dumps(obj, tabCount, withIndent=False):
    marshal(obj, tabCount, withIndent=False)


def marshal(obj, tabCount, withIndent=False):
    cybufBytes = b"{"
    if withIndent:
        cybufBytes += b"\n"
    tabs = b""
    if withIndent:
        tabs = b"\t" * tabCount
        
    if type(obj) == dict:
        for (k, v) in obj.items():
            cybufBytes += tabs
            cybufBytes += bytes(str(k),defaultEncoding)
            cybufBytes += b":"
            if withIndent:
                cybufBytes += b" "
                
            valueBytes = b""
            if type(v) == int:
                valueBytes = bytes(str(v),defaultEncoding)
            elif type(v) == float:
                valueBytes = bytes(str(v),defaultEncoding)
            elif type(v) == None:
                valueBytes += b"nil"
            elif type(v) == bool:
                valueBytes += bytes(str(v), defaultEncoding)
            elif type(v) == str:
                valueBytes += b"\"" + bytes(v,defaultEncoding) + b"\""
            cybufBytes += valueBytes
            if withIndent:
                cybufBytes += b"\n"
            else:
                if(type(v)!=str):
                    cybufBytes += MarshalSep
        cybufBytes += tabs[1:]
        cybufBytes += b"}"
    return cybufBytes

if __name__ == "__main__":
    print(marshal({"hello":1,"this":2,"key":"this"},1,True).decode(defaultEncoding))
    print(marshal({"hello":1,"this":2,"key":"this"},1).decode(defaultEncoding))