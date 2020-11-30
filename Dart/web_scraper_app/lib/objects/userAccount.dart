import "itemList.dart";
import "item.dart";

class UserAccount {
  String userEmail;
  String userPassword;
  ItemList userItemList;
  String apiKey;
  int id;

  UserAccount(this.userEmail, this.userPassword, this.userItemList, this.apiKey,
      this.id);

  bool setEmail(String email) {
    if (email is String) {
      this.userEmail = email;
      return true;
    } else {
      return false;
    }
  }

  bool setPassword(String password) {
    if (password is String) {
      this.userPassword = password;
      return true;
    } else {
      return false;
    }
  }

  bool addItem(Item item) {
    if (item is Item && this.userItemList.checkItemInList(item) == false) {
      this.userItemList.addItem(item);
      return true;
    } else {
      return false;
    }
  }

  bool removeItem(Item item) {
    if (item is Item && userItemList.checkItemInList(item) == true) {
      userItemList.removeItem(item);
      return true;
    } else {
      return false;
    }
  }

  factory UserAccount.fromJson(Map<String, dynamic> processedJson) {
    return UserAccount(
        processedJson['userEmail'],
        processedJson['userPassword'],
        processedJson['userItemsList'],
        processedJson['apiKey'],
        processedJson['id']);
  }
}
