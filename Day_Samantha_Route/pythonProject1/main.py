from drone import Drone

drone_is_on = True

while drone_is_on:
    file_name = input("Enter the next route instructions file or enter STOP to finish: ")

    if file_name == "STOP":
        print("End Programme")
        drone_is_on = False

    file = open(file_name, "r")

    raw_file_data = file.readlines()
    file_data = []

    for line in raw_file_data:
        if line[-1] == "\n":
            file_data.append(line[:-1])
        else:
            file_data.append(line)

    start_cor = list(map(int, file_data[:2]))
    directions = file_data[2:]

    x_cor = [start_cor[0]]
    y_cor = [start_cor[1]]

    drone = Drone()

    for direction in directions:
        if direction == "N":
            drone.move_north(x_cor,y_cor)
            print(f"({x_cor[-1]},{y_cor[-1]})")
        elif direction == "S":
            drone.move_south(x_cor,y_cor)
            print(f"({x_cor[-1]},{y_cor[-1]})")
        elif direction == "E":
            drone.move_east(x_cor,y_cor)
            print(f"({x_cor[-1]},{y_cor[-1]})")
        elif direction == "W":
            drone.move_west(x_cor,y_cor)
            print(f"({x_cor[-1]},{y_cor[-1]})")

        if x_cor[-1] < 0 or x_cor[-1] > 12:
            print("Drone is out of range")
            break
        elif y_cor[-1] < 0 or y_cor[-1] > 12:
            print("Drone is out of range")
            break

    drone.place_drone(x_cor,y_cor)
