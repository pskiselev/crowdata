import facebook
import requests

def get_fb_token():
    payload = {'grant_type': 'client_credentials', 'client_id': 216000105445673, 'client_secret':  "f7b72b26e029c7b74cceef476c1e1263"}
    file = requests.post('https://graph.facebook.com/oauth/access_token?', params = payload)
    #print file.text #to test what the FB api responded with
    result = file.text.split("=")[1]
    #print file.text #to test the TOKEN
    return result

#token = 'EAACEdEose0cBAGIXWEb03SS4XZC6yaeYosjf36LZB8UjoqrTLUwcYs2WZBQTGKqsA1fEW2UqP4Rd8OV5ubosNpM1ogeFVMKZCmQuutLjxrQnE8aDIYuikWr4rNc2w5ouxBNBYK0l0rwnk7ZBGHD8VC6fLuBnpgs100cLVQ04srQZDZD'

graph = facebook.GraphAPI("EAACEdEose0cBAEuMEogZCk43GVMoArS1PEMirOZAabrrfRQxw0C5xz3LPZCVtywh4RCyzlOZANv1klzr1qpXHrka6AZAN87zFmbE9quVDbfNgKDL1kULskq5R1dntwDWTBN07dbNCvhwztG8hyQatN15zyFyD6nq2ukIVxqTVc5DCnTK3IMuBaupdZANBTd hqvXnEcmZCqyngZDZD")
profile = graph.get_object("me")
friends = graph.get_connections("me", "friends")
graph.put_object("me", "feed", message="I am writing on my wall!")