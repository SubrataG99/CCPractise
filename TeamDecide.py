'''
Problem
As the football coach at your local school, you have been tasked with picking a team of exactly P students to represent your school. There are N students for you to pick from. The i-th student has a skill rating Si, which is a positive integer indicating how skilled they are.

You have decided that a team is fair if it has exactly P students on it and they all have the same skill rating. That way, everyone plays as a team. Initially, it might not be possible to pick a fair team, so you will give some of the students one-on-one coaching. It takes one hour of coaching to increase the skill rating of any student by 1.

The competition season is starting very soon (in fact, the first match has already started!), so you'd like to find the minimum number of hours of coaching you need to give before you are able to pick a fair team.

Input
The first line of the input gives the number of test cases, T. T test cases follow. Each test case starts with a line containing the two integers N and P, the number of students and the number of students you need to pick, respectively. Then, another line follows containing N integers Si; the i-th of these is the skill of the i-th student.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the minimum number of hours of coaching needed, before you can pick a fair team of P students.

------------+++++++++++++++---------------++++++++++++++++++
<INPUT>
3
4 3
3 1 9 100
6 2
5 5 1 2 3 4
5 5
7 7 1 7 7

<OUTPUT>
Case #1: 14
Case #2: 0
Case #3: 6
'''

T = int(input("Enter number of test cases : "))
for i in range(T) :
    N, P = [int(x) for x in input().split()]
    S = [int(x) for x in input().split()]
    inc = S
    dec = S
    inc.sort()
    maxInc = inc[P-1]
    IncTime = DecTime = 0
    for j in range(P) :
        IncTime += maxInc - inc[j]
    dec.sort(reverse = True)
    maxDec = dec[0]
    for j in range(P) :
        DecTime += maxDec - dec[j]
    if IncTime <= DecTime :
        print("Total inc time : ", IncTime, '\n')
    else :
        print("Total time : ", DecTime, '\n')