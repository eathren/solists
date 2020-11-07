function noPropagation(event) {
  event.stopImmediatePropagation();
}
var companyLink = document.getElementById("companyLink");
companyLink.addEventListener("click", noPropagation);
