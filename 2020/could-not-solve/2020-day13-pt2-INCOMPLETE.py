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
#  Link with congruence statements: https://www.reddit.com/r/adventofcode/comments/kc5a23/2020_day_13_part_2_chinese_remainder_theorem/gfo1f5f?utm_source=share&utm_medium=web2x&context=3
