This project explores and compares two fundamental approaches to handling large-scale data processing: MapReduce and Non-MapReduce methods.
Utilizing the Bitcoin Tweets Dataset from Kaggle, the project aims to illustrate the strengths and limitations of each approach.

Link of the dataset: https://www.kaggle.com/datasets/kaushiksuresh147/bitcoin-tweets/data

Two task is compared in this project:
1. Calculate Total Word Count: The first task involves calculating the total word count from the text column of the Bitcoin Tweets dataset. 
2. Find the Top 10 Words: The second task is to identify the top 10 most frequently occurring words in the text column.

This project suggests that the Non-MapReduce approach performs better. It demonstrates faster execution times and requires less code,
making it a more efficient and user-friendly option for processing and analyzing large datasets.

Possible Reasons for Non-Mapreduce outperform MapReduce approach:
1. The dataset size is still relatively small.
2. MapReduce overhead time overshadows its advantages.
3. Non-MapReduce methods leverage better-optimized librarie
