'''
Welcome my Read_Book homework
Name:Vicheka
'''
import json
from enum import Enum
class partenter(Enum):
    Part1 =  1
    Part2 = 2
    Part3 = 3
    Part4 = 4
    Exit = 0
class entermenu(Enum):
    Chapter1 = 1
    Chapter2 = 2
    Chapter3 = 3
    Exit = 0
class bookmenu(Enum):
    ReadBook = '1'
    Exit = '0'

file_book = open('book.json','r')
book_data = json.load(file_book)
contents=book_data['contents']

for name,info in book_data.items():
    show_name=name.title()
    show_BookName=book_data['Book_Name']
    show_Author=book_data['Author']
    show_Date=book_data['release_date']
chapters = contents.keys() 
parts = contents.values()
def Read_Book(n=1,pn=1):
    print('Welcome to The Power of Habit')
    print('-'*30)
    while True:
        for chapter in chapters :
            print(f'{n}.{chapter}')
            n +=1
            if n >=4 :
                n = 1
        print('-'*30)
        print('press 0 and enter to go back')
        CEnter=input('Input chapter u want to read:')
        print('-'*30)
        CEnter = int(CEnter)
        CEnters = CEnter - 1
        if CEnter == entermenu.Exit.value:
            break
        elif CEnter == entermenu.Chapter1.value:
            while True: 
                print(f'Chapter{CEnter}.{list(chapters)[CEnters]}')
                print('-'*30)
                for part in (list(parts)[CEnters]) :
                    print(f'Part{pn}.{part}')
                    pn += 1
                    if pn >=4 :
                        pn = 1
                print('-'*30)
                chapter1  = contents['ChapterOne:The Habits of Individuals']    
                print('Press 0 and enter to go back')
                PEnter = input('Enter part you want to read:')
                PEnter = int(PEnter)
                PEnters = PEnter - 1
                if PEnter == partenter.Exit.value:
                    break
                elif PEnter == partenter.Part1.value:
                    while True: 
                        print('-'*30)
                        print(f'Chapter{CEnter}.{list(chapters)[CEnters]}')
                        print(f'Part{PEnter}.{list(chapter1)[PEnters]}')
                        print('-'*30)
                        print(list(chapter1.values())[PEnters])
                        print('-'*30)
                        e = input('Press 0 and enter to go back')
                        print('-'*30)
                        #e = Exit
                        if e == '0':
                            break
                elif PEnter == partenter.Part2.value:
                    while True:
                        print('-'*30)
                        print(f'Chapter{CEnter}.{list(chapters)[CEnters]}')
                        print(f'Part{PEnter}.{list(chapter1)[PEnters]}')
                        print('-'*30)
                        print(list(chapter1.values())[PEnters])
                        print('-'*30)
                        e = input('Press 0 and enter to go back')
                        #e = Exit 
                        if e == '0':
                            break
                elif PEnter == partenter.Part3.value:         
                    while True:
                        print('-'*30)
                        print(f'Chapter{CEnter}.{list(chapters)[CEnters]}')
                        print(f'Part{PEnter}.{list(chapter1)[PEnters]}')
                        print('-'*30)
                        print(list(chapter1.values())[PEnters])
                        print('-'*30)
                        e = input('press 0 and enter to go back')
                        print('-'*30)
                        #e = Exit
                        if e == '0':   
                            break
        elif CEnter == entermenu.Chapter2.value:
            while True: 
                print(f'Chapter{CEnter}.{list(chapters)[CEnters]}')
                print('-'*30)
                for part in (list(parts)[CEnters]):
                    print(f'Part{pn}.{part}')
                    pn += 1
                    if pn >=5 :
                        pn = 1
                print('-'*30)
                chapter2  = contents['ChapterTwo:The Habits of Successful Organization']
                print('Press 0 and enter to go back')
                PEnter = input('Enter part you want to read:')
                PEnter = int(PEnter)
                PEnters = PEnter - 1
                if PEnter == partenter.Exit.value:
                    break
                elif PEnter == partenter.Part1.value:
                    while True: 
                        print('-'*30)
                        print(f'Chapter{CEnter}.{list(chapters)[CEnters]}')
                        print(f'Part{PEnter}.{list(chapter2)[PEnters]}')
                        print('-'*30)
                        print(list(chapter2.values())[PEnters])
                        print('-'*30)
                        e = input('Press 0 and enter to go back')
                        #e = Exit
                        if e == '0':
                            break
                elif PEnter == partenter.Part2.value:
                    while True:
                        print('-'*30)
                        print(f'Chapter{CEnter}.{list(chapters)[CEnters]}')
                        print(f'Part{PEnter}.{list(chapter2)[PEnters]}')
                        print('-'*30)
                        print(list(chapter2.values())[PEnters])
                        print('-'*30)
                        e = input('Press 0 and enter to go back')
                        #e = Exit 
                        if e == '0':
                            break
                elif PEnter == partenter.Part3.value:         
                    while True:
                        print('-'*30)
                        print(f'Chapter{CEnter}.{list(chapters)[CEnters]}')
                        print(f'Part{PEnter}.{list(chapter2)[PEnters]}')
                        print('-'*30)
                        print(list(chapter2.values())[PEnters])
                        print('-'*30)
                        e = input('press 0 and enter to go back')
                        #e = Exit
                        if e == '0':  
                            break 
                elif PEnter == partenter.Part4.value:
                    while True:
                        print('-'*30)
                        print(f'Chapter{CEnter}.{list(chapters)[CEnters]}')
                        print(f'Part{PEnter}.{list(chapter2)[PEnters]}')
                        print('-'*30)
                        print(list(chapter2.values())[PEnters])
                        print('-'*30)
                        e = input('press 0 and enter to go back')
                        #e = Exit
                        if e == '0':
                            break
        elif CEnter == entermenu.Chapter3.value:
            while True: 
                print(f'Chapter{CEnter}.{list(chapters)[CEnters]}')
                print('-'*30)
                for part in (list(parts)[CEnters]) :
                    print(f'Part{pn}.{part}')
                    pn += 1
                    if pn >=3 :
                        pn = 1
                print('-'*30)
                chapter3  = contents['ChapterThree:The Habits of Societies']    
                print('Press 0 and enter to go back')
                PEnter = input('Enter part you want to read:')
                PEnter = int(PEnter)
                PEnters = PEnter - 1
                if PEnter == partenter.Exit.value:
                    break
                elif PEnter == partenter.Part1.value:
                    while True: 
                        print('-'*30)
                        print(f'Chapter{CEnter}.{list(chapters)[CEnters]}')
                        print(f'Part{PEnter}.{list(chapter3)[PEnters]}')
                        print('-'*30)
                        print(list(chapter3.values())[PEnters])
                        print('-'*30)
                        e = input('Press 0 and enter to go back')
                        #e = Exit
                        if e == '0':
                            break
                elif PEnter == partenter.Part2.value:
                    while True:
                        print('-'*30)
                        print(f'Chapter{CEnter}.{list(chapters)[CEnters]}')
                        print(f'Part{PEnter}.{list(chapter3)[PEnters]}')
                        print('-'*30)
                        print(list(chapter3.values())[PEnters])
                        print('-'*30)
                        e = input('Press 0 and enter to go back')
                        #e = Exit 
                        if e == '0':
                            break
    return
def BookMenu():
    print('Welcome to Junglebook')
    while True:
        print('1.Read book')
        print('0.Exit')
        Bmenu = input('>>>') #Bmenu = BookMenu
        if Bmenu == bookmenu.ReadBook.value:
            Read_Book()
        elif Bmenu == bookmenu.Exit.value:
            break
    return
BookMenu()