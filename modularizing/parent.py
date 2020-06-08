local_val = "magical unicorns"
def square(x):
    return x*x

class User:
    def __init__(self, name):
        self.name = name
    def sayhello(self):
        return "Hello " + self.name

# dom = User("Dominic")
# print(dom.sayhello())

# print(__name__)

if __name__ == "__main__":
    print("the file being executed directly")
else:
    print("File is being executed because it's being imported. This file is called", __name__)