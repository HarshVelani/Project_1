def main():
    print("Welcome to the Agro Shop Retail Management System !")
    print("1. Worker \n2. Manager")
    c = input("Enter Choice 1/2 : ")
    print("------------------------------------------------------------")

    if c == "1":
        worker()
    elif c == "2":
        # login details for manager
        print("1. Login \n2. Change Password")
        con = input("Enter Choice 1/2 : ")
        print("------------------------------------------------------------")
        if con == '1' :
            # validation of Credentials
            p = input("Enter Password : ")
            with open("password.txt", "r") as psw:
                sec = psw.read()
            
            if sec == p:
                manager()
        elif con == '2':
            # for changing password
            p = input("Enter Password : ")
            with open("password.txt", "r") as psw:
                sec = psw.read()
       
            if sec == p:
                a = 0
                while a == 0:
                    print("New Password should contain either of these Special Characters ( % _ ! @ $ & ) ")
                    pas = input("Enter New Password : ")
                    li = pas.split(",")
                    
                    for l in li:
                        if "_" in l or "!" in l or '@' in l or "$" in l or "&" in l or "%" in l:
                            with open("password.txt", "w") as ps:
                                ps.write(pas)
                                a = 1
                                print("Your New Password has been successfully updated.")
                                break
                        else:
                            a = 0
                else:
                    manager()
            else:
                manager()
        else:
            main()
    else:
        main()


def worker():
    
    print("1. View Products \n2. View Stock \n3. Place Order \n4. View Orders \n5. Go To Main")
    c = input("Enter Choice 1/2/3/4/5 : ")
    print("------------------------------------------------------------")

    if c == '1':
        view_products()
    elif c == '2':
        view_stock()
    elif c == '3':
        place_order() 
    elif c == '4':
        view_orders()  
    elif c == '5':
        main()
    else:
        main()

def manager():

    print("1. Add New Products \n2. Update Stock of Existing Product \n3. Delete Product \n4. View Orders \n5. Edit Order \n6. Delete Order \n7. To Logout")
    c = input("Enter Choice 1/2/3/4/5/6/7 : ")
    if c == '1':
        add_products() 
    elif c == '2':
        update_stock()        
    elif c == '3':
        delete_product()
    elif c == '4':
        view_orders()
    elif c == '5':
        edit_order()
    elif c == '6':
        delete_order()
    elif c == '7':
        main()
    else:
        manager()


# User define function to read csv file and gives output in list of list where each inner list is the row
def read_csv(filepath):
    with open(filepath, "r") as f:
        da = f.readlines()
        main_lis = []
        for line in da:
            line = line.strip()
            line = line.split(",")
            main_lis.append(line)
    return main_lis


# User define function to write csv file same as above
def write_csv(filepath, list_of_list):
    with open(filepath, "w") as g:
        for line in list_of_list:
            line[-1] = str(line[-1])+"\n"
            coma_line = ",".join(line)
            g.write(coma_line)



# User define function to view Stock
def view_stock():

    filepath = "product.csv"
    main_list = read_csv(filepath)

    prod_list = main_list[1::]
    # print(data_list)
    dic = {}
    prod_dic_list = []
    for row in prod_list:
        # for n2, item in enumerate(row):
        dic = {"pid" : row[0],
            "Technical Name" : row[1],
            "Commercial Name" : row[2],
            "Type" : row[3],
            "Packaging" : row[4],
            "Rate per Packing" : row[5],
            "Rate per liter/kg" : row[6],
            "Stock" : row[7]}
        prod_dic_list.append(dic)
    # print(prod_dic_list)

    con = 1
    while con == 1:
        c = input("Enter Product Name : ").lower()
        for item in prod_dic_list:
            te = item.get("Technical Name").lower()
            com = item.get("Commercial Name").lower()
            if te.find(c) == 0 or com.find(c) == 0:

                con =  con + 1
                break
            else:
                con = 1

    print("------------------------------------------------------------")
    for row in prod_dic_list:
        
        if c in row.get("Technical Name").lower() or c in row.get("Commercial Name").lower():
            print("'pid :", row.get("pid"), 
                  "'\n'Technical Name :", row.get("Technical Name"), 
                  "'\n'Commercial Name :", row.get("Commercial Name"), 
                  "'\n'Type :", row.get("Type"), 
                  "'\n'Stock :", row.get("Stock"))
            print("------------------------------------------------------------")
    print("************************************************************")
    main()    

