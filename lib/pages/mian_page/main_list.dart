import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:sirius/design/images.dart';
import 'package:sirius/pages/text_input_page/text_input.dart';
import 'package:sirius/pages/voice_input_page/voice_input.dart';

class MainList extends StatelessWidget {
  const MainList({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Stack(
      children: <Widget>[
        _list(context),
        _burger_button(),
        _cards_button(),
        _friends_button(),
        _searching_bar(),
        _search_button(),
      ],
    );
  }

  Widget _list(BuildContext context) {
    final List<String> buttonTitles = [
      'Голосовой ввод',
      'Письменный ввод',
      'Загрузка файлов',
      'Ваши файлы',
    ];

    return ListView.builder(
      itemCount: buttonTitles.length,
      padding: const EdgeInsets.only(left: 38, right: 38, top: 220),
      itemBuilder: (BuildContext context, int index) {
        return _styledButton(buttonTitles[index], context);
      },
    );
  }

  Widget _styledButton(String title, BuildContext context) {
    return Container(
      width: 350,
      height: 108,
      margin: const EdgeInsets.only(bottom: 18),
      decoration: BoxDecoration(
        border: Border.all(color: const Color.fromARGB(255, 0, 179, 168)),
        borderRadius: BorderRadius.circular(25),
        gradient: const LinearGradient(
          colors: [
            Color.fromARGB(255, 0, 19, 69),
            Color.fromARGB(255, 0, 93, 87),
          ],
          begin: Alignment.topCenter,
          end: Alignment.bottomCenter,
        ),
      ),
      child: InkWell(
        borderRadius: BorderRadius.circular(25),
        onTap: () {
          if (title == 'Голосовой ввод') {
            Navigator.push(
              context,
              MaterialPageRoute(builder: (context) => const VoiceInputPage()),
            );
          } else if (title == 'Письменный ввод') {
            Navigator.push(
              context,
              MaterialPageRoute(builder: (context) => const TextInputPage()),
            );
          }
        },
        child: Center(
          child: Text(
            title,
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
      left: 25,
      top: 31,
      child: GestureDetector(
        onTap: () {
          if (kDebugMode) {
            print('Burger button pressed!');
          }
        },
        child: SizedBox(
          width: 50,
          height: 51,
          child: BurgerButton,
        ),
      ),
    );
  }

  Widget _cards_button() {
    return Positioned(
      left: 38,
      top: 99,
      child: GestureDetector(
        onTap: () {
          if (kDebugMode) {
            print('Cards button pressed!');
          }
        },
        child: Container(
          width: 158,
          height: 100,
          decoration: BoxDecoration(
            border: Border.all(color: const Color.fromARGB(255, 0, 179, 168)),
            borderRadius: BorderRadius.circular(25),
            gradient: const LinearGradient(
              colors: [
                Color.fromARGB(255, 0, 19, 69),
                Color.fromARGB(255, 0, 93, 87),
              ],
              begin: Alignment.topCenter,
              end: Alignment.bottomCenter,
            ),
          ),
          child: const Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Text(
                    'Карточки',
                    style: TextStyle(
                      color: Colors.white,
                      fontSize: 18,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                ],
              ),
              SizedBox(width: 16.0),
              Padding(
                padding: EdgeInsets.only(right: 16.0),
                child: Icon(
                  Icons.credit_card,
                  color: Colors.white,
                  size: 30,
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _friends_button() {
    return Positioned(
      right: 38,
      top: 99,
      child: GestureDetector(
        onTap: () {
          if (kDebugMode) {
            print('Cards button pressed!');
          }
        },
        child: Container(
          width: 158,
          height: 100,
          decoration: BoxDecoration(
            border: Border.all(color: const Color.fromARGB(255, 0, 179, 168)),
            borderRadius: BorderRadius.circular(25),
            gradient: const LinearGradient(
              colors: [
                Color.fromARGB(255, 0, 19, 69),
                Color.fromARGB(255, 0, 93, 87),
              ],
              begin: Alignment.topCenter,
              end: Alignment.bottomCenter,
            ),
          ),
          child: const Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Text(
                    'Ваши',
                    style: TextStyle(
                      color: Colors.white,
                      fontSize: 18,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                  Text(
                    'друзья',
                    style: TextStyle(
                      color: Colors.white,
                      fontSize: 18,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                ],
              ),
              SizedBox(width: 15.0),
              Padding(
                padding: EdgeInsets.only(right: 16.0),
                child: Icon(
                  Icons.people_alt_outlined,
                  color: Colors.white,
                  size: 45,
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

Widget _searching_bar() {
  return Positioned(
    left: 84,
    top: 35,
    child: GestureDetector(
      onTap: () {
        if (kDebugMode) {
          print('Burger button pressed!');
        }
      },
      child: Container(
        width: 210,
        height: 41,
        decoration: BoxDecoration(
          borderRadius: BorderRadius.circular(20),
          border: Border.all(
            color: const Color.fromARGB(255, 0, 179, 168),
            width: 2,
          ),
        ),
        child: const Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Icon(Icons.search),
            SizedBox(width: 8),
            Expanded(
              child: TextField(
                decoration: InputDecoration(
                  hintText: 'Главное меню',
                  hintStyle: TextStyle(
                    color: Color.fromARGB(255, 255, 240, 240),
                    fontSize: 18,
                  ),
                  border: InputBorder.none,
                ),
              ),
            ),
          ],
        ),
      ),
    ),
  );
}

Widget _search_button() {
  return Positioned(
    left: 194,
    top: 35,
    child: GestureDetector(
      onTap: () {
        if (kDebugMode) {
          print('Burger button pressed!');
        }
      },
      child: SizedBox(
        width: 280,
        height: 41,
        child: SearchbarButton,
      ),
    ),
  );
}
