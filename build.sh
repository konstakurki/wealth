#!/usr/bin/env sh
python3 ebook/ebook.py>temporary43889.html
pandoc -o wealth.epub temporary43889.html --toc --toc-depth=2 --epub-stylesheet='ebook/epub.css' --epub-metadata='ebook/epub.xml'
    rm temporary43889.html
ebook-convert wealth.epub wealth.mobi
