from datetime import date, datetime, time
from decimal import Decimal

from constance.settings import ADDITIONAL_FIELDS
from django.core.files import File

DEFAULT_ADDITIONAL_FIELDS = {
    int: [
        "django.forms.fields.IntegerField",
        {
            "widget": "unfold.widgets.UnfoldAdminIntegerFieldWidget",
        },
    ],
    float: [
        "django.forms.fields.FloatField",
        {
            "widget": "unfold.widgets.UnfoldAdminIntegerFieldWidget",
        },
    ],
    Decimal: [
        "django.forms.fields.DecimalField",
        {
            "widget": "unfold.widgets.UnfoldAdminIntegerFieldWidget",
        },
    ],
    bool: [
        "django.forms.fields.BooleanField",
        {
            "widget": "unfold.widgets.UnfoldBooleanSwitchWidget",
            "required": False,
        },
    ],
    File: [
        "django.forms.fields.FileField",
        {
            "widget": "unfold.widgets.UnfoldAdminFileFieldWidget",
        },
    ],
    str: [
        "django.forms.fields.CharField",
        {
            "widget": "unfold.widgets.UnfoldAdminTextInputWidget",
            "required": False,
        },
    ],
    "textarea": [
        "django.forms.fields.CharField",
        {
            "widget": "unfold.widgets.UnfoldAdminTextareaWidget",
            "required": False,
            "widget_kwargs": {
                "attrs": {"rows": 3},
            },
        },
    ],
    date: [
        "django.forms.fields.DateField",
        {
            "widget": "unfold.widgets.UnfoldAdminDateWidget",
        },
    ],
    time: [
        "django.forms.fields.TimeField",
        {
            "widget": "unfold.widgets.UnfoldAdminTimeWidget",
        },
    ],
    datetime: [
        "django.forms.fields.DateTimeField",
        {
            "widget": "unfold.widgets.UnfoldAdminSplitDateTimeVerticalWidget",
        },
    ],
}


def update_additional_fields(new_fields_dict) -> dict:
    """
    Safely update the additional_fields, checking the entries.
    With this we can have new additional fields without overriding the existing ones.
    """
    for field_type, field_config in new_fields_dict.items():
        if field_type not in ADDITIONAL_FIELDS:
            ADDITIONAL_FIELDS[field_type] = field_config


update_additional_fields(DEFAULT_ADDITIONAL_FIELDS)
