---
title: django-constance
order: 0
description: Integration with django-constance.
---

# django-constance

To make this application work, add `unfold.contrib.constance` into `settings.py` in `INSTALLED_APPS` variable before right after `unfold`. This app should ensure that templates coming from django-constance are overridden by Unfold.


tests/server/example/settings.py
```python
    from datetime import date, datetime, time
    from decimal import Decimal
    from django.core.files import File

    INSTALLED_APPS = [
        "unfold",
        "unfold.contrib.constance",
        ...
        "constance",
    ]

    CONSTANCE_CONFIG = {
        "String": (
            "default",
            "String",
            str,
        ),
        "TextArea": (
            "",
            "TextArea",
            "textarea",
        ),
        "Int": (
            0,
            "Integer",
            int,
        ),
        "Float": (
            0.01,
            "Float",
            float,
        ),
        "Decimal": (
            0.02,
            "Decimal",
            Decimal,
        ),
        "Select": (
            "Sunday",
            "The day of the week",
            "weekday_select",
        ),
        "Bool": (
            False,
            "Boolean",
            bool,
        ),
        "Date": (
            date(year=2025, month=1, day=1),
            "Date",
            date,
        ),
        "Time": (
            time(hour=20, minute=0),
            "TIME",
            time,
        ),
        "Datetime": (
            datetime(year=2025, month=1, day=1, hour=20, minute=0),
            "DateTime",
            datetime,
        ),
        "File": (
            "",
            "File",
            File,
        ),
    }

    # Example of an additional custom field
    CONSTANCE_ADDITIONAL_FIELDS = {
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
    }

    CONSTANCE_CONFIG_FIELDSETS = {
        "Test": {
            "fields": (
                "String",
                "TextArea",
                "Int",
                "Float",
                "Decimal",
                "Select",
                "Bool",
                "Date",
                "Time",
                "Datetime",
                "File",
            )
        },
    }

    CONSTANCE_BACKEND = "constance.backends.database.DatabaseBackend"

    TIME_ZONE = "Europe/Lisbon"
```
