import Client;
import Event;
import Account;
import Event;
# Simulate a 'server'

# These are static stuffs
#accounts : LTree;
#events : Heap;
#ads : list;

accounts = {};
events = {'life':[], 'sports':[], 'fun':[], 'film':[], 'food':[], \
          'vehicle':[], 'game':[], 'electronics':[]};
ads  = [];
def checkAccounts(accName):
    return accName in accounts;
#def updateAccounts
    
def register(accName, psw, tags) -> bool:
    if checkAccounts(accName):
        print("This account already exists!");
        return False;
    account = Account.Account(accName, psw, tags);
    print("Registered!");
    accounts[accName] = account;
    write_account(account);
    return True;

def getSuggestions(acc:Account.Account, seen):
    result = [];
    for t in eve.tag:
        for event in events[e]:
            result.append(event);
    return set(result);

        
#def get_events();
        
def add_event(eve:Event.Event);
    for t in eve.tag:
        event[t].append(eve);
    return True;
    write_event();
    

#def updateEvent

#def write_accounts();
def write_account(account:Account.Account):
    #fout = open(file = 'accs.txt', mode = 'a');
    
# load accounts from local file
def load_accounts():
    #fin = open('accs.txt', mode = 'r');
    
# load events from local file
def load_events();

def write_event();

def write_events()

def load_ads();

