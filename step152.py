


def gimme():
    var1 = input("\n please give me a number under 10:      ")
    return var1

def judge():
    now = True
    while now:
        var1 = gimme()
        try:
            var1 = int(var1)
            now = False
        except ValueError as e:
            print("{}:\n\n you did not provide a number under 10.".format(e))
    print("\nThanks for {}.".format(var1))


if __name__ == "__main__":
    judge()
        
