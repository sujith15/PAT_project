# Open MPI

### Description

This project aims to practice building and testing large Open MPI project, and analyzing the project and providing assessment of testing.

### **Setup & Build Instructions:**
* Below are the two commands used to configure the project before building it
````
./configure CC=gcc-11 CXX=g++-11
````
````
./configure CC=gcc-11 CXX=g++-11 --enable-coverage
````
* To build and execute all commands for the target, we used the below command
````
make -j8 all
````
* Below command is used to run test suite. After running this, .gcno & .gcda files will be generated in test folder
````
make check
````
* To generate coverage report in form of CSV file, we used the below command
````commandline
gcovr --gcov-executable gcov-11 --gcov-ignore-parse-errors --csv -o report.csv
````
* To generate coverage report in form of HTML file, we used the below command
````commandline
gcovr --gcov-executable gcov-11 --gcov-ignore-parse-errors --html -o reporthtml.html
````



