try:
    projectCodes = ("ProjectCode1.java", "ProjectCode2.py", "ProjectCode3.cpp")
    print(f"Project Codes: {projectCodes}")
    print("Modifying first element in the list to 'ProjectCode1.py'...")
    projectCodes[0] = "ProjectCode1.py"
    print(f"Project Codes: {projectCodes}")
except Exception as e:
    print(f"Modification failed! {e}")