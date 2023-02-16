'''
Duda the rock monster lives in the enchanted forest and has collected N energy stones for lunch. Since he has a small mouth, he eats energy stones one at a time. Some stones are tougher than others! The i-th stone takes him Si seconds to eat.

Duda eats energy stones to get energy. Different stones give him different amounts of energy. Furthermore, the stones lose energy over time. The i-th stone initially contains Ei units of energy and will lose Li units of energy each second. When Duda starts to eat a stone, he will receive all the energy the stone contains immediately (no matter how much time it takes to actually finish eating the stone). The stone's energy stops decreasing once it hits zero.

What is the largest amount of energy Duda could receive from eating his stones?

Input
The first line of the input gives the number of test cases, T. T test cases follow. Each test case starts with a line containing the integer N, the number of energy stones Duda has. Then, there are N more lines, the i-th of which contains the three integers Si, Ei and Li, as described above.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the maximum amount of energy Duda could receive from eating stones.

<INPUT>
2
3
10 4 1000
10 3 1000
10 8 1000
2
10 2 0
10 3 0

<OUTPUT>
Case #1: 8
Case #2: 5
'''

N = int(input("Enter the number of test cases : "))
for i in range(N) :
    t = int(input("Enter the number of Energy stones : "))
    time = 0
    energy = 0
    for j in range(t) :
        x, y, z = input().split()
        s = int(x)
        e = int(y)
        l = int(z)
        energy = energy + e
        time = time + s
        if energy > 0 :
            energy = energy - (l*s)
        if energy <= 0 :
            energy = 0
    print("Total energy left : ", energy)
    print("Total time taken : ", time)
    print("\n")