#The class creates "crosses" and "squares".
#Cross = The intersection between lines.
#Squares = The "boxes" with numbers that indicates how many surrounding lines.
#TODO #Could have a better class-name! But the last name, squares, was confusing. Remove comment if accepted.
class Controllers:
    def __init__(self, value, target_count, start_index):
        self.value = value                  #Value is defined as used/not used for "cross" (=0,2) and by how many connections for the "squares" (0-3).
        self.target_count = target_count    #Target count is the number of necessary intersections/accepted lines.
        self.start_count = start_index      #