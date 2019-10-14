# importing from another program
from mymodule import my_func
my_func()

# importing from another package
from MyMainPackage import some_main_script
from MyMainPackage.SubPackage import mysubscript

some_main_script.report_main()
mysubscript.sub_report()




# Advance Concets prictices
# __name__==__main__ means in python

# __name__ : it a special method which start the execution
"""print("Hello")
    __name__=="__main__"    
"""

print(type(__name__))