def view_products():
    filepath = "product.csv"
    main_list = read_csv(filepath)

    prod_list = main_list[1::]
    # print(data_list)
    dic = {}
    prod_dic_list = []
    for row in prod_list:
        # for n2, item in enumerate(row):
        dic = {"pid" : row[0],
            "Technical Name" : row[1],
            "Commercial Name" : row[2],
            "Type" : row[3],
            "Packaging" : row[4],
            "Rate per Packing" : row[5],
            "Rate per liter/kg" : row[6],
            "Stock" : row[7]}
        prod_dic_list.append(dic)
    # print(prod_dic_list)

    con = 1
    while con == 1:
        c = input("Enter Product Name : ").lower()
        for item in prod_dic_list:
            te = item.get("Technical Name").lower()
            com = item.get("Commercial Name").lower()
            if te.find(c) == 0 or com.find(c) == 0:
                # print("Invalid Entry!!!")
                con =  con + 1
                break
            else:
                con = 1

    print("------------------------------------------------------------")
    for row in prod_dic_list:
        
        if c in row.get("Technical Name").lower() or c in row.get("Commercial Name").lower():
            print("'pid :", row.get("pid"), 
                "'\n'Technical Name :", row.get("Technical Name"), 
                "'\n'Commercial Name :", row.get("Commercial Name"), 
                "'\n'Type :", row.get("Type"), 
                "'\n'Packaging :", row.get("Packaging"),
                "'\n'Rate per Packing :",  row.get("Rate per Packing"),
                "'\n'Rate per liter/kg :", row.get("Rate per liter/kg"),
                "'\n'Stock :", row.get("Stock"))
            print("------------------------------------------------------------")
    print("************************************************************")
    main()



# add 
def add_products():
    filepath = "product.csv"
    main_list = read_csv(filepath)

    prod_list = main_list[1::]

    dic = {}
    prod_dic_list = []
    for row in prod_list:
        # for n2, item in enumerate(row):
        dic = {"pid" : row[0],
            "Technical Name" : row[1],
            "Commercial Name" : row[2],
            "Type" : row[3],
            "Packaging" : row[4],
            "Rate per Packing" : row[5],
            "Rate per liter/kg" : row[6],
            "Stock" : row[7]}
        prod_dic_list.append(dic)
    # print(prod_dic_list)

    print("Enter Product Name which is similar to existing product")
    con = 1
    while con == 1:
        c = input("Enter Product Name : ").lower()
        for item in prod_dic_list:
            te = item.get("Technical Name").lower()
            com = item.get("Commercial Name").lower()
            if te.find(c) == 0 or com.find(c) == 0:
                # print("Invalid Entry!!!")
                con =  con + 1
                break
            else:
                con = 1 

    print("------------------------------------------------------------")
    for row in prod_dic_list:
        if c in row.get("Technical Name").lower() or c in row.get("Commercial Name").lower():
            print("'pid :", row.get("pid"), 
                "'\n'Technical Name :", row.get("Technical Name"), 
                "'\n'Commercial Name :", row.get("Commercial Name"), 
                "'\n'Type :", row.get("Type"), 
                "'\n'Packaging :", row.get("Packaging"),
                "'\n'Rate per Packing :",  row.get("Rate per Packing"),
                "'\n'Rate per liter/kg :", row.get("Rate per liter/kg"),
                "'\n'Stock :", row.get("Stock"))
            print("------------------------------------------------------------")

    print("Please Check the above list, if the product you want to ADD is present or not")
    print("1. Add \n2. Product Already exists")
    m = int(input("Enter Choice : "))
    if m == 1:
        pass
    elif m == 2:
        manager()
    else:
        manager()


    com_list = []
    for dic in prod_dic_list:
        com_list.append(dic.get("Commercial Name"))


    n = (input("Enter the no. of Products you want to ADD : "))
    n = int(n)
    m = 0

    while m != n:
        pid = int(prod_list[-1][0]) + 1
        tn = input("Enter Technical Name : ")
        cn =  input("Enter Commercial Name : ")

        if cn.lower() not in com_list:
            Type = input("Enter the type of product : ")
            pck =  input("Enter Packaging (x kg/litre) : ")
            r_p_pck =  input("Enter Rate Per Packing : ")
            r_p_kg_l = input("Enter Rate Per kg/litre : ")
            stock = input("Enter No. of Packets : ")
            nl = [str(pid), tn, cn, Type, pck, r_p_pck, r_p_kg_l, stock]

            prod_list.append(nl)
            m+=1
        else:
            print("------------------------------------------------------------")
            print("The product you want to enter already exists")
            print("------------------------------------------------------------")
            break
    # print(prod_list)

    p_list = [["pid","Technical Name","Commercial Name","Type","Packaging","Rate Per Packing","Rate Per liter/kg","Stock"]] + prod_list
    
    file_path = "product.csv"
    write_csv(file_path, p_list)

    print("Your New Product is successfully added to the product list.")
    print("************************************************************")
    manager()



