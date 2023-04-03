import os
from googleapiclient.discovery import build
import json

class Channel:

    def __init__(self, channel_id):
        api_key: str = os.getenv('API_KEY')
        self.__channel_id = channel_id
        youtube = build('youtube', 'v3', developerKey=api_key)
        self.channel_info = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        self.title = self.channel_info['items'][0]['snippet']['title']
        #AIzaSyDCatLeUpzhrL3CpW-dCsCMgZVbChvmRrs
        youtube = build('youtube', 'v3', developerKey=api_key)
        self.channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        self.description = self.channel_info['items'][0]['snippet']['description']
        self.url = 'https://www.youtube.com/channel/' + self.__channel_id
        self.subscriber_count = self.channel_info['items'][0]['statistics']['subscriberCount']
        self.video_count = self.channel_info['items'][0]['statistics']['videoCount']
        self.view_count = self.channel_info['items'][0]['statistics']['viewCount']

    def __str__(self):
        return f'Youtube-канал: {self.title}'

    def __add__(self, other):
        return int(self.subscriber_count) + int(other.subscriber_count)


    def __lt__(self, other):
        return self.subscriber_count < other.subscriber_count


    def __gt__(self, other):
        return self.subscriber_count > other.subscriber_count


    def __ge__(self, other):
        return self.subscriber_count >= other.subscriber_count

    def __le__(self, other):
        return self.subscriber_count <= other.subscriber_count


    def __eq__(self, other):
        return self.subscriber_count == other.subscriber_count

    def print_info(self):
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))


    @classmethod
    def get_service(self):
        service = build('youtube', 'v3', developerKey=os.environ.get('api_key'))
        return service


    def to_json(self):
        data = {
            "title": self.channel_info
        }
        with open('venv/filename.json', "w", encoding="UTF-8") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

#channel_id = 'UC1eFXmJNkjITxPFWTy6RsWg'    # Редакция
pivovarov = Channel('UC1eFXmJNkjITxPFWTy6RsWg')
# #vdud = Channel('')
# pivovarov.print_info()
#vdud.print_info()
print("Task2:")
vdud = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')

print(vdud.url)
print(vdud.subscriber_count)
print(pivovarov.subscriber_count)
# менять не можем
# vdud.channel_id= 'Новое название'
#
# # можем получить объект для работы с API вне класса
# print(Channel.get_service())
#
# # создать файл 'vdud.json' в данными по каналу
# vdud.to_json()

print("Task3:")
print(vdud)
#Youtube-канал: вДудь
print(pivovarov)
#Youtube-канал: Редакция
print(vdud > pivovarov)
print(vdud < pivovarov)
print(vdud + pivovarov)
print(vdud <= pivovarov)
print(vdud >= pivovarov)
print(vdud == pivovarov)
