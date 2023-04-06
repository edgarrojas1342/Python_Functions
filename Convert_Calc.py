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

def print_results(value, value_unit, converted_value, cv_unit):
    print(f"The result is {value} {value_unit} = {converted_value:.2f} {cv_unit}")

def perform_conversion(value, conversion_direction):
    #convert the length using appropriate function
    #in to mm
    value_unit = ""
    cv_unit = ""

    if conversion_direction == "in->mm":
        converted_value = inches_to_mm(value)
        value_unit = "inches"
        cv_unit = "mm"
    #mm to in
    elif conversion_direction == "mm->in":
        converted_value = mm_to_inches(value)
        value_unit = "mm"
        cv_unit = "inches"
    #ft to m
    elif conversion_direction == "ft->m":
        converted_value = feet_to_meter(value)
        value_unit = "feet"
        cv_unit = "meters"
    #m to ft
    elif conversion_direction == "m->ft":
        converted_value = meters_to_feet(value)
        value_unit = "meters"
        cv_unit = "feet"
    #F to C
    elif conversion_direction == "F->C":
        converted_value = F_to_C(value)
        value_unit = "F"
        cv_unit = "C"
    #C to F
    elif conversion_direction == "C->F":
        converted_value = C_to_F(value)
        value_unit = "C"
        cv_unit = "F"
    else:
        print("Invalid conversion direction")

    print_results(value, value_unit, converted_value, cv_unit)


while True:
    # get the length from the user
    conversion_direction = input("Enter conversion direction (in->mm, mm->in, ft->m, m->ft, C->F, F->C ) or 'q' to quit: ")

    #exit the loop if user types q
    if conversion_direction == 'q':
        break

    value = float(input("Enter value to be converted: "))

    perform_conversion(value, conversion_direction)


print ('Thanks for using The Calculator')