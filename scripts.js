// scripts.js

document.querySelectorAll('.sidebar ul li').forEach(item => {
    item.addEventListener('click', () => {
        alert('Anda mengklik ' + item.textContent);
    });
});
