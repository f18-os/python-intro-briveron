#! /usr/bin/env python3

import os, sys, time, re

pid = os.getpid()               # get and remember pid

#os.write(1, ("About to fork (pid=%d)\n" % pid).encode())



leave=""
leave=input("[Brian_Shell]$ ")


def isPipe(userIn):
    for i, Eric in enumerate(userIn):
        if Eric== '|':
            #print("I see the |")
            left,right = userIn.split('|')









while leave!="exit":
    leave=input("[Brian_Shell]$ ")
    print(leave)
    rc = os.fork()

    args = leave

    if rc < 0:
        sys.exit(1)


    for i, args in enumerate(args):
        if args[i]== '|':
            #print("I see the |")
            left,right = args.split('|')
            print(left, "|" ,right)













    os.close(1)                 # redirect child's stdout
    sys.stdout = open("p4-output.txt", "w")
    fd = sys.stdout.fileno() # os.open("p4-output.txt", os.O_CREAT)
    os.set_inheritable(fd, True)



    elif rc == 0:                   # child
        #os.write(1, ("Child: My pid==%d.  Parent's pid=%d\n" %
        #             (os.getpid(), pid)).encode())
        #os.write(2, ("Child: opened fd=%d for writing\n" % fd).encode())

        for dir in re.split(":", os.environ['PATH']): # try each directory in path
            program = "%s/%s" % (dir, leave[0])
            try:
                os.execve(program, args, os.environ) # try to exec program
            except FileNotFoundError:             # ...expected
                pass                              # ...fail quietly

        #os.write(2, ("Child:    Error: Could not exec %s\n" % args[0]).encode())
        sys.exit(1)                 # terminate with error

    #else:                           # parent (forked ok)
        #os.write(1, ("Parent: My pid=%d.  Child's pid=%d\n" %
        #             (pid, rc)).encode())
        #childPidCode = os.wait()
        #os.write(1, ("Parent: Child %d terminated with exit code %d\n" %
        #             childPidCode).encode())
