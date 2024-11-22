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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f0d8cc76-14ea-3e4b-a3e5-15dd7dbf13e1 | -3.4976 | -53.7935 | 2024-11-22 00:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 39b46610-0c44-37a7-b1f5-badc0b7355cb | -1.1857 | -51.948 | 2024-11-22 00:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 3745589d-618c-3293-8940-fcc0c892bbb6 | -4.2238 | -48.6342 | 2024-11-22 00:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 95.0 |
| dcf89862-b454-3a04-af75-04f1244d7e15 | -3.4778 | -45.9096 | 2024-11-22 00:20:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 94d6a210-6f87-3548-9c4e-35bcced169f3 | -14.558 | -54.7205 | 2024-11-22 00:20:00 | GOES-16 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 2b787919-bab2-3474-8a52-846f97a5e3da | -2.6965 | -46.2275 | 2024-11-22 00:20:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 101.9 |
| e973b1c8-cbba-37ae-b282-fb58ab13ec70 | -2.8504 | -44.9453 | 2024-11-22 00:20:00 | GOES-16 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 199e703b-0f25-321f-86c9-6ef3cae500cd | -1.1287 | -53.3951 | 2024-11-22 00:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 135.5 |
| 67eab105-30a1-342d-a634-ad8e1d2f1e3a | -3.516 | -53.793 | 2024-11-22 00:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 113.8 |
| 0ca89e21-cf9d-3b13-a26c-c90d1674b6f7 | -3.3338 | -53.3334 | 2024-11-22 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| bd210838-3775-355a-bddb-fc4b8b264eea | -3.4592 | -45.9104 | 2024-11-22 00:20:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 109.6 |
| 698ac6a0-f10b-3564-8222-3b19853b318a | -3.3451 | -50.5126 | 2024-11-22 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 122.7 |
| feafecc1-38dc-3f32-a2a1-6efa7ba8253c | -3.5159 | -53.8132 | 2024-11-22 00:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 114.8 |
| dfaeaeb7-b67f-3352-b403-ffa1adc87cb9 | -3.8355 | -52.2576 | 2024-11-22 00:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 105.4 |
| 9a65600e-c108-3bc6-80c5-ff751aa662db | -3.3452 | -50.4917 | 2024-11-22 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 100.0 |
| 8cc0b027-e6a6-3b6a-9eec-3ab1d336ccbf | -1.1287 | -53.4153 | 2024-11-22 00:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 62fd6bff-4f2b-30e5-8d32-6878eeb8b259 | -3.1831 | -54.3247 | 2024-11-22 00:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 100.4 |
| a8a33b12-8fa2-3fa9-b7d2-d93d110b6b9e | -2.6947 | -51.8597 | 2024-11-22 00:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 85e04082-49c1-3a09-bbd5-ff6efef2fb12 | -4.401 | -44.1215 | 2024-11-22 00:20:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 74cf9c88-7dbe-3bfc-98e9-0670e65ef377 | -4.2424 | -48.6334 | 2024-11-22 00:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 117.2 |
| a8ee9888-ba58-3abe-8ea1-81b323aded7e | -8.7228 | -66.7119 | 2024-11-22 00:20:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| a28a0b4e-e152-3c8e-a6a1-43b9ac4e9396 | -1.2041 | -51.9478 | 2024-11-22 00:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 3463def5-0c46-3d08-a0e5-55f6c7a3fda1 | -3.516 | -53.793 | 2024-11-22 00:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 108.0 |
| c61118ab-8d5d-376c-a5f6-5900e2618b4b | -4.2424 | -48.6334 | 2024-11-22 00:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 108.5 |
| 34542254-79ec-3b25-ba36-7444db5d15bf | -3.3452 | -50.4917 | 2024-11-22 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 101.4 |
| d089728d-9002-3e3d-9cf0-aa1fa53f550b | -3.8355 | -52.2576 | 2024-11-22 00:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 101.9 |
| ae007f99-8f7e-3e67-8aa9-bb36bc5a2afb | -2.5012 | -49.0162 | 2024-11-22 00:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| ac0d9074-d8ee-3c6e-a4fc-3043d400ec87 | -1.2228 | -51.7419 | 2024-11-22 00:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 8e81a807-a151-3100-8ab3-0034959a83a9 | -3.5159 | -53.8132 | 2024-11-22 00:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 110.7 |
| c956408c-8752-3030-b346-40030f1b9727 | -1.7892 | -53.6293 | 2024-11-22 00:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 8dd9a53d-d597-3b11-8917-2c4e73d75a5e | -3.4976 | -53.7935 | 2024-11-22 00:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 49fde8c8-a0a8-365a-84f8-e6093269b646 | -3.017 | -45.12 | 2024-11-22 00:30:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 54a1fffd-661c-3cea-9d17-a0b6fb1e16f5 | -2.9984 | -45.1207 | 2024-11-22 00:30:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 8f68a1c2-57b9-3ae3-a2a1-2028ddf88d92 | -2.504 | -54.1598 | 2024-11-22 00:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 845de97b-36ea-3795-b40f-1ad71792a703 | -1.2041 | -51.9683 | 2024-11-22 00:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| c417672a-4cfd-32fe-8bc5-545987f9af32 | -1.2041 | -51.9478 | 2024-11-22 00:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 113.5 |
| 6f6d44ab-5e26-3604-90c8-e307d8e8392c | -1.1857 | -51.9685 | 2024-11-22 00:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 32.2 |
| 71ff580b-2680-307d-8921-f4ff0241e99d | -2.6965 | -46.2275 | 2024-11-22 00:30:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 2adc6500-c92f-3fac-b6f8-900aed0fc19c | -3.7554 | -46.1204 | 2024-11-22 00:30:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 114.3 |
| afeff928-e449-3d41-bb73-ce04dad09b58 | -1.1103 | -53.3953 | 2024-11-22 00:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 93.6 |
| b0f42954-cee2-3763-ae8e-440b61be1559 | -3.1831 | -54.3247 | 2024-11-22 00:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 759d8523-f800-3f33-99ea-9a231e4405d1 | -4.2238 | -48.6342 | 2024-11-22 00:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 8eb96c83-c7d6-3b7b-a376-e2626dfb2829 | -3.3338 | -53.3334 | 2024-11-22 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 6e43e6d7-9693-36bf-9dd7-6dfa951a65f8 | -3.0169 | -45.1426 | 2024-11-22 00:30:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 2c468559-4dcb-3da1-bc49-515ab4ff36c4 | -1.1287 | -53.4153 | 2024-11-22 00:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 460acf86-93d0-33f1-ba80-29c3f30feb45 | -2.5013 | -48.9949 | 2024-11-22 00:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| ebc58b33-e4e9-3529-961f-90e1d7d3ec9f | -1.1857 | -51.948 | 2024-11-22 00:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 56931534-6a83-336b-b229-81a50386c105 | -9.2531 | -35.4539 | 2024-11-22 00:30:00 | GOES-16 | PASSO DE CAMARAGIBE | ALAGOAS | Brasil | 2706505 | 27 | 33 | nan | nan | nan | Mata Atlântica | 100.9 |
| c9586db8-40e6-36d9-a6f0-58b1b0a4d4c6 | -3.4975 | -53.8137 | 2024-11-22 00:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 49bc9889-1ac0-328d-afbb-b83df76ef878 | -3.4592 | -45.9104 | 2024-11-22 00:30:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 123.9 |
| 0b721b49-5da2-380f-9eb8-82e73d9671a9 | -2.8503 | -44.9679 | 2024-11-22 00:30:00 | GOES-16 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 74955545-c4fd-3d1c-a2ca-3e4aada92e8f | -1.2017 | -53.6769 | 2024-11-22 00:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 2f070e52-18e8-3ebd-8e96-d2ef4abe08c9 | -2.8504 | -44.9453 | 2024-11-22 00:30:00 | GOES-16 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 9d22df8c-18d1-3432-873b-d68f8bcd9a43 | -3.2768 | -53.8199 | 2024-11-22 00:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 2b9f3cea-04b3-35f1-b6e0-9735644b8c68 | -14.5577 | -54.7412 | 2024-11-22 00:30:00 | GOES-16 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 0d6e75e5-c875-3266-8577-5e45d4abdd52 | -3.4778 | -45.9096 | 2024-11-22 00:30:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 85.8 |
| d2f4a44e-7263-3b08-bcb6-87fbbd73514c | -3.774 | -46.1196 | 2024-11-22 00:30:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 989c47f0-54f9-3aa5-8c2c-0cfdb5a37e32 | -1.1287 | -53.3951 | 2024-11-22 00:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 120.8 |
| 78b133fc-aa0c-372d-a547-65cab60fc52f | -3.3451 | -50.5126 | 2024-11-22 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 120.6 |
| 6ece7e8a-0ffd-3e23-89d2-059c12430f7e | -3.2768 | -53.8199 | 2024-11-22 00:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 18990481-f3f2-3803-96b6-5a506c1b7e64 | -3.4406 | -45.9111 | 2024-11-22 00:40:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 70.0 |
| fdd2b087-4b7b-3906-b9f1-381db667ba86 | -3.4975 | -53.8137 | 2024-11-22 00:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 103.7 |
| e0fc88f3-b63e-30b3-aebd-f62a7f1089d8 | -1.1287 | -53.3951 | 2024-11-22 00:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 108.2 |
| 9ee4d6a5-e416-3c1b-baa1-a0fa622774ee | -5.9742 | -48.063 | 2024-11-22 00:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 55.5 |
| ab74917f-d25e-3b9c-b327-bdaa8ffa7309 | -1.7549 | -52.3913 | 2024-11-22 00:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 93fb9962-cb26-3377-9d01-874269d20aaa | -2.504 | -54.1598 | 2024-11-22 00:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| b1afa92f-c3cc-3b8a-b058-be2773bf172a | -1.7366 | -52.3916 | 2024-11-22 00:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 92c73061-ba3d-3a97-b6ac-996b22d9605d | -4.2424 | -48.6334 | 2024-11-22 00:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 121.5 |
| d0487217-9d6f-36dc-afb0-ff1e06b412d6 | -3.774 | -46.1196 | 2024-11-22 00:40:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 143.5 |
| 75f721c2-3316-30d6-b93d-4d25b193cc0f | -1.1287 | -53.4153 | 2024-11-22 00:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 43434559-a201-352f-84b7-b60f08da26f7 | -3.4593 | -45.8881 | 2024-11-22 00:40:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 9edcd44e-68d3-3c68-946d-deab96856685 | -1.1857 | -51.9685 | 2024-11-22 00:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 530e133f-589b-32dd-b1ce-4418dc4bb03f | -3.4592 | -45.9104 | 2024-11-22 00:40:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 190.3 |
| 09a65dd7-e61e-3474-903d-e456fe463a68 | -5.9744 | -48.0413 | 2024-11-22 00:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 698ec89a-2245-3492-b6ea-7509e04d3da6 | -2.504 | -54.1397 | 2024-11-22 00:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 84929c86-59b3-3cb2-812d-a21a7fef922d | -2.5013 | -48.9949 | 2024-11-22 00:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 50a18312-340c-3cba-b72d-99683236b8ae | -1.2041 | -51.9478 | 2024-11-22 00:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |
| af562a4a-0f32-3396-aedd-f47b50cc2533 | -3.516 | -53.793 | 2024-11-22 00:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 102.2 |
| 68fdf765-28ca-3426-8db4-74645d0d2610 | -5.9557 | -48.0425 | 2024-11-22 00:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 1ce59fe5-ade3-36e1-9261-29da7bbd7ed7 | -5.9556 | -48.0642 | 2024-11-22 00:40:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 3e1a4365-f85b-3250-a14c-81e0635e48db | -3.4778 | -45.9096 | 2024-11-22 00:40:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 2474e1d2-616c-3ef2-b388-0b0d5fd17c42 | -3.1831 | -54.3247 | 2024-11-22 00:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 100.1 |
| b60dc3fc-21ef-31ab-90d9-cd4514837674 | -3.8355 | -52.2576 | 2024-11-22 00:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 85da0df9-e353-30aa-a6a7-506c98ce3323 | -3.7555 | -46.0982 | 2024-11-22 00:40:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 72.8 |
| fcab460d-fd4d-3d1c-bc82-8931a0acbdc5 | -14.5577 | -54.7412 | 2024-11-22 00:40:00 | GOES-16 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 19a7c99f-a851-39ba-bf91-1a22cb1c1c08 | -1.2041 | -51.9683 | 2024-11-22 00:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 6133adb5-e98a-34e4-9cd1-e34b083201aa | -1.2017 | -53.6971 | 2024-11-22 00:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 0264c2fb-8dbc-32a9-9f4d-53130b0746c3 | -3.5159 | -53.8132 | 2024-11-22 00:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 121.5 |
| 06e2137d-b420-355b-91c1-a1590527f21e | -14.558 | -54.7205 | 2024-11-22 00:40:00 | GOES-16 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 64.9 |
| a5a9597f-27fe-34b7-93ae-597c364207b5 | -1.1857 | -51.948 | 2024-11-22 00:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 264fae9c-f9e5-3e98-8975-11bbc16fccc6 | -1.1103 | -53.3953 | 2024-11-22 00:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| f8a0f7c6-cf9f-3c02-b25c-f26652ff790e | -3.3452 | -50.4917 | 2024-11-22 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 100.9 |
| b5a60186-afe1-3649-ac84-e0bbc28744fc | -1.2017 | -53.6769 | 2024-11-22 00:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| bd34aede-0897-3e40-816a-1ccbec178670 | -6.2672 | -44.5442 | 2024-11-22 00:40:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| a73ed217-087f-347f-b28d-b00b820b5d17 | -3.4976 | -53.7935 | 2024-11-22 00:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 6d896f8e-2886-35cc-b772-1ff8c4fe386f | -1.2228 | -51.7419 | 2024-11-22 00:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 6ed9b976-fa1c-393e-a277-b848ddc1c99a | -3.7554 | -46.1204 | 2024-11-22 00:40:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 178.3 |
| 1142f629-f0f5-32c1-8820-f539b23296d4 | -4.1182 | -51.0486 | 2024-11-22 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 89c5256f-a604-3448-92b1-24e2806443bf | -3.3451 | -50.5126 | 2024-11-22 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 112.8 |
| c763163d-8256-3d5d-acec-d79ae0e7f58b | -1.7366 | -52.3916 | 2024-11-22 00:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |


[Clique aqui para ver as próximas entradas](README3.md)
