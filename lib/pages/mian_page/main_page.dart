import 'package:flutter/material.dart';
import 'package:sirius/design/colors.dart';
import 'package:sirius/pages/mian_page/main_list.dart';

class HomePage extends StatelessWidget {
  const HomePage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text(
          'Главная страница',
          style: TextStyle(color: MainPageColor), 
        ),
        centerTitle: true,
        backgroundColor: backgroundColor,
      ),
      body: const MainList(),
      backgroundColor: backgroundColor,
    );
  }
}
