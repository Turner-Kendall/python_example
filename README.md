## Python, a slight return

Python is what inspired me to get back into coding but I have not done it in a while. Python is kind of beautiful; almost elegant compared to JavaScript.

As I have had occasion to (re)use it more and more, I have found that I have had to relearn a few things. This is where I am collecting some of the files I generate as I dip my toes back into the pythonic waters.  As it were.

#### [Normalize a Pandas DataFrame Column](https://github.com/TripKendall/python_examples/tree/main/normalizePandasCol)
I will document my data cleaning efforts in a separate file but I wanted to share this little bit of code that I wrote to normalize a column in a Pandas DataFrame.  There are many ways to accomplish anything in Python but this is what I came up with.  

I also wanted to share just how simple Python can be if one lets it...
read more about it [here](https://tripkendall.com/normalize-a-pandas-dataframe-column/)


#### [Sentiment Analysis](https://github.com/TripKendall/python_examples/tree/main/sentimentAnalyzer)
Back before Elon Musk moved everything behind the login and increased the price of the developer program I scraped a bunch of tweets from Twitter.  I wanted to do some sentiment analysis on tweets about Trump. The script and data here show how simple that can be with Python.
This example uses the VADER sentiment analysis.

**The last run finished with:**
```
- neg:    25338
- pos:    22057
```
#### [Multi-File DataFrame](https://github.com/TripKendall/python_examples/tree/main/multiFileDataFrame)
Have a bunch of json files that you want to combine into a single DataFrame?  This is how I did it, it's literally only a dozen lines of Python.  I've included a subset of the data files and the script I used to combine them.  I also included a Jupyter Notebook that shows how to do it in a notebook.

#### [Add Keyword](https://github.com/TripKendall/python_examples/tree/main/addKeyword)
I had a bunch of json files that I needed to tag with the keyword that was used to generate them which I got from the file name. 

#### [Compare JSON Files](https://github.com/TripKendall/python_examples/tree/main/compareJsonFiles)
I have many directories of json files that I need to insure contain unique information.
Processing in the cloud can get expensive. This script compares two json files and deletes the duplicates.

Be careful with this one, it deletes files and can take a long time to run on directories with lots of files.  I often run it with nice 20 to keep it from bogging down my system.

#### [Seaborn Chart](https://github.com/TripKendall/python_examples/tree/main/seabornChart)
SeaBorn is a great library for creating charts.   This is a simple example of how I like to create a chart with SeaBorn - this uses a subset of the data that I have been tracking for over six years now.