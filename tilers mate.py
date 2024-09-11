#cost of tile
cost_per_tile = float(input("Enter the cost per tile: "))

#area of floor
length = float(input("Enter the length of the room: "))
width = float(input("Enter the width of the room: "))
area = length * width

#area of tile
tile_length = float(input("Enter the length of the tile: "))
tile_width = float(input("Enter the width of the tile: "))
tile_area = tile_length * tile_width

#number of tiles
tiles = area / tile_area
print("Number of tiles needed:", tiles)

#total cost
total_cost = tiles * cost_per_tile
print("Total cost: ", total_cost)