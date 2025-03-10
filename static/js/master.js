const s_list = document.getElementById('dates')


function createTableWithInnerHTML(data) {


    let tableHTML = document.getElementById('dummy')

    data.forEach(item => {
        let tr = document.createElement('tr')
        item.forEach(value => {
			let td = document.createElement('td')
			td.textContent = value
			tr.appendChild(td)
        });
        tableHTML.appendChild(tr)
    });
}

s_list.addEventListener('change', function(ev){
	const xhr = new XMLHttpRequest()
	xhr.open("GET", "/api/date/" + ev.target.value, true);
	xhr.send(null);
	xhr.onload = function() {
		document.getElementById('dummy').innerHTML = ''
		createTableWithInnerHTML(JSON.parse(xhr.response))
};
})
