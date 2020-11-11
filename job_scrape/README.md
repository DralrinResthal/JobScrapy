# Job_Scraper  

This program is inteded to scrape Indeed.com for jobs that fit a very particular set of requirements.  
Later improvements will include:  
- ZipRecruiter.com  
- Saving ALL jobs for repository management  
- Machine Learning to help me organize, find and possibly even classify jobs based on scraped data  

## Structure  

Originally I was not sure what I was going to do with this data. I knew I wanted to email myself of jobs I should apply for, however I wasn't sure how to go about processing the data completely.  

Originally, I though I might save data to a database, and maybe use a scheduled script to grab what I want from that database and email it to myself.  

After some thought on the subject, I have decided to build a Flask application to actually process the raw data pulled by Scrapy, clean it, save it to Mongo Atlas, and do the emailing for me. This way, not only can I run this scraper manually if I wanted to, but I can also much easier automate the rest of the project. This also gives me a chance to learn and better understand API development with Flask. If I decide to include ML at any point in this project, I can also much easier integrate that with Flask than a Scrapy spider or meaningless scheduled script.  

All data will be stored in JSON format and saved on Mongo Atlas

