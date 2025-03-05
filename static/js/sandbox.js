const data_input = document.getElementById('data')


function createTableWithInnerHTML(data) {


    let tableHTML = document.getElementById('dummy')
	tableHTML.innerHTML = ''

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

data_input.addEventListener("change", (event) => {
createTableWithInnerHTML(JSON.parse(data_input.value))

});

