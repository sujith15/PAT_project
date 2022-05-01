# Open MPI

### Description

This project aims to practice building and testing large Open MPI project, and analyzing the project and providing assessment of testing.

Here are the commands we used to build and get the coverage from the OpenMPI project

./configure CC=gcc-11 CXX=g++-11
./configure CC=gcc-11 CXX=g++-11 --enable-coverage
make -j8 all
make check (-- we can check the gcno and gcda files are generated in the test folder)
gcovr --gcov-executable gcov-11 --gcov-ignore-parse-errors --csv -o report.csv (CSV report is generated)
gcovr --gcov-executable gcov-11 --gcov-ignore-parse-errors --html -o reporthtml.csv (Html report is generated)
 


