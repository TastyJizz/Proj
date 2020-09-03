

#Put a list of keys with same values into a dictionary
def put_reversed(objs:dict, keys:list, value:str):
    for key in keys:
        objs[key] = value;
    return objs;

# static tag set in real life can be much bigger
tags = ('life', 'sports', 'fun', 'movie', 'food', 'vehicle', 'game', 'electronics', 'other');
# A static hash table to store keywords and their related tags
TKSet = {};
put_reversed(TKSet, ['drink', 'Chinese food', 'muslin', 'fast food', 'lunch', 'hotpot', 'sushi', \
                 'chicken', 'rice', 'seafood', 'curry', 'soup', 'noodles', 'cake', 'sandwich', \
                 'toast', 'porridge', 'pasta', 'dumpling'], 'food');
put_reversed(TKSet, ['insurance', 'salary', 'accommodation', 'lifestyle', 'daily', 'market', 'trip'], 'life');
put_reversed(TKSet, ['football', 'basketball', 'table tennis', 'badminton', 'swimming',\
                  'NBA', 'World Cup', 'Olympic', 'athlete', 'ball', 'base', 'boxing', 'champion', \
                  'championship', 'exercise', 'fitness', 'gym', 'goal', 'skating', 'lose', 'MVP', 'quarterback', 'team'], 'sports');
put_reversed(TKSet, ['interesting', 'funny', 'comedy', 'programme', 'video', 'joke', 'holiday', 'gif', 'friends'], 'fun');
put_reversed(TKSet, ['animation', 'mandarin', 'Chinese', 'English', 'Korean', 'Japanese', 'action', 'drama', 'cinema', 'horror', 'fantasy', 'romance',\
                  'thriller', 'ticket', 'booking', 'release', 'adventure'], 'movie');
put_reversed(TKSet, ['transport', 'bicycle', 'motor', 'car', 'truck', 'bus', 'train', 'tram', 'air', \
                    'airplane', 'Acura', 'Audi', 'Bentley', 'BMW', 'Buick', 'Chevrolet', 'Ferrari', 'Ford', \
                    'Honda', 'Hyundai', 'Jeep', 'Lexus', 'Mercedes', 'Benz', 'Mazda'], 'vehicle');
put_reversed(TKSet, ['hotel', 'flight', 'ticket', 'vacation', 'trip', 'fare', 'destination', \
                   'package', 'budget', 'expedia', 'cheap', 'expensive', 'place', 'scene', 'landscape', 'self-driving'], 'travel');
put_reversed(TKSet, ['mobile', 'PC', 'console', 'Android', 'iOS', 'apps', 'PS4', 'NS', 'RPG', 'ACT', 'AVG', 'FPS', 'ETC',\
                 'MMO', 'MUG', 'PUZ', 'RTS', 'SLG', 'STG', 'PUBG', 'Supercell', 'Ubisoft', 'EA', 'Nintendo', 'Blizzard', \
                 'Sony', 'Capcom', 'Konami', 'SE', 'SEGA', 'BANDAI'], 'game');
put_reversed(TKSet, ['television', 'air conditioning', '3D', 'printing', 'device', 'cable', 'earphone', \
                        'headphone', 'chip', 'Huawei', 'Apple', '5G', 'tablet', 'screen', 'powerbank', 'hardware', \
                        'CD', 'VCR', 'computer', 'Microsoft', 'GPU', 'CPU'], 'electronics');



class Event:
    tag : tuple;
    title : str;
    body : str;
    #self.likes : int;
#    self.dislikes : int;

    def __init__(self, tit, bod, tag = None):
        self.title = tit;
        self.body = bod;
        if tag == None:
            self.inspect();
        else:
            self.tag = tag;
    
    #def like(self):
        #self.likes += 1;
    #def getLikeNum(self) -> int:
        #return self.likes;
    def inspect(self):
        tokens = self.body.split(sep = ' ');
        self.search(tokens);

    def search(self, words:list):
        t:list = [];
        for w in words:
            if w in TKSet:
                if TKSet[w] not in t:
                    t.append(TKSet[w]);
        if len(t) < 1:
            t.append('other');
        self.tag = tuple(t);
        return True;
    def __str__(self):
        result = self.title + '\n' + self.body + '\n';
        return result;
        
