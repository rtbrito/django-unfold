![screenshot](https://github.com/user-attachments/assets/b5ec09b6-c8c7-454a-85af-1bba97593632)

## Unfold Django Admin Theme

[![PyPI - Version](https://img.shields.io/pypi/v/django-unfold.svg?style=for-the-badge)](https://pypi.org/project/django-unfold/)
[![Build](https://img.shields.io/github/actions/workflow/status/unfoldadmin/django-unfold/release.yml?style=for-the-badge)](https://github.com/unfoldadmin/django-unfold/actions?query=workflow%3Arelease)
![Pre Commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=for-the-badge)
![Code Style - Ruff](https://img.shields.io/badge/code%20style-ruff-30173D.svg?style=for-the-badge)

Unfold is a theme for Django admin that incorporates common best practices for building full-fledged admin areas. It is designed to work on top of the default administration provided by Django.

- **Documentation:** Full docs are available at [unfoldadmin.com](https://unfoldadmin.com?utm_medium=github&utm_source=unfold).
- **Unfold:** Demo site is available at [unfoldadmin.com](https://unfoldadmin.com?utm_medium=github&utm_source=unfold).
- **Formula:** Repository with demo implementation at [github.com/unfoldadmin/formula](https://github.com/unfoldadmin/formula?utm_medium=github&utm_source=unfold).
- **Turbo:** Django & Next.js boilerplate implementing Unfold at [github.com/unfoldadmin/turbo](https://github.com/unfoldadmin/turbo?utm_medium=github&utm_source=unfold).
- **Discord:** Join the Unfold community on [Discord](https://discord.gg/9sQj9MEbNz).

## Features

- **Visual**: Provides a new user interface based on the Tailwind CSS framework.
- **Sidebar:** Simplifies the creation of sidebar navigation with icons, collapsibles, and more.
- **Dark mode:** Supports both light and dark mode versions.
- **Actions:** Offers multiple ways to define actions within different parts of the admin interface.
- **Filters:** Custom dropdowns, numeric, datetime, and text fields.
- **Dashboard:** Includes helpers for creating custom dashboard pages.
- **Components:** Reusable UI components such as cards, buttons, and charts.
- **WYSIWYG widget:** Built-in support for WYSIWYG (Trix).
- **Array widget:** Built-in widget for `django.contrib.postgres.fields.ArrayField`.
- **Inline tabs:** Groups inlines into tab navigation in the change form.
- **Model tabs:** Allows defining custom tab navigation for models.
- **Fieldset tabs:** Merges multiple fieldsets into tabs in the change form.
- **Sortable inlines:** Allows sorting inlines by dragging and dropping.
- **Environment label**: Distinguishes between environments by displaying a label.
- **Nonrelated inlines**: Displays nonrelated models as inlines in the change form.
- **Favicons**: Built-in support for configuring various site favicons.
- **Colors:** Allows customization of the default color scheme.
- **Changeform modes:** Displays fields in compressed mode in the change form.
- **Parallel admin**: Supports [running the default admin](https://unfoldadmin.com/blog/migrating-django-admin-unfold/?utm_medium=github&utm_source=unfold) alongside Unfold.
- **Third party packages:** Default support for multiple popular applications.
- **Configuration:** Most basic options can be changed in `settings.py`.
- **Dependencies:** Fully based on `django.contrib.admin`.
- **VS Code**: Project configuration and development container included.


# Fork Updates
## Features

- Constance


# Third party packages

- Constance


## Constance

tests/server/example/settings.py
```python
    INSTALLED_APPS = [
        "unfold",
        "unfold.contrib.constance",
        ...
        "constance",
    ]

    CONSTANCE_CONFIG = {
        "Select": (
            "Sunday",
            ("The day of the week"),
            "weekday_select",
        ),
        "Bool": (
            False,
            ("Boolean"),
            "boolean_field",
        ),
        "DATE": (
            date(year=2025, month=1, day=1),
            ("Date"),
            date,
        ),
        "Time": (
            time(hour=20, minute=0),
            ("TIME"),
            time,
        ),
        "Range_Integer_Field": (
            1,
            ("Range Integer Field"),
            "range_integer_field",
        ),
    }

    CONSTANCE_ADDITIONAL_FIELDS = {
        "integer_field": [
            "django.forms.fields.IntegerField",
            {
                "widget": "unfold.widgets.UnfoldAdminIntegerFieldWidget",
            },
        ],
        "weekday_select": [
            "django.forms.fields.ChoiceField",
            {
                "widget": "unfold.widgets.UnfoldAdminSelectWidget",
                "choices": (
                    (0, ("Sunday")),
                    (1, ("Monday")),
                    (2, ("Tuesday")),
                    (3, ("Wednesday")),
                    (4, ("Thursday")),
                    (5, ("Friday")),
                    (6, ("Saturday")),
                ),
            },
        ],
        "range_integer_field": [
            "django.forms.fields.IntegerField",
            {
                "widget": "unfold.widgets.UnfoldAdminIntegerRangeWidget",
                "lower": 1,
                "upper": 30,
            },
        ],
        "boolean_field": [
            "django.forms.fields.BooleanField",
            {
                "widget": "unfold.widgets.UnfoldBooleanSwitchWidget",
            }
        ],
    }

    CONSTANCE_CONFIG_FIELDSETS = {
        "Test": {
            "fields": (
                "Select",
                "Bool",
                "DATE",
                "Time",
                "Range_Integer_Field",
            )
        },
    }

    CONSTANCE_BACKEND = "constance.backends.database.DatabaseBackend"

    TIME_ZONE = "Europe/Lisbon"
```
