python -m venv env

cd venv_name\Scripts
# 进入虚拟环境
activate
# 退出当前虚拟环境
deactivate
# 安装第三方包(必须进入虚拟环境)
pip install xxx

pip freeze > requestments.txt