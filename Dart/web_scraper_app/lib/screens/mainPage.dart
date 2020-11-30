import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:web_scraper_app/dependencies/login.dart';
import 'package:web_scraper_app/dependencies/endpoint.dart';
import 'package:web_scraper_app/screens/addItemScreen.dart';
import 'package:web_scraper_app/screens/loginPage.dart';

class MainPage extends StatelessWidget {
  MainPage();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: buildBody(),
      backgroundColor: Colors.cyanAccent,
      floatingActionButton: new FloatingActionButton(
        onPressed: () {
          Navigator.of(context)
              .push(MaterialPageRoute(builder: (context) => AddItemScreen()));
        },
        child: new Icon(Icons.add_circle),
      ),
    );
  }

  Widget buildBody() {
    return new Container(
      margin: const EdgeInsets.fromLTRB(8.0, 56.0, 8.0, 0.0),
      child: new Column(
        children: <Widget>[getAppTitleWid()],
      ),
    );
  }

  Widget getAppTitleWid() {
    return new Text(
      'Items',
      style: new TextStyle(
          color: Colors.white, fontWeight: FontWeight.bold, fontSize: 26.0),
    );
  }

  Container getListItemWid(Map item, MaterialColor color) {
    return new Container(
      margin: const EdgeInsets.only(top: 8.0),
      child: new Card(
        child: getListTile(item, color),
      ),
    );
  }

  ListTile getListTile(Map item, MaterialColor color) {
    return new ListTile(
      leading: getLeadingWid(item['name'], color),
      title: getTitleWid(item['name']),
      subtitle: getSubtitleText(item['price']),
      isThreeLine: true,
    );
  }

  CircleAvatar getLeadingWid(String itemName, MaterialColor color) {
    return new CircleAvatar(
      backgroundColor: color,
      child: new Text(itemName[0]),
    );
  }

  Text getTitleWid(String itemName) {
    return new Text(
      itemName,
      style: new TextStyle(fontWeight: FontWeight.bold),
    );
  }

  RichText getSubtitleText(String price) {
    TextSpan priceTextWid = new TextSpan(
      text: "\$$price\n",
      style: new TextStyle(color: Colors.black),
    );
    return new RichText(
      text: new TextSpan(children: [priceTextWid]),
    );
  }
}

/*
class MainPage extends StatefulWidget {
  @override
  _MainPageState createState() => _MainPageState();
}

class _MainPageState extends State<MainPage> {
  ItemEndPoint itemEndPoint;
  String apiKey = "";
  Login login = Login();

  @override
  Widget build(BuildContext context) {
    return FutureBuilder(
      future: userSignIn(),
      builder: (BuildContext context, AsyncSnapshot snap) {
        if (snap.hasData) {
          apiKey = snap.data;
          itemEndPoint = ItemEndPoint(apiKey);
        } else {
          print("No data found");
        }

        return apiKey.length > 0
            ? homePage()
            : LoginPage(
                loginInfo: loginInfo,
                newAccount: false,
              );
      },
    );
  }

  void loginInfo() {
    setState(() {
      build(context);
    });
  }

  Future userSignIn() async {
    String userEmail = "";
    apiKey = await getApiKey();
    if (apiKey == null) {
      print("Api key not found");
    } else {
      userEndPoint.userSignIn("", "", apiKey);
    }
    return apiKey;
  }

  Future getApiKey() async {
    SharedPreferences preferences = await SharedPreferences.getInstance();
    return await preferences.getString("apiToken");
  }

  Widget homePage() {
    return MaterialApp(Scaffold(
      body: buildBody(),
      backgroundColor: Colors.cyanAccent,
      floatingActionButton: new FloatingActionButton(
        onPressed: () {
          Navigator.of(context)
              .push(MaterialPageRoute(builder: (context) => AddItemScreen()));
        },
        child: new Icon(Icons.add_alert),
      ),
    ));
  }

  Widget buildBody() {
    return new Container(
      margin: const EdgeInsets.fromLTRB(8.0, 56.0, 8.0, 0.0),
      child: new Column(
        children: <Widget>[getAppTitleWid()],
      ),
    );
  }
}
*/
