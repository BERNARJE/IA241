...
#Lab 8 Function
...

#3.1

def count_words(input_str):
    
    return len(input_str.split())
    
# print(count_words('this is a string'))

#3.2

demo_str = 'hello world'

print(count_words(demo_str))

#3.3

def find_min(num_list):
    
    min_item = num_list[0]
    
    for num in num_list:
        if type(num) is not str:
            if min_item >= num:
                min_item = num
            
    return(min_item)
    
# print(find_min([1,2,3,4]))

#3.4

demo_list = [1,2,3,4,5,6]
print(find_min(demo_list))

#3.5

mix_list = [1,2,3,4,'a',5,6]
print(find_min(mix_list))