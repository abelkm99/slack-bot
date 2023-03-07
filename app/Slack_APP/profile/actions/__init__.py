from .register_user import handel_user_registration,handel_user_registration_submission
def register_actions(app):
    app.action("profile_menu_register_user")(handel_user_registration)
    app.view("profile_register_view_callback")(handel_user_registration_submission)