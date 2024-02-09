# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 19:08:20 2024

@author: cleme
"""
import numpy as np

class Etudiant:
    def __init__(self, Nom, Prénom, Notes_reçues_aux_exam):
        self.Nom=Nom
        self.Prénom=Prénom
        self.Notes_reçues_aux_exam=Notes_reçues_aux_exam
        
    def imprimer(self):
        if len(self.Notes_reçues_aux_exam)==0:
            print("Pas de notes pour l'étudiant" + self.Nom)
        else:
            print(np.mean(self.Notes_reçues_aux_exam))
        
lenny=Etudiant('Oui','Non',[])

lenny.imprimer()