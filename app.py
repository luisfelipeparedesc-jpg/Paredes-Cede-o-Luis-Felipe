<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Calculadora de Tabla de Verdad</title>
<style>
body {
    font-family: Arial;
    text-align: center;
    background: #f4f4f4;
}
.container {
    margin-top: 50px;
}
input {
    width: 300px;
    padding: 10px;
    font-size: 16px;
}
button {
    padding: 10px 20px;
    margin: 10px;
    font-size: 16px;
}
table {
    margin: 20px auto;
    border-collapse: collapse;
}
td, th {
    border: 1px solid black;
    padding: 8px;
}
</style>
</head>

<body>

<div class="container">
    <h2>Calculadora de Tabla de Verdad</h2>
    
    <input type="text" id="expresion" placeholder="Ej: p && q || !p">
    <br>
    <button onclick="generarTabla()">Calcular</button>

    <div id="resultado"></div>
</div>

<script>
function generarTabla() {
    let expr = document.getElementById("expresion").value;

    let variables = Array.from(new Set(expr.match(/[pqrst]/g)));

    if (!variables) {
        alert("Ingresa una expresión válida");
        return;
    }

    let filas = Math.pow(2, variables.length);
    let tabla = "<table><tr>";

    // Encabezado
    variables.forEach(v => tabla += `<th>${v}</th>`);
    tabla += "<th>Resultado</th></tr>";

    for (let i = 0; i < filas; i++) {
        let valores = {};
        tabla += "<tr>";

        variables.forEach((v, j) => {
            let valor = (i >> (variables.length - j - 1)) & 1;
            valores[v] = valor ? true : false;
            tabla += `<td>${valor ? "V" : "F"}</td>`;
        });

        try {
            let resultado = eval(expr.replace(/[pqrst]/g, m => valores[m]));
            tabla += `<td>${resultado ? "V" : "F"}</td>`;
        } catch {
            tabla += "<td>Error</td>";
        }

        tabla += "</tr>";
    }

    tabla += "</table>";
    document.getElementById("resultado").innerHTML = tabla;
}
</script>

</body>
</html>