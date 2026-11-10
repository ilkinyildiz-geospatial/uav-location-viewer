import tkinter as tk
from tkintermapview import TkinterMapView


pencere = tk.Tk()
pencere.title("İHA Konum Gösterici")

harita = TkinterMapView(pencere, width=700, height=400)
harita.pack(pady=10)

harita.set_position(39.7477,37.0179)
harita.set_zoom(6)


def konum_goster():
    harita.set_position(41.0027, 39.7168,)
    harita.set_zoom(12)
    # Marker ekle
    harita.set_marker(41.0027,39.7168, text="İHA Konumu")
    sonuc_label.config(text="Konum başarıyla gösterildi!")

buton = tk.Button(pencere, text="İHA Konumunu Göster", command=konum_goster)
buton.pack(pady=10)

sonuc_label = tk.Label(pencere, text="Konumu görmek için butona basınız")
sonuc_label.pack()

pencere.mainloop()