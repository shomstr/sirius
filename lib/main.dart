import 'package:flutter/material.dart';
import 'package:sirius/pages/mian_page/main_page.dart';


void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Voice Input App',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const HomePage(), 
    );
  }
}
