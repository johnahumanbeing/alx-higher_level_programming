#include "lists.h"

/**
 * reverse_list - reverses a linked list
 * @head: pointer to the head of the list
 *
 * Return: pointer to the new head of the reversed list
 */
void reverse_list(listint_t **head)
{
	listint_t *current, *prev = NULL, *next_node;

	current = *head;
	while (current)
	{
		next_node = current->next;
		current->next = prev;
		prev = current;
		current = next_node;
	}
	*head = prev;
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to the head of the linked list
 *
 * Return: 1 if it is a palindrome else 0
 */
int is_palindrome(listint_t **head)
{
	int length, i, j;
	listint_t *temp, *mid_node;

	temp = *head;
	if (!temp || !temp->next)
		return (1);

	for (length = 0; temp; length++, temp = temp->next)
		;

	mid_node = *head;
	j = (length % 2 == 0) ? (length / 2) : (length / 2) + 1;

	for (i = 0; i < j; i++)
		mid_node = mid_node->next;

	reverse_list(&mid_node);

	temp = *head;
	for (i = 0; i < j; i++)
	{
		if (temp->n != mid_node->n)
			return (0);
		temp = temp->next;
		mid_node = mid_node->next;
	}

	return (1);
}
