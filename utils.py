# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.6
#   kernelspec:
#     display_name: edsb26-g3 (3.13.7)
#     language: python
#     name: python3
# ---

# %%
import os

def print_centered_header(text):
    try:
        terminal_width = os.get_terminal_size().columns
    except OSError:
        terminal_width = 80
        
    # Format the text with padding spaces
    formatted_text = f" {text} "
    
    print(formatted_text.center(terminal_width, "-"))


# %%
print_centered_header("Keni")
