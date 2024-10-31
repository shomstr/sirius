import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:sirius/design/dessmissions.dart';
import 'package:sirius/design/images.dart';
import 'main_item.dart';

class MainList extends StatelessWidget {
  const MainList({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Stack(
      children: <Widget>[
        _list(),
        _burger_button(),
        _cards_button(),
        friends_button(),
      ],
    );
  }

  Widget _list() {
    final List<String> buttonTitles = [
      'Голосовой ввод',
      'Письменный ввод',
      'Загрузка файлов',
      'Другие действия',
    ];

    return ListView.builder(
      itemCount: buttonTitles.length,
      padding: const EdgeInsets.only(left: padding84, right: padding84),
      itemBuilder: (BuildContext context, int index) {
        return _styledButton(buttonTitles[index]); // Используем метод для создания кнопки
      },
    );
  }

  Widget _styledButton(String title) {
    return Container(
      width: 396, 
      height: 127, 
      margin: const EdgeInsets.only(bottom: 8), 
      decoration: BoxDecoration(
        border: Border.all(color: const Color.fromARGB(255, 0, 179, 168)), 
        borderRadius: BorderRadius.circular(25), 
        gradient: const LinearGradient(
          colors: [
            Color.fromARGB(255, 0, 195, 183),
            Color.fromARGB(255, 0, 93, 87), 
          ],
          begin: Alignment.topCenter,
          end: Alignment.bottomCenter,
        ),
      ),
      child: InkWell(
        borderRadius: BorderRadius.circular(25),
        onTap: () {
          print('Press $title'); 
        },
        child: Center(
          child: Text(
            title, // Заголовок кнопки
            style: const TextStyle(
              color: Colors.white,
              fontSize: 18,
              fontWeight: FontWeight.bold,
            ),
          ),
        ),
      ),
    );
  }

  Widget _burger_button() {
    return Positioned(
      left: 25, // Положение слева
      top: 31, // Положение сверху
      child: GestureDetector(
        onTap: () {
          // Действие при нажатии на кнопку
          if (kDebugMode) {
            print('Burger button pressed!');
          }
        },
        child: SizedBox(
          width: 50, // Ширина кнопки
          height: 51, // Высота кнопки
          child: BurgerButton, // Укажите путь к вашему изображению
        ),
      ),
    );
  }

  Widget _cards_button() {
    // Реализация кнопки карт
    return Container(); // Замените на вашу реализацию
  }

  Widget friends_button() {
    // Реализация кнопки друзей
    return Container(); // Замените на вашу реализацию
  }
}
