#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# interactive_plotter.py

import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, FloatSlider

def plot_segments(L, B, boundary1, boundary2, boundary3, boundary4, boundary5):
    """
    Helper function that plots data in six segments based on given boundaries.

    Parameters:
    - L: array-like, longitudes or x-axis values
    - B: array-like, data values to plot on the y-axis
    - boundary1 to boundary5: float, boundary values that define the segments
    """
    plt.figure(figsize=(10, 6))
    plt.plot(L, B, color='gray', alpha=0.3, label="Full Data")
    
    # Define segments
    mask1 = (L <= boundary1)
    mask2 = (L > boundary1) & (L <= boundary2)
    mask3 = (L > boundary2) & (L <= boundary3)
    mask4 = (L > boundary3) & (L <= boundary4)
    mask5 = (L > boundary4) & (L <= boundary5)
    mask6 = (L > boundary5)
    
    plt.plot(L[mask1], B[mask1], color='blue', label="Segment 1")
    plt.plot(L[mask2], B[mask2], color='green', label="Segment 2")
    plt.plot(L[mask3], B[mask3], color='orange', label="Segment 3")
    plt.plot(L[mask4], B[mask4], color='red', label="Segment 4")
    plt.plot(L[mask5], B[mask5], color='purple', label="Segment 5")
    plt.plot(L[mask6], B[mask6], color='brown', label="Segment 6")
    
    plt.xlabel("Longitude (degrees)")
    plt.ylabel("Data Value")
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_segments_interactive(L, B):
    """
    Interactive plotting function for segmenting data based on boundaries.
    
    Parameters:
    - L: array-like, longitudes or x-axis values
    - B: array-like, data values to plot on the y-axis
    """
    # Initialize sliders for defining boundaries
    boundary1_slider = FloatSlider(value=60, min=0, max=360, step=1, description='Boundary 1')
    boundary2_slider = FloatSlider(value=120, min=0, max=360, step=1, description='Boundary 2')
    boundary3_slider = FloatSlider(value=180, min=0, max=360, step=1, description='Boundary 3')
    boundary4_slider = FloatSlider(value=240, min=0, max=360, step=1, description='Boundary 4')
    boundary5_slider = FloatSlider(value=300, min=0, max=360, step=1, description='Boundary 5')
    
    # Function to keep sliders ordered correctly
    def update_constraints(*args):
        boundary2_slider.min = boundary1_slider.value + 1
        boundary3_slider.min = boundary2_slider.value + 1
        boundary4_slider.min = boundary3_slider.value + 1
        boundary5_slider.min = boundary4_slider.value + 1

    # Observe changes in boundary sliders to enforce order
    boundary1_slider.observe(update_constraints, 'value')
    boundary2_slider.observe(update_constraints, 'value')
    boundary3_slider.observe(update_constraints, 'value')
    boundary4_slider.observe(update_constraints, 'value')

    # Create interactive plot
    interact(lambda boundary1, boundary2, boundary3, boundary4, boundary5: 
             plot_segments(L, B, boundary1, boundary2, boundary3, boundary4, boundary5),
             boundary1=boundary1_slider, boundary2=boundary2_slider,
             boundary3=boundary3_slider, boundary4=boundary4_slider, boundary5=boundary5_slider)