# UPDATE STOCK
def update_stock():
    # Opening Product CSV
    filepath = "product.csv"
    main_list = read_csv(filepath)

    # Excluding the the First Row (Column Names)
    prod_list = main_list[1::]

    # dictionary of (list of Columns of product)
    dic = {}
    prod_dic_list = []
    for row in prod_list:
        dic = {"pid" : row[0],
            "Technical Name" : row[1],
            "Commercial Name" : row[2],
            "Type" : row[3],
            "Packaging" : row[4],
            "Rate per Packing" : row[5],
            "Rate per liter/kg" : row[6],
            "Stock" : row[7]}
        prod_dic_list.append(dic)
    # print(prod_dic_list)

    con = 1
    while con == 1:
        c = input("Enter Product Name : ").lower()
        for item in prod_dic_list:
            te = item.get("Technical Name").lower()
            com = item.get("Commercial Name").lower()
            if te.find(c) == 0 or com.find(c) == 0:
                # print("Invalid Entry!!!")
                con =  con + 1
                break
            else:
                con = 1
                    
            
    print("------------------------------------------------------------")
    for row in prod_dic_list:
        te = row.get("Technical Name").lower()
        com = row.get("Commercial Name").lower()
        if c in te or c in com:
        # if te.find(c) == 0 or com.find(c) == 0:
            print("'pid :", row.get("pid"), 
                "'\n'Technical Name :", row.get("Technical Name"), 
                "'\n'Commercial Name :", row.get("Commercial Name"), 
                "'\n'Type :", row.get("Type"), 
                "'\n'Packaging :", row.get("Packaging"),
                "'\n'Rate per Packing :",  int(row.get("Rate per Packing")),
                "'\n'Rate per liter/kg :", int(row.get("Rate per liter/kg")),
                "'\n'Stock :", row.get("Stock"))
            
            print("------------------------------------------------------------")


    pro_id = int(input("Enter Product ID : "))
    new_stock = int(input("Enter the number of packets/stock you want to add : "))
    for row in prod_dic_list:
        if pro_id == int(row.get("pid")):
            row["Stock"] = int(row.get("Stock")) + new_stock

    p_list = [["pid","Technical Name","Commercial Name","Type","Packaging","Rate Per Packing","Rate Per liter/kg","Stock"]]
        
    for row in prod_dic_list:
        row_l = []
        for val in row.values():
            row_l.append(val)
        p_list.append(row_l)
    # print(p_list)


    filepath = "product.csv"
    write_csv(filepath, p_list)

    print("************************************************************")
    manager()




# DELETE PRODUCT
def delete_product():
    filepath = "product.csv"
    main_list = read_csv(filepath)
    # print(main_lis)

    data_list = main_list[1::]
    # print(data_list)
    dic = {}
    prod_dic_list = []
    for row in data_list:
        dic = {"pid" : row[0],
            "Technical Name" : row[1],
            "Commercial Name" : row[2],
            "Type" : row[3],
            "Packaging" : row[4],
            "Rate per Packing" : row[5],
            "Rate per liter/kg" : row[6],
            "Stock" : row[7]}
        prod_dic_list.append(dic)
    # print(prod_dic_list)

    con = 1
    while con == 1:
        c = input("Enter Product Name : ").lower()
        for item in prod_dic_list:
            te = item.get("Technical Name").lower()
            com = item.get("Commercial Name").lower()
            if te.find(c) == 0 or com.find(c) == 0:
                # print("Invalid Entry!!!")
                con =  con + 1
                break
            else:
                con = 1

    print("------------------------------------------------------------")
    for row in prod_dic_list:
        if c in row.get("Technical Name").lower() or c in row.get("Commercial Name").lower():
            print("'pid :", row.get("pid"), 
                "'\n'Technical Name :", row.get("Technical Name"), 
                "'\n'Commercial Name :", row.get("Commercial Name"), 
                "'\n'Type :", row.get("Type"), 
                "'\n'Packaging :", row.get("Packaging"),
                "'\n'Rate per Packing :",  row.get("Rate per Packing"),
                "'\n'Rate per liter/kg :", row.get("Rate per liter/kg"),
                "'\n'Stock :", row.get("Stock"))
            print("------------------------------------------------------------")
    pro_id = int(input("Enter Product ID : "))

    for index, row in enumerate(prod_dic_list):
        if pro_id == int(row.get("pid")):
            del prod_dic_list[index]
    
    pro_list = []
    for row in prod_dic_list:
        row_l = []
        for val in row.values():
            row_l.append(val)
        pro_list.append(row_l)
    # print(p_list)

    p_list = [["pid","Technical Name","Commercial Name","Type","Packaging","Rate Per Packing","Rate Per liter/kg","Stock"]] + pro_list
    
    filepath = "product.csv"
    write_csv(filepath, p_list)

    print("************************************************************")
    manager()



