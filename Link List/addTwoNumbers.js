/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */

// Definition for singly-linked list.
 function ListNode(val, next) {
     this.val = (val===undefined ? 0 : val)
     this.next = (next===undefined ? null : next)
 }

const initListNode = (dataArray) => {
    //init a example link list
  const dummy = new ListNode(0);
  let current = dummy;

  dataArray.forEach((val) => {
    current.next = new ListNode(val);
    current = current.next;
  });
  return dummy.next;
}

 var addTwoNumbers = function(l1, l2) {
    let carry = 0;
    let dummy = new ListNode();
    let current = dummy;
    while (l1 != null || l2 != null){
        if(l1 != null){
            carry += l1.val;
            l1 = l1.next;
        }
        if(l2 != null){
            carry += l2.val;
            l2 = l2.next;
        }
        current.next = new ListNode(carry % 10);
        carry = carry > 9 ? 1:0;
        current = current.next;
    }
    if(carry != 0){
        dummy.next = new ListNode(carry);
    }
    return dummy.next;
 }


 var sortList = function(head) {
    return mergeSort(head);
};

const mergeSort = (head) => {
    if (head === null&& head.next ===null){
        return head;
    } 
    
    let dummy = new ListNode();
    dummy.next = head;
    let fast = dummy;
    let slow = dummy;
    
    if (fast != null && fast.next != null){
        fast = fast.next.next;
        slow = slow.next.next;
    }
    
    let head2 = new ListNode();
    head2 = slow.next;
    slow.next = null;
    
    head = mergeSort(head);
    head2 = mergeSort(head2);
    
    return merge(head,head2)
}

const merge = (head,head2) => {
    let dummy = new ListNode();
    let res = dummy.next;
    
    if (head.val < head2.val){
        res.next = head;
        res = res.next;
        head = head.next;
    }else {
        res.next = head2;
        res = res.next;
        head2 = head2.next;
    }
    
    if (head != null){
        res.next = head;
    }
    
    if(head2 != null){
        res.next = head2
    }
    
    return res
}

 const main = () => {
    data1 = [4, 3, 2, 1];
    data2 = [3,1,2];
    const l1 = initListNode(data1);
    // const l2 = initListNode(data2);
    // const res = addTwoNumbers(l1,l2);
    const res = sortList(l1)
    console.log("the result",res);
}

main();
