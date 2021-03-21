# Parse_Jest_To_CSV

Script to convert a Javascript Jest Test file to a csv compatible with Target Process.

This script is hacked together and prbably has many bugs, however, it works for my current purposes. I will probably continue to update it as new needs come along.

## Usage:

1. Run `python parseJestToCSV.py`
2. Input the path to your test file
3. Input the name of the method from which you want to extract the tests.
4. Input the name of the Output file (It would be easier if you attach .csv at the end of the output file name)

Output: a csv file containing the following info in this particular format:

Test Name | Inputs | Expected Value 
--- | --- | ---
Test 1 | Whatever your input is | Whatever your expected value is 

## Contibutions:

Please feel free to do whatever you want with this project.

If you want a new feature feel free to develop it yourself and do a pull request.

If you do not want to develop it yourself, then do include a feature request in the issues, however, I am not very likely to implement it.


