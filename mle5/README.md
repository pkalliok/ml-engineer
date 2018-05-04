# Machine Learning Engineer Programme - Excercise 5

Task 1 is about handling different files with code, task2 handling data in database

## Task 1 - Merge data in memory

1. Clone current repository for your computer
2. Install postgresql database to you computer, if not exist
  * MAC:
    * `brew update`
    * `brew install postgresql`
    * `brew services start postgresql`
  * Windows:
    * Download postgresql from [https://www.postgresql.org/download/windows/](https://www.postgresql.org/download/windows/) and install with installer
3. Create database from 'adult_dump.sql'
4. Read all data files (`adult.json`, `adult.parquet`,`adult.xml`,`adult1.json`,`adult2.json`) and the database dump into your application (in-memory).
   * Idea is to just read all data into memory, in order to provide it to the algorithm. This might be the first integration step in real-life too.
5. Merge and cleaning your data (remove duplicate rows etc) so that data looks like same as 3. exercice's  adult data
6. Validate that your datata is correct for algorithm and run your machine learning model (the same model you built in the third exercise) with this dataset


## Task 2 - Merge data into database (optional)

1. Try to move all different data files to database
2. Merge and clean data in database
3. Read data from database to application and run your model with this data
