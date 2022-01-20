#!/usr/bin/env python
# coding: utf-8

# In[1]:


def show_menu():
    print ("="*50)
    print (" "*20+"MY BAZAAR"+" "*20)
    print ("="*50)
    print ("Hello! Welcome to my grocery store")
    print ("Following are the products available in the shop:")
    print (" ")
    print ("-"*50)
    print (" CODE | DESCRIPTION | CATEGORY    | COST (Rs)")
    print (" 0    | Tshirt      | Apparels    | 500      ")
    print (" 1    | Trousers    | Apparels    | 600      ")
    print (" 2    | Scarf       | Apparels    | 250      ")
    print (" 3    | Smartphone  | Electronics | 20000    ")
    print (" 4    | iPad        | Electronics | 30000    ")
    print (" 5    | Laptop      | Electronics | 50000    ")
    print (" 6    | Eggs        | Eatables    | 5        ")
    print (" 7    | Chocolate   | Eatables    | 10       ")
    print (" 8    | Juice       | Eatables    | 100      ")
    print (" 9    | Milk        | Eatables    | 45       ")
    print ("-"*50)   


# In[ ]:





# In[2]:


def get_regular_input():
    print ("-"*50)
    print ("ENTER ITEMS YOU WISH TO BUY")
    print ("-"*50)
    n=(input("Enter the item codes (space-separated):"))
    global l
    l=[]
    for i in range (0,len(n)):
        if n[i]==" ":
            continue
        else:
            l.append (int(n[i]))
    l1=[0,0,0,0,0,0,0,0,0,0]
    for i in range (0,len(l)):
        if l[i]>=0 and l[i]<10:
            l1[l[i]]=l1[l[i]]+1
        else:
            print ("Error")
    return l1
    


# In[3]:


def print_order_details(quantities):
    print ("-"*50)
    print ("ORDER DETAILS")
    print ("-"*50)
#     print (quantities)
    count=0
    tc=0
    for i in range (len(quantities)):
        if quantities[i]!=0:
            tc=tc+(cost[i]*quantities[i])
            count=count+1
            print ("["+str(count)+"] "+description[i]+" x "+str(quantities[i])+" = Rs "+str(cost[i])+" * "+str(quantities[i])+" = Rs "+str(cost[i]*quantities[i]))
    print ()
    print ("TOTAL COST = Rs ",tc)
    
    
    


# In[4]:


def calculate_category_wise_cost(quantities):
    print ("-"*50)
    print ("CATEGORY-WISE COST")
    print ("-"*50)
    a=0
    b=0
    c=0
    for i in range (0,len(quantities)):
        if i>=0 and i<3:
            a=a+quantities[i]*cost[i]
        elif i>=3 and i<6:
            b=b+quantities[i]*cost[i]
        else:
            c=c+quantities[i]*cost[i]
    print ("Apparels = Rs ",a)
    print ("Electronics = Rs ",b)
    print ("Eatables = Rs ",c)
    return (a,b,c)
            


# In[5]:


def get_discount(cost, discount_rate):
    return int(cost*discount_rate)


# In[6]:


def calculate_discounted_prices(apparels_cost, electronics_cost, eatables_cost):
    print ("-"*50)
    print ("DISCOUNTS")
    print ("-"*50)
    d=0
    e=0
    f=0
    c1=apparels_cost
    c2=electronics_cost
    c3=eatables_cost
    if apparels_cost>=2000:
        d=get_discount(apparels_cost,0.1)
        c1=apparels_cost-d
        print ("[Apparels] Rs "+str(apparels_cost)+"- Rs "+str(d)+"= Rs "+str(c1))
    if electronics_cost>=25000:
        e=get_discount(electronics_cost,0.1)
        c2=electronics_cost-e
        print ("[Electronics] Rs "+str(electronics_cost)+"- Rs "+str(e)+"= Rs "+str(c2))
    if eatables_cost>=500:
        f=get_discount(eatables_cost,0.1)
        c3=eatables_cost-f
        print ("[Eatables] Rs "+str(eatables_cost)+"- Rs "+str(f)+"= Rs "+str(c3))
    print (" ")
    print ("TOTAL DISCOUNT = ",(d+e+f))
    print ("TOTAL COST = ",(c1+c2+c3))
    return (c1,c2,c3)
   
    
        


# In[7]:


def get_tax(cost, tax):
    return int(cost * tax)


# In[8]:


