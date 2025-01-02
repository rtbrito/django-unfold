(function ($) {
    'use strict';

    $(function () {

        $('#content-main').on('click', '.reset-link', function (e) {
            e.preventDefault();

            const field_selector = this.dataset.fieldId.replace(/ /g, "\\ ")
            const field = $('#' + field_selector);
            const fieldType = this.dataset.fieldType;

            if (fieldType === 'checkbox') {
                field.prop('checked', this.dataset.default === 'true');
            } else if (fieldType === 'date') {
                const defaultDate = new Date(this.dataset.default * 1000);
                $('#' + this.dataset.fieldId).val(defaultDate.strftime(get_format('DATE_INPUT_FORMATS')[0]));
            } else if (fieldType === 'datetime') {
                const defaultDate = new Date(this.dataset.default * 1000);
                $('#' + this.dataset.fieldId + '_0').val(defaultDate.strftime(get_format('DATE_INPUT_FORMATS')[0]));
                $('#' + this.dataset.fieldId + '_1').val(defaultDate.strftime(get_format('TIME_INPUT_FORMATS')[0]));
            } else {
                field.val(this.dataset.default);
            }
        });

        // Function for stylising elements on the page
        $('.min-w-sidebar').parent().removeClass('hidden');
        $('.min-w-sidebar').parent().removeClass('xl:hidden');
        $('.min-w-sidebar').parent().removeClass('xl\:hidden');

        $('#site-name').parent().removeClass('h-10').addClass('flex-col h-auto');

        $('label[for="id_expected_location"]').addClass('font-semibold mb-2 text-font-important-light text-sm');

        $('textarea, input[type=text]')
            .addClass('border bg-white font-medium min-w-20 rounded-md shadow-sm text-font-default-light text-sm')
            .addClass('focus:ring focus:ring-primary-300 focus:border-primary-600 focus:outline-none')
            .addClass('group-[.errors]:border-red-600 group-[.errors]:focus:ring-red-200')
            .addClass('px-3 py-2 w-full max-w-2xl')
            .attr('rows', 3);
    });
})(django.jQuery);
