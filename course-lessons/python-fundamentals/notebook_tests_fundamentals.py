import matplotcheck.base as mpc

# TESTS FOR THE VARIABLES NOTEBOOK
def variables_test_int(precip_int):
    """Testing that the integer variable was correctly assigned."""
    return_message = ""

    if isinstance(precip_int, int):
        return_message += "Variable precip_int is an integer, good job!\n"
        if precip_int == 46:
            return_message += "Variable precip_int equals 46, good job!"
        else:
            return_message += """Variable precip_int exists and is an integer,
but has the wrong value.
Make sure you assigned the value of precip_int to be a whole number closest
to the average annual rainfall in NYC."""
    else:
        return_message += """Variable precip_int exists, but is not an integer.
Make sure you assigned the value of precip_int to be a whole number."""

    return return_message


def variables_test_float(precip_float):
    """Testing that the float variable was correctly assigned."""
    return_message = ""

    if isinstance(precip_float, float):
        return_message += "Variable precip_float is a float, good job!\n"
        if precip_float == 46.23:
            return_message += "Variable precip_float equals 46.23, good job!"
        else:
            return_message += """Variable precip_float exists and is a float,
but has the wrong value.
Make sure you assigned the value of precip_float to be equivalent
to the average annual rainfall in NYC."""
    else:
        return_message += """Variable precip_float exists, but is not a float.
Make sure you assigned the value of precip_float to be a number
with a decimal value."""

    return return_message


def variables_test_string(location):
    """Testing that the string variable was correctly assigned."""
    return_message = ""

    if isinstance(location, str):
        return_message += "Variable location is a string, good job!\n"
        if location == "New York City":
            return_message += "Variable location equals New York City!"
        else:
            return_message += """Variable location exists and is a string,
but has the wrong value.
Make sure you assigned the value of location to be
a string of the location: New York City."""
    else:
        return_message += """Variable location exists, but is not a string.
Make sure you assigned the value of location
to be a value surrounded by quotes."""

    return return_message


# TESTS FOR THE LISTS NOTEBOOK
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
        return_message = """Your list didn't match the expected list. Here is
the list you produced:
{}""".format(
            precip_by_location
        )

    return return_message


# TESTS FOR THE OPERATORS NOTEBOOK
def operators_test_march_precip(march_precip_mm):
    """Test to make sure that march_precip_mm was assigned correctly"""
    if march_precip_mm == 46.99:
        return "Correctly assigned march_precip_mm to be 46.99!"
    else:
        return """march_precip_mm doesn't equal 46.99, it instead equals {}.
Make sure your arithmetic operators are accurate and correctly assigned
to the variable.""".format(
            march_precip_mm
        )


def operators_test_nyc_precip(annual_avg_precip_nyc):
    """Test to make sure that annual_avg_precip_nyc was assigned correctly"""
    if annual_avg_precip_nyc == 46.23:
        return "Variables added correctly!"
    else:
        return """Variables not added correctly, the variable total_precip_nyc
is assigned
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
                return_message += """Your {} operation is still returning False,
check to see why that may be!""".format(
                    operation_names[i]
                )

    return return_message

# TESTS FOR THE EXERCISE NOTEBOOK
def exercise_test_months_list(months):
    """Testing that the months list created is correct"""
    correct_month_names = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "June",
        "July",
        "Aug",
        "Sept",
        "Oct",
        "Nov",
        "Dec",
    ]

    if months == correct_month_names:
        return """List of month names successfully assigned and has correct values!"""
    else:
        error_msg = """There is a variable named 'months', but it is assigned
these values: {}
Please ensure that the values are strings with the month names
from the table above."""
        return error_msg.format(months)


def exercise_test_precip_list(precip):
    """Testing that the precip list created is correct"""
    correct_month_precip = [
        17.779999999999998,
        19.049999999999997,
        46.99,
        74.422,
        77.46999999999998,
        51.308,
        49.022,
        41.148,
        46.736,
        33.274,
        35.306,
        21.336,
    ]

    if precip == correct_month_precip:
        return "List of month precip values successfully assigned and has correct converted values!"
    else:
        error_msg = """There is a variable named 'precip', but it is assigned
these values:\n{}
Please ensure that the values are the values from the table above,
but converted to be mm instead of inches"""
        return error_msg.format(precip)


def exercise_test_plot(ax):
    """Testing the plot made by the student."""
    plot_test = mpc.PlotTester(ax)

    return_message = ""

    try:
        plot_test.assert_plot_type(
            "bar",
            """Plot is not a bar type, make sure that the original code you
copied wasn't modified to change the plot type!""",
        )
        return_message += "Plot is a bar type."
    except AssertionError as error:
        return_message += str(error)

    try:
        needed_title_words = [["Boulder"], ["average", "mean"], ["month"], ["precip"]]
        plot_test.assert_title_contains(
            strings_expected=needed_title_words,
            message_default="Please make sure that the title contains all needed keywords specified in the instructions",
        )
        return_message += "\nPlot has all of the needed keywords in the title."
    except AssertionError as error:
        return_message += "\n" + str(error)

    try:
        needed_xaxis_words = ["month"]
        plot_test.assert_axis_label_contains(
            axis="x",
            strings_expected=needed_xaxis_words,
            message_default="Please make sure that the x axis contains all needed keywords specified in the instructions",
        )
        return_message += "\nPlot has all of the needed keywords in the x axis."
    except AssertionError as error:
        return_message += "\n" + str(error)

    try:
        needed_yaxis_words = [["precip"], ["mm", "millimeters"]]
        plot_test.assert_axis_label_contains(
            axis="y",
            strings_expected=needed_yaxis_words,
            message_default="Please make sure that the y axis contains all needed keywords specified in the instructions",
        )
        return_message += "\nPlot has all of the needed keywords in the y axis."
    except AssertionError as error:
        return_message += "\n" + str(error)

    return return_message
