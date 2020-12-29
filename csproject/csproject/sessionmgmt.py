import django.contrib.sessions.backends.db as db

class SessionStore(db.SessionStore):
	
	cache_key_prefix = 'notes-prefix-'

	sessionCounter = 1

	def _get_new_session_key(self):

		while True:

			session_key = 'notes-app-session-' + str(SessionStore.sessionCounter)
			SessionStore.sessionCounter += 1


			if not self.exists(session_key):

				return session_key
