-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 04, 2023 at 11:42 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `web_service`
--

-- --------------------------------------------------------

--
-- Table structure for table `face`
--

CREATE TABLE `face` (
  `id` int(12) NOT NULL,
  `jenis_kelamin` varchar(25) NOT NULL,
  `rentang_umur` varchar(25) NOT NULL,
  `label` varchar(10) NOT NULL,
  `akurasi` varchar(8) NOT NULL,
  `nama_file` text NOT NULL,
  `date_created` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `face`
--

INSERT INTO `face` (`id`, `jenis_kelamin`, `rentang_umur`, `label`, `akurasi`, `nama_file`, `date_created`) VALUES
(20, 'Perempuan', '6-11 Tahun', 'Anak', '87.06', 'save/Image/aaf7d6a1-0d95-416b-a4f1-4de5669932fe2717032646484141412.jpg', '2023-06-04 09:16:10'),
(21, 'Perempuan', '6-11 Tahun', 'Anak', '84.32', 'save/Image/a8911eb2-bebc-47b6-a990-79f9ed27bebc3296516744943360218.jpg', '2023-06-04 09:17:14'),
(22, 'Perempuan', '6-11 Tahun', 'Anak', '98.04', 'save/Image/14e6bfe4-9177-4f07-84cd-8d101124fcc341880052594724467.jpg', '2023-06-04 09:18:02'),
(23, 'Perempuan', '6-11 Tahun', 'Anak', '95.8', 'save/Image/67d8f578-045c-4ace-898b-d4a676d815d5629857066711006347.jpg', '2023-06-04 09:23:52'),
(24, 'Perempuan', '6-11 Tahun', 'Anak', '95.38', 'save/Image/1798e1ab-4d95-4778-9687-038839c0e0524470979582402124168.jpg', '2023-06-04 09:24:35'),
(25, 'Laki-Laki', '>=20 Tahun', 'Dewasa', '63.98', 'save/Image/1822309a-9531-4760-bea2-32f5ec7af1505875219366425789117.jpg', '2023-06-04 09:27:53'),
(26, 'Perempuan', '6-11 Tahun', 'Anak', '99.58', 'save/Image/e8a093d0-4948-4e94-a240-af14241277ae7355466726318261015.jpg', '2023-06-04 09:28:46'),
(27, 'Laki-Laki', '>=20 Tahun', 'Dewasa', '78.94', 'save/Image/d3abde59-ab55-492c-a353-26130ddd42eb7237037021815126261.jpg', '2023-06-04 09:29:26'),
(28, 'Perempuan', '6-11 Tahun', 'Anak', '96.63', 'save/Image/1615de0c-830d-4dc3-82c3-86b22b31baa54210981060303337226.jpg', '2023-06-04 09:30:09'),
(29, 'Laki-Laki', '>=20 Tahun', 'Dewasa', '87.49', 'save/Image/a8579241-32d7-4739-b938-63226459f32a3824563507987863996.jpg', '2023-06-04 09:32:37'),
(30, 'Laki-Laki', '>=20 Tahun', 'Dewasa', '69.63', 'save/Image/4f142a29-4fd4-4612-b2e3-a7aa464e68094610258241727501787.jpg', '2023-06-04 09:33:25'),
(31, 'Laki-Laki', '>=20 Tahun', 'Dewasa', '95.89', 'save/Image/e5c07392-bb4f-40da-a9ac-2f54a521a3366392582997014692185.jpg', '2023-06-04 09:39:44');

-- --------------------------------------------------------

--
-- Table structure for table `gender`
--

CREATE TABLE `gender` (
  `id` int(11) NOT NULL,
  `jenis_kelamin` varchar(100) NOT NULL,
  `rentang_umur` varchar(100) NOT NULL,
  `label` varchar(100) DEFAULT NULL,
  `akurasi` varchar(8) NOT NULL,
  `nama_file` text NOT NULL,
  `date_created` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `gender`
--

INSERT INTO `gender` (`id`, `jenis_kelamin`, `rentang_umur`, `label`, `akurasi`, `nama_file`, `date_created`) VALUES
(76, 'Laki-Laki', '6-11 Tahun', 'Anak', '100.0', 'save/Audio/Anak-L-996.wav', '2023-05-26 15:44:00'),
(77, 'Perempuan', '>=20 Tahun', 'Dewasa', '86.45', 'save/Audio/Dewasa-P-999.wav', '2023-05-26 15:44:17'),
(78, 'Laki-Laki', '6-11 Tahun', 'Anak', '99.68', 'save/Audio/Anak-L-0.wav', '2023-05-26 16:09:50'),
(79, 'Laki-Laki', '6-11 Tahun', 'Anak', '99.68', 'save/Audio/Anak-L-0.wav', '2023-05-26 16:09:57'),
(80, 'Laki-Laki', '12-19 Tahun', 'Remaja', '90.25', 'save/Audio/Remaja-L-1.wav', '2023-05-26 16:10:16'),
(81, 'Perempuan', '12-19 Tahun', 'Remaja', '99.8', 'save/Audio/Remaja-P-5.wav', '2023-05-26 16:10:27'),
(82, 'Laki-Laki', '>=20 Tahun', 'Dewasa', '82.27', 'save/Audio/Dewasa-L-1.wav', '2023-05-26 16:10:44'),
(83, 'Laki-Laki', '12-19 Tahun', 'Remaja', '89.57', 'save/Audio/tesAnak.wav', '2023-05-27 03:46:25'),
(84, 'Perempuan', '12-19 Tahun', 'Remaja', '53.96', 'save/Audio/tes-fiqih.wav', '2023-05-27 03:46:43'),
(85, 'Perempuan', '12-19 Tahun', 'Remaja', '96.59', 'save/Audio/cobatest.wav', '2023-05-27 03:49:09'),
(86, 'Laki-Laki', '>=20 Tahun', 'Dewasa', '96.47', 'save/Audio/Dewasa-L-16.wav', '2023-05-27 03:50:00'),
(87, 'Laki-Laki', '>=20 Tahun', 'Dewasa', '82.84', 'save/Audio/Hallo_DewasaL.wav', '2023-05-27 03:50:24'),
(88, 'Perempuan', '12-19 Tahun', 'Remaja', '54.08', 'save/Audio/Hallo_DewasaP.wav', '2023-05-27 03:51:17'),
(89, 'Perempuan', '12-19 Tahun', 'Remaja', '61.89', 'save/Audio/Hallo_RemajaLP.wav', '2023-05-27 03:51:39'),
(90, 'Laki-Laki', '12-19 Tahun', 'Remaja', '89.57', 'save/Audio/tesAnak.wav', '2023-05-27 03:52:17'),
(91, 'Perempuan', '12-19 Tahun', 'Remaja', '53.96', 'save/Audio/tes-fiqih.wav', '2023-05-27 03:52:37'),
(92, 'Perempuan', '>=20 Tahun', 'Dewasa', '86.45', 'save/Audio/Dewasa-P-999.wav', '2023-05-27 11:34:54'),
(93, 'Laki-Laki', '12-19 Tahun', 'Remaja', '90.25', 'save/Audio/Remaja-L-1.wav', '2023-05-28 02:33:18'),
(94, 'Laki-Laki', '>=20 Tahun', 'Dewasa', '82.27', 'save/Audio/Dewasa-L-1.wav', '2023-05-28 02:33:34'),
(95, 'Laki-Laki', '12-19 Tahun', 'Remaja', '89.57', 'save/Audio/tesAnak.wav', '2023-05-28 02:33:51'),
(96, 'Perempuan', '12-19 Tahun', 'Remaja', '96.59', 'save/Audio/cobatest.wav', '2023-05-28 02:35:27'),
(97, 'Laki-Laki', '6-11 Tahun', 'Anak', '100.0', 'save/Audio/Anak-L-996.wav', '2023-05-28 02:36:17'),
(98, 'Laki-Laki', '6-11 Tahun', 'Anak', '99.68', 'save/Audio/Anak-L-0.wav', '2023-05-28 02:36:59'),
(99, 'Perempuan', '12-19 Tahun', 'Remaja', '99.8', 'save/Audio/Remaja-P-5.wav', '2023-05-28 03:07:50'),
(100, 'Laki-Laki', '6-11 Tahun', 'Anak', '100.0', 'save/Audio/Anak-L-996.wav', '2023-05-28 03:09:22'),
(101, 'Laki-Laki', '>=20 Tahun', 'Dewasa', '96.47', 'save/Audio/Dewasa-L-16.wav', '2023-05-28 03:09:51'),
(102, 'Perempuan', '12-19 Tahun', 'Remaja', '97.0', 'save/Audio/recording.wav', '2023-05-28 09:21:31'),
(103, 'Perempuan', '12-19 Tahun', 'Remaja', '84.83', 'save/Audio/recording.wav', '2023-05-28 09:22:22'),
(104, 'Perempuan', '12-19 Tahun', 'Remaja', '98.13', 'save/Audio/recording.wav', '2023-05-28 09:22:53'),
(105, 'Perempuan', '12-19 Tahun', 'Remaja', '64.94', 'save/Audio/recording.wav', '2023-05-28 09:26:20'),
(106, 'Perempuan', '12-19 Tahun', 'Remaja', '35.66', 'save/Audio/recording.wav', '2023-05-28 09:26:49'),
(107, 'Laki-Laki', '>=20 Tahun', 'Dewasa', '51.13', 'save/Audio/recording.wav', '2023-05-28 09:27:22'),
(108, 'Laki-Laki', '>=20 Tahun', 'Dewasa', '97.56', 'save/Audio/recording.wav', '2023-05-28 09:27:43'),
(109, 'Laki-Laki', '>=20 Tahun', 'Dewasa', '83.39', 'save/Audio/recording.wav', '2023-05-28 09:28:13'),
(110, 'Laki-Laki', '>=20 Tahun', 'Dewasa', '50.67', 'save/Audio/recording.wav', '2023-05-28 09:29:25'),
(111, 'Laki-Laki', '>=20 Tahun', 'Dewasa', '91.38', 'save/Audio/recording.wav', '2023-05-28 09:30:21'),
(112, 'Laki-Laki', '>=20 Tahun', 'Dewasa', '91.24', 'save/Audio/recording.wav', '2023-05-28 09:30:36'),
(113, 'Perempuan', '>=20 Tahun', 'Dewasa', '100.0', 'save/Audio/recording.wav', '2023-05-28 09:31:25'),
(114, 'Perempuan', '>=20 Tahun', 'Dewasa', '99.48', 'save/Audio/recording.wav', '2023-05-28 09:32:45'),
(115, 'Perempuan', '>=20 Tahun', 'Dewasa', '97.9', 'save/Audio/recording.wav', '2023-05-28 09:33:13'),
(116, 'Perempuan', '12-19 Tahun', 'Remaja', '100.0', 'save/Audio/recording.wav', '2023-05-28 09:33:41'),
(117, 'Perempuan', '12-19 Tahun', 'Remaja', '100.0', 'save/Audio/recording.wav', '2023-05-28 09:34:03'),
(118, 'Perempuan', '>=20 Tahun', 'Dewasa', '99.94', 'save/Audio/recording.wav', '2023-05-28 09:34:45'),
(119, 'Perempuan', '>=20 Tahun', 'Dewasa', '99.62', 'save/Audio/recording.wav', '2023-05-28 09:35:40'),
(120, 'Perempuan', '>=20 Tahun', 'Dewasa', '85.08', 'save/Audio/recording.wav', '2023-05-28 09:36:07'),
(121, 'Perempuan', '12-19 Tahun', 'Remaja', '100.0', 'save/Audio/recording.wav', '2023-05-28 09:36:54'),
(122, 'Perempuan', '12-19 Tahun', 'Remaja', '100.0', 'save/Audio/recording.wav', '2023-05-28 09:38:14'),
(123, 'Perempuan', '12-19 Tahun', 'Remaja', '94.75', 'save/Audio/recording.wav', '2023-05-28 09:38:55'),
(124, 'Laki-Laki', '>=20 Tahun', 'Dewasa', '82.35', 'save/Audio/recording.wav', '2023-05-28 09:40:11'),
(125, 'Perempuan', '12-19 Tahun', 'Remaja', '100.0', 'save/Audio/recording.wav', '2023-05-28 09:41:12'),
(126, 'Laki-Laki', '>=20 Tahun', 'Dewasa', '89.16', 'save/Audio/recording.wav', '2023-05-28 09:43:44'),
(127, 'Perempuan', '12-19 Tahun', 'Remaja', '99.72', 'save/Audio/recording.wav', '2023-05-28 09:52:43'),
(128, 'Perempuan', '12-19 Tahun', 'Remaja', '74.4', 'save/Audio/recording.wav', '2023-05-28 09:53:54'),
(129, 'Laki-Laki', '>=20 Tahun', 'Dewasa', '93.92', 'save/Audio/recording.wav', '2023-05-28 09:54:40'),
(130, 'Perempuan', '12-19 Tahun', 'Remaja', '79.55', 'save/Audio/recording.wav', '2023-05-28 09:55:11'),
(131, 'Perempuan', '>=20 Tahun', 'Dewasa', '90.3', 'save/Audio/recording.wav', '2023-05-28 09:56:35'),
(132, 'Perempuan', '12-19 Tahun', 'Remaja', '97.83', 'save/Audio/recording.wav', '2023-05-28 09:59:41'),
(133, 'Laki-Laki', '>=20 Tahun', 'Dewasa', '84.52', 'save/Audio/recording.wav', '2023-05-28 10:00:14'),
(134, 'Laki-Laki', '>=20 Tahun', 'Dewasa', '52.62', 'save/Audio/recording.wav', '2023-05-28 10:00:21'),
(135, 'Laki-Laki', '>=20 Tahun', 'Dewasa', '97.22', 'save/Audio/recording.wav', '2023-05-28 11:00:24'),
(136, 'Perempuan', '12-19 Tahun', 'Remaja', '99.62', 'save/Audio/recording.wav', '2023-05-28 11:02:09'),
(137, 'Perempuan', '12-19 Tahun', 'Remaja', '99.75', 'save/Audio/recording.wav', '2023-05-28 11:02:53'),
(138, 'Perempuan', '12-19 Tahun', 'Remaja', '98.78', 'save/Audio/recording2.wav', '2023-05-28 11:03:27'),
(139, 'Perempuan', '12-19 Tahun', 'Remaja', '88.38', 'save/Audio/recording2.wav', '2023-05-28 11:03:48'),
(140, 'Laki-Laki', '>=20 Tahun', 'Dewasa', '67.61', 'save/Audio/recording1.wav', '2023-05-28 11:06:10'),
(141, 'Laki-Laki', '>=20 Tahun', 'Dewasa', '59.63', 'save/Audio/recording1.wav', '2023-05-28 11:06:29'),
(142, 'Perempuan', '12-19 Tahun', 'Remaja', '99.99', 'save/Audio/recording1.wav', '2023-05-28 11:06:44'),
(143, 'Laki-Laki', '>=20 Tahun', 'Dewasa', '99.91', 'save/Audio/recording1.wav', '2023-05-28 11:07:49'),
(144, 'Laki-Laki', '12-19 Tahun', 'Remaja', '95.42', 'save/Audio/recording1.wav', '2023-05-28 11:08:05'),
(145, 'Laki-Laki', '>=20 Tahun', 'Dewasa', '96.56', 'save/Audio/recording1.wav', '2023-05-28 11:10:58'),
(146, 'Perempuan', '12-19 Tahun', 'Remaja', '75.01', 'save/Audio/recording1.wav', '2023-05-28 11:11:44'),
(147, 'Perempuan', '12-19 Tahun', 'Remaja', '84.45', 'save/Audio/recording1.wav', '2023-05-28 11:12:36'),
(148, 'Laki-Laki', '>=20 Tahun', 'Dewasa', '55.52', 'save/Audio/recording1.wav', '2023-05-28 11:13:23'),
(149, 'Perempuan', '12-19 Tahun', 'Remaja', '66.32', 'save/Audio/recording1.wav', '2023-05-28 11:13:44'),
(150, 'Perempuan', '12-19 Tahun', 'Remaja', '78.57', 'save/Audio/recording1.wav', '2023-05-28 11:13:57'),
(151, 'Laki-Laki', '>=20 Tahun', 'Dewasa', '91.93', 'save/Audio/recording1.wav', '2023-05-28 11:14:09'),
(152, 'Perempuan', '12-19 Tahun', 'Remaja', '98.91', 'save/Audio/recording2.wav', '2023-05-28 11:16:08'),
(153, 'Laki-Laki', '12-19 Tahun', 'Remaja', '98.69', 'save/Audio/recording2.wav', '2023-05-28 11:16:27'),
(154, 'Perempuan', '12-19 Tahun', 'Remaja', '98.4', 'save/Audio/recording2.wav', '2023-05-28 11:17:33'),
(155, 'Perempuan', '12-19 Tahun', 'Remaja', '99.96', 'save/Audio/recording2.wav', '2023-05-28 11:17:47'),
(156, 'Perempuan', '12-19 Tahun', 'Remaja', '95.37', 'save/Audio/recording2.wav', '2023-05-28 11:19:07'),
(157, 'Perempuan', '12-19 Tahun', 'Remaja', '100.0', 'save/Audio/recording2.wav', '2023-05-28 11:23:18'),
(158, 'Laki-Laki', '>=20 Tahun', 'Dewasa', '99.92', 'save/Audio/recording2.wav', '2023-05-28 11:54:55'),
(159, 'Perempuan', '12-19 Tahun', 'Remaja', '53.89', 'save/Audio/recording2.wav', '2023-05-29 02:58:50'),
(160, 'Laki-Laki', '>=20 Tahun', 'Dewasa', '70.96', 'save/Audio/recording2.wav', '2023-05-29 02:59:06'),
(161, 'Laki-Laki', '>=20 Tahun', 'Dewasa', '61.33', 'save/Audio/recording2.wav', '2023-05-29 02:59:25'),
(162, 'Perempuan', '>=20 Tahun', 'Dewasa', '72.73', 'save/Audio/recording2.wav', '2023-05-29 03:17:49'),
(163, 'Perempuan', '>=20 Tahun', 'Dewasa', '54.62', 'save/Audio/recording2.wav', '2023-05-29 03:45:53'),
(164, 'Laki-Laki', '>=20 Tahun', 'Dewasa', '99.21', 'save/Audio/recording2.wav', '2023-05-30 03:36:23'),
(165, 'Perempuan', '12-19 Tahun', 'Remaja', '79.01', 'save/Audio/recording2.wav', '2023-05-30 04:10:48'),
(166, 'Perempuan', '12-19 Tahun', 'Remaja', '98.03', 'save/Audio/recording2.wav', '2023-05-30 04:11:21'),
(167, 'Laki-Laki', '>=20 Tahun', 'Dewasa', '99.37', 'save/Audio/recording2.wav', '2023-05-30 04:12:23'),
(168, 'Laki-Laki', '>=20 Tahun', 'Dewasa', '99.62', 'save/Audio/recording2.wav', '2023-05-30 04:12:45'),
(169, 'Laki-Laki', '>=20 Tahun', 'Dewasa', '52.92', 'save/Audio/recording2.wav', '2023-05-30 04:18:30'),
(170, 'Perempuan', '12-19 Tahun', 'Remaja', '54.47', 'save/Audio/recording2.wav', '2023-05-30 04:19:20'),
(171, 'Perempuan', '12-19 Tahun', 'Remaja', '92.14', 'save/Audio/recording2.wav', '2023-05-30 04:20:16'),
(172, 'Perempuan', '12-19 Tahun', 'Remaja', '99.1', 'save/Audio/recording2.wav', '2023-05-30 04:24:27'),
(173, 'Perempuan', '12-19 Tahun', 'Remaja', '67.9', 'save/Audio/recording2.wav', '2023-05-30 04:24:56'),
(174, 'Perempuan', '12-19 Tahun', 'Remaja', '99.05', 'save/Audio/recording2.wav', '2023-05-30 04:29:44'),
(175, 'Perempuan', '12-19 Tahun', 'Remaja', '97.77', 'save/Audio/recording2.wav', '2023-05-30 04:31:45'),
(176, 'Perempuan', '12-19 Tahun', 'Remaja', '99.01', 'save/Audio/recording2.wav', '2023-05-30 04:33:18'),
(177, 'Perempuan', '12-19 Tahun', 'Remaja', '99.9', 'save/Audio/recording2.wav', '2023-05-30 04:39:26'),
(178, 'Perempuan', '12-19 Tahun', 'Remaja', '99.58', 'save/Audio/recording2.wav', '2023-06-01 08:04:23'),
(179, 'Perempuan', '12-19 Tahun', 'Remaja', '86.97', 'save/Audio/recording2.wav', '2023-06-01 08:16:25'),
(180, 'Perempuan', '12-19 Tahun', 'Remaja', '99.85', 'save/Audio/recording2.wav', '2023-06-01 08:18:16'),
(181, 'Perempuan', '12-19 Tahun', 'Remaja', '91.85', 'save/Audio/recording2.wav', '2023-06-01 08:20:44'),
(182, 'Perempuan', '12-19 Tahun', 'Remaja', '98.99', 'save/Audio/recording2.wav', '2023-06-01 08:21:42'),
(183, 'Laki-Laki', '12-19 Tahun', 'Remaja', '66.32', 'save/Audio/recording2.wav', '2023-06-01 08:23:22'),
(184, 'Laki-Laki', '>=20 Tahun', 'Dewasa', '62.69', 'save/Audio/recording2.wav', '2023-06-01 08:24:26'),
(185, 'Perempuan', '12-19 Tahun', 'Remaja', '96.11', 'save/Audio/recording2.wav', '2023-06-01 08:25:22'),
(186, 'Perempuan', '12-19 Tahun', 'Remaja', '84.82', 'save/Audio/recording2.wav', '2023-06-01 08:27:55'),
(187, 'Laki-Laki', '>=20 Tahun', 'Dewasa', '57.71', 'save/Audio/recording2.wav', '2023-06-01 08:29:22'),
(188, 'Perempuan', '12-19 Tahun', 'Remaja', '100.0', 'save/Audio/recording2.wav', '2023-06-01 08:30:17'),
(189, 'Perempuan', '12-19 Tahun', 'Remaja', '99.87', 'save/Audio/recording2.wav', '2023-06-01 08:31:24'),
(190, 'Laki-Laki', '>=20 Tahun', 'Dewasa', '87.54', 'save/Audio/recording2.wav', '2023-06-01 08:34:02'),
(191, 'Laki-Laki', '>=20 Tahun', 'Dewasa', '98.49', 'save/Audio/recording2.wav', '2023-06-01 08:34:36'),
(192, 'Perempuan', '12-19 Tahun', 'Remaja', '99.81', 'save/Audio/recording2.wav', '2023-06-01 08:35:14'),
(193, 'Perempuan', '12-19 Tahun', 'Remaja', '100.0', 'save/Audio/recording2.wav', '2023-06-01 08:36:39'),
(194, 'Laki-Laki', '>=20 Tahun', 'Dewasa', '79.32', 'save/Audio/recording2.wav', '2023-06-01 09:18:58'),
(195, 'Perempuan', '12-19 Tahun', 'Remaja', '99.88', 'save/Audio/recording2.wav', '2023-06-01 09:21:08'),
(196, 'Perempuan', '12-19 Tahun', 'Remaja', '50.81', 'save/Audio/recording2.wav', '2023-06-01 09:22:00'),
(197, 'Laki-Laki', '>=20 Tahun', 'Dewasa', '67.85', 'save/Audio/recording2.wav', '2023-06-01 09:22:54'),
(198, 'Perempuan', '12-19 Tahun', 'Remaja', '59.09', 'save/Audio/recording2.wav', '2023-06-01 09:24:33'),
(199, 'Laki-Laki', '>=20 Tahun', 'Dewasa', '99.8', 'save/Audio/recording2.wav', '2023-06-01 09:25:08'),
(200, 'Laki-Laki', '>=20 Tahun', 'Dewasa', '99.57', 'save/Audio/recording2.wav', '2023-06-01 09:25:35'),
(201, 'Laki-Laki', '>=20 Tahun', 'Dewasa', '95.53', 'save/Audio/recording2.wav', '2023-06-01 09:41:14'),
(202, 'Laki-Laki', '>=20 Tahun', 'Dewasa', '94.49', 'save/Audio/recording2.wav', '2023-06-01 09:43:04'),
(203, 'Laki-Laki', '>=20 Tahun', 'Dewasa', '81.22', 'save/Audio/recording2.wav', '2023-06-01 09:44:22'),
(204, 'Perempuan', '12-19 Tahun', 'Remaja', '99.38', 'save/Audio/recording2.wav', '2023-06-01 09:45:30'),
(205, 'Perempuan', '12-19 Tahun', 'Remaja', '98.47', 'save/Audio/recording2.wav', '2023-06-01 09:46:33'),
(206, 'Perempuan', '>=20 Tahun', 'Dewasa', '100.0', 'save/Audio/recording2.wav', '2023-06-01 09:48:25'),
(207, 'Laki-Laki', '>=20 Tahun', 'Dewasa', '46.89', 'save/Audio/recording2.wav', '2023-06-01 10:18:46'),
(208, 'Perempuan', '12-19 Tahun', 'Remaja', '99.03', 'save/Audio/recording2.wav', '2023-06-01 10:24:36'),
(209, 'Perempuan', '12-19 Tahun', 'Remaja', '99.97', 'save/Audio/recording2.wav', '2023-06-01 13:40:02'),
(210, 'Perempuan', '12-19 Tahun', 'Remaja', '81.79', 'save/Audio/recording2.wav', '2023-06-01 13:40:34'),
(211, 'Perempuan', '12-19 Tahun', 'Remaja', '70.42', 'save/Audio/recording2.wav', '2023-06-01 15:10:39'),
(212, 'Laki-Laki', '12-19 Tahun', 'Remaja', '58.39', 'save/Audio/recording2.wav', '2023-06-03 04:47:33'),
(213, 'Perempuan', '>=20 Tahun', 'Dewasa', '72.99', 'save/Audio/recording2.wav', '2023-06-03 04:58:41'),
(214, 'Laki-Laki', '>=20 Tahun', 'Dewasa', '74.14', 'save/Audio/recording2.wav', '2023-06-03 05:10:33'),
(215, 'Laki-Laki', '>=20 Tahun', 'Dewasa', '80.69', 'save/Audio/recording2.wav', '2023-06-03 06:45:23'),
(216, 'Laki-Laki', '12-19 Tahun', 'Remaja', '56.77', 'save/Audio/recording2.wav', '2023-06-04 06:58:05'),
(217, 'Laki-Laki', '12-19 Tahun', 'Remaja', '59.71', 'save/Audio/recording2.wav', '2023-06-04 06:58:14'),
(218, 'Perempuan', '12-19 Tahun', 'Remaja', '68.62', 'save/Audio/recording2.wav', '2023-06-04 06:58:55'),
(219, 'Laki-Laki', '>=20 Tahun', 'Dewasa', '88.66', 'save/Audio/recording2.wav', '2023-06-04 07:10:32'),
(220, 'Perempuan', '12-19 Tahun', 'Remaja', '56.49', 'save/Audio/recording2.wav', '2023-06-04 07:19:11'),
(221, 'Laki-Laki', '12-19 Tahun', 'Remaja', '98.52', 'save/Audio/recording2.wav', '2023-06-04 07:30:40'),
(222, 'Laki-Laki', '>=20 Tahun', 'Dewasa', '97.2', 'save/Audio/recording2.wav', '2023-06-04 07:52:23'),
(223, 'Laki-Laki', '>=20 Tahun', 'Dewasa', '93.17', 'save/Audio/recording2.wav', '2023-06-04 08:35:59'),
(224, 'Perempuan', '12-19 Tahun', 'Remaja', '49.35', 'save/Audio/recording2.wav', '2023-06-04 08:44:25'),
(225, 'Perempuan', '12-19 Tahun', 'Remaja', '51.93', 'save/Audio/recording2.wav', '2023-06-04 09:34:09');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `email` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `password` varchar(256) NOT NULL,
  `token` text DEFAULT NULL,
  `status_validasi` text DEFAULT NULL,
  `level` varchar(256) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `update_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `email`, `name`, `password`, `token`, `status_validasi`, `level`, `created_at`, `update_at`) VALUES
(3, 'mohfiqiherinsyah@gmail.com', 'Moh. Fiqih Erinsyah', 'pbkdf2:sha256:600000$BHVN6bAxNnddNalU$333a7226be8235449500a393f2781c3105f0c90de4a64b8df9acd16c4f43d36a', 'bW9oZmlxaWhlcmluc3lhaEBnbWFpbC5jb20=', 'Valid', 'Administrator', '2023-04-25 03:56:20', '2023-06-03 16:29:38'),
(9, 'mfiqiherinsyah90@gmail.com', 'mfiqiherinsyah90', 'pbkdf2:sha256:600000$sBgQVDT0nqhHg8Jz$b1a3a0f0a7c67835edb00b0371a3737299927085cb2000c534d7f7a1084e7c62', 'bWZpcWloZXJpbnN5YWg5MEBnbWFpbC5jb20=bWZpcWloZXJpbnN5YWg5MEBnbWFpbC5jb20=', 'Valid', 'User', '2023-05-08 08:31:51', '2023-06-04 09:39:18'),
(10, 'vitakarenina06@gmail.com', 'Vita Karenina', 'pbkdf2:sha256:600000$9Rf4kRVETy2SJcDR$a6d632caaaed7a6e99dfc7e81011fa7728b01c1bc98afba943a7cd0f87482f33', NULL, 'Belum Validasi', 'Administrator', '2023-05-08 08:33:01', '2023-05-15 14:52:51'),
(20, 'mfiqiher@gmail.com', 'm fiqih', 'pbkdf2:sha256:600000$STLU9K30Xo8VwZ49$9de1efb3833625f7b1bcfca35c7e943f0d40178fe9126558d33323f1c7421878', NULL, 'Belum Validasi', 'Administrator', '2023-05-25 15:48:46', '2023-05-25 15:48:46'),
(21, 'fiqih@gmail.com', 'fiqih', 'pbkdf2:sha256:600000$YpG5gReTXyjJEGWh$1b1e153b2ee72f23af98f18c6a5f0abc33c93baccf1de459aaf6be047473e93a', NULL, 'Belum Validasi', 'Administrator', '2023-05-30 14:05:44', '2023-05-30 14:05:44'),
(22, 'faqih@gmail.com', 'faqih', 'pbkdf2:sha256:600000$Y45Rh0XVpBCnFSwp$67efb940d37ec9e05ad3543346fe69ab6b07baed6d9f6e50fad40f0f5d13c21e', NULL, 'Belum Validasi', 'User', '2023-06-01 02:49:28', '2023-06-01 02:49:28'),
(24, 'fahrizul352@gmail.com', 'fahri', 'pbkdf2:sha256:600000$Sy1x1QlWrhckWOid$ca619bc74fdb787853457709919c14f18c7c9ba17f0706e1b20232cbf316b296', NULL, 'Belum Validasi', 'User', '2023-06-03 15:14:53', '2023-06-03 15:14:53');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `face`
--
ALTER TABLE `face`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `gender`
--
ALTER TABLE `gender`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `face`
--
ALTER TABLE `face`
  MODIFY `id` int(12) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- AUTO_INCREMENT for table `gender`
--
ALTER TABLE `gender`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=226;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
