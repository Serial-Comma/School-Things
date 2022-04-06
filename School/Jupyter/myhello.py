def hello_once(name):
    print('Hello {}'.format(name))

def hello_many(items):
    for item in items:
        hello_once(item)
