


def get_answers():
    go = True
    while go:
        answer = input('why don\'t you want me anymore?  ')
        if answer == '':
            print('you need to explain why.')
        elif answer == 'i don\'t know':
            print('I don\'t know is not an answer')
        else:
            go = False

get_answers()
        
