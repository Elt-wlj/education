# 配置文件的读取
import yaml

from config.path import config_yaml_path


def read_yaml(fpath):
    with open(fpath, encoding='utf-8') as f:
        data = yaml.safe_load(f)
        return data


yaml_config = read_yaml(config_yaml_path)
