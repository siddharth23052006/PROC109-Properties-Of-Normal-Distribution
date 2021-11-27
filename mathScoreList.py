from os import stat
import statistics
import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv("StudentsPerformance.csv")
mathScores_list = df["math score"].to_list()

mathScores_mean = statistics.mean(mathScores_list)
mathScores_median = statistics.median(mathScores_list)
mathScores_mode = statistics.mode(mathScores_list)
mathScores_stdev = statistics.stdev(mathScores_list)

print("The mean of this data is {}".format(mathScores_mean))
print("The median of this data is {}".format(mathScores_median))
print("The mode of this data is {}".format(mathScores_mode))

score_first_std_dev_start, score_first_std_dev_end = mathScores_mean-mathScores_stdev, mathScores_mean+mathScores_stdev
score_second_std_dev_start, score_second_std_dev_end = mathScores_mean-(2*mathScores_stdev), mathScores_mean+(2*mathScores_stdev)
score_third_std_dev_start, score_third_std_dev_end = mathScores_mean-(3*mathScores_stdev), mathScores_mean+(3*mathScores_stdev)

score_list_of_data_within_1_stdev = [result for result in mathScores_list if result>score_first_std_dev_start and result<score_first_std_dev_end]
score_list_of_data_within_2_stdev = [result for result in mathScores_list if result>score_second_std_dev_start and result<score_second_std_dev_end]
score_list_of_data_within_3_stdev = [result for result in mathScores_list if result>score_third_std_dev_start and result<score_third_std_dev_end]

print("{}% of data of 'Math Scores' lies within 1 standard deviation".format(len(score_list_of_data_within_1_stdev)*100.00/len(mathScores_list)))
print("{}% of data of 'Math Scores' lies within 2 standard deviations".format(len(score_list_of_data_within_2_stdev)*100.00/len(mathScores_list)))
print("{}% of data of 'Math Scores' lies within 3 standard deviations".format(len(score_list_of_data_within_3_stdev)*100.00/len(mathScores_list)))

fig = ff.create_distplot([mathScores_list], ["Math Results"],show_hist=False).show()