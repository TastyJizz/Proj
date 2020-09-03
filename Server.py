
import Event;
import Account;
import Event;
# Simulate a 'server'

# These are static stuffs
#accounts : LTree;
#events : Heap;
#ads : list;

accounts = {};
events = {'life':[], 'sports':[], 'fun':[], 'movie':[], 'food':[], \
          'vehicle':[], 'travel':[], 'game':[], 'electronics':[], 'other':[]};
#ads  = [];



def checkAccounts(accName):
    return accName in accounts;
#def updateAccounts
def check_account(accName, password):
    if accounts[accName].password == password:
        return True;
    return False;
def register(accName, psw, tags) -> bool:
    if checkAccounts(accName):
        print("This account already exists!");
        return False;
    account = Account.Account(accName, psw, tags);
    print("Registered!");
    accounts[accName] = account;
    write_account(account);
    return True;

def getSuggestions(acc:Account.Account) -> list:
    result = [];
    for t in acc.interests:
        if t == '':
            continue;
        for event in events[t]:
            if event not in result:
                result.append(event);
    return set(result);

        
#def get_events();
        
def add_event(eve:Event.Event):
    for t in eve.tag:
        events[t].append(eve);
    return True;
    

def upload_event(event):
    write_event(event);

#def write_accounts();
def write_account(account:Account.Account):
    fout = open(file = 'accs.txt', mode = 'a');
    fout.write(account.account_name + '\n');
    fout.write(account.password + '\n');
    for tag in account.interests:
        fout.write(tag + ' ');
    fout.write('\n');
    fout.close();
# load accounts from local file
def load_accounts():
    account_name:str;
    password:str;
    interests = [];
    fin = open('accs.txt', mode = 'r');
    line = fin.readline();
    while line != '':
        if line == '':
            return;
        account_name = line.rstrip('\n');
        line = fin.readline();
        password = line.rstrip('\n');
        line = fin.readline().rstrip('\n');
        interests = line.split(sep = ' ');
        #interests = tuple(interests);
        accounts[account_name] = \
            Account.Account(account_name, password, interests);
        line = fin.readline();
    fin.close();
# load events from local file
def load_events():
    title = None;
    body = None;
    tag = [];
    fin = open('events.txt');
    event = None;
    line = fin.readline();
    while line != '':
        if line == '\n':
            line = fin.readline();
        title = line.rstrip('\n');
        # May be changed
        line = fin.readline();
        body = line.rstrip('\n');
        line = fin.readline().rstrip('\n');
        tag = line.split(sep = ' ');
        if '' in tag:
            tag.remove('');
        tag = tuple(tag);
        line = fin.readline();
        add_event(Event.Event(title, body, tag));
        
    fin.close();
        
        
def write_event(event):
    fout = open('events.txt', mode = 'a');
    fout.write('\n');
    fout.write(event.title + '\n');
    fout.write(event.body + '\n');
    for t in event.tag:
        fout.write(t + ' ');
    fout.write('\n');
    fout.close();
def write_events(events):
    fout = open('events.txt', mode = 'a');
    for event in events:
        fout.write('\n');
        fout.write(event.title + '\n');
        fout.write(event.body + '\n');
        for t in event.tag:
            fout.write(t + ' ');
        fout.write('\n');
    fout.close();
#def load_ads();

load_events();
load_accounts();

