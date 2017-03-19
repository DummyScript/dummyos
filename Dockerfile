# Copyright (C) 2017 Alpha Griffin
# @%@~LICENSE~@%@

# echo "Starting The Docker Build Process"
FROM gentoo/stage3-amd64:latest

# echo "Installing Programs"
# install your apps
# USE RUN FOR COMMITTED CHANGES
# and setup instructions

# Starting Portage Package Manager
RUN emerge --sync 
# thats the hard part...

# Optional -- open ssh server
# RUN /etc/init.d/sshd stop
RUN /etc/init.d/sshd start

# fortune and cowsay for comedy...
RUN emerge games-misc/cowsay
RUN emerge games-misc/fortune-mod

# install git for moving public files around
RUN emerge dev-vcs/git

# Starting Git Startup and Basic Setup Still
RUN mkdir /repos
RUN cd /repos
RUN git clone http://git.alphagriffin.com/ruckusist/bash_utilities 


# this a Hack to keep a non serving docker open for use
CMD tail -f /dev/null

# end our program
# CMD fortune -a | cowsay
