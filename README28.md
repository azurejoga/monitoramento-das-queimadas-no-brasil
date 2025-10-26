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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bc84a440-7894-335b-b0e0-4285227886b4 | -17.53268 | -51.04867 | 2025-10-26 04:04:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| df3fc38e-239d-3b8b-8947-db0762581f5a | -18.15431 | -44.25947 | 2025-10-26 04:04:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8e8c3ca3-6094-33aa-9bb4-96a2c67ae200 | -18.6505 | -52.08627 | 2025-10-26 04:04:00 | NOAA-20 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 04f94f5d-cd0c-3765-8957-95f03124b9c5 | -15.94031 | -51.05896 | 2025-10-26 04:04:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cfb80043-71da-325b-8de1-ce8459b65149 | -20.51051 | -41.99234 | 2025-10-26 04:04:00 | NOAA-20 | CAPARAÓ | MINAS GERAIS | Brasil | 3112109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| de148454-868b-3640-a862-c0b69a8919db | -17.33148 | -43.64662 | 2025-10-26 04:04:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a878efea-d4fc-387a-b639-2afaf4805b1f | -20.50994 | -41.99609 | 2025-10-26 04:04:00 | NOAA-20 | CAPARAÓ | MINAS GERAIS | Brasil | 3112109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d63a83b2-2156-320e-beba-99d72110bfbe | -17.32753 | -43.64969 | 2025-10-26 04:04:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5ac38b05-6a94-37a4-b53b-5ecf9086fbdc | -15.93383 | -51.06451 | 2025-10-26 04:04:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b49b215-1423-3c8b-8dd8-9b8e97e98180 | -19.63948 | -42.42739 | 2025-10-26 04:04:00 | NOAA-20 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c677300e-6a0a-386c-b76f-e5a52becef9d | -20.97914 | -44.31646 | 2025-10-26 04:04:00 | NOAA-20 | RITÁPOLIS | MINAS GERAIS | Brasil | 3156106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b4960774-7484-37f7-95e9-e0fd9463dbf1 | -20.45218 | -44.41983 | 2025-10-26 04:04:00 | NOAA-20 | PIRACEMA | MINAS GERAIS | Brasil | 3150604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 21710fb2-f328-3547-9743-37edc0b01071 | -18.47612 | -44.43423 | 2025-10-26 04:04:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ab21f1d4-2336-3521-bdc1-9fdf44f47e7c | -23.0193 | -46.23271 | 2025-10-26 04:04:00 | NOAA-20 | PIRACAIA | SÃO PAULO | Brasil | 3538600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 27a0f377-2eb1-3bce-9c8d-26da4c834df6 | -21.92622 | -46.51214 | 2025-10-26 04:04:00 | NOAA-20 | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| b5dd54f7-7a1d-3fc2-abf1-2d43e23ea008 | -18.4662 | -47.16958 | 2025-10-26 04:04:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 61b27356-ec66-3ab6-a5c6-ea33f495ef14 | -18.6557 | -52.08745 | 2025-10-26 04:04:00 | NOAA-20 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f6ffb5df-539c-3354-a0e8-cffc5df6f839 | -20.31823 | -46.54297 | 2025-10-26 04:04:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc8dd2d9-bafb-31e7-9c5a-c114b44f331c | -17.52755 | -46.58492 | 2025-10-26 04:04:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5f8eda87-0b90-37aa-8129-88dc035e4646 | -23.26695 | -46.39259 | 2025-10-26 04:04:00 | NOAA-20 | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 970496e1-4ae0-3704-af54-0c28311c1bc9 | -18.48292 | -44.43544 | 2025-10-26 04:04:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 766f629f-fc45-312b-b2d6-b372b92e1163 | -16.31417 | -50.04805 | 2025-10-26 04:04:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a9844a14-204a-3a96-9308-25ac242816cf | -21.43362 | -49.59635 | 2025-10-26 04:04:00 | NOAA-20 | SABINO | SÃO PAULO | Brasil | 3544608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 28502fe6-2b35-3869-b364-49d6c21b0c81 | -22.37692 | -43.59511 | 2025-10-26 04:04:00 | NOAA-20 | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| d7aedb99-4b6f-38f4-9327-b01ca559ac21 | -18.46708 | -47.16469 | 2025-10-26 04:04:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c6f0a596-25ca-3def-bfa2-0b5e38eb66e2 | -18.46234 | -47.1689 | 2025-10-26 04:04:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fe9b060f-2cdd-376f-a79c-cacfba4fedb4 | -17.31289 | -43.65477 | 2025-10-26 04:04:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3e51fca8-ff69-3b44-81e7-b44b02cf26fc | -21.42942 | -49.5953 | 2025-10-26 04:04:00 | NOAA-20 | SABINO | SÃO PAULO | Brasil | 3544608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 57b8ea5b-6db9-32c5-a007-f269d34ef766 | -19.34894 | -45.60048 | 2025-10-26 04:04:00 | NOAA-20 | QUARTEL GERAL | MINAS GERAIS | Brasil | 3153707 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7c7ab4d4-fd0c-3c54-92d2-5d4eaaff30ea | -18.64978 | -52.08968 | 2025-10-26 04:04:00 | NOAA-20 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a8cdc02-8b9c-3f41-848e-fbc03c67a611 | -19.8216 | -46.62846 | 2025-10-26 04:04:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 63e8338a-15f0-3618-8a6c-f73b803d13d7 | -17.32235 | -43.66019 | 2025-10-26 04:04:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 12.2 |
| f2546c3c-0586-37b9-9f9b-99cedbb2324d | -17.32417 | -43.60696 | 2025-10-26 04:04:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ecdb6664-c5b8-33f7-9d6a-ed64a8429626 | -19.40295 | -45.87398 | 2025-10-26 04:04:00 | NOAA-20 | SERRA DA SAUDADE | MINAS GERAIS | Brasil | 3166600 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a29e4d1c-2fca-34e3-bb07-fa7702c7e3e7 | -23.45842 | -47.01679 | 2025-10-26 04:04:00 | NOAA-20 | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 64c42192-4f4b-3f3c-a14f-9f4a31992251 | -22.41553 | -43.41465 | 2025-10-26 04:04:00 | NOAA-20 | PATY DO ALFERES | RIO DE JANEIRO | Brasil | 3303856 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 29049bc3-8161-3ced-87ed-f248510e9878 | -17.05141 | -51.53069 | 2025-10-26 04:04:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a41a93d-e503-3d9e-a060-10d7783dc568 | -21.29855 | -47.1413 | 2025-10-26 04:04:00 | NOAA-20 | CÁSSIA DOS COQUEIROS | SÃO PAULO | Brasil | 3510906 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| c1c8a72d-dbf5-36ce-85c2-ef66382629e0 | -15.93964 | -51.06225 | 2025-10-26 04:04:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c6d2b7bb-22f5-3d11-b72e-7e8089bde816 | -17.37748 | -45.50664 | 2025-10-26 04:04:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 71b4cad6-27f3-3a5b-8179-fd51bb3a7761 | -20.98246 | -44.31712 | 2025-10-26 04:04:00 | NOAA-20 | RITÁPOLIS | MINAS GERAIS | Brasil | 3156106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0c63391b-b487-3d34-bea9-f549483e0fea | -16.77107 | -47.91565 | 2025-10-26 04:04:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 02ca4399-cc77-3287-ba77-bc194b79102c | -19.24892 | -44.37138 | 2025-10-26 04:04:00 | NOAA-20 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8ddd726c-f1f9-37a0-ab85-eed9881a971a | -17.33088 | -43.65029 | 2025-10-26 04:04:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bff248a5-eec5-387d-9129-dbdcaaeb5df2 | -17.01456 | -55.91282 | 2025-10-26 04:04:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| baaece3f-e453-33ba-b37d-c284b19e8831 | -18.19958 | -42.16968 | 2025-10-26 04:04:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 3ad15238-3e46-3279-b5b9-d3c2d502687d | -21.76384 | -50.04271 | 2025-10-26 04:04:00 | NOAA-20 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.3 |
| e89cfd44-bacb-34a0-9f9d-3c41fbc86123 | -19.74196 | -46.50678 | 2025-10-26 04:04:00 | NOAA-20 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c8dd7487-ef1e-3a9c-b0d9-3e7ec039ca3e | -17.31503 | -43.66276 | 2025-10-26 04:04:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| effa4aa7-7f78-3b36-a281-c84fb16e2a36 | -20.09613 | -44.82871 | 2025-10-26 04:04:00 | NOAA-20 | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 52613eba-9f13-32fa-a5d1-63391018d79d | -19.92562 | -44.65349 | 2025-10-26 04:04:00 | NOAA-20 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 548f4aff-5c7a-3a28-8fd5-14c9d614f307 | -17.32357 | -43.65279 | 2025-10-26 04:04:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 65.8 |
| e7cbd081-94d2-3b9f-9982-d17232991484 | -20.83862 | -45.60433 | 2025-10-26 04:04:00 | NOAA-20 | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6d93cb06-d81f-34f9-81cf-31a8aa82dbed | -18.65498 | -52.09087 | 2025-10-26 04:04:00 | NOAA-20 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ffd673cc-722a-3271-ab2b-dcde552ea1dd | -20.57875 | -43.3232 | 2025-10-26 04:04:00 | NOAA-20 | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 1a2ababc-9329-35d3-93c7-82dc2937a0dc | -22.59921 | -43.65034 | 2025-10-26 04:04:00 | NOAA-20 | PARACAMBI | RIO DE JANEIRO | Brasil | 3303609 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e814db00-b99f-3a99-aca2-8a7fefa46ade | -18.46528 | -47.17466 | 2025-10-26 04:04:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 55e7355c-5a5b-3055-8fed-a4b9c68ca3c6 | -17.3141 | -43.64736 | 2025-10-26 04:04:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c3cb58a9-6e10-302d-9756-15bd1d932de2 | -21.41479 | -44.08765 | 2025-10-26 04:04:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0cbab6a0-5de6-3209-a79a-2b3cd7b8df25 | -21.43025 | -49.59113 | 2025-10-26 04:04:00 | NOAA-20 | SABINO | SÃO PAULO | Brasil | 3544608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 21928c15-5375-3716-a510-245ec8ae4f03 | -21.92238 | -46.53384 | 2025-10-26 04:04:00 | NOAA-20 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c4041ae8-d22d-3bcf-894d-c37231f88f66 | -21.2977 | -47.14605 | 2025-10-26 04:04:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 9ff84cab-e415-3418-a939-da989bf3922b | -19.85994 | -42.18918 | 2025-10-26 04:04:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f6f54479-9ea5-3fcb-aaca-3dcd6e878244 | -16.60587 | -50.83811 | 2025-10-26 04:04:00 | NOAA-20 | IVOLÂNDIA | GOIÁS | Brasil | 5211602 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c6f395a1-781a-3f93-b231-5e5250f9258e | -17.33028 | -43.65396 | 2025-10-26 04:04:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3ac86338-b825-3c35-aa28-07425afbdbd0 | -19.71281 | -47.58256 | 2025-10-26 04:04:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2fc960ce-7bb6-3904-8d5a-7a6017ac4ef0 | -17.43208 | -46.88188 | 2025-10-26 04:04:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fbd86aa0-f5e8-350a-89c4-daf4988bc08a | -20.57933 | -43.31952 | 2025-10-26 04:04:00 | NOAA-20 | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ef3c5e87-45ea-3186-9c00-3c425752c5d0 | -20.24795 | -44.10804 | 2025-10-26 04:04:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| c18be780-e58a-3472-9aeb-1764f269ec8e | -17.56585 | -46.41544 | 2025-10-26 04:04:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f2b6e589-5f3f-3a0c-a3b5-7f5c7f9e69d4 | -17.05285 | -51.52364 | 2025-10-26 04:04:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cf53f52f-c9fc-3a0b-8184-6a25b80da651 | -21.76294 | -50.04717 | 2025-10-26 04:04:00 | NOAA-20 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.3 |
| a8761436-1bce-3e9e-95ca-1cba9a995a13 | -17.31625 | -43.65534 | 2025-10-26 04:04:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 85c0d51c-0572-3724-9266-78f91228cb5a | -19.88866 | -44.36924 | 2025-10-26 04:04:00 | NOAA-20 | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 51a32319-1b32-3fdc-bda8-545dd8f39652 | -19.95215 | -43.83737 | 2025-10-26 04:04:00 | NOAA-20 | RAPOSOS | MINAS GERAIS | Brasil | 3153905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5a952a0f-a7c3-326c-8015-e61a76b60940 | -18.65642 | -52.08405 | 2025-10-26 04:04:00 | NOAA-20 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7238705b-8fcb-3a3f-8fc1-fcb18386b687 | -20.77428 | -44.87155 | 2025-10-26 04:04:00 | NOAA-20 | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 999ef07a-99f0-3ec0-9d57-052500cd8de6 | -20.44991 | -44.18276 | 2025-10-26 04:04:00 | NOAA-20 | PIEDADE DOS GERAIS | MINAS GERAIS | Brasil | 3150406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e682fa97-e192-3a87-a4e5-bb7cba3bdba7 | -17.32082 | -43.64851 | 2025-10-26 04:04:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 8bdf4e26-58fa-33c7-bf05-10d6d7efdcf5 | -20.33846 | -46.42816 | 2025-10-26 04:04:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7d7f9b80-1156-3bff-a402-7454017011b1 | -21.9216 | -46.53822 | 2025-10-26 04:04:00 | NOAA-20 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| cdde3fe8-8d5f-39d4-8504-3c44eebda217 | -17.32813 | -43.64601 | 2025-10-26 04:04:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e1fa1489-afd5-3020-9336-dbf4d9c83782 | -20.24857 | -44.10427 | 2025-10-26 04:04:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 3f80ce7b-d6ce-3267-a353-8a2a4846d2e6 | -17.37954 | -45.51591 | 2025-10-26 04:04:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7e3f9035-6355-3839-a411-cc23f2d242e9 | -22.15747 | -43.19749 | 2025-10-26 04:04:00 | NOAA-20 | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a0c342a6-1572-35cc-93b8-360a83825519 | -23.23038 | -50.79007 | 2025-10-26 04:04:00 | NOAA-20 | URAÍ | PARANÁ | Brasil | 4128401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c2820f82-f5e1-3751-9ffc-b6230ff3342c | -17.4166 | -46.72541 | 2025-10-26 04:04:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cb8fb6c1-c315-37e6-83b9-9e614d23fd0f | -20.31901 | -46.53856 | 2025-10-26 04:04:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f2fd9748-eead-3562-9f0d-fc1085b7c83b | -22.91654 | -43.68346 | 2025-10-26 04:04:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| fedc70e5-8041-3a4a-b293-d8746bd1314f | -20.09652 | -44.82792 | 2025-10-26 04:04:00 | NOAA-20 | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 139cba98-58bc-3872-92aa-659380c018de | -18.47952 | -44.43484 | 2025-10-26 04:04:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0ad06f9f-c262-3703-ad53-462ff206393d | -18.66017 | -52.09212 | 2025-10-26 04:04:00 | NOAA-20 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f170b06f-d70e-34f0-8446-b5781bdc3a9b | -18.15495 | -44.25563 | 2025-10-26 04:04:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4480d739-a46f-3573-be3f-3589b329cd93 | -17.33242 | -43.66195 | 2025-10-26 04:04:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fd51ef9e-6162-368f-8f26-0f2853c14f3d | -20.98184 | -44.3209 | 2025-10-26 04:04:00 | NOAA-20 | RITÁPOLIS | MINAS GERAIS | Brasil | 3156106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 843a7250-7af9-3887-af2f-e9e89343a2fc | -17.32142 | -43.64481 | 2025-10-26 04:04:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 01ad6998-5534-34e0-bc6d-bae178ac6f0a | -19.8853 | -44.36864 | 2025-10-26 04:04:00 | NOAA-20 | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a9a1d87e-575d-3390-8c9d-7503f344bdbd | -21.76583 | -50.04996 | 2025-10-26 04:04:00 | NOAA-20 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.7 |
| a07b5ccb-da78-392e-9681-fe7724d6bcdf | -17.32571 | -43.66077 | 2025-10-26 04:04:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 447909ab-53ea-3256-b52f-d1de2086f953 | -15.93897 | -51.06559 | 2025-10-26 04:04:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README29.md)
