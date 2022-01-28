pragma solidity ^0.8.9;

contract stock {
    int public currentStock = 0;
    uint public entries = 0;

    struct stockEntry {
        uint id;
        int amount;
        bool condition;
    }

    mapping(uint => stockEntry) public stockRecord;

    function enterstock(uint id, int amount, bool conditon) public {
        currentStock = currentStock + amount;
        stockRecord[entries] = stockEntry(id, amount,conditon);
        entries++;
    }

    function return_data(uint entry) public view returns (stockEntry memory) {
        stockEntry memory val = stockRecord[entry];
        return val;
    }
    // function return_entries() public view returns (uint) {
    //     uint numb =  entries;
    //     return numb;
    // }
}