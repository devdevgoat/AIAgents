#%%
from agent import Agent

writer = Agent("writer","You are a documentation writer. A user will present code files, you must respond with an easy to understand README.md file describing the code. Documents will be delimited with double pipes ||")

files = ["agent.py","main.py"]
filesasstring = ""
for f in files:
    currentfile = open(f, 'r')
    filesasstring += f"{currentfile.read()}||"
    currentfile.close()
    
readme = writer.instruct(filesasstring[:-2])

out = open("README.md","w")
out.write(readme)
out.close()
# %%
