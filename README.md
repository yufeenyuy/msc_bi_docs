#### What you need to know for the b2c documentation

The docs are built with the help of **pandoc, miktex and markdown**.

#####
* To install miktex follow the installation guide on *https://miktex.org/download*.
* To install pandoc follow the installation guide on *https://pandoc.org/installing.html*.

You can learn markdown syntax on *https://www.markdownguide.org/*

##### Create pdf from Markdown using pandoc on terminal

In your *command line(dmd)*, navigate to the *.md* file(s) that you want to generate a *.pdf* file from.
* To create one .pdf file from a markdown document do: **pandoc file.md -o file.pdf**
* To create one pdf file from several markdowns do: **pandoc file1.md file2.md file3.md etc.md -o files.pdf**.
* To create one .pdf file from several .md files and adjust margins do:**pandoc fii1.md fii2.md fii3.md fii4.md complaint.md fii5.md -o fiis.pdf --variable geometry:margin=0.4in**. In this example the margin is set to 4 inches.