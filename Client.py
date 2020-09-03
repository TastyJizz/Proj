import Server;
import Event;
import Account;
# Simulate a 'client'
# Version 1.0

class Client:
    _account : Account.Account;
    _accountName:str;
    _password:str;
    _online = False;
    _suggestions:list;
    read = 0;
    def __init__(self):
        self._account = None;
        self._accountName = None
        self._password = None;
        self._online = False;
        self._suggestions = None;
        self.read = 0;
        
    def run(self):
        self.prompt_main();

    def prompt_main(self):
        option = '';
        while option != '3':
            print('======Welcome to daily news!=========', \
                  'Pick an action:', '1) Log in', '2) Register', \
                  '3) Quit the program', '(Please call our hotline if \
you want to report a bug or have any problems.\n', sep = '\n');
                  
            option = self.get_option(('1', '2', '3', 'a', 'e'));
            if option == '1':
                account = input('Please enter your account:');
                pwd = input('Please enter your password:');
                if not self.log_in(account, pwd):
                    'Back to the main menu...';
                    continue;
                self.prompt_user();
            if option == '2':
                self.register();
            if option == '3':
                self.log_out();
                return;
            if option == 'a':
                print(Server.accounts);
            if option == 'e':
                print(Server.events);
    # The prompts after user already  logged in            
    def prompt_user(self):
        option = '';
        read = 0;
        print('Hello! ', self._accountName, \
              ', Check what\'s happening right now!', \
              '\n-----Press \'U\' to upload your own moments!----',
              '\n-----Press \'R\' to refresh the page!----',
              '\n-----Press \'Q\' to log out!----', sep = '');
        self.get_suggestions(self.account);
        self.refresh();
        while option != 'q':
            print('Hello! ', self._accountName, \
              ', Check what\'s happening right now!', \
              '\n-----Press \'U\' to upload your own moments!----',
              '\n-----Press \'R\' to refresh the page!----',
              '\n-----Press \'Q\' to log out!----', sep = '');
            option = input();
            if option == 'u':
                self.prompt_upload();
            if option == 'r':
                print(self.refresh());
            if option == 'q':
                self.log_out();
                
    def prompt_upload(self):
        title : str;
        body :str;
        opt : str;
        # May add validations here
        title = input('Enter a title with a minimum letters of 10');
        body = input('How do you feel today?');
        print('Upload now? 1) yes 2) Cancel');
        opt = self.get_option(('1', '2'));
        if opt == '1':
            self.upload(title, body);
        
        
        
        
        
    def get_option(self, valid_opts:tuple):
        opt = input('Your choice:');
        while not opt in valid_opts:
            opt = input('Invalid option! Please do it again:');
        return opt;
    #def log_in_pressed(self)

    
    # All these are support methods if in GUI
    def log_in(self, acc, pwd) -> bool:
        if not Server.checkAccounts(acc):
            print("No such account!");
            return False;
        if not Server.check_account(acc, pwd):
            print("Incorrect password!");
            return False;
        self._accountName = acc;
        self._password = pwd;
        self._online = True;
        self.account = Server.accounts[self._accountName];
        self.get_suggestions(self.account);
        return True;
    
    def log_out(self):
        self._accountName = None;
        self._password = None;
        self._online = False;
        self.account = None;
        self.read = 0;

    # Register in the server and get the new user's interests
    def register(self):
        account : str;
        psw : str;
        tags = [];
        opt = "";
        account = input("Please enter the new acount name:");
        while Server.checkAccounts(account):
            account = input("Account name unavailable! Please input again: ");
        psw = input("Please enter your password:");
        while not psw == input("Please enter your password again:"):
            print("Passwords unmatch!");
            psw = input("Please enter again:");
        print("What are you interested in?", "1) Life", \
              "2) Sports", "3) Fun" , "4) Film", "5) Food", \
              "6) Vehicle", "7) Game", "8) Electronics", \
              "Press 'C' to confirm, ",sep = "\n");
        opt = self.get_option(('1', '2', '3', '4', \
                          '5', '6', '7', '8', 'c'));
        while opt != 'c':
            if not opt in tags:
                tags.append(Event.tags[int(opt)]);
            print("Pick another one?");
            opt = self.get_option(('1', '2', '3', '4', \
                          '5', '6', '7', '8', 'c'));
        Server.register(account, psw, tags);
        
        
    def upload(self, tit, bod):
        event = Event.Event(tit, bod);
        Server.add_event(event);
        Server.upload_event(event);
        print("Upload successful!");
        self.get_suggestions(self.account);
        
    def refresh(self):
        try:
            for n in range(3):
                if self.read > len(self._suggestions):
                    print("That's all... for now");
                    break;
                print(self._suggestions[self.read]);
                self.read += 1;
                
        except IndexError:
            print("That's all for now!");
        
        
    # get the keywords and pass them to the server
    #def search
    # Like or dislike the event
    #def comment

    #Retrieve account information
    #def retrieveAccInfo
    # Retrieve data or suggested events from the server
    # The read content would be ignored and user would be
    # informed if there are no more news left
    def get_suggestions(self, account) -> list:
        self._suggestions = list(Server.getSuggestions(account));
        return self._suggestions;

def main():
    cl = Client();
    cl.run();


main();




    
    
