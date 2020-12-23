import json

to_do_list = {}
to_do_list['tasks'] = []


while True:
    x = input('Choose what to do \n 1 - view a list \n 2 - add a task \n 3 - delete a task \n press "Enter" to quit \n')
    if x == '1':
        with open('to_do_list.json') as json_file:
            to_do_list = json.load(json_file)
            for t in to_do_list['tasks']:
                print('Title: ' + t['title'])
                print('Date: ' + t['date'])
                print('Description: ' + t['description'] + '\n')
    elif x == '2':
        to_do_list['tasks'].append({
        'title': input('Title: '),
        'date': input('Date: '),
        'description': input('Description: ')
    })
        with open('to_do_list.json', 'w') as outfile:
            json.dump(to_do_list, outfile)
    elif x == '3':
            to_do_list['tasks'].pop(0)
            with open('to_do_list.json', 'w') as outfile:
                json.dump(to_do_list, outfile)
    else: print ('unexpected number')

    if not x:
        print("exit")   # Enter to quit
        break