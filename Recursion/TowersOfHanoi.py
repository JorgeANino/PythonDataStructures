def towers_of_hanoi(numberOfDisks,startPeg=1,endPeg=3):
    if numberOfDisks:
        towers_of_hanoi(numberOfDisks-1,startPeg,6-startPeg-endPeg)
        print("Moving %d from peg %d to peg %d" %(numberOfDisks,startPeg,endPeg))
        towers_of_hanoi(numberOfDisks-1,6-startPeg-endPeg,endPeg)

towers_of_hanoi(6)