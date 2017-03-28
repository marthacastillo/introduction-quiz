import requests
import json
url ='http://10.110.70.11:9200/beeva_data/martha/2?pretty'

data = json.loads(open("/home/administradorcito/introduction-quiz/introduction_quiz.json").read())
print(data)
read = requests.post(url, json = data)
print(read.text)






