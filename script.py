
import os
import nbformat as nbf





def create_notebook(name, text):
    nb = nbf.v4.new_notebook()
    appo_string="# Problem "+ text[0].split()[2]
    for s in text[1:]:
        
        if s.startswith("### Problem") or s.startswith("#### Problem"):
            
            nb["cells"].append(nbf.v4.new_markdown_cell(appo_string))
            nb["cells"].append(nbf.v4.new_code_cell(""))
        
            appo_string=""
            appo_string+="# Problem "+ s.split()[2]
        else:
            appo_string+=s
    
    with open(name, 'w') as f:
        nb["cells"].append(nbf.v4.new_markdown_cell(appo_string))
        nb["cells"].append(nbf.v4.new_code_cell(""))
        nbf.write(nb, f)
        
        
f=open("list.txt","r")
count=10
appo=[]
flag=False
        
        
for line in f.readlines():

    if line.startswith("### Problem") or line.startswith("#### Problem"):
        number=int(line.split()[2])
        flag=True
    appo.append(line)

    if (number)%10==0 and flag==True:
        appo.pop(-1)
        folder=str(count-10).zfill(3)+ "-"+str(count-1).zfill(3)
        os.mkdir(folder)
        create_notebook(folder+"/"+ folder+".ipynb", appo)
        g=open(folder+"/README.md","w+")
        for l in appo:
            g.write(l)
        flag=False
        appo=[line]
        count+=10


folder="360-365"
os.mkdir(folder)
create_notebook(folder+"/"+ folder+".ipynb", appo)
g=open(folder+"/README.md","w+")
for l in appo:
    g.write(l)





os.system("mv 000-009/000-009.ipynb 000-009/001-009.ipynb")
os.system("mv 000-009 001-009")

