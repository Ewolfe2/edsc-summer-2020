# import matplotcheck.base as mpc


#
# def variables_test_int(precip_int):
#     try:
#         return (
#             "Variable precip_int has been assigned the value " + str(precip_int) + "."
#         )
#         if isinstance(precip_int, int):
#             return "Variable precip_int is an integer, good job!"
#             if precip_int == 46:
#                 return "Variable precip_int equals 46, good job!"
#             else:
#                 return (
#                     "Variable precip_int exists and is an integer, but has the wrong value.\n",
#                     "Make sure you assigned the value of precip_int to be a whole number closest\n",
#                     "to the average annual rainfall in NYC.",
#                 )
#         else:
#             return (
#                 "Variable precip_int exists, but is not an integer.\n",
#                 "Make sure you assigned the value of precip_int to be a whole number.",
#             )
#
#     except NameError:
#         return (
#             "Can't find a variable named precip_int, make sure you've\n",
#             "correctly spelled the variable name and assigned it a value!",
#         )
#
#
# def variables_test_float(precip_float):
#     try:
#         return (
#             "Variable precip_float has been assigned the value "
#             + str(precip_float)
#             + "."
#         )
#         if isinstance(precip_float, float):
#             return "Variable precip_float is a float, good job!"
#             if precip_float == 46.23:
#                 return "Variable precip_float equals 46.23, good job!"
#             else:
#                 return (
#                     "Variable precip_float exists and is a float, but has the wrong value.\n",
#                     "Make sure you assigned the value of precip_float to be equivalent\n",
#                     "to the average annual rainfall in NYC.",
#                 )
#         else:
#             return (
#                 "Variable precip_float exists, but is not a float.\n",
#                 "Make sure you assigned the value of precip_float to be a number with a decimal value.",
#             )
#     except NameError:
#         return (
#             "Can't find a variable named precip_float, make sure you've\n",
#             "correctly spelled the variable name and assigned it a value!",
#         )
#
#
# def variables_test_string(location):
#     try:
#         return "Variable location has been assigned the value " + str(location) + "."
#         if isinstance(location, str):
#             return "Variable location is a string, good job!"
#             if location == "New York City":
#                 return "Variable location equals New York City, good job!"
#             else:
#                 return (
#                     "Variable location exists and is a string, but has the wrong value.\n",
#                     "Make sure you assigned the value of location to be \n",
#                     "a string of the location: New York City.",
#                 )
#         else:
#             return (
#                 "Variable location exists, but is not a string.\n",
#                 "Make sure you assigned the value of location to be a value surrounded by quotes.",
#             )
#     except NameError:
#         return (
#             "Can't find a variable named location, make sure you've\n",
#             "correctly spelled the variable name and assigned it a value!",
#         )


def lists_test_precip_by_location(precip_by_location):
    """Test to ensure precip_by_location list contains all of the laid
    out requirements provided in the notebook."""
    return_message = ""
    if isinstance(precip_by_location, list):
        return_message += "precip_by_location is a list!"
        if len(precip_by_location) == 3:
            return_message += "\nprecip_by_location has the correct length!"
            if isinstance(precip_by_location[2], str):
                return_message += (
                    "\nprecip_by_location contains a string value at index 2!"
                )
            else:
                return_message += """
precip_by_location does not contain a string value at index 2.
Make sure to add a string value at list index 2.
Remember python list indexing starts at 0!"""
        else:
            return_message += """
precip_by_location does not have the correct length.
Make sure that the list has exactly 3 values in it."""
        if any([isinstance(i, str) for i in precip_by_location]):
            return_message += "\nprecip_by_location contains a string value!"
        else:
            return_message += """
precip_by_location does not contain a string value.
Make sure to make one of the values in your list a string."""
        if any([isinstance(i, float) for i in precip_by_location]):
            return_message += "\nprecip_by_location contains a float value!"
        else:
            return_message += """
precip_by_location does not contain a float value.
Make sure to make one of the values in your list a float."""
    else:
        return_message += """
precip_by_location is not a list. Make sure that you formatted the list
correctly and spelled the variable name correctly."""
    return return_message


def lists_test_precip_by_location_modify(precip_by_location):
    """Test to ensure that precip_by_location was correctly modified."""
    answer = [1, 20.23, "inches", "Boulder", "Colorado"]
    return_message = ""

    if precip_by_location == answer:
        return_message = "You correctly modified the list, good job!"
    else:
        return_message = """
Your list didn't match the expected list. Here is the list you produced:
{}""".format(
            precip_by_location
        )
    return return_message


def operators_test_march_precip(march_precip_mm):
    """Test to make sure that march_precip_mm was assigned correctly"""
    if march_precip_mm == 46.99:
        return "Correctly assigned march_precip_mm to be 46.99!"
    else:
        return """
march_precip_mm doesn't equal 46.99, it instead equals {}.
Make sure your arithmetic operators are accurate and correctly assigned
to the variable.""".format(
            march_precip_mm
        )


def operators_test_nyc_precip(annual_avg_precip_nyc):
    """Test to make sure that annual_avg_precip_nyc was assigned correctly"""
    if annual_avg_precip_nyc == 46.23:
        return "Variables added correctly!"
    else:
        return """
Variables not added correctly, the variable total_precip_nyc is assigned
{}.""".format(
            annual_avg_precip_nyc
        )


def operators_test_operation_modifications(relational, identity, membership, logical):
    """Tests to see if the operations have been modified correctly"""
    operations = [relational, identity, membership, logical]
    operation_names = ["relational", "identity", "membership", "logical"]

    return_message = ""

    if all(operations):
        return_message = "All operations are now returning True, good job!"
    else:
        for i, operation in enumerate(operations):
            if not operation:
                return_message += """
Your {} operation is still returning False,
check to see why that may be!""".format(
                    operation_names[i]
                )
    return return_message
