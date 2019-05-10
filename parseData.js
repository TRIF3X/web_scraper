const fs = require('fs')
// change file destination here of the data you want to parse
let data = require('./WomensData/womenTops.json')

// parses the data set used
function parseData(data) {

    let mapped = data.map(data => {
        const {name, price, image} = data;
        return ({
            name: name.slice(1, -1),
            price,
            'image': image === null ? 'https:' + data['image-alt']: 'https:' + image
        })
    })
    
    return mapped;
}

let completeData = parseData(data)

// writes to file the new updated data
fs.writeFile('./ParsedData/Womens/tops.js', JSON.stringify(completeData), (err) => {
    if (err) {
        console.log(err)
    }
})

