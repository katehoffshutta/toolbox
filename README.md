# toolbox

The file `parse_hmdb_functions.py` provides a basic set of functions for parsing XML downloads from the HMDB (https://hmdb.ca/downloads). These functions are inspired by this blog post: https://yufree.cn/en/2018/04/11/play-with-hmdb-datasets/

The file `parse_hmdb.py` shows how you can use these functions to parse an XML file.

Note that the current code DOES NOT extract every field from the xml. It extracts some fields that I was curious about, but you will need to adapt the function `populateMetabDict` in `parse_hmdb_functions.py` to extract the specific fields that you are interested in. 

A basic unit test is provided in `test_parse_hmdb.py` and the file `unit_test.xml` is the input needed for the unit test. I have only tested the fields extracted by the version of `populateMetabDict` shown here. 