# BUY
def place_order():
    from datetime import datetime, date

    # Opening Product CSV
    filepath = "product.csv"
    main_list = read_csv(filepath)

    # Excluding the the First Row (Column Names)
    prod_list = main_list[1::]
    # print(prod_list)


    # dictionary of (list of Columns of product)
    dic = {}
    prod_dic_list = []
    for row in prod_list:
        dic = {"pid" : row[0],
            "Technical Name" : row[1],
            "Commercial Name" : row[2],
            "Type" : row[3],
            "Packaging" : row[4],
            "Rate per Packing" : row[5],
            "Rate per liter/kg" : row[6],
            "Stock" : row[7]}
        prod_dic_list.append(dic)


    # Opening Order CSV
    filepath1 = "order.csv"
    o_list = read_csv(filepath1)

    ord_list = o_list[1::]
    # print(ord_list)

    print("Please Enter Personal Information Of Customer")
    # Collecting Details for order
    ord_num = int(ord_list[-1][0]) + 1
    sr_no = 1
    current_date = date.today()
    # print(str(current_date))
    first_name = input("Enter Customer's First Name : ")
    last_name = input("Enter Customer's Last Name : ")
    address = input("Enter Address : ")

    # Condition for Contact number
    con = 1
    while con == 1:
        contact_no = int(input("Enter Contact Number : "))  
        if len(str(contact_no)) != 10:
                print("!!! Invalid Phone Number !!!")
                continue
        con = con + 2

    total_price_per_order = 0
    codn = 1
    while codn != 2:
        
        current_time = datetime.now().strftime("%H:%M:%S")
        
        con = 1
        while con == 1:
            c = input("Enter Product Name : ").lower()
            for item in prod_dic_list:
                te = item.get("Technical Name").lower()
                com = item.get("Commercial Name").lower()
                if te.find(c) == 0 or com.find(c) == 0:
                    # print("Invalid Entry!!!")
                    con =  con + 1
                    break
                else:
                    con = 1   
                
        print("------------------------------------------------------------")
        for row in prod_dic_list:
            te = row.get("Technical Name").lower()
            com = row.get("Commercial Name").lower()
            if c in te or c in com:
            # if te.find(c) == 0 or com.find(c) == 0:
                print("'pid :", row.get("pid"), 
                    "'\n'Technical Name :", row.get("Technical Name"), 
                    "'\n'Commercial Name :", row.get("Commercial Name"), 
                    "'\n'Type :", row.get("Type"), 
                    "'\n'Packaging :", row.get("Packaging"),
                    "'\n'Rate per Packing :",  int(row.get("Rate per Packing")),
                    "'\n'Rate per liter/kg :", int(row.get("Rate per liter/kg")))
                
                print("------------------------------------------------------------")


        pro_id = int(input("Enter Product ID : "))

        for row in prod_dic_list:
            if pro_id == int(row.get("pid")):
                pid = row.get("pid")
                tn = row.get("Technical Name")
                cn = row.get("Commercial Name")
                Type = row.get("Type")
                pck = row.get("Packaging")
                r_p_pck =  int(row.get("Rate per Packing"))
                r_p_kg_l = int(row.get("Rate per liter/kg"))
                no_of_packs = int(input("Enter the No. of Packings to Purchase : "))

                if no_of_packs > int(row.get("Stock")):
                    print("NOT Enough Stock!!")
                    s = row.get("Stock")
                    print(f"There are {s} number of packings for the entered product.")    
                    sr_no = sr_no - 1
                    break
                row["Stock"] = int(row.get("Stock")) - no_of_packs

                t_price_per_prod = (int(row.get("Rate per Packing")))*int(no_of_packs)
                nl = [str(ord_num), str(sr_no), str(current_date), str(current_time), first_name, last_name, address, str(contact_no), str(pid), tn, cn, Type, pck, str(r_p_pck), str(r_p_kg_l), str(no_of_packs), str(t_price_per_prod), "NA"]
                total_price_per_order = total_price_per_order + int(t_price_per_prod)
                ord_list.append(nl)
        
        sr_no = sr_no + 1
        print("Enter Choice :\n1. Buy \n2. Quit")
        codn = int(input("Enter 1 OR 2 : "))
    ord_list[-1][-1] = str(total_price_per_order)

    ord_list = [["Order Id","Sr. No.","Date of Purchase","Time of Purchase","First Name","Last Name","Address","Contact No","pid","Technical Name","Commercial Nam","Type","Packaging","Rate per Packing","Rate per liter/kg","No. of Packings purchased","Total price","Grand Total"]] + ord_list

    filepath1 = "order.csv"
    write_csv(filepath1, ord_list)

    # print("------------------------------------------------------------")
    p_list = [["pid","Technical Name","Commercial Name","Type","Packaging","Rate Per Packing","Rate Per liter/kg","Stock"]]
    
    for row in prod_dic_list:
        row_l = []
        for val in row.values():
            row_l.append(val)
        p_list.append(row_l)
    # print(p_list)
    print("------------------------------------------------------------")
    
    filepath = "product.csv"
    write_csv(filepath, p_list)

    print("Your Order is Successfully Placed.\nThank You for choosing us.")
    print("************************************************************")
    main()



