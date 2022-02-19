# Discord Nitro Generator
Generates Discord Nitro codes without any interference for the end-user. Free Nitro!

# How it Works
The algorithm for generating the code links comes from /ZexZee/Python-steamkey-generator. I cloned the code and redesigned the code in a way that it can work in server infastructures without stopping at all. All codes are generated and checked at the same time without the need to stop the program to do each one seperately. Without stopping the program it checks the code and discards of invalid ones (who wants invalid codes clogging up your storage?) and saves the good ones to a file named `goodies.txt`. Check this file from time to time for new codes!

# Issues 💣
Heroku uses a block based storage solution for all of their web apps and there is no way to change it, but there are plenty of workarounds. This means that all the files are reset at the end of the day to keep storage usage to a minimum, clearing the `goodies.txt` file if there were any valid codes in it.

We can workaround this by creating an AWS S3 bucket with bucketeer for *$5 a month* through heroku or host one for free with *Amazon AWS S3*. If you chose this repo becuase it would *save you money* then the free version is probably right for you when we implement it.
