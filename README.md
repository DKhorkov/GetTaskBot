# "GetTaskBot"

This is sources of GetTaskBot in Telegram Messanger. This bot
offers suer to take a task to do it on some event or with
friends, for example. On current stage, each person can take 
only one task from tasks list. 

GetTaskBot can be easily customized (message text; buttons 
text in reply markup; tasks, which can be received) via 
corresponding YAML files, placed in 
<i><b>src/yaml_configs</b></i> directory.

### LOCAL RUN:

Before local run you should create a
<b><i>configs.py</i></b> file in
<b><i>src/</i></b> directory and put a variable
into it:<br>

    TOKEN="<your telegram bot token>"

There are two ways to run this application locally: 
1. run docker container
2. run source file main.py.

To run project via docker do next steps:<br>

1. Install docker: https://docs.docker.com/engine/install/
2. In CMD in directory of project run next commands:<br>
   1) <i><b>sudo docker-compose build</b></i><br>
   2) <i><b>sudo docker-compose up</b></i>
3. [OPTIONAL] Now, it will be an opportunity to see logs 
and database, which will be displayed via docker-volumes in
<i><b>docker_files/</b></i> directory.

To run project using source files do next steps:<br>

1. Install REQUIREMENTS (Instruction is presented below in 
corresponding section of this file)
2. In CMD in directory of project run next command:
   <i><b>python src/main.py</b></i><br>

### REQUIREMENTS:

    pip install -r /path/to/requirements.txt