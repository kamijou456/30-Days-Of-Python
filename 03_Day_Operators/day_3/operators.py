
base = input('Base of Triangle: ')
height = input('Height of Triangle: ')
area = 0.5 * float(base) * float(height)

print('Area of the Triangle:',area)

side_a = input('Enter Length of Side A: ')
side_b = input('Enter Length of Side B: ')
side_c = input('Enter Length of Side C: ')
perimeter = float(side_a) + float(side_b) + float(side_c)

print('Perimeter of Triangle:', perimeter)

x = 1
y = 1

while x <= 5:
    z = x * y
    a = z * x
    b = a * z
    print(x, y, z, a, b)
    x += 1

print('Is there an on in jargon and python?','on' in 'jargon' and 'on' in 'python')

print('Is jargon in the sentence. I hope this course is not full of jargon? ', 'jargon' in 'I hope this course is not full of jargon')