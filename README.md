# hadoop-Web-Server-Traffic-Analyzer
Find hourly traffic stats of any site using it's Server logs.

Aggregate simplifies obtaining aggregate statistics of data set. These Packages fucntions as reducer while Streaming scripts.

Execute:
hadoop jar /usr/local/hadoop/hadoop-streaming-2.8.4.jar -reducer aggregate -mapper "python AggregateAnalyzer.py" -input /user/hduser/weblog.csv -output /user/hduser/webAnalyzer
