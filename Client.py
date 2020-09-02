import Server;
import Event;
import Account;
# Simulate a 'client'
# Version 1.0

class Client:
    self._account : Account.Account;
    self._accountName:str;
    self._password:str;
    self._online = False;

    def __init__(self):
        #......
        
    def run(self):
        self.prompt_main();

    def prompt_main(self);
        option : str;
        while option != '3':
            print('======Welcome to daily news!=========', \
                  'Pick an action:', '1) Log in', '2) Register', \
                  '3) Quit the program', '(Please call our hotline if \
you want to report a bug or have any problems.\n', sep = '\n');
                  
            option = self.get_option(('1', '2', '3'));
            if option == '1':
                account = input('Please enter your account:');
                pwd = input('Please enter your password:');
                if not log_in(account, pwd):
                    'Back to the main menu...';
                    continue;
                self.prompt_user();
            if option == '2':
                self.register();
            if option == '3':
                self.log_out();
                return;
    # The prompts after user already  logged in            
    def prompt_user(self):
        option : str;
        read = 0;
        print('Hello! ', self._accountName, \
              ', Check what\'s happening right now!', \
              '\n-----Press \'U\' to upload your own moments!----',
              '\n-----Press \'R\' to refresh the page!----',
              '\n-----Press \'Q\' to log out!----', sep = '');
        print(self.get_suggestions(read));
        read += 3;
        while option != 'q':
            option = input();
            if option == 'u':
                self.prompt_upload();
            if option == 'r':
                print(self.get_suggestions(read));
                read += 3;
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
        opt = get_option(('1', '2'));
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
        if not Server.checkAccounts(acc, pwd):
            print("Incorrect account name or password.");
            return False;
        self._accountName = acc;
        self._password = pwd;
        self._online = True;
        return True;
    
    def log_out():
        self._accountName = None;
        self._password = None;
        self._online = False;

    # Register in the server and get the new user's interests
    def register(self):
        account : str;
        psw : str;
        tags = [];
        opt = "";
        account = input("Please enter the new acount name:");
        while Server.checkAccounts(account):
            acount = input("Account name unavailable! Please input again: ");
        psw = input("Please enter your password:");
        while not psw == input("Please enter your password again:"):
            print("Passwords unmatch!");
            psw = input("Please enter again:");
        print("What are you interested in?", "1) Life", \
              "2) Sports", "3) Fun" , "4) Film", "5) Food", \
              "6) Vehicle", "7) Game", "8) Electronics", \
              "Press 'C' to confirm, "sep = "\n");
        opt = get_option(('1', '2', '3', '4', \
                          '5', '6', '7', '8', 'c');
        while opt != 'c':
            if not opt in tags:
                tags.append(opt);
            print("Pick another one?");
            opt = get_option(('1', '2', '3', '4', \
                          '5', '6', '7', '8', 'c');
        Server.register(account, psw, tags);
        
        
    def upload(self, tit, bod);
        Server.add_event(Event.Event(tit, bod));
        
    def refresh
    # get the keywords and pass them to the server
    #def search
    # Like or dislike the event
    #def comment

    #Retrieve account information
    def retrieveAccInfo
    # Retrieve data or suggested events from the server
    # The read content would be ignored and user would be
    # informed if there are no more news left
    def get_suggestions(self, read):
    

def main():
    cl = Client();
    cl.run();


main();




    
    
