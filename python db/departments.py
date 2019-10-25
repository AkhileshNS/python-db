# '''Departments = 

# {

# ​	(did) : {

# ​						'did' : autonum() + year + sem,

# ​						'name' : '',

# ​						'long name' : '',

# ​						'hod' : (fid ''),

# ​						...

# ​				}

# }

# Faculty = 

# {

# ​	(fid) : {

# ​						'fid' : autonum() + year + sem,

# ​						'name' : '',

# ​						'dept aff.' : (did ''),

# ​						('ufn' (univarsal faculty number) : '',)

# ​						...

# ​				}

# }
# '''

from __future__ import print_function
import json

Departments = {
  '1O2019' : {
    'id' : '1O2019',
    'name' : 'ISE',
    'long name' : 'Information Science and Engineering',
    'hod' : '1O2019'
  }
}

Faculty = {
  '1O2019' : {
    'id' : '1O2019',
    'name' : 'Dr. Dakshayani M.',
    'dept' : '1O2019'
  },
  '2O2019' : {
    'id' : '2O2019',
    'name' : 'Dr. Guruprasad',
    'dept' : '1O2019'
  },
  '3O2019' : {
    'id' : '3O2019',
    'name' : 'Dr. Shubha Rao',
    'dept' : '1O2019'
  }
}

Courses = {
  '1O2019' : {
    'id' : '1O2019',
    'name' : 'Data Structures',
    'dept' : '1' + 'O' + '2019',
    'course code' : '16IS6DCDSC',
    'sem' : 3,
    'sheets' : ['1' + 'O' + '2019', '2' + 'O' + '2019']
  },
  '2O2019' : {
    'id' : '2O2019',
    'name' : 'Java Programming',
    'dept' : '1' + 'O' + '2019',
    'course code' : '16IS6DCJAV',
    'sem' : 5,
    'sheets' : ['3' + 'O' + '2019', '4' + 'O' + '2019']
  }
}

Sheets = {
  '1O2019' : {
    'id' : '1O2019',
    'faculty' : '2O2019',
    'cid' : '1O2019',
    'name' : '3A DS'
  },

  '2O2019' : {
    'id' : '2O2019',
    'faculty' : '3O2019',
    'cid' : '1O2019',
    'name' : '3B DS'
  },

  '3O2019' : {
    'id' : '3O2019',
    'faculty' : '2O2019',
    'cid' : '2O2019',
    'name' : '5A Java'
  },

  '4O2019' : {
    'id' : '4O2019',
    'faculty' : '3O2019',
    'cid' : '2O2019',
    'name' : '5B Java'
  }
}

with open('dummy_db.json', 'w') as file:
  toWrite = '{"Departments" : ' + json.dumps(Departments) + '}'
  file.write(toWrite)


def teach_sub(fid):
  res = []
  global Sheets
  global Courses
  for sid, sheet in Sheets.items():
    if sheet['faculty'] == fid:
      res.append(Courses[sheet['cid']].copy())
  return(res)

# print(Departments)
# print(Faculty)
# print(Courses)
# print(Sheets)

def search_teach(name):
  import re
  global Faculty
  for teacher in Faculty.values():
    if re.search(name.lower().strip(), teacher['name'].lower()) is not None:
      return teacher['id']
  return None

def print_subject(course):
  global Departments
  print('Subject : ', course['name'])
  print('Course Code : ', course['course code'])
  print('Department : ', Departments[course['dept']]['name'])
  print('Semester : ', course['sem'])
  print()

name = raw_input('Enter teacher name : ')
print()
print()

teach_code = search_teach(name)
#print(teach_code)
if teach_code is not None:
  for course in teach_sub(teach_code):
    print_subject(course)