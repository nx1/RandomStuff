#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 15:05:01 2019

@author: nk7g14
"""

import numpy as np
from itertools import combinations

class Charge:
    def __init__(self, number):
        self.number = number
        self.magnitude = 1
        self.position = [np.random.random(), np.random.random() * 2 * np.pi]

    def Move(self):
        dr = 0.01
        dpsi = 0.1

        r = self.position[0]
        psi = self.position[1]
        
        r_new = r + np.random.choice([-1, 1]) * dr
        psi_new = (psi + np.random.choice([-1, 1]) * dpsi)%2*np.pi

        if r_new > self.R:
            print('Charge radius greater than disk radius, not moving.')
        else:
            self.position[0] = r_new
            self.position[1] = psi_new
        return self.position
    
    
class Disk:
    def __init__(self):
        self.DISK_RADIUS = 1
        self.charges = None
        self.N = None

    def PopulateDisk(self, N):
        self.N = N
        self.charges = [None] * self.N

        for i in range(self.N):
            self.charges[i] = Charge(i)
        return self.charges

    def GetTotalEnergy(self):
        E_list = np.empty(N)
        positions = self.GetAllChargePositions()

        for combo, i in zip(combinations(positions, 2), range(N)):
            print(combo)
            pos1 = combo[0]
            pos2 = combo[1]

            d = self.Distance(pos1, pos2)

            E = 1/d
            E_list[i] = E
        return np.sum(E_list)

    def GetTwoChargeDistance(charge1, charge2):
        r1 = charge1.position[0]
        psi1 = charge1.position[1]
        r2 = charge2.position[0]
        psi2 = charge2.position[1]

        d = np.sqrt((r1 * np.cos(psi1) - r2 * np.cos(psi2))**2 +
                    (r1 * np.sin(psi1) - r2 * np.sin(psi2))**2)
        return d


N = 3
disk = Disk()
disk.PopulateDisk(N)