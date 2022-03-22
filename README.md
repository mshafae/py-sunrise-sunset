
# Python Virtual Environment Warm Up Exercise

This is a little exercise to walk you through the process of using a Python Virtual Environment.

The included program, `sunrise-sunset.py`, takes two arguments. The first argument is an address, such as `800 N State College Blvd, Fullerton, CA 92831`. The second argument is a date given as the year, month, and day; for example 2022-03-18. The date must be expressed with dashes delimited each field, the year must be four digits, and the month and day must be two digits.

The program will calculate the time the sun will rise and set on the given day from the given address. Let's assume the you wish to calculate the sun rise and set time for March 18, 2022 from the address 800 N State College Blvd, Fullerton, CA 92831, then:
```
(env) $ ./sunrise-sunset.py "800 N State College Blvd, Fullerton, CA 92831" 2022-03-18
The address you provided is 800 N State College Blvd, Fullerton, CA 92831
The date you provided is 2022-03-18
The sun will rise at 2022-03-18 06:57:44.995932-07:00
The sun will set at 2022-03-18 19:01:45.349124-07:00
```
This means that the sun will rise on March 18, 2022 at 6:57 AM and set on March 18, 2022 at 7:01 PM.

# Exercise
Follow the steps and seek assistance from your instructor as necessary.

1. Clone the repository to your computer
1. Attempt to run the program `sunrise-sunset.py`

`./sunrise-sunset.py "800 N State College Blvd, Fullerton, CA 92831" 2022-03-18`
This will generate an error and not work because of the missing Python packages.

1. Create a Python Virtual Environment
    `python3 -m venv env`
1. Activate the Python Virtual Environment
    `source env/bin/activate`
1. Install the required Python packages with `pip`
    `pip install geopy<br/>
    pip install python-dateutil<br/>
    pip install skyfield`
1. Run the program with the correct command line arguments to verify that you have successfully.
    `./sunrise-sunset.py "800 N State College Blvd, Fullerton, CA 92831" 2022-03-18`
    The output will show that the sun will rise at 6:57 AM and set at 7:01 PM.
1. Run `pylint` on `sunrise-sunset.py`
    This will generate errors because it cannot find the packages that are installed in the virtual environment.
1. Install `pylint` into the virtual environment
    `pip install pylint`
1. Deactivate the virtual environment
    `deactivate`
1. Reactivate the virtuali environment. This will reload the environment and `pylint` will be able to see all the additional packages.
    `source env/bin/activate`
1. Run `pylint` on `sunrise-sunset.py`