def calculate_tax(apparels_cost, electronics_cost, eatables_cost):
    print ("-"*50)
    print ("TAX")
    print ("-"*50)
    d=0
    e=0
    f=0
    c1=apparels_cost
    c2=electronics_cost
    c3=eatables_cost
    d=get_tax(apparels_cost,0.1)
#     c1=apparels_cost*d
    print ("[Apparels] Rs "+str(apparels_cost)+"* 0.10 = Rs "+str(d))
    e=get_tax(electronics_cost,0.15)
#     c2=electronics_cost*e
    print ("[Electronics] Rs "+str(electronics_cost)+"* 0.15 = Rs "+str(e))
    f=get_tax(eatables_cost,0.05)
#     c3=eatables_cost*f
    print ("[Eatables] Rs "+str(eatables_cost)+"* 0.05 = Rs "+str(f))
    print (" ")
    print ("TOTAL TAX = ",(d+e+f))
    print ("TOTAL COST = ",(c1+c2+c3)+(d+e+f))
    return ((c1+c2+c3)+(d+e+f),d+e+f)


# In[9]:


def apply_coupon_code(total_cost):
    print ("-"*50)
    print ("COUPON CODE")
    print ("-"*50)
    td=0
    while True:
        c=input ("Enter coupon code (else leave blank):")
        if c=="HELLE25":
            if total_cost>=25000:
                td=0.25*total_cost
                if td>5000:
                    td=5000
            print ("[HELLE25] min(5000, Rs "+str(total_cost)+"* 0.25) = Rs "+str(td))
            print ()
            break
        if c=="CHILL50":
            if total_cost>=50000:
                td=0.5*total_cost
                if td>10000:
                    td=10000
            print ("[CHILL50] min(10000, Rs "+str(total_cost)+"* 0.50) = Rs "+str(td))
            print ()
            break
        if len(c)==0:
            print ("No coupon code applied.")
            print ()
            break
        else:
            print ("Invalid coupon code. Try again.")
            print ()
    print ("TOTAL COUPON DISCOUNT = Rs ",td)
    print ("TOTAL COST = Rs ",(total_cost-td))
    return (total_cost-td,td)
        
        


# In[10]:


def get_bulk_input():
    print ("-"*50)
    print ("ENTER ITEM AND QUANTITIES")
    print ("-"*50)
    l=[0,0,0,0,0,0,0,0,0,0]
    while True:
        n=input("Enter code and quantity (leave blank to stop):")
        count=0
        for i in n:
            if i==' ':
                break
            count=count+1
        if n=="":
            print ("Your order has been finalised.")
            break
        elif int(n[0:count])<0 or int(n[0:count])>9 and int(n[count+1:])<=0:
            print ("Invalid code and quantity. Try again.")
        elif int(n[count+1:])<=0:
            print ("Invalid quantity. Try again ")    
        elif int(n[0:count])<0 or int(n[0:count])>9:
            print ("Invalid code. Try again.")
        else:
            l[int(n[0:count])]=l[int(n[0:count])]+int(n[count+1:])
            print ("You added "+n[count+1:]+" "+description[int(n[0:count])])
        print ()
    return l
            


# In[ ]:


def main():
    code=["0","1","2","3","4","5","6","7","8","9"]
    description=["Tshirt","Trousers","Scarf","Smartphone","Ipad","Laptop","Eggs","Chocolate","Juice","Milk"]
    category=["Apparels","Apparels","Apparels","Electronics","Electronics","Electronics","Eatables","Eatables","Eatables","Eatables"]
    cost=[500,600,250,20000,30000,50000,5,10,100,45]
    (show_menu())
    while True:
        m=input("Would you like to buy in bulk? (y or Y/n or N):")
        if m=="y" or m=="Y" or m=="n" or m=="N":
            break
        else:
            continue
    if m=="n" or m=="N":
        x=(get_regular_input())
        print_order_details(x)
    if m=="y" or m=="Y":
        x=(get_bulk_input())
        print_order_details(x)
    tple=calculate_category_wise_cost(x)
    tple1=calculate_discounted_prices(tple[0], tple[1], tple[2])
    tple2=calculate_tax(tple1[0], tple1[1], tple1[2])
    tple3=apply_coupon_code(tple2[0])
    print ()
    print ("Thank you for visiting!")
#!/usr/bin/env python
# coding: utf-8

# In[1]:


