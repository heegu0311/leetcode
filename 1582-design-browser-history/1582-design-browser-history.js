/**
 * Definition for doubly-linked list node.
 */
class ListNode {
  constructor(url) {
    this.url = url;
    this.prev = null;
    this.next = null;
  }
}

/**
 * @param {string} homepage
 */
var BrowserHistory = function (homepage) {
  this.current = new ListNode(homepage);
};

/**
 * @param {string} url
 * @return {void}
 */
BrowserHistory.prototype.visit = function (url) {
  const newNode = new ListNode(url);
  this.current.next = newNode;
  newNode.prev = this.current;
  this.current = newNode;
};

/**
 * @param {number} steps
 * @return {string}
 */
BrowserHistory.prototype.back = function (steps) {
  while (steps > 0 && this.current.prev) {
    this.current = this.current.prev;
    steps--;
  }
  return this.current.url;
};

/**
 * @param {number} steps
 * @return {string}
 */
BrowserHistory.prototype.forward = function (steps) {
  while (steps > 0 && this.current.next) {
    this.current = this.current.next;
    steps--;
  }
  return this.current.url;
};

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * var obj = new BrowserHistory(homepage)
 * obj.visit(url)
 * var param_2 = obj.back(steps)
 * var param_3 = obj.forward(steps)
 */

// Test cases
const browserHistory = new BrowserHistory("leetcode.com");
browserHistory.visit("google.com");
browserHistory.visit("facebook.com");
browserHistory.visit("youtube.com");
console.log(browserHistory.back(1)); // facebook.com
console.log(browserHistory.back(1)); // google.com
console.log(browserHistory.forward(1)); // facebook.com
browserHistory.visit("linkedin.com");
console.log(browserHistory.forward(2)); // linkedin.com
console.log(browserHistory.back(2)); // google.com
console.log(browserHistory.back(7)); // leetcode.com
