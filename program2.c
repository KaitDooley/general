#include <stdio.h>
#include <stdlib.h>

typedef struct Node
{
    int data;
    struct Node *next;
} Node;

/**
 * Write a function that builds linked list with values:
 *   5 -> 10 -> 15
 *
 * @return Pointer to the linked list.
 */
Node *create_list_1(void);

/**
 * Write a function that builds linked list with values:
 *   3 -> 7 -> 8 -> 20
 *
 * @return Pointer to the linked list.
 */
Node *create_list_2(void);

/**
 * Print a linked list.
 * Each item should be separated by arrows, as seen in the comments of the
 * above functions.
 *
 * @param  list  Pointer to the list
 */
void print_list(Node *list);

/**
 * Merge two sorted linked lists together.
 *
 * @param  list_1    First linked list
 * @param  list_2    Second linked list
 * @return Pointer to the head of the merged list.
 */
Node *merge_lists(Node *list_1, Node *list_2);

/**
 * Free all memory.
 *
 * @param  list_1       First linked list
 * @param  list_2       Second linked list
 * @param  merged_list  Merged linked list
 */
void free_memory(Node *list_1, Node *list_2, Node *merged_list);

Node *node_create(int data);
//void list_add(Node *tail, int data);
void free_list(Node *head);

int main(void)
{
    Node *list_1 = create_list_1();
    print_list(list_1);
    Node *list_2 = create_list_2();
    print_list(list_2);

    Node *merged_list = merge_lists(list_1, list_2);
    print_list(merged_list);

    free_memory(list_1, list_2, merged_list);

    return 0;
}

/** DO NOT EDIT ABOVE THIS LINE **/


Node *node_create(int data) {
	Node *n = malloc(sizeof(Node));
	if (!n) return NULL;
	n->data = data;
	n->next = NULL;
		
	return n;
}
/*
void list_add(Node *tail, int data) {
	(*tail)->next = node_create(data);
	tail = tail->next;
	return;
}
*/

/**
 * Write a function that builds linked list with values:
 *   5 -> 10 -> 15
 *
 * @return Pointer to the linked list.
 */
Node *create_list_1(void) {
	Node *head = node_create(5);
	if (!head) return NULL;
	Node *tail = head;
	tail->next = node_create(10);
	tail = tail->next;
	tail->next = node_create(15);
	tail = tail->next;
	return head;
}

/**
 * Write a function that builds linked list with values:
 *   3 -> 7 -> 8 -> 20
 *
 * @return Pointer to the linked list.
 */
Node *create_list_2(void) {
	Node *head = node_create(3);
	if (!head) return NULL;
	Node *tail = head;
	tail->next = node_create(7);
	tail = tail->next;
	tail->next = node_create(8);
	tail = tail->next;
	tail->next = node_create(20);
	tail = tail->next;
	return head;
}	
/**
 * Print a linked list.
 * Each item should be separated by arrows, as seen in the comments of the
 * above functions.
 *
 * @param  list  Pointer to the list
 */
void print_list(Node *list) {
	if (!list) return;
	printf("%d", list->data);
	list = list->next;
	while(list) {
		printf(" -> %d", list->data);
		list = list->next;
	}
	printf("\n");
}


/**
 * Merge two sorted linked lists together.
 *
 * @param  list_1    First linked list
 * @param  list_2    Second linked list
 * @return Pointer to the head of the merged list.
 */
Node *merge_lists(Node *list_1, Node *list_2) {
	int data;
	if (list_1->data <= list_2->data) { 
		data = list_1->data;
		list_1 = list_1->next;
	} else {
		data = list_2->data;
		list_2 = list_2->next;
	}
	Node *head = node_create(data); 
	Node *tail = head;
	while (list_1 || list_2) {
		if (list_1 && list_2) {	
			if (list_1->data <= list_2->data) { 
				tail->next = node_create(list_1->data);
				tail = tail->next;
				list_1 = list_1->next;
			} else {
				tail->next = node_create(list_2->data);
				tail = tail->next;
				list_2 = list_2->next;
			}
		} else if (list_1) {
			tail->next = node_create(list_1->data);
			tail = tail->next;
			list_1 = list_1->next;
		} else {	
			tail->next = node_create(list_2->data);
			tail = tail->next;
			list_2 = list_2->next;
		}
	}

	return head;
}

/**
 * Free all memory.
 *
 * @param  list_1       First linked list
 * @param  list_2       Second linked list
 * @param  merged_list  Merged linked list
 */
void free_memory(Node *list_1, Node *list_2, Node *merged_list) {
	free_list(list_1);
	free_list(list_2);
	free_list(merged_list);
	return;
}


void free_list(Node *head) {
	Node *curr = head;
	Node *next = curr->next;

	while (curr) {
		free(curr);
		curr = next;
		if (next) next = next->next;
	}
	return;
}


