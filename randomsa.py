import random
import xlsxwriter

workbook = xlsxwriter.Workbook('CWSA6.xlsx')
sheet = workbook.add_worksheet()

# Generate some sample data.
gt = []
for num in range (20):
    questions = [1,2,3,4,5,6,7,8,9,10]
    nums = (random.sample(questions, 3,))
    #print(nums)

    gt.append(nums)
print(gt)

#Add some formatted headers.
bold = workbook.add_format({'bold': 1,'font_color':'#FF0000'})

sheet.write('A1','Student Name',bold)
sheet.write('B1','CW1',bold)
sheet.write('C1','CW2',bold)
sheet.write('D1','CW3',bold)

for row in range(len(gt)):
   for col in range(len(gt[row])):
      sheet.write(row +1, col +1, gt[row][col])
      

workbook.close()