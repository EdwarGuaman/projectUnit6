const ENDPOINT ="http://localhost:3000"

function mostrarPerfiles() {

   
   let url= ENDPOINT+'/users/profileslistapi/' 
    // URL a Consumir
   fetch(url)                   // Fetch maneja Promise
       .then(Response => Response.json()) // se resuelve la promesa y al obtener la respuesta la pasa a un determinado formato JSON
       .then(data => Mostrardata(data))  // leemos el objeto data y lo mostramos por consola 
       .catch(error => console.log(error) ) // me captura el error en la palabra catch 
 

    
    const Mostrardata = (data) => {

     console.log(data)

        

        let Campostabla = "<th scope='col'>ID</th>" +"<th scope='col'>NAME</th>" +"<th scope='col'>DOCUMENT</th>" +"<th scope='col'>ADDRESS</th>"
        let body =""
        

      for( let indice in data){

        //console.log(data[indice]);
        let id = data[indice].User.id
        let name = data[indice].User.first_name
        let documento = data[indice].documento
        let direccion = data[indice].direccion

        body +=  '<tr> <td>' + id + '</td> <td>' + name + '</td> <td>' + documento+  '</td> <td>' +direccion+  '</td></tr>'   
         

      }
      
      document.getElementById('primercampo').innerHTML = Campostabla
      document.getElementById('mytable').innerHTML = body 
      

    }


}

/* Funcion a llamar los productos*/ 

function mostrarProductos() {

   
  let url= ENDPOINT+'/productos/productlistapi/'   // URL a Consumir

  fetch(url)                   // Fetch maneja Promise
      .then(Response => Response.json()) // se resuelve la promesa y al obtener la respuesta la pasa a un determinado formato JSON
      .then(data => Mostrardata(data))  // leemos el objeto data y lo mostramos por consola 
      .catch(error => console.log(error) ) // me captura el error en la palabra catch 


   
   const Mostrardata = (data) => {

    console.log(data)

       let Campostabla = "<th scope='col'>ID</th>" +"<th scope='col'>PRODUCTO</th>" +"<th scope='col'>CATEGORIA</th>" +"<th scope='col'>PRECIO</th>"
       let body =""
       

     for( let indice in data){
 
       console.log(data[indice]);
       let id = data[indice].descripcion
       let producto = data[indice].nombre
       let categoria = data[indice].idCategoria.nombre
       let precio = data[indice].precio

       body +=  '<tr> <td>' + id + '</td> <td>' + producto + '</td> <td>' + categoria+  '</td> <td>' +precio+  '</td></tr>'   
       

     }

       document.getElementById('primercampo').innerHTML = Campostabla
       document.getElementById('mytable').innerHTML = body 

   }


}

/* Funcion a llamar los Detalles de Consultas*/ 

function mostrarDetalles() {

   
  let url= ENDPOINT+'/compras/DetalleConsultalistapi/'   // URL a Consumir

  fetch(url)                   // Fetch maneja Promise
      .then(Response => Response.json()) // se resuelve la promesa y al obtener la respuesta la pasa a un determinado formato JSON
      .then(data => Mostrardata(data))  // leemos el objeto data y lo mostramos por consola 
      .catch(error => console.log(error) ) // me captura el error en la palabra catch 


   
   const Mostrardata = (data) => {

    console.log(data)

       let Campostabla = "<th scope='col'>Consulta</th>" +"<th scope='col'>User</th>" +"<th scope='col'>Descripcion</th>"
       let body =""
       

     for( let indice in data){
 
       console.log(data[indice]);
       let Consulta = data[indice].idConsulta.id
       let Usuario = data[indice].idUsuario.last_name
       let Descripcion = data[indice].descripcion

       body +=  '<tr> <td>' + Consulta + '</td> <td>' + Usuario + '</td> <td>' + Descripcion+  '</td> </tr>' 
       

     }

       document.getElementById('primercampo').innerHTML = Campostabla
       document.getElementById('mytable').innerHTML = body 

   }


}