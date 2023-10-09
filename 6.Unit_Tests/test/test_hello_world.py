from hello_world import hello

def main():
    test_default()
    test_arg()

def test_default():
    assert hello()=="Hello, world"

def test_arg():
    assert hello("Gyan")=="Hello, Gyan"

if __name__=="__main__":
    main()