# check ORDERS
def view_orders():
    
    # Opening Order CSV
    filepath1 = "order.csv"
    o_list = read_csv(filepath1)

    ord_list = o_list[1::]
    # print(ord_list)

    # Data Frame for Order CSV
    ord_dic = {}
    ord_dic_list = []
    for row in ord_list:
        ord_dic = {"Order Id" : row[0], 
                "Sr. No." : row[1],
                "Date of Purchase" : row[2],
                "Time of Purchase" : row[3],
                "First Name" : row[4],
                "Last Name" : row[5],
                "Address" : row[6],
                "Contact No." : row[7],                                                  # To add farmers Name, Address, Contact no., Date of Order/Purchase
                "pid" : row[8],
                "Technical Name" : row[9],
                "Commercial Name" : row[10],
                "Type" : row[11],
                "Packaging" : row[12],
                "Rate per Packing" : row[13],
                "Rate per liter/kg" : row[14],
                "No. of Packings purchased" : row[15],
                "Total Price" : row[16],
                "Grand Total" : row[17]}
        ord_dic_list.append(ord_dic)
    # print(ord_dic_list)

    # Condition For Validating Farmer's Name in Order list
    con = 1
    while con == 1:
        c = input("Enter Customer's Name : ").lower()
        for row in ord_dic_list:
            fname = row.get("First Name").lower()
            lname = row.get("Last Name").lower()
            # if c in row.get("Technical Name").lower() or c in row.get("Commercial Name").lower():
            if fname.find(c) == 0 or lname.find(c) == 0:
                # print("Invalid Name!!!")
                con =  con + 1
                break
            else:
                con = 1
    print("------------------------------------------------------------")
    # View Farmer and Order Information
    for row in ord_dic_list:
        
        te = row.get("First Name").lower()
        com = row.get("Last Name").lower()
        # if c in row.get("Technical Name").lower() or c in row.get("Commercial Name").lower():
        if te.find(c) == 0 or com.find(c) == 0:
            
            print("'Order Id :", row.get("Order Id"),
                "\nSr. No. : ", row.get("Sr. No."),
                "\nDate of Purchase : ", row.get("Date of Purchase"),
                "\nTime of Purchase : ", row.get("Time of Purchase"),
                "\nFirst Name : ", row.get("First Name"),
                "\nLast Name : ", row.get("Last Name"),
                "\nAddress : ", row.get("Address"),
                "\nContact No. : ", row.get("Contact No."))
            print("------------------------------------------------------------")

    print("Please Confirm the Customer name and Enter Order ID to view Whole Information")
    ord_id = input("Enter Order ID : ")

    print("------------------------------------------------------------")
    # View Order Details
    for row in ord_dic_list:
        if ord_id == row.get("Order Id"):
            
            print("'Order Id :", row.get("Order Id"),
                "\nSr. No. :", row.get("Sr. No."),
                "\nDate of Purchase :", row.get("Date of Purchase"),
                "\nTime of Purchase :", row.get("Time of Purchase"),
                "\nFirst Name :", row.get("First Name"),
                "\nLast Name :", row.get("Last Name"),
                "\nAddress :", row.get("Address"),
                "\nContact No. :", row.get("Contact No."),
                "\npid :", row.get("pid"),
                "\nTechnical Name :", row.get("Technical Name"),
                "\nCommercial Name :", row.get("Commercial Name"),
                "\nType :", row.get("Type"),
                "\nPackaging :", row.get("Packaging"),
                "\nRate per Packing :", row.get("Rate per Packing"),
                "\nRate per liter/kg :", row.get("Rate per liter/kg"),
                "\nNo. of Packings purchased :", row.get("No. of Packings purchased"),
                "\nTotal price per product :", row.get("Total Price"))
            print("------------------------------------------------------------")
            if row.get("Grand Total").isdigit():
                print("GRAND TOTAL :",int(row.get("Grand Total")))

    print("************************************************************")
    main()



