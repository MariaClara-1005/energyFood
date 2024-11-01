document.addEventListener('DOMContentLoaded', () => {
    const cartItems = [
        { id: 1, name: 'Coxinha', price: 3.50, quantity: 1 },
        { id: 2, name: 'Risole', price: 4.50, quantity: 1 },
    ];

    const cartItemsContainer = document.getElementById('items');
    const totalDisplay = document.getElementById('total');

    function renderCart() {
        cartItemsContainer.innerHTML = '';
        let total = 0;

        cartItems.forEach(item => {
            const li = document.createElement('li');
            li.className = 'carrinho-item';
            li.innerHTML = `
                <div class="imagem">
                    <img src="src/${item.name.toLowerCase()}.png" alt="${item.name}">
                </div>
                <div class="info">
                    <h4>${item.name}</h4>
                    <div class="detalhes">
                        <div class="colaborador">
                            <i class='bx bx-body'></i>
                            <span>Colaborador</span>
                        </div>
                        <div class="status">
                            <i class='bx bx-package'></i>
                            <span>Disponibilidade</span>
                        </div>
                    </div>
                    <div class="valor-da-doacao">
                        <p>R$ ${item.price.toFixed(2)}</p>
                        <div class="contador">
                            <button class='bx bx-minus' onclick="decreaseQuantity(${item.id})"></button>
                            <span>${item.quantity}</span>
                            <button class='bx bx-plus' onclick="increaseQuantity(${item.id})"></button>
                        </div>
                    </div>
                </div>
            `;
            cartItemsContainer.appendChild(li);
            total += item.price * item.quantity;
        });

        totalDisplay.textContent = `R$ ${total.toFixed(2)}`;
    }

    window.decreaseQuantity = (productId) => {
        const item = cartItems.find(item => item.id === productId);
        if (item.quantity > 0) {
            item.quantity--;
        }
        renderCart();
    };

    window.increaseQuantity = (productId) => {
        const item = cartItems.find(item => item.id === productId);
        item.quantity++;
        renderCart();
    };

    document.getElementById('checkout').addEventListener('click', () => {
        alert('Redirecionando para o pagamento!');
        cartItems.length = 0;
        renderCart();
    });

    renderCart();
});
