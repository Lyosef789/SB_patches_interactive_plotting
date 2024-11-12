#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, FloatSlider

def plot_segments(L, B, boundary1, boundary2, boundary3, boundary4, boundary5, boundary6, boundary7, ylabel):
    """
    Plots data in segments based on provided boundaries, with 7 boundaries to create 8 segments.
    
    Parameters:
    - L: array-like, x-axis data (e.g., longitude)
    - B: array-like, y-axis data (e.g., magnetic field or velocity)
    - boundary1 through boundary7: float, boundary values for segmenting
    - ylabel: string, label for the y-axis
    """
    plt.figure(figsize=(10, 6))
    plt.plot(L, B, color='gray', alpha=0.3, label="Full Data")
    
    # Define and plot each segment based on boundaries
    mask1 = (L <= boundary1)
    mask2 = (L > boundary1) & (L <= boundary2)
    mask3 = (L > boundary2) & (L <= boundary3)
    mask4 = (L > boundary3) & (L <= boundary4)
    mask5 = (L > boundary4) & (L <= boundary5)
    mask6 = (L > boundary5) & (L <= boundary6)
    mask7 = (L > boundary6) & (L <= boundary7)
    mask8 = (L > boundary7)
    
    plt.plot(L[mask1], B[mask1], color='blue', label="Segment 1")
    plt.plot(L[mask2], B[mask2], color='green', label="Segment 2")
    plt.plot(L[mask3], B[mask3], color='orange', label="Segment 3")
    plt.plot(L[mask4], B[mask4], color='red', label="Segment 4")
    plt.plot(L[mask5], B[mask5], color='purple', label="Segment 5")
    plt.plot(L[mask6], B[mask6], color='brown', label="Segment 6")
    plt.plot(L[mask7], B[mask7], color='magenta', label="Segment 7")
    plt.plot(L[mask8], B[mask8], color='cyan', label="Segment 8")
    
    plt.xlabel("SS Longitude (degrees)")
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.show()

def generate_set_code(set_num, L, B, L_v, V):
    """
    Generates sliders, constraints, and interactive plots for a specified data set.
    
    Parameters:
    - set_num: integer, identifier for the set (used in labels)
    - L: array-like, longitude data for the magnetic field plot
    - B: array-like, magnetic field data
    - L_v: array-like, longitude data for the velocity plot
    - V: array-like, velocity data
    """
    # Define 7 sliders for each boundary in Set
    sliders = {
        f'boundary1_slider_set{set_num}': FloatSlider(value=40, min=0, max=360, step=1, description='green'),
        f'boundary2_slider_set{set_num}': FloatSlider(value=80, min=0, max=360, step=1, description='orange'),
        f'boundary3_slider_set{set_num}': FloatSlider(value=120, min=0, max=360, step=1, description='red'),
        f'boundary4_slider_set{set_num}': FloatSlider(value=160, min=0, max=360, step=1, description='purple'),
        f'boundary5_slider_set{set_num}': FloatSlider(value=200, min=0, max=360, step=1, description='brown'),
        f'boundary6_slider_set{set_num}': FloatSlider(value=240, min=0, max=360, step=1, description='magenta'),
        f'boundary7_slider_set{set_num}': FloatSlider(value=280, min=0, max=360, step=1, description='cyan'),
    }

    # Extract individual sliders for easier reference in constraints
    boundary1_slider = sliders[f'boundary1_slider_set{set_num}']
    boundary2_slider = sliders[f'boundary2_slider_set{set_num}']
    boundary3_slider = sliders[f'boundary3_slider_set{set_num}']
    boundary4_slider = sliders[f'boundary4_slider_set{set_num}']
    boundary5_slider = sliders[f'boundary5_slider_set{set_num}']
    boundary6_slider = sliders[f'boundary6_slider_set{set_num}']
    boundary7_slider = sliders[f'boundary7_slider_set{set_num}']
    
    # Constraint function to keep sliders in ascending order
    def update_constraints(*args):
        if boundary2_slider.value > boundary1_slider.value:
            boundary2_slider.min = boundary1_slider.value + 1
        if boundary3_slider.value > boundary2_slider.value:
            boundary3_slider.min = boundary2_slider.value + 1
        if boundary4_slider.value > boundary3_slider.value:
            boundary4_slider.min = boundary3_slider.value + 1
        if boundary5_slider.value > boundary4_slider.value:
            boundary5_slider.min = boundary4_slider.value + 1
        if boundary6_slider.value > boundary5_slider.value:
            boundary6_slider.min = boundary5_slider.value + 1
        if boundary7_slider.value > boundary6_slider.value:
            boundary7_slider.min = boundary6_slider.value + 1

    # Attach observers to enforce slider constraints
    for slider in sliders.values():
        slider.observe(update_constraints, 'value')

    # Interactive plot for magnetic field data (B vs L) with sliders, labeled as "Br*R^2"
    interact(lambda boundary1, boundary2, boundary3, boundary4, boundary5, boundary6, boundary7:
             plot_segments(L, B, boundary1, boundary2, boundary3, boundary4, boundary5, boundary6, boundary7, ylabel="Br*R^2"),
             boundary1=boundary1_slider, boundary2=boundary2_slider, boundary3=boundary3_slider,
             boundary4=boundary4_slider, boundary5=boundary5_slider, boundary6=boundary6_slider, boundary7=boundary7_slider)

    # Interactive plot for velocity data (V vs L_v) with sliders, labeled as "V [km/s]"
    interact(lambda boundary1, boundary2, boundary3, boundary4, boundary5, boundary6, boundary7:
             plot_segments(L_v, V, boundary1, boundary2, boundary3, boundary4, boundary5, boundary6, boundary7, ylabel="Vp [km/s]"),
             boundary1=boundary1_slider, boundary2=boundary2_slider, boundary3=boundary3_slider,
             boundary4=boundary4_slider, boundary5=boundary5_slider, boundary6=boundary6_slider, boundary7=boundary7_slider)

