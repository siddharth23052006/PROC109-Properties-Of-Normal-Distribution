from os import stat
import statistics
import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("StudentsPerformance.csv")
writingScores_list = df["writing score"].to_list()

writingScores_mean = statistics.mean(writingScores_list)
writingScores_median = statistics.median(writingScores_list)
writingScores_mode = statistics.mode(writingScores_list)
writingScores_stdev = statistics.stdev(writingScores_list)

print("The mean of this data is {}".format(writingScores_mean))
print("The median of this data is {}".format(writingScores_median))
print("The mode of this data is {}".format(writingScores_mode))

score_first_std_dev_start, score_first_std_dev_end = writingScores_mean-writingScores_stdev, writingScores_mean+writingScores_stdev
score_second_std_dev_start, score_second_std_dev_end = writingScores_mean-(2*writingScores_stdev), writingScores_mean+(2*writingScores_stdev)
score_third_std_dev_start, score_third_std_dev_end = writingScores_mean-(3*writingScores_stdev), writingScores_mean+(3*writingScores_stdev)

score_list_of_data_within_1_stdev = [result for result in writingScores_list if result>score_first_std_dev_start and result<score_first_std_dev_end]
score_list_of_data_within_2_stdev = [result for result in writingScores_list if result>score_second_std_dev_start and result<score_second_std_dev_end]
score_list_of_data_within_3_stdev = [result for result in writingScores_list if result>score_third_std_dev_start and result<score_third_std_dev_end]

print("{}% of data of 'Math Scores' lies within 1 standard deviation".format(len(score_list_of_data_within_1_stdev)*100.00/len(writingScores_list)))
print("{}% of data of 'Math Scores' lies within 2 standard deviations".format(len(score_list_of_data_within_2_stdev)*100.00/len(writingScores_list)))
print("{}% of data of 'Math Scores' lies within 3 standard deviations".format(len(score_list_of_data_within_3_stdev)*100.00/len(writingScores_list)))

fig = ff.create_distplot([writingScores_list], ["Writing Results"],show_hist=False).show()