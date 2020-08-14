#!/usr/bin/env python3
# -*- coding: utf-8 -*-

extensions = []

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

# General information about the project.
project = 'Aging PMC Corrections documents'
copyright = '2019, Aging'
author = 'Aginh'


version = '0.1'
release = '0.1'

language = None
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

html_theme = 'default'

html_static_path = ['_static']

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'AgingPMCCorrectionsdocumentsdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'AgingPMCCorrectionsdocuments.tex', 'Aging PMC Corrections documents Documentation',
     'Aging', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'Agingpmccorrectionsdocuments', 'AgingPMC Corrections documents Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'AgingPMCCorrectionsdocuments', 'AgingPMC Corrections documents Documentation',
     author, 'AgingPMCCorrectionsdocuments', 'One line description of project.',
     'Miscellaneous'),
]

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'https://docs.python.org/': None}


# -- ReadTheDoc requirements and local template generation---------------------

# on_rtd is whether we are on readthedocs.org, this line of code grabbed from docs.readthedocs.org

html_context = {
    'css_files': [
        'https://media.readthedocs.org/css/sphinx_rtd_theme.css',
        'https://media.readthedocs.org/css/readthedocs-doc-embed.css',
        '_static/theme_overrides.css',
    ],
}
