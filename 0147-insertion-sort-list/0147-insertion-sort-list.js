/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var insertionSortList = function (head) {
  let dummy = new ListNode();
  let curr = head;
  while (curr !== null) {
    // At each iteration, we insert an element into the resulting list.
    let prevFinder = dummy;
    // find the position to insert the current node
    while (prevFinder.next !== null && prevFinder.next.val <= curr.val) {
      prevFinder = prevFinder.next;
    }
    let next = curr.next;
    // insert the current node to the new list
    curr.next = prevFinder.next;
    prevFinder.next = curr;
    // moving on to the next iteration
    curr = next;
  }

  return dummy.next;
};