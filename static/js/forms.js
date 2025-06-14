function renderFoodBadges() {
  const trigger = $(this);
  const value = trigger.val();
  const target = trigger.data("target");

  $(target).empty();
  JSON.parse(value).forEach((item) => {
    $(target).append(`
                <div class="badge">x${item.quantity} ${item.name}</div>
                `);
  });
}

function renderBadges() {
  const trigger = $(this);
  const value = trigger.val();
  const target = trigger.data("target");

  $(target).empty();
  JSON.parse(value).forEach((item) => {
    $(target).append(`
              <div class="badge">${item}</div>
              `);
  });
}

function triggerLogForm() {
  $.get("/logs/form", function (response) {
    $("#log-form-container").html(response);
  });
}



$(document).ready(() => {
  $(document).on("click", "[data-action='triggerLogForm']", triggerLogForm); // +
  // $(document).on("click", '[data-action="toggle-badge"]', toggleBadge);
  $(document).on("input", '[data-action="render-food-badges"]', renderFoodBadges); //prettier-ignore
  $(document).on("input", '[data-action="render-badges"]', renderBadges);
});
