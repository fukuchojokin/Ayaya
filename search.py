def search(file_name, string_to_search):
    with open(file_name, 'r') as read_obj:
        for line in read_obj:
            if string_to_search in line:
                return line
        return False


while 1:
    to_search = input("Enter string to search: ").upper()
    if to_search == 'STOP':
        exit()
    x = search("opcodes8085.txt", to_search)
    print(x)
