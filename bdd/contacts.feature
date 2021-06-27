Scenario Outline: Add new contact
Given a contact list
Given a contact with <firstname>, <lastname> and <mobile_phone>

When I add the contact to the list
Then the new contact list is equal to the old list with the added contact

Examples:
|firstname   |lastname   |mobile_phone|
|firstname123|lastname345|89098765432 |
|firstname321|lastname333|89223335432 |


Scenario: Delete a contact
Given a non-empty contact list
Given a random contact from the list

When I delete the contact from the list
Then the new contact list is equal to the old list without the deleted contact


Scenario Outline: Modify a contact
Given a non-empty contact list
Given a random contact from the list
Given a contact with <firstname>, <lastname> and <mobile_phone>

When I modify the random contact
Then the new contact list is equal to the old list with the modify contact

Examples:
|firstname   |lastname   |mobile_phone|
|firstname111|lastname111|89098765111 |
|firstname222|lastname222|89223335222 |