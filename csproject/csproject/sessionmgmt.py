import django.contrib.sessions.backends.db as db

class SessionStore(db.SessionStore):
	sessionCounter = 0

	def _get_new_session_key(self):
		while True:
			session_key = 's-' + str(SessionStore.sessionCounter)
			SessionStore.sessionCounter += 1
			print(session_key)

		if not self.exists(session_key):

			return session_key
