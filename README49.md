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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 663b206f-ef5d-3911-9a9f-cc88ecde85b5 | -5.203 | -37.63021 | 2025-10-07 04:34:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.9 |
| a1e45dfa-5e04-388c-872d-c1dd02da1795 | -3.20095 | -51.01513 | 2025-10-07 04:34:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d8e6515e-e4e3-34cd-a13f-aeaa99ac6666 | -3.11529 | -40.99274 | 2025-10-07 04:34:00 | NPP-375D | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6d68e4f5-f474-371b-afae-afe46c07d246 | -3.08947 | -51.24672 | 2025-10-07 04:34:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b4421bc1-ac6c-3891-b894-1e36cfec7c05 | -1.70503 | -55.68387 | 2025-10-07 04:34:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 52607860-b607-3de1-9fc6-d09f3aab19b4 | -4.44236 | -43.23454 | 2025-10-07 04:34:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 53b080ec-2b6d-304c-9a8b-72b8a9141217 | -4.44384 | -43.22501 | 2025-10-07 04:34:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 465ff29f-2d88-3beb-bbc6-3d552fc94c9c | 0.74556 | -51.58108 | 2025-10-07 04:34:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 34dd00bf-be54-3491-93c9-1d230c6b8718 | -2.24588 | -47.86933 | 2025-10-07 04:34:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bba297e4-c35d-322b-bc6d-136d7ef4601d | -4.44769 | -43.22561 | 2025-10-07 04:34:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 0f34b1f4-a75c-3492-93cc-d832a68ed13d | -3.08626 | -50.58276 | 2025-10-07 04:34:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5120442b-5c54-3eec-8404-5829553bbae9 | -3.10125 | -47.02299 | 2025-10-07 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c308b8a3-881e-39f0-987f-031685d74255 | -1.7109 | -55.68447 | 2025-10-07 04:34:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 120b4306-f208-337b-b2b7-c61979f45ee3 | -2.24923 | -47.86986 | 2025-10-07 04:34:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a12b9f4c-d765-3df6-a547-2d6a1d177214 | -3.0885 | -47.01746 | 2025-10-07 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cddf61e8-b803-3ec7-87a4-674bb2b2893e | -4.44838 | -43.22835 | 2025-10-07 04:34:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 20eb4389-fc1a-380d-a007-3f7cf9eeaab6 | -2.43901 | -48.43094 | 2025-10-07 04:34:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96259412-2ec4-366f-97f9-365de6a1a0fe | -1.56904 | -55.43687 | 2025-10-07 04:34:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 29bd6dbd-bbef-385c-a1f6-36652c328656 | -3.8778 | -38.43146 | 2025-10-07 04:34:00 | NPP-375D | EUSÉBIO | CEARÁ | Brasil | 2304285 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 72f645bf-e5eb-349f-a9a6-712f0f86ded6 | -2.27181 | -47.19688 | 2025-10-07 04:34:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4079f722-e194-3233-85f8-544047834e2e | -3.37211 | -52.17902 | 2025-10-07 04:34:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| eee644a3-19b9-3d0a-bcd8-2b0a631b2760 | -3.46943 | -51.63938 | 2025-10-07 04:34:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb454650-6882-3beb-b6f3-4fe545b24277 | -3.0946 | -47.02195 | 2025-10-07 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 2cf9cec1-0a8f-3e34-a709-1d2d4bfe0c61 | -2.13372 | -48.0036 | 2025-10-07 04:34:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8bce4a25-cb92-3754-aa5c-42831640571f | -4.06949 | -44.51096 | 2025-10-07 04:34:00 | NPP-375D | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| c03d86e4-df85-329e-8058-7f00605b5da8 | 0.74969 | -51.58043 | 2025-10-07 04:34:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9b973121-905f-31e5-8249-d7880d353747 | -1.09714 | -53.68616 | 2025-10-07 04:34:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a4e9db47-8361-3098-9779-2949ce462082 | -4.05876 | -44.50931 | 2025-10-07 04:34:00 | NPP-375D | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ef3e6132-a363-3542-b9a1-e2dc5249c106 | -3.14009 | -44.42371 | 2025-10-07 04:34:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 119b3cd3-6ce2-3321-886b-6ff56eea8166 | -4.25742 | -44.25658 | 2025-10-07 04:34:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 75461da4-74a6-3d77-a6bf-83c7195b6a0e | -1.08551 | -53.69925 | 2025-10-07 04:34:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3696a9f9-8116-3016-aa4d-f469cc8b6ee7 | -4.45303 | -43.21664 | 2025-10-07 04:34:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5c52777b-721d-3712-b236-69e223e472f6 | -2.89169 | -50.72915 | 2025-10-07 04:34:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 94086cde-1185-3df3-b808-6765210e44ed | -3.14365 | -44.42427 | 2025-10-07 04:34:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d9198cbc-ba89-35c5-b2af-74c5f446d750 | -1.09246 | -53.68575 | 2025-10-07 04:34:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 58215b8e-3c4e-34d3-84bb-a96c8c7d7e36 | -4.84136 | -42.92247 | 2025-10-07 04:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 2da17f46-63de-34fd-b6a2-7977c6b15c1b | -2.145 | -47.50693 | 2025-10-07 04:34:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52b78a42-0182-368c-bf6c-502814c41865 | -4.83741 | -42.92184 | 2025-10-07 04:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| eec30b20-51d0-3e8b-b6d6-b393be51a5b0 | -5.5529 | -37.32195 | 2025-10-07 04:34:00 | NPP-375D | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 429fb045-c7de-35f2-8773-a6ffed8f67b0 | -2.24309 | -47.8653 | 2025-10-07 04:34:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 336a2e2a-dc78-37d7-a939-72d640b2f145 | -4.44453 | -43.22775 | 2025-10-07 04:34:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 27.0 |
| af31e898-afd9-3e9a-9663-ea6b01810734 | -1.09015 | -53.69995 | 2025-10-07 04:34:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c881f2ab-72ce-314e-92ec-3ef4e44ad2c1 | -3.09902 | -47.01556 | 2025-10-07 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 743929f2-6e3f-3548-8da0-9c59cefed455 | -2.89098 | -50.73354 | 2025-10-07 04:34:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a264f8cd-7cf9-3e2f-a624-6f03513bb9ad | -1.70562 | -55.68374 | 2025-10-07 04:34:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 89a5378a-e561-3e86-9dcb-a40e21516d0c | -4.45081 | -43.23096 | 2025-10-07 04:34:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 9ab24e7c-aa90-35bc-964c-502061aa663e | -4.44843 | -43.22083 | 2025-10-07 04:34:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3a87a73c-ab87-3181-9dd5-0b3bd713e708 | -2.93711 | -54.17966 | 2025-10-07 04:34:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b639358d-cbdd-3bf2-afe3-f515509c6071 | -2.26849 | -47.19637 | 2025-10-07 04:34:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e86d5d12-9561-3b2a-955d-ad034b69b0f3 | -5.55348 | -37.31781 | 2025-10-07 04:34:00 | NPP-375D | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 14e3bc70-ce17-3dc7-87f5-0dc039c4a54e | -4.44523 | -43.22298 | 2025-10-07 04:34:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 27.0 |
| b42f0de7-54d5-3b3a-8767-6eb3e205ded1 | -3.57003 | -43.51477 | 2025-10-07 04:34:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cf463191-6fa3-344d-bcc7-1443b00e4418 | -4.44695 | -43.23037 | 2025-10-07 04:34:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 28.8 |
| f33fc4cc-31fe-3199-8fb7-b86e0a2c6f46 | -3.09569 | -47.01505 | 2025-10-07 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94ee0c4d-fa99-3247-a560-16347ed528e4 | -3.50721 | -50.47585 | 2025-10-07 04:34:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2c77ece7-6e4b-334e-9ace-1cd27e1dd200 | -4.8649 | -42.79139 | 2025-10-07 04:34:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 54cc7370-1013-307e-878f-c2208b183fe1 | -4.4431 | -43.22977 | 2025-10-07 04:34:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3ef4404e-341f-3bfe-907d-6ff9f5c42390 | -1.71031 | -55.68459 | 2025-10-07 04:34:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8b0e257-3850-3046-8893-945d19a8e674 | -3.09793 | -47.02247 | 2025-10-07 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| f79ba7a8-b619-3c00-b50f-58012e075388 | -1.61474 | -46.66621 | 2025-10-07 04:34:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d34ede31-8cc1-34ee-b97b-5c0bb3faf23a | -4.44458 | -43.22023 | 2025-10-07 04:34:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 61ed6f5f-4736-3ed4-a018-5bd4256b1469 | -3.3386 | -46.54477 | 2025-10-07 04:34:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c40f1f37-15cb-34eb-aa8c-1b8c2b668300 | -2.99241 | -39.89999 | 2025-10-07 04:34:00 | NPP-375D | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3d5be507-e7e3-3556-ab9a-3192be91b2c5 | 0.7544 | -51.58347 | 2025-10-07 04:34:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 29a9bf0d-6ac1-3765-a7f3-6f5f1990841c | -3.09073 | -47.02488 | 2025-10-07 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a7e2490-beb4-3013-a00b-0aa05e8d7d90 | 0.75382 | -51.57979 | 2025-10-07 04:34:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c1e79115-30fd-3c87-a340-0847e0a5f896 | -3.09956 | -47.01211 | 2025-10-07 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d4db556-a078-3e11-9e6c-67096b46b193 | -1.37036 | -49.03619 | 2025-10-07 04:34:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 157cfd6a-7cae-3949-aea8-347c670b83e3 | -3.14071 | -44.41973 | 2025-10-07 04:34:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a68a6ef2-ac02-329e-8ca7-9aad1cd650fa | -4.45366 | -43.21938 | 2025-10-07 04:34:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 461483a4-ff17-3d2a-a8ba-947ff9ac0a9d | -3.08607 | -51.25343 | 2025-10-07 04:34:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4bc10a7d-8111-338a-a007-6dad8f9d4517 | -2.5572 | -47.66069 | 2025-10-07 04:34:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 14e1b40c-a0cb-3788-bb71-d601416de41e | -1.3433 | -55.47269 | 2025-10-07 04:34:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04e25fc3-f199-33fc-81d4-f521b68f13a4 | -4.45229 | -43.22142 | 2025-10-07 04:34:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d31658d1-681c-3b59-ad68-0d106e35204c | -2.5332 | -54.73833 | 2025-10-07 04:34:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bbdf896f-5301-39f9-a361-43f92f28e73b | -4.44594 | -43.21818 | 2025-10-07 04:34:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 375d4ea7-604c-3e28-8b98-fcb9b444d5b3 | -3.63551 | -44.54747 | 2025-10-07 04:34:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 12f9b1e7-ae07-3276-8f2b-28143691d542 | -2.53807 | -54.7391 | 2025-10-07 04:34:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5465cbb6-0c44-35a0-9a95-9c2a8be05964 | -3.69709 | -49.41791 | 2025-10-07 04:34:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 11b0a2e4-bdb5-3415-af82-adf56c0f7b4b | -3.08452 | -50.57991 | 2025-10-07 04:34:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21c99f7f-f75d-376b-908c-b71f511f6d97 | -2.98574 | -52.62981 | 2025-10-07 04:34:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 263302c0-0d5c-3d56-9a89-65a44d189bca | -3.08697 | -50.57841 | 2025-10-07 04:34:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 44a05d63-019c-3e79-913b-7fd9d8ae1621 | -3.09624 | -47.01159 | 2025-10-07 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4bf1433-9fb7-3334-b2c3-1054043b8c0c | -2.26516 | -47.19585 | 2025-10-07 04:34:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| baabbf3c-2b2d-306a-bd41-4805a6a984ff | -4.06653 | -44.50636 | 2025-10-07 04:34:00 | NPP-375D | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8fefc981-b238-36c4-8e3f-d5db89f4f681 | -4.44909 | -43.22357 | 2025-10-07 04:34:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 7d97f54f-dda4-33a4-9fc3-c204e8a67cb5 | -2.93246 | -54.17887 | 2025-10-07 04:34:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f80ff9f5-1796-387e-b205-fcc8ec5f32dc | -3.08328 | -50.57788 | 2025-10-07 04:34:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 41ffe4fa-e5b1-3e1a-b1dc-454cee8ea4de | -3.09738 | -47.02592 | 2025-10-07 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 210a0477-c4c7-3c95-a40f-644fe923fbb2 | -4.06233 | -44.50986 | 2025-10-07 04:34:00 | NPP-375D | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 170eeb61-1288-3ac0-8df0-2f571e4eadbf | -3.09847 | -47.01902 | 2025-10-07 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 15baa027-ed52-3431-9d10-b59f550eda36 | -3.09182 | -47.01798 | 2025-10-07 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 47475831-0773-3f04-94c7-be5271d47101 | -3.09128 | -47.02143 | 2025-10-07 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4ebd234f-52fd-398a-9bae-e0f4db57e91d | -2.9345 | -54.18047 | 2025-10-07 04:34:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1214956d-580d-30bc-ae7a-f42905025321 | -4.44768 | -43.23312 | 2025-10-07 04:34:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 77f94128-39f9-33a7-94b1-b158ceef93e7 | -3.1018 | -47.01954 | 2025-10-07 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef5b072b-6f94-3b72-ac8c-917226ebab2c | -1.09639 | -53.69081 | 2025-10-07 04:34:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 82e713fb-9f1e-3817-a776-f4fa27446a82 | -2.87372 | -45.43549 | 2025-10-07 04:34:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| cf06d88d-17ce-3fa4-9318-4ad734b18cae | -3.14427 | -44.42028 | 2025-10-07 04:34:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 49301384-3c9e-3ea4-a6ca-db584e97abc9 | -4.06295 | -44.50581 | 2025-10-07 04:34:00 | NPP-375D | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README50.md)
