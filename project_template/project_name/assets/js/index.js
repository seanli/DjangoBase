var serialize_form = function($form) {
  data = {};
  $form.find('input').each(function() {
    var name = $(this).attr('name');
    data[name] = $(this).val();
  });
  return data;
};

$(document).ready(function() {

  $('#form-signup').submit(function() {
    $this = $(this);
    var data = serialize_form($this);
    $.ajax({
      type: 'POST',
      url: '/api/user/add/',
      data: data,
      success: function(data) {
        $('.field-error').remove();
        if (!data.errors) {
          window.location.reload();
        } else {
          for (var name in data.errors) {
            if (data.errors.hasOwnProperty(name)) {
              $this.find('input[name="' + name + '"]').after('<div class="field-error">' + data.errors[name] + '</div>');
            }
          }
        }
      }
    });
    return false;
  });

  $('#form-login').submit(function() {
    $this = $(this);
    var data = serialize_form($this);
    $.ajax({
      type: 'POST',
      url: '/api/user/login/',
      data: data,
      success: function(data) {
        $('.field-error').remove();
        if (!data.errors) {
          window.location.reload();
        } else {
          for (var name in data.errors) {
            if (data.errors.hasOwnProperty(name)) {
              if (name != '__all__') {
                $this.find('input[name="' + name + '"]').after('<div class="field-error">' + data.errors[name] + '</div>');
              } else {
                $this.find('button[type="submit"]').before('<div class="field-error">' + data.errors[name] + '</div>');
              }
            }
          }
        }
      }
    });
    return false;
  });

});
