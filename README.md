# hnjobs
A Python 3 library that can support extracting Hacker News job posts. It is a command-line tool on top of the Python library that supports searching keywords in Hacker News job posts within a time period.

# Avaliable functions 
1. `get_job_posts(year, month)`: return all the job posts (as strings) at a specific month
2. `get_job_posts(start_year, start_month, end_year, end_month)`:return all the job posts (as strings) in this duration
3. `search_in_job_posts(keyword, year, month)`: return all the job posts that contains the keyword at a specific month
4. `search_in_job_posts(keyword, start_year, start_month, end_year, end_month)`: return all the job posts that contains the keyword in this duration
