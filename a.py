students = []
input_filename = 'participants_cs457_lec1_20210302.csv'
outout_filename = 'out_attendance_0302.csv'

with open('students_cs457.csv', 'r', encoding='utf-8') as f: # 학생 리스트
    f.readline()

    while True:
        line = f.readline()
        if not line: break

        items = line.split(',')
        students.append({
            'id': items[2],
            'name': items[3],
            'attendance': 'None'
        })

#print(students)

for i in range(len(students)): # checking same rows (students)
    for j in range(i+1, len(students)):
        if students[i]['id'] == students[j]['id']:
            print('!!!!!!!!!!!!!!!!!!!!!!!!!', i, j)
        if students[i]['name'] == students[j]['name']:
            print('!!!!!!!!!!!!!!!!!!!!!!!!!', i, j)


with open(input_filename, 'r', encoding='utf-8') as f: # 교수님이 주시는 duration 파일
    lines = f.readlines()

print(lines)
print()

items = lines[2].rstrip('\n').split(',')
duration = int( items[5] )
print('duration of professor = ', duration)

lines = lines[10:]

print()
print(lines)
print()

not_late = 9999
absent = 9999

for i in range(1, len(lines)):
    if lines[i] != '\n' and lines[i] != ',,\n':
        items = lines[i].rstrip('\n').split(',')
        name = items[0].strip()
        email = items[1].strip()
        duration = int('0' if items[2] == '' else items[2])
        attendance = 'be present'

        #if name == 'In-Young Ko':
        #not_late = duration * 0.8 + 2 # adding 2 minutes
        #absent = duration * 0.5 + 2 # adding 2 minutes


not_late = duration * 0.8 + 2 # adding 2 minutes
absent = duration * 0.5 + 2 # adding 2 minutes
print('[지각 기준:', not_late, '결석 기준:', absent, ']\n')

num_of_participants = 0
for i in range(1, len(lines)): # 학생당 출석/지각/결석 여부 -> attendance 변수에 저장
    if lines[i] != '\n':
        items = lines[i].rstrip('\n').split(',')

        num_of_participants +=1
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
            if students[j]['name'].strip() in name: # 아 뭐라도 줌 name에 들어가면 student 속 사람이랑 줌에 접속한 사람이랑 동일한 걸로 취급했구나
                students[j]['attendance'] = attendance
                check = True
            elif students[j]['id'].strip() in name:
                students[j]['attendance'] = attendance
                check = True

            if check == True:
                break
        if not check: # 이쪽으로 가는 케이스 때문에 Zoom 유저 네임에 대한 정책이 필요한 것임 -> 아마 정연이는 수작업으로 한듯..?
            print('출석/지각/결석 여부: ',end='')
            print(attendance)

print()
print('참가자 수: ', num_of_participants)
print()

with open(outout_filename, 'w', encoding="utf-8") as f:

    for student in students:
        #f.write(student['id'] + ',' + student['name'] + ',' + student['attendance'] + '\n')
        f.write(student['id'] + ',' + student['attendance'] + '\n')