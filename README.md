# YouTubeWapper

This is an implementation of example of Youtube OpenAPI v3.0. This submits query and receives video ids which results of query, and save urls of video with ids. In order to use this API, you should acquire an access key from Google.


## The repository includes:
### Source code
* youtube_query_template.py - extract video ids
* youtube_dl_template.py - extract video's context information. This uses the result file of youtube_query_template.py

### Compile & Run

```bash
$ python youtube_query_template.py
$ python youtube_dl_template.py
```

### Status

Version 1.0
