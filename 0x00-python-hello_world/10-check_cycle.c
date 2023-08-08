#include "lists.h"

/**
 * check_cycle - checks if a linked list has a cycle or loop
 * @list: pointer to the head of the linked list
 *
 * Return: 1 if there is a cycle or loop, else return 0
 */

int check_cycle(listint_t *list)
{
    listint_t *slow;
    listint_t *fast;

    if (list == NULL)
        return (0);

    slow = list;
    fast = list;
    while (fast && fast->next && slow)
    {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast)
            return (1);
    }
    return (0);
}
