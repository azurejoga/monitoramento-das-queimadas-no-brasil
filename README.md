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
| 7f2e17ad-da3e-3a41-9dee-6f0cc8117d7e | -4.7857 | -45.1249 | 2025-11-06 00:00:00 | GOES-19 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 105.6 |
| f878e1fb-36a7-3444-b9d5-7fcb5af2501a | -4.0976 | -48.0144 | 2025-11-06 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| a17a9da7-c328-328c-8330-d325779c0c3d | -4.1161 | -48.0136 | 2025-11-06 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 100.0 |
| 51b6437e-1117-3cd8-89ed-54d4d2b79f5d | -3.4896 | -43.6846 | 2025-11-06 00:00:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| f8bab7fa-0a8a-38f7-aa5e-6362afa4b6f5 | -2.986 | -52.835 | 2025-11-06 00:00:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| ecd922c8-2700-3d49-8462-2bae38d888da | -4.4632 | -43.2386 | 2025-11-06 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 161.0 |
| 418d4c24-5c5b-3bcc-9167-f5941cb551e9 | -4.7012 | -46.5394 | 2025-11-06 00:00:00 | GOES-19 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 395b12b7-faa2-352f-9e51-5294de446e85 | -4.0292 | -46.9923 | 2025-11-06 00:00:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 110.9 |
| efd0354d-7b27-3d1e-a409-8f39617e90b9 | -7.506 | -44.5503 | 2025-11-06 00:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 122.3 |
| b58c2c45-1c3e-39f7-a2e8-eb4c001382ed | -3.7752 | -49.4219 | 2025-11-06 00:00:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 115.5 |
| c48722bf-cfb0-3173-95be-4144948060bb | -3.8397 | -44.4032 | 2025-11-06 00:00:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| f385fd53-2c45-33ce-8ffe-da532554c17a | -7.4871 | -44.5521 | 2025-11-06 00:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 174.0 |
| 43cc1cee-87fe-3b0e-ab24-deba31546b69 | -5.1533 | -41.2468 | 2025-11-06 00:00:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 77.4 |
| 94e652bf-2edb-3442-8bf8-191616b0ae16 | -4.5932 | -43.3471 | 2025-11-06 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 699.8 |
| 88a564e5-5def-3215-8253-d5580736fb53 | -7.4379 | -37.9002 | 2025-11-06 00:00:00 | GOES-19 | SANTANA DOS GARROTES | PARAÍBA | Brasil | 2513604 | 25 | 33 | nan | nan | nan | Caatinga | 81.0 |
| a65e3e71-6ca5-385b-bbc7-c6eb40a83af5 | -4.0476 | -47.0134 | 2025-11-06 00:00:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 6731962e-d63a-3a5c-aaea-570791ccc7bb | -4.0477 | -46.9915 | 2025-11-06 00:00:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 192.7 |
| cdcd21a1-5b88-327a-8339-b1758ab2ca2a | -3.4712 | -43.6392 | 2025-11-06 00:00:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 252.1 |
| c6520196-510b-3536-adbf-2906a7c34986 | -4.6121 | -43.3227 | 2025-11-06 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 284.3 |
| a1bced70-a513-3f4d-91d9-b635a6768cca | -4.4633 | -43.2152 | 2025-11-06 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 160.9 |
| 4235a320-4094-3e65-8ddf-a977d30705c7 | 0.4466 | -60.4873 | 2025-11-06 00:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 8ccaa257-2fe2-3122-b3e1-a0fae90adb22 | -3.4711 | -43.6623 | 2025-11-06 00:00:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 848.6 |
| 9ef5e5ee-0ffc-3bc2-a35f-848554878189 | 0.4877 | -50.8992 | 2025-11-06 00:00:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 0368c642-13bb-3fe7-a417-8eb3eb883fd7 | -4.5936 | -43.3006 | 2025-11-06 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 59.7 |
| df40b9bc-3acb-347e-ba6a-5d23a6fe5943 | -7.4686 | -44.5309 | 2025-11-06 00:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 91.9 |
| e7198c92-8d13-349c-b2e7-d1f75de91ee4 | -7.5062 | -44.5273 | 2025-11-06 00:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 182.7 |
| 36a6cdb2-9c63-3de6-b524-c5e0fdfe824f | -4.5747 | -43.325 | 2025-11-06 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 135.7 |
| c385ad94-d0c9-3c38-a75a-d4252faee858 | -3.7751 | -49.4431 | 2025-11-06 00:00:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 99.6 |
| c2e49948-cc31-3299-97b0-663090125c5e | -3.9324 | -47.6962 | 2025-11-06 00:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 120.9 |
| ebc24d1e-d75d-3738-bd42-ab391c4794f4 | -2.986 | -52.8146 | 2025-11-06 00:00:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 9f7cd871-5874-3d9f-8f68-19cbc780b846 | -4.6119 | -43.346 | 2025-11-06 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 342.9 |
| f6a5db62-988b-3a7c-93c1-7792956507ed | -3.4898 | -43.6614 | 2025-11-06 00:00:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 328.5 |
| 5d44b996-09c9-3678-9e98-935d89bb5e13 | -4.7014 | -46.5173 | 2025-11-06 00:00:00 | GOES-19 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 9a43b3de-6aa3-3da5-9b84-b7038df2bfa7 | -3.4899 | -43.6383 | 2025-11-06 00:00:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 114.2 |
| e24b1152-5af1-36c9-87fa-7c903bf4d51b | -7.9228 | -44.3251 | 2025-11-06 00:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 91.4 |
| bed78224-02ce-38fd-a336-a6d762a2144d | -3.471 | -43.6854 | 2025-11-06 00:00:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 157.0 |
| 483cda86-b16f-39fd-9a6b-b6b7908f0dfa | -3.9071 | -42.5436 | 2025-11-06 00:00:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 57.8 |
| 9a5d9116-1f76-3005-945c-b656e56dfb21 | -4.5934 | -43.3239 | 2025-11-06 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 588.0 |
| fb338fcd-8f15-3407-b2f9-9d66143338ca | -7.4874 | -44.5291 | 2025-11-06 00:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 260.5 |
| ccefc502-ee95-3d7a-8500-2447304d9cbb | -3.4231 | -54.0172 | 2025-11-06 00:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 8f4c1c91-1a2c-3f9d-a34c-95f9d9cd4b3b | -3.4525 | -43.6631 | 2025-11-06 00:00:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 0896a043-6ac8-3fc6-9460-c2ecd98d4964 | -3.8884 | -42.5446 | 2025-11-06 00:00:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 55.5 |
| a5c288a1-c52a-366b-9dbc-e3114e25368c | -3.621 | -43.5396 | 2025-11-06 00:00:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 58.2 |
| e44eda91-e7b7-3de1-a073-a8ddfc528166 | -3.0034 | -40.2326 | 2025-11-06 00:00:00 | GOES-19 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 54.3 |
| 7882974c-9395-3a66-a970-252a22c46892 | -2.893 | -53.122 | 2025-11-06 00:00:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 90dafcb1-6d01-3f4e-8e5a-671d4b083249 | -4.5745 | -43.3483 | 2025-11-06 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 152.4 |
| 197052a7-c1bb-3376-afc5-ee6e82f777a3 | -3.9071 | -42.5436 | 2025-11-06 00:10:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 55.6 |
| c6cca7f1-3b58-3463-92be-0635751fbe5c | -3.4231 | -54.0172 | 2025-11-06 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| c8375c98-a0c8-3a8a-b5cc-d4b942d3dea0 | -4.6121 | -43.3227 | 2025-11-06 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 244.0 |
| 460d5c41-f3ce-3366-b221-bf31b4e70850 | -5.1533 | -41.2468 | 2025-11-06 00:10:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 118.3 |
| 43607c95-837f-3935-adf1-d54031ae2850 | -4.0477 | -46.9915 | 2025-11-06 00:10:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 205.7 |
| 9d368df1-e378-3b37-aa7a-44d309a5573c | -7.4686 | -44.5309 | 2025-11-06 00:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 213.3 |
| 10700164-163f-3d30-8ee7-cc9a96c21ff7 | -3.4899 | -43.6383 | 2025-11-06 00:10:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 203.0 |
| bf83f72d-93c7-3aea-8bc2-cc1fcb3878cf | -4.5745 | -43.3483 | 2025-11-06 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 104.0 |
| f07eeabe-4a16-3642-92a4-c90e29d13106 | -4.5934 | -43.3239 | 2025-11-06 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 642.4 |
| 6c8bbae0-2a8a-309b-9c8c-1faa886599c5 | -4.72 | -46.5162 | 2025-11-06 00:10:00 | GOES-19 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 3385aede-7c19-3dce-8e24-b2e198c9351b | -3.3758 | -44.0582 | 2025-11-06 00:10:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 45.1 |
| a59a0b3d-51a6-35da-a50f-088624abce16 | -3.7752 | -49.4219 | 2025-11-06 00:10:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 115.9 |
| 36a450ac-d589-39da-9214-1f256f21b644 | -3.4898 | -43.6614 | 2025-11-06 00:10:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 400.4 |
| f9fadd51-8e86-3cb9-8d11-e10722e9b68a | -3.4711 | -43.6623 | 2025-11-06 00:10:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 829.9 |
| 9fc1b1f2-f6ad-30bd-ab3f-6c336d67885a | -4.1161 | -48.0136 | 2025-11-06 00:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 1636c909-5a16-3bc5-8e31-c0a5c7f1b16b | -3.4525 | -43.6631 | 2025-11-06 00:10:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 6c56619b-0741-3bbd-971f-9dbddfb30405 | -3.8397 | -44.4032 | 2025-11-06 00:10:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 291d1604-27f9-318b-b16d-1baa5112064a | -7.4871 | -44.5521 | 2025-11-06 00:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 214.6 |
| 9a4c84ff-521f-3777-9fae-a7c2af2589be | -4.7012 | -46.5394 | 2025-11-06 00:10:00 | GOES-19 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 05bffd80-d917-3948-a930-cbec5908211d | -2.986 | -52.8146 | 2025-11-06 00:10:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| f75911b1-d84b-33a5-af0a-564527159846 | -5.1531 | -41.271 | 2025-11-06 00:10:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 95.0 |
| 33f8d016-b7db-3367-967a-bd9af415228a | -4.0476 | -47.0134 | 2025-11-06 00:10:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 300001b2-2a17-3f7d-bb00-b2a79f238cb6 | -3.9324 | -47.6962 | 2025-11-06 00:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 118.6 |
| 617a7387-4f16-3627-bbc1-4605be591b66 | -7.4874 | -44.5291 | 2025-11-06 00:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 527.2 |
| 579f5615-2aae-30c6-954f-e302bd59a260 | -4.7855 | -45.1475 | 2025-11-06 00:10:00 | GOES-19 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 8f37a7fa-f856-34a7-a9c6-ed0e1c707562 | -4.6119 | -43.346 | 2025-11-06 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 218.4 |
| 53f122db-295a-3a57-ac36-b712bf3133a0 | -5.1345 | -41.2482 | 2025-11-06 00:10:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 69.9 |
| 6ecf5399-4b43-33e5-8d48-7b1ac43f2645 | 0.4283 | -60.4874 | 2025-11-06 00:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 73.0 |
| ca93aaf2-3670-3d70-b0ad-dbf2b7080aeb | -7.4683 | -44.5539 | 2025-11-06 00:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 148.9 |
| 704184a7-226f-3306-a7c0-71a204b969c0 | -3.471 | -43.6854 | 2025-11-06 00:10:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 66b99a92-77c2-35de-9b0b-74f12e249e0f | -3.4896 | -43.6846 | 2025-11-06 00:10:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 2024ef8d-9ec7-3d0e-8337-3134c70446b6 | -4.4633 | -43.2152 | 2025-11-06 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 132.2 |
| e393a264-7acc-3945-9ee1-4ad8e720dfbe | -4.7857 | -45.1249 | 2025-11-06 00:10:00 | GOES-19 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 93.5 |
| e4afe4df-c0ac-3b5e-9763-6dcb07338a65 | -4.0292 | -46.9923 | 2025-11-06 00:10:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 105.2 |
| a815987b-fe94-3537-85f3-405fc0770790 | -4.7198 | -46.5384 | 2025-11-06 00:10:00 | GOES-19 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 85.9 |
| cee92076-ba4f-396d-8630-fbf5166a19ab | -2.986 | -52.835 | 2025-11-06 00:10:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 0225e9c4-9dfb-3af9-a781-2bd4861de7d6 | -4.0976 | -48.0144 | 2025-11-06 00:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 5f8b25b4-2c42-34be-9792-a12592b8e483 | -3.621 | -43.5396 | 2025-11-06 00:10:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 33e4b31c-c3c3-320a-b603-0d14d0ec1d33 | -7.5062 | -44.5273 | 2025-11-06 00:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 198.7 |
| 2778436e-8389-311c-b568-cfe72454f60f | -7.9228 | -44.3251 | 2025-11-06 00:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 55b9ff8e-b964-3c96-a563-3a0d002e9f27 | -4.5747 | -43.325 | 2025-11-06 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 6a8dc18d-c1a0-304f-a60e-b0ab551e4626 | -6.2757 | -43.6675 | 2025-11-06 00:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 9f3644bb-da21-3869-b551-42a776bd67fb | 0.4466 | -60.4873 | 2025-11-06 00:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 3568b8d0-4aeb-3748-9933-103bed818b8b | -4.0479 | -46.9695 | 2025-11-06 00:10:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 81.4 |
| e557e5cf-0ed1-3fd9-8e35-14a26a9da7cf | -4.5932 | -43.3471 | 2025-11-06 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 523.7 |
| 68bdb171-389b-33d6-830c-a78dac9ef3cc | -3.4712 | -43.6392 | 2025-11-06 00:10:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 397.0 |
| be2d88b0-0b50-3de0-b419-052f21770ed7 | -4.593 | -43.3704 | 2025-11-06 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 90b2d5d1-a9d7-3928-afae-86f94914b7b4 | -7.506 | -44.5503 | 2025-11-06 00:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 61335f21-510d-35b5-88b3-4aa3a18a76b6 | -4.4632 | -43.2386 | 2025-11-06 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 148.8 |
| 6789987b-0ee4-3e3d-bc94-e243abdcd64c | -12.49878 | -42.9189 | 2025-11-06 00:11:00 | TERRA_M-M | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 9bfd207e-f255-327b-9247-097257ae7aa2 | -16.51843 | -41.64446 | 2025-11-06 00:11:00 | TERRA_M-M | ITAOBIM | MINAS GERAIS | Brasil | 3133303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.8 |
| b84f468d-4c77-3288-8cb5-a10ae7da600d | -11.88167 | -40.95754 | 2025-11-06 00:11:00 | TERRA_M-M | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 342948cf-6008-358d-b4ce-2e8c18aa2dfd | -16.67098 | -41.36036 | 2025-11-06 00:11:00 | TERRA_M-M | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 58818936-9065-35a0-8554-4bc9732c93b1 | -12.33435 | -43.64835 | 2025-11-06 00:11:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |


[Clique aqui para ver as próximas entradas](README2.md)
