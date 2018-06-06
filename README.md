# Markdown kernel for Jupyter

## Installation

With a working [Jupyter](http://jupyter.org/) installation, run

```
$ pip install markdown-kernel
$ python -m markdown_kernel.install
```

Verify if you have `markdown` kernel installed with command

```
$ jupyter kernelspec list
```

Then start `jupyter notebook` and create a notebook with `markdown` kernel? Not so fast.

## Why a markdown kernel for Jupyter?

This markdown kernel is a simple Jupyter kernel that parses and displays
 cell content as markdown. Cells with markdown texts such as

```
* This is *important*
* This is not. 
```

would produce output

* This is *important*
* This is not. 

But wait, this is *stupid* because you can do the same thing in
Jupyter, only easier. What is the point of a markdown kernel by itself?

The first application of a markdown kernel is to write a notebook entirely in markdown without involving any other kernel. It can be useful  ([jupyter/notebook#2908](https://github.com/jupyter/notebook/issues/2908)) and somewhat more convenient than using a Python 3 (or any other) kernel and switching each new cell to markdown cell, but it is not so appealing in appearance because you see both the input markdown and rendered output in your notebook.

The second, less obvious application, is to "evaluate" markdown cells with string interpolation. A big problem with Jupyter's markdown cells is that they are rendered at the frontend and do not interact with Jupyter kernels. It is therefore difficult to pass variables from kernels to markdown cells to create dynamic output, as what RStudio/RMarkdown has been doing for a while (See [ipython/ipython#2592](https://github.com/ipython/ipython/issues/2592), [jupyter/help#41](https://github.com/jupyter/help/issues/41),and [jupyter/notebook#3463](https://github.com/jupyter/notebook/issues/3463) for related discussions). Although a markdown kernel without a computing kernel cannot accept string interpolation either, you can use a markdown kernel with [SoS
Notebook](http://vatlab.github.com/sos-docs). In a SoS Notebook, you can
create variables in SoS (Python) and pass them to cells of a Markdown kernel
as

```
%expand
The result of the analysis is {result}
```

or if you have multiple `{ }` in your text, you can specify an alternative sigil

```
%expand ${ }
The result of the analysis is ${result}
```
as shown in
![example](https://user-images.githubusercontent.com/9889312/37932344-e1c13e96-310d-11e8-963c-5fe26c6523d1.png)

Note that SoS recognizes the [`%expand` magic](https://vatlab.github.io/sos-docs/doc/documentation/SoS_Magics.html#magic_expand) and highlights the intepolated expressions. SoS essentially treats the cell content as [Python f-strings](https://www.python.org/dev/peps/pep-0498/) (with configurable sigil) so almost arbitrary Python expressions could be used. In addition, instead of passing variables from subkernels to SoS and to a markdown cell, you can use a [`%render` magic](https://vatlab.github.io/sos-docs/doc/documentation/SoS_Magics.html#magic_render) to render output from any subkernels as markdown. The input of markdown cells will be hidden in exported HTML reports if you are using one of the SoS templates, as shown in [this example](https://vatlab.github.io/sos-docs/doc/examples/Preview_and_Report_Generation.html).
