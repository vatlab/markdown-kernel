# Markdown kernel for Jupyter

## Installation

With a working [Jupyter](http://jupyter.org/) installation, run

```
$ pip install markdown-kernel
$ python markdown_kernel.install
```

Verify if you have `markdown` kernel install with command

```
$ jupyter kernelspec list
```

## Why a markdown kernel for Jupyter?

A markdown kernel for Jupyter sounds like a stupid idea because Jupyter has
native Markdown cells. The problem is that Jupyter markdown cells are
rendered at the frontend and does not interact with Jupyter kernels.
It is therefore difficult to pass variables from kernels to markdown cells
to create dynamic output.

This markdown kernel is a simple Jupyter kernel that parses and displays
the cell content as markdown. So that you can type in markdown texts

```
This is a summary of results

* item 1
* item 2
```

and it would be rendered as

* item 1
* item 2


But wait, this is *still stupid* because you can do the same thing in
Jupyter, only easier. And what is the point of a markdown kernel by itself
without any variables?

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

![example](https://user-images.githubusercontent.com/9889312/37932344-e1c13e96-310d-11e8-963c-5fe26c6523d1.png)
