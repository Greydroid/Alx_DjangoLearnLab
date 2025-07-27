my first django project
# Bookshelf Permissions and Groups

This app uses custom permissions (`can_view`, `can_create`, `can_edit`, `can_delete`) for the Book model.

Permissions are enforced using Django's `@permission_required` decorator.

Groups like Editors, Viewers, and Admins can be managed in the Django admin to control access levels.
t
