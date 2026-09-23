import time
print("Running Frontend")

time.sleep(4)

with open("frontend_report.txt","w") as f:
    f.write("Application Report\n")
    f.write("Backend run\n")
    
    
print("Frontend report Generated")