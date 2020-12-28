# from utils.config_utils import local_config
#
# print(local_config.HOSTS)
import configparser
cfg=configparser.ConfigParser()
cfg.read('D:\\API_TEST_Framework\\conf\\localconfig.ini')
host=cfg.get('default','hosts')
print(host)

