################Library Management System (Without Functions)#####################

print("################Library Management System (Without Functions)#####################")

books = {}

while True:
    print("\n========== LIBRARY MENU ==========")
    print("1. Add Book")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Search Book")
    print("5. Display Books")
    print("6. Exit")

    choice = int(input("Enter your choice :"))

    if choice == 1 :
        book = input("Enter your book").strip().title()

        if book in books:
            print("\nBook already avaialble")
        else :
            books[book]="available"
            print(book,"Added successfully.")

    elif choice == 2:
        book =   input("Enter your book").strip().title()   

        if book in books :
            if books[book] == "Borrowed" :
             print("Book already borrowed") 
            else :
              books[book]="Borrowed"  
              print(book,"Alloted to") 

    elif choice==3:
        book = input("Enter the name of the book you want to return").strip().title()

        if book not in books:
             print("Book not found")
        elif books[book]== "Borrowed":
            books[book]="available"
            print(book,"Returned successfully")
        elif books[book]=="available" :
            print("Error! This book was not borrowed.")  

    elif choice==4:
        book = input("Enter the name of the book you want to search").strip().title()
        try :
            if book in books:
                print(book,"is available in the bank.")
        except Exception:
                    print(book,"is not available in the bank.")
        else:
                print(book,"is not available in the bank.")

    elif choice==5:
                print("List of vailable books  in the bank.")
                print(books)
    elif choice==6:
                    print("Exiting from the bank.")
                    break 
            
    else :
        print("Invalid choice. Please try again")


