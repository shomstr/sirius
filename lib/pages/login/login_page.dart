import 'package:flutter/material.dart';
import 'package:hive/hive.dart';
import 'package:http/http.dart' as http;
import 'package:sirius/pages/mian_page/main_page.dart';
import 'dart:convert';
import 'registration_page.dart'; 

class LoginPage extends StatefulWidget {
  const LoginPage({Key? key}) : super(key: key);

  @override
  _LoginPageState createState() => _LoginPageState();
}

class _LoginPageState extends State<LoginPage> {
  final _formKey = GlobalKey<FormState>();
  String email = '';
  String password = '';
  String username = ''; 

  Future<void> _login() async {
    if (_formKey.currentState!.validate()) {
      final response = await http.post(
        Uri.parse('http://127.0.0.1:8000/login'), 
        headers: {
          'Content-Type': 'application/json',
        },
        body: jsonEncode({
          'email': email,
          'password': password,
        }),
      );

      if (response.statusCode == 200) {
        final responseData = jsonDecode(response.body);
        var box = await Hive.openBox('userBox');
        await box.put('id', responseData['id']);
        await box.put('username', username);
        await box.put('email', email); 
        await box.put('password', password); 
        
        Navigator.pushAndRemoveUntil(
          context,
          MaterialPageRoute(builder: (context) => HomePage()), 
          (Route<dynamic> route) => false,
        );
      } else {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(content: Text('Неверные учетные данные')),
        );
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Логин')),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Form(
          key: _formKey,
          child: Column(
            children: [
              TextFormField(
                decoration: InputDecoration(labelText: 'Имя пользователя'), 
                validator: (value) {
                  if (value == null || value.isEmpty) {
                    return 'Пожалуйста, введите имя пользователя';
                  }
                  return null;
                },
                onChanged: (value) {
                  username = value; 
                },
              ),
              TextFormField(
                decoration: InputDecoration(labelText: 'Электронная почта'),
                validator: (value) {
                  if (value == null || value.isEmpty || !value.contains('@')) {
                    return 'Пожалуйста, введите корректный адрес электронной почты';
                  }
                  return null;
                },
                onChanged: (value) {
                  email = value;
                },
              ),
              TextFormField(
                decoration: InputDecoration(labelText: 'Пароль'),
                obscureText: true,
                validator: (value) {
                  if (value == null || value.isEmpty) {
                    return 'Пожалуйста, введите пароль';
                  }
                  return null;
                },
                onChanged: (value) {
                  password = value;
                },
              ),
              SizedBox(height: 20),
              ElevatedButton(
                onPressed: _login,
                child: Text('Войти'),
              ),
              SizedBox(height: 20),
              TextButton(
                onPressed: () {
                  Navigator.push(
                    context,
                    MaterialPageRoute(builder: (context) => RegistrationPage()),
                  );
                },
                child: Text('Нет аккаунта? Зарегистрируйтесь'),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
