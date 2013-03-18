Tachikoma
=========

oni@section9.co.uk

A short python script that does the same thing as Jekyll, only stripped out and in Python. It builds a static website from posts and templates, thus giving a sense of a dynamic website with no overhead of databases and similar.

This is written in Python3 and requires the following packages:

* markdown
* jinja2
* jinja2 loop extention
* yaml [download](http://pyyaml.org/wiki/PyYAML "PyYAML download page")
* sudo pip-3.2 install git+git://github.com/OniDaito/mdx_outline.git

The last requirement is a custom version of the mdx_outline plugin for Markdown. You can use the master branch instead but check the comment in the code for this one.

The structure of the website should be as follows


    -\Your Site Dir
     .
     -\_posts
     .
     -\_layouts
     .
     -\_site
     .
     -\any extra directories such as images, css etc


Posts should be in the form YYYY-MM-DD-Title-goes-here.markdown (or .md) and be placed in the _posts directory.

Layouts should be placed in _layouts and be of the form .html with Jinja2 markup.

Markdown and HTML files must have YAML front matter, in the same style as Jekyll. Something along the lines of:

    ---
    layout: default
    title: Section9 dot co dot uk ltd - Benjamin Blundell - Wouldn't it be nice if...
    idx: home
    ---

Layout is the only required field. Any files without front matter are not considered.

Your final site appears in the _site directory, nicely compiled.

To execute the script run the following

    python3 tachikoma.py <path to your site directory> -s 


The '-s' is optional. It runs a small server at localhost:8000 for you to check your page. It checks the directory every 2 seconds for changes and rebuilds if needed.

