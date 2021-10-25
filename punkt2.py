time_in_sec = int(input("Enter time in sec: "))
hours = time_in_sec // 3600
a = time_in_sec % 3600
minutes = a // 60
sec = a % 60
print(f"{hours}:{minutes}:{sec} ") 