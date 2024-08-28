
document.addEventListener('DOMContentLoaded', function () {
    const invoiceItemsContainer = document.getElementById('invoice-items-container');
    const addItemButton = document.getElementById('add-item');
    const invoiceTotalInput = document.getElementById('invoice-total');

    // Function to calculate total for each item row
    function calculateRowTotal(row) {
        const unitPrice = row.querySelector('.unit-price').value;
        const quantity = row.querySelector('.quantity').value;
        const total = row.querySelector('.total');

        const calculatedTotal = (unitPrice * quantity).toFixed(2);
        total.value = calculatedTotal;

        calculateInvoiceTotal();
    }

    // Function to calculate the total sum of all item totals
    function calculateInvoiceTotal() {
        let invoiceTotal = 0.0;
        const allTotals = document.querySelectorAll('.total');
        allTotals.forEach(function (total) {
            invoiceTotal += parseFloat(total.value) || 0;
        });
        invoiceTotalInput.value = invoiceTotal.toFixed(2);
        document.getElementById('{{ form.total_amount.auto_id }}').value = invoiceTotal.toFixed(2);
    }

    // Event listener to add a new row
    addItemButton.addEventListener('click', function () {
        const newRow = document.createElement('div');
        newRow.classList.add('row', 'invoice-item-row');
        newRow.innerHTML = `
          <div class="col-8">
              <input type="text" class="form-control" name="description[]" placeholder="Description">
          </div>
          <div class="col-1">
              <input type="number" class="form-control unit-price" name="unit_price[]" placeholder="Unit Price" step="0.01">
          </div>
          <div class="col-1">
              <input type="number" class="form-control quantity" name="quantity[]" placeholder="Quantity">
          </div>
          <div class="col-1">
              <input type="text" class="form-control total" name="total[]" placeholder="Total" readonly>
          </div>
          <div class="col-1">
              <button type="button" class="btn btn-danger remove-item">Remove</button>
          </div>
        `;
        invoiceItemsContainer.appendChild(newRow);

        // Attach event listeners to the new inputs
        newRow.querySelector('.unit-price').addEventListener('input', function () {
            calculateRowTotal(newRow);
        });
        newRow.querySelector('.quantity').addEventListener('input', function () {
            calculateRowTotal(newRow);
        });
    });

    // Event delegation for removing rows
    invoiceItemsContainer.addEventListener('click', function (event) {
        if (event.target.classList.contains('remove-item')) {
            event.target.closest('.invoice-item-row').remove();
            calculateInvoiceTotal();
        }
    });

    // Attach event listeners to the initial row inputs
    invoiceItemsContainer.querySelectorAll('.unit-price, .quantity').forEach(function (input) {
        input.addEventListener('input', function () {
            calculateRowTotal(input.closest('.row'));
        });
    });
});
