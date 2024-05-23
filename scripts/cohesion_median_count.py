
import statistics
percentages_wizard = [66.67, 83.33, 160.0, 0.0, 0.0, 25.0, 91.67, 100.0, 0.0, 0.0, 64.29]
percentages_wizard_wout_util = [66.67, 83.33, 160.0, 0.0, 0.0, 25.0, 91.67, 100.0, 0.0, 64.29]
percentages_GPT_all_classes = [83.33, 100.0, 0.0, 66.67, 0.0, 0.0, 60.0, 100.0, 160.0, 0.0, 91.67, 25.0, 100.0, 100.0, 100.0, 0.0, 90.0, 75.0, 0.0, 0.0]
percentages_GPT_wout_util = [83.33, 100.0, 66.67, 0.0, 0.0, 60.0, 100.0, 160.0, 0.0, 91.67, 25.0, 100.0, 100.0, 100.0, 0.0, 90.0, 75.0, 0.0]
print(len(percentages_wizard))
print(len(percentages_wizard_wout_util))
print(len(percentages_GPT_all_classes))
print(len(percentages_GPT_wout_util))

print(statistics.median(percentages_wizard))
print(statistics.median(percentages_wizard_wout_util))
print(statistics.median(percentages_GPT_all_classes))
print(statistics.median(percentages_GPT_wout_util))

