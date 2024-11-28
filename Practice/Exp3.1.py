'''Write a python program to read the numbers until -1 is
encountered. Find the average of positive numbers and negative
numbers entered by the user'''

num_list = []
entered_num = 0
while entered_num != -1 :
    entered_num = int(input("Enter Numbers Other Than -1 : "))
    num_list.append(entered_num)

pos_num = [num for num in num_list if num > 0]
neg_num = [num for num in num_list if num < 0]

avg_pos_num = 0
pos_count = 0

for num in pos_num:
    avg_pos_num += num
    pos_count += 1

avg_pos_num = avg_pos_num/pos_count

avg_neg_num = 0
neg_count = 0

for num in neg_num:
    avg_neg_num += num
    neg_count += 1

avg_neg_num = avg_neg_num/neg_count

print(f"Average Of Positive Number : {avg_pos_num}")
print(f"Average Of Negative Number : {avg_neg_num}")