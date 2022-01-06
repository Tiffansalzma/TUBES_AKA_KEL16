import random
import math
from types import DynamicClassAttribute
import pygame
import argparse
import os
import sys
import itertools

# TUGAS BESAR ANALISIS KOMPLEKSITAS DATA 
# KELAS IF-44-09
# KELOMPOK 16
# Fahri Sunarya (1301204196)
# Fachrul Febriana (1301204407)

# Arguments parsing
parser = argparse.ArgumentParser(description="Sorting algorithms visualization by Broksy")
parser.add_argument("--output", action="store_true")
args = parser.parse_args()

# White RGB constant (digunakan untuk teks)
WHITE = (255,255,255)

# QUICKSORT O(n*log(n))
def quicksort(a, l=0, r=None):
    if r is None:
        r = len(a)-1
    if l < r:
        p = partition(a,l,r)
        quicksort(a, l, p-1)
        quicksort(a, p+1, r)

# function pembantu untuk quicksort
def partition(a, l, r):
    draw_array(a, (23,145,64), "Quicksort : O(n*log(n))", "percobaan ")
    i = l-1
    pivot = a[r]
    for j in range(l,r):
        if a[j] < pivot:
            i += 1
            a[j], a[i] = a[i], a[j]
    a[i+1], a[r] = a[r], a[i+1]
    draw_array(a, (23,145,64), "Quicksort : O(n*log(n))", "percobaan ")
    return i+1
 # COCKTAIL SORT O(n^2)
def cocktail_sort(a):
    swap = True
    while swap:
        swap = False
        for i in range(len(a)-1):
            if a[i+1]<a[i]:
                swap = True
                a[i+1], a[i] = a[i], a[i+1]
        draw_array(a, (135,12,64), "Cocktail sort : O(n²)", "percobaan ")
        if not swap:
            break
        for i in range(len(a)-1, 1, -1):
            if a[i]<a[i-1]:
                swap = True
                a[i], a[i-1] = a[i-1], a[i]
        draw_array(a, (135,12,64), "Cocktail sort : O(n²)", "percobaan ")
 # Function to represent array as bars
def draw_array(arr, base_color, title, time):
    global frame_number

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    n = len(arr)

    # Texts to be displayed
    title_text = font.render(title, True, WHITE)
    time_text = small_font.render(str(time)+"10 000 numbers", True, WHITE)

    # Clear screen
    window.fill((0,0,0))

    # Draw array as bars
    for i in range(n):
        rect = pygame.Rect(round(i/n*1920), 1080-round(arr[i]/n*1080), round(1920/n), round(arr[i]/n*1080))
        color_change = round(arr[i]/n*100)
        color = tuple(channel+color_change for channel in base_color)
        pygame.draw.rect(window, color, rect)
    
    # Add text and update
    if title:
        window.blit(title_text, (20,20))
    if time:
        window.blit(time_text, (20, 80))
    pygame.display.update()

    # Save frame if required
    if args.output:
        pygame.image.save(window, f"./out/frame_{frame_number}.jpg")
        frame_number+=1


# Preparation for image sequence output
if args.output:    
 # Check if output directory exists, and create it if it doesn't
    if not os.path.exists("./out"):
        os.mkdir("./out")
    frame_number=0

# Pygame initialization
pygame.init()
pygame.font.init()
font = pygame.font.SysFont("Times New Roman", 48, italic=True)
small_font = pygame.font.SysFont("Times New Roman", 32, italic=True)
window = pygame.display.set_mode((0,0), pygame.RESIZABLE)
pygame.display.set_caption("Broksy's sorting algorithms visualization")
clock = pygame.time.Clock()

# Array initialization (960 elements = every element is 2px wide)
nums = [i for i in range(1,961)]

# Animation start

random.shuffle(nums)
quicksort(nums)

random.shuffle(nums)
cocktail_sort(nums)
