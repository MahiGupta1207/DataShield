
USE datashield;
CREATE OR REPLACE VIEW vendor_vulnerability_summary AS
SELECT
vendorProject,
COUNT(*) AS total_vulnerabilities
FROM vulnerabilities
GROUP BY vendorProject;
CREATE OR REPLACE VIEW ransomware_summary AS
SELECT
knownRansomwareCampaignUse,
COUNT(*) AS total_vulnerabilities
FROM vulnerabilities
GROUP BY knownRansomwareCampaignUse;
DROP PROCEDURE IF EXISTS get_top_vendors;
DELIMITER //
CREATE PROCEDURE get_top_vendors()
BEGIN
SELECT
vendorProject,
COUNT(*) AS total_vulnerabilities
FROM vulnerabilities
GROUP BY vendorProject
ORDER BY total_vulnerabilities DESC
LIMIT 10;
END //
DELIMITER ;
