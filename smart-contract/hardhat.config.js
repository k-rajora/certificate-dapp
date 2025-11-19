require("@nomicfoundation/hardhat-toolbox");

module.exports = {
  solidity: "0.8.20",
  defaultNetwork: "amoy",
  networks: {
   amoy: {
      url: process.env.AMOY_RPC,
      accounts: [process.env.PRIVATE_KEY]
    }
  }
};
