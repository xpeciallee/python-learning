import os


# 获取当前文件的绝对路径
# path1 = os.path.abspath(__file__)

# 获取当前文件的目录
# path2 = os.path.dirname(__file__)

# 获取当前文件的文件夹路径
# path3 = os.path.dirname(path1)


ROOT_PATH = os.path.dirname(os.path.abspath("__file__"))
TEMPLATE_PATH = os.path.join(ROOT_PATH, 'template')

print(ROOT_PATH)
