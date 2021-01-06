input = """73
114
100
122
10
141
89
70
134
2
116
30
123
81
104
42
142
26
15
92
56
60
3
151
11
129
167
76
18
78
32
110
8
119
164
143
87
4
9
107
130
19
52
84
55
69
71
83
165
72
156
41
40
1
61
158
27
31
155
25
93
166
59
108
98
149
124
65
77
88
46
14
64
39
140
95
113
54
66
137
101
22
82
21
131
109
45
150
94
36
20
33
49
146
157
99
7
53
161
115
127
152
128"""

# https://adventofcode.com/2020/day/10

inputSplit = input.split("\n")
adaptors = {}
for i in inputSplit:
    iInt = int(i)
    if not adaptors.get(iInt):
        adaptors[iInt] = True
    else:
        print("duplicate adaptors detected")
        break

adaptorsSorted = sorted(adaptors.keys())
print(adaptorsSorted)
prevJolt = 0
oneJoltDiffs = 0
threeJoltDiffs = 0
for a in adaptorsSorted:
    diff = a - prevJolt
    if diff == 1:
        oneJoltDiffs = oneJoltDiffs + 1
    elif diff == 3:
        threeJoltDiffs = threeJoltDiffs + 1
    prevJolt = a

print("Product of number of 1-jolt differences multiplied by 3-jolt differences:")
print(oneJoltDiffs * (threeJoltDiffs + 1))
    
