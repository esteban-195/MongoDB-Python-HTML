-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: localhost    Database: biblioteca02
-- ------------------------------------------------------
-- Server version	9.2.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `autores`
--

DROP TABLE IF EXISTS `autores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `autores` (
  `autor_id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) DEFAULT NULL,
  `nacionalidad` varchar(100) DEFAULT NULL,
  `f_de_nac` smallint DEFAULT NULL,
  PRIMARY KEY (`autor_id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `autores`
--

LOCK TABLES `autores` WRITE;
/*!40000 ALTER TABLE `autores` DISABLE KEYS */;
INSERT INTO `autores` VALUES (1,'Stephen King','Estadounidense',1947),(2,'Miguel de Cervantes','Español',1547),(3,'Gabriel García Márquez','',NULL),(4,'Jane Austen','Británica',1775),(5,'Dan Brown','',1964),(6,'Suzanne Collins','Estadounidense',1962),(7,'George Orwell','Británico',1903),(8,'Bram Stoker','Irlandés',1847);
/*!40000 ALTER TABLE `autores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `copias`
--

DROP TABLE IF EXISTS `copias`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `copias` (
  `copia_id` int NOT NULL AUTO_INCREMENT,
  `libro_id` int DEFAULT NULL,
  `estado` varchar(20) DEFAULT NULL,
  `ubicacion` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`copia_id`),
  KEY `copias_ibfk_1` (`libro_id`),
  CONSTRAINT `copias_ibfk_1` FOREIGN KEY (`libro_id`) REFERENCES `libros` (`libro_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `copias`
--

LOCK TABLES `copias` WRITE;
/*!40000 ALTER TABLE `copias` DISABLE KEYS */;
/*!40000 ALTER TABLE `copias` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `historial_prestamo`
--

DROP TABLE IF EXISTS `historial_prestamo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `historial_prestamo` (
  `hist_id` int NOT NULL AUTO_INCREMENT,
  `usuario_id` int NOT NULL,
  `libro_id` int NOT NULL,
  `copia_id` int NOT NULL,
  `fecha_prestamo` date NOT NULL,
  `fecha_devolución` date DEFAULT NULL,
  PRIMARY KEY (`hist_id`),
  KEY `usuario_id` (`usuario_id`),
  KEY `libro_id` (`libro_id`),
  KEY `copia_id` (`copia_id`),
  CONSTRAINT `historial_prestamo_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`usuario_id`),
  CONSTRAINT `historial_prestamo_ibfk_2` FOREIGN KEY (`libro_id`) REFERENCES `libros` (`libro_id`),
  CONSTRAINT `historial_prestamo_ibfk_3` FOREIGN KEY (`copia_id`) REFERENCES `copias` (`copia_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `historial_prestamo`
--

LOCK TABLES `historial_prestamo` WRITE;
/*!40000 ALTER TABLE `historial_prestamo` DISABLE KEYS */;
/*!40000 ALTER TABLE `historial_prestamo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `libros`
--

DROP TABLE IF EXISTS `libros`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `libros` (
  `libro_id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(500) NOT NULL,
  `autor` varchar(100) NOT NULL,
  `isbn` varchar(100) NOT NULL,
  `copias` int DEFAULT NULL,
  `copias_disp` int DEFAULT NULL,
  PRIMARY KEY (`libro_id`),
  UNIQUE KEY `isbn` (`isbn`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `libros`
--

LOCK TABLES `libros` WRITE;
/*!40000 ALTER TABLE `libros` DISABLE KEYS */;
INSERT INTO `libros` VALUES (1,'Cien años de soledad','Gabriel García Marquez','654-4562-7895-45',5,5),(3,'El resplandor','Stephen King','978-0307743657',4,4),(4,'Cementerio de animales','Stephen King','978-1501156700',2,2),(5,'Los juegos del hambre','Suzanne Collins','978-0439023481',4,4),(6,'1984','George Orwell','978-0451524935',2,2),(7,'Don Quijote de la Mancha','Miguel de Cervantes','978-0060934347',6,6),(8,'Crónica de una muerte anunciada','Gabriel García Márquez','978-0307387134',2,2),(9,'Orgullo y prejuicio','Jane Austen','978-1503290563',2,2),(10,'El código Da Vinci','Dan Brown','978-0307474278',2,2),(11,'Drácula','Bram Stoker','978-0486411095',2,2),(12,'It (Eso)','Stephen King','978-1501142970',2,2),(13,'Ángeles y demonio','Dan Brown','978-0307474279',1,1);
/*!40000 ALTER TABLE `libros` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `libros_autores`
--

DROP TABLE IF EXISTS `libros_autores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `libros_autores` (
  `libro_id` int NOT NULL,
  `autor_id` int NOT NULL,
  PRIMARY KEY (`libro_id`,`autor_id`),
  KEY `llave_foranea_autores` (`autor_id`),
  CONSTRAINT `libros_autores_ibfk_1` FOREIGN KEY (`libro_id`) REFERENCES `libros` (`libro_id`),
  CONSTRAINT `llave_foranea_autores` FOREIGN KEY (`autor_id`) REFERENCES `autores` (`autor_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `libros_autores`
--

LOCK TABLES `libros_autores` WRITE;
/*!40000 ALTER TABLE `libros_autores` DISABLE KEYS */;
INSERT INTO `libros_autores` VALUES (3,1),(4,1),(12,1),(7,2),(1,3),(8,3),(9,4),(10,5),(13,5),(5,6),(6,7),(11,8);
/*!40000 ALTER TABLE `libros_autores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reservas`
--

DROP TABLE IF EXISTS `reservas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reservas` (
  `reserva_id` int NOT NULL AUTO_INCREMENT,
  `libro_id` int DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `expira` date DEFAULT NULL,
  PRIMARY KEY (`reserva_id`),
  KEY `reservas_ibfk_1` (`libro_id`),
  CONSTRAINT `reservas_ibfk_1` FOREIGN KEY (`libro_id`) REFERENCES `libros` (`libro_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reservas`
--

LOCK TABLES `reservas` WRITE;
/*!40000 ALTER TABLE `reservas` DISABLE KEYS */;
/*!40000 ALTER TABLE `reservas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `usuario_id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(500) NOT NULL,
  `email` varchar(100) NOT NULL,
  `telefono` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`usuario_id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,'Momo','momo@gmail.com','4566548521'),(2,'Guaza','guaza@gmail.com','451239523'),(3,'Momo','momo2@gmail.com','');
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-03-30 20:40:07
