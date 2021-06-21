import os

print("clean Setup")
print("Custom Setup")
i = input("$")
if i == "help":
    print("clean Setup")
    print("Custom Setup")

if i == "clean Setup":
    try:
        os.system("pip install django")
        os.system("pip install pillow")
        os.system("git clone https://github.com/ojudsonleo/Modle.git")

        os.system("cd ModlePro")
        os.system("python manage.py migrate")
        os.system("python manage.py runserver")
    except:
        os.system("pip install python-git")
        os.system("pip install pillow")
        os.system("pip install django")
        os.system("git clone https://github.com/ojudsonleo/Modle.git")
if i == "Custom Setup":
    c = input("$")
    if c == "help":
        print("conda Setup")
        print("pip Setup")
    if c == "conda setup":
        os.system("conda install -c anaconda django")
        os.system("conda install -c anaconda pillow")
        os.system("git clone https://github.com/ojudsonleo/Modle.git")
        os.system("cd ModlePro")
        os.system("python manage.py migrate")
        os.system("python manage.py runserver")