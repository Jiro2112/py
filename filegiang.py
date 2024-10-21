#dao chuoi
s="abcdefgh"
print(s[3:6])
print("--")
print(s[3:6:2])
print("--")
print(s[::])
print("--")
print(s[::-1])
print("--")
print(s[4:1:-2])
#viet binh thuong
s=input()
for index in range(len(s)):
    if s[index] == 'i' or s[index] == 'u':
        print("there is an i or  u")
#viet theo phong cach python
for char in s:
    if char=='i' or char=='u':
        print("there is an i or_u")
# kiem tra tu co trong chuoi hay khoong
string="Python is easy"
print('P'in string)
print('K'not in string)
# #thay bang cach tao chuoi moi
a='python'
a=a.replace('py','e')
print(a)
#so sanh chuoi
s1='Python'
s2='Python'
s3='Java'
s4='123456'
s5='123456'
print(s1==s2)
print(s4<s5)
print(s3>s1)
#kiem tra tu giong nhau
s='mit u rock'
s2='i rule mit'
if len(s)==len(s2):
    for char1 in s:
        for char2 in s2:
            if char1==char2:
                print(char1)
                break
print('----------------------------------------------------------------')
#