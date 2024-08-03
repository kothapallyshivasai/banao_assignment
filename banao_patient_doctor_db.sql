-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Aug 03, 2024 at 08:18 PM
-- Server version: 8.0.31
-- PHP Version: 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `banao_patient_doctor_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add user', 6, 'add_customuserprofile'),
(22, 'Can change user', 6, 'change_customuserprofile'),
(23, 'Can delete user', 6, 'delete_customuserprofile'),
(24, 'Can view user', 6, 'view_customuserprofile'),
(25, 'Can add blog', 7, 'add_blog'),
(26, 'Can change blog', 7, 'change_blog'),
(27, 'Can delete blog', 7, 'delete_blog'),
(28, 'Can view blog', 7, 'view_blog');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(2, 'auth', 'permission'),
(3, 'auth', 'group'),
(4, 'contenttypes', 'contenttype'),
(5, 'sessions', 'session'),
(6, 'myapp', 'customuserprofile'),
(7, 'myapp', 'blog');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-08-03 00:07:30.244518'),
(2, 'contenttypes', '0002_remove_content_type_name', '2024-08-03 00:07:30.346635'),
(3, 'auth', '0001_initial', '2024-08-03 00:07:30.788373'),
(4, 'auth', '0002_alter_permission_name_max_length', '2024-08-03 00:07:30.842363'),
(5, 'auth', '0003_alter_user_email_max_length', '2024-08-03 00:07:30.851531'),
(6, 'auth', '0004_alter_user_username_opts', '2024-08-03 00:07:30.858546'),
(7, 'auth', '0005_alter_user_last_login_null', '2024-08-03 00:07:30.864978'),
(8, 'auth', '0006_require_contenttypes_0002', '2024-08-03 00:07:30.865980'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2024-08-03 00:07:30.872512'),
(10, 'auth', '0008_alter_user_username_max_length', '2024-08-03 00:07:30.878511'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2024-08-03 00:07:30.884126'),
(12, 'auth', '0010_alter_group_name_max_length', '2024-08-03 00:07:30.921320'),
(13, 'auth', '0011_update_proxy_permissions', '2024-08-03 00:07:30.928260'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2024-08-03 00:07:30.932810'),
(15, 'myapp', '0001_initial', '2024-08-03 00:07:31.512721'),
(16, 'admin', '0001_initial', '2024-08-03 00:07:31.779951'),
(17, 'admin', '0002_logentry_remove_auto_add', '2024-08-03 00:07:31.791385'),
(18, 'admin', '0003_logentry_add_action_flag_choices', '2024-08-03 00:07:31.805645'),
(19, 'myapp', '0002_customuserprofile_address_customuserprofile_pincode_and_more', '2024-08-03 00:07:32.040180'),
(20, 'myapp', '0003_alter_customuserprofile_profile_picture_blog', '2024-08-03 00:07:32.197642'),
(21, 'sessions', '0001_initial', '2024-08-03 00:07:32.269709');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `myapp_blog`
--

DROP TABLE IF EXISTS `myapp_blog`;
CREATE TABLE IF NOT EXISTS `myapp_blog` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(50) NOT NULL,
  `image` varchar(100) NOT NULL,
  `draft` tinyint(1) NOT NULL,
  `category_type` varchar(20) NOT NULL,
  `content` longtext NOT NULL,
  `summary` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `author_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_blog_author_id_ec39f0f2` (`author_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `myapp_blog`
--

INSERT INTO `myapp_blog` (`id`, `title`, `image`, `draft`, `category_type`, `content`, `summary`, `created_at`, `updated_at`, `author_id`) VALUES
(1, 'Covid-19 Awareness', 'blogs/covid-19-1.jpg', 0, 'Covid-19', 'Covid-19, caused by the novel coronavirus SARS-CoV-2, emerged in late 2019 and rapidly spread across the globe, leading to an unprecedented global health crisis. The virus primarily spreads through respiratory droplets, making close contact and crowded places high-risk areas for transmission.', 'Covid-19, caused by the SARS-CoV-2 virus, has led to a global health crisis with a wide range of symptoms and significant mortality, especially in vulnerable populations. Measures like social distancing and vaccination are critical in controlling its spread.', '2024-08-03 16:18:32.815436', '2024-08-03 17:56:51.528931', 4),
(2, 'Mental Health Awareness', 'blogs/mental-health-1.jpg', 0, 'Mental Health', 'Mental health is the state of our emotional, psychological, and social well-being, affecting how we think, feel, and act in our daily lives.', 'Mental health impacts our emotions, thoughts, and interactions, essential for overall well-being. Mental health impacts our emotions, thoughts, and interactions, essential for overall well-being.', '2024-08-03 16:57:50.367417', '2024-08-03 16:57:50.367417', 4),
(4, 'Heart Disease Awareness', 'blogs/heart-disease-1.jpg', 0, 'Heart Disease', 'Heart disease remains one of the leading causes of death globally, impacting millions of lives each year. Awareness and early detection are crucial in managing risk factors such as high blood pressure, high cholesterol, and lifestyle choices. Implementing heart-healthy practices can significantly reduce the risk of cardiovascular conditions and improve overall health.', 'Heart disease is a major health concern worldwide. Promoting awareness and adopting heart-healthy habits are key to reducing the risk and improving cardiovascular health.', '2024-08-03 17:44:40.864164', '2024-08-03 18:08:48.093651', 4),
(5, 'Immunization Awareness', 'blogs/immunization-1.jpg', 1, 'Immunization', 'Immunization is crucial for protecting individuals and communities from preventable diseases. Vaccines help build immunity, preventing the spread of infectious diseases and safeguarding public health. Regular vaccinations are essential for maintaining overall health and preventing outbreaks.', 'Immunization protects against preventable diseases by building immunity and preventing outbreaks. Regular vaccines are crucial for public health.', '2024-08-03 18:08:25.534947', '2024-08-03 18:08:25.534947', 4);

