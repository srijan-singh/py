def incSalary(employee_list : list) -> list:
    
    for index in range(len(employee_list)):

        emp = employee_list[index]

        dsgn, salary = emp

        if (dsgn == "Manager"):
            salary+=5000

        elif (dsgn == "General Manager"):
            salary+=10000
        
        elif (dsgn == "CEO"):
            salary+=20000

        elif (dsgn == "Worker"):
            salary+=2000

        else:
            print("No Designation Found!!!!!!")
    
        employee_list[index] = (dsgn, salary)
        
    return employee_list


employee_list = [("Manager", 50000), ("General Manager", 100000), ("CEO", 150000), ("Worker", 2000)]

print(employee_list)

print(incSalary(employee_list))