# AmiiboFlipperConverter

Converts Amiibo .bins to a flipper compatible format

Run `amiiboconvert.py -i [filename].bin` to convert a single file.

To convert multiple files in a directory, run `amiiboconvert.py -i [input-folder] -o [output-folder]`.
If you want to keep the folder structure, you would need to pass an extra `-t` argument, eg. `amiiboconvert.py -i [input-folder] -o [output-folder] -t`

To display help, run `amiiboconvert.py -h`

The original code was created in the Flipper Discord by Friendartiste

The code was modified to run itteratively by Lamp

I, VapidAnt, have modified the code to work in a variety of situations with a recursive function and have uploaded to github
I believe this will make it easy to modify the code in the future and track changes over time.

The code was modfied by Lanjelin to be able to handle .bin-files of varying sizes.
Option to keep folder structure in the output folder added as well. Updated README/docs.

If you have problems, please make an issue or ping me in the flipper discord.

Feel free to itterate off this and make pull requests.

Happy Flipping!
