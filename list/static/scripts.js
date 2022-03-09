const handleAdd = async (e) => {
  const id = e.target.getAttribute("data-food-id");

  await fetch(`/food/${id}`)
  .then((res) => res.json())
  .then((data) => {
    console.log('data', data);
  });

  const foodListItem = document.querySelector(`div[data-food-id="${id}"]`);
  const foodListItemBtn = document.querySelector(`button[data-food-id="${id}"]`);
  
  // change inner html of food list item to "Added"
  foodListItemBtn.innerHTML = "Added!";

  setTimeout(() => {
    foodListItem.style.opacity = "0.5";
  }, 500);

  setTimeout(() => {
    foodListItem.classList.add("d-none");
  }, 1000);
};

const handleRemove = async (e) => {
  const id = e.target.getAttribute("data-food-id");
  window.localStorage.removeItem(id);

  await fetch(`/food/${id}`)
  .then((res) => res.json())
  .then((data) => {
    console.log('data', data);
  });

  const foodListItem = document.querySelector(`div[data-food-id="${id}"]`);
  foodListItem.classList.add("d-none");
};

const handleCrossOut = async (e) => {
  const id = e.target.getAttribute("data-food-id");
  const checkbox = document.querySelector(`input[data-food-id="${id}"]`);
  const foodItem = document.querySelector(`label[data-food-id="${id}"]`);

  if (!foodItem.classList.contains("crossed-out")) {
    foodItem.style.textDecoration = "line-through";
    foodItem.classList.add("crossed-out");
    checkbox.checked = true;
    window.localStorage.setItem(id, true);
  } else {
    foodItem.style.textDecoration = "none";
    foodItem.classList.remove("crossed-out");
    checkbox.checked = false;
    window.localStorage.setItem(id, false);
  }
};

document.addEventListener("DOMContentLoaded", () => {
  const addBtn = document.querySelectorAll("button.add");
  addBtn.forEach((btn) => btn.addEventListener("click", handleAdd));

  const removeBtn = document.querySelectorAll("button.remove");
  removeBtn.forEach((btn) => btn.addEventListener("click", handleRemove));

  const foodItem = document.querySelectorAll("h4.food");
  foodItem.forEach((item) => item.addEventListener("click", handleCrossOut));

  // maintain the state of items in the list that were crossed out in local storage
  const storage = window.localStorage;
  for (const [key, value] of Object.entries(storage)) {
    if (value === "true") {
      const foodItem = document.querySelector(`label[data-food-id="${key}"]`);
      const checkbox = document.querySelector(`input[data-food-id="${key}"]`);
      foodItem.style.textDecoration = "line-through";
      foodItem.classList.add("crossed-out");
      checkbox.checked = true;
    }
  }
});
