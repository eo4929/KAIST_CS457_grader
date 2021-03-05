students = []

with open('students.csv', 'r') as f:
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
            'participation': 0
        })

for i in range(len(students)): # checking same rows (students)
    for j in range(i+1, len(students)):
        if students[i]['id'] == students[j]['id']:
            print('!!!!!!!!!!!!!!!!!!!!!!!!!', i, j)
        if students[i]['name'] == students[j]['name']:
            print('!!!!!!!!!!!!!!!!!!!!!!!!!', i, j)
        if students[i]['email'] == students[j]['email']:
            print('!!!!!!!!!!!!!!!!!!!!!!!!!', i, j)

with open('in_participation.txt', 'r', encoding='UTF8') as f:
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
            elif students[j]['alias'].strip() in new_lines[i]:
                students[j]['participation'] += 1
                check = True
            
            if check == True:
                break
        if not check:
            print(new_lines[i])


with open('out_participation.csv', 'w') as f:
    for student in students:
        #f.write(student['id'] + ',' + student['name'] + ',' + str(student['participation']) + '\n')
        f.write(student['id'] + ',' + str(student['participation']) + '\n')