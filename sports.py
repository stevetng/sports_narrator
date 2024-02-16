from exa_py import Exa
api_key = "a6a6e1cb-7273-4f57-9d59-e8633bc0eeb5"
exa = Exa(api_key)
# notes for self: i'm creating an instance of a Exa class here
# you need to import the Exa class from the Python SDK first, use the API key as a password and then create the Exa class 

query = "Articles and discussions about latest political events"
use_autoprompt = True  # Set to True to let Exa optimize the query

# setting up the query to find the recent news articles, and setting the autoprompt parameter to true to then set into the search

options = {
    "num_results": 5,  # Adjust based on how many results you want
    "start_published_date": "2024-01-01",  # Adjust date range as needed
    "end_published_date": "2024-02-14",
    "use_autoprompt": use_autoprompt
}

# dictionaries are similar to JSON files, essentially allowing you to create key value pairs that can be easily changed

search_response = exa.search(query, **options)
print(search_response)
# creating a variable to store the result returned by the search method from the Exa class instance, the ** is used in the function call to unpack the dictionary into arguments for the function, cool way to parse it


document_ids = [result.id for result in search_response.results]

# creating a list of IDs for the documents I want to smmarize, here we're using list comprehension, where you can parse through a list and return a list

highlights_options = {
    "query": "Summarize this content as if it's a thrilling sports match commentary",
    "num_sentences": 5,  # Adjust as needed
    "highlights_per_url": 2  # Number of highlights per URL
}
# creating a highlights_option dictionary to then pass into the contents method
contents_response = exa.get_contents(document_ids, highlights=highlights_options)
# using the contents method to generate highlights of the same documents I've just now found
