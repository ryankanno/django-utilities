#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin


class CreatedModifiedAdminMixin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        if not change: 
            obj.created_by = request.user
        obj.updated_by = request.user
        super(CreatedModifiedAdminMixin, self).save_model(request, 
            obj, form, change)

# vim: filetype=python
