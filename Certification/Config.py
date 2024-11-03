import yaml

class Config:
    def __init__(self, config_yaml="testdata.yaml"):
        with open(config_yaml, 'r') as input:
            data = yaml.safe_load(input)
        self.host = data['address']
        self.password = data['password']
        self.username = data['username']
        self.browser = data['browser']
        self.sleep_time = data['sleep_time']
        self.wait = data['wait']
        self.unknown = data['unknown']
        self.sometext = data['sometext']
        self.email = data['email']