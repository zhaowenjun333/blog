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

 Date: 31/01/2018 13:38:50
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for content
-- ----------------------------
DROP TABLE IF EXISTS `content`;
CREATE TABLE `content`  (
  `id` bigint(20) NOT NULL,
  `content` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  CONSTRAINT `content_ibfk_1` FOREIGN KEY (`id`) REFERENCES `post` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

SET FOREIGN_KEY_CHECKS = 1;
