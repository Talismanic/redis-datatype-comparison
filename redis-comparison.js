var redis = require('redis');
var client = redis.createClient();
var randomstring = require("randomstring");
var datetime = require('node-datetime');
var dt = datetime.create();


function setString(){
    var str = randomstring.generate(25);
    var usr = randomstring.generate(11);


    return new Promise(function(resolve, reject){
        client.set(usr, str, function(err, res ){
            if(err) reject(err);
            else{
                resolve(usr);
            }

        })
    })
}


function printResult(start_time){
    var start_time = start_time;
    var end_time = Date.now()/1000;
    var diff = end_time - start_time;
    console.log(diff);


}

function main(){

    var promises = [];

    var start_time = Date.now()/1000;

    for(var i =0; i< 100; i++){
        var initializePromise = setString();
        promises.push(initializePromise);
        
    }

    Promise.all(promises).then(printResult(start_time));

}


main();


// async function setBulkString(){
//     var consts = [];
//     var start_time = Date.now()/1000
//     for (var i= 0; i<100; i++){
//         consts.push(await setString());

//     }

//     return start_time;
// }

// setBulkString().then((result)=>{
//     printResult(result);
// });