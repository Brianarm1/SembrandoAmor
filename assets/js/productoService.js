function agregarAlCarrito(producto){
    const memoria =JSON.parse(localStorage.getItem("semillas"));
    console.log(memoria);
    if(!memoria){
        const nuevoProducto = getNuevoProductoParaMemoria(producto);
        nuevoProducto.cantidad = 1;
        localStorage.setItem("semillas",JSON.stringify([nuevoProducto]));
    }else{
        const indiceProducto = memoria.findIndex(semilla => semilla.id === producto.id);
        console.log(indiceProducto)
        const nuevaMemoria = memoria;

        if(indiceProducto === -1){
            nuevaMemoria.push(getNuevoProductoParaMemoria(producto));

        }else{
            nuevaMemoria[indiceProducto].cantidad ++;
        }
        localStorage.setItem("semillas",JSON.stringify(nuevaMemoria));

    }
    actualizarNumeroCarrito();
}

/*Toma nuevo producto, le agrega cantidad 1 y lo devuelve*/
function getNuevoProductoParaMemoria(producto){
    const nuevoProducto = producto;
    nuevoProducto.cantidad = 1
    return nuevoProducto;
}

const cuentaCarritoElement = document.getElementById("cuenta-carrito");
function actualizarNumeroCarrito(){

    const memoria =JSON.parse(localStorage.getItem("semillas"));
    const cuenta = memoria.reduce((acum, current) => acum+current.cantidad,0);
    cuentaCarritoElement.innerText = cuenta;

}