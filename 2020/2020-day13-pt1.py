input = """1002618
19,x,x,x,x,x,x,x,x,41,x,x,x,37,x,x,x,x,x,367,x,x,x,x,x,x,x,x,x,x,x,x,13,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,29,x,373,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,23"""

testInput = """939
7,13,x,x,59,x,31,19"""

def run(input):
    iParsed = input.split("\n")
    earliestTimeToDepart = int(iParsed[0])
    buses = iParsed[1].split(",")
    earliestBus = 0
    earliestBusTime = 0
    for bus in buses:
        if bus == "x":
            continue
        bus = int(bus)
        thisBusDepartsAt = 0
        # calculate earliest bus after earliest time to depart
        # divide earliest time to depart by bus number
        # if number is a float, round up
        div = earliestTimeToDepart / bus
        if isinstance(div, float):
            div = earliestTimeToDepart // bus + 1
            thisBusDepartsAt = bus * div
        elif isinstance(div, int):
            thisBusDepartsAt = bus * div
        else:
            print("error: div is neither float or int")
            break
        if earliestBusTime == 0 or thisBusDepartsAt < earliestBusTime:
            earliestBus = bus
            earliestBusTime = thisBusDepartsAt
    print("What is the ID of the earliest bus you can take to the airport multiplied by the number of minutes you'll need to wait for that bus?")
    waitTime = earliestBusTime - earliestTimeToDepart
    print(earliestBus * waitTime)
    
    
run(testInput)
run(input)
