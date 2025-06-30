# virtual enviornment 
# isolated python environment 
# uss python ke under keval  wo pakages dikhayi denge jo hmne letar kiye hai unka dusaron se and global koi lena dena nahi hoga 
# unn sabhi ke under same pakages ke 10 sare alag alag version daal skte ho 
# virtual environment ki jarurat tb padti hai jb tumhara dost kisi dusare version of libraries ko use kr raha hai or tum kisi dusare version ki library ko use kr rahe ho 
# or
# VE ki jarurat tb padti hai kisi ek librray ka version kisi dusare verson pe deped krta hai or koi orr library koi dusre version ko use kr raha hai 
# 

# step to create vertual environment 
# step1!! create new folder(python-venv) open same folder in command prompt 
# type python -n venu myenv (hamre version ki copy bn gayi hai)
# (now we want to download a pandas or tensorflow for this folder only ) python-venv% source myenv/bin/activate
# ab pip ka use krne pr local environment install hoga pandas and else library 
        # python3
        # import pandas as pd
        # (will show error because we still hadnt downloaded pandas for locacl environment)
# 





# -------------------------------------------------------------------------------------
# To create a requirements.txt file, you can use the following command in your terminal:
# pip freeze > requirements.txt
# This will generate a requirements.txt file with all the installed packages in your virtual environment/also all the library of ur global enviromnet if u r in global.
# pip freeze -r requirements.txt  # to donload all those file  

# create new folder in directory  named it vertual enviornment(VE)
# open same folder in terminal
# run this command  "python -n venv myenv" ---> hmne isske upper ek folder banaya tha uss folder ke under ek aur folder bn jaeyga "myenv" naam se
# run from our own file i.e(VE) "source myenv/bin/activate" ab vertual inviron tment tayar hoo agay hai 
#
# 
#   

# Windows PowerShell
# PS C:\Users\thaku\OneDrive\Desktop\PROGRAMMING\pythonAPNACOLLEGE\VE> python -m venv myenv
# PS C:\Users\thaku\OneDrive\Desktop\PROGRAMMING\pythonAPNACOLLEGE\VE>
# PS C:\Users\thaku\OneDrive\Desktop\PROGRAMMING\pythonAPNACOLLEGE\VE> source myenv/bin/activate
# # 
# PS C:\Users\thaku\OneDrive\Desktop\PROGRAMMING\pythonAPNACOLLEGE\VE> source myenv/bin/activate
# # 
# PS C:\Users\thaku\OneDrive\Desktop\PROGRAMMING\pythonAPNACOLLEGE\VE> .\myenv\Scripts\Activate
# (myenv) PS C:\Users\thaku\OneDrive\Desktop\PROGRAMMING\pythonAPNACOLLEGE\VE> import pandas as pd
# # 
# # 
# (myenv) PS C:\Users\thaku\OneDrive\Desktop\PROGRAMMING\pythonAPNACOLLEGE\VE> pip install pandas
# # 
# (myenv) PS C:\Users\thaku\OneDrive\Desktop\PROGRAMMING\pythonAPNACOLLEGE\VE> pip install pandas==1.4.4
# Collecting pandas==1.4.4'
# # 
# (myenv) PS C:\Users\thaku\OneDrive\Desktop\PROGRAMMING\pythonAPNACOLLEGE\VE> import pandas as pd
# import : The term 'import' is not recognized as the name of a
# # 
# (myenv) PS C:\Users\thaku\OneDrive\Desktop\PROGRAMMING\pythonAPNACOLLEGE\VE> pythan
# # 
# (myenv) PS C:\Users\thaku\OneDrive\Desktop\PROGRAMMING\pythonAPNACOLLEGE\VE> python
# # 
# >>> pandas import as pd
#   File "<stdin>", line 1
#     pandas import as pd
#            ^^^^^^
# # 
# >>> import pandas as pd
#   File "<stdin>", line 1, in <module>
# NameError: name 'pd' is not defined. Did you mean: 'id'?
# >>> exit()
# # 
# (myenv) PS C:\Users\thaku\OneDrive\Desktop\PROGRAMMING\pythonAPNACOLLEGE\VE> deactivate
# PS C:\Users\thaku\OneDrive\Desktop\PROGRAMMING\pythonAPNACOLLEGE\VE>

# requirement file 

