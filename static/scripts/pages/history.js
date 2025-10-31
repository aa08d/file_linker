document.querySelectorAll('tbody td:last-child').forEach(cell => {
	cell.addEventListener('click', () => {
		const text = cell.textContent;
		navigator.clipboard.writeText(text).then(() => {
			alert('Текст скопирован: ' + text);
		}).catch(() => {
			alert('Ошибка копирования');
		});
	})
});