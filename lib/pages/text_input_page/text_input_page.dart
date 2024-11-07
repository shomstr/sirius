import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

class TextInputPage extends StatefulWidget {
  const TextInputPage({Key? key}) : super(key: key);

  @override
  _TextInputPageState createState() => _TextInputPageState();
}

class _TextInputPageState extends State<TextInputPage> {
  final TextEditingController _controller = TextEditingController();
  String _resultText = '';

  Future<void> _sendData() async {
    final String inputText = _controller.text;

    final response = await http.post(
      Uri.parse('http://127.0.0.1:8000/submit-text'),
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode({'text': inputText}),
    );

    if (response.statusCode == 200) {
      final data = jsonDecode(response.body);
      setState(() {
        _resultText = data['message'];
        print(data['message']);
      });
    } else {
      // Обработка ошибок
      setState(() {
        _resultText = 'Ошибка: ${response.statusCode}';
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Страница ввода текста'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            TextField(
              controller: _controller,
              decoration: const InputDecoration(
                labelText: 'Введите текст',
                border: OutlineInputBorder(),
              ),
            ),
            const SizedBox(height: 20),
            ElevatedButton(
              onPressed: _sendData,
              child: const Text('Отправить'),
            ),
            const SizedBox(height: 20),
            Text(
              'Результат: $_resultText',
              style: TextStyle(fontSize: 18),
            ),
          ],
        ),
      ),
    );
  }
}
