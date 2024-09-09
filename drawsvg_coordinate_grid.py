import drawsvg as draw

# Create a 200x200 canvas with the origin at the center
d = draw.Drawing(200, 200, origin='center')

# Draw the grid lines (every 20 units)
for i in range(-90, 100, 10):
    if i != 0:  # Skip the axis lines
        d.append(draw.Line(i, -100, i, 100, stroke='#e5e5e5', stroke_width=3))  # Vertical lines
        d.append(draw.Line(-100, i, 100, i, stroke='#e5e5e5', stroke_width=3))  # Horizontal lines

# Draw the horizontal and vertical axes
d.append(draw.Line(-100, 0, 100, 0, stroke='#afafaf', stroke_width=3))  # X-axis
d.append(draw.Line(0, -100, 0, 100, stroke='#afafaf', stroke_width=3))  # Y-axis

# Mark a point at (3, 4)
d.append(draw.Circle(3*10, 4*10, 5, fill='#1cb0f6', stroke_width=2, stroke='white'))  # Scale the coordinates by 10 for visibility

# Optional: Label the point (3, 4)
d.append(draw.Text('(3, 4)', 10, 3*10+10, 4*10+10, fill='#1cb0f6'))

# Display and save
d.set_pixel_scale(2)
d.save_svg('coordinate_grid_with_point.svg')