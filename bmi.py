def calculate_bmi(height,weight):
    bmi = weight/(height*height)
    return bmi

calculated_value = calculate_bmi(weight=57, height=1.23)
print(calculated_value)

if calculated_value < 18.5:
    print("Under Weight")
elif calculated_value > 18.5 and calculated_value <25.0:
    print("Normal Weight")
else:
    print("Over Weight")