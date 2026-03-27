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
| 53b78d25-fb4a-3555-b2cd-8604b7d10a66 | 0.8116 | -59.7256 | 2026-03-27 00:00:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 3b4aa8e4-71fa-329b-ba17-045bcf914f01 | 1.9405 | -61.3287 | 2026-03-27 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 72.4 |
| d31d763b-691c-3dfe-8d2a-f4a168ce36bf | 2.1601 | -60.8352 | 2026-03-27 00:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 58.4 |
| d5a44063-3ea9-3d1b-8218-9e881d3fd4e9 | 1.9405 | -61.3098 | 2026-03-27 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 03f14dc7-0666-33ae-8e93-fc39f6100699 | 0.8116 | -59.7066 | 2026-03-27 00:00:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 56e18e80-f394-3e1e-ba0e-6854b20147e4 | 1.9223 | -61.3289 | 2026-03-27 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 0ce29fef-c8b3-3cfa-a891-527e3323664b | 1.9405 | -61.3098 | 2026-03-27 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 5ec9b93c-6ae5-36e3-96d6-03367d1329d8 | 1.9405 | -61.3287 | 2026-03-27 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 73.9 |
| ced31b08-fa74-342f-8f32-d09d61b5c78a | 2.032 | -61.1013 | 2026-03-27 00:20:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 56.5 |
| c380643f-9ca0-32f9-b242-6d02990ca088 | -5.529 | -35.5218 | 2026-03-27 00:20:00 | GOES-19 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 82.0 |
| 66c3f4c4-473a-34cf-8846-2d82c22b9a7c | 2.1957 | -61.3637 | 2026-03-27 00:20:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 0865b6cb-1f21-3506-8be9-7a36c6dc63cf | 1.9405 | -61.3287 | 2026-03-27 00:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 65.1 |
| e516f536-27ec-355a-ad3d-6e96c7aae717 | 2.1957 | -61.3637 | 2026-03-27 00:30:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 693c8a47-4e57-37a8-8839-f86b73f8c529 | 2.1957 | -61.3449 | 2026-03-27 00:30:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 165a9791-a201-39c5-a709-c2f94e5c2681 | 2.1601 | -60.8352 | 2026-03-27 00:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 54.1 |
| b99c65cd-213e-3c0c-9e10-18e257a0dcdf | 2.032 | -61.1013 | 2026-03-27 00:30:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 8b3bc0b9-cb7e-3958-aab8-26ba1b181a28 | -23.78446 | -49.0407 | 2026-03-27 00:37:00 | TERRA_M-M | ITABERÁ | SÃO PAULO | Brasil | 3521705 | 35 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e115e5fb-15c0-3aca-8a2e-49a056e6551d | -23.78615 | -49.05168 | 2026-03-27 00:37:00 | TERRA_M-M | ITABERÁ | SÃO PAULO | Brasil | 3521705 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| aa2e4003-8209-3bd8-a837-db1aad366c05 | -22.26822 | -48.4638 | 2026-03-27 00:37:00 | TERRA_M-M | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 71f5070c-4a8f-3760-b068-476ac7c7bf4a | -26.46237 | -51.51091 | 2026-03-27 00:37:00 | TERRA_M-M | GENERAL CARNEIRO | PARANÁ | Brasil | 4108502 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| ad05d5be-5a00-3675-ad23-5d28005b5a26 | -22.27019 | -48.47596 | 2026-03-27 00:37:00 | TERRA_M-M | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 6e5bac22-c1dd-38b6-a5e2-8f06822eef7c | 2.1601 | -60.8541 | 2026-03-27 00:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 54.2 |
| ca820ea5-d745-366f-b68b-af02d333da2c | 2.1601 | -60.8352 | 2026-03-27 00:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 4f6b17e1-22a2-30b2-bf18-595503b8fe1e | 1.9405 | -61.3287 | 2026-03-27 00:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 65.2 |
| f29c1228-343d-3fff-b0cf-412dbfea99bf | 2.1957 | -61.3637 | 2026-03-27 00:40:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 42436622-7c43-3313-91c0-80307369b91b | 2.2139 | -61.3635 | 2026-03-27 00:40:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 51.2 |
| e731d8e3-ad83-3a88-882f-16afabc3c82d | 2.1957 | -61.3449 | 2026-03-27 00:40:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 60.3 |
| dfbc9885-2372-3e9c-9629-08e41bf90fa9 | -6.57042 | -51.11536 | 2026-03-27 00:41:00 | TERRA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| a63048a5-c764-3467-86ce-7a7a518d1f4b | 2.20495 | -61.3677 | 2026-03-27 00:43:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 79bdeb80-31c6-3438-8e9a-c6c5ada099be | -1.62378 | -54.60282 | 2026-03-27 00:43:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 46e4d66c-3530-32fb-a7d5-036a84c11e38 | 0.63772 | -59.7146 | 2026-03-27 00:43:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 2ecb40db-f16e-3027-b324-d177751803b7 | 0.62795 | -59.71321 | 2026-03-27 00:43:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 5a467736-9e75-31cd-81b8-96f48873be1b | 2.03702 | -61.10427 | 2026-03-27 00:43:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 290267b1-fe67-37c1-99f0-a54655362b22 | 2.20688 | -61.35426 | 2026-03-27 00:43:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 26.5 |
| d6480f98-4c92-3c8c-90c2-34cda4c12d8b | 0.63622 | -59.72551 | 2026-03-27 00:43:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 91f53fcf-cf30-324a-a920-d4467ece2deb | 1.93485 | -61.32466 | 2026-03-27 00:43:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 23713118-8f1b-3eb2-9ade-ce5061a35f74 | 0.7219 | -59.41687 | 2026-03-27 00:43:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 40a9e420-7251-3527-9886-4f89c0c841bd | 2.19615 | -61.35273 | 2026-03-27 00:43:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 49ea7bb0-4716-32e2-9a31-acce6dbbb2b7 | 4.0548 | -59.89233 | 2026-03-27 00:45:00 | TERRA_M-M | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 641f6e56-b94d-3312-ac62-6593528ebac9 | -22.259899 | -48.443901 | 2026-03-27 00:48:00 | METOP-B | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| debf2611-92ce-3c5f-b72a-974f59033650 | -22.2637 | -48.458 | 2026-03-27 00:48:00 | METOP-B | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 21cb0d48-6b4f-3253-883f-7b56c012bea7 | 2.1957 | -61.3637 | 2026-03-27 00:50:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 91.9 |
| c09d99c6-899c-3535-837a-c957e3255636 | 2.1957 | -61.3449 | 2026-03-27 00:50:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 52.5 |
| ff3f886e-9c06-3f9c-bfa6-2f428955ba6c | 1.9405 | -61.3287 | 2026-03-27 00:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 53.9 |
| d16bba63-c8c3-303d-bf29-711e68f9785e | 2.2139 | -61.3635 | 2026-03-27 00:50:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 48.8 |
| e9f4e6ac-e9de-390c-9daf-0d4ba3551af2 | 2.1601 | -60.8541 | 2026-03-27 00:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 4dde3946-dba8-302d-bbcb-1670f8cbe415 | 2.032 | -61.1013 | 2026-03-27 00:50:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 4a004acb-a511-3ffc-9519-c72a2d2fe118 | 2.1601 | -60.8352 | 2026-03-27 00:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 66.5 |
| b6822813-3f2c-3121-9499-2507740f4d83 | 2.1957 | -61.3637 | 2026-03-27 01:00:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 73dcd3b6-3c71-3cae-aced-4a01dc5c3c4a | 2.1957 | -61.3449 | 2026-03-27 01:00:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 62.4 |
| d7df56c2-5377-35f2-b3fe-daa81bff3ff7 | 2.2139 | -61.3635 | 2026-03-27 01:00:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 7d87b60c-d47c-3638-b28e-1588ee7d1d13 | 2.032 | -61.1013 | 2026-03-27 01:00:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 3dc9098a-d16f-33cb-a5a5-60a2f65d75d9 | 2.1601 | -60.8352 | 2026-03-27 01:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 7ed5c094-e685-3cde-998d-441aa29afc14 | 1.9405 | -61.3287 | 2026-03-27 01:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 06cf9344-c71e-350c-a642-6b5306e8258b | 1.1396 | -60.1046 | 2026-03-27 01:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 910b367e-ffb0-33a8-83ea-745bd7d05267 | 2.1601 | -60.8541 | 2026-03-27 01:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 2ca44059-01f6-3c91-9dad-9c7863c51b44 | 2.2139 | -61.3635 | 2026-03-27 01:10:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 55.9 |
| b6c1ee94-6115-384a-b952-20e31e6c1cc5 | 1.1396 | -60.1046 | 2026-03-27 01:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 15bad6c5-ab0d-32fb-a806-a9f35c13ca0e | 1.9405 | -61.3287 | 2026-03-27 01:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 0db00731-418f-37c2-89c8-1ff746fc677e | 2.1957 | -61.3449 | 2026-03-27 01:10:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 72.3 |
| bfc8f5e9-1818-3f75-829c-8e51eb5dae00 | 1.1396 | -60.1236 | 2026-03-27 01:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 891040cd-9638-398b-9414-36e9c4df161f | 2.1957 | -61.3637 | 2026-03-27 01:10:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 106.9 |
| baa94179-9818-30e8-a417-02da6b344b2b | 2.1957 | -61.3826 | 2026-03-27 01:20:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 554eeec3-af02-3afc-a869-324878648748 | 2.1957 | -61.3449 | 2026-03-27 01:20:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 28b2e0ff-2ea9-3c7f-948b-0ee320d692ee | 2.1957 | -61.3637 | 2026-03-27 01:20:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 149.8 |
| f4838331-afb7-3890-9f4c-c74845d75484 | 1.1396 | -60.1236 | 2026-03-27 01:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 09a4d8c8-fb7f-3109-97cb-80f274ae444e | 2.214 | -61.3447 | 2026-03-27 01:20:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 020a465d-b2a6-3579-9e1c-8458a6dc7c2d | 1.1396 | -60.1046 | 2026-03-27 01:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 51d737cf-ab21-30d8-9c8f-b2a2994cad81 | 2.2139 | -61.3635 | 2026-03-27 01:20:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 99.2 |
| 3dc4ff21-edcd-32d1-919e-1c5fd9cc0302 | 2.214 | -61.3447 | 2026-03-27 01:30:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 7156a68f-11f2-34d4-91aa-29960e16d68e | 2.1957 | -61.3637 | 2026-03-27 01:30:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 277.8 |
| 95cf8bb6-d45f-321a-81c6-1752958b4f4b | 2.1957 | -61.3826 | 2026-03-27 01:30:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 53.9 |
| ee018a7e-b6cd-389d-a7bb-fd2a63bad665 | 2.1957 | -61.3449 | 2026-03-27 01:30:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 110.8 |
| 859b6411-1fc3-30d2-a021-716d30b7593f | 2.2139 | -61.3635 | 2026-03-27 01:30:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 93.7 |
| f20a15ba-c0f0-36e7-9c29-312a8a38a0a4 | 2.1775 | -61.3639 | 2026-03-27 01:30:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 5f3179aa-3e17-34f0-b5c5-48b86b023d1f | 2.1957 | -61.3449 | 2026-03-27 01:40:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 55.3 |
| ae4344d6-8dcd-3d33-854c-2d30faa432d3 | 2.1775 | -61.3639 | 2026-03-27 01:40:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 68c88342-a972-3aa6-ae20-9ee1342f6870 | 2.1957 | -61.3637 | 2026-03-27 01:40:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 128.0 |
| 2d6904b3-3f21-388e-8d40-c51773d16b52 | 2.2139 | -61.3635 | 2026-03-27 01:40:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 9ece627a-8678-3ab7-84aa-dbf33824b504 | 2.214 | -61.3447 | 2026-03-27 01:50:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 0c2de66c-3727-335e-ba94-80e0a32a060a | 2.1957 | -61.3637 | 2026-03-27 01:50:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 162.3 |
| 063982e7-aa0f-3b60-99a6-77189c574189 | 2.2139 | -61.3635 | 2026-03-27 01:50:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 77.7 |
| d9ba09f4-aa5c-338c-91d1-890b80d79c36 | 2.1957 | -61.3449 | 2026-03-27 01:50:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 72.9 |
| f6a0fdeb-9a82-321c-b3b3-f8d4235bf7d2 | 2.1957 | -61.3449 | 2026-03-27 02:00:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 10f10fa4-451f-3608-85b0-3725c85abd81 | 2.2139 | -61.3635 | 2026-03-27 02:00:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 51.7 |
| a35efbee-7c83-37db-8c76-84939b04cd13 | 2.1957 | -61.3637 | 2026-03-27 02:00:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 154.1 |
| 53d01338-9bf3-3238-9c85-6f2e2023b3e2 | 2.1957 | -61.3637 | 2026-03-27 02:10:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 76a70904-193a-3bce-81b1-e83cd5dc4575 | 2.2139 | -61.3635 | 2026-03-27 02:20:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 5d2b4b92-05df-365a-90cc-9b09193c3220 | 2.1957 | -61.3637 | 2026-03-27 02:20:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 104.4 |
| d1cee908-a0fe-328b-ba71-5612625e2161 | 2.1957 | -61.3637 | 2026-03-27 02:30:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 75.2 |
| b4b5852d-90f3-389a-b4de-711d4ff7b8be | -5.51321 | -35.59262 | 2026-03-27 03:13:00 | NOAA-20 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b73a15ce-31da-352d-86a4-24a4f729b054 | -5.44698 | -36.7895 | 2026-03-27 03:13:00 | NOAA-20 | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 15da376e-4aaf-34a6-8e7a-5600521caef4 | -5.53103 | -35.51959 | 2026-03-27 03:13:00 | NOAA-20 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5f7687ab-af07-3b8d-b8c5-01b185c64b2a | -4.97041 | -37.40515 | 2026-03-27 03:13:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 11e1d56a-267f-3e69-a8c5-c45550c76af5 | -5.53052 | -35.52255 | 2026-03-27 03:13:00 | NOAA-20 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1807eb6b-71fc-3d40-bed3-85e4fefc4aaa | -5.53153 | -35.51666 | 2026-03-27 03:13:00 | NOAA-20 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 84f40a17-31de-35e0-b9db-6bfe317afcdc | -5.44634 | -36.7932 | 2026-03-27 03:13:00 | NOAA-20 | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1eb94083-7d13-32c1-95bd-8e8e06474216 | -4.96464 | -37.40414 | 2026-03-27 03:13:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ccb1aae4-e410-330e-a844-f2a16081eed7 | -5.5127 | -35.59557 | 2026-03-27 03:13:00 | NOAA-20 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c332bae1-d3cb-321a-b882-c54aba096e52 | -6.07574 | -37.30479 | 2026-03-27 04:02:00 | NOAA-21 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |


[Clique aqui para ver as próximas entradas](README2.md)
