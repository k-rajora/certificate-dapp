// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract CertificateRegistry {
    
    struct Certificate {
        bytes32 hash;
        uint256 timestamp;
        string issuer; // example.com
    }

    mapping(string => Certificate) public certificates;

    event CertificateStored(
        string certificateID,
        bytes32 hash,
        uint256 time,
        string issuer
    );

    function storeCertificate(
        string memory certificateID, 
        bytes32 hash, 
        string memory issuer
    ) public {
        require(certificates[certificateID].timestamp == 0, "Certificate already exists");

        certificates[certificateID] = Certificate(hash, block.timestamp, issuer);

        emit CertificateStored(
            certificateID,
            hash,
            block.timestamp,
            issuer
        );
    }

    function getCertificate(string memory certificateID)
        public view
        returns (bytes32, uint256, string memory)
    {
        Certificate memory cert = certificates[certificateID];
        return (cert.hash, cert.timestamp, cert.issuer);
    }
}
