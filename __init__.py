from comparative_1.guess import guess
from comparative_1.stringDatabase import stringDatabase


def main():
    print("** The great guessing game **")

    stringDatabaseObject = stringDatabase()
    guessObject =guess()
    stringDatabaseObject.readfile()
    guessObject.calling()

main()
