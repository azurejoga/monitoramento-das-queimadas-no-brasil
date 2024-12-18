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
| ba58fb58-f12b-3f67-9b8b-95bd66aa8311 | -15.23855 | -59.92747 | 2024-12-18 05:46:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc7c16a2-8880-329c-8292-53adb6ce8aec | -15.09329 | -59.6416 | 2024-12-18 05:46:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5b1103a1-3901-3b8a-9646-7cd08c15d78d | -15.24394 | -59.92291 | 2024-12-18 05:46:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 83dea39d-007c-3125-b802-6f9769345b8f | -15.23792 | -59.93272 | 2024-12-18 05:46:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ce9623f4-3b14-307a-b897-a9d3d821ec68 | -15.08846 | -59.641 | 2024-12-18 05:46:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6a78c1b7-5862-3212-9d74-ceff4b3f374c | -15.07814 | -59.64514 | 2024-12-18 05:46:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e4f73532-0648-35e0-b86d-7184abe34f8f | -15.08779 | -59.64638 | 2024-12-18 05:46:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e43b6c8c-96c7-3979-8d51-ab9438efae6c | -12.02126 | -62.79462 | 2024-12-18 05:46:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 229cd1d3-f244-3309-804e-515270231416 | -15.08296 | -59.64577 | 2024-12-18 05:46:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0f03805f-044e-3eef-bd95-512adc390451 | -15.23728 | -59.93796 | 2024-12-18 05:46:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5b6213e7-0809-3120-808d-2a94a9941298 | -12.01749 | -62.79406 | 2024-12-18 05:46:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2a8e7303-32b7-3a54-b06f-73ecf93bfd09 | -20.73379 | -54.42063 | 2024-12-18 05:48:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c0afe1d6-010f-3bd1-a686-198d475d3081 | -20.72666 | -54.42013 | 2024-12-18 05:48:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| da9831a5-fe72-3ab3-8541-ed158bc8efd0 | -22.07273 | -56.20319 | 2024-12-18 05:48:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 767014b6-e4ae-3dfe-9cdb-0e9248506a3e | -4.983 | -43.7169 | 2024-12-18 05:50:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 107.1 |
| e3577ee8-7f87-3413-8003-fd5be674fd82 | -4.9643 | -43.7182 | 2024-12-18 05:50:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 809e48df-1040-3470-ae02-258f6cd72ade | -4.983 | -43.7169 | 2024-12-18 06:00:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| a6d01dcc-1526-3254-8596-7f36f998b947 | -4.9643 | -43.7182 | 2024-12-18 06:00:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 80292e12-a777-3c18-942b-7684e058420a | -15.08219 | -59.6497 | 2024-12-18 06:09:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9633981f-069d-35ec-ad62-3fb4148e53bf | -15.09008 | -59.64325 | 2024-12-18 06:09:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d3a11ac0-c998-3ebc-899f-647795bc717b | -15.24077 | -59.93614 | 2024-12-18 06:09:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 485b4939-d3c2-30c2-bc0a-507fcb2da7b7 | -15.23371 | -59.93531 | 2024-12-18 06:09:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 312bf3fc-31e2-35b9-9ade-8fb52b1a583d | -15.24145 | -59.92921 | 2024-12-18 06:09:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 169dd1f6-be08-38f0-a9ce-99af432dd2a6 | -4.983 | -43.7169 | 2024-12-18 06:10:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 1896d902-c9c4-30af-91ae-ea6af0f6b8b7 | -4.9643 | -43.7182 | 2024-12-18 06:10:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 88.0 |
| d9f38073-6c34-3989-bf86-a9ba119aafba | -4.983 | -43.7169 | 2024-12-18 06:20:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| ec85427a-b729-3c4e-ab7f-fd977dfb0ab1 | -4.9643 | -43.7182 | 2024-12-18 06:20:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 4ef535e8-4647-3bfe-b038-872b1d05f7a4 | -4.9643 | -43.7182 | 2024-12-18 06:30:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 99.7 |
| e2bdaaba-b83b-3ce7-8de6-a43fb3038290 | -4.983 | -43.7169 | 2024-12-18 06:30:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 356af62d-5a29-3c46-9d62-40c41f6beca0 | -4.9643 | -43.7182 | 2024-12-18 06:40:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 17fd7414-c9ae-3fa9-add3-d96d56f13320 | -4.983 | -43.7169 | 2024-12-18 06:40:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 52bedab9-f926-36cf-acd0-aee02c2d9596 | -4.2244 | -45.4492 | 2024-12-18 06:50:00 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 45.6 |
| f2f673b9-e5e7-36d7-97b2-2b44a0203005 | -4.2243 | -45.4717 | 2024-12-18 06:50:00 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 46.5 |
| e47c0185-f99f-3733-ace1-a846529ec470 | -4.983 | -43.7169 | 2024-12-18 06:50:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 1f134e9e-e76e-342e-abe1-21d3dc78d419 | -4.9643 | -43.7182 | 2024-12-18 06:50:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 7121cb85-737e-30a1-be6f-d2264a5767ed | -4.9643 | -43.7182 | 2024-12-18 07:00:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 194be4c6-2590-395b-9ca4-188d5da8bd8b | -4.983 | -43.7169 | 2024-12-18 07:00:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 2fce4ca9-1c36-3bd5-8523-a970c44ba543 | -4.2244 | -45.4492 | 2024-12-18 07:00:00 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 23b9b222-be62-3896-b8a3-f02c0caa3d36 | -4.2243 | -45.4717 | 2024-12-18 07:00:00 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 01003132-bc3c-3c61-9f44-63a560e6468c | -4.9643 | -43.7182 | 2024-12-18 07:10:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 59.6 |
| c1182ca3-c83f-34b2-bae3-80044639d542 | -4.983 | -43.7169 | 2024-12-18 07:10:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 13a6ac8c-974b-35f5-80dd-ed72d8f3f7c3 | -4.9643 | -43.7182 | 2024-12-18 07:20:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| a5d9bab1-4ed9-33da-870f-db2d9b48ae64 | -4.2244 | -45.4492 | 2024-12-18 07:20:00 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 953b2137-7b4c-3048-a403-e2c3c1cf8bc9 | -4.983 | -43.7169 | 2024-12-18 07:20:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 3aff81b2-446e-3772-a098-b092a3516ba0 | -4.2243 | -45.4717 | 2024-12-18 07:20:00 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 49.2 |
| a013cbe4-bddb-3d55-bfed-95a2957e232d | -4.2243 | -45.4717 | 2024-12-18 07:30:00 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 63ad939c-860d-3179-9cb5-67b2abaa5d7d | -4.2244 | -45.4492 | 2024-12-18 07:30:00 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 5d29b535-abbb-35f3-8253-39be922cdf3f | -4.983 | -43.7169 | 2024-12-18 07:30:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| cf4fada5-4827-3885-9c1f-f07f69677f04 | -4.9643 | -43.7182 | 2024-12-18 07:30:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 2c32c648-3f02-326d-9c2a-f1123eb6f7b8 | -4.2244 | -45.4492 | 2024-12-18 07:40:00 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 29e377e3-c8f0-31e5-91eb-6a0f51acbf1a | -4.2243 | -45.4717 | 2024-12-18 07:40:00 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 23cf703e-b13a-3094-b88e-fa3d5bccda68 | -4.983 | -43.7169 | 2024-12-18 07:40:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 75.8 |
| d14a28b3-17a5-36b9-a713-e148ee5eecd3 | -4.2244 | -45.4492 | 2024-12-18 07:50:00 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 57f1741c-b6ae-3d72-a727-7582b4bac812 | -4.9643 | -43.7182 | 2024-12-18 07:50:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 3412a194-bd1a-32ee-abb0-8a5a836f7596 | -4.983 | -43.7169 | 2024-12-18 07:50:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| bad77eb3-6f48-3c1e-9bf7-4e731e4afdd3 | -4.2243 | -45.4717 | 2024-12-18 07:50:00 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 53586c4e-2179-3c6f-89bf-32f120e699f5 | -4.9643 | -43.7182 | 2024-12-18 08:00:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| caff97cb-7639-334f-84d6-264ee1d14b3e | -4.2243 | -45.4717 | 2024-12-18 08:00:00 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 46.9 |
| e5cb204f-8685-3db1-9dd8-c2b2b3271ef2 | -4.9643 | -43.7182 | 2024-12-18 11:50:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 6936a08a-6d76-35b4-9cc5-5ab1e66ede5d | -4.9643 | -43.7182 | 2024-12-18 12:00:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| b6ccc564-8bdf-34b7-a518-d5b3c065a575 | -4.9643 | -43.7182 | 2024-12-18 12:10:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 0f6a9ccf-b704-3156-874d-bc8518421cbe | -4.9643 | -43.7182 | 2024-12-18 12:20:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 6a19330e-912a-3e49-9fa5-6396b3c0aff8 | -4.983 | -43.7169 | 2024-12-18 12:20:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 3b8d6c7a-4673-37e9-9a6a-f43c2cb89b31 | -4.9643 | -43.7182 | 2024-12-18 12:30:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 119.4 |
| b6f83689-4669-35aa-aa5b-65693bb2ee0e | -6.9592 | -42.9994 | 2024-12-18 12:30:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 97.1 |
| 3e9ba215-30d9-30f6-8394-d289b7590aa8 | -4.983 | -43.7169 | 2024-12-18 12:30:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 124.0 |
| d3cb1168-a005-3328-aa50-e09629c24d97 | -4.9643 | -43.7182 | 2024-12-18 12:40:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 5ce8ca71-cc62-32fe-b93b-af3d0a3dadea | -4.983 | -43.7169 | 2024-12-18 12:40:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 114.7 |
| e597dbdc-881b-3f2f-8311-1c0ea903c9f2 | -2.53604 | -45.54351 | 2024-12-18 12:44:00 | TERRA_M-T | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 19891b0e-3a4b-37c5-8f1b-f8799f51ba8b | -3.52112 | -41.96577 | 2024-12-18 12:44:00 | TERRA_M-T | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 128.8 |
| 1d8cbfa3-c2be-34a4-ac55-59d4a740165f | -3.51867 | -41.98413 | 2024-12-18 12:44:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 117.0 |
| 0d9a419e-8d5a-394d-bef6-4f89297f504c | -4.36563 | -47.32286 | 2024-12-18 12:44:00 | TERRA_M-T | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 70288a7e-3aba-3367-b26e-eaeaa154174f | -3.89391 | -46.10024 | 2024-12-18 12:44:00 | TERRA_M-T | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 3aa40be5-cad0-3980-aa34-9787594c85d1 | -4.12114 | -43.56317 | 2024-12-18 12:44:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 566be3ea-6bf4-3e7c-9a4a-2c203b5d94bd | -3.18896 | -44.48727 | 2024-12-18 12:44:00 | TERRA_M-T | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 2bec939f-d6d8-385e-8dc1-98702871613c | -3.89528 | -46.09054 | 2024-12-18 12:44:00 | TERRA_M-T | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 86d64455-88c8-3010-a8a5-4af4ba95ca03 | -6.94546 | -42.99847 | 2024-12-18 12:44:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 22.5 |
| 352d3fe5-ca2f-3f72-adbf-c4c9ed417921 | -2.85896 | -41.99246 | 2024-12-18 12:44:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 36.6 |
| 3a1e28ba-87c6-3905-b5a6-ec9c930fb894 | -6.95751 | -43.00011 | 2024-12-18 12:44:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 69.6 |
| 5d7caaec-e315-3667-bab3-e2a4cc1677bf | -8.04375 | -38.5303 | 2024-12-18 12:44:00 | TERRA_M-T | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 163.5 |
| b7985fd6-b2a4-347b-9564-a5a518fec206 | -3.21795 | -42.70156 | 2024-12-18 12:44:00 | TERRA_M-T | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 23.0 |
| c5603f62-3b8b-3714-97cf-9f796ae0b019 | -1.77209 | -46.04266 | 2024-12-18 12:44:00 | TERRA_M-T | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 63.1 |
| fd87b05d-3723-369d-a900-35f973b1f6cb | -4.09225 | -41.60584 | 2024-12-18 12:44:00 | TERRA_M-T | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 16.2 |
| 64cb0074-c8bc-36e0-a1df-234b82d0d133 | -0.33438 | -48.52264 | 2024-12-18 12:44:00 | TERRA_M-T | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 6cd6ae5a-27b4-35a8-b101-f61b1fd3bc02 | -4.97147 | -43.71875 | 2024-12-18 12:44:00 | TERRA_M-T | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 148.7 |
| 898b9498-87cf-3e90-a588-e078e7f6a8c9 | -2.89473 | -42.21564 | 2024-12-18 12:44:00 | TERRA_M-T | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 53.6 |
| e5655863-babf-3adf-b5ce-e3f302cc22c7 | -1.4042 | -46.67882 | 2024-12-18 12:44:00 | TERRA_M-T | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| f64d46a6-dd68-34d0-9b7d-d7790db59c72 | -4.08498 | -44.58687 | 2024-12-18 12:44:00 | TERRA_M-T | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 45271947-fcee-3243-94e8-3f6c04db545b | -4.02938 | -41.96994 | 2024-12-18 12:44:00 | TERRA_M-T | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 71.0 |
| 3dc6e7d2-bbb0-3cd8-9ea6-9153491d4a95 | -3.20635 | -42.70002 | 2024-12-18 12:44:00 | TERRA_M-T | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 3d013b69-4ac8-391a-b3f9-7e8ee390f17f | -2.849 | -42.06289 | 2024-12-18 12:44:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 6e55ae8c-30fa-37ba-bcdd-5cb10a4123e1 | -4.15411 | -43.56749 | 2024-12-18 12:44:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 1d8df361-382c-3b06-8460-e93f072fdfc9 | -0.3357 | -48.51349 | 2024-12-18 12:44:00 | TERRA_M-T | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 505def07-1531-3af7-acdf-093beb6169c0 | -6.91054 | -42.84631 | 2024-12-18 12:44:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 79.2 |
| 11fb75b3-1a4e-3a0f-bbad-b4528baac507 | -4.11954 | -43.55717 | 2024-12-18 12:44:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 95fbd566-3856-334a-a2a0-7e91fb2e743b | -2.53748 | -45.53352 | 2024-12-18 12:44:00 | TERRA_M-T | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 4e86ac2d-6586-36e4-b7a5-deb27195088e | -3.15335 | -44.45216 | 2024-12-18 12:44:00 | TERRA_M-T | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 5ca1178c-638c-351e-9bf7-2de7384817ba | -3.5161 | -41.97726 | 2024-12-18 12:44:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 140.3 |
| ba92f0c3-7d78-3a88-9b63-62bc7b71ce51 | -2.92775 | -45.24813 | 2024-12-18 12:44:00 | TERRA_M-T | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 6d7627e5-1406-3a48-a9be-6e5170082b69 | -5.3887 | -43.35111 | 2024-12-18 12:44:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |


[Clique aqui para ver as próximas entradas](README22.md)
