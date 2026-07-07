def fun ():
    x=50
    def fun2():
        print(x)
    fun2()
fun()
company_budget = 500000
def company_tracker( ):
    total_projects = 100
    def update_project():
        nonlocal total_projects
        global company_budget
        total_projects += 20
        company_budget += 100000
    update_project()
        print("updated total_projects")
         print("company_budget")

company_tracker()