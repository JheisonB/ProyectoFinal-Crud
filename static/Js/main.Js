const btnDelete = document.querySelectorAll('.btn-delete')
if (btnDelete) {
    const btnArray = Array.from(btnDelete);
    btnArray.forEach((btn) => {
        btn.addEventListener('Click', ( e) =>{
            if (! confirm('Are you sure Yo want to delete it?'))
            e.preventDefault();
        });
    } );
}
