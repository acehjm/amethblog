from material.frontend import Module


class Admin(Module):
    icon = "mdi-action-settings-applications"
    order = 1000

    @property
    def label(self):
        return 'ace_hjm'

    def has_perm(self, user):
        return user.is_staff
