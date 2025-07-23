SELECT * from paciente;
SELECT Nombre, Apellido FROM pacientes;
SELECT * from  doctores;
SELECT * FROM Pacientes WHERE Nombre = "ANA"; 
SELECT * FROM Pacientes WHERE Apellido LIKE "L%";
SELECT * FROM doctores WHERE Nombre LIKE "Dr.%";
SELECT * FROM Pacientes WHERE Apellido LIKE"5 LETRAS";
SELECT * FROM Pacientes ORDER BY Apellido ASC;
SELECT * FROM consultas ORDER BY Fecha DESC;
SELECT * FROM doctores ORDER BY especialidad ASC;
SELECT MIN 