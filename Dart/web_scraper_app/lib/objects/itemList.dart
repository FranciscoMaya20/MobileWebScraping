import "item.dart";

class ItemList {
  List<Item> itemList = [];

  ItemList(this.itemList);
  bool addItem(Item item) {
    if (item is Item) {
      this.itemList.add(item);
      return true;
    } else {
      return false;
    }
  }

  bool removeItem(Item item) {
    if (item is Item && this.itemList.contains(item)) {
      this.itemList.remove(item);
      return true;
    } else {
      return false;
    }
  }

  List getItemList() {
    return this.itemList;
  }

  bool checkItemInList(Item item) {
    if (this.itemList.contains(item)) {
      return true;
    } else {
      return false;
    }
  }

  int length() {
    return this.itemList.length;
  }

  Item getItemAt(int index) {
    return this.itemList[index];
  }
}
