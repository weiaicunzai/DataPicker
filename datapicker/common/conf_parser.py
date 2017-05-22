
import json

class ConfParser(object):

    def __init__(self, *args ,**kwargs):
        super(ConfParser, self).__init__(*args, **kwargs)

    def parser_conf(self):
        with open('../config.conf', 'r') as conf:
            for cur in conf:
                if cur.startswith('#'):
                    continue

                cur_list = cur.strip().split('=')
                if len(cur_list) > 1:
                    attr_dict = {}
                    for k,v in json.loads(cur_list[1]).items():
                        #print k,json.loads(v, encoding='utf-8')
                        try:
                            attr_dict[k] = json.loads(v, encoding='utf-8')
                        except ValueError:
                            attr_dict[k] = v
                    setattr(self, cur_list[0].strip(), attr_dict)

