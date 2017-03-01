# Visualize Presidential Election Polls, 2012-2016

## Summary
Uses CNN's Presidential Exit Polls and viusalizes them using a slopegraph made in D3.

The easiest way to run:

`python -m SimpleHTTPServer`
`open index.html`

### Data Gathering
Each state's exit poll is found online at a URL that looks like this: `http://data.cnn.com/ELECTION/[year]/[state]/xpoll/Pfull.json`. The `download.py` script downloads these JSON files stores them in data folders for 2012 and 2016. Note that not all states have exit poll data, e.g. Wyoming in 2016.

`extract_to_csv.py` takes in these JSON files as input and creates one CSV for all the exit polls.

`join` is a notebook I used to to play around with the CSV. It filters for questions that are present in both 2012 and 2016, and excludes categories that are somewhat duplicative. For example, there are two separate age questions in the exit polls that simply break down the respondents into different buckets.

## Design
The inspiration for this project comes from reading [The Middle Class is Waking Up](https://avichal.wordpress.com/2016/11/12/the-middle-class-is-waking-up/). It uses CNN's table visualizations to compare exit poll performance across years. I found this difficult to read and thought that Tufte's slopegraph may make it easier to see differences between how votes were cast in 2012 vs. 2016 in Ohio.

index_old.html shows an early version of this. After collecting feedback, I did the following:

* Fixed overlapping labels, by using [Borgar's slopegraph](https://bl.ocks.org/borgar/67a2173ef40f08129201)
* Added labels to indicate percentage
* Made the labels larger
* Labeled the year axes
* Added a way to choose states for self-exploration

## Feedback
Here are some quotes from gathering user feedback. Each quote is from a different person:

1. "Wow, this really does show how badly Clinton did. Why did this happen?"
2. "Visualization is helpful, but the text is hard to read."
3. "It would be nice to be able to select the labels in some way"
4. "How do I see this for California?"

## Resources
I looked at a few different slopegraph implementations:

* [Borgar](https://bl.ocks.org/borgar/67a2173ef40f08129201)
* [Zach Bjornson](http://bl.ocks.org/zbjornson/2573074)

## Further Directions
* Choose between Republican/Democrat exit polls
* Choose which exit polls should be visible on the graph
* Make this work better for smaller graph heights. Borgar's d3 slopegraph implementation doesn't try to maintain consistency between the two axes. This is okay if your graph is pretty tall, but fails in obvious ways if the graph is smaller (e.g. 45 to 43 may look like an upward sloping line).

