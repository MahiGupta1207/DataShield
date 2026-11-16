USE datashield;
SELECT COUNT(*) AS total_vulnerabilities
FROM vulnerabilities;
SELECT vendorProject, COUNT(*) AS total_vulnerabilities
FROM vulnerabilities
GROUP BY vendorProject
ORDER BY total_vulnerabilities DESC
LIMIT 10;
SELECT knownRansomwareCampaignUse, COUNT(*) AS total
FROM vulnerabilities
GROUP BY knownRansomwareCampaignUse;
SELECT YEAR(dateAdded) AS vulnerability_year,
COUNT(*) AS total_vulnerabilities
FROM vulnerabilities
GROUP BY YEAR(dateAdded)
ORDER BY vulnerability_year;
SELECT vendorProject, COUNT(*) AS total_vulnerabilities
FROM vulnerabilities
GROUP BY vendorProject
HAVING COUNT(*) > 10
ORDER BY total_vulnerabilities DESC;
SELECT cveID, vendorProject, product, dateAdded
FROM vulnerabilities
ORDER BY dateAdded DESC
LIMIT 10;
SELECT COUNT(*) AS ransomware_vulnerabilities
FROM vulnerabilities
WHERE knownRansomwareCampaignUse = 'Known';
