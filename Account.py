class Account:
    # Temperarily public, would be private in version 2.0
    account_name : str;
    password : str;
    interests : list;
    def __init__(self, acc, psw, tags):
        self.account_name = acc;
        self.password = psw;
        self.interests = tags;