# EDIT ORDERS
def edit_order():

    from datetime import datetime, date
    # Opening Order CSV
    filepath1 = "order.csv"
    o_list = read_csv(filepath1)

    ord_list = o_list[1::]
    # print(ord_list)

    # Data Frame for Order CSV
    ord_dic = {}
    ord_dic_list = []
    for row in ord_list:
        ord_dic = {"Order Id" : row[0], 
                "Sr. No." : row[1],
                "Date of Purchase" : row[2],
                "Time of Purchase" : row[3],
                "First Name" : row[4],
                "Last Name" : row[5],
                "Address" : row[6],
                "Contact No." : row[7],                                                  # To add farmers Name, Address, Contact no., Date of Order/Purchase
                "pid" : row[8],
                "Technical Name" : row[9],
                "Commercial Name" : row[10],
                "Type" : row[11],
                "Packaging" : row[12],
                "Rate per Packing" : row[13],
                "Rate per liter/kg" : row[14],
                "No. of Packings purchased" : row[15],
                "Total Price" : row[16],
                "Grand Total" : row[17]}
        ord_dic_list.append(ord_dic)


    print("To Edit Order, Select the number accordingly from below options")
    print("1. Personal Information\n2. Return Products")
    opt = int(input("Enter the number : "))
    print("------------------------------------------------------------")
    print("Please Enter the below Information")
    old_fname = input("Enter the old First Name : ").lower()
    old_lname = input("Enter the old Last Name : ").lower()
    print("------------------------------------------------------------")
    if opt == 1:
        nfirstname = input("Enter new First Name : ")
        nlastname = input("Enter new Last Name : ")

        # Condition for Contact number
        con = 1
        while con == 1:
            contact_num = int(input("Enter Contact Number : "))  
            if len(str(contact_num)) != 10:
                    print("!!! Invalid Phone Number !!!")
                    continue
            con = con + 2
        address = input("Enter the new address : ")

        # Condition For Validating Farmer's Name in Order list
        while con == 1:
            c = input("Enter Product Name : ").lower()
            for row in ord_dic_list:
                fname = row.get("First Name").lower()
                lname = row.get("Last Name").lower()
                # if c in row.get("Technical Name").lower() or c in row.get("Commercial Name").lower():
                if fname.find(old_fname) == 0 and lname.find(old_lname) == 0:
                    # print("Invalid Entry!!!")
                    con =  con + 1
                    break
                else:
                    con = 1
        print("------------------------------------------------------------")
        # View Farmer and Order Information
        for row in ord_dic_list:
            
            fname = row.get("First Name").lower()
            lname = row.get("Last Name").lower()
            # if c in row.get("Technical Name").lower() or c in row.get("Commercial Name").lower():
            if fname.find(old_fname) == 0 and lname.find(old_lname) == 0:
                print("'Order Id :", row.get("Order Id"),
                    "\nSr. No. : ", row.get("Sr. No."),
                    "\nDate of Purchase : ", row.get("Date of Purchase"),
                    "\nTime of Purchase : ", row.get("Time of Purchase"),
                    "\nFirst Name : ", row.get("First Name"),
                    "\nLast Name : ", row.get("Last Name"),
                    "\nAddress : ", row.get("Address"),
                    "\nContact No. : ", row.get("Contact No."))
                print("------------------------------------------------------------")
        ord_id = int(input("Enter Order ID : "))

        # Editing Farmer Information
        for row in ord_dic_list:
            if ord_id == int(row.get("Order Id")):
                current_date = date.today()
                current_time = datetime.now().strftime("%H:%M:%S")
                row["Date of Purchase"] = str(current_date)
                row["Time of Purchase"] = str(current_time)
                row["First Name"] = nfirstname
                row["Last Name"] = nlastname
                row["Address"] = address
                row["Contact No."] = str(contact_num)

        # print(ord_dic_list)
        o_list = []
        for row in ord_dic_list:
            row_l = []
            for val in row.values():
                row_l.append(val)
            o_list.append(row_l)
        # print(o_list)

        o_list = [["Order Id","Sr. No.","Date of Purchase","Time of Purchase","First Name","Last Name","Address","Contact No","pid","Technical Name","Commercial Nam","Type","Packaging","Rate per Packing","Rate per liter/kg","No. of Packings purchased","Total price","Grand Total"]] + o_list
        # print(ord_list)
        
        filepath1 = "order.csv"
        write_csv(filepath1, o_list)

        print("Your New Information is Successfully Updated")


    elif opt == 2:

        # Condition For Validating Farmer's Name in Order list
        con = 1
        while con == 1:
            # c = input("Enter Product Name : ").lower()
            for row in ord_dic_list:
                fname = row.get("First Name").lower()
                lname = row.get("Last Name").lower()
                # if c in row.get("Technical Name").lower() or c in row.get("Commercial Name").lower():
                if fname.find(old_fname) == 0 and lname.find(old_lname) == 0:
                    # print("Invalid Entry!!!")
                    con =  con + 1
                    break
                else:
                    con = 1
        print("------------------------------------------------------------")
        # View Farmer and Order Information
        for row in ord_dic_list:
            fname = row.get("First Name").lower()
            lname = row.get("Last Name").lower()
            # if c in row.get("Technical Name").lower() or c in row.get("Commercial Name").lower():
            if fname.find(old_fname) == 0 and lname.find(old_lname) == 0:
                print("'Order Id :", row.get("Order Id"),
                    "'\n'Sr. No. :", row.get("Sr. No."),
                    "\nDate of Purchase :", row.get("Date of Purchase"),
                    "\nTime of Purchase :", row.get("Time of Purchase"),
                    "\nFirst Name :", row.get("First Name"),
                    "\nLast Name :", row.get("Last Name"),
                    "\nAddress :", row.get("Address"),
                    "\nContact No. :", row.get("Contact No."),
                    "\npid :", row.get("pid"),
                    "\nTechnical Name :", row.get("Technical Name"),
                    "\nCommercial Name :", row.get("Commercial Name"),
                    "\nType :", row.get("Type"),
                    "\nPackaging :", row.get("Packaging"),
                    "\nRate per Packing :", row.get("Rate per Packing"),
                    "\nRate per liter/kg :", row.get("Rate per liter/kg"),
                    "\nNo. of Packings purchased :", row.get("No. of Packings purchased"),
                    "\nTotal price per product :", row.get("Total Price"))
                print("------------------------------------------------------------")
                if row.get("Grand Total").isdigit():
                    print("GRAND TOTAL :",int(row.get("Grand Total")))
                print("------------------------------------------------------------")
        # Editing the Products bought
        ord_id = int(input("Enter Order ID : "))
        sr_no = int(input("Enter Sr. No. : "))
        no_of_pac_return = int(input("Enter the number packings returned : "))

        for row in ord_dic_list:
            if ord_id == int(row.get("Order Id")) and sr_no == int(row.get("Sr. No.")):
                
                prod_id = int(row.get("pid"))
                
                npp = int(row.get("No. of Packings purchased")) - no_of_pac_return
                row["No. of Packings purchased"] = str(npp)

                tp = int(row.get("Rate per Packing")) * int(row.get("No. of Packings purchased"))
                row["Total Price"] = str(tp)

        
        total_price_per_order = 0
        for row in ord_dic_list:
            if ord_id == int(row.get("Order Id")):
                total_price_per_order = total_price_per_order + int(row.get("Total Price"))
                s_no = int(row.get("Sr. No."))

        for row in ord_dic_list:
            if ord_id == int(row.get("Order Id")) :
                if row.get("Grand Total").isdigit():
                    row["Grand Total"] = str(total_price_per_order)
        
        # print(ord_dic_list)
        o_list = []
        for row in ord_dic_list:
            row_l = []
            for val in row.values():
                row_l.append(val)
            o_list.append(row_l)
        # print(o_list)

        ord_list = [["Order Id","Sr. No.","Date of Purchase","Time of Purchase","First Name","Last Name","Address","Contact No","pid","Technical Name","Commercial Nam","Type","Packaging","Rate per Packing","Rate per liter/kg","No. of Packings purchased","Total price","Grand Total"]] + o_list
        # print(ord_list)

        filepath1 = "Final_Project\order.csv"
        write_csv(filepath1, ord_list)

        # Opening Product CSV
        filepath = "product.csv"
        main_list = read_csv(filepath)
        
        # Excluding the the First Row (Column Names)
        prod_list = main_list[1::]
            # print(prod_list)


        # dictionary of (list of Columns of product)
        dic = {}
        prod_dic_list = []
        for row in prod_list:
            dic = {"pid" : row[0],
                "Technical Name" : row[1],
                "Commercial Name" : row[2],
                "Type" : row[3],
                "Packaging" : row[4],
                "Rate per Packing" : row[5],
                "Rate per liter/kg" : row[6],
                "Stock" : row[7]}
            prod_dic_list.append(dic)    
        
        for row in prod_dic_list:
            if int(row.get("pid")) == prod_id:
                stk = int(row.get("Stock")) + int(no_of_pac_return)
                row["Stock"] = stk

        p_list = [["pid","Technical Name","Commercial Name","Type","Packaging","Rate Per Packing","Rate Per liter/kg","Stock"]]
            
        for row in prod_dic_list:
            row_l = []
            for val in row.values():
                row_l.append(val)
            p_list.append(row_l)
        # print(p_list)
        print("------------------------------------------------------------")

        filepath = "product.csv"
        write_csv(filepath, p_list)

        print("Your Order is Successfully Updated")

        
    print("************************************************************")
    main()





