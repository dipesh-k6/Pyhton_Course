\# Django Admin Cheatsheet

&#x09;-List View Customization:

&#x09;

&#x09;class MyModelAdmin(admin.ModelAdmin):

&#x20;   

&#x20;   		- columns to display in list

&#x20;   		list\_display = \['field1', 'field2', 'field3']

&#x20;   

&#x20;   		- fields editable directly from list

&#x20;   		list\_editable = \['field2']

&#x20;   

&#x20;   		- filter sidebar on right

&#x20;   		list\_filter = \['field1', 'field2']

&#x20;   

&#x20;   		- search bar — fields to search through

&#x20;   		search\_fields = \['field1', 'field2']

&#x20;   

&#x20;   		- default ordering (- means descending)

&#x20;   		ordering = \['-field1']

&#x20;   

&#x20;   		- records per page

&#x20;   		list\_per\_page = 10

&#x20;   

&#x20;   		- date drill-down navigation

&#x20;   		date\_hierarchy = 'created\_at'

\--------------------------------------------------------------------------------------



&#x09;-Detail View Customization:



&#x09;- fields user cannot edit

&#x20;   	readonly\_fields = \['created\_at', 'updated\_at']

&#x20;   

&#x20;   	- organize fields into sections

&#x20;   	fieldsets = \[

&#x20;       ('Section Name', {

&#x20;           'fields': \['field1', 'field2'],

&#x20;           'classes': \['collapse']  # makes section collapsible

&#x20;       }),

&#x20;       ('Another Section', {

&#x20;           'fields': \['field3'],

&#x20;       }),

&#x20;   	]

&#x20;   

&#x20;   	- fields to show in add/edit form

&#x20;   	fields = \['field1', 'field2']  # simple alternative to fieldsets

&#x20;   

&#x20;   	- fields to exclude from form

&#x20;   	exclude = \['field3']

