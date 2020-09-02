class Account:
    self._accountName : str;
    self._password : str;
    self._interests : list;
    def __init__(self, acc, psw, tags):
        self._accountName = acc;
        self._password = psw;
        self._interests = tags;
