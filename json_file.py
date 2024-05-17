import json 

data = '''
    {
        "name" : "Daniel",
        "phone" : {
            "type" : "intl",
            "number" : "+1 734 303 4456"
        },
        "email" : {
            "hide" : "yes"
        }
    }
'''


info = json.loads(data)

print("Name: ", info['name'])
print("Phone Number:", info['phone']['number'])
print("Hidden:", info['email']['hide'])


input = '''
    [
        {
            "id" : "001",
            "x" : "2",
            "name" : "Chuck"
        },
        {
            "id" : "009",
            "x" : "7",
            "name" : "Brent"
        }
    ]
'''

info = json.loads(input)

print("Users:", len(info))
for i in info:
    print(i['id'], i['x'], i['name'])