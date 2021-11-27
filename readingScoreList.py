from os import stat
import statistics
import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("StudentsPerformance.csv")
readingScores_list = df["reading score"].to_list()

readingScores_mean = statistics.mean(readingScores_list)
readingScores_median = statistics.median(readingScores_list)
readingScores_mode = statistics.mode(readingScores_list)
readingScores_stdev = statistics.stdev(readingScores_list)

print("The mean of this data is {}".format(readingScores_mean))
print("The median of this data is {}".format(readingScores_median))
print("The mode of this data is {}".format(readingScores_mode))

score_first_std_dev_start, score_first_std_dev_end = readingScores_mean-readingScores_stdev, readingScores_mean+readingScores_stdev
score_second_std_dev_start, score_second_std_dev_end = readingScores_mean-(2*readingScores_stdev), readingScores_mean+(2*readingScores_stdev)
score_third_std_dev_start, score_third_std_dev_end = readingScores_mean-(3*readingScores_stdev), readingScores_mean+(3*readingScores_stdev)

score_list_of_data_within_1_stdev = [result for result in readingScores_list if result>score_first_std_dev_start and result<score_first_std_dev_end]
score_list_of_data_within_2_stdev = [result for result in readingScores_list if result>score_second_std_dev_start and result<score_second_std_dev_end]
score_list_of_data_within_3_stdev = [result for result in readingScores_list if result>score_third_std_dev_start and result<score_third_std_dev_end]

print("{}% of data of 'Math Scores' lies within 1 standard deviation".format(len(score_list_of_data_within_1_stdev)*100.00/len(readingScores_list)))
print("{}% of data of 'Math Scores' lies within 2 standard deviations".format(len(score_list_of_data_within_2_stdev)*100.00/len(readingScores_list)))
print("{}% of data of 'Math Scores' lies within 3 standard deviations".format(len(score_list_of_data_within_3_stdev)*100.00/len(readingScores_list)))

fig = ff.create_distplot([readingScores_list], ["Reading Results"],show_hist=False).show()