guest_list = ['Joan', 'Katie', 'Marion', 'Maureen', 'Brian']
event_details ={
    'date': 24,
    'month': 'November',
    'venue1': 'home',
    'venue2': 'the club'
}

message = 'Hi ' + guest_list[0] + '! I am holding a dinner party on %i %s' %(event_details['date'], 
event_details['month']) + ' at %s' %(event_details['venue1']) + '. I hope you can come!'
print(message)
print(guest_list)
guest_list.append('Michael')
print(guest_list)
