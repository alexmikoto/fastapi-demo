// This script is horrible but you do what you can
"use strict";

async function load_persons() {
	const tbl = document.querySelector("#person-crud > table");
	const template = document.querySelector("#person-crud-template");

	const r = await fetch("/api/person/");
	const persons = await r.json();
	for (const p of persons) {
		const newRow = template.content.cloneNode(true);
		const cells = newRow.querySelectorAll("td");

		cells[0].textContent = p.id;
		cells[1].textContent = p.name;
		cells[2].textContent = p.email;

		tbl.appendChild(newRow);
	}
}

async function load_vehicles() {
	const tbl = document.querySelector("#vehicle-crud > table");
	const template = document.querySelector("#vehicle-crud-template");

	const r = await fetch("/api/vehicle/");
	const vehicles = await r.json();
	for (const v of vehicles) {
		const newRow = template.content.cloneNode(true);
		const cells = newRow.querySelectorAll("td");

		cells[0].textContent = v.id;
		cells[1].textContent = v.license_plate;
		cells[2].textContent = v.brand;
		cells[3].textContent = v.color;
		cells[4].textContent = v.person.name;

		tbl.appendChild(newRow);
	}
}

async function load_officers() {
	const tbl = document.querySelector("#officer-crud > table");
	const template = document.querySelector("#officer-crud-template");

	const r = await fetch("/api/officer/");
	const officers = await r.json();
	for (const o of officers) {
		const newRow = template.content.cloneNode(true);
		const cells = newRow.querySelectorAll("td");

		cells[0].textContent = o.id;
		cells[1].textContent = o.name;

		tbl.appendChild(newRow);
	}
}

async function main() {
	await load_persons();
	await load_vehicles();
	await load_officers();
}


document.addEventListener("DOMContentLoaded", main, false);
