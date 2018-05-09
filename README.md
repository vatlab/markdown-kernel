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

A markdown kernel for Jupyter sounds like a stupid idea because Jupyter has
native Markdown cells. The problem is that Jupyter markdown cells are
rendered at the frontend and do not interact with Jupyter kernels.
It is therefore difficult to pass variables from kernels to markdown cells
to create dynamic output, as what RStudio/RMarkdown has been doing for a while
(See [ipython/ipython#2592](https://github.com/ipython/ipython/issues/2592), [jupyter/help#41](https://github.com/jupyter/help/issues/41),and [jupyter/notebook#3463](https://github.com/jupyter/notebook/issues/3463) for related discussions).

This markdown kernel is a simple Jupyter kernel that parses and displays
 cell content as markdown. Cells with markdown texts such as

```
* This is *important*
* This is not. 
```

would produce output

* This is *important*
* This is not. 

But wait, this is *still stupid* because you can do the same thing in
Jupyter, only easier. What is the point of a markdown kernel by itself?

The answer is that you can use this a markdown kernel with [SoS
Notebook](http://vatlab.github.com/sos-docs). In SoS Notebook, you can
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
