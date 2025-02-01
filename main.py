def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    book = file_contents.lower()
    myDict = {}
    for char in book:
        if len(myDict) == 0:
            myDict[char] = 1
        else:
            if char in myDict:
                myDict[char] += 1
            else:
                myDict[char] = 1
    dic_list=[] 
    for char in myDict:
        if char.isalpha():
            dic_list.append(f"The '{char}' character was found {myDict[char]} times")
    
    for i in dic_list
        print(i)

    
    
if __name__ == "__main__":
    main()