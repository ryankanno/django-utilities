#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

from utilities.db.fields import CreatedDateTimeField, ModifiedDateTimeField
import datetime


class CreatedModifiedMixin(models.Model):

    modified_at = ModifiedDateTimeField()
    modified_by = models.ForeignKey(User, 
        related_name='modified_by_%(class)s_set', null=True, blank=True)

    created_at = CreatedDateTimeField()
    created_by = models.ForeignKey(User, 
        related_name='created_by_%(class)s_set', null=True, blank=True)

    class Meta:
        abstract = True

# vim: filetype=python
