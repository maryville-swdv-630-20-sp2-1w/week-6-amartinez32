from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer, String
from sqlalchemy.orm import sessionmaker


Base = declarative_base()



class Employee(Base):

    def __init__(self, employee_id, employee_position, employee_salary):
        self.employee_id = employee_id
        self.employee_position = employee_position
        self.employee_salary = employee_salary


    __tablename__ = 'Employee'

    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer)
    employee_position = Column(String)
    employee_salary = Column(Integer)


    def __repr__(self):
        return  "Employee ID: {0}, Employee Position: {1}, Employee Salary: ${2}".format(self.employee_id, self.employee_position, self.employee_salary)



def main():
    engine = create_engine('sqlite:///:memory:', echo=True)

    Base.metadata.create_all(engine)

    employee1 = Employee(3484509, "Manager", 45000)
    print(employee1)

    Session = sessionmaker(bind=engine)
    session = Session()

    session.add(employee1)

  



    session.add_all([
        Employee(employee_id=3480412, employee_position='Chef', employee_salary=33000),
        Employee(employee_id=3489432, employee_position='Cashier', employee_salary=21250),
        Employee(employee_id=3481875, employee_position='Delivery Driver', employee_salary=17500),

        ])

    session.commit()

    for row in session.query(Employee).all():
        print(row.employee_position, row.employee_salary)


main()