import getopt
import sys
from math import sqrt, ceil
import datetime


def main(argv):
    h = 0
    g = 0
    p = 0
    try:
        opts, args = getopt.getopt(argv, "h:g:p:")
    except getopt.GetoptError:
        print('For Solving DLP in Form of "h = g^x mod p" enter:')
        print('BabyStepGiantStep.py -h <12345> -g <12345> -p <12345>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            h = int(arg)
        elif opt == '-g':
            g = int(arg)
        elif opt == '-p':
            p = int(arg)
    print("\n------ Baby Step Giant Step DL Solver ------")
    print("Equation: " + str(h) + " = " + str(g) + " ^ x (mod " + str(p) + ")")
    print("calculating...")
    solveDLOG(h, g, p)


def solveDLOG(h, g, p):
    timeStart = datetime.datetime.now()
    N = ceil(sqrt(p - 1))
    f = pow(g, (N*(p-2)), p)
    babyStep = calcBabyStep(g, p, N)
    if len(babyStep) < 60:
        print("BabySteps: " + str(babyStep))
    else:
        print("BabySteps: Too many for printing")
    calcGiantAndCompare(h, f, N, p, babyStep, timeStart)


def calcBabyStep(g, p, N):
    babyStep = {1: 0, g: 1}
    lastValue = g
    print()
    for i in range(2, N):
        newValue = (lastValue * g) % p
        babyStep[newValue] = i
        lastValue = newValue
    return babyStep


def calcGiantAndCompare(h, f, N, p, babyStep, timeStart):
    lastInsert = (h * f) % p
    giantStep = {0: h, 1: lastInsert}

    if h in babyStep.keys():
        solution = babyStep.get(h)
        timeEnd = datetime.datetime.now()
        timeDelta = timeEnd - timeStart
        print("GiantSteps up to Solution: " + str(giantStep))
        print("\nSolution x = " + str(solution))
        return

    elif lastInsert in babyStep:
        solution = babyStep.index(lastInsert) + 1 * N
        timeEnd = datetime.datetime.now()
        timeDelta = timeEnd - timeStart
        print("GiantSteps up to Solution: " + str(giantStep))
        print("\nSolution x = " + str(solution))
        return

    for j in range(2, N):
        nextInsert = (lastInsert * f) % p
        giantStep[j] = nextInsert
        if nextInsert in babyStep.keys():
            solution = babyStep.get(nextInsert) + j * N
            timeEnd = datetime.datetime.now()
            timeDelta = timeEnd - timeStart
            if len(giantStep) < 60:
                print("GiantSteps up to Solution: " + str(giantStep))
            else:
                print("GiantSteps: Too many for printing")
            print("\nSolution x = " + str(solution))
            print("Calculation took " + str(timeDelta.total_seconds()) + " Seconds")
            return
        lastInsert = nextInsert
    timeEnd = datetime.datetime.now()
    timeDelta = timeEnd - timeStart
    print ("\nNo Solution found!")
    print("Calculation took " + str(timeDelta.total_seconds()) + " Seconds")


if __name__ == "__main__":
    main(sys.argv[1:])
