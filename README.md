# WebScraper
Webscraper developed on contract for Yelp to gather supply data from HomeAdvisor. 

Yelp wanted data regarding their competitors in the professional services industry ("Pros"), and unfortunately one of their largest competitors (HomeAdvisor) had very little publicly available supply data. 

Thankfully, HomeAdvisor does have an exhaustive directory search that lists all Pros in a zipcode for a particular service. It also turns out that the URLs associated with the response of each zipcode-service strictly follow a few patterns, depending on the service. So, my thought - gather all the zipcodes and services, map them out to URLs (3 million+), scrape each response, then load the results in an Excel file! Simple enough, right? 

After several weeks of frustrating bugs, I made a working version that would take roughly 6 months to execute on my computer. Definitely too slow. On a strict deadline, I instead chose to rent out a powerful AWS server, calculate the optimal amount of threads and workload, and voila! I had results within ~30 hours, and Yelp was very happy. 


Uses Python with bs4, pandas, multiprocessing, and pickle.  If you want to understand the design of this program, check out the documentation here:

https://accurate-country-6ae.notion.site/Yelp-WebScraper-Ecosystem-b6726ab8d1974ab4b8acc5fc408bca7f

