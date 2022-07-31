import yaml


class YamlUtil:

    @staticmethod
    def load(file_name):
        with open(file_name, encoding='utf-8') as f:
            data = yaml.load(f.read(), Loader=yaml.FullLoader)
        return data
