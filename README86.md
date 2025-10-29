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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 58ea3cdc-12b9-3a59-9e6e-523052e0400b | -4.5157 | -38.7741 | 2025-10-29 13:30:00 | GOES-19 | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 219.2 |
| 64720f8d-e92a-33af-9448-1cd8a34889fe | -6.1249 | -41.8414 | 2025-10-29 13:30:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 67.5 |
| abb750fd-e83b-33f6-b832-ba0c9401c0b2 | -13.9337 | -48.4305 | 2025-10-29 13:30:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 3f39164e-376e-31ee-8908-0c7271126e5a | -12.3867 | -50.1731 | 2025-10-29 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 119.6 |
| 866e5c94-3193-3d21-a1cb-3bbe67bf0e4c | -6.165 | -41.5979 | 2025-10-29 13:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 89.6 |
| bb71269b-9244-3231-b6a4-635f67c3162c | -12.387 | -50.1515 | 2025-10-29 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 774a75a8-88cb-3296-add4-dd53738c5361 | -15.4581 | -43.6408 | 2025-10-29 13:30:00 | GOES-19 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 109.0 |
| 163f7178-bde5-362b-a269-63195626fbea | -15.0706 | -48.7638 | 2025-10-29 13:30:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 157.4 |
| d0a5d94e-93e0-3755-af08-9fd91e93e34b | -15.0711 | -48.7415 | 2025-10-29 13:30:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 128.6 |
| dde357c1-7949-3642-bb13-9a894bd135ec | -13.0639 | -47.535 | 2025-10-29 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 84f1ef2c-a2a0-3267-8d05-2f6fd9ffd998 | -12.3679 | -50.1539 | 2025-10-29 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 166.0 |
| 92b1164b-d0a1-3d26-81f4-10977a286f3a | -13.5682 | -47.3468 | 2025-10-29 13:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 7a1d98f1-bae4-3883-947e-ff00b32ddf39 | -12.3676 | -50.1755 | 2025-10-29 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 118.6 |
| a1d05576-1a74-340e-98c5-959f67498673 | -3.7261 | -41.579 | 2025-10-29 13:30:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 134.6 |
| 9626a736-8739-3811-abce-70c678a069e1 | -13.411 | -42.7185 | 2025-10-29 13:30:00 | GOES-19 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 108.1 |
| eabc8abb-178d-3aa5-acdb-322841c2851d | -3.7074 | -41.58 | 2025-10-29 13:40:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 147.8 |
| 44520593-af2d-3223-a511-1ab26054b0ba | -12.3676 | -50.1755 | 2025-10-29 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 129.9 |
| 8b2fabaf-c24e-3a16-84ce-3a216020422a | -3.6731 | -44.2053 | 2025-10-29 13:40:00 | GOES-19 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 005b43d1-81f3-3bdd-a139-1350450de3b6 | -14.2685 | -48.1118 | 2025-10-29 13:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 18a00695-4a92-3c38-b770-e74b302032be | -6.1249 | -41.8414 | 2025-10-29 13:40:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 69.9 |
| e99174ad-b12f-3ab1-ae57-423ff70db2ac | -15.4581 | -43.6408 | 2025-10-29 13:40:00 | GOES-19 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 103.1 |
| 71b2d9d3-4b54-3b55-b8a2-09f89c994ac3 | -14.3199 | -46.5226 | 2025-10-29 13:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 43c18df7-0131-3505-8f3c-4c94125b8488 | -3.7075 | -41.556 | 2025-10-29 13:40:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 119.4 |
| fd049d41-0beb-309c-a041-dc446ed7a685 | -13.411 | -42.7185 | 2025-10-29 13:40:00 | GOES-19 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 118.1 |
| 0e504b82-19d7-3d40-874d-4925280d99d1 | -3.8997 | -40.797 | 2025-10-29 13:40:00 | GOES-19 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 190.8 |
| c59f3bee-8974-3bf8-88a7-ac665419d8ea | -7.3418 | -42.4894 | 2025-10-29 13:40:00 | GOES-19 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 183.2 |
| 840008b4-84ae-32d5-9ff8-c71df3b42d01 | -13.0446 | -47.5379 | 2025-10-29 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 842b39a1-a3b0-3cb1-94e6-ee0bb0b71caf | -12.3867 | -50.1731 | 2025-10-29 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 134.2 |
| f5f8b80a-13f4-3fc2-bcc0-2a680586a277 | -4.9983 | -44.1541 | 2025-10-29 13:40:00 | GOES-19 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| cdcd7028-6d82-3a6c-99d0-13509af1c9bc | -12.3679 | -50.1539 | 2025-10-29 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 228.6 |
| 192de641-37f8-3684-924a-65dcc10e6815 | -7.3421 | -42.4656 | 2025-10-29 13:40:00 | GOES-19 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 193.3 |
| 7aad3cd2-6bc4-366c-a06a-1bb7ba29c366 | -13.5682 | -47.3468 | 2025-10-29 13:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 81.5 |
| c6fbbf95-8618-3218-9847-e9a83a7f4a11 | -15.0711 | -48.7415 | 2025-10-29 13:40:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 5a22e4ba-27c6-3776-aabd-2a3310dcd350 | -12.387 | -50.1515 | 2025-10-29 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 150.5 |
| ffc4e9a6-f670-348b-be2a-42a6346a1e75 | -3.7404 | -42.2927 | 2025-10-29 13:40:00 | GOES-19 | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 96.9 |
| 26d32e66-eefe-3709-8897-b5967e127298 | -12.3488 | -50.1563 | 2025-10-29 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 0db14108-af99-32c4-89ff-8cc39347a6aa | -15.0706 | -48.7638 | 2025-10-29 13:40:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 870038b0-772f-3b97-a893-c876f5ea8db8 | -3.7261 | -41.579 | 2025-10-29 13:40:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 178.6 |
| 1b948041-2195-34cf-b362-a94dc9853b8f | -4.5157 | -38.7741 | 2025-10-29 13:40:00 | GOES-19 | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 234.4 |
| 3b3b4209-5cba-3508-b5de-567aca221f64 | -14.8981 | -46.7659 | 2025-10-29 13:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 6bfc941f-a9a0-3a42-9caa-7d6f0d15a757 | -3.7262 | -41.555 | 2025-10-29 13:40:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 131.4 |
| 1e8907b1-2f26-3f58-906d-070d98f6fed0 | -13.0442 | -47.5603 | 2025-10-29 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| ae9bfe81-b8f4-340d-a8cb-141aee32c871 | -12.3676 | -50.1755 | 2025-10-29 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 128.2 |
| 8d97cc49-2f20-39fc-85b8-065461d8ea6b | -15.1338 | -48.5309 | 2025-10-29 13:50:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 489f5b0d-3949-317c-9a48-2836aa287dc0 | -3.8997 | -40.797 | 2025-10-29 13:50:00 | GOES-19 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 186.5 |
| b10a8603-953a-39c9-ab4c-b642c0ee48ee | -14.23 | -43.4776 | 2025-10-29 13:50:00 | GOES-19 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 270.9 |
| 48f4554d-d2e2-31eb-875b-0090e64e208f | -7.5928 | -43.5699 | 2025-10-29 13:50:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 6def2b0b-efe1-383c-939d-3217cdc20509 | -7.3421 | -42.4656 | 2025-10-29 13:50:00 | GOES-19 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 203.2 |
| 1d4ccb53-d064-362e-9857-fa1e1bd22a68 | -13.411 | -42.7185 | 2025-10-29 13:50:00 | GOES-19 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 123.2 |
| 7224bfc8-3c0a-3319-875a-1c22a6e4ae91 | -7.0695 | -44.9335 | 2025-10-29 13:50:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 124.0 |
| f646c7e7-db9d-3834-b5c8-246f4c68d2ae | -7.6114 | -43.5914 | 2025-10-29 13:50:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 0c9a6ed5-dcab-3c6e-a1fc-71463851ab23 | -15.0706 | -48.7638 | 2025-10-29 13:50:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 108.2 |
| b4781881-4ad8-3254-b460-3eb01b8c33e0 | -3.7075 | -41.556 | 2025-10-29 13:50:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 98.8 |
| 4cbf48da-fbf6-3c0b-989b-2ff3df977e05 | -13.5686 | -47.3242 | 2025-10-29 13:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 67.8 |
| cd03601c-b029-30ba-b6f1-7ab4d46d1417 | -13.7343 | -48.7701 | 2025-10-29 13:50:00 | GOES-19 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 78.4 |
| e4c06dbd-00a0-3ee1-889d-ac0c67758a5a | -14.6119 | -48.3921 | 2025-10-29 13:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 82.8 |
| e8f41b6d-b459-3fb5-bde3-2e1123d27648 | -12.3679 | -50.1539 | 2025-10-29 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 252.9 |
| 58decd41-95f8-3587-b184-08e3a69321ac | -12.7021 | -46.303 | 2025-10-29 13:50:00 | GOES-19 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 130.4 |
| c00a419d-2354-32be-9d12-2dfdacbe9157 | -3.7262 | -41.555 | 2025-10-29 13:50:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 116.6 |
| 14a7b951-7024-3ad7-b0f1-ef2fd49b4401 | -13.0446 | -47.5379 | 2025-10-29 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 96.4 |
| e882bce0-db98-3ed6-9e9b-d866b3324645 | -12.387 | -50.1515 | 2025-10-29 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 136.3 |
| 35c799e8-1c46-3694-9529-c31a47ff5f7c | -12.3488 | -50.1563 | 2025-10-29 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 6051755a-351b-32c8-a08f-2b3855003515 | -3.7261 | -41.579 | 2025-10-29 13:50:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 156.3 |
| c95ecae9-0cea-338e-80c2-7cda2b58e4d3 | -3.6545 | -44.2062 | 2025-10-29 13:50:00 | GOES-19 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 149.5 |
| a8ca579b-8e91-3ebc-bee4-6a8849c76e2d | -7.3232 | -42.4675 | 2025-10-29 13:50:00 | GOES-19 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 139.5 |
| a1a7322f-9c74-34ec-85b6-abc9c3595962 | -6.8808 | -45.041 | 2025-10-29 13:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 200.8 |
| dd37793e-3a8d-3121-b394-08dcf2cd3214 | -7.0883 | -44.9319 | 2025-10-29 13:50:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 423c5cae-c749-3d6a-b7f6-964346ad9d1b | -6.6781 | -44.6935 | 2025-10-29 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 9c3b8745-9f91-3c62-b108-cac58c4e723d | -7.2565 | -45.0079 | 2025-10-29 13:50:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 0041db78-62e9-3a7b-aa64-2bc652c45c9e | -3.6731 | -44.2053 | 2025-10-29 13:50:00 | GOES-19 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 123.9 |
| 5309c37b-0962-37b8-945a-60f503cf145d | -13.5682 | -47.3468 | 2025-10-29 13:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 110.8 |
| b7ea985e-d95b-3775-ad9f-9e7171cb0707 | -4.2568 | -40.678 | 2025-10-29 13:50:00 | GOES-19 | PIRES FERREIRA | CEARÁ | Brasil | 2310951 | 23 | 33 | nan | nan | nan | Caatinga | 110.1 |
| 01dfc899-6af2-37b9-998c-b9a9edf9cdfb | -13.7348 | -48.748 | 2025-10-29 13:50:00 | GOES-19 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 74fcbdbd-ad57-30dd-9f39-1df77fbf48a8 | -7.0693 | -44.9563 | 2025-10-29 13:50:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |
| a968fb82-010d-343c-bce9-e30a4945e578 | -13.0442 | -47.5603 | 2025-10-29 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 84fb378a-44e4-33c1-998d-57504e471e08 | -12.7214 | -46.3001 | 2025-10-29 13:50:00 | GOES-19 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 55abaaf2-c988-3174-b081-9f14b6a6637c | -15.0711 | -48.7415 | 2025-10-29 13:50:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 37a3fe4b-3c3f-3ef7-a6a6-13e763dde8ea | -7.3418 | -42.4894 | 2025-10-29 13:50:00 | GOES-19 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 212.9 |
| 371ecfd2-63fb-3faf-bc3b-10dacaa7496b | -14.4754 | -45.5984 | 2025-10-29 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 363.8 |
| 45482fe7-05bc-3c59-bdd1-104ef8e61d2f | -4.2567 | -40.7024 | 2025-10-29 13:50:00 | GOES-19 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 104.5 |
| 8a6b2c78-9372-37c1-9297-bf65c1a2ba82 | -3.6732 | -44.1824 | 2025-10-29 13:50:00 | GOES-19 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 499811f6-055b-3570-b949-dabff3c06509 | -7.6116 | -43.568 | 2025-10-29 13:50:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 51defd47-d20f-36b6-9607-a3d6872f4610 | -6.165 | -41.5979 | 2025-10-29 13:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 79.2 |
| 6799b5c4-5d83-31b4-8928-9ce75461596e | -13.7343 | -48.7701 | 2025-10-29 14:00:00 | GOES-19 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 689ffc8f-fe8a-3f55-900e-641c1d8a7a0e | -13.5682 | -47.3468 | 2025-10-29 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 3d8db931-96a5-389a-a85f-67f92378f5f7 | -6.967 | -39.1051 | 2025-10-29 14:00:00 | GOES-19 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 93.4 |
| d735d9b2-e5a2-3a9e-a4c3-4ea6668de90c | -7.3421 | -42.4656 | 2025-10-29 14:00:00 | GOES-19 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 210.7 |
| b45651ae-07d7-35a1-a1e4-5f4cead6fc6b | -6.165 | -41.5979 | 2025-10-29 14:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 109.5 |
| 5c2f1a9b-6693-3462-b499-56e4cfe31c5e | -13.0442 | -47.5603 | 2025-10-29 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 82.5 |
| a292d80f-a8fd-38b1-84cd-dead9edb7be6 | -6.1464 | -41.5755 | 2025-10-29 14:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 81.8 |
| eb62b0e2-271e-3296-b536-228a698291c4 | -6.1249 | -41.8414 | 2025-10-29 14:00:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 69.6 |
| 8febcfc2-2f3f-3b21-ad36-daf38575e653 | -3.8997 | -40.797 | 2025-10-29 14:00:00 | GOES-19 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 158.4 |
| 9f69a18d-5208-31d0-84e2-8650d4050325 | -7.6116 | -43.568 | 2025-10-29 14:00:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 127.7 |
| ba1a7874-1776-3d15-81b2-e90eccda280b | -7.3232 | -42.4675 | 2025-10-29 14:00:00 | GOES-19 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 127.3 |
| f4faa1e7-5558-3710-89ff-b7a4264f6eb4 | -12.7021 | -46.303 | 2025-10-29 14:00:00 | GOES-19 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 160.1 |
| f38b153a-1d02-3c23-9437-36835c7d0b7c | -12.3488 | -50.1563 | 2025-10-29 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 03f5875c-4d8c-37e5-95d7-c98d84c9696d | -3.7261 | -41.579 | 2025-10-29 14:00:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 179.5 |
| 1b3985a0-ebd6-3fe6-91b4-ad4725490f38 | -15.0711 | -48.7415 | 2025-10-29 14:00:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 5a79ae74-658e-3f18-a8c1-05cc56208ecd | -7.0693 | -44.9563 | 2025-10-29 14:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| a393d20a-1f81-3864-8811-3a2a2c69bc85 | -5.639 | -41.5464 | 2025-10-29 14:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 97.8 |


[Clique aqui para ver as próximas entradas](README87.md)
