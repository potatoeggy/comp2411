# raw queries go here

RESET_DB = """
-- Drop tables in reverse order to handle foreign key constraints
DROP TABLE IF EXISTS `WorkerWorksOnActivity`;
DROP TABLE IF EXISTS `CompanyWorksOnActivity`;
DROP TABLE IF EXISTS `Activity`;
DROP TABLE IF EXISTS `ExternalCompany`;
DROP TABLE IF EXISTS `CampusRegionLocation`;
DROP TABLE IF EXISTS `CampusRegion`;
DROP TABLE IF EXISTS `Worker`;
DROP TABLE IF EXISTS `Manager`;
DROP TABLE IF EXISTS `Executive`;
DROP TABLE IF EXISTS `Admin`;

-- CreateTable
CREATE TABLE `Admin` (
    `id` INTEGER NOT NULL AUTO_INCREMENT,

    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- CreateTable
CREATE TABLE `Executive` (
    `id` INTEGER NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(191) NOT NULL,

    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- CreateTable
CREATE TABLE `Manager` (
    `id` INTEGER NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(191) NOT NULL,
    `executive_id` INTEGER NOT NULL,

    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- CreateTable
CREATE TABLE `Worker` (
    `id` INTEGER NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(191) NOT NULL,
    `manager_id` INTEGER NOT NULL,

    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- CreateTable
CREATE TABLE `CampusRegion` (
    `id` INTEGER NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(191) NOT NULL,
    `manager_id` INTEGER NULL,
    `type` ENUM('BUILDING', 'SQUARE', 'GATE') NOT NULL,

    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- CreateTable
CREATE TABLE `CampusRegionLocation` (
    `id` INTEGER NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(191) NOT NULL,
    `root_campus_region_id` INTEGER NOT NULL,

    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- CreateTable
CREATE TABLE `Activity` (
    `id` INTEGER NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(191) NOT NULL,
    `type` ENUM('CLEANING', 'WEATHER_ISSUE', 'AGING_ISSUE') NOT NULL,
    `start_time` DATETIME(3) NOT NULL,
    `end_time` DATETIME(3) NOT NULL,
    `uses_chemicals` BOOLEAN NOT NULL DEFAULT false,
    `location_id` INTEGER NOT NULL,

    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- CreateTable
CREATE TABLE `ExternalCompany` (
    `id` INTEGER NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(191) NOT NULL,

    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- CreateTable
CREATE TABLE `CompanyWorksOnActivity` (
    `activity_id` INTEGER NOT NULL,
    `company_id` INTEGER NOT NULL,

    PRIMARY KEY (`activity_id`, `company_id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- CreateTable
CREATE TABLE `WorkerWorksOnActivity` (
    `worker_id` INTEGER NOT NULL,
    `activity_id` INTEGER NOT NULL,

    PRIMARY KEY (`worker_id`, `activity_id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- AddForeignKey
ALTER TABLE `Manager` ADD CONSTRAINT `Manager_executive_id_fkey` FOREIGN KEY (`executive_id`) REFERENCES `Executive`(`id`) ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `Worker` ADD CONSTRAINT `Worker_manager_id_fkey` FOREIGN KEY (`manager_id`) REFERENCES `Manager`(`id`) ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `CampusRegion` ADD CONSTRAINT `CampusRegion_manager_id_fkey` FOREIGN KEY (`manager_id`) REFERENCES `Manager`(`id`) ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `CampusRegionLocation` ADD CONSTRAINT `CampusRegionLocation_root_campus_region_id_fkey` FOREIGN KEY (`root_campus_region_id`) REFERENCES `CampusRegion`(`id`) ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `Activity` ADD CONSTRAINT `Activity_location_id_fkey` FOREIGN KEY (`location_id`) REFERENCES `CampusRegionLocation`(`id`) ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `CompanyWorksOnActivity` ADD CONSTRAINT `CompanyWorksOnActivity_activity_id_fkey` FOREIGN KEY (`activity_id`) REFERENCES `Activity`(`id`) ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `CompanyWorksOnActivity` ADD CONSTRAINT `CompanyWorksOnActivity_company_id_fkey` FOREIGN KEY (`company_id`) REFERENCES `ExternalCompany`(`id`) ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `WorkerWorksOnActivity` ADD CONSTRAINT `WorkerWorksOnActivity_worker_id_fkey` FOREIGN KEY (`worker_id`) REFERENCES `Worker`(`id`) ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `WorkerWorksOnActivity` ADD CONSTRAINT `WorkerWorksOnActivity_activity_id_fkey` FOREIGN KEY (`activity_id`) REFERENCES `Activity`(`id`) ON DELETE RESTRICT ON UPDATE CASCADE;

"""