from utils import countFiles

path = "./custom"
numberTopics, docs = countFiles(DIR=path)
nWords = 5
defaultDistro = "all"
helpTask = "Provide task to perform [default : 'run'] [values : 'run', 'delete', 'display', 'man']"

helpTopics = (
    "How many topics do you expect? [with : 'run'] [default : "
    + str(numberTopics)
    + "]"
)
helpnWords = (
    "How many words per topic/doc do you want to display? [with : 'display'] [default : "
    + str(nWords)
    + "]"
)
helpDistro = (
    "What distributions do you want to display? [with : 'display'] [default : "
    + defaultDistro
    + "] [values : 'dt', 'tw', 'dw', 'voc']"
)
helpPath = "Provide directory of text files. [with : 'run'] [default : '" + path + "']"

run = "[Running the model] it may take a while. Hang tight!"
choice = "[`meta.zsm` is empty. Should I 'run' first?] y/n\n"
delete = "[Deleting `meta.zms`]"
