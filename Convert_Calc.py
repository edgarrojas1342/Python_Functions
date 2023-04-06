#conversion functions
def inches_to_mm(length_in_inches):
    length_in_mm = length_in_inches * 25.4
    return length_in_mm

def mm_to_inches(length_in_mm):
    length_in_inches = length_in_mm / 25.4
    return length_in_inches

def feet_to_meter(length_in_feet):
    length_in_meters = length_in_feet * 0.3048
    return length_in_meters

def meters_to_feet(length_in_meters):
    length_in_feet = length_in_meters / 0.3048
    return length_in_feet

def F_to_C(temp_in_F):
    temp_in_C = (temp_in_F -32) * 5/9
    return temp_in_C

def C_to_F(temp_in_C):
    temp_in_F = (temp_in_C *9/5 + 32)
    return temp_in_F

def perform_conversion(value, conversion_direction):
    #convert the length using appropriate function
    #in to mm
    if conversion_direction == "in->mm":
        converted_value = inches_to_mm(value)
        print (f"{value} inches = {converted_value} mm")
    #mm to in
    elif conversion_direction == "mm->in":
        converted_value = mm_to_inches(value)
        print (f"{value} mm = {converted_value} inches")
    #ft to m
    elif conversion_direction == "ft->m":
        converted_value = feet_to_meter(value)
        print (f"{value} feet = {converted_value} meters")

    else:
        print("Invalid conversion direction")

while True:
    # get the length from the user
    conversion_direction = input("Enter conversion direction (in->mm, mm->in, ft->m) or 'q' to quit: ")

    #exit the loop if user types q
    if conversion_direction == 'q':
        break

    value = float(input("Enter value to be converted: "))

    perform_conversion(value, conversion_direction)


print ('Thanks for using The Calculator')