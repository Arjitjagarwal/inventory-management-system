from multiprocessing.connection import address_type
from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry



# Functionality Part

def employee_frame():
    global back_image
    employee_frame = Frame(window, width=1400, height=800, bg='white')
    employee_frame.place(x=200, y=100)
    heading_label = Label(employee_frame, text='Manage Employee Details', font=('times new roman', 20, 'bold'),
                        bg='#ff9933', fg='white')
    heading_label.place(x=0, y=0, relwidth=1)
    back_image = PhotoImage(file='back.png')
    back_button = Button(employee_frame, image=back_image, bd=0, cursor='hand2', bg='white',
                        command=lambda: employee_frame.place_forget())
    back_button.place(x=0, y=50, )

    top_frame = Frame(employee_frame, bg='white', )
    top_frame.place(x=0, y=90, relwidth=1, height=400)
    search_frame = Frame(top_frame, bg='white')
    search_frame.pack()
    search_combobox = ttk.Combobox(search_frame, values=('Id', 'Name', 'Email'), font=('times new roman', 16, 'bold'),
                                state='readonly')
    search_combobox.set('Search by')
    search_combobox.grid(row=0, column=0, padx=20)
    search_entry = Entry(search_frame, font=('times new roman', 12), bg='lightyellow')
    search_entry.grid(row=0, column=1)
    search_button = Button(search_frame, text='SEARCH', font=('times new roman', 12), width=10, cursor='hand2',
                    fg='white', bg='#0039e6')
    search_button.grid(row=0, column=6, padx=20)
    show_button = Button(search_frame, text='Show All', font=('times new roman', 12), width=10, cursor='hand2',
                        fg='white', bg='#0039e6')
    show_button.grid(row=0, column=7,padx=20)


    employee_treeview = ttk.Treeview(top_frame, columns=('empid','name','email','phone no.','gender','dob',
                                                        'employment_type','address','doj',
                                                        'salary','usertype'), show='headings',)

    employee_treeview.pack(pady=10)

    employee_treeview.heading('empid',text='Employee ID')
    employee_treeview.heading('name',text='Name')
    employee_treeview.heading('email',text='Email')
    employee_treeview.heading('phone no.',text='Contact Number')
    employee_treeview.heading('gender',text='Gender')
    employee_treeview.heading('dob',text='Date Of Bith')
    employee_treeview.heading('employment_type',text='Employment Type')
    employee_treeview.heading('address',text='Address')
    employee_treeview.heading('doj',text='Date Of Joining')
    employee_treeview.heading('salary',text='Salary')
    employee_treeview.heading('usertype',text='User Type')



    employee_treeview.column('empid', width=60)
    employee_treeview.column('name', width=140)
    employee_treeview.column('email', width=180)
    employee_treeview.column('phone no.', width=100)
    employee_treeview.column('gender', width=80)
    employee_treeview.column('dob', width=100)
    employee_treeview.column('employment_type', width=120)
    employee_treeview.column('address', width=100)
    employee_treeview.column('doj', width=100)
    employee_treeview.column('salary', width=100)
    employee_treeview.column('usertype', width=120)

    detail_frame=Frame(employee_frame,bg='white')
    detail_frame.place(x=30,y=400)

    empid_label=Label(detail_frame,text='Employee ID:',font=('times new roman', 12, 'bold'),bg='white')
    empid_label.grid(row=0, column=0,padx=10,pady=10)
    empid_entry=Entry(detail_frame,font=('times new roman',12),bg='lightyellow')
    empid_entry.grid(row=0, column=1,padx=10,pady=10)

    name_label = Label(detail_frame, text='Name:', font=('times new roman', 12, 'bold'), bg='white')
    name_label.grid(row=0, column=3, padx=10, pady=10)
    name_entry = Entry(detail_frame, font=('times new roman', 12), bg='lightyellow')
    name_entry.grid(row=0, column=4, padx=10, pady=10)

    email_label = Label(detail_frame, text='Email:', font=('times new roman', 12, 'bold'), bg='white')
    email_label.grid(row=0, column=6, padx=10, pady=10)
    email_entry = Entry(detail_frame, font=('times new roman', 12), bg='lightyellow')
    email_entry.grid(row=0, column=7, padx=10, pady=10)

    gender_label = Label(detail_frame, text='Gender :', font=('times new roman', 12, 'bold'), bg='white')
    gender_label.grid(row=0, column=11, pady=10)

    gender_combobox=ttk.Combobox(detail_frame,value=('Male','Female'),state='readonly')
    gender_combobox.set('Select Gender')
    gender_combobox.grid(row=0, column=12)

    dob_label = Label(detail_frame, text='       Date Of Birth :', font=('times new roman', 12, 'bold'), bg='white')
    dob_label.grid(row=1, column=3, pady=20 )

    dob_label_entry=DateEntry(detail_frame,font=('times new roman', 12),date_pattern='DD/MM/YYYY',bg='white')
    dob_label_entry.grid(row=1, column=4)

    doj_label = Label(detail_frame, text='       Date Of Joining :', font=('times new roman', 12, 'bold'), bg='white')
    doj_label.grid(row=1, column=6, pady=20)

    doj_label_entry = DateEntry(detail_frame, font=('times new roman', 12), date_pattern='DD/MM/YYYY', bg='white')
    doj_label_entry.grid(row=1, column=7)

    contact_label = Label(detail_frame, text='  Contact No. :', font=('times new roman', 12, 'bold'), bg='white')
    contact_label.grid(row=1, column=0)
    contact_entry = Entry(detail_frame, font=('times new roman', 12), bg='lightyellow')
    contact_entry.grid(row=1, column=1)

    employment_type_label = Label(detail_frame, text='Employment Type :', font=('times new roman', 12, 'bold'), bg='white')
    employment_type_label.grid(row=3, column=0, pady=10)

    employment_type_combobox = ttk.Combobox(detail_frame, value=('Full Time', 'Part Time','Intern','Contract','Casual'), state='readonly')
    employment_type_combobox.set('Select Type')
    employment_type_combobox.grid(row=3, column=1)

    eduction_label = Label(detail_frame, text='Eduction :', font=('times new roman', 12, 'bold'), bg='white')
    eduction_label.grid(row=3, column=3, pady=10)

    eduction_label=ttk.Combobox(detail_frame,value=('B.tech','BCA','BBA','B.Com','B.Sc','Deploma','M.Com','M.Sc',),state='readonly')
    eduction_label.set('Select Degree')
    eduction_label.grid(row=3, column=4)

    work_shift_label = Label(detail_frame, text='Work Shift :', font=('times new roman', 12, 'bold'), bg='white')
    work_shift_label.grid(row=1, column=11, pady=10)

    work_shift_combobox = ttk.Combobox(detail_frame, value=('Day', 'Night'), state='readonly')
    work_shift_combobox.set('Select work_shift')
    work_shift_combobox.grid(row=1, column=12)

    address_label= Label(detail_frame, text='Address :', font=('times new roman', 12, 'bold'), bg='white')
    address_label.grid(row=4, column=0, pady=10)
    address_text = Text(detail_frame,width=20,height=3, font=('times new roman', 12), bg='lightyellow')
    address_text.grid(row=4, column=1, padx=10, pady=10)

    salary_type_label = Label(detail_frame, text='Salary :', font=('times new roman', 12, 'bold'),
                                  bg='white')
    salary_type_label.grid(row=3, column=6, pady=10)
    salary_entry = Entry(detail_frame, font=('times new roman', 12), bg='lightyellow')
    salary_entry.grid(row=3, column=7)

    password_type_label = Label(detail_frame, text='Password :', font=('times new roman', 12, 'bold'),
                              bg='white')
    password_type_label.grid(row=3, column=11, pady=10)
    password_entry = Entry(detail_frame, font=('times new roman', 12), bg='lightyellow')
    password_entry.grid(row=3, column=12)

    user_type_label = Label(detail_frame, text='User Type :', font=('times new roman', 12, 'bold'), bg='white')
    user_type_label.grid(row=4, column=2, pady=10)

    user_type_combobox = ttk.Combobox(detail_frame, value=('Day', 'Night'), state='readonly')
    user_type_combobox.set('Select user_type')
    user_type_combobox.grid(row=4, column=3)




