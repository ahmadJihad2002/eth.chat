//SPDX-License-Identifier:MIT
pragma solidity >= 0.3.0 <0.8.17;

contract chat {

    // Stores the default name of an user and her friends info
    struct user {
        string name;
        friend[] friendList;
    }

    // Each friend is identified by its address and name assigned by the second party
    struct friend {
        address pubkey;
        string name;

    }

    // message construct stores the single chat message and its metadata
    struct message {
        address sender;
        uint256 timestamp;
        string msg;
    }
    struct point   {
        string x;
        string y;

    }

    // Collection of users registered on the application
    mapping(address => point) public public_key_points;
    mapping(address => user) public userList;
    // Collection of messages communicated in a channel between two users
    mapping(bytes32 => message[]) allMessages; // key : Hash(user1,user2)

    // It checks whether a user(identified by its public key)
    // has created an account on this application or not
    function checkUserExists(address pubkey) public view returns (bool) {
        return bytes(userList[pubkey].name).length > 0;
    }


    // Registers the caller(msg.sender) to our app with a non-empty username
    function createAccount(string calldata name, address sender ,string memory x,string memory y ) external returns (bool){
        require(checkUserExists(sender) == false, "User already exists!");
        require(bytes(name).length > 0, "Username cannot be empty!");
        userList[sender].name = name;
        add_public_key_points( sender, x, y) ;

        return true;
    }

    // Returns the default name provided by an user
    function getUsername(address pubkey) external view returns (string memory) {
        require(checkUserExists(pubkey), "User is not registered!");
        return userList[pubkey].name;
    }

    // Adds new user as your friend with an associated nickname
    function addFriend(address friendAddress, string calldata name,address sender) public  {
        // require(checkUserExists(msg.sender), "Create an account first!");
        // require(checkUserExists(friendAddress), "User is not registered!");
        //  require(msg.sender!= friendAddress, "Users cannot add themselves as friends!");
        require(checkAlreadyFriends(msg.sender, friendAddress)==false, "These users are already friends!");

        _addFriend(sender, friendAddress, name);
        _addFriend(friendAddress,sender, userList[sender].name);

    }

    function add_public_key_points( address sender,string memory x,string memory y) internal  {
        point memory newPoints = point(x,y);
        public_key_points[sender]=newPoints;

    }


    function get_public_key_points( address userAddress ) public view returns(point memory) {
         return public_key_points[userAddress];

    }





    // Checks if two users are already friends or not
    function checkAlreadyFriends(address pubkey1, address pubkey2) internal view returns (bool) {

        if (userList[pubkey1].friendList.length > userList[pubkey2].friendList.length)
        {
            address tmp = pubkey1;
            pubkey1 = pubkey2;
            pubkey2 = tmp;
        }

        for (uint i = 0; i < userList[pubkey1].friendList.length; ++i)
        {
            if (userList[pubkey1].friendList[i].pubkey == pubkey2)
                return true;
        }
        return false;
    }

    // A helper function to update the friendList
    function _addFriend(address me, address friend_key, string memory name) internal {
        friend memory newFriend = friend(friend_key, name);
        userList[me].friendList.push(newFriend);
    }

    // Returns list of friends of the sender
    function getMyFriendList(address sender) external view returns (friend[] memory) {
        return userList[sender].friendList;
    }

    // Returns a unique code for the channel created between the two users
    // Hash(key1,key2) where key1 is lexicographically smaller than key2
    function _getChatCode(address pubkey1, address pubkey2) internal pure returns (bytes32) {
        if (pubkey1 < pubkey2)
            return keccak256(abi.encodePacked(pubkey1, pubkey2));
        else
            return keccak256(abi.encodePacked(pubkey2, pubkey1));
    }

    // Sends a new message to a given friend
    function sendMessage(address friend_key, string calldata _msg,address sender) external {
        // require(checkUserExists(msg.sender), "Create an account first!");
        //require(checkUserExists(friend_key), "User is not registered!");
        //require(checkAlreadyFriends(msg.sender,friend_key), "You are not friends with the given user");

        bytes32 chatCode = _getChatCode( sender, friend_key);
        message memory newMsg = message(sender, block.timestamp, _msg);
        allMessages[chatCode].push(newMsg);
    }

    // Returns all the chat messages communicated in a channel
    function readMessage(address friend_key,address sender) external view returns (message[] memory) {
        bytes32 chatCode = _getChatCode(sender, friend_key);
        return allMessages[chatCode];
    }

 }




