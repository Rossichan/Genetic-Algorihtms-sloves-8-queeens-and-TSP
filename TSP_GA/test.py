import operator
fitness=[1.1,2.1,3.1,4.1,5.1,6.1,7.1,8.1,9.1,10.1]
sort_dict = {}
for i in range(10):
    sort_dict[(fitness[i], 1 / fitness[i])] = i

sorted_key = sorted(sort_dict.keys(), key=operator.itemgetter(0), reverse=True)
#print(sorted_key)
sorted_index = [sort_dict[i] for i in sorted_key]
#print(sorted_index)

print(fitness[:2])
