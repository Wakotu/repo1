'''
Author: Axiuxiu
Date: 2021-12-29 21:41:18
LastEditors: Please set LastEditors
LastEditTime: 2022-03-02 19:53:31
Description: 

'''
from functools import wraps


def get_parameters(*args, **kwargs):
    print(args)
    print(kwargs)


def outter(tips):
    def middle(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(tips)
            return func(*args, **kwargs)
        return wrapper
    return middle


@outter('decorated')
def func(num):
    print('the original func', num)


def main():
    # get_parameters(1, 2, 3, a='a', b='b')
    func(2)
    print(func.__name__)


if __name__ == '__main__':
    # 主函数
    main()
