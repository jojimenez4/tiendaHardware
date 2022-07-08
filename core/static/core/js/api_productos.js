$(document).ready(function(){  
    $.get("http://127.0.0.1:8000/api/listar_productos", 
        function(data){
            $.each(data, function(i, item){
                $("#productos").append("<tr><td>"+item.nombre+"</td><td>"+item.categoria+
                    "</td><td><img src='"+item.foto+"'>"+
                    "</td><td>"+item.precio+"</td></tr>");
        });
    });
}); 