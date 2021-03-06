#!/usr/bin/python

# original source example: https://developers.google.com/youtube/v3/docs/search/list
# assumes use of Python 3

# This sample executes a search request for the specified search term.
# Sample usage:
#   python search.py --q=surfing --max-results=10
# NOTE: To use the sample, you must provide a developer key obtained
#       in the Google APIs Console. Search for "REPLACE_ME" in this code
#       to find the correct place to provide that key..

import argparse

# library googleapiclient installed with: pip install --upgrade google-api-python-client
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = ''
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'


def youtube_search(query_term, max_results):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
        developerKey=DEVELOPER_KEY)

    # Call the search.list method to retrieve results matching the specified
    # query term.
    request = youtube.search().list(
        q=query_term,
        part='id,snippet',
        type='video',
        relevanceLanguage='en',
        maxResults=max_results
    )

    video_ids = []

    while request is not None and len(video_ids) < 1000:
        search_response = request.execute()

        # Add each result to the appropriate list, and then display the lists of
        # matching videos, channels, and playlists.
        items = search_response.get('items', [])
        if len(items) == 0:
            break

        for search_result in items:
            video_ids.append(search_result['id']['videoId'])

        request = youtube.search().list_next(request, search_response)

    return video_ids


if __name__ == '__main__':
    url_prefix = 'https://www.youtube.com/watch?v='
    query_terms = ['"NoSQL"', '"relational database"']
    max_results = 50

    ids = []

    try:
        for query_term in query_terms:
            ids = ids + youtube_search(query_term, max_results)
            if 1000 < len(ids):
                break
    except HttpError as e:
        print('An HTTP error %d occurred:\n%s' % (e.resp.status, e.content))
    else:
        with open('query_output.txt', 'w') as f:
            for i in ids:
                f.write(url_prefix+i+"\n")
