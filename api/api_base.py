import requests


class BaseRequest():
    # def api_post(self,url, handers, body):
    #     request = requests.post(url, headers=handers , json=body)
    #     return request
    #
    # def api_get(self, url, handers):
    #     request = requests.get()
    def base_request(self, methon, url, headers, body):
        request = requests.request(method=methon, url=url, headers=headers, json=body)
        print(request.json())
        return request


if __name__ == '__main__':
    request = BaseRequest().base_request("post","http://hn216.api.yesapi.cn/?&s=App.Config.AddConfig", {"Content-Type":"application/json"}, {"app_key": "6A3D030D071263AEDC8F8E115C30CA3E","config_name": "testa2pg","config_value": "3"})
    print(request.json())