var stock = artifacts.require("stock.sol");

module.exports = function(deployer) {
  deployer.deploy(stock);
};
