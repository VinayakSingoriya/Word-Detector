import os
def isword(filename):
    with open(filename, 'r') as f:
        file_content = f.read()
        if word in file_content.lower():
            return True
        else:
            return False    
if __name__ == "__main__":
    found_word = 0
    word = input("Enter word which you want to search \n")
    dir_content = os.listdir()
    for item in dir_content:
        if item.endswith('txt'):
            print(f"detecting {word} in {item}.....")
            flag = isword(item)
            if (flag):
                print(f">>>{word} found in {item}!!!!\n")
                found_word += 1
            else:
                print(f">>>{word} not found in {item}\n")    
