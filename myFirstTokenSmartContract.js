// SPDX-License-Identifier: MIT
pragma solidity 0.8.26;

contract MyToken {
    address public owner; // set the contract deployer as owner
    modifier onlyOwner(){ // restrict access to onlyOwner
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    uint256 public totalSupply;
    uint256 public feePercentage;  // Fee percentage for transactions
    address public feeRecipient;  // Address to receive the fees

    string public name;
    string public symbol;
    uint8 immutable public decimals;

    mapping(address => uint256) public balance;
    mapping(address => mapping(address => uint256)) public allowance; 

    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Transfer(address indexed from, address indexed to, uint256 value);

    constructor(string memory _name, string memory _symbol, uint8 _decimals, uint256 _initialSupply, address _feeRecipient, uint256 _feePercentage) {
        owner = msg.sender;
        
        name = _name;
        symbol = _symbol;
        decimals = _decimals;
        
        totalSupply = _initialSupply;
        feeRecipient = _feeRecipient;  // Initialize with an address passed to the constructor
        feePercentage = _feePercentage;  // Initialize with a percentage (as an integer out of 100)
        
        balance[msg.sender] = _initialSupply;
        emit Transfer(address(0), msg.sender, _initialSupply);
    }

    function mint(address to, uint256 value) external onlyOwner{
        _mint(to, value);
    }

    function _mint(address to, uint256 value) internal {
        require(to != address(0), "Mint to the zero address");
        totalSupply += value;
        balance[to] += value;
        emit Transfer(address(0), to, value);
    }

    function burn(uint256 value) external onlyOwner{
        _burn(msg.sender, value);
    }

    function _burn(address from, uint256 value) internal{
        require(from != address(0), "Burned from the zero address");
        require(balance[from] >= value, "Burn amount exceeds balance");
        totalSupply -= value;
        balance[from] -= value;
        emit Transfer(from, address(0), value);
    }

    function deposit() public payable {
        uint256 tokensToMint = msg.value; // Assuming 1 token per wei
        balance[msg.sender] += tokensToMint;
        totalSupply += tokensToMint;
        emit Transfer(address(0), msg.sender, tokensToMint);
    }

    function redeem(uint256 tokenAmount) public {
    require(balance[msg.sender] >= tokenAmount, "Insufficient token balance");
    require(allowance[msg.sender][address(this)] >= tokenAmount, "Allowance too low");
    transferFrom(msg.sender, address(this), tokenAmount);

    _burn(address(this), tokenAmount); // Burn the tokens internally

    (bool sent, ) = msg.sender.call{value: tokenAmount}(""); // Send Ether back to the sender
    require(sent, "Failed to send Ether");
    }


    function transfer(address to, uint256 value) public returns (bool success) {
        uint256 fee = calculateFee(value);
        uint256 amountToSend = value - fee;
        require(balance[msg.sender] >= value, "Insufficient Balance");
        balance[msg.sender] -= value;
        balance[to] += amountToSend;
        balance[feeRecipient] += fee;  // Send the fee to the fee recipient
        emit Transfer(msg.sender, to, value);
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
