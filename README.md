[![Anaconda-Server Badge](https://anaconda.org/conda-forge/markdown-kernel/badges/version.svg)](https://anaconda.org/conda-forge/markdown-kernel)
[![PyPI version](https://badge.fury.io/py/markdown-kernel.svg)](https://badge.fury.io/py/markdown-kernel)

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

## Use a Markdown kernel in SoS Notebook

If you are familiar with [`R Markdown`](https://github.com/rstudio/rmarkdown), you might know and like its [inline code](https://rmarkdown.rstudio.com/lesson-4.html) that allows results to be inserted directly into the text of a .Rmd file by enclosing the code with `r `. This is really convenient for
writing Rmarkdown report but cannot be done in Jupyter because Jupyter's markdown cells are rendered at the frontend and do not interact with Jupyter kernels  (See [ipython/ipython#2592](https://github.com/ipython/ipython/issues/2592), [jupyter/help#41](https://github.com/jupyter/help/issues/41),and [jupyter/notebook#3463](https://github.com/jupyter/notebook/issues/3463) for related discussions).

[SoS Notebook](https://vatlab.github.io/sos-docs/) is a Jupyter kernel that supports the use of multiple kernels in one Jupyter notebook.
Although a markdown kernel by itself cannot interpolate and evaluate expressions either, you can the `%expand` magic of SoS to enable
inline expressions in Jupyter, for Python, R, and potentially many other languages. Here is how it works:

### `%expand` content of a cell using SoS (Python) variables

![image](https://user-images.githubusercontent.com/9889312/68431746-878ba280-0178-11ea-8c47-79f5db775299.png)

### `%expand` in subkernels such as R

The `--in` option of magic `%expand` allows you to expand the cell content in specified subkernel.

![image](https://user-images.githubusercontent.com/9889312/68431685-6fb41e80-0178-11ea-8ccb-56135d6a1c37.png)

