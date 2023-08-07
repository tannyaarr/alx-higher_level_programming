#include <stdio.h>
#include "lists.h"

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
