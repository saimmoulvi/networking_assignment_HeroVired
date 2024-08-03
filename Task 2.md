## Imports:
- Importing the necessary libraries: 'requests', 'tabulate' and 'time'

*Define a list of subdomains to check*

## Check Status Function:
- 'check_status(url) function sends a GET request to the provided URL and returns 'True' if the status code is 200,
  indicating the subdomain is up. If any exception occurs it returns 'False'.

## Main Function:
The 'main()' function runs an infinite loop that will:
 - Check the status of each subdomain.
 - Collect the result in a list
 - Clear the screen using 'print("\033" , end="")
 - Display the status in a tabular format using 'tabulate'
 - Waits for 60 seconds before repeating the process
