from simulator import robot, FORWARD, BACKWARD, STOP

if mode == "manual":
    print("Manual mode: use w/a/s/d to move, q to quit.")

running = True
while running:
    cmd = input("Command: ")

    if cmd == "w":
        robot.motors(FORWARD, FORWARD, 0.5)
    elif cmd == "a":
        robot.motors(STOP, FORWARD, 0.4)
    elif cmd == "d":
        robot.motors(FORWARD, STOP, 0.4)
    elif cmd == "s":
        robot.motors(BACKWARD, BACKWARD, 0.5)
    elif cmd == "q":
        running = False
    else:
        print("Not a valid command.")

if mode == "auto":
    print("Autonomous mode for 20 seconds.")

start = time.time()

while time.time() - start < 20:
    left = robot.left_sonar()
    right = robot.right_sonar()

    if left < 7 and right < 7:
        robot.motors(BACKWARD, BACKWARD, 0.5)
        robot.motors(STOP, FORWARD, 0.5)   # turn left
    elif left < 7:
        robot.motors(FORWARD, STOP, 0.4)   # turn right
    elif right < 7:
        robot.motors(STOP, FORWARD, 0.4)   # turn left
    else:
        robot.motors(FORWARD, FORWARD, 0.3)


else:
    print("Unknown mode. Exiting.")


# TODO: Write your code here!
# Use robot.motors() to move
# Use robot.left_sonar() and robot.right_sonar() to sense obstacles

# When you're done, close the simulator
robot.exit()