$(document).ready(function() {
    $('#add-product').click(function() {
        var count = $('.product-form').length;
        var newForm = $('.product-form:last').clone();
        newForm.find('input, select').each(function() {
            var newName = this.name.replace('-' + (count - 1) + '-', '-' + count + '-');
            this.name = newName;
            this.value = '';
        });
        newForm.insertAfter('.product-form:last');
    });
});