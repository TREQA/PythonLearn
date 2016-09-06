#operatiuni cu dictionare
nums = {
    1: "one",
    2: "two",
    3: "three"
}

result = []
print (1 in nums)
print ("three" in nums)
print (4 in nums)
for index in nums:
    if int(index)%2!=0:
        result.append(nums[index])
print ("numere prime: " + str(result))
# test 2
# test
#test 3
# test 7
