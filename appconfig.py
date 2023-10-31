import yaml


class Config:
    def __init__(self):
        with open("app_cred", "r") as f:
            self.values_yaml = yaml.load(f, Loader=yaml.FullLoader)

    def service(self):
        return self.values_yaml['service']