-- --------------------------------------------------------

--
-- Table structure for table `myapp_customuserprofile`
--

DROP TABLE IF EXISTS `myapp_customuserprofile`;
CREATE TABLE IF NOT EXISTS `myapp_customuserprofile` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `user_type` varchar(10) NOT NULL,
  `address` longtext,
  `pincode` int DEFAULT NULL,
  `profile_picture` varchar(100) DEFAULT NULL,
  `state` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `myapp_customuserprofile`
--

INSERT INTO `myapp_customuserprofile` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `user_type`, `address`, `pincode`, `profile_picture`, `state`) VALUES
(1, 'pbkdf2_sha256$720000$hvxKSifiGLNcUjrTrmQoOn$9q2iWmUvzCR73Y6bf7QoHqASD/2WEg4JaPbHmrYJJG8=', NULL, 1, 'shiva', '', '', 'shiva@gmail.com', 1, 1, '2024-08-03 00:07:51.687351', '', NULL, NULL, '', NULL),
(3, 'pbkdf2_sha256$720000$p6PKSOnfsASmoU5JqamzYk$LwOLbv8LihgxLx1FySKz2cE+HTK+zBim8+whx6oB8Q4=', '2024-08-03 20:00:55.916759', 0, 'patient1', 'Patient', 'One', 'patient1@gmail.com', 0, 1, '2024-08-03 00:16:53.465284', 'PATIENT', '2-10-913/1/102', 506001, 'profile/gojo_satoru_qq3JXgn.jpg', 'Telangana'),
(4, 'pbkdf2_sha256$720000$wZrZjmmuudtS1DvLEsd2q2$SOmbZmYZIG53M6d/uaICSpzx9YhDAu5NPwvNVkma2A4=', '2024-08-03 19:58:51.952051', 0, 'doctor1', 'doctor', 'one', 'doctor1@gmail.com', 0, 1, '2024-08-03 00:22:26.369484', 'DOCTOR', '2-9-10/102, Hanamkonda', 506001, 'profile/spiderman-2099_Lm0GEcX.jpg', 'Telangana'),
(6, 'pbkdf2_sha256$720000$6w4v1X7VOUtGFRPkDBcKfc$XiHqgnlL1Bbi/XBBQ/9454O7q/uBJq9/94ixgmKPyBk=', '2024-08-03 00:35:27.637549', 0, 'patient2', 'patient', 'two', 'patient2@gmail.com', 0, 1, '2024-08-03 00:30:03.056720', 'PATIENT', '20-913/102, Hanamkonda', 506001, 'profile/random_guy_image.jpg', 'Telangana');

-- --------------------------------------------------------

--
-- Table structure for table `myapp_customuserprofile_groups`
--

DROP TABLE IF EXISTS `myapp_customuserprofile_groups`;
CREATE TABLE IF NOT EXISTS `myapp_customuserprofile_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customuserprofile_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `myapp_customuserprofile__customuserprofile_id_gro_4449653f_uniq` (`customuserprofile_id`,`group_id`),
  KEY `myapp_customuserprofile_groups_customuserprofile_id_e2cb63fe` (`customuserprofile_id`),
  KEY `myapp_customuserprofile_groups_group_id_9f50783e` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `myapp_customuserprofile_user_permissions`
--

DROP TABLE IF EXISTS `myapp_customuserprofile_user_permissions`;
CREATE TABLE IF NOT EXISTS `myapp_customuserprofile_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `customuserprofile_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `myapp_customuserprofile__customuserprofile_id_per_94371e19_uniq` (`customuserprofile_id`,`permission_id`),
  KEY `myapp_customuserprofile_use_customuserprofile_id_ea405ec8` (`customuserprofile_id`),
  KEY `myapp_customuserprofile_user_permissions_permission_id_099155e9` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
