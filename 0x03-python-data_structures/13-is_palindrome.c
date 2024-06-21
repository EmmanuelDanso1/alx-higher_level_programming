#include "lists.h"
#include <stdio.h>

void reverse(listint_t **head);
int compare_lists(listint_t *head,  listint_t *middle, int len);
/**
*is_palindrome - checkes if the list is a palindrome
*@head: pointer of the first node
*Return 0 if palindrome not detected and 1 if yes
*/
int is_palindrome(listint_t **head)
{
	int lenth, i;
	listint_t *tmp;
	listint_t *middle;

	if (head == NULL || *head == NULL)
		return (1);
	tmp = *head;
	middle = *head;

	for (lenth = 0; tmp != NULL; lenth++)
		tmp = tmp->next;
	lenth = lenth / 2;
	for (i = 1; i < lenth; i++)
		middle = middle->next;
	if (lenth % 2 != 0 && lenth != 1)
	{
		middle = middle->next;
		lenth = lenth - 1;
	}
	reverse(&middle);
	i = compare_lists(*head, middle, lenth);
	return (i);
}
/**
 *compare_lists - compare two lists
 *@head: pointer to the head
 *@middle: pointer to the middle node
 *@lenth: lenght of the list
 @Return: if same 1, else 0
 */
int compare_lists(listint_t *head, listint_t *middle, int lenth)
{
	int i;
	if (head == NULL || middle == NULL)
		return (1);
	for (i = 0; i < lenth; i++)
	{
		if (head->n != middle->n)
			return (0);
		head = head->next;
		middle = middle->next;
	}
	return (1);

}
/**
 * reverse - reverse a list
 * @head: pointer to the reverse head
 */
void reverse(listint_t **head)
{
	listint_t *current;
	listint_t *next;
	listint_t *prev;
	if (head == NULL || *head == NULL)
		return;
	prev = NULL;
	current = *head;
	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
}

