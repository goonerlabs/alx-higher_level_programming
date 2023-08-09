#include "lists.h"

/**
 * insert_node - inserts a new node into a sorted linked list.
 * @head: pointer to the head of the list.
 * @number: integer to be inserted.
 *
 * Return: the address of the new element, or NULL if it failed.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *temp,  *temp2;

	if (head == NULL)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	temp = *head;
	temp2 = *head;
	new->n = number;
	new->next = NULL;
	if (*head == NULL || number < (*head)->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	temp = temp->next;
	while (temp)
	{
		if (number <= temp->n)
		{
			temp2->next = new;
			new->next = temp;
			return (new);
		}
		temp2 = temp;
		temp = temp->next;
	}
	return (new);
}


