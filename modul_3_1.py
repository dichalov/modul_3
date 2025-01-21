#Домашняя работа по уроку "Пространство имён"
#Задача "Счётчик вызовов

calls=0
def count_calls():
    global calls
    calls+=1
    return calls


def string_info (string):
    global calls
    count_calls()
    info=[len(string), string.lower(),string.upper()]

    return info

def is_contains (string,list_to_search):
    global calls
    count_calls()
    normal_string=string.lower()
    normal_list_to_search=[i.lower() for i in list_to_search]
    #print(normal_list_to_search)
    if normal_string in normal_list_to_search:
        return True
    else: return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)



