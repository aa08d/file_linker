 function copyLink() {
	const copyText = document.getElementById('copyLinkInput');
	copyText.select();
	copyText.setSelectionRange(0, 99999);
	navigator.clipboard.writeText(copyText.value)
	.then(() => alert('Ссылка скопирована!'))
	.catch(() => alert('Ошибка копирования'));
}
