def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    book = file_contents.lower()
    myDict = {}
    for char in book:
        if len(myDict) == 0:
            myDict[char] = 1
        else
            if char in myDict:
                myDict[char] += 1
            else
                myDict[char] = 1 
    print(myDict)

    
    
if __name__ == "__main__":
    main()