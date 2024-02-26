import random
import pandas as pd

questions = list(range(1, 11))

num_questions = int(input("How many questions would you want to give the students? "))
column_labels = ['CW'+(str(n+1)) for n in range(num_questions)]


num_students = int(input("Number of Students?"))


blank_row = [0 for i in range(num_questions)]

output_df = pd.DataFrame([blank_row], columns=column_labels)
for _ in range(num_students):
   nums = random.sample(questions, num_questions)
   df = pd.DataFrame([nums], columns=column_labels)
   output_df = pd.concat([output_df, df], ignore_index=True)

# this skips the first row so our index starts at 1.
output_df[1:].to_excel('out1.xlsx', sheet_name='CWSA')