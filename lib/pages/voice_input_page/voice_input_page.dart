import 'package:flutter/material.dart';
import 'voice_input.dart';

class VoiceInputPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Audio Recorder'),
      ),
      body: Center(
        child: Recorder(
          onStop: (String path) {
            ScaffoldMessenger.of(context).showSnackBar(
              SnackBar(content: Text('Запись сохранена: $path')),
            );
          },
        ),
      ),
    );
  }
}
