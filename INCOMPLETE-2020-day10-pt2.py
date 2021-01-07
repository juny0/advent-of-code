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

testInput = """16
10
15
5
1
11
7
19
6
12
4"""

import queue

def evaluate(currAdaptor, adaptorsList, adaptorsDict, chain, numArrangements):
    chain.put(currAdaptor)
    availableNextAdaptors = []
    #print("---")
    #print("current adaptor: " + str(currAdaptor))
    #print("current num arrangements: " + str(numArrangements))
    for i in range(1,4):
        nextAdaptor = adaptorsDict.get(currAdaptor + i)
        if nextAdaptor:
            availableNextAdaptors.append(currAdaptor + i)
    #print("next available adaptors: " + str(availableNextAdaptors))
    
    # adaptor chain is an elgible candidate
    if len(availableNextAdaptors) == 0 and currAdaptor == adaptorsList[len(adaptorsList) - 1]:
        #print("*****")
        #print("chain:" + str(chain.queue))
        #print("*****")
        return numArrangements + 1
    if len(availableNextAdaptors) == 0:
        return numArrangements
    for i in availableNextAdaptors:
        numArrangements = evaluate(i, adaptorsList, adaptorsDict, chain, numArrangements)
        #print("current num arrangements in loop: " + str(numArrangements))
    chain.get()
    # print("return from recursion")
    # print("current adaptor: " + str(currAdaptor))
    # print("returning current num arrangements: " + str(numArrangements))
    return numArrangements
    

def run(inp):
    inputSplit = inp.split("\n")
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
    arrangements = evaluate(0, adaptorsSorted, adaptors, queue.LifoQueue(), 0)
    print("Number of valid arrangements:")
    print(arrangements)

run(testInput) 
run(input)
    
