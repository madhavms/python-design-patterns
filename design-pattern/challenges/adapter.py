# Mock class representing the legacy database interaction
class LegacyDatabase:
    def fetch_legacy_user_data(self, user_id):
        # Simulating data retrieval from the legacy database
        if user_id == 1:
            return {"userId": 1, "fullName": "John Doe", "emailAddress": "john@example.com"}
        elif user_id == 2:
            return {"userId": 2, "fullName": "Jane Smith", "emailAddress": "jane@example.com"}
        else:
            return None


# Mock class representing the new modern service
class ModernService:
    def get_user_details(self, user_data):
        # Simulating data retrieval from the modern service
        if user_data:
            return f"User Details: {user_data}"
        else:
            return "User details not found"


# Adapter: Adapts legacy user data to match the format of the modern service
class LegacyToModernAdapter:
    @staticmethod
    def adapt_user_data(legacy_data):
        if legacy_data:
            return {
                "id": legacy_data.get("userId", None),
                "name": legacy_data.get("fullName", None),
                "email": legacy_data.get("emailAddress", None),
                "address": "N/A",   # Placeholder for missing data in the legacy system
                "phone": "N/A",     # Placeholder for missing data in the legacy system
                "role": "N/A"       # Placeholder for missing data in the legacy system
            }
        else:
            return None


if __name__ == '__main__':
    legacy_db = LegacyDatabase()
    modern_service = ModernService()
    
    # Fetching user data from the legacy system
    legacy_user_data = legacy_db.fetch_legacy_user_data(1)  # Simulating fetching user data from the legacy system

    # Adapting legacy data to match the format expected by the new system
    adapted_data = LegacyToModernAdapter.adapt_user_data(legacy_user_data)

    # Sending adapted data to the modern service
    result = modern_service.get_user_details(adapted_data) if adapted_data else None

    # Displaying Results
    print("Before Integration (Legacy System):")
    print(legacy_user_data)  # Old system data

    print("\nAfter Integration (Using New System with Adapter):")
    print(result)  # Result after adapting and sending to the modern service
