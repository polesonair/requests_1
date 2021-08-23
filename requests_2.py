import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token
        self.APT_BASE_URL = 'https://cloud-api.yandex.net/'
        self.headers = {'Authorization': OAuth}

    def upload(self, file_path: str):
        req = requests.get(self.APT_BASE_URL + 'v1/disk/resources/upload', params={'path': 'Netology/test.txt'}, headers=self.headers)
        upload_url = req.json().get('href')  # ссылка

        #  Открываем файл для отправки и отправляем
        with open(file_path, 'r', encoding='utf-8') as f:
            data = f.read()
        req1 = requests.put(upload_url, headers=self.headers, files={'file': data})
        print(req1.status_code)


OAuth = ''
file_path = 'files/test.txt'
uploader = YaUploader(OAuth)
result = uploader.upload(file_path)

