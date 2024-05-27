
import statistics
percentages_wizard = [66.67, 83.33, 160.0, 0.0, 0.0, 25.0, 91.67, 100.0, 0.0, 0.0, 64.29]
percentages_wizard_wout_util = [66.67, 83.33, 160.0, 0.0, 0.0, 25.0, 91.67, 100.0, 0.0, 64.29]

percentages_GPT_all_classes = [83.33, 100.0, 0.0, 66.67, 0.0, 90.0, 0.0, 60.0, 100.0, 160.0, 0.0, 91.67, 25.0, 100.0, 100.0, 100.0, 0.0, 90.0, 75.0, 0.0, 0.0]
percentages_GPT_solution_code =[83.33, 100.0, 0.0, 66.67, 0.0, 100.0, 0.0, 65.0, 75.0, 160.0, 0.0, 83.33, 25.0, 100.0, 100.0, 80.0, 0.0, 100.0, 75.0, 0.0, 0.0]

percentages_wizard_solution_code =[66.67, 83.33, 160.0, 0.0, 0.0, 83.33, 25.0, 80.0, 0.0, 0.0, 57.14]
print(len(percentages_wizard))
#print(len(percentages_wizard_wout_util))
print(len(percentages_GPT_all_classes))
#print(len(percentages_GPT_wout_util))
print(len(percentages_GPT_solution_code))

#print(statistics.mean(percentages_wizard))
#print(statistics.mean(percentages_wizard_wout_util))
print(statistics.mean(percentages_GPT_all_classes))
#print(statistics.mean(percentages_GPT_wout_util))
print(statistics.mean(percentages_GPT_solution_code))
#print(statistics.mean(percentages_wizard_solution_code))