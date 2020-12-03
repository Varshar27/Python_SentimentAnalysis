-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 09, 2020 at 02:48 AM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `csa`
--

-- --------------------------------------------------------

--
-- Table structure for table `categories`
--

CREATE TABLE `categories` (
  `catid` int(11) NOT NULL,
  `catname` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `categories`
--

INSERT INTO `categories` (`catid`, `catname`) VALUES
(1, 'Baby Products'),
(2, 'Haircare'),
(3, 'Skincare'),
(4, 'Food Products');

-- --------------------------------------------------------

--
-- Table structure for table `country`
--

CREATE TABLE `country` (
  `con_id` int(11) NOT NULL,
  `country` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `country`
--

INSERT INTO `country` (`con_id`, `country`) VALUES
(1, 'UK'),
(2, 'USA'),
(3, 'Ireland');

-- --------------------------------------------------------

--
-- Table structure for table `customerfeedback`
--

CREATE TABLE `customerfeedback` (
  `csfeed_id` int(11) NOT NULL,
  `qus1` int(11) NOT NULL,
  `qus2` int(11) NOT NULL,
  `qus3` int(11) NOT NULL,
  `qus4` int(11) NOT NULL,
  `qus5` int(11) NOT NULL,
  `qus6` int(11) NOT NULL,
  `qus7` text NOT NULL,
  `salesid` int(11) NOT NULL,
  `polarity` decimal(10,2) NOT NULL,
  `confidence` decimal(10,2) NOT NULL,
  `ts` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `customerfeedback`
--

INSERT INTO `customerfeedback` (`csfeed_id`, `qus1`, `qus2`, `qus3`, `qus4`, `qus5`, `qus6`, `qus7`, `salesid`, `polarity`, `confidence`, `ts`) VALUES
(1, 1, 8, 8, 1, 4, 0, 'this is not good ', 1, '-0.35', '0.60', '2019-12-29 06:26:55'),
(2, 0, 9, 9, 1, 9, 0, 'this is good product', 2, '0.70', '0.60', '2019-12-29 07:11:01'),
(3, 0, 2, 3, 1, 3, 0, '', 6, '0.00', '0.00', '2020-01-08 19:31:16'),
(4, 1, 0, 0, 0, 8, 7, 'The chcolate is great and yummy', 7, '0.80', '0.75', '2020-01-09 01:38:25'),
(5, 1, 0, 0, 0, 6, 7, 'its an amazing product', 8, '0.60', '0.90', '2020-01-09 01:39:08'),
(6, 1, 0, 0, 0, 6, 6, 'excellent products', 9, '1.00', '1.00', '2020-01-09 01:40:37'),
(7, 1, 0, 0, 0, 8, 8, 'Good product ', 10, '0.70', '0.60', '2020-01-09 01:41:15'),
(8, 1, 0, 0, 0, 7, 7, 'Good shampoo', 11, '0.70', '0.60', '2020-01-09 01:42:05'),
(9, 1, 0, 0, 0, 8, 8, 'amazing product', 12, '0.60', '0.90', '2020-01-09 01:44:09'),
(10, 0, 8, 9, 1, 8, 0, 'love the taste , ', 13, '0.50', '0.60', '2020-01-09 01:45:22');

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `product_id` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `sku` varchar(200) NOT NULL,
  `image` text NOT NULL,
  `description` text NOT NULL,
  `category` int(11) NOT NULL,
  `subcategory` int(11) NOT NULL,
  `ts` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`product_id`, `name`, `sku`, `image`, `description`, `category`, `subcategory`, `ts`) VALUES
(1, 'MilkyBar', 'MilkyBar', '143078mk.jpg', 'Milkybar', 0, 0, '2019-12-29 06:24:24'),
(2, 'Cadbury', 'Cadbury', 'C87D68cb.jpg', 'Cadbury', 0, 0, '2019-12-29 06:25:59'),
(3, 'Snickers', 'Snickers', 'F827F95db34664045a3122137b8863.jpg', 'Snickers', 4, 7, '2020-01-02 05:11:13'),
(4, 'Cerelac', 'Baby care', '36BC1481jQkHzgL._SL1500_.jpg', 'Baby care', 1, 1, '2020-01-08 19:39:03'),
(5, 'Johnsons baby oil', 'Baby care', 'F4CD7081Tp-oKzKmL._SY355_.jpg', 'Baby care', 1, 1, '2020-01-08 19:39:53'),
(6, 'Johnsons baby moisturizer ', 'Baby care', '8C85B706798-150x150.jpg', 'Baby care', 1, 1, '2020-01-08 19:41:18'),
(7, 'Baby pampers', 'Baby care', '1D528Dnappies-silver-pampers_w227_h218.jpg', 'Baby care', 1, 1, '2020-01-08 19:42:37'),
(8, 'Cerelac Wheat Ble', 'Baby care', '5E81AAsnapshotimagehandler_1939087489.jpeg', 'Baby care', 1, 1, '2020-01-08 19:45:41'),
(9, 'Johnsons baby powder', 'Baby care', 'D0B757Powder.jpg', 'Baby care', 1, 1, '2020-01-08 19:47:08'),
(10, 'Panteen Shampoo', 'Hari Care', 'F79E9D71g-PAOElL._SL1500_.jpg', 'Hair Care', 2, 1, '2020-01-08 19:52:11'),
(11, 'TRESemme', 'Hair care', '54310771OLi65waUL._SL1500_.jpg', 'Hair Care', 2, 1, '2020-01-08 19:53:43'),
(12, 'TRESemme Keratin Smooth', 'Hair Care', 'F3772E00022400000510-943589-png.png', 'Hair Care', 1, 1, '2020-01-08 19:55:16'),
(13, 'TRESemme Keratin Smooth and Silky', 'Hair Care', '4339165012254060810_fop-1054649-png.png', 'Hair Care', 1, 1, '2020-01-08 19:56:33'),
(14, 'Dove Shampoo', 'Hair Care', 'BFEE1FDove_Straight_and_Silky_Shampoo_M_1.jpg', 'Hair Care', 1, 1, '2020-01-08 19:57:55'),
(15, 'LISTERINE', 'Mouth Care', '2EE8F281RFTTa8djL._SX466_.jpg', 'Mouth Care', 1, 1, '2020-01-08 20:02:51'),
(16, 'LISTERINE ORIGINAL', 'Mouth Care', '9C8CE1original.png', 'Mouth Care', 1, 1, '2020-01-08 20:04:32'),
(17, 'Colgate', 'Colgate', '89FAD5item_XL_24186465_35372301.jpg', 'Mouth Care', 1, 1, '2020-01-08 20:05:48'),
(18, 'ORAL B ', 'Mouth Care', '0A8761Oral-B-Pro-Expert-Strong-Teeth-Toothpaste_1200x1200.png', 'Mouth Care', 1, 1, '2020-01-08 20:07:06'),
(19, 'Vaseline Intensive care', 'Skin Care', '3CB5941534542.jpg', 'Skin Care', 3, 1, '2020-01-08 20:14:33'),
(20, 'Vaseline care', 'Skin Care', 'BEE7EFmedium_1445642124.jpeg', 'Skin Care', 1, 1, '2020-01-08 20:16:18'),
(21, 'NIVEA', 'Skin Care', '3A7070NIVEA-MEN-DARK-SPOT-REDUCTION-WHITENING-EFFECT-1416818899-10014518.jpg', 'Skin Care', 3, 1, '2020-01-08 20:20:37'),
(22, 'NIVEA Cream', 'Skin Care', 'E9C4CC81CGBGpbNqL._SY355_.jpg', 'Skin Care', 1, 1, '2020-01-08 20:21:58'),
(23, 'NIVEA Body Lotion ', 'Skin Care', '70B305e-287202-1.png', 'Skin Care', 3, 1, '2020-01-08 20:50:09'),
(24, 'kellogg Corn Flakes', 'Food Products', 'D7920FKellogg-s-moves-to-responsibly-sourced-Corn-Flakes_wrbm_large.jpg', 'Food Products', 4, 1, '2020-01-08 20:58:13');

-- --------------------------------------------------------

--
-- Table structure for table `product_price`
--

CREATE TABLE `product_price` (
  `prd_price_id` int(11) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `country` int(11) NOT NULL,
  `prod_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `product_price`
--

INSERT INTO `product_price` (`prd_price_id`, `price`, `country`, `prod_id`) VALUES
(1, '100.00', 1, 1),
(2, '80.00', 2, 1),
(3, '120.00', 3, 1),
(4, '85.00', 1, 2),
(5, '80.00', 2, 2),
(6, '95.00', 3, 2),
(7, '45.00', 1, 3),
(8, '50.00', 2, 3),
(9, '50.00', 3, 3),
(10, '4.00', 1, 4),
(11, '3.00', 2, 4),
(12, '5.00', 3, 4),
(13, '12.00', 1, 5),
(14, '3.00', 2, 5),
(15, '5.00', 3, 5),
(16, '6.00', 2, 6),
(17, '11.00', 1, 6),
(18, '9.00', 3, 6),
(19, '22.00', 3, 7),
(20, '21.00', 2, 7),
(21, '26.00', 1, 7),
(22, '24.00', 1, 8),
(23, '27.00', 3, 8),
(24, '30.00', 2, 8),
(25, '15.00', 1, 9),
(26, '18.00', 2, 9),
(27, '22.00', 3, 9),
(28, '30.00', 2, 10),
(29, '24.00', 2, 10),
(30, '28.00', 3, 10),
(31, '32.00', 1, 11),
(32, '30.00', 2, 11),
(33, '31.00', 3, 11),
(34, '33.00', 2, 12),
(35, '32.00', 3, 12),
(36, '31.00', 1, 12),
(37, '23.00', 2, 13),
(38, '34.00', 1, 13),
(39, '35.00', 3, 13),
(40, '16.00', 2, 14),
(41, '12.00', 1, 14),
(42, '14.00', 3, 14),
(43, '6.00', 1, 15),
(44, '8.00', 2, 15),
(45, '7.00', 3, 15),
(46, '6.00', 1, 16),
(47, '4.00', 2, 16),
(48, '7.00', 3, 16),
(49, '5.00', 1, 17),
(50, '7.00', 2, 17),
(51, '9.00', 3, 17),
(52, '12.00', 1, 18),
(53, '14.00', 2, 18),
(54, '16.00', 3, 18),
(55, '8.00', 1, 19),
(56, '10.00', 2, 19),
(57, '12.00', 3, 19),
(58, '8.00', 1, 20),
(59, '10.00', 2, 20),
(60, '7.00', 3, 20),
(61, '12.00', 1, 21),
(62, '14.00', 2, 21),
(63, '16.00', 3, 21),
(64, '4.00', 1, 22),
(65, '4.00', 2, 22),
(66, '5.00', 1, 22),
(67, '6.00', 1, 23),
(68, '5.00', 2, 23),
(69, '12.00', 3, 23),
(70, '11.00', 1, 24),
(71, '16.00', 2, 24),
(72, '12.00', 3, 24);

-- --------------------------------------------------------

--
-- Table structure for table `sales`
--

CREATE TABLE `sales` (
  `salesid` int(11) NOT NULL,
  `cusid` int(11) NOT NULL,
  `date` timestamp NOT NULL DEFAULT current_timestamp(),
  `salesitems` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `sales`
--

INSERT INTO `sales` (`salesid`, `cusid`, `date`, `salesitems`) VALUES
(1, 1, '2019-12-29 06:26:32', '1,2,3,4,5,6,'),
(2, 1, '2019-12-29 07:10:36', '1,2,5,'),
(3, 1, '2019-12-31 13:27:15', '3,'),
(4, 5, '2019-12-31 14:19:37', '1,'),
(5, 5, '2019-12-31 14:23:36', '1,'),
(6, 6, '2020-01-08 19:30:57', '7,'),
(7, 6, '2020-01-09 01:37:50', '1,'),
(8, 6, '2020-01-09 01:38:44', '13,21,22,'),
(9, 7, '2020-01-09 01:40:21', '31,36,41,43,46,'),
(10, 7, '2020-01-09 01:40:52', '67,'),
(11, 7, '2020-01-09 01:41:53', '28,33,'),
(12, 8, '2020-01-09 01:43:52', '4,13,'),
(13, 8, '2020-01-09 01:44:19', '4,');

-- --------------------------------------------------------

--
-- Table structure for table `subcategories`
--

CREATE TABLE `subcategories` (
  `subid` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `catid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `subcategories`
--

INSERT INTO `subcategories` (`subid`, `name`, `catid`) VALUES
(1, 'tutyutr', 3),
(2, 'sadfsafs', 3),
(3, 'yreyrey', 1),
(4, 'yreyery', 1),
(5, 'rytreyery', 1),
(6, 'yreyery', 1),
(7, 'tyerytery', 1),
(8, 'rttr', 3),
(9, '123', 1);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `type` int(11) NOT NULL,
  `password` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `zipcode` varchar(100) NOT NULL,
  `city` varchar(100) NOT NULL,
  `state` varchar(100) NOT NULL,
  `country` int(11) NOT NULL,
  `ts` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `name`, `email`, `type`, `password`, `address`, `zipcode`, `city`, `state`, `country`, `ts`) VALUES
(1, 'qwerwer', 'admin@admin.com', 1, 'qwer', 'sadsadsa', 'qwewqe', 'qwer', 'qwer', 1, '2019-12-27 16:48:41'),
(5, 'Shyaamlin', 'shyam@gmail.con', 0, '123456', 'Address', '123', '1', 'Dublin', 1, '2019-12-31 12:54:50'),
(6, 'Raki', 'rakesh@gmail.com', 0, '1234', 'Crumlin1', 'd012', 'Dublin', 'dublin ', 3, '2020-01-08 19:30:17'),
(7, 'varsha', 'varsha@gmail.com', 0, 'Amrutha', '23444555', 'd012', 'Dublin', 'ST', 1, '2020-01-09 01:39:44'),
(8, 'Naghma', 'naghma@gmail.com', 0, '1234', 'dublin', '123', 'Bangalore', 'ST', 2, '2020-01-09 01:42:59');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `categories`
--
ALTER TABLE `categories`
  ADD PRIMARY KEY (`catid`);

--
-- Indexes for table `country`
--
ALTER TABLE `country`
  ADD PRIMARY KEY (`con_id`);

--
-- Indexes for table `customerfeedback`
--
ALTER TABLE `customerfeedback`
  ADD PRIMARY KEY (`csfeed_id`);

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`product_id`);

--
-- Indexes for table `product_price`
--
ALTER TABLE `product_price`
  ADD PRIMARY KEY (`prd_price_id`);

--
-- Indexes for table `sales`
--
ALTER TABLE `sales`
  ADD PRIMARY KEY (`salesid`);

--
-- Indexes for table `subcategories`
--
ALTER TABLE `subcategories`
  ADD PRIMARY KEY (`subid`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `categories`
--
ALTER TABLE `categories`
  MODIFY `catid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `country`
--
ALTER TABLE `country`
  MODIFY `con_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `customerfeedback`
--
ALTER TABLE `customerfeedback`
  MODIFY `csfeed_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `product_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `product_price`
--
ALTER TABLE `product_price`
  MODIFY `prd_price_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=73;

--
-- AUTO_INCREMENT for table `sales`
--
ALTER TABLE `sales`
  MODIFY `salesid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `subcategories`
--
ALTER TABLE `subcategories`
  MODIFY `subid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
