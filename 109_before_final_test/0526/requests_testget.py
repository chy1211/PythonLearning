import requests

data = {'username':'測試使用者'}
response = requests.get("http://192.168.58.133/~handsome/testget.php",data)

if response.status_code == 200:
    print(response.content.decode('utf-8'))