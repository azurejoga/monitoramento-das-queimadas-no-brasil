# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d364c57d-b6ae-351f-a50a-8b49448a5319 | -11.5364 | -56.45527 | 2025-06-07 04:46:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c4f4cf83-19a4-3f47-b4f5-5ecc96d4fe7a | -12.32506 | -52.47967 | 2025-06-07 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f455f8af-81d6-394b-835a-e645b8f3ba07 | -14.04239 | -55.13785 | 2025-06-07 04:46:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f57d6784-0787-3bce-8095-cdbe84e3f728 | -13.89029 | -54.66422 | 2025-06-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a95e642-1479-3c1f-9f36-04cd56dbfb33 | -14.74525 | -45.10085 | 2025-06-07 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0fd4eda7-0b08-3234-8a4e-a7b7e0fc7479 | -11.5419 | -56.44634 | 2025-06-07 04:46:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6f1ee0e-f420-325a-878f-48297c6c445b | -12.20877 | -49.63354 | 2025-06-07 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 81c0e29b-1c0d-3f61-a2bc-5ae9b33f153f | -18.23422 | -47.94154 | 2025-06-07 04:46:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f0a1e664-8572-3051-aa25-7a2965f70d65 | -14.74538 | -45.09126 | 2025-06-07 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| af3730e8-cd0c-3d2e-883d-68093d783a82 | -10.29874 | -57.14156 | 2025-06-07 04:46:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f80988e-9bde-351e-bb0a-0d82c691b48b | -11.25308 | -60.80669 | 2025-06-07 04:46:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 39a5cacc-e574-3f89-b5e4-c7b43adc8b9f | -17.12956 | -45.2664 | 2025-06-07 04:46:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9228a3dd-86f3-3875-9904-577dae928d2d | -17.26457 | -42.65627 | 2025-06-07 04:46:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ac74a2b5-53cf-3fdf-b157-494c91450bdb | -14.73281 | -45.08296 | 2025-06-07 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 93cf9cdb-c72c-3808-b54f-94a71a3788f3 | -17.25957 | -42.65406 | 2025-06-07 04:46:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4dd84833-b3f7-3f70-97a7-d8294f3618e6 | -13.29006 | -58.01093 | 2025-06-07 04:46:00 | NOAA-20 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 819f1fc9-948c-3de7-8533-8df5cdc9abd4 | -11.83857 | -60.92509 | 2025-06-07 04:46:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2fd3bf3f-8237-3172-b539-956da4b3d612 | -12.32617 | -52.47263 | 2025-06-07 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 48e71411-0e1f-33cf-950f-f1f4f1a6b705 | -13.06351 | -49.24511 | 2025-06-07 04:46:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5315d1f8-e4c9-334c-a0d2-6024e5dd41fe | -12.33004 | -52.46965 | 2025-06-07 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 39e8c5f8-017e-30c6-b225-976abe885f5f | -11.67624 | -54.55326 | 2025-06-07 04:46:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 164dae2f-7cc0-3822-a0a0-52673056f420 | -17.80772 | -51.0132 | 2025-06-07 04:46:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 799c1dc8-258e-3f3c-971f-9801267f50d0 | -13.51618 | -56.5602 | 2025-06-07 04:46:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 313777ea-a0e7-36d1-a154-78de3db6c844 | -12.27695 | -50.09935 | 2025-06-07 04:46:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 48f5017d-3589-3102-8c11-eec8372d6f75 | -11.41098 | -55.08022 | 2025-06-07 04:46:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9aa961de-aae8-3b4c-9e22-32bd404306ed | -14.73765 | -45.08348 | 2025-06-07 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6dd23990-0bb5-309b-93df-ec80fec059b5 | -11.53892 | -56.4409 | 2025-06-07 04:46:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27c9e4f9-2106-321c-bcf0-be6916fa2a4c | -12.29138 | -50.09761 | 2025-06-07 04:46:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ea10a899-c63c-35ad-9416-e926f48694b2 | -12.33335 | -52.4702 | 2025-06-07 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d9572c7-86b2-3c1a-af8b-1d271e05f486 | -10.69432 | -57.64712 | 2025-06-07 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a9d312a2-9dcc-3c4f-85fc-15eb6aa7b143 | -12.70972 | -58.0262 | 2025-06-07 04:46:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc9d63c6-2407-3969-9595-801845755891 | -12.33112 | -52.48427 | 2025-06-07 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8c642b87-4ae9-3244-8aa4-e18df7e309bf | -12.53559 | -45.41368 | 2025-06-07 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c7bf0892-85cf-3ddf-87a9-50bba513c24a | -13.07139 | -49.2419 | 2025-06-07 04:46:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9ef8748e-7b92-3dc0-8e94-a399ad5722c8 | -13.28155 | -57.94024 | 2025-06-07 04:46:00 | NOAA-20 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 22698879-df98-3b90-b405-23bd73b4946a | -13.30322 | -57.93661 | 2025-06-07 04:46:00 | NOAA-20 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f3ed3529-c94d-3b10-ade8-1b085d75dbe9 | -12.27983 | -50.10376 | 2025-06-07 04:46:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1c56c43d-02ac-3618-bfdb-7b15fbd37c30 | -12.7807 | -48.71933 | 2025-06-07 04:46:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 5122d6be-f428-3a85-91d2-c3149ccfbc12 | -14.03546 | -55.13658 | 2025-06-07 04:46:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8507dca2-06a6-3845-bd00-b7426472dbcf | -10.67144 | -57.63072 | 2025-06-07 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d25bc132-a79e-3464-bb79-e78f26e5851c | -12.32837 | -52.48021 | 2025-06-07 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dfb713d5-d1f1-3bc1-8777-74c3618a52e2 | -12.33666 | -52.47074 | 2025-06-07 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cee2f535-3d91-397e-ba55-aefd1cba6009 | -12.69718 | -58.24083 | 2025-06-07 04:46:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1e59f11d-dd29-34b6-9d84-a712e9e3f207 | -14.72666 | -45.0837 | 2025-06-07 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f743fe66-073d-34c5-b208-ec701e88d094 | -11.54572 | -56.44702 | 2025-06-07 04:46:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 696e5ce9-7113-373d-a12e-8e9d5226471f | -14.03892 | -55.1372 | 2025-06-07 04:46:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d9f85463-3ab9-3371-8829-a3a69290777b | -10.63422 | -55.0192 | 2025-06-07 04:46:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e92748c-b04f-3ed0-aa18-ba44791fe5e7 | -14.02738 | -55.13174 | 2025-06-07 04:46:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c7621f24-48f4-3165-8d9d-158259c7b182 | -12.96355 | -46.76456 | 2025-06-07 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3005a282-f25d-3a23-85ca-0263c25dee59 | -17.81123 | -51.01376 | 2025-06-07 04:46:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 86fa888f-f8df-3a6c-9ef6-8ed6cce1fde7 | -11.7123 | -56.45432 | 2025-06-07 04:46:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46972f87-8666-3fa8-9429-db36f6ba6f33 | -13.07077 | -49.24618 | 2025-06-07 04:46:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 523eeaef-3373-3abd-b3da-e964dae46c08 | -11.14161 | -53.9219 | 2025-06-07 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45889d48-cbaf-33c8-bbeb-27bcd67e74a3 | -14.21926 | -45.48599 | 2025-06-07 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 03c9f6fc-b043-33fd-ad4d-80d926b64711 | -11.78583 | -47.40193 | 2025-06-07 04:46:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1f6b38ca-92df-3449-b65c-b767c2268d54 | -11.8986 | -63.32516 | 2025-06-07 04:46:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b6cfd1aa-f155-390f-8d4d-3d5b7d511334 | -10.29467 | -57.14085 | 2025-06-07 04:46:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c7b4a1f-4b07-3802-a909-100350b5cf54 | -16.97665 | -49.72616 | 2025-06-07 04:46:00 | NOAA-20 | VARJÃO | GOIÁS | Brasil | 5221908 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8eaf2c7f-79e6-3a70-977c-2a75e7e5ecc0 | -11.42394 | -54.29868 | 2025-06-07 04:46:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 21d50337-ba58-3fb3-809a-0ee10a8aedfe | -13.46947 | -56.85127 | 2025-06-07 04:46:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 745c158a-a0a9-310f-a731-a3eb7e572122 | -17.27085 | -42.65271 | 2025-06-07 04:46:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 82e9dcd2-b9c8-34f3-8587-c063e4248ceb | -11.25482 | -60.79734 | 2025-06-07 04:46:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 66377835-0075-3e13-b9d3-4657f5c9ae00 | -11.26499 | -60.79938 | 2025-06-07 04:46:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74c1b6ca-0f09-36ea-a6f0-13aad2a5ff30 | -15.07939 | -48.94618 | 2025-06-07 04:46:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 36f64f28-6c8b-3c2b-9782-e158ff8a590e | -14.72384 | -45.07621 | 2025-06-07 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 29df681a-a4f4-3b8b-9c36-d6a629385d1d | -10.88197 | -54.30873 | 2025-06-07 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 961c5ec2-756e-3e7a-9c4f-b294fe6b8491 | -14.03479 | -55.1405 | 2025-06-07 04:46:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4fecd9a5-2dc8-3baf-9ff5-4a3907d46c7d | -12.33168 | -52.48075 | 2025-06-07 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 55b2d850-1d13-3447-8b77-4be3d2972ef6 | -11.53731 | -60.99616 | 2025-06-07 04:46:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 80ef5020-d179-3565-be1b-435530649cf1 | -11.89461 | -56.40863 | 2025-06-07 04:46:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be99dee0-f9d0-3926-9699-b589ef02978f | -12.28964 | -50.10923 | 2025-06-07 04:46:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1b7d016c-ae78-3cc3-8ac7-4c649810aac0 | -11.68666 | -54.55497 | 2025-06-07 04:46:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b66e69b-d17f-3cd6-97a4-56763c665b7b | -14.74472 | -45.09675 | 2025-06-07 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6853f34c-0d23-361a-9abc-9456ddc89aec | -13.66069 | -47.70692 | 2025-06-07 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e2e387c4-8ec8-3ece-9815-1908554aa062 | -11.25596 | -60.7912 | 2025-06-07 04:46:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 096819b6-05b6-30b0-8fb0-4f206700861e | -17.11116 | -49.14368 | 2025-06-07 04:46:00 | NOAA-20 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 66fcb014-3099-3f19-b74b-7e6ad2558801 | -11.25026 | -60.79348 | 2025-06-07 04:46:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1a586382-b2c0-3932-8751-6dba7f52acef | -12.47339 | -46.34299 | 2025-06-07 04:46:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1a381fa7-3ba8-3760-b113-ca28d6975311 | -11.53808 | -56.44567 | 2025-06-07 04:46:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c0b2bb2-c3c2-3cf8-a1fe-d8f5db29a9c7 | -13.07564 | -49.23817 | 2025-06-07 04:46:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2d5f21a8-fd8e-397c-adf7-83358d80c658 | -14.74408 | -45.10213 | 2025-06-07 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aa0627d4-0da7-30c5-8e49-7e3e28b53452 | -11.41454 | -55.08082 | 2025-06-07 04:46:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e168f9e1-babd-3fa1-a489-83eb0225005a | -14.7315 | -45.08426 | 2025-06-07 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8f2b7bf7-ef25-32b9-9bee-bbaf8a8d8fbf | -13.09167 | -52.29002 | 2025-06-07 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f6eb69f5-8508-3a7d-8939-e23aa47a9bf2 | -12.33499 | -52.4813 | 2025-06-07 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ba19485e-c3a2-3d3a-916a-68c24bf570fa | -14.74054 | -45.09078 | 2025-06-07 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 86cb398a-4c93-3c6c-b6d2-be15efea85ed | -14.89981 | -48.11061 | 2025-06-07 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 96ac2ba4-3210-3514-8eb7-f8d5e53892e8 | -14.02673 | -55.13566 | 2025-06-07 04:46:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ff2ceb3-fb80-395b-b2f5-ae40213ef292 | -12.27637 | -50.10323 | 2025-06-07 04:46:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 07a21d94-bae6-3588-86ff-e850391e0664 | -12.32561 | -52.47615 | 2025-06-07 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d7bdc35b-9997-31da-b38e-8a848e146d3a | -12.33554 | -52.47778 | 2025-06-07 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 717e82c1-b08d-3580-9582-07e897b40cbe | -12.29485 | -50.09814 | 2025-06-07 04:46:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 59a56780-ac4c-39c6-91b4-dcd535fb2097 | -14.21989 | -45.48101 | 2025-06-07 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1727d1fb-a0b5-3259-b6b1-5df8f673a4de | -11.36495 | -56.55453 | 2025-06-07 04:46:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a4d20b3f-73cc-3731-89e7-73a28a49195d | -12.38657 | -47.31313 | 2025-06-07 04:46:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 763717b5-1f1d-3860-86c4-9df6546ad3e8 | -12.3245 | -52.48319 | 2025-06-07 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ac7a0792-25e6-3c22-89bd-3ac22000304f | -14.88457 | -48.11129 | 2025-06-07 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| de7571aa-3c46-3d42-a97f-49f286b8775d | -12.37801 | -47.31556 | 2025-06-07 04:46:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1d37c1df-5acb-30a5-8e48-304634fa4a49 | -10.53541 | -56.38944 | 2025-06-07 04:46:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a00abc4-f83c-3e74-8f22-c9ef2e39dc04 | -11.38587 | -56.54819 | 2025-06-07 04:46:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README22.md)
