/**
 * nightmode.js by kamiheku
 */

/**
 * Gets and returns the classname for the body element
 */
function getBodyClassName() {
  return document.getElementsByTagName("body")[0].className;
}

/**
 * Gets and returns the cookie that contains the user's preference for
 * nightmode
 */
function getCookie() {
  return document.cookie.replace(/(?:(?:^|.*;\s*)lights\s*\=\s*([^;]*).*$)|^.*$/, "$1");
}

/**
 * Run on page load; checks if user prefers night or day mode and sets the
 * class for body accordingly
 */
function lightsOnCookie() {
  var lights = getCookie();

  document.getElementsByTagName("body")[0].className = (lights === "on") ?
    "night" : "day";
}

/**
 * Run on clicking the lightswitch; toggles the day/night class for body and
 * on/off for the cookie
 */
function lightswitch() {
  var name = getBodyClassName();
  var lights = getCookie();

  document.getElementsByTagName("body")[0].className = (name === "day") ?
    "night" : "day";
  document.cookie = (lights === "on") ?
    "lights=off;path=/" : "lights=on;path=/";
}
