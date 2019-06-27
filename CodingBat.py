def make_ends(nums):
  if len(nums) < 2:
    return [nums[0],nums[0]]
  else:
    return [nums[0],nums[-1]]

def middle_way(a, b):
  c = [a[1],b[1]]
  return c

def sum2(nums):
  sum = 0
  length = len(nums)
  if length <1:
    return sum
  elif length < 2:
    return nums[0]
  else:
    return nums[0]+ nums[1]
    
def max_end3(nums):
  if nums[0]> nums[-1]:
    nums = [nums[0]]*(len(nums))
    return nums
  else:
    nums = [nums[-1]]*len(nums)
    return nums

def reverse3(nums):
  nums.reverse()
  return nums

def rotate_left3(nums):
  return  nums[1:] + nums[0:1]
    

def sum3(nums):
  sum = 0
  for i in nums:
    sum += i
  return sum  

def common_end(a, b):
  return a[0] ==b[0] or a[-1] ==b[-1]

def make_pi():
  return [3,1,4]

def same_first_last(nums):
  return len(nums) >= 1 and nums[0] == nums[-1]

def first_last6(nums):
  return nums[0]==6 or nums[-1] == 6

#String-1 begins:
def left2(str):
  return str[2:]+ str[0:2]  

def non_start(a, b):
  return a[1:]+b[1:]

def combo_string(a, b):
  if len(a) < len(b):
    shorter = a
    larger = b
  else:
    shorter = b
    larger = a
  return shorter + larger + shorter  

def without_end(str):
  
  newStr = str[1:-1]
  return newStr

def first_half(str):
  return str[:len(str)/2]  

def first_two(str):
  if len(str)<2:
    return str
  else:
    return str[:2]
  
def extra_end(str):
  return str[-2:]*3

def make_out_word(out, word):
  return out[0:len(out)/2]+word+ out[len(out)/2:len(out)]
def make_tags(tag, word):
  return "<"+tag+">"+word+"</"+tag+">"
def make_abba(a, b):
  return a+b+b+a

def hello_name(name):
  return "Hello "+ name+"!"

#Warmup 2 begins:
def string_match(a, b):
  count = 0
  mini = 0
  len1 = len(a)
  len2 = len(b)
  if len1<len2:
    mini = len1
  else:
    mini = len2  
  if(len1<2 or len2 <2):
    return count
  for i in range(mini-1):
    print(a[i:i+2]+" "+b[i:i+2])
    if a[i:i+2] == b[i:i+2]:
      count += 1
  print(count)      
def array123(nums):
  if(len(nums)<3):
    return False
  for i in range(0,len(nums)-2):
    if nums[i]==1 and (nums[i+1] == 2 and nums[i+2]==3):
      return True
      break
  return False
      
def array_front9(nums):
  list1 = nums[0:4]
  if 9 in list1:
    return True
  else:
    return False
def array_count9(nums):
  count = 0
  for i in nums:
    if i==9:
      count+=1
      
  return count    

def last2(str):
  count = 0
  length = len(str)
  temp = str[length -2:length]
  for i in range(length-2):
    if str[i:i+2] == temp:
        count+= 1    
  return count
def string_splosion(str):
  temp = ""
  length = len(str)
  
  for i in range(length+1):
    temp += str[0:i]
  return temp


def string_bits(str):
  return str[0:len(str):2]
def front_times(str, n):
  if len(str)<1:
    return str
  elif len(str)<3:
    return str*n
  else:
    return str[0:3]*n

def string_times(str, n):
  return str*n
#-------------------------------------------------------------------------#
#WarmUp 1 goes below:
def parrot_trouble(talking, hour):
  if talking == True and (hour < 7 or hour > 20):
    return True
  else:
    return False

def diff21(n):
  if(n<=21):
    return abs(n-21)
  else:
    return abs(n-21)*2

def sum_double(a, b):
  if a!=b:
    return a+b
  else:
    return (a+b)*2
    
def front3(str):
  if len(str)<1:
    return str
  elif len(str)<3:
    return str*3
  else:
    return str[0:3]*3

def front_back(str):
  if len(str)<2:
    return str
  else:
    return str[len(str)-1]+ str[1:len(str)-1]+str[0]
    
def missing_char(str, n):
  return str[0:n]+str[n+1:len(str)]

def not_string(str):
  if str.startswith("not"):
    return str
  else:
    return "not " + str
def pos_neg(a, b, negative):
  if (negative == True and (a < 0 and b < 0)) or (((a<0 and b>0) or (a>0 and b<0)) and negative != True):
    return True
  else:
    return False

def near_hundred(n):
  if abs(n-100)<=10 or abs(n - 200) <=10:
    return True
  else:
    return False
  
def makes10(a, b):
  if (a == 10 or b == 10) or (a+b)==10:
    return True
  else:
    return False

def monkey_trouble(a_smile, b_smile):
  if (a_smile and b_smile == True) or ((a_smile or b_smile) == False):
      return True
  else:
      return False
def sleep_in(weekday, vacation):
  if weekday == False or vacation == True:
    return True
    
  else:
    return False
#Warmup 1 ends here.
string_match('xxcaazz', 'xxbaaz')

