#include "lists.h"

/**
 * insert_node - insert a number in a singly linked list
 * @head: list to traverse
 * @number: num to insert
 * Return: address of new node
 */

listint_t *insert_node(listint_t **head, int number)
{
listint_t *new_node;
listint_t *curr;

curr = *head;

new_node = malloc(sizeof(listint_t));

if (new_node == NULL)
return (NULL);

new_node->n = number;
new_node->next = NULL;

if (*head == NULL || curr->n > new_node->n)
{
new_node->next = *head;
*head = new_node;
return (new_node);
}

while (curr->next != NULL)
{
if ((curr->next->n > new_node->n && curr->n < new_node->n) 
		|| new_node->n == curr->n)
{
new_node->next = curr->next;
curr->next = new_node;
return (new_node);
}
curr = curr->next;
}
new_node->next = curr->next;
curr->next = new_node;
return (new_node);
}

