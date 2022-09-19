salary = [4000,3000,1000,2000]
salary.remove(min(salary))
salary.remove(max(salary))
averageSalary = sum(salary) / len(salary)
print(averageSalary)
