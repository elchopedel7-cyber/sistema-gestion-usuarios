CREATE DATABASE  IF NOT EXISTS `gestion_usuarios_db` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `gestion_usuarios_db`;
-- MySQL dump 10.13  Distrib 8.0.46, for Win64 (x86_64)
--
-- Host: localhost    Database: gestion_usuarios_db
-- ------------------------------------------------------
-- Server version	8.0.46

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
-- Table structure for table `auditoria`
--

DROP TABLE IF EXISTS `auditoria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auditoria` (
  `id_auditoria` int NOT NULL AUTO_INCREMENT,
  `id_usuario` int DEFAULT NULL,
  `accion` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `fecha` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `ip` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id_auditoria`),
  KEY `id_usuario` (`id_usuario`),
  CONSTRAINT `auditoria_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auditoria`
--

LOCK TABLES `auditoria` WRITE;
/*!40000 ALTER TABLE `auditoria` DISABLE KEYS */;
INSERT INTO `auditoria` VALUES (1,2,'Registro de usuario: juan@test.com','2026-10-01 22:28:47','127.0.0.1'),(2,2,'Inicio de sesión: juan@test.com','2026-10-01 22:32:54','127.0.0.1'),(3,2,'Inicio de sesión: juan@test.com','2026-10-01 22:52:09','127.0.0.1'),(4,2,'Editó al usuario ID 2','2026-10-01 22:59:23','127.0.0.1'),(5,2,'Inicio de sesión: juan@test.com','2026-10-01 23:08:38','127.0.0.1'),(6,3,'Registro de usuario: maria@test.com','2026-10-01 23:11:38','127.0.0.1'),(7,2,'Eliminó lógicamente al usuario ID 3','2026-10-01 23:12:54','127.0.0.1'),(8,2,'Reactivó al usuario ID 3','2026-10-01 23:17:57','127.0.0.1'),(9,2,'Eliminó lógicamente al usuario ID 3','2026-10-01 23:18:04','127.0.0.1'),(10,2,'Reactivó al usuario ID 3','2026-10-01 23:18:14','127.0.0.1'),(11,2,'Eliminó lógicamente al usuario ID 3','2026-10-01 23:18:18','127.0.0.1'),(12,2,'Reactivó al usuario ID 3','2026-10-01 23:18:24','127.0.0.1'),(13,2,'Eliminó lógicamente al usuario ID 3','2026-10-01 23:19:09','127.0.0.1'),(14,2,'Reactivó al usuario ID 3','2026-10-01 23:19:11','127.0.0.1'),(15,2,'Asignó rol \'Editor\' al usuario ID 2','2026-10-01 23:47:27','127.0.0.1'),(16,2,'Editó al usuario ID 2','2026-10-01 23:47:58','127.0.0.1'),(17,2,'Inicio de sesión: juan@test.com','2026-10-01 23:54:49','127.0.0.1'),(18,2,'Asignó rol \'Editor\' al usuario ID 2','2026-10-01 23:55:04','127.0.0.1'),(19,2,'Creó el rol: Supervisor','2026-10-01 23:55:18','127.0.0.1'),(20,2,'Inicio de sesión: juan@test.com','2026-10-02 00:10:18','127.0.0.1'),(21,2,'Inicio de sesión: juan@test.com','2026-10-02 20:23:51','127.0.0.1'),(22,2,'Inicio de sesión: juan@test.com','2026-10-02 20:32:49','127.0.0.1'),(23,4,'Registro de usuario: conexion@test.com','2026-10-04 00:32:01','127.0.0.1'),(26,1,'Inicio de sesión: nuevo_admin@sgu.com','2026-10-04 01:49:13','127.0.0.1'),(28,1,'Editó al usuario ID 3','2026-10-04 02:13:04','127.0.0.1'),(29,1,'Asignó rol \'Lector\' al usuario ID 3','2026-10-04 02:13:04','127.0.0.1'),(30,1,'Eliminó lógicamente al usuario ID 4','2026-10-04 02:13:12','127.0.0.1'),(31,1,'Reactivó al usuario ID 4','2026-10-04 02:13:17','127.0.0.1'),(32,1,'Eliminó lógicamente al usuario ID 4','2026-10-04 02:13:21','127.0.0.1'),(33,1,'Reactivó al usuario ID 4','2026-10-04 02:13:38','127.0.0.1'),(34,1,'Eliminó lógicamente al usuario ID 3','2026-10-04 02:20:48','127.0.0.1'),(35,1,'Reactivó al usuario ID 3','2026-10-04 02:21:00','127.0.0.1'),(36,1,'Eliminó lógicamente al usuario ID 4','2026-10-04 02:21:25','127.0.0.1'),(37,1,'Reactivó al usuario ID 4','2026-10-04 02:21:48','127.0.0.1'),(38,2,'Inicio de sesión: juan@test.com','2026-10-17 22:28:21','127.0.0.1'),(39,2,'Editó al usuario ID 2','2026-10-17 22:42:11','127.0.0.1'),(40,2,'Eliminó lógicamente al usuario ID 3','2026-10-17 22:53:30','127.0.0.1'),(41,2,'Reactivó al usuario ID 3','2026-10-17 22:55:03','127.0.0.1'),(42,2,'Eliminó lógicamente al usuario ID 3','2026-10-17 23:05:59','127.0.0.1'),(43,2,'Inicio de sesión: juan@test.com','2026-10-18 00:13:08','127.0.0.1'),(44,2,'Editó al usuario ID 2','2026-10-18 00:18:45','127.0.0.1'),(45,2,'Reactivó al usuario ID 3','2026-10-18 00:23:49','127.0.0.1'),(46,2,'Eliminó lógicamente al usuario ID 3','2026-10-18 00:23:59','127.0.0.1'),(47,2,'Reactivó al usuario ID 3','2026-10-18 00:25:59','127.0.0.1'),(48,2,'Inicio de sesión: juan@test.com','2026-10-18 00:40:33','127.0.0.1'),(49,2,'Inicio de sesión: juan@test.com','2026-10-18 03:02:18','127.0.0.1'),(50,2,'Inicio de sesión: juan@test.com','2026-10-18 03:19:00','127.0.0.1'),(51,2,'Editó al usuario ID 2','2026-10-18 03:23:41','127.0.0.1'),(52,2,'Eliminó lógicamente al usuario ID 3','2026-10-18 03:24:47','127.0.0.1'),(53,2,'Reactivó al usuario ID 3','2026-10-18 03:26:23','127.0.0.1'),(54,1,'Inicio de sesión: nuevo_admin@sgu.com','2026-10-31 00:35:01','127.0.0.1');
/*!40000 ALTER TABLE `auditoria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `permiso`
--

DROP TABLE IF EXISTS `permiso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `permiso` (
  `id_permiso` int NOT NULL AUTO_INCREMENT,
  `nombre_permiso` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `descripcion` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id_permiso`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `permiso`
--

LOCK TABLES `permiso` WRITE;
/*!40000 ALTER TABLE `permiso` DISABLE KEYS */;
INSERT INTO `permiso` VALUES (1,'ver_usuarios','Ver listado de usuarios'),(2,'crear_usuarios','Registrar nuevos usuarios'),(3,'editar_usuarios','Modificar datos de usuarios'),(4,'eliminar_usuarios','Desactivar usuarios'),(5,'gestionar_roles','Asignar roles y permisos'),(6,'ver_auditoria','Consultar registro de actividades'),(7,'configuracion','Acceder a la configuración');
/*!40000 ALTER TABLE `permiso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rol`
--

DROP TABLE IF EXISTS `rol`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rol` (
  `id_rol` int NOT NULL AUTO_INCREMENT,
  `nombre_rol` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `descripcion` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id_rol`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rol`
--

LOCK TABLES `rol` WRITE;
/*!40000 ALTER TABLE `rol` DISABLE KEYS */;
INSERT INTO `rol` VALUES (1,'Administrador','Control total del sistema'),(2,'Editor','Puede editar usuarios pero no eliminarlos'),(3,'Lector','Solo puede visualizar información'),(4,'Supervisor','Supervisa usuarios sin editarlos');
/*!40000 ALTER TABLE `rol` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rol_permiso`
--

DROP TABLE IF EXISTS `rol_permiso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rol_permiso` (
  `id_rol` int NOT NULL,
  `id_permiso` int NOT NULL,
  PRIMARY KEY (`id_rol`,`id_permiso`),
  KEY `id_permiso` (`id_permiso`),
  CONSTRAINT `rol_permiso_ibfk_1` FOREIGN KEY (`id_rol`) REFERENCES `rol` (`id_rol`) ON DELETE CASCADE,
  CONSTRAINT `rol_permiso_ibfk_2` FOREIGN KEY (`id_permiso`) REFERENCES `permiso` (`id_permiso`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rol_permiso`
--

LOCK TABLES `rol_permiso` WRITE;
/*!40000 ALTER TABLE `rol_permiso` DISABLE KEYS */;
INSERT INTO `rol_permiso` VALUES (1,1),(2,1),(3,1),(4,1),(1,2),(1,3),(2,3),(1,4),(1,5),(1,6),(2,6),(4,6),(1,7);
/*!40000 ALTER TABLE `rol_permiso` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario` (
  `id_usuario` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `correo` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `contrasena` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `estado` tinyint(1) NOT NULL DEFAULT '1',
  `fecha_creacion` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `ultimo_acceso` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id_usuario`),
  UNIQUE KEY `correo` (`correo`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES (1,'Admin Nuevo','nuevo_admin@sgu.com','$2b$12$JlYVABPWHzH2hTktljWmmOWKSxiCwuym01HwmrjsaOQ9rRXt23RM2',1,'2026-10-04 01:47:03','2026-10-31 00:34:58'),(2,'Juan Editado 2 desde Postman','juan@test.com','$2b$12$V6hX5dardCUpfkep.nNEcORtqMfe/ICfeA5HdKeG3UVHTaBMr0Viu',1,'2026-10-01 22:28:45','2026-10-18 03:18:59'),(3,'Maria','maria@test.com','$2b$12$T7UArbcih0fvPnnpQ6LH6.2cPON9tzMZVtSUiCCxNJ/xBangYtVsW',1,'2026-10-01 23:11:38',NULL),(4,'Test Conexión','conexion@test.com','$2b$12$jeaKeJZMQCsvAyBe3epi6eQyb3mDjRVHCPbpLgbXSmQqZCKslrNKG',1,'2026-10-04 00:31:57',NULL);
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario_rol`
--

DROP TABLE IF EXISTS `usuario_rol`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario_rol` (
  `id_usuario` int NOT NULL,
  `id_rol` int NOT NULL,
  PRIMARY KEY (`id_usuario`,`id_rol`),
  KEY `id_rol` (`id_rol`),
  CONSTRAINT `usuario_rol_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`) ON DELETE CASCADE,
  CONSTRAINT `usuario_rol_ibfk_2` FOREIGN KEY (`id_rol`) REFERENCES `rol` (`id_rol`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario_rol`
--

LOCK TABLES `usuario_rol` WRITE;
/*!40000 ALTER TABLE `usuario_rol` DISABLE KEYS */;
INSERT INTO `usuario_rol` VALUES (1,1),(2,2),(3,3),(4,3);
/*!40000 ALTER TABLE `usuario_rol` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-10-30 15:32:17
