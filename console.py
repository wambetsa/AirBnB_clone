import cmd

class HBNBCommand(cmd.Cmd):
    if cmd.PROMPT in ["quit", "EOF"]:
        exit