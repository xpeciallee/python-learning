import time

from config.config import TEMPLATE_PATH
from utils.yaml_utils import YamlUtil
import os
import threading


def test_01(*, a: str, b: int, **kwargs):
    # 默认参数，可变参数， 关键字参数， 命令关键字参数
    print(a)
    print(b)
    print(kwargs)


if __name__ == '__main__':
    # data = YamlUtil.load(os.path.join(TEMPLATE_PATH, 'login.yaml'))

    # print(data)
    test_01(b=2, a='hello', c=2, d=6)
    # 推导式
    num_list = [1, 3, 4, 5, 6, 6, 7, 8]
    new_list = [i for i in num_list if i % 2 == 0]
    print(new_list)
