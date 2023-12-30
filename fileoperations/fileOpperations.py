
def update_server_config(filePath, key, value):

    with open(filePath,"r") as file:
        
        # print(file)
        lines = file.readlines()
        print (lines)
    
    with open(filePath, "w") as file:

        for line in lines:
            if key in line:
                file.write(key + "=" + value + "\n")
            else:
             file.write(line)
    
update_server_config("server.config", "TIMEOUT", "1000" )     