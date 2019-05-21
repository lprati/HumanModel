def setup():
    fill(0,0,0)
    size(1280, 720, P3D)

def draw():    
    beginCamera()
    camera()
    
    translate(150,150,-300)
    #rotateY()
    for j in range(0,720,5):
        for i in range(0,1280,5):
            draw_human_model(176)
            translate(i,j)
    endCamera()
    
def draw_cylinder(sides, r, h):
    angle = 360/sides
    half_height = h/2
    
    # Top shape
    beginShape()
    for i in range(sides):
        x = cos(radians(i * angle)) * r
        y = sin(radians(i * angle)) * r
        vertex(x, y, h)
    endShape(CLOSE)
    
    # Bottom shape
    beginShape()
    for i in range(sides):
        x = cos(radians(i * angle)) * r
        y = sin(radians(i * angle)) * r
        vertex(x, y, 0)
    endShape(CLOSE)

    beginShape(TRIANGLE_STRIP)
    for i in range(sides + 1):
        x = cos(radians(i * angle)) * r
        y = sin(radians(i * angle)) * r
        vertex(x, y, 0)
        vertex(x, y, h)
    endShape(CLOSE)
    
# Given the number of pixels that correspond with average human height,
# draws a human model solid with pre-fixed aspect ratios
def draw_human_model(avg_height_in_pixels):
    
    """
    The human body 3D model, using the default size of cylinders as described in:
        Zhong Zhang, Peter L. Venetianer, Alan J. Lipton. A Robust Human Detection and Tracking System
        Using a Human-Model-Based Camera Calibration. The Eighth International Workshop on Visual Surveillance - VS2008
    """
    fill(255,255,255)
    stroke(255,255,255)    
    # Head
    head_height_ratio = 0.1534
    head_radius_ratio = 0.0511
    
    # Torso
    torso_height_ratio = 0.3797
    torso_radius_ratio = 0.1193
    
    # Leg
    leg_height_ratio = 0.4488
    leg_radius_ratio = 0.0681
    
    # Number of faces in cylinder
    faces = 60
    translated_height = 0
    
    r = leg_radius_ratio * avg_height_in_pixels
    h = leg_height_ratio * avg_height_in_pixels
    draw_cylinder(faces, r, h)
    translate(0,0,h)
    translated_height += h
    
    r = torso_radius_ratio * avg_height_in_pixels
    h = torso_height_ratio * avg_height_in_pixels
    draw_cylinder(faces, r, h)
    translate(0,0,h)
    translated_height += h
    
    r = head_radius_ratio * avg_height_in_pixels
    h = head_height_ratio * avg_height_in_pixels
    draw_cylinder(faces, r, h)

    # Repositioning draw plane
    translate(0,0,-translated_height)
        
    
