import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:file_picker/file_picker.dart';

class UploadFilePage extends StatefulWidget {
  const UploadFilePage({Key? key}) : super(key: key);

  @override
  _UploadFilePageState createState() => _UploadFilePageState();
}

class _UploadFilePageState extends State<UploadFilePage> {
  String? _filePath;
  String _responseMessage = '';

  Future<void> _pickFile() async {
    FilePickerResult? result = await FilePicker.platform.pickFiles(
      type: FileType.any,
    );

    if (result != null) {
      setState(() {
        _filePath = result.files.single.path;
      });
    }
  }

  Future<void> _uploadFile() async {
    if (_filePath == null) {
      setState(() {
        _responseMessage = 'Пожалуйста, выберите файл для загрузки.';
      });
      return;
    }

    var request = http.MultipartRequest(
      'POST',
      Uri.parse('http://127.0.0.1:8000/upload_file'), // Замените на ваш URL
    );

    request.fields['user_id'] = '1'; // Укажите user_id
    request.files.add(await http.MultipartFile.fromPath('file', _filePath!));

    var response = await request.send();

    if (response.statusCode == 200) {
      final responseData = await response.stream.bytesToString();
      final data = jsonDecode(responseData);
      
      setState(() {
        _responseMessage = 'Файл успешно загружен: ${data['success']}';
      });
    } else {
      setState(() {
        _responseMessage = 'Ошибка загрузки: ${response.statusCode}';
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Загрузка файла'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            ElevatedButton(
              onPressed: _pickFile,
              child: Text('Выбрать файл'),
            ),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: _uploadFile,
              child: Text('Загрузить файл'),
            ),
            SizedBox(height: 20),
            Text(_responseMessage),
          ],
        ),
      ),
    );
  }
}
