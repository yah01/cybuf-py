import cybuf

testdata = {
    "hello": 1,
    "this": 2.0,
    "is": False,
    "a": "a",
    "test": None
    }

print(cybuf.dumps(testdata, 1))
print(cybuf.dumps(testdata, 1, with_indent=True))
