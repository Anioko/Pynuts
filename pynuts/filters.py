# -*- coding: utf-8 -*-

"""Jinja environment filters for Pynuts."""

from flask import escape
from flask.ext.wtf import (
    QuerySelectField, QuerySelectMultipleField, BooleanField, DateField)


def data(field):
    """Field data beautifier.

    QuerySelectMultipleField
      Renders comma-separated data.
    QuerySelectField
      Renders the selected value.
    BooleanField
      Renders '✓' or '✕'

    Example:

    .. sourcecode:: html+jinja

        <dd>{{ field | data }}</dd>

    """
    if isinstance(field, QuerySelectMultipleField):
        if field.data:
            return escape(
                u', '.join(field.get_label(data) for data in field.data))
        else:
            return u'∅'
    elif isinstance(field, QuerySelectField):
        if field.data:
            return escape(field.get_label(field.data))
    elif isinstance(field, BooleanField):
        return u'✓' if field.data else u'✕'
    elif isinstance(field, DateField):
        if field.data:
            return field.data.strftime(field.format)
    return escape(field.data)