import pandas as pd

# Globals
student_dict = {}

def gatherdata():
  add_data('match1.csv', '1')
  add_data('match2.csv', '2')
  add_data('match3.csv', '3')
  add_data('match4.csv', '4')
  add_data('match5.csv', '5')
  add_data('match6.csv', '6')
  
def make_key(row):
  return row['Last'].strip().lower() + "|" + row['First'].strip().lower() + "|" + row['School'].lower()


def update_total(id):
  student_dict[id]['Total'] = student_dict[id]['M1'] + student_dict[id]['M2'] + student_dict[id]['M3'] + student_dict[id]['M4'] + student_dict[id]['M5'] + student_dict[id]['M6']
  
def add_data(filename, round_id):

  result = pd.read_csv(filename)
  
  for idx in result.index:
    if not pd.isna(result['Last'][idx]):
      print(result['Last'][idx])
      record = {'Last': result['Last'][idx].strip(),
                'First': result['First'][idx].strip(),
                'Grade': int(result['Grade'][idx]),
                'School': result['School'][idx],
                'M1': 0,
                'M2': 0,
                'M3': 0,
                'M4': 0,
                'M5': 0,
                'M6': 0,
                'Total': 0}

      id = make_key(result.iloc[idx]);
      score = int(result['Scores'][idx]);
      record['M' + round_id] = score;
      
      if id in student_dict:
        student_dict[id]['M' + round_id] = score
      else: 
        student_dict[id] = record

      update_total(id)
      
# ===================================================
gatherdata()

## convert to a data frame?
first = []
last = []
school = []
total = []
m1 = []
m2 = []
m3 = []
m4 = []
m5 = []
m6 = []
grade = []
for id in student_dict:
  last.append(student_dict[id]['Last']);
  first.append(student_dict[id]['First']);
  school.append(student_dict[id]['School']);
  grade.append(student_dict[id]['Grade']);
  m1.append(student_dict[id]['M1']);
  m2.append(student_dict[id]['M2']);
  m3.append(student_dict[id]['M3']);
  m4.append(student_dict[id]['M4']);
  m5.append(student_dict[id]['M5']);
  m6.append(student_dict[id]['M6']);
  total.append(student_dict[id]['Total']);

new_dict = {'Last': last, 'First': first, 'School': school, 'Grade': grade, '1': m1, '2': m2, '3': m3, '4': m4, '5': m5, '6': m6,'Total:': total}

df = pd.DataFrame(new_dict)
df.to_csv('output.csv')