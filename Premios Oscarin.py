categorias= {}

def registrar_pelicula(): 
    categoria = input("Ingrese la categoría (ej. Mejor Guion): ").strip() 
    titulo = input("Ingrese el título de la película: ").strip() 
    if categoria not in categorias: 
        categorias[categoria] = {} 

    if titulo in categorias[categoria]: 
        print("❌ Error: La película ya fue registrada en esta categoría.") 

    else: 
        categorias[categoria][titulo] = 0 
        print(f"✅ Película '{titulo}' registrada en la categoría '{categoria}'.") 