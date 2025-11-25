import requests


user_id = 'SKROSURI'
password = 'Surya@8900'
consumer_key = '5a890664d48449f29ca51f0212259cfc'
secret_key = '2965beb9d20641e28017ba1b8b821260'
datbase_name = 'C0000017469P_1_ALLWORLDPM0'

vantage_url = 'https://allworldpm.deltekfirst.com/AllworldPM/api/token'
data = f"Username={user_id}&Password={password}&grant_type=password&Integrated=N&database={datbase_name}&Client_Id={consumer_key}&client_secret={secret_key}&culture=en-US"
token = requests.post(vantage_url, data = data).json()
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': f"Bearer {token['access_token']}",
}

employees = requests.get('https://allworldpm.deltekfirst.com/AllworldPM/api/project/P250010.000/proposal', headers = headers).json()
#print([i for i in employees if i['Employee'] == '0196'])


print(employees)


