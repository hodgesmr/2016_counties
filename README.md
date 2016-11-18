# 2016 Counties

![clinton-map](https://raw.githubusercontent.com/hodgesmr/2016_counties/master/img/clinton_map_small.png)
![trump-map](https://raw.githubusercontent.com/hodgesmr/2016_counties/master/img/trump_map_small.png)

This is an interactive map that shows the county-level vote density for Donald Trump and Hillary Clinton across all counties.

Unlike what we see in many other maps, I wanted to show how each candidate performed across all counties, not just the counties they won.

## Downloading data

I've included a recent fetch of the election result data, but as of this writing, votes are still being counted across the country. You can fetch new data with:

```sh
python download_and_parse.py
```

## Special thanks

- This was my first time playing with [D3](https://d3js.org/). Shoutout to [Chris Canipe's example](http://bl.ocks.org/chriscanipe/071984bcf482971a94900a01fdb988fa) for getting me 95% of the way there!

- This project pulls data from [tonmcg's parsed election results](https://github.com/tonmcg/County_Level_Election_Results_12-16)

- This project pulls county topology json from [john-guerra's map projct](https://github.com/john-guerra/US_Elections_Results)

## A Matt Hodges project

This project is maintained by [@hodgesmr](http://twitter.com/hodgesmr).
