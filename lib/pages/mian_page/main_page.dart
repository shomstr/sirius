import 'package:flutter/material.dart';
import 'package:sirius/design/colors.dart';
import 'package:sirius/pages/mian_page/main_list.dart';

class HomePage extends StatelessWidget {
  const HomePage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return const Scaffold(
      body: MainList(),
      backgroundColor: MainPageColor,
    );
  }
}