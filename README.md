## Web scraping detection prototype
A prototype for detection of web scraping by only analyzing logs.

This was a part of my bachelor's thesis that I wrote in collaboration with
[@callmeGoldenboy](https://github.com/callmeGoldenboy).

## The goal
We explored if web scraping could be detected (with server logs only) and to what extent. 
This prototype aided in the exploration of the thesis question.

By analyzing the history of requests done by an IP and its attributes (such as user-agents and timestamps), we score it between 1-4, representing how likely it is that it is a web scraper.

## Code functionality 
- **Analyzer** - Takes in a list of unique IPs (from the batch of logs) and gives a score between 1-4 for each IP.
- **Log reader** - Processes the batch of logs (JSON) by filtering and storing them in DB. It returns a list of unique IPs in the given batch.
- **Request** - Class for representing a request.
- **Detection** - Used for testing the prototype. It calls the log reader to process the batch. Then it calls the analyzer with the list of unique IPs. Finally, it prints the results for each IP.
- **Database handler** - Handles all the communication with the SQLite DB.
- **Client info** - Returns useful info for a given IP if there are any prior requests done by it. It returns info such as request rate, number of user agents etc.


Logs that were used are not included in the repository.