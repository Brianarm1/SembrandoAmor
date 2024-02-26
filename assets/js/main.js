function toggleForms() {
    var registerForm = document.getElementById('registerForm');
    var loginForm = document.getElementById('loginForm');
    if (registerForm.style.display === 'none') {
        registerForm.style.display = 'block';
        loginForm.style.display = 'none';
    } else {
        registerForm.style.display = 'none';
        loginForm.style.display = 'block';
    }
}


const contenedorTarjetas = document.getElementById('productos-container');


function crearTarjetaProductos(productos){
    productos.forEach(producto => {
        const nuevaSemilla = document.createElement("div");
        nuevaSemilla.classList="tarjeta-producto";
        nuevaSemilla.innerHTML=`

        <img src={{url_for('static',filename='img/imgproduto/semilla-ceiba bonga.jpg')}}/${producto.id}>
        <h3>${producto.nombre}</h3>
        <p>${producto.texto}</p>
        <p class="price">${producto.precio}</p>
        <p class="value">${producto.valor}</p>
        <button class="comprar">Agregar al carrito </button>
        `
        contenedorTarjetas.appendChild(nuevaSemilla);
        nuevaSemilla.getElementsByTagName("button")[0].addEventListener("click",()=> agregarAlCarrito(producto))
    });

}

crearTarjetaProductos(semillas);






