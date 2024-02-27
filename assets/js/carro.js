const contenedorTarjetas1 = document.getElementById('productos-container');


function crearTarjetaProductos(){
    const productos = JSON.parse(localStorage.getItem("semillas"));
    console.log(productos);

    if(productos && productos.length > 0){

        productos.forEach(producto => {
            const nuevaSemilla = document.createElement("div");
            nuevaSemilla.classList="tarjeta-producto";
            nuevaSemilla.innerHTML=`
    
            <img src={{url_for('static',filename='img/carrito/carro-de-la-carretilla')}}${producto.id}>
            <h3>${producto.nombre}</h3>
            <p>${producto.texto}</p>
            <p class="price">${producto.precio}</p>
            <p class="value">${producto.valor}</p>
            <div> 

            <button class="">-</button>
            <span class="cantidad">0</span>
            <button class="">+</button>
            
            </div>

            `
            contenedorTarjetas1.appendChild(nuevaSemilla);
            nuevaSemilla.getElementsByTagName("button")[0].addEventListener("click",()=> agregarAlCarrito(producto))
        });
    
    }

    }


crearTarjetaProductos(semillas);