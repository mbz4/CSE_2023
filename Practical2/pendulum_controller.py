import math

def control_function(angle, angular_velocity, time):
    # return max(min(2*(math.pi - angle) - 0.5*angular_velocity, 1), -1) #6*math.sin(angle) 
    return -1