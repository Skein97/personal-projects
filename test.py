import calendar
import math as m
import scipy.stats as s
import numpy as np
import matplotlib.pyplot as plt
from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'took {t2 - t1}s')
        return result

    return wrapper


def daily_wsi():
    time = [((str(num * 100).zfill(4)) + 'hrs') for num in range(24)]
    wsi1 = [float(input(f'{time[i]} wsi value: ')) for i in range(24)]
    daily_wsi_fn = dict(zip(time, wsi1))
    return daily_wsi_fn

print(daily_wsi())
# rotor_diameter = 117
# rotor_area = m.pi * ((rotor_diameter / 2)**2)
# max_power = 4000
# speed_ci = 3
# speed_co = 25
# wt_efficiency = 34
# air_density = 1.283117721
# wind_speed = 6.45
#
#
#
#
#
#
#
# def avg_hpg():
#     # power curve function
#     def pc(x):
#         power_curve = ((x / 100) ** 3) * rotor_area * air_density * (wt_efficiency / 100) / 2000
#         if power_curve > max_power:
#             power_curve = max_power
#         else:
#             power_curve = power_curve
#         return power_curve
#
#     # Probability density function using a weibull distribution
#     def weib(x, n, a):
#         prob_density = (a / n) * (x / n) ** (a - 1) * np.exp(-(x / n) ** a)
#         return prob_density
#
#     # Generate a list of probability of power generated at any wind speed
#     ep_pot = [(pc(x) * weib(x/100, wind_speed, 2)) for x in range(int(speed_ci * 100), int((speed_co + 0.1) * 100), 10)]
#     # Generate a list of probability density of wind speeds at a location based on average wind speed
#     pd = [weib(x/100, wind_speed, 2) for x in range(0, int((speed_co + 0.1) * 100), 10)]
#     return sum(ep_pot) / sum(pd)
#
# print(avg_hpg())



#
#
#
# def wt_pc():
#     pc = [((x/100)**3) * rotor_area * air_density * wt_efficency / 2 for x in range(0, int(speed_co*100), 10) if (x/100) < int(speed_ci)]
#     for i in pc:
#         if i > max_power:
#             i = max_power
#         else:
#             pass
#     print(pc)
#
# wt_pc()
#
# print(wt_pc)


# Demand class
# class Demand:
#     # Attributes
#     def __init__(self, hourly_demand=None):
#         print('-------------------------------------------')
#         print('Input Power Demand')
#         print('-------------------------------------------')
#         if not hourly_demand:
#             self.hourly_demand = input('Hourly demand: ')
#         else:
#             self.hourly_demand = hourly_demand
#
#         print('-------------------------------------------')
#
#     def xteristics(self):
#         print('-------------------------------------------')
#         print(f'Hourly demand: {self.hourly_demand}kWh')
#         print('-------------------------------------------')
#
#
# class WindTurbine:
#     # Attributes function
#     def __init__(self, wt_name=None, rotor_diameter=None, hub_height=None, max_power=None, speed_ci=None, speed_co=None,
#                  wt_unit_cost=None, wt_efficiency=None, wt_lifetime=None):
#         print('-------------------------------------------')
#         print('Input Wind Turbine Characteristics')
#         print('-------------------------------------------')
#         if not wt_name:
#             self.wt_name = input('Wind turbine type: ')
#         else:
#             self.wt_name = wt_name
#
#         if not rotor_diameter:
#             self.rotor_diameter = input('Rotor Diameter: ')
#         else:
#             self.rotor_diameter = rotor_diameter
#
#         if not hub_height:
#             self.hub_height = input('Hub height: ')
#         else:
#             self.hub_height = hub_height
#
#         if not max_power:
#             self.max_power = input('Max power rating: ')
#         else:
#             self.max_power = max_power
#
#         if not speed_ci:
#             self.speed_ci = input('Cut in speed: ')
#         else:
#             self.speed_ci = speed_ci
#
#         if not speed_co:
#             self.speed_co = input('Cut out speed: ')
#         else:
#             self.speed_co = speed_co
#
#         if not wt_unit_cost:
#             self.wt_unit_cost = input('Cost of wind turbine unit: ')
#         else:
#             self.wt_unit_cost = wt_unit_cost
#
#         if not wt_efficiency:
#             self.wt_efficiency = input('Wind turbine Efficiency: ')
#         else:
#             self.wt_efficiency = wt_efficiency
#
#         if not wt_lifetime:
#             self.wt_lifetime = input('Wind turbine lifetime: ')
#         else:
#             self.wt_lifetime = wt_lifetime
#
#         print('-------------------------------------------')
#
#     # characteristics function
#     def xteristics(self):
#         print('-------------------------------------------')
#         print(f'Wind turbine name: {self.wt_name}')
#         print(f'Rotor Diameter: {self.rotor_diameter}m')
#         print(f'Hub height: {self.hub_height}m')
#         print(f'Max power rating: {self.max_power}kw')
#         print(f' Cut in speed: {self.speed_co}m/s')
#         print(f' Cut out speed: {self.speed_ci}m/s')
#         print(f'Cost of wind turbine unit: {self.wt_unit_cost}£')
#         print(f'Wind turbine efficiency: {self.wt_efficiency}%')
#         print(f'Wind turbine lifetime: {self.wt_lifetime}years')
#         print('-------------------------------------------')
#
#
# # Wind farm object
# class WindFarm:
#     def __init__(self, wt=None, demand=None, cost=None):
#         # Create attribute objects
#         #demand_in =
#         #wt_in =
#
#
#         # Perform internal calculations
#         #num_wt_units = float(demand_in.hourly_demand) / float(wt_in.max_power)
#        # wt_installation_cost = num_wt_units * float(wt_in.wt_unit_cost)
#
#         if not demand:
#             self.demand = Demand()
#         else:
#             self.demand = demand
#         if not wt:
#             self.wt = WindTurbine(max_power= self.demand.hourly_demand)
#         else:
#             self.wt = wt
#         if not cost:
#             self.cost = float(self.demand.hourly_demand) * float(self.wt.wt_unit_cost) / float(self.wt.max_power)
#         else:
#             self.cost = cost
#
#     def in_xteristics(self):
#         print('-------------------------------------------')
#
#
#         print(f'Wind farm cost: £{self.cost}')
#         print('-------------------------------------------')
#
#     def xteristics(self):
#         self.in_xteristics()
#         print('It worked??!')
#
#
# wf1 = WindFarm()
# wf1.xteristics()

# class myStruct():
#     def __init__(self,name=None,salary=None,doB=None,title=None):
#         if not name:
#             self.name = input('Enter name: ')
#         else:
#             self.name=name
#         if not salary:
#             self.salary = input('Enter salary: ')
#         else:
#             self.salary=salary
#         if not doB:
#             self.doB = input('Enter doB: ')
#         else:
#             self.doB=doB
#         if not title:
#             self.title = input('Enter title: ')
#         else:
#             self.title=title
#
#
# structure1 = myStruct()
# print(vars(structure1))


# def daily_wsi():
#     time = [((str(num * 100).zfill(4))+'hrs') for num in range(0,3)]
#     wsi1 = [input(f'{time[i]} wsi value: ') for i in range(0,3)]
#     daily_wsi = dict(zip(time, wsi1))
#     return daily_wsi
#
#
# print(f'Daily wind speed index: {daily_wsi()} ')


# def monthly_wsi():
#     date = [calendar.month_name[i] for i in range(1, 13)]
#     wsi2 = [input(f'{date[i]} wsi value: ') for i in range(12)]
#     monthly_wsi = dict(zip(date, wsi2))
#     return monthly_wsi
#

