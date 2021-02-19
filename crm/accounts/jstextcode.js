let array = [1,2,3,5,6]
console.log(array)

let index = array.findIndex(function(eachItem) {
		if (eachItem === 5) {
			return true
		}
	}) 
console.log(index)
