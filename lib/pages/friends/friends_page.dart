import 'package:flutter/material.dart';
import 'package:hive/hive.dart';

class FriendsPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Профиль пользователя')),
      body: FutureBuilder(
        future: Hive.openBox('userBox'), // Открытие коробки Hive
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            return Center(child: CircularProgressIndicator());
          }

          var box = snapshot.data as Box; // Получение данных из коробки
          String? username = box.get('username'); 
          String? id = box.get('id'); 

          return Center(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Text(
                  'Имя пользователя:',
                  style: TextStyle(fontSize: 24),
                ),
                SizedBox(height: 10),
                Text(
                  username ?? 'Не указано',
                  style: TextStyle(fontSize: 32, fontWeight: FontWeight.bold),
                ),
                SizedBox(height: 20), // Добавляем отступ между текстами
                Text(
                  'ID пользователя:',
                  style: TextStyle(fontSize: 24),
                ),
                SizedBox(height: 10),
                Text(
                  id?.toString() ?? 'Не указано',
                  style: TextStyle(fontSize: 32, fontWeight: FontWeight.bold),
                ),
              ],
            ),
          );
        },
      ),
    );
  }
}
