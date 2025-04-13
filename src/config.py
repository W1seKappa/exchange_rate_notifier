import toml

class Config:
    def __init__(self, path_to_config, config_name):
        self.path_to_config = path_to_config
        self.config_name = config_name
        with open(self.path_to_config + self.config_name, 'r') as conf_file:
            self.config = toml.load(conf_file)

    def get_param(self, key, value):
        return self.config[key][value]


