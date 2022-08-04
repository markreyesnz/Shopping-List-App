
# Mark Reyes
# 04/09/2021
# Shopping List App

def display_as_list(display_items,message="Item",counter_reqd=True):
    """ Code to display list """

    if len(display_items) > 0:
        print()
        for counter, item in enumerate(display_items, start=1):
            if counter_reqd:
                print(f'{message} {counter}: {item}')
            else:
                print(f'{item}')
    else:
        print('Sorry, the list is empty.')
    return bool(len(display_items)>0)

def get_option(prompt_msg='Option: '):
    """get_option to allow user to enter Option"""
    prompt_msg = str(input(f'{prompt_msg}').strip().lower())

    return prompt_msg

def get_item(prompt_msg='Item: '):
    """get_item to allow user to enter Item"""
    prompt_msg = str(input(f'{prompt_msg}').strip().lower())

    return prompt_msg.capitalize()

def get_total_items(user_list):
    """get_total_items returns a string"""

    result = ''

    if len(user_list) == 1:
        result += f'There is {len(user_list)} item in the list.'
    else:
        result += f'There are {len(user_list)} items in the list.'

    return result

def add_item(user_list):
    """ The add_item function makes use of the get_item, get_total_items and get_option functions. """

    item_please = get_item('Please enter the item to be added: ')

    if item_please == '':
        print('No item was entered.')
        print(get_total_items(user_list))
        return False
    else:
        if item_please in user_list:
            item_confirmation = get_option(f'[{item_please}] is already in the list, please confirm that you want to add another (y/n): ')

        else:
            item_confirmation = 'y'

        if item_confirmation == 'y':
            user_list.append(item_please)
            print(f'[{item_please}] has been added to the list.')
            output = True

        else:
            print(f'[{item_please}] was not added.')
            output = False

        print(get_total_items(user_list))
        get_total_items(user_list)
        return output

def remove_item(user_list):
    """ remove_item asks the user to enter the item number to be removed by calling get_option. """
    
    if len(user_list) > 0:
        remove_alpha = 'a'
        while not(remove_alpha.isdigit()):
            remove_alpha = get_option('Please enter the item number of the item to remove or 0 to cancel: ')

            if not(remove_alpha.isdigit()):
                print('The item number must be a positive integer.')

        remove_alpha = int(remove_alpha)

        if remove_alpha == 0:
            print('Remove request cancelled.')
            return False

        else:
            if remove_alpha <= len(user_list):
                yes_no = get_option('Are you sure (y/n)? ')

                if yes_no == 'y':
                    item = user_list.pop(remove_alpha - 1)
                    print(f'Item {remove_alpha} [{item}] has been removed from the list.')
                    return True
                else:
                    print(f'Item {remove_alpha} [{item}] was not removed from the list.')
            else:
                print(f'Sorry item {remove_alpha} does not exist in the list.')
                return False
    else:
        print('Sorry, the list is empty.')
        return False

def sort_list(user_list):
    """ If there are enough items in the list then sort_list sorts the items in the list, informs the user and returns boolean True. """

    user_list.sort()
    
    if len(user_list) > 1:
        print('The list has been sorted.')
        return True
    if len(user_list) == 1:
        print('There is only one item in the list, the list does not need to be sorted.')
        return False
    else:
        print('Sorry, the list is empty.')
        return False

def empty_list(user_list):
    """ If the list is not empty and the user confirms they want to empty the list (by entering 'y' in either case) then empty_list clears the items from the list and returns boolean True. """

    if len(user_list) >= 1:
        yes_no = get_option('Please confirm that you want to empty the list (y/n): ')
        if yes_no =='y':
            print('All the items have been removed from the list.')
            user_list.clear()
            return True
        else:
            print('The list has not been emptied.')
            return False
    else:
        print('Sorry, the list is empty.')
        return False

def count_instances(user_list):
    """ If there are items in the list then count_instances asks the user to enter the item to be counted by calling the get_item function and informs the user how many instances were found and returns boolean True. """

    
    if len(user_list) > 0:
        item = get_item('Please enter the item to be counted: ')
        if not item == 'Alpha':
            list_number = user_list.count(item)
            print(f'There are {list_number} instances of [{item}] in the list.')
            return True   
        if len(user_list) == 1:
            list_number = user_list.count(item)
            print(f'There is {list_number} instance of [{item}] in the list.')
            return True
        if len(user_list) > 1:
            list_number = user_list.count(item)
            print(f'There are {list_number} instances of [{item}] in the list.')
            return True
    else:
        print('Sorry, the list is empty.')
        return False

items_list = []

list_of_options = [

'Shopping list options.',
'A) Add an item.',
'R) Remove an item by its item number.',
'D) Display the total number of items in the list.',
'L) List all the items.',
'S) Sort the list.',
'E) Empty the list.',
'C) Count the instances of an item in the list.',
'Q) Quit.'
]

program = True

while program == True :
    display_as_list(list_of_options, counter_reqd = False)
    input_item = get_option()
    if input_item == "a":
        add_item(items_list)
        
    elif input_item == "r":
        remove_item(items_list)
        
    elif input_item == "d":
        print (get_total_items(items_list))
        
    elif input_item =="l":
        display_as_list(items_list)

    elif input_item =="s":
        sort_list(items_list)

    elif input_item == "e":
        empty_list(items_list)

    elif input_item == "c":
        count_instances(items_list)

    elif input_item == "q":
        program = False

print ('Shopping time.')
