import requests

data = {'username':'測試使用者'}
response = requests.post("http://192.168.58.133/~handsome/testpost.php",data)

if response.status_code == 200:
    print(response.content.decode('utf-8'))