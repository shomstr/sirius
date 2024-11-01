import 'package:flutter/material.dart';
import 'package:sirius/design/colors.dart';

class VoiceInputPage extends StatelessWidget {
  const VoiceInputPage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return const Scaffold(
      body: Center(child: Text('Это страница голосового ввода')),
      backgroundColor: MainPageColor,
    );
  }
}