def show_menu():
    print ("="*50)
    print (" "*20+"MY BAZAAR"+" "*20)
    print ("="*50)
    print ("Hello! Welcome to my grocery store")
    print ("Following are the products available in the shop:")
    print (" ")
    print ("-"*50)
    print (" CODE | DESCRIPTION | CATEGORY    | COST (Rs)")
    print (" 0    | Tshirt      | Apparels    | 500      ")
    print (" 1    | Trousers    | Apparels    | 600      ")
    print (" 2    | Scarf       | Apparels    | 250      ")
    print (" 3    | Smartphone  | Electronics | 20000    ")
    print (" 4    | iPad        | Electronics | 30000    ")
    print (" 5    | Laptop      | Electronics | 50000    ")
    print (" 6    | Eggs        | Eatables    | 5        ")
    print (" 7    | Chocolate   | Eatables    | 10       ")
    print (" 8    | Juice       | Eatables    | 100      ")
    print (" 9    | Milk        | Eatables    | 45       ")
    print ("-"*50)   


# In[ ]:





# In[2]:


def get_regular_input():
    print ("-"*50)
    print ("ENTER ITEMS YOU WISH TO BUY")
    print ("-"*50)
    n=(input("Enter the item codes (space-separated):"))
    global l
    l=[]
    for i in range (0,len(n)):
        if n[i]==" ":
            continue
        else:
            l.append (int(n[i]))
    l1=[0,0,0,0,0,0,0,0,0,0]
    for i in range (0,len(l)):
        if l[i]>=0 and l[i]<10:
            l1[l[i]]=l1[l[i]]+1
        else:
            print ("Error")
    return l1
    


# In[3]:


def print_order_details(quantities):
    print ("-"*50)
    print ("ORDER DETAILS")
    print ("-"*50)
#     print (quantities)
    count=0
    tc=0
    for i in range (len(quantities)):
        if quantities[i]!=0:
            tc=tc+(cost[i]*quantities[i])
            count=count+1
            print ("["+str(count)+"] "+description[i]+" x "+str(quantities[i])+" = Rs "+str(cost[i])+" * "+str(quantities[i])+" = Rs "+str(cost[i]*quantities[i]))
    print ()
    print ("TOTAL COST = Rs ",tc)
    
    
    


# In[4]:


def calculate_category_wise_cost(quantities):
    print ("-"*50)
    print ("CATEGORY-WISE COST")
    print ("-"*50)
    a=0
    b=0
    c=0
    for i in range (0,len(quantities)):
        if i>=0 and i<3:
            a=a+quantities[i]*cost[i]
        elif i>=3 and i<6:
            b=b+quantities[i]*cost[i]
        else:
            c=c+quantities[i]*cost[i]
    print ("Apparels = Rs ",a)
    print ("Electronics = Rs ",b)
    print ("Eatables = Rs ",c)
    return (a,b,c)
            


# In[5]:


def get_discount(cost, discount_rate):
    return int(cost*discount_rate)


# In[6]:


def calculate_discounted_prices(apparels_cost, electronics_cost, eatables_cost):
    print ("-"*50)
    print ("DISCOUNTS")
    print ("-"*50)
    d=0
    e=0
    f=0
    c1=apparels_cost
    c2=electronics_cost
    c3=eatables_cost
    if apparels_cost>=2000:
        d=get_discount(apparels_cost,0.1)
        c1=apparels_cost-d
        print ("[Apparels] Rs "+str(apparels_cost)+"- Rs "+str(d)+"= Rs "+str(c1))
    if electronics_cost>=25000:
        e=get_discount(electronics_cost,0.1)
        c2=electronics_cost-e
        print ("[Electronics] Rs "+str(electronics_cost)+"- Rs "+str(e)+"= Rs "+str(c2))
    if eatables_cost>=500:
        f=get_discount(eatables_cost,0.1)
        c3=eatables_cost-f
        print ("[Eatables] Rs "+str(eatables_cost)+"- Rs "+str(f)+"= Rs "+str(c3))
    print (" ")
    print ("TOTAL DISCOUNT = ",(d+e+f))
    print ("TOTAL COST = ",(c1+c2+c3))
    return (c1,c2,c3)
   
    
        


# In[7]:


def get_tax(cost, tax):
    return int(cost * tax)


# In[8]:


