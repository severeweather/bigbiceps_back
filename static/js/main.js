function triggerForm() {
  const trigger = $(this);
  const form = trigger.data("form");
  const target = trigger.data("target");

  $.get(`/api/logs/form/${form}`)
    .done((response) => {
      $(target).html(response); // всё ок, отрисуй форму
    })
    .fail((xhr) => {
      if (xhr.status === 401) {
        // пользователь не залогинен → перенаправь на login
        window.location.href = "/auth/login?next=" + window.location.pathname;
      }
    });
}

function getCookie(name) {
  const value = document.cookie
    .split("; ")
    .find((row) => row.startsWith(name + "="));
  return value ? decodeURIComponent(value.split("=")[1]) : null;
}

function deleteLog() {
  const trigger = $(this);
  const item_id = trigger.data("log-id");

  $.ajax({
    method: "DELETE",
    url: `/api/logs/${item_id}`,
    headers: { "X-CSRFToken": getCookie("csrftoken") },
    success: function () {
      location.reload();
    },
  });
}

$(document).ready(() => {
  $.get("/api/logs", {}, function (response) {
    response.collection.forEach((log) => {
      let food_list = "";
      log.foods.forEach((food) => {
        food_list =
          food_list +
          `<a href="/food/${food.id}" target="_blank" rel="noopener noreferrer">x${food.quantity} ${food.name}</a>`;
      });

      $("#logs-container").append(
        `<div class="-top-border -flex-col" style="padding: 1rem 1.5rem; gap: 0.5rem">
          <header class="-flex-row">
            <h4>Dynamic name</h4>
            <button type="button" class="btn-red" data-action="delete-log" data-log-id="${log.id}">Delete</button>
          </header>
          <div class="-flex-col" style="gap: 0.5rem">
            ${food_list}
          </div>
        </div>`
      );
    });
  });
});

$(document).ready(() => {
  $(document).on("click", "[data-action='delete-log']", deleteLog);

  $(document).on("click", "[data-action='follow-unfollow']", function () {
    const id = $(this).data("id");

    console.log("click");
    $.ajax({
      method: "PATCH",
      url: `/api/social/follow-unfollow/${id}`,
      headers: { "X-CSRFToken": getCookie("csrftoken") },
      success: function (response) {
        if (response.ok) location.reload();
      },
    });
  });
});
