import 'package:flutter/material.dart';
import 'package:hive/hive.dart';
import 'package:http/http.dart' as http;
import 'package:sirius/pages/mian_page/main_page.dart';
import 'dart:convert';

class RegistrationPage extends StatefulWidget {
  const RegistrationPage({Key? key}) : super(key: key);

  @override
  _RegistrationPageState createState() => _RegistrationPageState();
}

class _RegistrationPageState extends State<RegistrationPage> {
  final _formKey = GlobalKey<FormState>();
  String username = '';
  String email = '';
  String password = '';

  Future<void> _register() async {
    if (_formKey.currentState!.validate()) {
      try {
        final response = await http.post(
          Uri.parse('http://10.0.2.2:8000/register'), 
          headers: {'Content-Type': 'application/json'},
          body: jsonEncode({
            'email': email,
            'password': password
          }),
        );

        if (response.statusCode == 200) {
          final responseData = jsonDecode(response.body);

          if (responseData.containsKey('id')) { 
            int id = responseData['id'];
            var box = await Hive.openBox('userBox');
            await box.put('id', id);
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
                SnackBar(content: Text('Ошибка регистрации: Отсутствует идентификатор пользователя.')));
          }
        } else if (response.statusCode == 409) {
          ScaffoldMessenger.of(context).showSnackBar(
              SnackBar(content: Text('Ошибка: такой пользователь уже существует')));
        } else {
          ScaffoldMessenger.of(context).showSnackBar(
              SnackBar(content: Text('Ошибка регистрации: ${response.statusCode}')));
        }
      } catch (e) {
        ScaffoldMessenger.of(context).showSnackBar(
            SnackBar(content: Text('Ошибка сети: $e')));
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Регистрация')),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Form(
          key: _formKey,
          child: Column(
            children: [
              TextFormField(
                key: ValueKey('username'),
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
                key: ValueKey('email'),
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
                key: ValueKey('password'),
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
                onPressed: _register,
                child: Text('Зарегистрироваться'),
              ),
              SizedBox(height: 20),
              TextButton(
                onPressed: () {
                  Navigator.pop(context);
                },
                child: Text('Уже есть аккаунт? Войдите'),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
