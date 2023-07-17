import json


class LikeDB:
    def __init__(self, path):
        self.path = path
        try:
            with open(path) as f:
                self.data = json.load(f)
        except:
            self.data = {}


    def get_likes(self):
        return self.data
    
    def save(self, data):
        with open(self.path, 'w') as f:
            json.dump(data, f, indent=4)

    def add_user(self, chat_id):
        data = self.get_likes()
        keys = data.keys()

        if str(chat_id) not in keys:
            data[str(chat_id)] = {
                "like": 0,
                "dislike": 0
            }
            self.save(data)

        return data
    
    def add_like(self, chat_id):
        data = self.add_user(chat_id)
        if data[str(chat_id)]["like"]==0:
            data[str(chat_id)]['like'] += 1
            data[str(chat_id)]["dislike"]=0
        else:
            data[str(chat_id)]['like']=0

        self.save(data)
    
    def add_dislike(self, chat_id):
        data = self.add_user(chat_id)

        if data[str(chat_id)]["dislike"]==0:
            data[str(chat_id)]["like"]=0
            data[str(chat_id)]['dislike'] += 1
        else:
            data[str(chat_id)]['dislike']=0

        self.save(data)