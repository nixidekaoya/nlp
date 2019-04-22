# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 21:53:53 2019

@author: LI Mofei
"""

import sqlitedatastore as datastore

if __name__ == '__main__':
    datastore.connect()
    datastore.create_table()
    datastore.close()