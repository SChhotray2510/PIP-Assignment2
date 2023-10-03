def are_points_collinear(x1, y1, x2, y2, x3, y3):
   
 slope1 = (y2 - y1) / (x2 - x1) if x2 - x1 != 0 else float('inf')
 slope2 = (y3 - y2) / (x3 - x2) if x3 - x2 != 0 else float('inf')
    
   
 return slope1 == slope2 or (slope1 == float('inf') and slope2 == float('inf'))


x1, y1 = 1, 1
x2, y2 = 2, 2
x3, y3 = 3, 3

result = are_points_collinear(x1, y1, x2, y2, x3, y3)
print("Points are collinear." if result else "Points are not collinear.")
