if __name__ == '__main__':
    print("This is program is being run by itself")
else:
    print("i am being imported from another module")

from mymodule import sayhi,version

sayhi()
print("Verison",version)
