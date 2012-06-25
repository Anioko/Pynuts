# -*- coding: utf-8 -*-

"""Jinja environment filters for Pynuts."""

from flask import escape
from flask.ext.wtf import (
    QuerySelectField, QuerySelectMultipleField, BooleanField)


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
    elif isinstance(field, QuerySelectField):
        if field.data:
            return escape(field.get_label(field.data))
    elif isinstance(field, BooleanField):
        return u'✓' if field.data else u'✕'
    return escape(field.data)
