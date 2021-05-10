import pytest
from redes_sociais.redes_sociais import facebook, linkedin, github, instagram
from redes_sociais.sessoes import AlbumSection, PersonalSection, PublicationSection, UploadCodeSection


class TestFacebook:
    def test_instance_facebook(self):
        objeto = facebook()
        assert isinstance(objeto, facebook)


class TestLinkedin:
    def test_instance_linkedin(self):
        objeto = linkedin()
        assert isinstance(objeto, linkedin)


class TestGithub:
    def test_instance_github(self):
        objeto = github()
        assert isinstance(objeto, github)


class TestInstagram:
    def test_instance_instagram(self):
        objeto = instagram()
        assert isinstance(objeto, instagram)