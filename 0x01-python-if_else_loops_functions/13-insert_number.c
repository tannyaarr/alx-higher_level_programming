#include "lists.h"
#include <stdio.h>
#include <stddef.h>
#include <stdlib.h>

/**
 * @head:
 * Return: address of new node or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *current_num;
	current_num = *head;

	while (current_num->next && (current_num->next->n < number))
	{
		current_num = current_num->next;
	}
	new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
	{
		return (NULL);
	}
	new_node->n = number;
	new_node->next = current_num->next;
	current_num->next = new_node;
	
	return (new_node);
}
