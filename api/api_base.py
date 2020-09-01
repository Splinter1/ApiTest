import requests


class BaseApi():
    def api_post(self,url, handers, body):
        api = requests.post(url, headers=handers , json=body)
        return api


if __name__ == '__main__':
    request = BaseApi().api_post("http://hn216.api.yesapi.cn/?&s=App.Config.AddConfig", {"Content-Type":"application/json"}, {"app_key": "6A3D030D071263AEDC8F8E115C30CA3E","config_name": "testa2pg","config_value": "3"})
    print(request.json())