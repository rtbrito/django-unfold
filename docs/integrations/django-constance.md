---
title: django-constance
order: 0
description: Integration with django-constance.
---

# django-constance

To make this application work, add `unfold.contrib.constance` into `settings.py` in `INSTALLED_APPS` variable before right after `unfold`. This app should ensure that templates coming from django-constance are overridden by Unfold.


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
        "Date": (
            date(year=2025, month=1, day=1),
            ("Date"),
            "date_field",
        ),
        "Time": (
            time(hour=20, minute=0),
            ("TIME"),
            "time_field",
        ),
        "File_atribute": (
            "",
            ("File"),
            "filefield",
        ),
    }

    CONSTANCE_ADDITIONAL_FIELDS = {
        "integer_field": [
            "django.forms.fields.IntegerField",
            {
                "widget": "unfold.widgets.UnfoldAdminIntegerFieldWidget",
            }
        ],
        "boolean_field": [
            "django.forms.fields.BooleanField",
            {
                "widget": "unfold.widgets.UnfoldBooleanSwitchWidget",
                "required": False,
            }
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
        "filefield": [
            "django.forms.fields.FileField",
            {
                "widget": "unfold.widgets.UnfoldAdminFileFieldWidget",
            }
        ],
        "date_field": [
            "django.forms.fields.DateField",
            {
                "widget": "unfold.widgets.UnfoldAdminDateWidget",
            }
        ],
        "time_field": [
            "django.forms.fields.TimeField",
            {
                "widget": "unfold.widgets.UnfoldAdminTimeWidget",
            }
        ],
    }

    CONSTANCE_CONFIG_FIELDSETS = {
        "Test": {
            "fields": (
                "Select",
                "Bool",
                "Date",
                "Time",
                "File_atribute",
            )
        },
    }

    CONSTANCE_BACKEND = "constance.backends.database.DatabaseBackend"

    TIME_ZONE = "Europe/Lisbon"
```
