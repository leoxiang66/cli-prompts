from .utils import truncate

def cli(options:dict):

    prompt = ''
    max_len = max([len(x) for x in options.keys()])
    for i,j in options.items():
        prompt += i.ljust(max_len+5) + truncate(j,max_len+5,30)+'\n'
    usr = input(prompt)

