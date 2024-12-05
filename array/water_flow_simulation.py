def print_terrain(heights):
    # Find the maximum height to know how many rows we need
    max_height = max(heights)
    
    # Print terrain from top to bottom
    for height in range(max_height, 0, -1):
        # For each level, print either a block or space
        for column in heights:
            if column >= height:
                print('#', end=' ')
            else:
                print(' ', end=' ')
        print()  # New line after each row
    
    # Print the bottom line with indices
    for i in range(len(heights)):
        print(i, end=' ')
    print()

# Test with your example
terrain = [5, 4, 3, 2, 1, 3, 4, 0, 3, 4]
print_terrain(terrain)


def simulate_water(heights, water_column, water_units):
    n = len(heights)
    water_levels = [0] * n  # Array to track water at each position
    
    # Add initial water
    water_levels[water_column] = water_units
    
    # Keep simulating until water settles
    while True:
        changed = False
        for i in range(n):
            current_height = heights[i] + water_levels[i]
            
            # Check left neighbor
            if i > 0:
                left_height = heights[i-1] + water_levels[i-1]
                if current_height > left_height + 1:
                    # Water flows left
                    flow = (current_height - left_height) // 2
                    water_levels[i] -= flow
                    water_levels[i-1] += flow
                    changed = True
            
            # Check right neighbor
            if i < n-1:
                right_height = heights[i+1] + water_levels[i+1]
                if current_height > right_height + 1:
                    # Water flows right
                    flow = (current_height - right_height) // 2
                    water_levels[i] -= flow
                    water_levels[i+1] += flow
                    changed = True
        
        if not changed:  # Water has settled
            break
    
    return water_levels

def print_terrain_with_water(heights, water_levels):
    max_height = max(max(heights) + max(water_levels), max(heights))
    
    # Print terrain and water from top to bottom
    for height in range(max_height, 0, -1):
        for i in range(len(heights)):
            total_height = heights[i] + water_levels[i]
            if total_height >= height:
                if heights[i] >= height:
                    print('#', end=' ')  # Terrain
                else:
                    print('~', end=' ')  # Water
            else:
                print(' ', end=' ')
        print()
    
    # Print the bottom line with indices
    for i in range(len(heights)):
        print(i, end=' ')
    print()

# Test with your example
terrain = [5, 4, 3, 2, 1, 3, 4, 0, 3, 4]
water_column = 3  # Drop water at index 3
water_units = 4   # Drop 4 units of water

water_levels = simulate_water(terrain, water_column, water_units)
print("Terrain with water:")
print_terrain_with_water(terrain, water_levels)
