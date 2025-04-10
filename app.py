WEEK_DAYS =["monday", "tuesday", "wednesday", "thursday", "friday", "saturday","sunday"]
input_day_index=5
print(WEEK_DAYS[input_day_index])
residual_days=0
output_index=(input_day_index+residual_days)% len(WEEK_DAYS)

print(output_index,WEEK_DAYS[output_index])


