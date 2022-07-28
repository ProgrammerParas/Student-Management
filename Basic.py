import mysql.connector as ms

default_database = "student_management"

con = ms.connect(
    host="localhost",
    user="root",
    password="",
    database=None
)

cur = con.cursor()
print(r"""
███████╗████████╗██╗   ██╗██████╗ ███████╗███╗   ██╗████████╗    ███╗   ███╗ █████╗ ███╗   ██╗ ██████╗ ███████╗███╗   ███╗███████╗███╗   ██╗████████╗
██╔════╝╚══██╔══╝██║   ██║██╔══██╗██╔════╝████╗  ██║╚══██╔══╝    ████╗ ████║██╔══██╗████╗  ██║██╔════╝ ██╔════╝████╗ ████║██╔════╝████╗  ██║╚══██╔══╝
███████╗   ██║   ██║   ██║██║  ██║█████╗  ██╔██╗ ██║   ██║       ██╔████╔██║███████║██╔██╗ ██║██║  ███╗█████╗  ██╔████╔██║█████╗  ██╔██╗ ██║   ██║   
╚════██║   ██║   ██║   ██║██║  ██║██╔══╝  ██║╚██╗██║   ██║       ██║╚██╔╝██║██╔══██║██║╚██╗██║██║   ██║██╔══╝  ██║╚██╔╝██║██╔══╝  ██║╚██╗██║   ██║   
███████║   ██║   ╚██████╔╝██████╔╝███████╗██║ ╚████║   ██║       ██║ ╚═╝ ██║██║  ██║██║ ╚████║╚██████╔╝███████╗██║ ╚═╝ ██║███████╗██║ ╚████║   ██║   
╚══════╝   ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝   ╚═╝       ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝   
                                                                                                                                                     
""")
if con.is_connected():
    print("Database Connected")
else:
    print("Connection Error")
while True:
    def choices():
        print("\n")
        print("[1]:- To Add Student")
        print("[2]:- To See All Student Data")
        print("[4]:- To Edit")
        print("[5]:- To Delete Data")
        print("[6]:- To Search Science Stream")
        print("[7]:- To Serach Commerce")
        print("[8]:- To Search Humanities")
        print("[9]:- DANGER ZONE:- Format Data")
        print("[10]:- To Create New Data")
        print("[0]:- To Exit")
    choices()
    choice = input("\nEnter Your Choice: ")

    def add_student():
        urollno = input("Enter Roll No.: ")
        if urollno.isnumeric():
            ufname = input("Enter Father Name: ")
            if ufname.isalpha():
                umname = input("Enter Mother Name: ")
                usname = input("Enter Student Name: ")
                udob = input("Enter Date Of Birth: ")
                ugen = input("Enter Gender: ")
                ustream = input("Enter Stream: ")
                cquery = "INSERT INTO student_data(rollno, fname, mname, sname, dob, gender, stream) VALUES({}, '{}', '{}', '{}', '{}', '{}', '{}')".format(
                    urollno, ufname, umname, usname, udob, ugen, ustream)
                cquery2 = "SELECT * FROM student_data"
                cur.execute(cquery, cquery2)
                con.commit()
                print("STUDENT ADDED")
            else:
                print("Inavalid")
        else:
            print("Invalid")

    def view_sdata():
        q2 = "SELECT * FROM student_data"
        cur.execute(q2)
        result = cur.fetchall()
        for i2 in result:
            for j in i2:
                print(j, end=" | ")

    def data_edit():
        c4 = input("Enter Student Roll No.: ")
        print("R FOR ROLL NO")
        print("S FOR Student Name")
        print("D FOR DOB")
        print("St FOR Stream")
        print('Father Name, Mother Name & Gender Are Not Editable')
        c4c = input("ENTER TO CONTINUE: ")
        if c4c == 'R':
            nr = input("Enter New Roll No.: ")
            rq = "UPDATE student_data SET Rollno = %s WHERE Rollno = %s"
            c4q = (nr, c4)
            cur.execute(rq, c4q)
            con.commit()
            print("ROLL NO UPDATED")
        if c4c == 'S':
            nsn = input("Enter New Name: ")
            rn = "UPDATE student_data SET Rollno = %s WHERE Rollno = %s"
            c5q = (nsn, rn)
            cur.execute(rq, c4q)
            con.commit()
            print("NAME UPDATED")
        if c4c == 'D':
            ndob = input("Enter New Date Of Birth: ")
            rdq = "UPDATE student_data SET Rollno = %s WHERE Rollno = %s"
            c6q = (ndob, rdq)
            cur.execute(rq, c6q)
            con.commit()
            print("DOB UPDATED")
        if c4c == 'St':
            nst = input("Enter New Stream: ")
            rstq = "UPDATE student_data SET Rollno = %s WHERE Rollno = %s"
            c7q = (nr, c4)
            cur.execute(rq, c7q)
            con.commit()
            print("STREAM UPDATED")

    def delete_s_data():
        showdeldata = input("Want To See Student List? (Y/N): ")
        if showdeldata == 'Y':
            showdeldataq = "SELECT * FROM student_data"
            cur.execute(showdeldataq)
            for deldata in cur:
                print(deldata)
            din = input("Enter Roll No.: ")
            delete_choice = input("DO YOU WANT TO CONTINUE? (Y/N): ")
            if din not in cur:
                print("Student Not Found")
            else:
                if delete_choice == 'Y':
                    dquery = "DELETE FROM student_data WHERE Rollno=%s"
                    val = (din)
                    cur.execute(dquery)
                    print("STUDENT DELTED")
                else:
                    print("Cancelled")
        else:
            din = input("Enter Roll No.: ")
            delete_choice = input("Confirm? (Y/N): ")
            if delete_choice == 'Y':
                dquery = "DELETE FROM student_data WHERE Rollno=%s"
                val = (din)
                cur.execute(dquery)
                print("STUDENT DELTED")
            else:
                print("Cancelled")

    def search_sci():
        c6query = "SELECT * FROM student_data WHERE Stream = 'Science'"
        cur.execute(c6query)
        results6 = cur.fetchall()
        if 'Science' not in cur:
            print("Science Stream Is Empty")
        for i6 in results6:
            print(i6)

    def search_com():
        c7query = "SELECT * FROM student_data WHERE Stream = 'Commerce'"
        cur.execute(c7query)
        results7 = cur.fetchall()
        if 'Commerce' not in cur:
            print("Commerce Stream Is Empty")
        for i7 in results7:
            print(i7)

    def search_hum():
        c8query = "SELECT * FROM student_data WHERE Stream = 'Humanities'"
        cur.execute(c8query)
        results8 = cur.fetchall()
        if 'Humanities' not in cur:
            print("Humanities Stream Is Empty")
        for i8 in results8:
            print(i8)

    def format_s_data():
        confirm_format = input("DO YOU WANT TO CONTINUE? (Y/N): ")
        if confirm_format == 'Y':
            formatq = "DELETE FROM student_data"
            cur.execute(formatq)
            print("Data Formatted")
        else:
            print("Cancelled")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_sdata()
    elif choice == '4':
        data_edit()
    elif choice == '5':
        delete_s_data()
    elif choice == '6':
        search_sci()
    elif choice == '7':
        search_com()
    elif choice == '8':
        search_hum()
    elif choice == '9':
        format_s_data()
    elif choice == '0':
        print('Goodbye!')
        break
    else:
        print('Invalid Choice')
