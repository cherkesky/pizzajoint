'''
Practice: Companies and Employees

Instructions
Create an Employee type that contains information about employees of a company. Each employee must have a name, job title, and employment start date.
Create a Company type that employees can work for. A company should have a business name, address, and industry type.
Create two companies, and 5 people who want to work for them.
Assign 2 people to be employees of the first company.
Assign 3 people to be employees of the second company.
Output a report to the terminal the displays a business name, and its employees.
For example:

Acme Explosives is in the chemical industry and has the following employees
   * Michael Chang
   * Martina Navritilova

Jetways is in the transportation industry and has the following employees
   * Serena Williams
   * Roger Federer
   * Pete Sampras

   '''

class Employee :
  def __init__ (self, name, title, start_date):
    self.name = name
    self.title = title
    self.start_date = start_date

class Company:
  def __init__ (self, name, address, industry):
    self.name = name
    self.address = address
    self.industry = industry
    self.employees = list()


guy = Employee("Guy Cherkesky", "CEO", "01/01/2018")
samuel = Employee("Samuel Jackson", "CFO", "01/02/2018")
tammy = Employee("Tammy Harris", "CTO", "01/03/2018")
jordan = Employee("Jordan Tang", "Secretary", "01/04/2018")
yeezy = Employee("Yeezy Little", "Driver", "01/05/2018")

nss = Company("NSS", "301 Plus Park Blvd", "Software")
abc = Company("ABC", "302 Plus Park Blvd", "Hardware")



nss.employees.append(guy)
nss.employees.append(samuel)
nss.employees.append(tammy)

abc.employees.append(jordan)
abc.employees.append(yeezy)


print(f'{nss.name} is in the {nss.industry} industry and has the following employees:')
for employee in nss.employees:
  print(f'* {employee.name}')

print ("")

print(f'{abc.name} is in the {abc.industry} industry and has the following employees:')
for employee in abc.employees:
  print(f'* {employee.name}')
