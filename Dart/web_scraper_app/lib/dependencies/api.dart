import 'dart:async';
import 'package:http/http.dart' show Client;
import 'package:web_scraper_app/objects/item.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'dart:convert';
import 'package:web_scraper_app/objects/userAccount.dart';

class API {
  Client client = Client();
  final apiKey = 'currentApiKey';

  Future<UserAccount> createAccount(
      String userEmail, String userPassword) async {
    final response = await client.post(
        "http://127.0.0.1:5000/api/createAccount",
        body: jsonEncode(
            {"emailadress": userEmail, "userPassword": userPassword}));
    final Map result = json.decode(response.body);
    if (response.statusCode == 201) {
      await saveApiKey(result["data"]["apiKey"]);
      return UserAccount.fromJson(result["data"]);
    } else {
      throw Exception('Data not found in Api.dart');
    }
  }

  Future userSignIn(
      String userEmail, String userPassword, String apiKey) async {
    final response = await client.post("http://127.0.0.1:5000/api/userSignIn",
        headers: {"Authorization": apiKey},
        body: jsonEncode({
          "useremail": userEmail,
          "userpassword": userPassword,
        }));
    final Map result = json.decode(response.body);
    if (response.statusCode == 201) {
      await saveApiKey(result["data"]["apiKey"]);
    } else {
      throw Exception("Data not found for userSignIn");
    }
  }

  Future<List<Item>> getUserItems(String apiKey) async {
    final response = await client.get(
      "http://127.0.0.1:5000/api/verify",
      headers: {"Authorization": apiKey},
    );
    final Map result = json.decode(response.body);
    if (response.statusCode == 201) {
      List<Item> items = [];
      for (Map json in result["data"]) {
        try {
          items.add(Item.fromJson(json));
        } catch (Exception) {
          print(Exception);
        }
      }
      for (Item item in items) {
        print(item.UPC);
      }
      return items;
    } else {
      throw Exception("Couldn't find items");
    }
  }

  Future addUserItem(String apiKey, String itemName) async {
    final response = await client.post("http://127.0.0.1:5000/api/verify",
        headers: {"Authorization": apiKey},
        body: jsonEncode({"title": "", "item": itemName}));
    if (response.statusCode == 201) {
      print("Item added");
    } else {
      print(json.decode(response.body));
      throw Exception("Couldn't load items");
    }
  }

  saveApiKey(String apiKey) async {
    SharedPreferences preferences = await SharedPreferences.getInstance();
    await preferences.setString("apiToken", apiKey);
  }
}
