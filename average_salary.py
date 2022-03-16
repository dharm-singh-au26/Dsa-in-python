'''
Given an array of unique integers salary where salary[i] is the salary of the employee i.

Return the average salary of employees excluding the minimum and maximum salary.

 

Example 1:

Input: salary = [4000,3000,1000,2000]
Output: 2500.00000
Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively.
Average salary excluding minimum and maximum salary is (2000+3000)/2= 2500z
'''
salary = [4000,3000,1000,2000]
def average_salary(salary):
    # Total_salary = sum(salary)
    # min_salary = min(salary)
    # max_salary = max(salary)
    # salary_of = (Total_salary - max_salary - min_salary)//(len(salary)-2)
    return((sum(salary)-min(salary)-max(salary))/(len(salary)-2))
    

    # print(Total_salary)
print(average_salary(salary))