import argparse as arp

# Add a general description (optional)
## parser is now an object of the class ArgumentParser 
parser = arp.ArgumentParser(description='Sample tester')

## Positional Argument. (Positional arguments are mandatory)
parser.add_argument("num_to_square", help="Enter a number you want square for", type=int)

## Optional Argument with a value. ( Use --verbosity 1 )
parser.add_argument("-v", "--verbosity", help="Switch on for more verbosity", type=int, default=0, choices=[0,1,2] )

## Optional argument, without value.
## 'action' parameter will store a value = True for args.greeting if --greetings is specified. Otherwise stores false.
## There are some predefined actions which can be used for arguments for which you do not want to specify a value.
parser.add_argument("-g", "--greetings", help="Specify this to enable some greeting", action='store_true')

## Command to parse all the arguments.
## After this we can access the arguments as args.<argument_name>
args = parser.parse_args()

sq_ans = args.num_to_square**2

if (args.verbosity == 1 ):
    print ( " {} ^ {} " .format(args.num_to_square, sq_ans))
elif (args.verbosity > 1 ):
    print ( " The square of {} = {}".format(args.num_to_square, sq_ans))
else:
    print (args.num_to_square**2)


if (args.greetings):
    print ( " You enabled the greetings message ")


## TO add mutually exclusive arguments ( Only 1 can be specified at once )

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
######### Out of -v and -q only 1 can be specified.
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")

parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")


if __name__ == 'main':
	print ( ' This program is being run by itself ' )
	# Execute_func1
	# Execute_func2
else:
	print ( ' I am being called from somewhere else ' )
			 
