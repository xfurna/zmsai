from utils import countFiles

path = "./custom"
numberTopics = countFiles(DIR=path)

helpTask = (
    "Provide task to perform [default : 'run'] [values : 'run', 'delete', display]"
)

helpTopics = (
    "Provide directory of text files. [with : 'run'] [default : "
    + str(numberTopics)
    + "]"
)
helpPath = "Provide directory of text files. [with : 'run'] [default : '" + path + "']"
