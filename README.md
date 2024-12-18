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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 606281ed-d0a7-3535-b4ac-93088f0e8e42 | -1.7148 | -45.786 | 2024-12-18 00:00:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 136.2 |
| 83f88866-b62a-380d-ad14-8718f29a2696 | -2.2535 | -45.5943 | 2024-12-18 00:00:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 6170aa36-cfcf-330f-af90-877cc3fcd18a | -11.8455 | -43.8202 | 2024-12-18 00:00:00 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 103.0 |
| cee27d96-e4f8-33aa-8134-b12595a9c752 | -2.0816 | -54.2278 | 2024-12-18 00:00:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 56332c34-fcf1-3b78-bcbe-6e8b26656d62 | -4.5376 | -43.2807 | 2024-12-18 00:00:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 47f499f8-72ee-3ad9-b9e0-da61fd88aa08 | -4.0864 | -46.7255 | 2024-12-18 00:00:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 57.9 |
| d795ba4e-88dc-3fb2-9bef-8b11a596d4fc | -11.8648 | -43.8172 | 2024-12-18 00:00:00 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 188.9 |
| 26e61508-de4b-3fe4-b01f-16bb07c76bb0 | -1.7149 | -45.7637 | 2024-12-18 00:00:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 313fecc2-3faa-3f83-99a6-1acf8a23537f | -1.6963 | -45.7864 | 2024-12-18 00:00:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 158.1 |
| c0751b5b-d82f-3ad7-8e7a-2a3cf3fe3a22 | -4.9645 | -43.695 | 2024-12-18 00:00:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 96.4 |
| e16253f2-b8a0-37da-8134-293c8e79c97b | -5.9369 | -48.0654 | 2024-12-18 00:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 0e6d2cd0-6fb2-30a8-bbfb-6b27d04adde7 | -11.884 | -43.8142 | 2024-12-18 00:00:00 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 76.9 |
| eb752f60-ad0f-3e89-8a10-12c17e82edb9 | -1.6219 | -45.8548 | 2024-12-18 00:00:00 | GOES-16 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 52b69950-ed27-316b-a0ab-c75369863bd1 | -4.983 | -43.7169 | 2024-12-18 00:00:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 171.5 |
| c58e41a2-b16d-3c00-a17a-9af567a40d9b | -1.6963 | -45.7641 | 2024-12-18 00:00:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 2c0fc15d-4c0d-3421-9ccb-d259a9dd9fd2 | -20.7425 | -54.409 | 2024-12-18 00:00:00 | GOES-16 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 107.3 |
| afcca3ed-2251-3751-8868-a14f9be2a88d | -4.1236 | -46.7237 | 2024-12-18 00:00:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 60.6 |
| d3a65ef7-4745-39c7-87ee-b320befeacbd | -11.8643 | -43.8408 | 2024-12-18 00:00:00 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 117.5 |
| e79f615b-7368-318e-8438-17f1f06b885b | -5.3523 | -44.2913 | 2024-12-18 00:00:00 | GOES-16 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 117.1 |
| d9ca0c85-dc88-3718-a2ce-f784bc5e0b5e | -4.5375 | -43.304 | 2024-12-18 00:00:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 95.8 |
| be49e129-e9ce-38c0-8214-10d91a2b448e | -11.8451 | -43.8438 | 2024-12-18 00:00:00 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 63beb91e-f755-351d-b564-2797b01bdc23 | -5.9183 | -48.0667 | 2024-12-18 00:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 0487b655-5cc9-337b-a3c2-060c0b8e31b4 | -20.7421 | -54.4306 | 2024-12-18 00:00:00 | GOES-16 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 1410523f-8cd9-3fb2-bd17-ea1afe80c444 | -4.9641 | -43.7413 | 2024-12-18 00:00:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 99.7 |
| be9ca1be-1480-3ad9-bd43-71600eb7b52d | -9.9328 | -59.9247 | 2024-12-18 00:00:00 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 7a53bd8b-6c1a-3e0e-8361-b4469fecb617 | -4.9643 | -43.7182 | 2024-12-18 00:00:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 367.0 |
| 913a5d44-efa8-366a-997f-f993edf246f2 | -6.6334 | -47.34 | 2024-12-18 00:00:00 | GOES-16 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 35ad92e7-7989-3e15-951a-a150d9da7f8a | -4.105 | -46.7246 | 2024-12-18 00:00:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 89.3 |
| c3fbe218-bef1-3bb4-bf04-f0b64dc308cf | -4.96 | -43.72 | 2024-12-18 00:00:00 | MSG-03 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6304df13-c5b5-3deb-9b3b-77e5117c8ead | -5.3336 | -44.2926 | 2024-12-18 00:10:00 | GOES-16 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 2c7ef137-20fe-335c-8986-fbcce9e9978c | -4.5562 | -43.3028 | 2024-12-18 00:10:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 917a28ed-674e-3b3e-9318-47543c219a24 | -1.7149 | -45.7637 | 2024-12-18 00:10:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 84.7 |
| eac8fa59-11af-3e2f-941b-c5b5805f8ad9 | -1.7148 | -45.786 | 2024-12-18 00:10:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 125.7 |
| 45f587aa-e03a-3c1c-868f-bf7ad62e6a4a | -5.9369 | -48.0654 | 2024-12-18 00:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 93.9 |
| d66df5d2-b3f2-3eb6-9725-cae82ff6ab74 | -4.1049 | -46.7467 | 2024-12-18 00:10:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 56b9a41f-e777-3fec-923c-39188efeb0f6 | -20.7222 | -54.4124 | 2024-12-18 00:10:00 | GOES-16 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 86.7 |
| e04ecfa7-0d75-34fe-9fde-b38eb8615390 | -9.9141 | -59.9257 | 2024-12-18 00:10:00 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 620d9d98-19a9-3c4c-b214-0e007041b76b | -4.9643 | -43.7182 | 2024-12-18 00:10:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 373.3 |
| 5905653e-c83a-347c-a403-087353f10b9e | -1.6963 | -45.7641 | 2024-12-18 00:10:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 4c67a307-775c-389e-b86f-66a4fa428211 | -11.8455 | -43.8202 | 2024-12-18 00:10:00 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 67.9 |
| f24fb0a6-fab5-377f-a7cc-b14dfae5931b | -1.6963 | -45.7864 | 2024-12-18 00:10:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 120.0 |
| f21d0330-8006-3827-91de-51c6290215ce | -4.9641 | -43.7413 | 2024-12-18 00:10:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 37c38244-d6a4-36fc-9793-f1d592047642 | -5.9183 | -48.0667 | 2024-12-18 00:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 27f7c3aa-069b-3d71-afb6-612855763f54 | -4.983 | -43.7169 | 2024-12-18 00:10:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 386.2 |
| 66113115-ea12-3e38-ae99-7df9f35d074b | -1.6219 | -45.8548 | 2024-12-18 00:10:00 | GOES-16 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 3ba63b56-f88f-3368-a255-4e15d461e425 | -4.9832 | -43.6938 | 2024-12-18 00:10:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| c4ea138b-42c8-3e98-b7cf-68eb2b620b10 | -11.8643 | -43.8408 | 2024-12-18 00:10:00 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 190.0 |
| a2594a81-d35f-3dfd-8d3b-f321440d23a2 | -4.5375 | -43.304 | 2024-12-18 00:10:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 90.0 |
| c74ebd08-9be8-341e-b9e2-edbee0fc5c8a | -20.7425 | -54.409 | 2024-12-18 00:10:00 | GOES-16 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 51b91fba-bd16-316a-bf63-c2840cec60d8 | -4.9828 | -43.7401 | 2024-12-18 00:10:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 55273bea-0aab-39f5-82a4-fba153d3e73c | -4.9645 | -43.695 | 2024-12-18 00:10:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 89.6 |
| cc0fced1-b924-334d-b37d-58f6f9664ae9 | -9.9328 | -59.9247 | 2024-12-18 00:10:00 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 794726f8-3e06-3b00-8fbe-296704e8e665 | -11.8648 | -43.8172 | 2024-12-18 00:10:00 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 261.9 |
| 00204f70-ce5c-3d84-a432-79ca0eb44a4e | -4.5376 | -43.2807 | 2024-12-18 00:10:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 61c7049f-45a9-3871-86f8-25753470f471 | -4.105 | -46.7246 | 2024-12-18 00:10:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 99.4 |
| dcd76be9-00b5-300f-aceb-a8666373b8a4 | -4.105 | -46.7246 | 2024-12-18 00:20:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 70b18d80-cad6-3a1e-b9ed-2357f1e2affe | -4.1236 | -46.7237 | 2024-12-18 00:20:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 59.7 |
| d44398b7-f35a-3a4b-921d-5112c263d85f | -4.9641 | -43.7413 | 2024-12-18 00:20:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 78345a7c-8360-33b1-90c0-6b3d95e35b48 | -6.9718 | -43.56 | 2024-12-18 00:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 997de933-744c-30d6-824d-deacf28a5647 | -4.9832 | -43.6938 | 2024-12-18 00:20:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 95.1 |
| c9246715-4772-3371-98de-9007c1ff6e6d | -3.8805 | -47.021 | 2024-12-18 00:20:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 2ab4012f-5a6c-3b5b-a044-403894ab0dd1 | -5.3523 | -44.2913 | 2024-12-18 00:20:00 | GOES-16 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 5a56589e-fb13-3bca-9b27-4e6a7131ce4c | -6.6334 | -47.34 | 2024-12-18 00:20:00 | GOES-16 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 05918d7f-8f3b-3cc6-8dd2-ca0ad08256d1 | -11.8455 | -43.8202 | 2024-12-18 00:20:00 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 02ee06e0-c110-3a65-8815-0e642b2b8032 | -3.4969 | -53.9547 | 2024-12-18 00:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 304307ee-f42b-3958-b045-74664ca18ed7 | -5.9369 | -48.0654 | 2024-12-18 00:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 717e9a6a-1c73-3bc6-82a9-5addf11d2146 | -20.7425 | -54.409 | 2024-12-18 00:20:00 | GOES-16 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 3ee176c8-938f-34ab-9121-fab60775d9e7 | -11.8451 | -43.8438 | 2024-12-18 00:20:00 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 71c6ef7d-f148-37e0-8e8f-dcc869671067 | -11.8643 | -43.8408 | 2024-12-18 00:20:00 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 186.1 |
| 10f665c4-c149-3f44-9ae7-7db868ec31d9 | -4.983 | -43.7169 | 2024-12-18 00:20:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 447.8 |
| 3ef85120-282c-3781-8eb9-436487e9b979 | -4.9643 | -43.7182 | 2024-12-18 00:20:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 390.0 |
| a80cb7e6-4f3f-3e40-886d-ee90061ca593 | -1.6963 | -45.7864 | 2024-12-18 00:20:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 119.8 |
| c76b3811-a037-33e0-99a9-450653fd636e | -3.7682 | -47.1794 | 2024-12-18 00:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 6bf24a2b-de68-3de7-84d4-0114914e1cef | -4.1049 | -46.7467 | 2024-12-18 00:20:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 59.1 |
| a65845b2-373b-3a96-8737-efddc6320e18 | -9.9141 | -59.9257 | 2024-12-18 00:20:00 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 50386af7-bf97-3681-8246-44940759b456 | -4.9828 | -43.7401 | 2024-12-18 00:20:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 1740ec2e-6bfe-3cf0-94ac-f21efbb5d536 | -5.3336 | -44.2926 | 2024-12-18 00:20:00 | GOES-16 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| ad0d9ac7-879c-31fa-9b4a-3332c780f673 | -5.9183 | -48.0667 | 2024-12-18 00:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 85a38cda-a463-3634-92ef-827baca6d34c | -1.7148 | -45.786 | 2024-12-18 00:20:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 7238651e-64ed-3b15-9cd3-5dd2fb026040 | -4.9645 | -43.695 | 2024-12-18 00:20:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 0e3075c5-e81c-330b-bdc9-5dcb76fdbca7 | -3.8619 | -47.0218 | 2024-12-18 00:20:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 9abdd4f8-95be-3c96-bbea-6db5fa39a18a | -6.9906 | -43.5582 | 2024-12-18 00:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 77cf8769-8564-39b2-83f4-89d2301b101e | -3.7868 | -47.1786 | 2024-12-18 00:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 7a52f01d-7dfd-31d7-8abd-4b472dde0964 | -11.8648 | -43.8172 | 2024-12-18 00:20:00 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 279.5 |
| 84d9698f-d2ce-334d-a319-e6f86f957fdd | -1.6219 | -45.8548 | 2024-12-18 00:20:00 | GOES-16 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 82.7 |
| a34f9e32-1ee8-3495-b9f8-496301bb2783 | -1.6963 | -45.7641 | 2024-12-18 00:20:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 83.7 |
| e1abc1e1-14bc-37b5-903a-60b1749a59c6 | -11.79904 | -37.97646 | 2024-12-18 00:20:00 | TERRA_M-M | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 91998026-c19e-3b8c-b9d6-b1581d3c267a | -11.16947 | -40.42767 | 2024-12-18 00:20:00 | TERRA_M-M | CAÉM | BAHIA | Brasil | 2905107 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 86f96783-f599-330d-a646-e8607ee4d3bc | -12.38066 | -41.15968 | 2024-12-18 00:20:00 | TERRA_M-M | WAGNER | BAHIA | Brasil | 2933406 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 626d375d-b6b9-3fa3-83f8-a2f8d8a9b9a3 | -10.60705 | -37.03306 | 2024-12-18 00:20:00 | TERRA_M-M | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 55.5 |
| 0e51de5b-77ab-3d94-9811-c07fa912e58c | -10.60539 | -37.02205 | 2024-12-18 00:20:00 | TERRA_M-M | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 15.6 |
| 5b3c5ad2-eea3-34ee-8475-20caecb287ba | -5.83431 | -44.08322 | 2024-12-18 00:22:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| cfb2cd24-b4b1-38d2-8f71-48be6b8c6513 | -9.46323 | -40.87736 | 2024-12-18 00:22:00 | TERRA_M-M | SOBRADINHO | BAHIA | Brasil | 2930774 | 29 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 57ccbef3-6591-3c44-a8df-a37ce62c90ef | -10.75974 | -40.33326 | 2024-12-18 00:22:00 | TERRA_M-M | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| ef48ed97-bd8a-3907-b0ec-d162cff80262 | -4.92855 | -43.96378 | 2024-12-18 00:22:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 96c1b912-e48a-3f7c-a8c9-40a3595967f4 | -4.4421 | -38.05493 | 2024-12-18 00:22:00 | TERRA_M-M | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 2ab58f9e-58c9-327c-b5cf-e9ff2cac12bf | -6.55379 | -44.49403 | 2024-12-18 00:22:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 7b716a49-91e4-394a-b653-1b80d34cf4ad | -6.98142 | -40.63476 | 2024-12-18 00:22:00 | TERRA_M-M | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 23ca7ce3-925f-3fca-bc03-524db4401be7 | -5.22127 | -44.90518 | 2024-12-18 00:22:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 0cf3cf5f-e7fc-3eb0-8557-8e7606dad574 | -6.97256 | -40.63603 | 2024-12-18 00:22:00 | TERRA_M-M | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |


[Clique aqui para ver as próximas entradas](README2.md)
