![screenshot](https://github.com/user-attachments/assets/b5ec09b6-c8c7-454a-85af-1bba97593632)

## Unfold Django Admin Theme

[![PyPI - Version](https://img.shields.io/pypi/v/django-unfold.svg?style=for-the-badge)](https://pypi.org/project/django-unfold/)
[![Build](https://img.shields.io/github/actions/workflow/status/unfoldadmin/django-unfold/release.yml?style=for-the-badge)](https://github.com/unfoldadmin/django-unfold/actions?query=workflow%3Arelease)
![Pre Commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=for-the-badge)
![Code Style - Ruff](https://img.shields.io/badge/code%20style-ruff-30173D.svg?style=for-the-badge)

Unfold is a theme for Django admin that incorporates common best practices for building full-fledged admin areas. It is designed to work on top of the default administration provided by Django.

- **Documentation:** Full docs are available at [unfoldadmin.com](https://unfoldadmin.com?utm_medium=github&utm_source=unfold).
- **Formula:** Repository with demo implementation at [github.com/unfoldadmin/formula](https://github.com/unfoldadmin/formula?utm_medium=github&utm_source=unfold).

## Table of contents <!-- omit from toc -->

- [Fork Updates](#fork-updates)
- [Third party packages support](#third-party-packages-support)
- [Instalattion](#installation)

## Fork Updates <!-- omit from toc -->
- Constance
- Footer


## Third party packages support <!-- omit from toc -->

- Constance -> [documentation and settings.py example](docs/integrations/django-constance.md)


## Installation <!-- omit from toc -->
### Compiling Styles

When creating a custom admin dashboard, you are going to locate all your HTML code with Tailwind classes in your project, so newly added dashboard styles are not compiled. To do so, the first thing which is needed is to edit `UNFOLD` variable in `settings.py` and add `STYLES` key pointing at the new CSS stylesheet containing all new styles.

```python
# settings.py
from django.templatetags.static import static


UNFOLD = {
    "STYLES": [
        lambda request: static("css/styles.css"),
    ],
}
```

Before compiling the styles it is important to install all node dependencies as well which in our case contain just TailwindCSS and its typography plugin for styling formatted blocks of texts inside the WYSIWYG editor.

```bash
npm install
```
To compile new styles, run one of the commands below depending on your needs. To see what exactly the commands are doing and how the files are linked check `scripts` section inside `package.json`.


```bash
npm run tailwind:build  # one-time build
npm run tailwind:watch  # watch all files for changes
```
