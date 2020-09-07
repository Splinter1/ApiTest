import requests
from tools.handle_ini import HandleIni

class BaseRequest():
    # def api_post(self,url, handers, body):
    #     request = requests.post(url, headers=handers , json=body)
    #     return request
    #
    # def api_get(self, url, handers):
    #     request = requests.get()
    def base_request(self, methon, url, headers, body):
        # 若excel中的地址提供了url，则不拼接默认host
        if "http" in url:
            pass
        else:
            base_url = HandleIni().read_ini("host")
            url = base_url + url
        request = requests.request(method=methon, url=url, headers=headers, json=body)
        # print(request.json())
        return request.json()


if __name__ == '__main__':
    request = BaseRequest().base_request("post","/?&s=App.Config.AddConfig", {"Content-Type":"application/json"}, {"app_key": "6A3D030D071263AEDC8F8E115C30CA3E","config_name": "testa2pg","config_value": "3"})
    print(request.json())