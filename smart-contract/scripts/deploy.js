async function main() {
    const Contract = await ethers.getContractFactory("CertificateRegistry");
    const contract = await Contract.deploy();
    await contract.waitForDeployment();
  
    console.log("Contract deployed at:", await contract.getAddress());
  }
  
  main();
  