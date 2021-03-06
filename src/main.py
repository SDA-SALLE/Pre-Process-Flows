# -*- encoding: utf-8 -*-

#! /usr/bin/env python
#created by @ceapalaciosal
#under code Creative Commons
import sys
import os
sys.path.append('core')
from clear import *
from ExcelCSV import*
from CSVMatriz import*
from disolver import*
from projection import *

print 'Insert information'
Year = raw_input('Insert Year Flows:')
YearProjection = raw_input('Insert Year Proyection:')


folder = os.path.join('..', 'data','out', '')
clear(folder)

print ('Realizando Proceso para Fuentes Moviles')
folder = os.path.join('..', 'data', 'in', 'Flows', '')

listaExcel (folder)
listaCSV(folder, Year)

flows = os.path.join('..', 'data', 'out', 'RPM' + '_' + Year + '.csv')
category = os.path.join ('..', 'data', 'in','Constants', 'CATEGORY.xlsx')
disolver(flows, category, Year)

#flows = os.path.join('..', 'data', 'out', 'RPM.csv')
projections = os.path.join('..', 'data','in', 'Projection', 'Resuspended_grow_factors.xlsx')
projection(flows, projections, YearProjection , 0)

flows = os.path.join('..', 'data', 'out', 'MOB' + '_' + Year + '.csv')
projections = os.path.join('..', 'data','in', 'Projection', 'Movile_grow_factors.xlsx')
projection(flows, projections,YearProjection , 1)
