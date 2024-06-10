<!DOCTYPE html>
<html>
<head>
    <title>Horarios Laborales</title>
</head>
<body>
    <h1>Horarios Laborales - <?php echo $_GET['fecha']; ?></h1>
    <table border="1">
        <tr>
            <th>Nombre del Trabajador</th>
            <th>Departamento</th>
            <th>Horario</th>
            <th>Horas Totales</th>
            <th>Horas Extras</th>
        </tr>
        <?php
        // Conexión a la base de datos
        $conn = mysqli_connect("localhost", "usuario", "contraseña", "basededatos");
        if (!$conn) {
            die("Error en la conexión: " . mysqli_connect_error());
        }

        // Consulta para obtener los horarios de la fecha seleccionada
        $fecha = $_GET['fecha'];
        $query = "SELECT * FROM horarios WHERE fecha='$fecha'";
        $result = mysqli_query($conn, $query);
        if (mysqli_num_rows($result) > 0) {
            while ($row = mysqli_fetch_assoc($result)) {
                echo "<tr>";
                echo "<td>" . $row["nombre_trabajador"] . "</td>";
                echo "<td>" . $row["departamento"] . "</td>";
                echo "<td>" . $row["horario"] . "</td>";
                echo "<td>" . $row["horas_totales"] . "</td>";
                echo "<td>" . $row["horas_extras"] . "</td>";
                echo "</tr>";
            }
        } else {
            echo "<tr><td colspan='5'>No se encontraron horarios para esta fecha.</td></tr>";
        }

        mysqli_close($conn);
        ?>
    </table>
</body>
</html>
