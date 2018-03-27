# Markdown kernel for Jupyter

## Installation

With a working [Jupyter](http://jupyter.org/) installation, run

```
$ pip install markdown-kernel
$ python markdown_kernel.install
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
to create dynamic output.

This markdown kernel is a simple Jupyter kernel that parses and displays
the cell content as markdown. So that you can type in markdown texts

```
* This is *important*
* This is not. 
```

and it would be rendered as

* This is *important*
* This is not. 


But wait, this is *still stupid* because you can do the same thing in
Jupyter, only easier. What is the point of a markdown kernel by itself?

The answer is that you can use this markdown kernel with [SoS
Notebook](http://vatlab.github.com/sos-docs). In SoS Notebook, you can
create variables in SoS (Python) and pass them to cells of Markdown kernel
as

```
%expand
The result of the analysis is {result}
```

or if you have `{ }` in your text, you can specify an alternative sigil

```
%expand ${ }
The result of the analysis is ${result}
```
as shown in
![example](https://user-images.githubusercontent.com/9889312/37932344-e1c13e96-310d-11e8-963c-5fe26c6523d1.png)

Note that SoS recognizes the `%expand` magic and highlights the intepolated texts.
