# bloom-filter
Simple bloom filter, part of a project in the course of ICOM4025 (Análisis y Diseño de Algorítmos)

## Instructions

- The Goal of project one is to create a Bloom Filter. based on multiple hashes.
- The Bloom Filter will be created dynamically based on dummy inputs (emails) from a file that must be evaluated at run time.
- Bloom Filter must have a false positive probability of 0.0000001
- You can understand the equations involved at https://hur.st/bloomfilter/ 
- Your program must take 2 files as inputs.

      Example: python <your_program> db_input.csv db_check.csv
      The input file names must not be hardcoded, it must take whatever input files the professor passes as input on whatever location.  It must not assume the file is in the local directory.

- The input comma-separated files will contain 1 column: Email.   Based on the email key, your program will build the Bloom Filter based on file 1 inputs.  Then it will need to check file 2 entries against the bloom filter and provide its assessment.
- Your program must create a results file (must be called results.csv) that will contain the following:

```
    Example Output file

Email,Result
weseGLCIEPTUusDlU@aol.com,Probably in the DB
uEUSgDKJN@hotmail.com,Not  in the DB
PLekUVqtWnRVWShep,Not  in the DB
BXgWIGaZRv@aol.com,Probably in the DB
```

- The application can be developed in the Language of your choosing between Python (preferred) or Java 
- The Professor will run your code with his own parameters and will validate your implementation.
- The Rubric in this section contains the specific values of the specific aspects of the project.
- The application will be handled by e-mail to the professor with the following subject: "Project 2: Bloom Filter Code"

## Rubric Task

Parameters | %
----------- | -----------
The program must take 2 csv files as command-line inputs. The first CSV will be used to create the Bloom Filter, the second will be used to validate against the Bloom Filter. | 10
Create Bloom Filter based on parameters.  Bloom Filter must be an object since in the future the code must be able to generate multiple bloom filters with different parameters. | 10
On-time delivery. | 15
Followed Instructions. | 10
Code Documentation. | 5
Code must output a "Results.csv" file that will contain all e-mails on the second CSV with a new field "Result" that will contain the result of the Bloom Filter for that e-mail.  The Result must be one of 2 possible values: "Probably in the DB" or "Not in the DB". | 20
Algorithm Accuracy (This will be determined and calculated by the professor)

## References used

- [Explanation of a Bloom Filter by my professor](https://www.youtube.com/watch?v=PJaWZ7Seg7c)

- [Hashing Lecture Playlist by by professor](https://www.youtube.com/playlist?list=PLpfW_LYjNenGhPzT5vJnYEg0JpOVuMGZF)

- [Wikipedia on bloom filter](https://en.wikipedia.org/wiki/Bloom_filter)

- [Bloom filter calculator](https://programming.guide/bloom-filter-calculator.html)

- [Another calculator](https://hur.st/bloomfilter/?n=4000&p=1.0E-7&m=&k=)

- [Geeks for geeks explanation of a hash function](https://www.geeksforgeeks.org/hash-functions-and-list-types-of-hash-functions)

- [Dumb question of mine on how to read csv data for numpy](https://stackoverflow.com/questions/3518778/how-do-i-read-csv-data-into-a-record-array-in-numpy)

