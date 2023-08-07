#include <stdio.h>
#include "lists.h"

/**
 * check if list is empty
 * create pointer to head
 * traverse through linked list
 * if NULL is found return 0
 * if pointer to head == head pointer
 * return 1
 */

int check_cycle(listint_t *list)
{
	listint_t *temp = list;
	if (temp == NULL)
		return (0);
	while (temp)
	{
		if (temp->next ==NULL)
			return (0);
		temp = temp->next;
		if (temp ==list)
			break;
	}
	return (1);
}
