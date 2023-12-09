import customtkinter as ctk
from tkinter import messagebox
from dijkstra import dijkstra, draw_graph

def calculate_path():
    start_node = start_entry.get()
    end_node = end_entry.get()

    if start_node not in graph or end_node not in graph:
        messagebox.showerror("Error", "Invalid start or end node.")
        return

    distances, paths = dijkstra(graph, start_node)
    formatted_distance = "{:.2f}".format(distances[end_node])

    result_text.set(
        f"The shortest distance from {start_node} to {end_node} is {formatted_distance}\n"
        f"The shortest path from {start_node} to {end_node} is {paths[end_node]}"
    )

    draw_graph(graph, paths[end_node])


graph = {
     "CGK": {
        "KNO": 31.75,
        "PKU": 23.85,
        "DJB": 18.12,
        "PLM": 15.94,
        "BKS": 17.03,
        "TKG": 11.31,
        "BTH": 22.76,
        "PGK": 14.72,
        "PNK": 20.44,
        "BPN": 28.35,
        "BDJ": 24.94,
        "UPG": 31.75,
        "SUB": 20.44,
        "LOP": 28.35,
        "SOC": 17.03,
        "DJJ": 68.14
    },
    "UPG": {
        "BPN": 15.94,
        "SRG": 23.85,
        "YIA": 27.25,
        "SUB": 21.53,
        "DPS": 19.35,
        "TIM": 38.57,
        "DJJ": 47.7,
        "AMQ": 23.85,
        "BIK": 37.48,
        "MKW": 36.39,
        "SOQ": 28.35,
        "TTE": 26.16,
        "MDC": 26.16,
        "GTO": 19.35,
        "PLW": 15.94,
        "KDI": 12.54,
        "CGK": 31.75 
    },
    "DPS": {
        "UPG": 19.35,
        "YIA": 19.35,
        "SOC": 18.12,
        "SRG": 18.12,
        "SUB": 14.72,
        "BDJ": 15.94,
        "BPN": 24.94,
        "KOE": 22.76
    },
    "KNO": {
        "BTJ": 15.94,
        "BTH": 19.35,
        "YIA": 37.48,
        "CGK": 31.75, 
        "PKU": 23.85 
    },
    "PKU": {
        "BTH": 12.54,
        "YIA": 29.57,
        "KNO": 23.85, 
        "CGK": 23.85 
    },
    "PLM": {
        "CGK": 15.94,
        "BTH": 14.72,
        "PGK": 10.22,
        "SUB": 26.16
    },
    "BTH": {
        "PDG": 17.03,
        "SUB": 30.66,
        "PNK": 17.03,
        "CGK": 22.76, 
        "PKU": 12.54, 
        "PLM": 14.72, 
        "KNO": 19.35  
    },

    "YIA" : {
        "UPG" : 27.25,
        "DPS" : 19.35,
        "KNO" : 37.48,
        "PKU" : 29.57,
        "BDJ" : 19.35,
        "BPN" : 23.85
    },

    "SRG" : {
        "UPG" : 23.85,
        "DPS" : 18.12,
        "BDJ" : 18.12,
        "BPN" : 22.76
    },

    "SUB" : {
        "UPG" : 21.53,
        "CGK" : 20.44,
        "DPS" : 14.72,
        "PLM" : 26.16,
        "BTH" : 30.66,
        "PNK" : 21.53,
        "BDJ" : 15.94,
        "TRK" : 27.25,
        "BPN" : 19.35,
        "MDC" : 38.57,
        "LOP" : 15.94,
        "KOE" : 27.25
    },

    "BPN" : {
        "CGK" : 28.35,
        "UPG" : 15.94,
        "DPS" : 24.94,
        "SRG" : 22.76,
        "YIA" : 23.85,
        "SUB" : 19.35
    },

    "BDJ" : {
        "CGK" : 24.95,
        "DPS" : 15.94,
        "SRG" : 18.12,
        "YIA" : 19.35,
        "SUB" : 15.94
    },

    "DJB" : {
        "CGK" : 18.12

    },
    "BKS" : {
        "CGK" : 17.03

    },
    "TKG" : {
        "CGK" : 11.31
    },

    "PGK" : {
        "CGK" : 14.72,
        "PLM" : 10.22
    },
    
    "PNK" : {
        "CGK" : 20.44,
        "BTH" : 17.03,
        "SUB" : 21.53
    },

    "LOP" : {
        "CGK" : 28.35,
        "SUB" : 15.94
    },

    "SOC" : {
        "CGK" : 17.03,
        "DPS" : 18.12
    },

    "DJJ" : {
        "CGK" : 68.14,
        "UPG" : 47.70,
        "SOQ" : 23.85,
        "MKW" : 19.35,
        "BIK" : 18.12,
        "TIM" : 17.03
    },

    "TIM" : {
        "UPG" : 38.57,
        "DJJ" : 17.03
    },

    "AMQ" : {
        "UPG" : 23.85,
        "LUV" : 15.94
    },

    "BIK" : {
        "UPG" : 37.48,
        "DJJ" : 18.12
    },

    "MKW" : {
        "UPG" : 36.39,
        "SOQ" : 12.54,
        "DJJ" : 19.35
    },

    "SOQ" : {
        "UPG" : 28.35,
        "MDC" : 19.35,
        "DJJ" : 23.85,
        "MKW" : 12.54
    },

    "TTE" : {
        "UPG" : 26.16
    },

    "MDC" : {
        "UPG" : 26.16,
        "SUB" : 38.57,
        "SOQ" : 19.35
    },

    "GTO" : {
        "UPG" : 19.35
    },

    "PLW" : {
        "UPG" : 15.94
    },

    "KDI" : {
        "UPG" : 12.54
    },

    "KOE" : {
        "DPS" : 22.76,
        "SUB" : 27.25
    },

    "BTJ" : {
        "KNO" : 15.94
    },

    "PDG" : {
        "BTH" : 17.03
    },

    "TRK" : {
        "SUB" : 27.25
    },

    "LUV" : {
        "AMQ" : 15.94
    },
}

root = ctk.CTk()
root.geometry("500x400")

title = ctk.CTkLabel(
    root, text="Traveling Dibikin Ga Pusing :D", font=("Helvetica", 30, "bold")
)
title.place(relx=0.5, rely=0.1, anchor="center")

subtitle = ctk.CTkLabel(root, text="Mencari jalur penerbangan paling efisien dengan menggunakan pendekatan algoritma Dijkstra", font=("Helvetica", 16))
subtitle.place(relx=0.5, rely=0.2, anchor='center')

start_label = ctk.CTkLabel(root, text="Start node:")
start_label.place(relx=0.5, rely=0.3, anchor="center")

start_entry = ctk.CTkEntry(root)
start_entry.place(relx=0.5, rely=0.35, anchor="center")

end_label = ctk.CTkLabel(root, text="End node:")
end_label.place(relx=0.5, rely=0.45, anchor="center")

end_entry = ctk.CTkEntry(root)
end_entry.place(relx=0.5, rely=0.5, anchor="center")

calculate_button = ctk.CTkButton(
    root, text="Calculate shortest path", command=calculate_path
)
calculate_button.place(relx=0.5, rely=0.6, anchor="center")

result_text = ctk.StringVar()
result_label = ctk.CTkLabel(root, textvariable=result_text)
result_label.place(relx=0.5, rely=0.7, anchor="center")

root.mainloop()
