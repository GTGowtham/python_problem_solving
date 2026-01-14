
def nearest_power_2(n):
     lower=1
     upper=1
     while upper<n:
         lower=upper
         upper=upper*2
     lower_dis=n-lower
     upper_dis=upper-n
     return min(lower_dis,upper_dis)

print(nearest_power_2(10))


