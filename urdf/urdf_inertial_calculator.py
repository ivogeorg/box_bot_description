#! /usr/bin/python3

# After https://get-help.theconstruct.ai/t/inertia-calculator/7295

import math

class InertialCalculator(object):

    def __init__(self):
          print ("URDF Inertial Calculator Initialised...")

    def start_ask_loop(self):

        selection = "START"

        while selection.upper() != "Q":     # accept 'q' as well
            print ("#############################")
            print ("Select Geometry to Calculate:")
            print ("[1]Box width(x-axis)*depth(y-axis)*height(z-axis)")
            print ("[2]Sphere radius(r)")
            print ("[3]Cylinder radius(r)*height(h)")
            print ("[Q]END program")
            selection = input(">>")
            self.select_action(selection)

        print ("URDF Inertial Calculator Quit...Thank you")

    def select_action(self, selection):
        if selection == "1":
            mass = float(input("mass>>"))
            width = float(input("x-axis length>>"))
            depth = float(input("y-axis length>>"))
            height = float(input("z-axis length>>"))
            self.calculate_box_inertia(m=mass, w=width, d=depth, h=height)
        elif selection == "2":
            mass = float(input("mass>>"))
            radius = float(input("radius>>"))
            self.calculate_sphere_inertia(m=mass, r=radius)
        elif selection == "3":
            mass = float(input("mass>>"))
            radius = float(input("radius>>"))
            height = float(input("height>>"))
            self.calculate_cylinder_inertia(m=mass, r=radius, h=height)
        elif selection.upper() == "Q": # accept 'q' as well
            print ("Selected Quit")
        else:
            print ("Usage: Select one of the give options")


    def calculate_box_inertia(self, m, w, d, h):
        Iw = (m/12.0)*(pow(d,2)+pow(h,2))
        Id = (m / 12.0) * (pow(w, 2) + pow(h, 2))
        Ih = (m / 12.0) * (pow(w, 2) + pow(d, 2))
        print ('BOX ixx="' + str(Iw) + '" ixy="0.0" ixz="0.0" iyy="' 
                + str(Id) + '" iyz="0.0" izz="' + str(Ih) + '"')

    def calculate_sphere_inertia(self, m, r):
        I = (2*m*pow(r,2))/5.0
        print ('SPHERE ixx="' + str(I) + '" ixy="0.0" ixz="0.0" iyy="' 
                + str(I) + '" iyz="0.0" izz="' + str(I) + '"')

    def calculate_cylinder_inertia(self, m, r, h):
        Ix = (m/12.0)*(3*pow(r,2)+pow(h,2))
        Iy = Ix
        Iz = (m*pow(r,2))/2.0
        print ('Cylinder ixx="' + str(Ix) + '" ixy="0.0" ixz="0.0" iyy="' 
                + str(Iy) + '" iyz="0.0" izz="' + str(Iz) + '"')

if __name__ == "__main__":
    inertial_object = InertialCalculator()
    inertial_object.start_ask_loop()
