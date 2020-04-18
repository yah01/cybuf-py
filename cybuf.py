defaultEncoding="utf-8"

def dumps(obj):
    marshal(obj)

def marshal(obj):
    cybufBytes = b"{\n"
    cybufBytes += _marshal(obj,1)
    cybufBytes += b"}"
    return cybufBytes

def _marshal(obj, tabCount):
    cybufBytes = b""
    tabsBytes = b"\t" * tabCount
    if (type(obj) == dict):
        for (k, v) in obj.items():
            cybufBytes += tabsBytes
            cybufBytes += bytes(str(k),defaultEncoding)
            cybufBytes += b":" + b" "

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
            cybufBytes += b"\n"
    return cybufBytes

if __name__ == "__main__":
    print(marshal({"hello":1,"this":2,"key":"this"}).decode(defaultEncoding))