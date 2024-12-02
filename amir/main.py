# with open('file.txt','w',encoding='utf-8') as file:
#     writer = file.write('ismailmendgaliev')
#     print(writer)

# with open('file.txt','a',encoding='utf-8',newline='\n')as file:
#     append = file.write('curcle\n')
#     print(append)


with open('file.txt','r',encoding='utf-8')as file:
    num = int(input("Какую строчку вы хотите удалить"))
    reader = list(file.readlines())
    reader.pop(num)
    print(reader)
    with open("file.txt", "w", encoding="utf-8") as f:
        f.write(''.join(reader))
        