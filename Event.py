import nltk;

# static tag set in real life can be much bigger
tags = ('life', 'sports', 'fun', 'film', 'food', 'vehicle', 'game', 'electronics');
# A static hash table to store keywords and their related tags
TKSet : Dictionary;
class Event:
    self.tag : tuple;
    self.title : str;
    self.body : str;
    self.likes : int;
#    self.dislikes : int;

    def __init__(self, tit, bod):
        self.title = tit;
        self.body = bod;
        self.inspect();

    def like(self):
        self.likes += 1;
    def getLikeNum(self) -> int:
        return self.likes;
    def inspect(self):
        nltk_tokens = nltk.word_tokenize(body);
        self.search(nltk_tokens);

    def search(self, words:list):
        t:list = [];
        for w in words:
            if TKSet[w] in tags:
                t.append(TKSet[w]);
        self.tag = tuple(t);
        return True;
