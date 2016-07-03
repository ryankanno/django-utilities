#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings

from ..db.fields import CreatedDateTimeField
from ..db.fields import ModifiedDateTimeField


class CreatedModifiedMixin(models.Model):

    modified_at = ModifiedDateTimeField()
    modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='modified_by_%(class)s_set', null=True, blank=True)

    created_at = CreatedDateTimeField()
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='created_by_%(class)s_set', null=True, blank=True)

    class Meta:
        abstract = True

# vim: filetype=python
