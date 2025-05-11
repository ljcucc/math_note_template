# Math note template

Purpose of this note template must trace back to my backstory.

## Origin

When I was in high school, I used to write math notes for homework by hand, just like two people talking to each other, carrying on a conversation from the beginning to the end of a math topic.

During high school, I was deeply impacted by the support from my classmates and teachers. I always expect my notes would be helpful to others, and at the same time, I told myself they were also for my future self. However, upon entering university, that supportive environment was gone, and I fell into deep depression.

After 5 years, I finally started developing this latex template system to improve my note-taking efficiency and manage my math notes in a more advanced way.

For this template, My Math Notes can be stored separately in another repository by copying it to this folder and renaming it Pages. If pages.tex is found in your notes repository, the template will automatically switch from the example/demo content to your notes content.

I also implemented a few macros to help me take notes, as shown below.

See [examples.pdf](https://github.com/ljcucc/math_note_template/releases/download/demonstration/examples.pdf) for the result.

## Get Started

[comment]: comment

To get started...

git clone your other pages writing as submodule, and applied your pages in pages.tex. for example

```
git clone https://github.com/ljcucc/my-math-note.git
mv my-math-note pages
```

Compile your note via

```sh
xelatex main.tex # without irasutoya

# with irasutoya
xelatex -synctex=1 -interaction=nonstopmode --shell-escape main.tex; open ./main.pdf
```

> Creation of the table of contents and cross-referencing call-outs -- take more than one compilation round to complete fully. [ref](https://tex.stackexchange.com/questions/301103/empty-table-of-contents)

```sh
latexmk -c # Clear .aux files
```

## Writing your note

Your notes will stored in `pages/`, and defined in `pages/pages.tex`. you should not put any context inside `pages.tex`, instead you can put into something like `main.tex`. usually you dont needed to change codes to this template.

Reference [my math note](https://github.com/ljcucc/my-math-note) as demo.

the file sturcture will look like this:

* `pages/`: your git repository
  * `pages.tex`: fixed, necessary.
  * `my_first_chapter/`: example chapter one (any name you want)
    * `main.tex`: recommended name
    * `some_paeg.tex`: ...
    * ...
  * `another_chapter/`: example chatper tw (any name you want)
    * `main.tex`: recommended name
    * ...

for example `pages/pages.tex`

```latex
\maketitle
\characterPage % making a character introduction page
\tableofcontents % making pages of table of contents

\chapter{This is chapter one} % a chapter is defined
\import{pages/my_first_chapter}{main} % full path from the note template

% ...
```

and your `pages/my_first_chapter/main.tex` could contains the chapter one outlines:

```latex
\documentclass[class=article, crop=false]{standalone}

\usepackage[subpreambles=true]{standalone}

\begin{document}

% where, your chapter's sections were defined in other files:

\include{sec1.tex}
\include{sec2.tex}
\include{sec3.tex}
% ...\include{sec[n].tex}

\end{document}
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

To use irasutoya

```latex
\irasutoya{Your image search keyword in japanese}{image width}
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

## Dialogue usage

```latex
% Reader Dialogue
\readerConfused{text}
\readerEureka{text}
\readerExcitment{text}
\readerQuestioning{text}
\readerGrinning{text}

% Teacher Dialogue
\teacherConfident{text}
\teacherPause{text}
\teacherTalking{text}
\teacherAgree{text}
\teacherAngry{text}
\teacherNervous{text}
\teacherAfraid{text}

\begin{readerConfused}
\end{readerConfused}

\begin{readerEureka}
\end{readerEureka}

\begin{readerExcitment}
\end{readerExcitment}

\begin{readerQuestioning}
\end{readerQuestioning}

\begin{readerGrinning}
\end{readerGrinning}

\begin{teacherConfident}
\end{teacherConfident}

\begin{teacherPause}
\end{teacherPause}

\begin{teacherTalking}
\end{teacherTalking}

\begin{teacherAgree}
\end{teacherAgree}

\begin{teacherAngry}
\end{teacherAngry}

\begin{teacherNervous}
\end{teacherNervous}

\begin{teacherAfraid}
\end{teacherAfraid}
```

Reference `example/` for more dialogue usage.

## Create VN(Visual Novel) with your note - Ren'Py

See [latex_renpy](https://github.com/ljcucc/latex_renpy) for more.

## Copyright and License

see [License](LICENSE) for license.

All image applied to CC BY-NC-ND 4.0.

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><span property="dct:title">Default image</span> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/ljcucc">ljcucc</a> is licensed under <a href="https://creativecommons.org/licenses/by-nc-nd/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY-NC-ND 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nd.svg?ref=chooser-v1" alt=""></a></p>
