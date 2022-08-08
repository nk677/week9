import json
import os

directory = input("Please enter the preferred directory to save the file: ")
fileName = input("Please enter the name of the file: ") + '.json'


def readFile():
    try:
        if os.path.isdir(directory):
            # print("directory exist")
            with open(os.path.join(directory, fileName)) as f:
                data = json.load(f)
                f.close()

    except FileNotFoundError:
        return None

    else:
        return data


def writeFile():
    userFileName = readFile()
    if userFileName:
        print(f"The below are the existing record\n {userFileName}")

    else:
        if os.path.isdir(directory):
            # print("directory exist")
            name = input("Please enter your name: ")
            address = input("Please enter your address: ")
            phone = input("Please enter your phone number: ")
            with open(os.path.join(directory, fileName), 'w') as f:
                json.dump(name.strip() + ',' + address.strip() + ',' + phone.strip(), f)
                f.close()


if __name__ == "__main__":
    writeFile()
