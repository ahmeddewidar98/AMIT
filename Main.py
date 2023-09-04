#!/usr/bin/env python
# coding: utf-8

# The Main Code for the calculator
# 

# In[1]:


import calc

def Main ():
    while True :
        calc_type = input('Insert your Calculation type: \n "add" for Addition \n "sub" for Substraction \n "div" for Division \n "mult" for multiplication \n')
        if calc_type == 'add' or  calc_type == 'sub'or calc_type == 'mult'or calc_type == 'div':
            pass
        else :
            print('Undefied Operation input 🤦‍♂️')
            Main()
        nums = input('\n Insert your numbers sepaeated by space: ')
        try :
            nums = nums.split()
            num1 = float(nums[0])
            num2 = float(nums[1])

            if calc_type == 'add' :
                result = calc.add(num1,num2)
                print(f'your result is \t: {result} \n')
            elif calc_type == 'sub' :
                result = calc.sub(num1,num2)
                print(f'your result is : {result} \n')
            elif calc_type == 'div' :
                result = calc.div(num1,num2)
                print(f'your result is : {result} \n')
            elif calc_type == 'mult' :
                result = calc.mult(num1,num2)
                print(f'your result is: {result} \n')
            else:
                print('Undefined Operation 🤦‍♂️')
            rep = input('Do you need another operation ?? \n "y"    for Yes \n "stop" for No \n')
            if rep == 'y':
                pass
            elif rep == 'stop' :
                break
        except :
            print('Invalid input numbers 🤦‍♂️')

Main()


# In[ ]:





# In[12]:





# In[1]:


a = 4
if a == 5 | a==6:
    print('ok')
else:
    print('gd')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




