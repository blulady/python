#
# Python 3.8.3
#
#
#mulitple variable rquirement
#
#




def start():
    f_name = 'Sarah'
    l_name = 'Conner'
    age = 28
    gender = 'Female'
    get_info(f_name,l_name,age,gender)


    


def get_info(f_name,l_name,age,gender):
    print("My name is {} {}. I am a {} yearold {}.".format(f_name,l_name,age,gender))

#wild cards fire off in order, could use an index starting with 0







if __name__ == "__main__":
    start()
    
