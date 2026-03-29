
grades: list[int] = []
while True:
    stud_grade = int(input('Enter grade [-999 to exit]: '))

    try:
        grade = str(stud_grade)
    except ValueError:
        print('Invalid intput, skip')
        continue

    if stud_grade == -999:
        if len(grades) >= 10:
            break
        else:
            print('Need at least 10 valid grades, Keep entering')
            continue

    if 0 <= stud_grade <= 100:
        grades.append(stud_grade)
    else:
        print('Not in range, skip')



def get_statistics(grades):
    return {'sum': sum(grades),
            'class avg': sum(grades) / len(grades),
            'highest grade': max(grades),
            'Number of valid grades': len(grades)}
result = get_statistics(grades)
for key, value in result.items():
    print(f"{key}: {value}")





