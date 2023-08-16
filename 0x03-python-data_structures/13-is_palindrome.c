#include "lists.h"

/**
 * check_palindrome - utility function to check if a list is  a palindrome
 * @head: pointer to the head node
 * @iterator:  pointer to the current node
 * Return: 1 if it is a palindrome, 0 otherwise
 */

int check_palindrome(listint_t **head, listint_t *iterator)
{
    int i, j;

    if (iterator == NULL)
        return (1);
    i = check_palindrome(head, iterator->next);
    if (i == 0)
        return (0);
    j = (iterator->n == (*head)->n);
    *head = (*head)->next;
    return (j);
}


/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to the head of linked list
 * Return: 1 if palindrome else return 0
 */

int is_palindrome(listint_t **head)
{
    return (check_palindrome(head, *head));
}
