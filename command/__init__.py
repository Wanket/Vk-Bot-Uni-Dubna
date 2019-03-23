from command.DoMake import Make
from command.Homework import Homework
from command.Remind import Remind
from command.Command import commands
from command.Echo import Echo
from command.Help import Help
from command.Remember import Remember
from command.Schedule import Schedule

# EU
commands["/echo"] = Echo()
commands["/help"] = Help()
commands["/remember"] = Remember()
commands["/remind"] = Remind()
commands["/schedule"] = Schedule()
commands["/homework"] = Homework()

# RU
commands["/сделай"] = Make()
