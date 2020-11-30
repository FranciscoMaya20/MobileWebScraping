class Item {
  // ignore: non_constant_identifier_names
  int UPC;
  double price;
  String name;
  String store;

  Item(this.UPC, this.price, this.name, this.store);

  // ignore: non_constant_identifier_names
  bool setUPC(int UPC) {
    if (UPC is int) {
      this.UPC = UPC;
      return true;
    } else {
      return false;
    }
  }

  int getUPC() {
    return this.UPC;
  }

  bool setPrice(double price) {
    if (price is double) {
      this.price = price;
      return true;
    } else {
      return false;
    }
  }

  double getPrice() {
    return this.price;
  }

  bool setName(String name) {
    if (name is String) {
      this.name = name;
      return true;
    } else {
      return false;
    }
  }

  String getName() {
    return this.name;
  }

  bool setStore(String store) {
    if (store is String) {
      this.store = store;
      return true;
    } else {
      return false;
    }
  }

  String getStore() {
    return this.store;
  }

  factory Item.fromJson(Map<String, dynamic> processedJson) {
    return Item(processedJson["UPC"], processedJson["price"],
        processedJson["name"], processedJson["store"]);
  }
}
