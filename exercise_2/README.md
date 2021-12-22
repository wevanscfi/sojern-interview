# Prerequisites
- python3
- pip3

# Install 
`pip3 install -r requirements.txt`

# Notes for the interviewer 
I felt that using the packaging lib was a little bit outside of the spirit of the exercise, even though I would not recommend reimplementing the PEP standard in a real use case.
I dropped a second example that does not utilize any outside libs in ./version_compare_custom.py using pythons tuple comparison to meet the requirements, but it is expected to raise an error with version strings that contain invalid / non-digit chars.

# Run
`./version_compare.py <version1> <version2>`

# Run custom version parser
`./version_compare_custom.py <version1> <version2>`

# Run Tests
`./test.py`

