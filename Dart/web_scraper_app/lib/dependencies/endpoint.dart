import 'package:web_scraper_app/objects/item.dart';
import 'package:rxdart/rxdart.dart';
import 'package:web_scraper_app/objects/userAccount.dart';
import 'package:web_scraper_app/dependencies/login.dart';

class UserEndPoint {
  final login = Login();
  // ignore: close_sinks
  final gettingUser = PublishSubject<UserAccount>();

  Observable<UserAccount> get getUser => gettingUser.stream;

  createAccount(String userEmail, String userPassword) async {
    UserAccount account = await login.createAccount(userEmail, userPassword);
    gettingUser.sink.add(account);
  }

  userSignIn(String userEmail, String userPassword, String apiKey) async {
    UserAccount account =
        await login.userSignIn(userEmail, userPassword, apiKey);
    gettingUser.sink.add(account);
  }

  close() {
    gettingUser.close();
  }
}

class ItemEndPoint {
  final login = Login();
  // ignore: close_sinks
  final item = BehaviorSubject<List<Item>>();
  String apiKey;

  var items = <Item>[];

  ItemEndPoint(String apiKey) {
    this.apiKey = apiKey;
    updateItems(apiKey).then((_) {
      item.add(items);
    });
  }

  Stream<List<Item>> get getItems => item.stream;

  Future<Null> updateItems(String apiKey) async {
    items = await login.getUserItems(apiKey);
  }
}

final userEndPoint = UserEndPoint();
