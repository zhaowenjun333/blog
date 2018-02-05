/*
 Navicat Premium Data Transfer

 Source Server         : 172.16.101.67
 Source Server Type    : MariaDB
 Source Server Version : 100033
 Source Host           : 172.16.101.67:3306
 Source Schema         : blog

 Target Server Type    : MariaDB
 Target Server Version : 100033
 File Encoding         : 65001

 Date: 31/01/2018 14:28:34
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for content
-- ----------------------------
DROP TABLE IF EXISTS `content`;
CREATE TABLE `content`  (
  `id` bigint(20) NOT NULL,
  `content` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  CONSTRAINT `content_ibfk_1` FOREIGN KEY (`id`) REFERENCES `post` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of content
-- ----------------------------
INSERT INTO `content` VALUES (4, 'polie');
INSERT INTO `content` VALUES (5, '5vmwareasgasgasg');
INSERT INTO `content` VALUES (6, 'asgdasgvmwareasdgasdgasg');
INSERT INTO `content` VALUES (7, 'vmware7');
INSERT INTO `content` VALUES (8, 'vmware8');
INSERT INTO `content` VALUES (9, 'vmware9');
INSERT INTO `content` VALUES (10, 'vmware10');
INSERT INTO `content` VALUES (11, '使用vmware的虚拟机过程中');
INSERT INTO `content` VALUES (12, '使用vmware的虚拟机过程中');
INSERT INTO `content` VALUES (13, '使用vmware的虚拟机过程中');
INSERT INTO `content` VALUES (14, '使用vmware的虚拟机过程中');
INSERT INTO `content` VALUES (15, '使用vmware的虚拟机过程中');

-- ----------------------------
-- Table structure for course
-- ----------------------------
DROP TABLE IF EXISTS `course`;
CREATE TABLE `course`  (
  `id` int(11) NOT NULL,
  `coursename` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  CONSTRAINT `course_ibfk_1` FOREIGN KEY (`id`) REFERENCES `subject` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for dig
-- ----------------------------
DROP TABLE IF EXISTS `dig`;
CREATE TABLE `dig`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `post_id` bigint(20) NOT NULL,
  `state` tinyint(4) NOT NULL,
  `pubdate` datetime(0) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `unq_user_post`(`user_id`, `post_id`) USING BTREE,
  INDEX `ix_dig_post_id`(`post_id`) USING BTREE,
  INDEX `ix_dig_user_id`(`user_id`) USING BTREE,
  CONSTRAINT `dig_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `dig_ibfk_2` FOREIGN KEY (`post_id`) REFERENCES `post` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for post
-- ----------------------------
DROP TABLE IF EXISTS `post`;
CREATE TABLE `post`  (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `title` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `author_id` int(11) NOT NULL,
  `postdate` datetime(0) NOT NULL,
  `hits` bigint(20) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `author_id`(`author_id`) USING BTREE,
  INDEX `ix_post_hits`(`hits`) USING BTREE,
  CONSTRAINT `post_ibfk_1` FOREIGN KEY (`author_id`) REFERENCES `user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 16 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of post
-- ----------------------------
INSERT INTO `post` VALUES (1, 'sorry', 5, '2018-01-25 16:50:16', 1);
INSERT INTO `post` VALUES (2, 'whay', 5, '2018-01-25 16:54:42', 1);
INSERT INTO `post` VALUES (3, 'xinwentoutiao', 5, '2018-01-25 16:55:10', 1);
INSERT INTO `post` VALUES (4, 'xinwentoutiao', 5, '2018-01-25 16:58:45', 1);
INSERT INTO `post` VALUES (5, 'vmware5', 5, '2018-01-25 17:12:52', 0);
INSERT INTO `post` VALUES (6, 'vmware5', 5, '2018-01-25 17:15:34', 0);
INSERT INTO `post` VALUES (7, 'vmware7', 5, '2018-01-25 17:16:09', 0);
INSERT INTO `post` VALUES (8, 'vmware8', 5, '2018-01-25 17:22:04', 0);
INSERT INTO `post` VALUES (9, 'vmware9', 5, '2018-01-25 17:24:57', 0);
INSERT INTO `post` VALUES (10, 'vmware10', 5, '2018-01-25 17:26:56', 0);
INSERT INTO `post` VALUES (11, 'vmware11', 5, '2018-01-25 17:38:25', 0);
INSERT INTO `post` VALUES (12, 'vmware12', 5, '2018-01-25 17:39:51', 0);
INSERT INTO `post` VALUES (13, 'vmware13', 5, '2018-01-25 17:41:27', 0);
INSERT INTO `post` VALUES (14, 'vmware14', 5, '2018-01-25 17:42:16', 0);
INSERT INTO `post` VALUES (15, 'vmware异问题解决办法', 5, '2018-01-25 17:43:31', 0);

-- ----------------------------
-- Table structure for subject
-- ----------------------------
DROP TABLE IF EXISTS `subject`;
CREATE TABLE `subject`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `subjectname` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(48) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `email` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `password` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `email`(`email`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES (1, 'zilong', 'zy@163.com', '$2b$12$/YZDSo/FKtjJIlun.zYGlOWH1SjaXbYtAXHN7VJHpszpy4iBlXvHW');
INSERT INTO `user` VALUES (2, 'zhangfei', 'zf@163.com', '$2b$12$b74clAzGLFpPdH9A/3rJV.fEOMWbRtRaoABhDtwzzmEdC5H/TYGtq');
INSERT INTO `user` VALUES (3, 'liubei', 'lb@163.com', '$2b$12$hdGIw2x/wKoM.isosTK1Q.MKDcyY9/ib.iU7vWjr4hf2kUX0frTsC');
INSERT INTO `user` VALUES (4, 'guanyu', 'gy@163.com', '$2b$12$S14WkiCix2tjqThzTv0jduo.2k4t3T19lyjI.Zxiw5VJGKAPZEAeS');
INSERT INTO `user` VALUES (5, 'huangzhong', 'hz@163.com', '$2b$12$gL1gAOgtGuVjarH6sS3tu.AFKSzRgUjCox7SM30BNyT8cgtLHiazq');

SET FOREIGN_KEY_CHECKS = 1;
