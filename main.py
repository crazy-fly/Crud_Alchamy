from sqlalchemy import create_engine,MetaData,Table, engine,String,Integer,Boolean
from sqlalchemy.sql.schema import Column, PrimaryKeyConstraint 


engine = create_engine('sqlite:///Student.db',echo = True)
meta = MetaData()

Students_Table = Table(
    'students',meta,
    Column('USN',String(10),primary_key= True),
    Column('student_name',String(26)),
    Column('gender',String(12)),
    Column('entry_type',String(10)),
    Column('YOA',Integer),
    Column('migrated',String(3)),
    Column('Details_of_transfer', String(100)),
    Column('admission_in_separate_division',String(3)),
    Column('Details_of_admission_in_seperate_division', String(100)),
    Column('YOP',Integer),
    Column('degree_type',String(2)),
    Column('pu_marks',Integer),
    Column('entrance_marks',Integer)
)

meta.create_all(engine)
connect = engine.connect()

def create():
    USN = input("Enter the Admission")
    Student_name = input("Name of the Student")
    Gender = input('Gender: ')
    Entry_Type = input('Entry Type (Normal or lateral')
    YOA = int(input("year of Admission"))
    migrated = input("migrated from other programs / Insitutions")
    if migrated == "Yes":
        #migrated = Boolean(True)
        Details_of_Transfer = input("Details of Transfer")
    else:
        #migrated = Boolean(False)
        Details_of_Transfer = None
    admission_separate = input("Admisiion in separate division")
    if admission_separate == "yes":
        #admission_separate = Boolean(True)
        admission_separate_details = input("Details :")
    else:
        #admission_separate = Boolean(False)
        admission_separate_details = None
    YOP = int(input("Year of Passing"))
    degree_type = input('UG/PG')
    pu_marks = int(input("Marks in 12 grade:"))
    entrance_marks = int(input("Entrance Exam Rank: "))

    ins = Students_Table.insert().values(
        USN = USN,
        student_name = Student_name, 
        gender = Gender, 
        entry_type = Entry_Type, 
        YOA = YOA, 
        migrated = migrated, 
        Details_of_transfer = Details_of_Transfer,
        admission_in_separate_division = admission_separate,
        Details_of_admission_in_seperate_division = admission_separate_details,
        YOP = YOP , 
        degree_type = degree_type, 
        pu_marks = pu_marks, 
        entrance_marks = entrance_marks)


    result = connect.execute(ins)

def read():
    sel = Students_Table.select()
    result = connect.execute(sel)

    for student in result:
        print(student)


def update():
    primary = input('Enter USN : ')
    Year = input('Enter passing year: ')
    ud_statement = Students_Table.update().where(Students_Table.c.USN == primary).values(YOP = Year)
    result = connect.execute(ud_statement)

def delete():
    Primary = input('Enter USN: ')
    del_sta = Students_Table.delete().where(Students_Table.c.USN = Primary)
    result = connect.execute(del_sta)

opt_dict = {1: create,2:read,3:update,4:delete}

while(True):
    opt = int(input("""To perform the following operations 
          Press 1 to enter new values
          Press 2 to view the table 
          Press 3 to update Passing Year 
          Press 4 to delete a record """))
    performing = opt_dict[opt]()


