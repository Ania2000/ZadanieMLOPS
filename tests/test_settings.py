from settings import Settings


def test_settings_load_correctly() -> None:

    settings = Settings()

    assert settings.ENVIRONMENT == "test"
    assert settings.APP_NAME == "MyApp-Test"
    assert settings.API_KEY == "fake_test_api_key"
    assert settings.HASLO == "fake_test_password"
