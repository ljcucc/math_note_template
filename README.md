# Math note template

git clone your other pages writing as submodule, and applied your pages in pages.tex. for example

```
git clone https://github.com/ljcucc/my-math-note.git
mv my-math-note pages
```

Compile your note via

```
xelatex main.tex
```

## Using irasutoya(いらすとや) in latex

Required `nodejs` and `npm` to be installed.

```latex
\input{irasutoya} % insert this line into main.tex
```

```sh
mkdir irasutoya # make a image folder for latex to download
xelatex -synctex=1 -interaction=nonstopmode --shell-escape main.tex; open ./main.pdf
```

## Setup characters

To showing your characters between dialogue, you'll need to add image files into `./assets` folder. dialogs.txt is depended on these images.

list of image needed is down below, you can also generate dialogue with AI by including these descriptions.

for reader character:

* `a-confused.png`: reader is confused about some concept.
* `a-eureka.png`: eureka moment.
* `a-excitement.png`: more exciting eureka moment.
* `a-questioning.png`: reader is questioning about the current statement
* `a-settings`: characters settings
* `a-grinning`: smiling with mouth open wide.

for teacher character

* `b-confident.png`: teacher is confident about zirs statement.
* `b-pause.png`: teacher is pausing for a moment.
* `b-talking.png`: teacher is talking.
* `b-settings`: characters settings

## Copyright and License

see [License](LICENSE) for license.

All image applied to CC BY-NC-ND 4.0.

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><span property="dct:title">Default image</span> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/ljcucc">ljcucc</a> is licensed under <a href="https://creativecommons.org/licenses/by-nc-nd/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY-NC-ND 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nd.svg?ref=chooser-v1" alt=""></a></p>
