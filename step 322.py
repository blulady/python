#people_dictionary = {'Brett' :['Male' , 'Weight 175'], 'Nancy' : ['Female', 'Weight 125'], 'Patrick' : ['Male', 'Weight 195'], 'Diane' : ['Female', 'Wieght 115'], 'Adam' : ['Male' , 'Weight 215']}
#print(people_dictionary)
#Name = input('Please type in a name:')
#print ('You typened in the name ' + Name)
#Persons_Data = people_dictionary[Name]
#print(Persons_Data)

def start():
    
    people_dictionary = {'brett' :['Male' , 'Weight 175'], 'nancy' : ['Female', 'Weight 125'], 'patrick' : ['Male', 'Weight 195'], 'diane' : ['Female', 'Wieght 115'], 'adam' : ['Male' , 'Weight 215']}
    print(people_dictionary)
    Name = input('Please type in a name:').lower()
    print ('You typed in the name ' + Name.capitalize())    
    try:
        Persons_Data = people_dictionary[Name]
        print ('Name: ' + Name.capitalized())
        print ('Sex: ' + Persons_Data[0])
        print ('Weight: ' + Persons_Data[1])
        more()
    except:
        print ('That name, (as written) was not found in the dictionary.')
        more()
def more():
    if More == 'No':
        quit()
    if More == 'Yes':
        start()
    else:
        print("Please enter Yes or No.")
        more()

start()
