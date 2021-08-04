import requests
import json
import time

PUSHSHIFT_REDDIT_URL = "http://api.pushshift.io/reddit"

# http://api.pushshift.io/reddit/search/submission/


#TODO: rewrite this


def fetchObjects(**kwargs):
    # Default paramaters for API query
    params = {
        "sort_type": "created_utc",
        "sort": "asc",
        "size": 1000,
    }

    # Add additional paramaters based on function arguments
    for key, value in kwargs.items():
        params[key] = value

    # Print API query paramaters
    print(params)

    # Set the type variable based on function input
    # The type can be "comment" or "submission", default is "comment"
    type = "comment"
    if 'type' in kwargs and kwargs['type'].lower() == "submission":
        type = "submission"

    # Perform an API request
    #put this in a while loop and try except
    
    active = True
    while active:
        try:
          r = requests.get(PUSHSHIFT_REDDIT_URL + "/" + type +
                           "/search/", params=params, timeout=60)
          active = False
        except:
          continue
    
    
    
    

    #This is loading JSON data to python object
    # Check the status code, if successful, process the data
    if r.status_code == 200:
        response = json.loads(r.text)
        data = response['data']
        sorted_data_by_id = sorted(data, key=lambda x: int(x['id'], 36))
        return sorted_data_by_id


def extract_reddit_data(**kwargs):
    # It's the start timestamp
    max_created_utc = 1614432640
    max_id = 0

    # Open a file for JSON output
    file = open("submissions.json", "a")

    # While loop for recursive function
    while 1:
        nothing_processed = True
        # Call the recursive function
        objects = fetchObjects(**kwargs, after=max_created_utc)

        # Loop the returned data, ordered by date
        #TODO: The error is empty data being pulled by API. Rewrite this with logic to handle

        #if object not nonetype do this
        # else wait for .5 and try again until answered and call api again

        try:
          for object in objects:
            id = int(object['id'], 36)
            if id > max_id:
                nothing_processed = False
                created_utc = object['created_utc']
                max_id = id
                if created_utc > max_created_utc:
                    max_created_utc = created_utc
                # Output JSON data to the opened file
                print(json.dumps(object, sort_keys=True,
                      ensure_ascii=True), file=file)
        except:
          print("error")  
          continue


        

        # Exit if nothing happened
        if nothing_processed:
            return
        max_created_utc -= 1

        # Sleep a little before the next recursive function call
        time.sleep(.5)





# Start program by calling function with:
# 1) Subreddit specified
# 2) The type of data required (comment or submission)
extract_reddit_data(subreddit="wallstreetbets", type="submission")





#Sometimes API fails to return, so you get nonetype not iterable
#When that happens you need to repeat that request until you get a response
