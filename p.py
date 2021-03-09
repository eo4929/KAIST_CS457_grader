students = []
input_filename = 'chat_cs457_lec1_20210304.txt'
outout_filename = 'out_participation_0304.csv'

with open('students_cs457.csv', 'r', encoding='utf-8') as f:
    f.readline()

    while True:
        line = f.readline()
        if not line: break

        items = line.split(',')
        students.append({
            'id': items[2],
            'name': items[3],
            'participation': 0
        })

for i in range(len(students)): # checking same rows (students)
    for j in range(i+1, len(students)):
        if students[i]['id'] == students[j]['id']:
            print('!!!!!!!!!!!!!!!!!!!!!!!!!', i, j)
        if students[i]['name'] == students[j]['name']:
            print('!!!!!!!!!!!!!!!!!!!!!!!!!', i, j)
        

with open(input_filename, 'r', encoding='UTF8') as f:
    lines = f.readlines()

print('len(line): ', len(lines))
print('lines: ', lines)

new_lines = [] # Thank you, Yes, No , Ok 포함한 원소는 제거한 lines

found = [-1,-1,-1,-1,-1,-1,-1,-1]
for line in lines:
    found[0] = line.find('Thank you') # 인자 포함한 인덱스 반환
    found[1] = line.find('thank you')
    found[2] = line.find('Yes')
    found[3] = line.find('yes')
    found[4] = line.find('No')
    found[5] = line.find('no')
    found[6] = line.find('Ok')
    found[7] = line.find('ok')

    if sum(found) == -8:
        new_lines.append(line)
    found = [-1,-1,-1,-1,-1,-1,-1,-1]

print('len(new_lines): ', len(new_lines))
print('new_lines: ', new_lines)

for i in range(len(new_lines)):
    if new_lines[i] != '\n':
        # items = lines[i].split()
        # items = set(items)

        check = False
        for j in range(len(students)):
            if students[j]['name'].strip() in new_lines[i]:
                students[j]['participation'] += 1
                check = True
            elif students[j]['id'].strip() in new_lines[i]:
                students[j]['participation'] += 1
                check = True
            
            if check == True:
                break
        if not check: # zoom 유저 네임에 id나 실제 name(student_cs457.csv 상) 관련된 게 없으면 일로 간다->수작업으로 참가점수 카운팅하기 위한 코드
            print(new_lines[i])


with open(outout_filename, 'w') as f:
    for student in students:
        #f.write(student['id'] + ',' + student['name'] + ',' + str(student['participation']) + '\n')
        f.write(student['id'] + ',' + str(student['participation']) + '\n')