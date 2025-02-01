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
    dic_list.sort()
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{len(book.split())} words found in the document")
    print("")


    for i in range(0,len(dic_list)):
        print(dic_list[i])

    print("--- End report ---")
    
    
if __name__ == "__main__":
    main()