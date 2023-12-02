$(document).ready(function() {
    $('#add-drug').click(function() {
        var count = $('.drug-form').length;
        var newForm = $('.drug-form:last').clone();
        newForm.find('input, select').each(function() {
            var newName = this.name.replace('-' + (count - 1) + '-', '-' + count + '-');
            this.name = newName;
            this.value = '';
        });
        newForm.insertAfter('.drug-form:last');
    });
});