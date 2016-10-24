# -*- coding: utf-8 -*-

print '...imports and setup'

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import StringIO
import os
import sys
import plotly.plotly as py
import cufflinks as cf
import plotly.graph_objs as go


#filepath='C:\\Users\\freud\\Dropbox\\wit\\projects\\CityInSight\\plotly'
filepath='C:\\Users\\mwilliams\\Dropbox\\wit\\projects\\CityInSight\\plotly'
os.chdir(filepath)

plt.style.use('ggplot')


#%% Import data
print '...import data'
     

# testing github


    
#%%
    
#py_emissions = df_emissions.iplot(kind='area', fill=True,
#                                  sharing='private',
#                                  filename='test1/emissions')
                                  
#print py_emissions._repr_html_()

#%% stacked area chart

filename = 'emissionsTest.csv'
df_emissions = pd.read_csv(filename, index_col=0).T

layout1 = go.Layout(title='Emissions', width=800, height=600)

fg_emissions = df_emissions.iplot(kind='area', fill=True,
                                  sharing='private',
                                  layout=layout1,
                                  asFigure=True,
                                  filename='test1/fg_emissions')
                                  
py.image.save_as(fg_emissions, filename='fg_emissions.pdf')

#%% stacked area chart - population

filename = 'population.csv'
df_population = pd.read_csv(filename, index_col=0)

df_population.rename(columns={
    'transition' : 'external_students'},
    inplace=True)

layout1 = go.Layout(width=800, height=600)

fg_population = df_population.iplot(kind='area', fill=True,
                                  sharing='private',
                                  layout=layout1,
                                  asFigure=True)
                                  
py.image.save_as(fg_population, filename='fg_population.png')

#%% stacked area chart - energy_residential

filename = 'energy_residential.csv'
df_energy_residential = pd.read_csv(filename, index_col=0).T

layout1 = go.Layout(width=800, height=600)

fg_energy_residential = df_energy_residential.iplot(kind='area', fill=True,
                                  sharing='private',
                                  layout=layout1,
                                  asFigure=True)

fg_energy_residential['layout']['xaxis'].update({'gridwidth' : 2})
fg_energy_residential['layout']['yaxis'].update({'gridwidth' : 2})
                                  
py.image.save_as(fg_energy_residential, filename='fg_energy_residential.png')


fg_energy_residential_2 = df_energy_residential.iplot(kind='line',
                                  sharing='private',
                                  layout=layout1,
                                  asFigure=True)

fg_energy_residential_2['layout']['xaxis'].update({'gridwidth' : 2})
fg_energy_residential_2['layout']['yaxis'].update({'gridwidth' : 2})
                                  
py.image.save_as(fg_energy_residential_2, filename='fg_energy_residential_2.png')

#%% stacked area chart - dwelling units total

filename = 'dwellingUnits_tot.csv'
df_dwellingUnits_tot = pd.read_csv(filename, index_col=0)

layout1 = go.Layout(width=800, height=600)

fg_dwellingUnits_tot = df_dwellingUnits_tot.iplot(kind='area', fill=True,
                                  sharing='private',
                                  layout=layout1,
                                  asFigure=True)

fg_dwellingUnits_tot['layout']['xaxis'].update({'gridwidth' : 2})
fg_dwellingUnits_tot['layout']['yaxis'].update({'gridwidth' : 2})
                                  
py.image.save_as(fg_dwellingUnits_tot, filename='fg_dwellingUnits_tot.png')

fg_dwellingUnits_tot2 = df_dwellingUnits_tot.iplot(kind='line',
                                  sharing='private',
                                  layout=layout1,
                                  asFigure=True)

fg_dwellingUnits_tot2['layout']['xaxis'].update({'gridwidth' : 2})
fg_dwellingUnits_tot2['layout']['yaxis'].update({'gridwidth' : 2})
fg_dwellingUnits_tot2['layout']['yaxis'].update({'range' : [0,140000]})
                                  
py.image.save_as(fg_dwellingUnits_tot2, filename='fg_dwellingUnits_tot2.png')

#%% stacked area chart - dwelling units new

filename = 'dwellingUnits_newCum.csv'
df_dwellingUnits_newCum = pd.read_csv(filename, index_col=0)

layout1 = go.Layout(width=800, height=600)

fg_dwellingUnits_newCum = df_dwellingUnits_newCum.iplot(kind='area', fill=True,
                                  sharing='private',
                                  layout=layout1,
                                  asFigure=True)

fg_dwellingUnits_newCum['layout']['xaxis'].update({'gridwidth' : 2})
fg_dwellingUnits_newCum['layout']['yaxis'].update({'gridwidth' : 2})
                                  
py.image.save_as(fg_dwellingUnits_newCum, filename='fg_dwellingUnits_newCum.png')

fg_dwellingUnits_newCum2 = df_dwellingUnits_newCum.iplot(kind='line',
                                  sharing='private',
                                  layout=layout1,
                                  asFigure=True)

fg_dwellingUnits_newCum2['layout']['xaxis'].update({'gridwidth' : 2})
fg_dwellingUnits_newCum2['layout']['yaxis'].update({'gridwidth' : 2})
                                  
py.image.save_as(fg_dwellingUnits_newCum2, filename='fg_dwellingUnits_newCum2.png')

#%% stacked bar chart

filename = 'trans_dailyPersonTrips.csv'
df_trans_dailyPersonTrips = pd.read_csv(filename, index_col=0)

layout1 = go.Layout(title='Daily Person Trips',
                    width=800, height=600, barmode='stack')

fg_trans_dailyPersonTrips = df_trans_dailyPersonTrips.iplot(kind='bar',
  sharing='private',
  layout=layout1,
  asFigure=True,
  filename='test1/fg_trans_dailyPersonTrips')

#barmode parameter above not working so update manually  
#fg_trans_dailyPersonTrips['layout'].update({'barmode' : 'stack'})
                                  
py.image.save_as(fg_trans_dailyPersonTrips,
                 filename='fg_trans_dailyPersonTrips.pdf')