window = Tk()
window.title('Inventory Management System | By Arjit Tank')
window.geometry('1530x800+1+3')

bg_Image = PhotoImage(file='inventory-system.png')
tittlelabel = Label(window, image=bg_Image, compound=LEFT, text="  Inventory Management System",
                    font=("Times New Roman", 40, 'bold'), bg='#00008B', fg='white')
tittlelabel.place(x=0, y=0, relwidth=1)

logout_icon = PhotoImage(file='logout.png')
logoutButton = Button(window, image=logout_icon, compound=LEFT, text='Logout', cursor='hand2',
                    font=('times new roman', 20, 'bold'))
logoutButton.place(x=1340, y=10)
subtitleLable = Label(window, text='Welecome Admin\t\t Date:25-07-2025\t\t Time: 10:26:14 AM',
                    font=('times new roman',), bg='#808080', fg='white')
subtitleLable.place(x=0, y=70, relwidth=1)

leftFrame = Frame(window)
leftFrame.place(x=0, y=102, relwidth=200, height=555)

logoImage = PhotoImage(file='inventory.png')
imageLabel = Label(leftFrame, image=logoImage)
imageLabel.grid(row=0, column=0)

menuLabel = Label(leftFrame, text='     Menu      ', font=('times new roman', 20), bg='#009688')
menuLabel.grid()

employee_icon = PhotoImage(file='employees.png')
employee_button = Button(leftFrame, image=employee_icon, compound=LEFT, text='Employee', cursor='hand2',
                        font=('times new roman', 20, 'bold'), command=employee_frame)
employee_button.grid()

Supplier_icon = PhotoImage(file='supplier.png')
Supplier_button = Button(leftFrame, image=Supplier_icon, compound=LEFT, text='Supplier  ', cursor='hand2',
                        font=('times new roman', 20, 'bold'))
