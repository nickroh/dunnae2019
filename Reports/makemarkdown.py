s = '''

// 여기에 복붙

'''

s = s.replace('''나의 이름\n''', '## 봉사자 ')
s = s.replace('''
학생 이름
''', ', 배우미 ')

s = s.replace('''
수업 내용
''', '''

### 수업 내용

* ''')

s = s.replace('. ', '.\n* ')

s = s.replace('''
수업 내용
''', '''

### 수업 내용

* ''')
s = s.replace('''
이해도
''', '''

### 이해도

* ''')
s = s.replace('''
어려웠던 점
''', '''

### 어려웠던 점

* ''')
s = s.replace('''
수월했던 점
''', '''

### 수월했던 점

* ''')

s = s.replace('''
제안 및 느낀 점
''', '''

### 제안 및 느낀 점

* ''')

print('\n\n\n\n\n\n\n')
print(s)
print('\n\n\n\n\n\n\n')