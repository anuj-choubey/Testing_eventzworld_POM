# Run command
# pytest -vs --browser filename --------->All test case run
# pytest -vs --browser filename::test function name ---------->single test case run commaand
# pytest --html=report.html --self-contained-html ------>genrate html report command
# pytest -m others -v --------->Now to run the tests marked as others,
# pytest -k TestClassDemoInstance -q -------->run class
# pytest --durations=10 --durations-min=1.0
# -----------> To get a list of the slowest 10 test durations over 1.0s long: