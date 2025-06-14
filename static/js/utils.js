function show() {
  const trigger = $(this);
  const target = trigger.data("action-target");

  if (["block", "flex"].includes($(target).css("display"))) {
    $(target).hide();
    return;
  }

  $(target).show();
}

function hide() {
  const trigger = $(this);
  const target = trigger.data("action-target");

  $(target).hide();
}

function close() {
  const trigger = $(this);
  const target = trigger.data("action-target");

  $(target).remove();
}

$(document).ready(() => {
  $(document).on("click", "[data-action='show']", show);
  $(document).on("click", "[data-action='hide']", hide);
  $(document).on("click", "[data-action='close']", close);
});
