/*
 Navicat Premium Dump SQL

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 80035 (8.0.35)
 Source Host           : localhost:3306
 Source Schema         : unwomen

 Target Server Type    : MySQL
 Target Server Version : 80035 (8.0.35)
 File Encoding         : 65001

 Date: 27/02/2025 15:20:29
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for appointments
-- ----------------------------
DROP TABLE IF EXISTS `appointments`;
CREATE TABLE `appointments`  (
  `appointment_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NULL DEFAULT NULL,
  `doctor_id` int NULL DEFAULT NULL,
  `appointment_date` timestamp NOT NULL,
  `status` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `notes` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`appointment_id`) USING BTREE,
  INDEX `doctor_id`(`doctor_id` ASC) USING BTREE,
  INDEX `idx_appointments_user`(`user_id` ASC) USING BTREE,
  INDEX `idx_appointments_date`(`appointment_date` ASC) USING BTREE,
  CONSTRAINT `appointments_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `appointments_ibfk_2` FOREIGN KEY (`doctor_id`) REFERENCES `doctors` (`doctor_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `status_check` CHECK (`status` in (_utf8mb4'scheduled',_utf8mb4'completed',_utf8mb4'cancelled'))
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of appointments
-- ----------------------------
INSERT INTO `appointments` VALUES (1, 1, 1, '2024-01-20 10:00:00', 'scheduled', '首次咨询', '2025-02-26 16:54:00');
INSERT INTO `appointments` VALUES (2, 2, 3, '2024-01-21 14:30:00', 'scheduled', '复诊', '2025-02-26 16:54:00');
INSERT INTO `appointments` VALUES (3, 3, 2, '2024-01-22 09:30:00', 'scheduled', '常规检查', '2025-02-26 16:54:00');
INSERT INTO `appointments` VALUES (4, 4, 4, '2024-01-23 15:00:00', 'scheduled', '心理咨询', '2025-02-26 16:54:00');
INSERT INTO `appointments` VALUES (5, 5, 5, '2024-01-24 11:00:00', 'scheduled', '中医调理', '2025-02-26 16:54:00');

-- ----------------------------
-- Table structure for chat_history
-- ----------------------------
DROP TABLE IF EXISTS `chat_history`;
CREATE TABLE `chat_history`  (
  `chat_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NULL DEFAULT NULL,
  `conversation_id` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `message` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `is_user` tinyint(1) NOT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`chat_id`) USING BTREE,
  INDEX `idx_chat_history_user`(`user_id` ASC) USING BTREE,
  CONSTRAINT `chat_history_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of chat_history
-- ----------------------------
INSERT INTO `chat_history` VALUES (1, 1, 'conv1', '我最近经常头痛，该怎么办？', 1, '2025-02-26 16:53:59');
INSERT INTO `chat_history` VALUES (2, 2, 'conv2', '建议您记录头痛发生的时间和情况', 0, '2025-02-26 16:53:59');
INSERT INTO `chat_history` VALUES (3, 3, 'conv3', '我的经期不规律正常吗？', 1, '2025-02-26 16:53:59');
INSERT INTO `chat_history` VALUES (4, 4, 'conv4', '更年期的症状会持续多久？', 1, '2025-02-26 16:53:59');
INSERT INTO `chat_history` VALUES (5, 5, 'conv5', '请问如何缓解痛经？', 1, '2025-02-26 16:53:59');

-- ----------------------------
-- Table structure for cycle_records
-- ----------------------------
DROP TABLE IF EXISTS `cycle_records`;
CREATE TABLE `cycle_records`  (
  `record_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NULL DEFAULT NULL,
  `cycle_start_date` date NOT NULL,
  `cycle_end_date` date NULL DEFAULT NULL,
  `symptoms` json NULL,
  `mood` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `notes` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`record_id`) USING BTREE,
  INDEX `idx_cycle_records_user`(`user_id` ASC) USING BTREE,
  CONSTRAINT `cycle_records_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of cycle_records
-- ----------------------------
INSERT INTO `cycle_records` VALUES (1, 1, '2024-01-01', '2024-01-05', '[\"腹痛\", \"疲劳\"]', '平静', '正常周期', '2025-02-26 16:53:59');
INSERT INTO `cycle_records` VALUES (2, 2, '2024-01-10', '2024-01-15', '[\"头痛\", \"情绪波动\"]', '焦虑', '症状较重', '2025-02-26 16:53:59');
INSERT INTO `cycle_records` VALUES (3, 3, '2024-01-05', '2024-01-09', '[\"轻微不适\"]', '愉快', '状态良好', '2025-02-26 16:53:59');
INSERT INTO `cycle_records` VALUES (4, 4, '2024-01-15', '2024-01-20', '[\"潮热\", \"失眠\"]', '疲惫', '更年期症状', '2025-02-26 16:53:59');
INSERT INTO `cycle_records` VALUES (5, 5, '2024-01-08', '2024-01-12', '[\"腰痛\"]', '正常', '轻微不适', '2025-02-26 16:53:59');

-- ----------------------------
-- Table structure for daily_cycle_status
-- ----------------------------
DROP TABLE IF EXISTS `daily_cycle_status`;
CREATE TABLE `daily_cycle_status`  (
  `status_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `date` date NOT NULL,
  `symptoms` json NULL,
  `mood` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `notes` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`status_id`) USING BTREE,
  INDEX `idx_daily_cycle_status_user`(`user_id` ASC) USING BTREE,
  CONSTRAINT `daily_cycle_status_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of daily_cycle_status
-- ----------------------------
INSERT INTO `daily_cycle_status` VALUES (1, 1, '2024-01-01', '[\"腹痛\", \"疲劳\"]', '平静', '正常周期', '2025-02-26 16:53:59');
INSERT INTO `daily_cycle_status` VALUES (2, 1, '2024-01-02', '[\"头痛\"]', '焦虑', '轻微不适', '2025-02-26 16:53:59');
INSERT INTO `daily_cycle_status` VALUES (3, 2, '2024-01-03', '[\"疲劳\"]', '愉快', '状态良好', '2025-02-26 16:53:59');
INSERT INTO `daily_cycle_status` VALUES (4, 3, '2024-01-04', '[\"潮热\", \"失眠\"]', '疲惫', '更年期症状', '2025-02-26 16:53:59');
INSERT INTO `daily_cycle_status` VALUES (5, 4, '2024-01-05', '[\"腰痛\"]', '正常', '轻微不适', '2025-02-26 16:53:59');

-- ----------------------------
-- Table structure for doctors
-- ----------------------------
DROP TABLE IF EXISTS `doctors`;
CREATE TABLE `doctors`  (
  `doctor_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `specialty` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `availability` json NULL,
  `contact_info` json NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`doctor_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of doctors
-- ----------------------------
INSERT INTO `doctors` VALUES (1, '张医生', '妇科', '{\"周一\": \"9:00-17:00\", \"周三\": \"9:00-17:00\"}', '{\"电话\": \"123-4567\", \"邮箱\": \"zhang@hospital.com\"}', '2025-02-26 16:53:59');
INSERT INTO `doctors` VALUES (2, '李医生', '内分泌科', '{\"周二\": \"9:00-17:00\", \"周四\": \"9:00-17:00\"}', '{\"电话\": \"123-4568\", \"邮箱\": \"li@hospital.com\"}', '2025-02-26 16:53:59');
INSERT INTO `doctors` VALUES (3, '王医生', '妇科', '{\"周三\": \"9:00-17:00\", \"周五\": \"9:00-17:00\"}', '{\"电话\": \"123-4569\", \"邮箱\": \"wang@hospital.com\"}', '2025-02-26 16:53:59');
INSERT INTO `doctors` VALUES (4, '赵医生', '心理咨询', '{\"周一\": \"13:00-17:00\", \"周五\": \"9:00-12:00\"}', '{\"电话\": \"123-4570\", \"邮箱\": \"zhao@hospital.com\"}', '2025-02-26 16:53:59');
INSERT INTO `doctors` VALUES (5, '刘医生', '中医科', '{\"周二\": \"9:00-17:00\", \"周四\": \"9:00-17:00\"}', '{\"电话\": \"123-4571\", \"邮箱\": \"liu@hospital.com\"}', '2025-02-26 16:53:59');

-- ----------------------------
-- Table structure for symptom_logs
-- ----------------------------
DROP TABLE IF EXISTS `symptom_logs`;
CREATE TABLE `symptom_logs`  (
  `log_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NULL DEFAULT NULL,
  `log_date` date NOT NULL,
  `symptom_type` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `severity` int NULL DEFAULT NULL,
  `notes` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`log_id`) USING BTREE,
  INDEX `idx_symptom_logs_user`(`user_id` ASC) USING BTREE,
  CONSTRAINT `symptom_logs_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `severity_check` CHECK (`severity` between 1 and 5)
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of symptom_logs
-- ----------------------------
INSERT INTO `symptom_logs` VALUES (1, 1, '2024-01-01', '头痛', 3, '午后加重', '2025-02-26 16:53:59');
INSERT INTO `symptom_logs` VALUES (2, 2, '2024-01-10', '腹痛', 4, '需要止痛药', '2025-02-26 16:53:59');
INSERT INTO `symptom_logs` VALUES (3, 3, '2024-01-05', '疲劳', 2, '休息后好转', '2025-02-26 16:53:59');
INSERT INTO `symptom_logs` VALUES (4, 4, '2024-01-15', '失眠', 3, '睡眠质量差', '2025-02-26 16:53:59');
INSERT INTO `symptom_logs` VALUES (5, 5, '2024-01-08', '情绪波动', 2, '轻微影响', '2025-02-26 16:53:59');

-- ----------------------------
-- Table structure for user_profiles
-- ----------------------------
DROP TABLE IF EXISTS `user_profiles`;
CREATE TABLE `user_profiles`  (
  `profile_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NULL DEFAULT NULL,
  `birth_date` date NULL DEFAULT NULL,
  `menstrual_status` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `health_conditions` json NULL,
  `privacy_settings` json NULL,
  `last_updated` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`profile_id`) USING BTREE,
  UNIQUE INDEX `user_id`(`user_id` ASC) USING BTREE,
  CONSTRAINT `user_profiles_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user_profiles
-- ----------------------------
INSERT INTO `user_profiles` VALUES (1, 1, '1990-01-15', 'regular', '[\"偏头痛\", \"轻度贫血\"]', '{\"data_sharing\": false}', '2025-02-26 16:53:59');
INSERT INTO `user_profiles` VALUES (2, 2, '1988-03-22', 'irregular', '[\"内分泌失调\"]', '{\"data_sharing\": true}', '2025-02-26 16:53:59');
INSERT INTO `user_profiles` VALUES (3, 3, '1995-07-08', 'regular', '[\"痛经\"]', '{\"data_sharing\": true}', '2025-02-26 16:53:59');
INSERT INTO `user_profiles` VALUES (4, 4, '1992-11-30', 'menopause', '[\"更年期症状\"]', '{\"data_sharing\": false}', '2025-02-26 16:53:59');
INSERT INTO `user_profiles` VALUES (5, 5, '1993-05-17', 'regular', '[\"无\"]', '{\"data_sharing\": true}', '2025-02-26 16:53:59');

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users`  (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `password_hash` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`user_id`) USING BTREE,
  UNIQUE INDEX `email`(`email` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of users
-- ----------------------------
INSERT INTO `users` VALUES (1, 'user1@example.com', 'hash1', '2025-02-26 16:53:59');
INSERT INTO `users` VALUES (2, 'user2@example.com', 'hash2', '2025-02-26 16:53:59');
INSERT INTO `users` VALUES (3, 'user3@example.com', 'hash3', '2025-02-26 16:53:59');
INSERT INTO `users` VALUES (4, 'user4@example.com', 'hash4', '2025-02-26 16:53:59');
INSERT INTO `users` VALUES (5, 'user5@example.com', 'hash5', '2025-02-26 16:53:59');

SET FOREIGN_KEY_CHECKS = 1;
