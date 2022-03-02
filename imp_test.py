# import my_module.func1
# from my_module.func1 import add
from my_module.func2 import sq_diff


# def test1():
#     res = add(1, 2)
#     print(res)


def test2():
    print(sq_diff(3, 2))


def main():
    test2()


if __name__ == '__main__':
    main()
