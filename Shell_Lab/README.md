## Theory of Operating Systems


- prints a command prompt which is "$ " and waits for the user to enter a command
- create a child process that uses execve to run the command with its arguments.  
- the parent process should wait for the child to terminate before printing another command prompt.
- print "command not found" if the command is not found
- if the command fails (with a non-zero exit value N), your shell should print "Program terminated with exit code N."
- empty commands should do nothing
- the "exit" command should cause your shell to terminate.
