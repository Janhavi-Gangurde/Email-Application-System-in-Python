-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 17, 2022 at 11:42 AM
-- Server version: 10.4.20-MariaDB
-- PHP Version: 8.0.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `computer`
--

-- --------------------------------------------------------

--
-- Table structure for table `subject`
--

CREATE TABLE `subject` (
  `Java` int(11) NOT NULL,
  `Python` int(11) NOT NULL,
  `Android` int(11) NOT NULL,
  `PHP` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `userdetails`
--

CREATE TABLE `userdetails` (
  `name` varchar(100) NOT NULL,
  `birthdate` varchar(30) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `userdetails`
--

INSERT INTO `userdetails` (`name`, `birthdate`, `username`, `password`) VALUES
('Ajay shah', '19/05/2002', 'ajay@gmail.com', 'ajay'),
('YashAher', '12/03/2004', 'yashaher@gmail.com', 'Yash@123'),
('omakrBirajdar', '12/03/2003', 'omar@123', 'Omkar12@'),
('KundanZope', '14/09/2003', 'kundan@gmail.com', 'Kundan@12'),
('yashaher', '12/03/2004', 'yash@gmail.com', 'Yash12@'),
('Amarpatil', '12/03/2003', 'amar@gmail.com', 'Amar@13'),
('ChetanPatil', '12/03/2003', 'chetan@gmail.com', 'Chetan@123'),
('yashAher', '13/03/2004', 'aheryash@gmail.com', 'Yash@19');

-- --------------------------------------------------------

--
-- Table structure for table `username`
--

CREATE TABLE `username` (
  `user` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
