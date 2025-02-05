week = input('Enter week name: ').upper()
if week in ['MON','TUE','WED','THU','FRI','SAT','SUN','MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']:
    match(week[0:3]):
        case 'MON'|'TUE'|'WED'|'THU'|'FRI':
            print('Working Day')
        case 'SAT'|'SUN':
            print('WeekOff')
else:
    print('Enter valid day')