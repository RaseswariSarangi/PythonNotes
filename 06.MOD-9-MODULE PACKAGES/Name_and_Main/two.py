#for easy running put it in pythonProjects of pycharm_projects
#then carry out the following lines

import one

print("top-level in two.py")

one.func()

if __name__ == "__main__":
    print("two.py is being run directly")
else:
    print("two.py is being imported into another module")
