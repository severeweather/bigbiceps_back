function search(url, query, offset) {
  return $.ajax({
    method: "GET",
    url: url,
    data: {
      q: query,
      offset: offset,
    },
  });
}

function renderSearchResults(results, container) {
  results.forEach((result) => {
    $(container).append(
      `
      <div>
        <label for="${result.id}">${result.name}</label>
        <input type="checkbox" name="food_children" value="${result.id}" id="${result.id}"/>
      </div>
      `
    );
  });
}

$(document).ready(() => {
  let offset = 0;
  let loading = false;
  let search_bar = $("[type='search']");

  $("[type='search']").on("keydown", function (e) {
    if (e.key === "Enter") {
      const url = $(this).data("url");
      const value = $(this).val();
      const container = "#search-results-container";

      if (loading) {
        console.log("loading");
        return;
      }

      $(container).empty();
      search(url, value, 0)
        .then((response) => {
          renderSearchResults(response.results, container);
          offset = response.limit;
        })
        .always(() => {
          loading = false;
        });
    }
  });

  $("#search-results-container").on("scroll", function () {
    const container = $(this).get(0);
    if (
      container.scrollTop + container.clientHeight >=
      container.scrollHeight
    ) {
      console.log("Scrolled to bottom");

      const url = search_bar.data("url");
      const value = search_bar.val();

      if (loading) {
        console.log("loading");
        return;
      }
      loading = true;

      search(url, value, offset)
        .then((response) => {
          renderSearchResults(response.results, "#search-results-container");
          offset = offset + response.limit;
        })
        .always(() => {
          loading = false;
        });
    }
  });
});
