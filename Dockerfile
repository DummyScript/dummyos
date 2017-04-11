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
# RUN /etc/init.d/sshd start
WORKDIR /
# fortune and cowsay for comedy...
RUN emerge games-misc/cowsay
RUN emerge games-misc/fortune-mod
RUN emerge dev-lang/python

# install git for moving public files around
RUN emerge dev-vcs/git

# Starting Git Startup and Basic Setup Still
#RUN git clone https://github.com/alphagriffin/tf_utilities
#WORKDIR /tf_utilities
#RUN python3 setup.py install
# Install Git repos
#RUN python3 tf_curses/setup.py install

# this is a chatbot-- for now... !!!
#CMD tf_curses
