people = {

    'Alice':{
        'phone':'1166',
        'addr':'Foo drive 123'
        },
    
    'jobs':{
        'phone':'5311',
        'addr':'koo street 64'
        },

    'ceal':{
        'phone':'3158',
        'addr':'Buu aven 34'
        }
    }

labels = {
    'phone':'phone number',
    'addr':'address'
    }

name = raw_input('name: ')

request = raw_input('Phone number (p) or address (a)? ')

if request == 'p':key = 'phone'
if request == 'a':key = 'addr'

person = people.get(name,{})
label = labels.get(key,key)
result = person.get(key,'not availble')

print "%s's %s is %s."%(name,label,result)