def calculate_tax(apparels_cost, electronics_cost, eatables_cost):
    print ("-"*50)
    print ("TAX")
    print ("-"*50)
    d=0
    e=0
    f=0
    c1=apparels_cost
    c2=electronics_cost
    c3=eatables_cost
    d=get_tax(apparels_cost,0.1)
#     c1=apparels_cost*d
    print ("[Apparels] Rs "+str(apparels_cost)+"* 0.10 = Rs "+str(d))
    e=get_tax(electronics_cost,0.15)
#     c2=electronics_cost*e
    print ("[Electronics] Rs "+str(electronics_cost)+"* 0.15 = Rs "+str(e))
    f=get_tax(eatables_cost,0.05)
#     c3=eatables_cost*f
    print ("[Eatables] Rs "+str(eatables_cost)+"* 0.05 = Rs "+str(f))
    print (" ")
    print ("TOTAL TAX = ",(d+e+f))
    print ("TOTAL COST = ",(c1+c2+c3)+(d+e+f))
    return ((c1+c2+c3)+(d+e+f),d+e+f)


# In[9]:


def apply_coupon_code(total_cost):
    print ("-"*50)
    print ("COUPON CODE")
    print ("-"*50)
    td=0
    while True:
        c=input ("Enter coupon code (else leave blank):")
        if c=="HELLE25":
            if total_cost>=25000:
                td=0.25*total_cost
                if td>5000:
                    td=5000
            print ("[HELLE25] min(5000, Rs "+str(total_cost)+"* 0.25) = Rs "+str(td))
            print ()
            break
        if c=="CHILL50":
            if total_cost>=50000:
                td=0.5*total_cost
                if td>10000:
                    td=10000
            print ("[CHILL50] min(10000, Rs "+str(total_cost)+"* 0.50) = Rs "+str(td))
            print ()
            break
        if len(c)==0:
            print ("No coupon code applied.")
            print ()
            break
        else:
            print ("Invalid coupon code. Try again.")
            print ()
    print ("TOTAL COUPON DISCOUNT = Rs ",td)
    print ("TOTAL COST = Rs ",(total_cost-td))
    return (total_cost-td,td)
        
        


# In[10]:


def get_bulk_input():
    print ("-"*50)
    print ("ENTER ITEM AND QUANTITIES")
    print ("-"*50)
    l=[0,0,0,0,0,0,0,0,0,0]
    while True:
        n=input("Enter code and quantity (leave blank to stop):")
        count=0
        for i in n:
            if i==' ':
                break
            count=count+1
        if n=="":
            print ("Your order has been finalised.")
            break
        elif int(n[0:count])<0 or int(n[0:count])>9 and int(n[count+1:])<=0:
            print ("Invalid code and quantity. Try again.")
        elif int(n[count+1:])<=0:
            print ("Invalid quantity. Try again ")    
        elif int(n[0:count])<0 or int(n[0:count])>9:
            print ("Invalid code. Try again.")
        else:
            l[int(n[0:count])]=l[int(n[0:count])]+int(n[count+1:])
            print ("You added "+n[count+1:]+" "+description[int(n[0:count])])
        print ()
    return l
            


# In[ ]:


def main():
    code=["0","1","2","3","4","5","6","7","8","9"]
    description=["Tshirt","Trousers","Scarf","Smartphone","Ipad","Laptop","Eggs","Chocolate","Juice","Milk"]
    category=["Apparels","Apparels","Apparels","Electronics","Electronics","Electronics","Eatables","Eatables","Eatables","Eatables"]
    cost=[500,600,250,20000,30000,50000,5,10,100,45]
    (show_menu())
    while True:
        m=input("Would you like to buy in bulk? (y or Y/n or N):")
        if m=="y" or m=="Y" or m=="n" or m=="N":
            break
        else:
            continue
    if m=="n" or m=="N":
        x=(get_regular_input())
        print_order_details(x)
    if m=="y" or m=="Y":
        x=(get_bulk_input())
        print_order_details(x)
    tple=calculate_category_wise_cost(x)
    tple1=calculate_discounted_prices(tple[0], tple[1], tple[2])
    tple2=calculate_tax(tple1[0], tple1[1], tple1[2])
    tple3=apply_coupon_code(tple2[0])
    print ()
    print ("Thank you for visiting!")
code=[]
description=[]
category=[]
cost=[]
    
if __name__ == '__main__':
    main()
    


# In[ ]:





# In[ ]:





        
    
if __name__ == '__main__':
    main()
    


# In[ ]:





# In[ ]:




