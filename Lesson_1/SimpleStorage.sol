// SPDX-License-Identifier: MIT

//SPDX License Identifier Agregar siempre

pragma solidity ^0.6.0;

contract SimpleStorage{
    
    //this will get initialized to 0!
    uint256 favoriteNumber;
    
    struct People{
        uint256 favoriteNumber;
        string name;
    }
    
    //People public person = People({favoriteNumber: 2,name: "Javier"});
    //Fixed array People[1] public Only one Person
    //Dynamic  array
    //Para llamarlo poner el indice.
    People[] public people;
    mapping(string => uint256) public nameToFavoriteNumber;
    
    //Memory elimina el objeto despues de la ejecucion
    //storage Mantener un parametro por siempre.
    function addPerson(string memory _name, uint256 _favoriteNumber) public{
        //people.push(People({favoriteNumber: _favoriteNumber,name: _name}));
        
        //Recuerda el indice.
        people.push(People( _favoriteNumber, _name));
        nameToFavoriteNumber[_name] = _favoriteNumber;
    }
    
    function store(uint256 _favoriteNumber) public{
        favoriteNumber = _favoriteNumber;
    }
    //view is a non state functions (No transacciona)
    function retrieve() public view returns(uint256){
        return favoriteNumber;
    }
    
    ///AHORA A PONERLO EN LIVE
    

}