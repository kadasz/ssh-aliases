# ssh-aliases
That's a quicky way to prepare bash alliases with ssh connection based on available Hosts in Foreman. 

## How's it work?
Just specify required parameters like Foreman's url, Foreman's admin password and username for ssh connections and optionally name of output file which will store ssh aliases entry as: 

```bash
$ ./autogen_aliases.py --h
usage: autogen_aliases.py [-h] [-v] [--url URL] [--pwd PWD] [-u USER] [--output OUTPUT]

Simple script to crate bash aliases with ssh connection base on Foreman Hosts

optional arguments:
  -h, --help       show this help message and exit
  -v, --version    Print version
  --url URL        Type domain or IP of Foreman
  --pwd PWD        Enter passwd of Foreman's admin
  -u USER          Type your user for ssh session
  --output OUTPUT  Optionally specify the name of output file

```

The output is created files named **bash_ssh_aliases_autogen** or which was specify by **--output** parameter like:

```bash
$ ./autogen_aliases.py --url foreman.domain.com --pwd mypass1qaz -u myuser
$ cat bash_ssh_aliases_autogen
ssh_myserver1="sshpass -p $PASSWD ssh myuser@10.0.0.10"
ssh_myserver2="sshpass -p $PASSWD ssh myuser@10.0.0.11"
ssh_serverap1="sshpass -p $PASSWD ssh myuser@10.0.0.21"
ssh_serverap2="sshpass -p $PASSWD ssh myuser@10.0.0.22"
ssh_serverdb1="sshpass -p $PASSWD ssh myuser@10.0.0.23"
```
As you see  also need to determine **$PASSWD** env variables for storing password of ssh connection, for that create a file called e.g. pass and put password there:

```bash
$ cat .pass
export PASSWD="mysupersecurepassword"
```

and at last let's configure bash aliases by adding to bashrc entries something like that:

```
if [ -f  ~/.bash_ssh_aliases_autogen ]; then
  . ~/.pass
  . ~/.bash_ssh_aliases_autogen
fi
```

That's all, help yourself! 
