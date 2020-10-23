from readData import countFiles
path = "./custom"
numberTopics = countFiles(DIR=path)
helpTopics="Provide directory of text files. [default : " + str(base.numberTopics) + "]"
helpPath="Provide directory of text files. [default : '"+ base.path + "']"
helpTask="Provide task to perform [default : 'run'] [values : 'run', 'delete', display]"