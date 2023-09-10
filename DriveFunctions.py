# Drive Forward: Drive forward
# All motors spin forward
# @parameter inches: number of inches
def driveForward(inches):
    numTurns = inches / 12.0
    brain.screen.print("Drive Forward")
    brain.screen.next_row()
    LeftFront.spin_for(FORWARD, numTurns, TURNS, wait=False)
    RightFront.spin_for(FORWARD, numTurns, TURNS, wait=False)
    LeftRear.spin_for(FORWARD, numTurns, TURNS, wait=False)
    RightRear.spin_for(FORWARD, numTurns, TURNS, wait=False)
    
    # Wait for the motors to complete their spin
    while not LeftFront.is_done(): 
        pass
    return()

# Drive Reverse: Drive forward
# All motors spin reverse
# @parameter inches: number of inches to move
def driveReverse(inches):
    numTurns = inches / 12.0 # one turn of the motor = 12.0 inches movement
    brain.screen.print("Drive Reverse")
    brain.screen.next_row()
    LeftFront.spin_for(REVERSE, numTurns, TURNS, wait=False)
    RightFront.spin_for(REVERSE, numTurns, TURNS, wait=False)
    LeftRear.spin_for(REVERSE, numTurns, TURNS, wait=False)
    RightRear.spin_for(REVERSE, numTurns, TURNS, wait=False)
    
    # Wait for the motors to complete their spin
    while not LeftFront.is_done(): 
        pass
    return()

# Turn right: Tank turn, clockwise
# Left front and left rear spin forward
# Right front and right rear spin in reverse
# @parameter degrees: number of degrees (clockwise) to rotate
def turnRight(degrees):
    temp = degrees / 90.0 
    numTurns = temp * 1.16 # 1.16 rotations required for 90 degree turn
    brain.screen.print("Turn Right")
    brain.screen.next_row()
    LeftFront.spin_for(FORWARD, numTurns, TURNS, wait=False)
    LeftRear.spin_for(FORWARD, numTurns, TURNS, wait=False)
    RightFront.spin_for(REVERSE, numTurns, TURNS, wait=False)
    RightRear.spin_for(REVERSE, numTurns, TURNS, wait=False)
    
    # Wait for the motors to complete their spin
    while not LeftFront.is_done(): 
        pass
    return()

# Turn left: tank turn, counter clockwise
# Left front and left rear spin reverse
# Right front and right rear spin forward
# @parameter degrees: number of degrees (counter-clockwise) to rotate
def turnLeft(degrees):
    temp = degrees / 90.0 
    numTurns = temp * 1.16 # 1.16 rotations required for 90 degree turn
    brain.screen.print("TurnLeft")
    brain.screen.next_row()
    RightFront.spin_for(FORWARD, numTurns, TURNS, wait=False)
    RightRear.spin_for(FORWARD, numTurns, TURNS, wait=False)
    LeftFront.spin_for(REVERSE, numTurns, TURNS, wait=False)
    LeftRear.spin_for(REVERSE, numTurns, TURNS, wait=False)
    
    # Wait for the motors to complete their spin
    while not LeftFront.is_done(): 
        pass
    return()

# Drift Right: Move the robot right
# Left front and right rear spin forward
# Right front and left rear spin in reverse
# @parameter inches: number of inches to move right
def driftRight(inches):
    numTurns = inches /12.0 # one turn of the motor = 12.0 inches movement
    brain.screen.print("Drift Right")
    brain.screen.next_row()
    LeftFront.spin_for(FORWARD, numTurns, TURNS, wait=False)
    RightFront.spin_for(REVERSE, numTurns, TURNS, wait=False)
    LeftRear.spin_for(REVERSE, numTurns, TURNS, wait=False)
    RightRear.spin_for(FORWARD, numTurns, TURNS, wait=False)
    
    # Wait for the motors to complete their spin
    while not LeftFront.is_done(): 
        pass
    return()

# Drift Left: Move the robot left
# Left front and right rear spin in reverse
# Right front and left rear spin forward
# @parameter inches: number of inches to move left
def driftLeft(inches):
    numTurns = inches /12.0 # one turn of the motor = 12.0 inches movement
    brain.screen.print("Drift Left")
    brain.screen.next_row()
    LeftFront.spin_for(REVERSE, numTurns, TURNS, wait=False)
    RightFront.spin_for(FORWARD, numTurns, TURNS, wait=False)
    LeftRear.spin_for(FORWARD, numTurns, TURNS, wait=False)
    RightRear.spin_for(REVERSE, numTurns, TURNS, wait=False)
        
    # Wait for the motors to complete their spin
    while not LeftFront.is_done(): 
        pass
    return()

# Diagonal Right: Move the robot left
# Left front and right rear spin forward
# @parameter numTurns: number of inches to move
def diagonalRight(inches):
    numTurns = inches / 6.0 # one turn of the motor = 6.0 inches movement
    brain.screen.print("Diagonal Right")
    brain.screen.next_row()
    LeftFront.spin_for(FORWARD, numTurns, TURNS, wait=False)
    RightRear.spin_for(FORWARD, numTurns, TURNS, wait=False)
        
    # Wait for the motors to complete their spin
    while not LeftFront.is_done(): 
        pass
    return()

# Diagonal Left: Move the robot right
# Right front and left rear spin forward
# @parameter inches: number of inches to move
def diagonalLeft(inches):
    numTurns = inches / 6.0 # one turn of the motor = 6.0 inches movement
    brain.screen.print("Diagonal Left")
    brain.screen.next_row()
    RightFront.spin_for(FORWARD, numTurns, TURNS, wait=False)
    LeftRear.spin_for(FORWARD, numTurns, TURNS, wait=False)

    # Wait for the motors to complete their spin
    while not RightFront.is_done(): 
        pass
    return()