Supplier_button.grid()

Category_icon = PhotoImage(file='Category.png')
Category_button = Button(leftFrame, image=Category_icon, compound=LEFT, text='Category ', cursor='hand2',
                        font=('times new roman', 20, 'bold'))
Category_button.grid()

Product_icon = PhotoImage(file='Product.png')
Product_button = Button(leftFrame, image=Product_icon, compound=LEFT, text='Product   ', cursor='hand2',
                        font=('times new roman', 20, 'bold'))
Product_button.grid()

Sales_icon = PhotoImage(file='Sales.png')
Sales_button = Button(leftFrame, image=Sales_icon, compound=LEFT, text=' Sales       ', cursor='hand2',
                    font=('times new roman', 20, 'bold'))
Sales_button.grid()

Exit_icon = PhotoImage(file='Exit.png')
Exit_button = Button(leftFrame, image=employee_icon, compound=LEFT, text='  Exit        ', cursor='hand2',
                    font=('times new roman', 20, 'bold'))
Exit_button.grid()

emp_frame = Frame(window, bg='#90EE90', bd=3, relief=SUNKEN)
emp_frame.place(x=400, y=125, height=170, width=280)
total_emp_icon = PhotoImage(file='total_employee.png')
total_emp_icon_label = Label(emp_frame, image=total_emp_icon, bg='#90EE90')
total_emp_icon_label.place(x=100, y=0)

total_emp_label_label = Label(emp_frame, text='Total Employee', bg='#90EE90', fg='black',
                            font=('times new roman', 15, 'bold'))
total_emp_label_label.place(x=70, y=65)

total_emp_count_label_label = Label(emp_frame, text='0', bg='#90EE90', fg='black', font=('times new roman', 32, 'bold'))
total_emp_count_label_label.place(x=120, y=100)

sup_frame = Frame(window, bg='#00FFFF', bd=3, relief=SUNKEN)
sup_frame.place(x=1000, y=125, height=170, width=280)
total_sup_icon = PhotoImage(file='total suppliers.png')
total_sup_icon_label = Label(sup_frame, image=total_sup_icon, bg='#00FFFF')
total_sup_icon_label.place(x=100, y=0)

total_sup_label_label = Label(sup_frame, text='Total Suppliers', bg='#00FFFF', fg='black',
                            font=('times new roman', 15, 'bold'))
total_sup_label_label.place(x=70, y=70)

total_sup_count_label_label = Label(sup_frame, text='0', bg='#00FFFF', fg='black', font=('times new roman', 32, 'bold'))
total_sup_count_label_label.place(x=120, y=100)

cat_frame = Frame(window, bg='#ff8080', bd=3, relief=SUNKEN)
cat_frame.place(x=400, y=350, height=170, width=280)
total_cat_icon = PhotoImage(file='total categories.png')
total_cat_icon_label = Label(cat_frame, image=total_cat_icon, bg='#ff8080')
total_cat_icon_label.place(x=100, y=0)

total_cat_label_label = Label(cat_frame, text='Total Categories', bg='#ff8080', fg='black',
                            font=('times new roman', 15, 'bold'))
total_cat_label_label.place(x=70, y=70)

total_cat_count_label_label = Label(cat_frame, text='0', bg='#ff8080', fg='black', font=('times new roman', 32, 'bold'))
total_cat_count_label_label.place(x=120, y=100)

pro_frame = Frame(window, bg='#e6ccff', bd=3, relief=SUNKEN)
pro_frame.place(x=1000, y=350, height=170, width=280)
total_pro_icon = PhotoImage(file='total_product.png')
total_pro_icon_label = Label(pro_frame, image=total_pro_icon, bg='#e6ccff')
total_pro_icon_label.place(x=100, y=0)

total_pro_label_label = Label(pro_frame, text='Total Products', bg='#e6ccff', fg='black',
                            font=('times new roman', 15, 'bold'))
total_pro_label_label.place(x=70, y=70)

total_pro_count_label_label = Label(pro_frame, text='0', bg='#e6ccff', fg='black', font=('times new roman', 32, 'bold'))
total_pro_count_label_label.place(x=120, y=100)

sal_frame = Frame(window, bg='#ffb3ff', bd=3, relief=SUNKEN)
sal_frame.place(x=700, y=550, height=170, width=280)
total_sal_icon = PhotoImage(file='total_sales.png')
total_sal_icon_label = Label(sal_frame, image=total_sal_icon, bg='#ffb3ff')
total_sal_icon_label.place(x=100, y=0)

total_sal_label_label = Label(sal_frame, text='Total Sales', bg='#ffb3ff', fg='black',
                            font=('times new roman', 15, 'bold'))
total_sal_label_label.place(x=88, y=75)

total_sal_count_label_label = Label(sal_frame, text='0', bg='#ffb3ff', fg='black', font=('times new roman', 32, 'bold'))
total_sal_count_label_label.place(x=120, y=105)

window.mainloop()
