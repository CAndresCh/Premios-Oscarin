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

def registrar_voto():
    try:
        titulo = input("Ingrese el título de la película que desea votar: ").strip()
        encontrada = False
        for cat in categorias:
            if titulo in categorias[cat]:
                categorias[cat][titulo] += 1
                print(f"✅ Voto registrado para '{titulo}' en la categoría '{cat}'.")
                encontrada = True
                break
        if not encontrada:
            raise ValueError("Película no encontrada.")
    except ValueError as e:
        print(f"❌ Error: {e}")