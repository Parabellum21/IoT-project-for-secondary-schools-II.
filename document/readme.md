# About

Template for final theses writing at _DCI FEEI TUKE_. 

Warning! The encoding of all documents is set to _UTF-8_! So don't forget to set up your environment in which you will write your thesis to use this encoding!

The current version is based on the official release, also available on the website of the University Library. However, it has not been updated for some time, so this project is an effort to keep the current version of this project in collaboration with students. However, please note that this version is still under development and due to potential changes, we recommend _changelog_ monitoring.

## Install

We recommend installing the [TeX Live](https://www.tug.org/texlive/) package.

As an editor, we recommend installing [TeX Studio](http://www.texstudio.org/) or [TeX Maker](http://www.xm1math.net/texmaker/).

Fedora users will write: 

```bash
sudo dnf install texlive-collection-latexrecommended \
    texlive-collection-langczechslovak texlive-totalcount \
    texlive-biblatex texlive-biblatex-iso690 texlive-glossaries \
    latexmk texstudio
```

Similarly, Debian and Ubuntu users will write:

```bash
sudo apt-get install texlive-latex-extra texlive-fonts-recommended \
    texlive-lang-czechslovak texlive-bibtex-extra biber latexmk texstudio
```

## Compilation

To create a document, type the following command from the command line:

```bash
latexmk -pdf -bibtex -pvc thesis
```

Running this command will create the resulting document in _PDF_ format, which will be displayed in the document browser afterwards. However, the tool will not quit and will monitor changes, while with each change (saving a _.tex_ file), the resulting document will be re-generated.

Of course, you can open the project in any _LaTeX_ editor or IDE, e.g. _TeX Studio_.


## Update

In case the template is updated, just update the `kithesis.cls` file in your project. However, always look in the `CHANGELOG.md` file to make sure there was an update. 


## Spell Checking

In case your editor does not support spell-checking, you can use the `aspell` tool as follows: 

```bash
aspell -d sk_SK -t -c file.tex
```


## Troubleshooting

### Q1: I found an error in the template. Where can I report it? 

Either by e-mail to miroslav.binas@tuke.sk or directly here on gitlab. Ideally with a _merge request_. 


### Q2: The page numbering of the table of contents is in Roman numerals. Is that all right? 

Yes, it is OK. The work uses two styles of page numbering. Numbering with Roman numerals is in the introductory part of the work (table of contents and all lists). Numbering of the rest of the work, starting from the introduction or motivation, is numbered in Arabic numerals. Numbering of the second part of the work begins on the page with the introduction or motivation.


### Q3: Table of contents is not displayed.

Try compiling the work again. It is typical for _LaTeX_. If you want to have your table of contents updated, it is always necessary to translate it twice. 


### Q4: The bibliography only shows 3 records, even though I have more.

_BibTeX_ is used to generate the bibliography. It only displays those items that you actually quote in the work. Therefore, if you cite only 3 documents in the work, only those will be displayed in the bibliography. 


## Additional Resources

### LaTeX writing support for popular IDEs and editors

* [TeXiFy IDEA for IntelliJ IDEs](https://plugins.jetbrains.com/plugin/9473-texify-idea)
* [LaTeX Workshop for VS Code](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop)
* [VimTeX: A modern Vim and neovim filetype plugin for LaTeX files](https://github.com/lervag/vimtex)

### Books about using LaTeX

* [The Not So Short Introduction to LaTeX 2ε](http://tug.ctan.org/tex-archive/info/lshort/english/lshort.pdf)
* [Nie príliš stručný úvod do systému LaTeX 2ε](http://people.tuke.sk/jan.busa/kega/latex/latex_uvod.pdf) (Slovak translation)
* [LaTeX Wikibook](https://en.wikibooks.org/wiki/LaTeX)
