import 'dart:async';
import 'api.dart';
import 'package:web_scraper_app/objects/userAccount.dart';

class Login {
  final api = API();

  Future userSignIn(String userEmail, String userPassword, String apiKey) =>
      api.userSignIn(userEmail, userPassword, apiKey);

  Future<UserAccount> createAccount(String userEmail, String userPassword) =>
      api.createAccount(userEmail, userPassword);

  Future getUserItems(String apiKey) => api.getUserItems(apiKey);

  Future<Null> addUserItem(String apiKey, String itemName) async {
    api.addUserItem(apiKey, itemName);
  }
}
