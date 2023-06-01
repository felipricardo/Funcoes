

def minhafuncao(*args):
    print(type(args))
    for item in args:
        print(item)
minhafuncao("texto")
minhafuncao(123)
minhafuncao(True)
minhafuncao(True,123,"texto")
