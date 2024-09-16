# Modules required for token generation
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type


## For 'Forgot password' page token generation
class TokenGenerator(PasswordResetTokenGenerator):
	def _make_hash_value(self, user, timestamp):
		# return a hash value of user's Pid, time of token generation and user's active status
		return (
			text_type(user.pk) + text_type(timestamp) +
			text_type(user.is_active)
		)
account_activation_token = TokenGenerator()
