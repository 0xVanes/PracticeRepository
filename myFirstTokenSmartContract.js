// SPDX-License-Identifier: MIT
pragma solidity 0.8.26;

contract MyToken {
    uint256 public totalSupply;
    uint256 public feePercentage;  // Fee percentage for transactions
    address public feeRecipient;  // Address to receive the fees

    string constant public name = "Herring";
    string constant public symbol = "HRR";
    uint8 constant public decimals = 18;  // Correct naming for ERC-20 compliance

    mapping(address => uint256) public balance;  // Should be public to allow visibility
    mapping(address => mapping(address => uint256)) public allowance;  // Changed variable name for clarity

    // Correct event names to follow Solidity naming conventions
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Transfer(address indexed from, address indexed to, uint256 value);

    constructor(uint256 _initialSupply, address _feeRecipient, uint256 _feePercentage) {
        totalSupply = _initialSupply;
        feeRecipient = _feeRecipient;  // Initialize with an address passed to the constructor
        feePercentage = _feePercentage;  // Initialize with a percentage (as an integer out of 100)
        
        balance[msg.sender] = _initialSupply;
        emit Transfer(address(0), msg.sender, _initialSupply);
    }

    function transfer(address to, uint256 value) public returns (bool success) {
        uint256 fee = calculateFee(value);
        uint256 amountToSend = value - fee;
        require(balance[msg.sender] >= value, "Insufficient Balance");
        balance[msg.sender] -= value;
        balance[to] += amountToSend;
        balance[feeRecipient] += fee;  // Send the fee to the fee recipient
        emit Transfer(msg.sender, to, value);  // Corrected `from` to `msg.sender`
        return true;
    }

    function calculateFee(uint256 amount) public view returns (uint256) {
        return amount * feePercentage / 100;
    }

    function approve(address spender, uint256 value) public returns (bool success) {
        allowance[msg.sender][spender] = value;
        emit Approval(msg.sender, spender, value);
        return true;
    }

    function transferFrom(address from, address to, uint256 value) public returns (bool success) {
        require(value <= balance[from], "Insufficient Balance");
        require(value <= allowance[from][msg.sender], "Allowance exceeded");
        balance[from] -= value;
        balance[to] += value;
        allowance[from][msg.sender] -= value;
        emit Transfer(from, to, value);
        return true;
    }
}
