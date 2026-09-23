import time
print("Running Backend")

time.sleep(4)

with open("backend_report.txt","w") as f:
    f.write("Application Report\n")
    f.write("Backend run\n")

print("Backend report Generated")
