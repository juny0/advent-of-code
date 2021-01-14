########### COMMENTS ON DAY 13 PART 2 ###########
# Many solutions make use of mildly brute forcing the solution by
#  finding the LCM of all the buses (or simply multiplying the buses together since they are all primes)
#  and using that as the step size for incrementing the value of the timestamp.
#  At first I was planning to go down this route after wrestling with Day 13 Part 2 for multiple
#  consecutive days, still struggling even after looking up solutions and tips online.
#  The reason being that I never learned about the Chinese Remainder Theorem and it has no application in my life.
#  However, none of the solutions using LCM to brute force the timestamp mathematically proved my following concern:
#    - How can you guarantee that there is no value 't' in between increments of the LCM of the buses
#      such that '(t + offset) % bus = 0'? This math stackexchange link 
#      https://math.stackexchange.com/questions/2218763/how-to-find-lcm-of-two-numbers-when-one-starts-with-an-offset
#      seems to provide that (not sure if it's a formal proof), but it looks more confusing than the Chinese Remainder Theorem.
#
# Below are links to resources I used to vaguely understand the solution
#  - congruence statements: https://www.reddit.com/r/adventofcode/comments/kc5a23/2020_day_13_part_2_chinese_remainder_theorem/gfo1f5f?utm_source=share&utm_medium=web2x&context=3
#  - congruence section in wikipedia to format offset statements: https://en.wikipedia.org/wiki/Modular_arithmetic#Congruence althought it turns out this wasnt necessary
#  - how to solve CRT https://www.youtube.com/watch?v=zIFehsBHB8o&feature=youtu.be

input = """19,x,x,x,x,x,x,x,x,41,x,x,x,37,x,x,x,x,x,367,x,x,x,x,x,x,x,x,x,x,x,x,13,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,29,x,373,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,23"""

testInput = """7,13,x,x,59,x,31,19"""

def modInverse(N_i, mod): 
    for i in range(1, mod): 
        if ((N_i * i) % mod == 1): 
            return i 
    return 1

def run(input):
    buses = input.split(",")

    # Notes on setting up modular equation in format for CRT
    # x_i + offset ≡ 0 (mod bus)
    # x_i ≡ -offset (mod bus)         ## subtraction
    # x_i ≡ (-offset % bus) (mod bus) ## apply modulus to simplify equation because remainder can't be negative
    # x_i ≡ b_i (mod n_i)
    # n_i = bus
    # b_i = -offset % bus
    
    # For CRT, N is the product of all moduluses
    N = 1
    # Calculate N
    for offset in range(0,len(buses)):
        if buses[offset] == "x":
            continue
        bus = int(buses[offset])
        N *= bus
    
    # Apply CRT
    sum = 0
    for offset in range(0,len(buses)):
        if buses[offset] == "x":
            continue
        bus = int(buses[offset])
        
        # b_i = -offset % bus
        b_i = (-1 * offset) % bus
        print("x_i ≡ " + str(b_i) + "mod(" + str(bus) + ")")
        
        # n_i = bus
        # N_i = N / n_i
        N_i = N // bus # do not use floats for some reason
        
        # x_i is the inverse of N_i
        # which can be found by
        # N_i * x ≡ 1 (mod n_i)
        x_i = modInverse(N_i, bus)
        b_iN_ix_i = b_i * N_i * x_i
        print(b_iN_ix_i)
        sum += b_iN_ix_i

    print("What is the earliest timestamp such that all of the listed bus IDs depart at offsets matching their positions in the list?") 
    print(sum % N)
    print("")
    print("")
    return sum % N
            
result = run(testInput)
if result != 1068781:
    print("You Got The Wrong Answer")
    
test2 = "17,x,13,19"
result = run(test2)
if result != 3417:
    print("You Got The Wrong Answer")
    
test6 = "1789,37,47,1889"
result = run(test6)
if result != 1202161486:
    print("You Got The Wrong Answer")

run(input)
