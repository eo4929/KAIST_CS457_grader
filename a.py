students = []

with open('students.csv', 'r') as f: # 학생 리스트
    f.readline()

    while True:
        line = f.readline()
        if not line: break

        items = line.split(',')
        students.append({
            'id': items[2],
            'name': items[3],
            'email': items[5],
            'alias': items[6],
            'attendance': 'None'
        })

for i in range(len(students)): # checking same rows (students)
    for j in range(i+1, len(students)):
        if students[i]['id'] == students[j]['id']:
            print('!!!!!!!!!!!!!!!!!!!!!!!!!', i, j)
        if students[i]['name'] == students[j]['name']:
            print('!!!!!!!!!!!!!!!!!!!!!!!!!', i, j)
        if students[i]['email'] == students[j]['email']:
            print('!!!!!!!!!!!!!!!!!!!!!!!!!', i, j)

with open('in_attendance.csv', 'r', encoding='utf-8') as f: # 교수님이 주시는 duration 파일
    lines = f.readlines()

not_late = 9999
absent = 9999
for i in range(1, len(lines)):
    if lines[i] != '\n' and lines[i] != ',,\n':
        items = lines[i].rstrip('\n').split(',')
        name = items[0].strip()
        email = items[1].strip()
        duration = int('0' if items[2] == '' else items[2])
        attendance = 'be present'

        if name == 'In-Young Ko':
            not_late = duration * 0.8 + 2 # adding 2 minutes
            absent = duration * 0.5 + 2 # adding 2 minutes

print('[지각 기준:', not_late, '결석 기준:', absent, ']\n')

#print(lines)

for i in range(1, len(lines)): # 학생당 출석/지각/결석 여부 -> attendance 변수에 저장
    if lines[i] != '\n':
        items = lines[i].rstrip('\n').split(',')

        print('items= ', end='')
        print(items)
        name = items[0].strip()
        email = items[1].strip()
        duration = int('0' if items[2] == '' else items[2])
        #print('duration = ', duration)
        attendance = 'be absent'

        if duration >= not_late:
            attendance = 'be present'
        elif duration >= absent:
            attendance = 'be late'

        #print('attendance = ', attendance)

        check = False
        for j in range(len(students)):
            if students[j]['name'].strip() in name:
                students[j]['attendance'] = attendance
                check = True
            elif students[j]['id'].strip() in name:
                students[j]['attendance'] = attendance
                check = True
            elif students[j]['alias'].strip() in name:
                students[j]['attendance'] = attendance
                check = True
            elif students[j]['email'].strip() == email:
                students[j]['attendance'] = attendance
                check = True
            if check == True:
                break
        if not check:
            print('출석/지각/결석 여부: ',end='')
            print(attendance, lines[i])

#print(students) # 아 잘 들어있네 아래 코드에서 writing만 안되고 있을 뿐

with open('out_attendance.csv', 'w', encoding="utf-8") as f:

    for student in students:
        #f.write(student['id'] + ',' + student['name'] + ',' + student['attendance'] + '\n')
        f.write(student['id'] + ',' + student['attendance'] + '\n')