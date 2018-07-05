# coding=utf-8

from .models import BaseInfo
import xadmin
from .models import wantJob, experience
from xadmin.layout import Fieldset, Main, Side, Row, FormHelper

class wantJobInline(object):
    model = wantJob
    extra = 0

    def get_form_layout(self):
        if self.org_obj:
            self.form_layout = (
                Main(
                    Fieldset('基本信息',

                             Row('expectSalary', 'position')
                     ),
                ),
            )
        return super(wantJobInline, self).get_form_layout()


class experienceInline(object):
    model = experience
    extra = 0



class BaseInfoAdmin(object):
    list_display = ['name', 'application', 'match', 'workExperiod']

    inlines = [wantJobInline, experienceInline]

    def get_form_layout(self):
        if self.org_obj:
            self.form_layout = (
                Main(
                    Fieldset('基本信息',
                             Row('application', 'name'),

                     ),
                ),
            )
        return super(BaseInfoAdmin, self).get_form_layout()



xadmin.site.register(BaseInfo, BaseInfoAdmin)