# DELETE ORDER
def delete_order():
    
    # Opening Product CSV
    filepath = "product.csv"
    main_list = read_csv(filepath)

    # Excluding the the First Row (Column Names)
    prod_list = main_list[1::]

    # Opening Order CSV
    filepath1 = "order.csv"
    o_list = read_csv(filepath1)

    ord_list = o_list[1::]

    # Data Frame for Order CSV
    ord_dic = {}
    ord_dic_list = []
    for row in ord_list:
        ord_dic = {"Order Id" : row[0], 
                "Sr. No." : row[1],
                "Date of Purchase" : row[2],
                "Time of Purchase" : row[3],
                "First Name" : row[4],
                "Last Name" : row[5],
                "Address" : row[6],
                "Contact No." : row[7],                                                  # To add farmers Name, Address, Contact no., Date of Order/Purchase
                "pid" : row[8],
                "Technical Name" : row[9],
                "Commercial Name" : row[10],
                "Type" : row[11],
                "Packaging" : row[12],
                "Rate per Packing" : row[13],
                "Rate per liter/kg" : row[14],
                "No. of Packings purchased" : row[15],
                "Total Price" : row[16],
                "Grand Total" : row[17]}
        ord_dic_list.append(ord_dic)
    # print(ord_dic_list)


    # Condition For Validating Farmer's Name in Order list
    con = 1
    while con == 1:
        c = input("Enter Customer's Name : ").lower()
        for item in ord_dic_list:
            f_name = item.get("First Name").lower()
            l_name = item.get("Last Name").lower()
            if f_name.find(c) == 0 or l_name.find(c) == 0:
                # print("Invalid Name!!!")
                con =  con + 1 
                break
            else:
                con = 1
                
    print("------------------------------------------------------------")
    # View Farmer and Order Information
    for row in ord_dic_list:
        fname = row.get("First Name").lower()
        lname = row.get("Last Name").lower()
        # if c in row.get("Technical Name").lower() or c in row.get("Commercial Name").lower():
        if fname.find(c) == 0 or lname.find(c) == 0:
            print("'Order Id :", row.get("Order Id"),
                "'\n'Sr. No. : ", row.get("Sr. No."),
                "'\n'Date of Purchase : ", row.get("Date of Purchase"),
                "'\n'Time of Purchase : ", row.get("Time of Purchase"),
                "'\n'First Name : ", row.get("First Name"),
                "'\n'Last Name : ", row.get("Last Name"),
                "'\n'Address : ", row.get("Address"),
                "'\n'Contact No. : ", row.get("Contact No."),
                "'\n'pid :", row.get("pid"),
                "'\n'Technical Name :", row.get("Technical Name"),
                "'\n'Commercial Name :", row.get("Commercial Name"),
                "'\n'Type :", row.get("Type"),
                "'\n'Packaging :", row.get("Packaging"),
                "'\n'Rate per Packing :", row.get("Rate per Packing"),
                "'\n'Rate per liter/kg :", row.get("Rate per liter/kg"),
                "'\n'No. of Packings purchased :", row.get("No. of Packings purchased"),
                "'\n'Total price per product :", row.get("Total Price"))
            print("------------------------------------------------------------")
            if row.get("Grand Total").isdigit():
                print("GRAND TOTAL :",int(row.get("Grand Total")))
            print("------------------------------------------------------------")

    ord_id = int(input("Enter Order ID : "))


    o_list = []
    for row in ord_dic_list:
        row_l = []
        for val in row.values():
            row_l.append(val)
        o_list.append(row_l)

    s = 0
    num_of_packs_l = []
    prod_id_l = []
    while s == 0:
        for index,lis in enumerate(o_list):
            if ord_id == int(lis[0]):
                prod_id_l.append(lis[8])
                num_of_packs_l.append(lis[-3])
                del o_list[index]
                s = 0
                break
        else:
            s = s + 1


    ord_list = [["Order Id","Sr. No.","Date of Purchase","Time of Purchase","First Name","Last Name","Address","Contact No","pid","Technical Name","Commercial Nam","Type","Packaging","Rate per Packing","Rate per liter/kg","No. of Packings purchased","Total price","Grand Total"]] + o_list

    filepath1 = "order.csv"
    write_csv(filepath1, ord_list)

    s = 0
    while s == 0:
        for i in range(len(prod_id_l)):
            for index,lis in enumerate(prod_list):
                if int(prod_id_l[i]) == int(lis[0]):
                    lis[-1] = int(lis[-1]) + int(num_of_packs_l[i])
        else:
            s = s + 1     
    # print(prod_list)
    prod_list = [["pid","Technical Name","Commercial Name","Type","Packaging","Rate Per Packing","Rate Per liter/kg","Stock"]] + prod_list

    filepath = "product.csv"
    write_csv(filepath, prod_list)
    
    print("Order has been successfully deleted.")
    print("************************************************************")
    manager()