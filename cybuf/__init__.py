from .marshal import _marshal

def dumps(obj, tab_count, with_indent=False):
    return _marshal(obj, tab_count, with_indent)

if __name__ == "__main__":
    print("test mode, __init__.py")