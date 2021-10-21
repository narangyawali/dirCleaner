
#! /usr/bin/bash

chmod +x ./dist/dirclean
sudo cp ./dist/dirclean /bin/

if [ -f ~/.bashrc ]
then
	echo "alias dc='dirclean'
" >> ~/.bashrc
else
	touch ~/.bashrc;	
	echo "alias dc='dirclean'" >> ~/.bashrc
fi