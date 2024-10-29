calls = 0
def count_calls ():
    global calls
    calls = calls + 1

def string_info (string):
    str(string)
    up = string.upper()
    low = string.lower()
    cor = ( len(string), up, low)
    print(cor)
    count_calls()

def is_contains (string, list_to_search):
    str(string)
    up = string.upper()
    new_list_to_search = []
    for i in list_to_search:
        up_2 = i.upper()
        new_list_to_search.append(up_2)
    for j in new_list_to_search:
        if up == j:
            print('True')
            break
        if up != j:
            print('False')
            break
    count_calls()


string_info('home')
is_contains( 'YEAT' , ['yeat', 'boss'])
is_contains( 'dad' , ['girl', 'man', 'mom'])
print(calls)
