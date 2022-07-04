#include "lists.h"

/**
 * list_len - finds the num of items int the list
 * @h: pointer to the liked list
 *
 * Return: number of elements
 */

size_t list_len(listint_t *h)
{
size_t nodes = 0;

if (h == NULL)
return (0);

while (h != NULL)
{
nodes++;
h = h->next;
}
return (nodes);
}

/**
 * is_palindrome - checks if a list is a palindrome
 * @head: head of the list
 *
 * Return: 0 if not pali or 1 if is palin
 */

int is_palindrome(listint_t **head)
{
int *arr, i = 0, j = 0, length;
listint_t *temp;

if (*head == NULL)
return (1);

temp = *head;
length = list_len(temp);
arr = (int *)malloc(sizeof(int) * length);

if (arr == NULL)
return (2);

temp = *head;
while (temp != NULL)
{
arr[j] = temp->n;
j++;
temp = temp->next;
}

for (i = 0, j = length - 1; i < j; i++, j--)
{
if (arr[i] != arr[j])
return (0);
}
return (1);
}
