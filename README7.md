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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 080ac9a1-d02a-329a-b195-5e1d0c0a4143 | -3.9071 | -42.5436 | 2025-11-06 00:40:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 60.0 |
| ce7a12ad-fad2-3043-9e29-ef40229e2062 | -5.7589 | -40.81 | 2025-11-06 00:40:00 | GOES-19 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 80.8 |
| 36af3777-061a-334c-9c83-68fdad438840 | -4.72 | -46.5162 | 2025-11-06 00:40:00 | GOES-19 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 159.5 |
| b240919e-3fa1-347d-b3c3-751b8585a0d6 | -4.7014 | -46.5173 | 2025-11-06 00:40:00 | GOES-19 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 122.3 |
| 5c366fbc-fc57-3963-8a61-42c364e9c254 | -3.4899 | -43.6383 | 2025-11-06 00:40:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 500df01c-1e66-3a46-98d5-0386b9bcecc5 | -4.6119 | -43.346 | 2025-11-06 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 239.9 |
| 1ff1f02c-1eeb-3841-99ae-b19aad8a6349 | -4.5934 | -43.3239 | 2025-11-06 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 844.0 |
| e18f44cb-a7f7-38e3-bff3-8c398c8ecff0 | -7.5062 | -44.5273 | 2025-11-06 00:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 148.4 |
| 28020912-44da-3ed1-b8af-24cc881d78e4 | -4.6121 | -43.3227 | 2025-11-06 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 278.5 |
| cc2a4a12-388e-3be9-a6d6-1fd87912d11a | -4.593 | -43.3704 | 2025-11-06 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 4c2f099b-bb32-3f5c-aa3d-16392d670026 | -3.7752 | -49.4219 | 2025-11-06 00:40:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| fd745795-6925-3d6f-b234-6c0efb925bc6 | -4.0479 | -46.9695 | 2025-11-06 00:40:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 6ed16de5-2eb0-3314-b462-1cbeed7d38d6 | -3.4711 | -43.6623 | 2025-11-06 00:50:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 186.2 |
| 7754f68f-b8eb-30b1-bc1b-d4b6fea5de17 | -3.4712 | -43.6392 | 2025-11-06 00:50:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 134.9 |
| 0b2b9a84-16c0-3137-a42a-580a574b7301 | -4.72 | -46.5162 | 2025-11-06 00:50:00 | GOES-19 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 0cede0d5-02be-384a-b640-08126e259f27 | -4.0476 | -47.0134 | 2025-11-06 00:50:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 102.9 |
| d0ba3383-f388-3a0c-919d-353587ce8e2e | -2.986 | -52.8146 | 2025-11-06 00:50:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 4951346f-a819-33ca-b7aa-8a6b99a159eb | -3.4231 | -54.0172 | 2025-11-06 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 9000d86e-f6c4-3e38-be9b-effb8c64c5af | -3.4898 | -43.6614 | 2025-11-06 00:50:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 410f399e-3105-3aed-9bf7-105bf72d0c44 | -4.5747 | -43.325 | 2025-11-06 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 474b9ddb-aa9e-3e61-9b4a-fcc7ea8bd2b9 | -4.5934 | -43.3239 | 2025-11-06 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 311.2 |
| 7f0fee38-20ed-328b-93d7-e5648d4d43ed | -5.7966 | -40.8068 | 2025-11-06 00:50:00 | GOES-19 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 73.6 |
| 95b456da-b28e-39c9-8e30-552fc8c23a1e | -3.9071 | -42.5436 | 2025-11-06 00:50:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 55.5 |
| c990370d-00c2-3e9f-b3a4-020130d063d8 | -4.7014 | -46.5173 | 2025-11-06 00:50:00 | GOES-19 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 112.1 |
| 3f3d73da-24a6-307b-9c6a-c71e6d25c726 | -9.5534 | -40.3254 | 2025-11-06 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 73.0 |
| 4919b84c-a996-3e64-97ae-7c5ceeb44c3c | -3.9324 | -47.6962 | 2025-11-06 00:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 665601c1-1c54-3936-bff2-c3d0781adeaa | -4.029 | -47.0143 | 2025-11-06 00:50:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 961801fd-a0b3-3f28-8e7a-dfd62269cf0b | -5.1533 | -41.2468 | 2025-11-06 00:50:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 71.7 |
| dd2aab91-2861-356d-8e92-9c1f95fc9abe | -4.7012 | -46.5394 | 2025-11-06 00:50:00 | GOES-19 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 91828c95-5be5-3a13-aa61-fc8901231fdd | -4.6121 | -43.3227 | 2025-11-06 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 219.3 |
| cc3eb12d-09f1-3725-88af-f2264c156052 | -4.5745 | -43.3483 | 2025-11-06 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 98.4 |
| b27857cf-e4d0-33aa-88e9-6a5f553aee62 | -4.5932 | -43.3471 | 2025-11-06 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 356.9 |
| a277046b-4b0a-3073-8db2-ff5c58f76bee | -4.4633 | -43.2152 | 2025-11-06 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 106.6 |
| d3311e52-6c2d-3a78-a8d1-bc7d46284260 | -4.4632 | -43.2386 | 2025-11-06 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 58f0de46-a1c2-30dd-be46-92167d596180 | -4.7857 | -45.1249 | 2025-11-06 00:50:00 | GOES-19 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 9cffb67d-185a-3d7b-ba01-6edd37c80348 | -4.0477 | -46.9915 | 2025-11-06 00:50:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 218.4 |
| db884f77-f708-30f6-bc37-46f2655a96c1 | 0.4283 | -60.4874 | 2025-11-06 00:50:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 80.4 |
| b5a8c008-bbef-3149-9b76-cf21d20cdffa | 0.4466 | -60.4873 | 2025-11-06 00:50:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 98.5 |
| 43d4e0f2-87e6-36bf-a494-d26767dcf1a7 | -3.4899 | -43.6383 | 2025-11-06 00:50:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 49.9 |
| cb0907b4-a376-3e7e-b879-b95238299e1b | -4.6119 | -43.346 | 2025-11-06 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 249.2 |
| 418c4d8b-67e4-35b8-abaa-ca51a3acbb37 | -7.4874 | -44.5291 | 2025-11-06 00:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 126.4 |
| ba787acc-3f1f-3689-8db0-8f5d7410a78c | -7.5062 | -44.5273 | 2025-11-06 00:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 159.8 |
| 19377a14-af89-3276-a807-072bd95b4d7e | -4.1161 | -48.0136 | 2025-11-06 00:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 109.3 |
| 4278a094-842f-3036-b7ee-c5bb3eb86537 | -4.0292 | -46.9923 | 2025-11-06 00:50:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 158.3 |
| f222b185-5ac3-3029-ade8-32e16adfff4c | -5.1533 | -41.2468 | 2025-11-06 01:00:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 73.9 |
| eabaac74-908c-3cd3-8fb9-9e8795123dba | -4.5747 | -43.325 | 2025-11-06 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 340fe189-29fe-330f-a83a-01ccb237b38c | -4.0477 | -46.9915 | 2025-11-06 01:00:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 233.5 |
| 13e1bfb3-8e2c-3bf1-9f82-4d82f1724fc7 | 0.4466 | -60.4873 | 2025-11-06 01:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 8b192fe8-58ba-3515-8f0e-8c5b11115527 | -9.9919 | -36.0871 | 2025-11-06 01:00:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 82.8 |
| 8337a7fe-48f8-37ec-9615-1f2404f2fa73 | -4.5932 | -43.3471 | 2025-11-06 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 278.0 |
| cb6b1194-de30-3b34-9d95-57ca760e1c21 | -5.1531 | -41.271 | 2025-11-06 01:00:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 71.5 |
| ad5ae990-398a-3b4c-acb6-4de633ac8611 | -3.4899 | -43.6383 | 2025-11-06 01:00:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 034a7662-dbf3-3120-bed4-41e41ee1864e | -9.9924 | -36.0599 | 2025-11-06 01:00:00 | GOES-19 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 89.1 |
| 57cc3f8d-73fe-3dc8-abb8-eb1c53c9ddf1 | -7.5062 | -44.5273 | 2025-11-06 01:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 9ef48b60-4327-301e-a24a-274fc7879926 | -9.5343 | -40.3282 | 2025-11-06 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 100.7 |
| 32a514d7-6675-3518-bc61-e69927bdd6d4 | -7.4871 | -44.5521 | 2025-11-06 01:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 1803f1f3-c437-3237-be89-9f3dee2bf08c | -3.4712 | -43.6392 | 2025-11-06 01:00:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 194.0 |
| 3d7f3c81-1304-36a2-a865-5ab8fbbd5b46 | -4.4632 | -43.2386 | 2025-11-06 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 8275a13a-bdd3-3064-8d0b-264acf601e48 | 0.4283 | -60.4874 | 2025-11-06 01:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 156a900e-c745-30d3-9329-73e33e37ee86 | -4.1161 | -48.0136 | 2025-11-06 01:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 3478c74c-3816-3816-ac70-ad34adb75312 | -4.6121 | -43.3227 | 2025-11-06 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 182.5 |
| f6d6bb85-354e-369e-8aa7-5d991fceb78a | -3.4711 | -43.6623 | 2025-11-06 01:00:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 208.0 |
| bd7ad44f-d3f0-3506-92a1-9f841a0a4166 | -3.9324 | -47.6962 | 2025-11-06 01:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| f7b71547-0acf-3ec0-8c3f-d5ce5747364f | -4.5745 | -43.3483 | 2025-11-06 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 3a8932b8-7803-37d6-8b30-a439fae6f095 | -4.6119 | -43.346 | 2025-11-06 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 164.5 |
| dd023ca5-dcbc-3780-b70e-059195fb24bd | -4.5934 | -43.3239 | 2025-11-06 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 308.1 |
| 943f9e54-1a5c-3a61-974b-116449cf06d2 | -7.4874 | -44.5291 | 2025-11-06 01:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 164.0 |
| a931d343-d4d8-3529-8038-c01950f57125 | -4.4633 | -43.2152 | 2025-11-06 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 3207c506-39e3-35b0-8d70-71fc3303c05f | -4.2824 | -45.1305 | 2025-11-06 01:00:00 | GOES-19 | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 68.8 |
| e62d474d-4068-39e7-9f91-99d27ac0c104 | -3.4898 | -43.6614 | 2025-11-06 01:00:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 080aeb9f-10e3-3538-beee-d5bfa51aa6d0 | -4.0292 | -46.9923 | 2025-11-06 01:00:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 104.5 |
| df0e482b-5118-3411-958d-ad5cbeee9a7f | -9.5534 | -40.3254 | 2025-11-06 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 191.1 |
| e920cd86-6313-3454-8f22-deab366286b9 | -2.986 | -52.8146 | 2025-11-06 01:00:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 7130249c-55b4-3662-9a30-898a5b655b80 | -9.4761 | -40.3862 | 2025-11-06 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 74.7 |
| af4f5ac3-57dc-3661-92fa-0ed6bc4a8006 | -4.7857 | -45.1249 | 2025-11-06 01:00:00 | GOES-19 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 31dc4099-59ce-30a1-b3d4-04bdd5ba241c | -9.9731 | -36.0634 | 2025-11-06 01:00:00 | GOES-19 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 86.2 |
| 0e0d989b-673c-398a-838e-c40a8dc9d6ca | -9.9726 | -36.0905 | 2025-11-06 01:00:00 | GOES-19 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 78.3 |
| 5054d33d-c0be-38d9-8f9e-0cd495719c72 | -4.0476 | -47.0134 | 2025-11-06 01:00:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 77.5 |
| c22356b2-68db-32f5-b006-3d61717dae63 | -3.4231 | -54.0172 | 2025-11-06 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 165b33a9-2b76-3937-9e9a-88baa34a3741 | -4.5934 | -43.3239 | 2025-11-06 01:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 324.7 |
| 508e991a-69e2-3ac9-8816-f75a017fecd6 | -4.4633 | -43.2152 | 2025-11-06 01:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 2ffd606c-36c8-3692-9255-51ae6d55ea17 | 0.4283 | -60.4874 | 2025-11-06 01:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 25395416-4fb3-3725-8ba0-3c3755f4468d | -3.4711 | -43.6623 | 2025-11-06 01:10:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 219.6 |
| 44609340-8e94-3938-aecc-42848312c3ec | -2.986 | -52.8146 | 2025-11-06 01:10:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| e746e497-33e6-3291-a38a-86e42ff9853a | -9.5534 | -40.3254 | 2025-11-06 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 247.0 |
| d5dd8b67-8968-3d40-8bb1-397d784c0823 | -4.5747 | -43.325 | 2025-11-06 01:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| ff58825f-9a0f-389b-8c10-227b824e4917 | -4.6119 | -43.346 | 2025-11-06 01:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 146.6 |
| 4388e84a-35ca-34ec-a739-3e0c5da5b6e4 | -7.4874 | -44.5291 | 2025-11-06 01:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 267.3 |
| 9b538aa9-53cf-38a5-b319-aec8c326d898 | -4.0477 | -46.9915 | 2025-11-06 01:10:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 189.1 |
| 0bb4e107-7101-304d-87d5-b235c482b450 | -7.4686 | -44.5309 | 2025-11-06 01:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 88.4 |
| a4d77f57-9782-33d9-91f1-fa7fd4b7efca | -3.4526 | -43.64 | 2025-11-06 01:10:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 45.7 |
| dd42dbd9-39ea-38bc-a730-741abbdf2b72 | -9.553 | -40.3503 | 2025-11-06 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 80.6 |
| 9249e492-88e7-3307-8ed8-1cdd01e8326b | -4.5932 | -43.3471 | 2025-11-06 01:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 258.5 |
| 95de01b2-8eaa-349e-aeef-0e0c106dde07 | 0.4466 | -60.4873 | 2025-11-06 01:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 16ce06d6-e41a-317b-87e1-539e6f80b78e | -9.5725 | -40.3227 | 2025-11-06 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 76.9 |
| a019baca-2cdd-3554-b877-9ba92f22fc7d | -7.4871 | -44.5521 | 2025-11-06 01:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 33d838bc-db9f-3fc7-8b8c-754964cf681d | -3.4898 | -43.6614 | 2025-11-06 01:10:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 395e32d0-35b7-3750-a00c-042ae77d5878 | -7.5062 | -44.5273 | 2025-11-06 01:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 118.7 |
| b6c948a6-fae3-3909-80d1-5700eb397ac4 | -5.1533 | -41.2468 | 2025-11-06 01:10:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 115.6 |
| 1253109a-9fde-31a2-a05d-8f501fe0992f | -5.1531 | -41.271 | 2025-11-06 01:10:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 95.1 |


[Clique aqui para ver as próximas entradas](README8.md)
