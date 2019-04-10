# -*- coding: utf-8 -*-
'''
Management of Microsoft SQLServer Database Jobs
===========================================

The mssql_job module is used to create
and manage SQL Server Jobs

.. code-block:: yaml

    yolo:
      mssql_job.present
'''
from __future__ import absolute_import


def __virtual__():
    '''
    Only load if the mssql module is present
    '''
    return 'mssql.version' in __salt__





def absent(name, **kwargs):
    '''
    Ensure that the named job is absent

    name
        The name of the database to remove
    '''
    ret = {'name': name, 'changes': {}, 'result': True, 'comment': ''}

    if not __salt__['mssql.job_exists'](name):
        ret['comment'] = 'Job {0} is not present'.format(name)
        return ret
    if __opts__['test']:
        ret['result'] = None
        ret['comment'] = 'Job {0} is set to be removed'.format(name)
        return ret
    if __salt__['mssql.job_remove'](name, **kwargs):
        ret['comment'] = 'Job {0} has been removed'.format(name)
        ret['changes'][name] = 'Absent'
        return ret
    # else:
    ret['result'] = False
    ret['comment'] = 'Job {0} failed to be removed'.format(name)
    return ret
