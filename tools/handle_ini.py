import os
import configparser


class HandleIni():

    def load_ini(self):
        path = os.path.dirname(os.path.dirname(__file__))
        file_path = path + "/data/server.ini"
        cf = configparser.ConfigParser()
        cf.read(file_path, encoding="utf-8-sig")
        return cf

    def read_ini(self, key, section=None):
        if section == None:
            section = 'server'
        cf = self.load_ini()
        try:
            data = cf.get(section, key)
        except Exception:
            print("没有获取到值")
            data = None
        return data


if __name__ == '__main__':
    hi = HandleIni()
    data1 = hi.read_ini("host")
    print(data1)


