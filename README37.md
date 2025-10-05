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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 767b249b-70d4-3a4d-9285-aa61a41ae578 | -8.5764 | -46.3041 | 2025-10-05 03:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 227.8 |
| 6e28b642-9eab-37cb-8b9c-f5e94ac00c02 | -6.1534 | -44.6903 | 2025-10-05 03:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 21e71363-1d44-3cc3-bc93-9d05f6e09306 | -6.1349 | -44.6689 | 2025-10-05 03:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 388735ff-761e-3d8a-a096-f0ddb9475b5d | -18.3338 | -45.8971 | 2025-10-05 03:50:00 | GOES-19 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 0dc355b0-01d1-3a04-82d4-9e963705ef6d | -4.6318 | -43.1816 | 2025-10-05 03:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| d9f5b130-1d65-3430-9c4c-4920830c590e | -8.5956 | -46.2798 | 2025-10-05 03:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 72b766fe-1250-3362-a9cf-bf5c89e35b2a | -4.3197 | -48.0908 | 2025-10-05 03:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 30.9 |
| aabae7c5-4fa9-33e4-912b-7625d88d2874 | -4.4445 | -43.2397 | 2025-10-05 03:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 42cc32e2-ef86-35ec-b907-d046ee9ff80f | -18.3345 | -45.8734 | 2025-10-05 03:50:00 | GOES-19 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 98.2 |
| c59807c7-7374-3415-adf4-929b90d1db42 | -5.795 | -42.9358 | 2025-10-05 03:50:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 71.1 |
| 28c219fa-fc54-3e4f-b9fc-89a42a6114a7 | -8.5761 | -46.3266 | 2025-10-05 03:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 430.8 |
| 0dce46b7-2681-37b1-94fb-5aff9b179527 | -6.1351 | -44.6461 | 2025-10-05 03:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 104.4 |
| ab4d0573-b964-3170-9fd6-dd863ee3136f | -4.6505 | -43.1805 | 2025-10-05 03:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 8d3420ac-4d05-32ac-9b07-fe6aadfae845 | -10.6568 | -46.3372 | 2025-10-05 03:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 04adee7b-b2c5-3e2c-9c10-3daed773eb43 | -5.7762 | -42.9372 | 2025-10-05 03:50:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 105.0 |
| 44cf843e-5e30-3162-8cd8-4093abde35e8 | -4.6317 | -43.205 | 2025-10-05 03:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 27454667-8275-3e70-8614-2680bcee6a2d | -6.1538 | -44.6446 | 2025-10-05 03:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 168.7 |
| 0ae63a66-7084-3e66-9efd-24750aab532e | -5.8891 | -42.9048 | 2025-10-05 03:50:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 67.6 |
| d741dd36-259c-3f4d-8530-179e68c99af2 | -6.4134 | -43.0489 | 2025-10-05 03:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 48549452-db23-3dd3-a4cf-1dce3b395a4f | -6.1536 | -44.6675 | 2025-10-05 03:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 326.9 |
| b5aa7e88-e637-3f85-bb21-f5ef793e8641 | -8.595 | -46.3246 | 2025-10-05 03:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 194.1 |
| dc2dcf23-324c-3af6-805f-8275f9523f22 | -8.5759 | -46.349 | 2025-10-05 03:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 97.0 |
| f31766c7-d23a-323d-b87e-4f3a9ba4cd4c | -10.6378 | -46.3396 | 2025-10-05 03:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 148.4 |
| 7b32ea25-825b-3ba2-ac69-30deeb326448 | -13.1161 | -43.847 | 2025-10-05 03:50:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 04f5939b-6a80-38bc-93b9-e72ebfba574e | -5.0912 | -37.60812 | 2025-10-05 03:51:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 4635f44c-d731-393a-aa76-e72c7ff396d1 | -4.4315 | -40.76558 | 2025-10-05 03:51:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a138508d-82bd-3dd4-8d36-2eb0906cb842 | -4.73352 | -43.26104 | 2025-10-05 03:51:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ab4bd918-2da6-3f26-a38a-01daf8fdcda9 | -5.06517 | -40.47384 | 2025-10-05 03:51:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 8.2 |
| aa818718-a690-34c0-94e0-6031acdcc2ba | -4.64663 | -43.1824 | 2025-10-05 03:51:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 9879eebb-7470-3e83-afb3-d66867cfe340 | -4.64539 | -43.18979 | 2025-10-05 03:51:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 682c20c2-4c65-3146-9f97-37daace4708c | -4.45072 | -43.2347 | 2025-10-05 03:51:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d88aa5b8-a109-3cd2-bb82-fc85f2cb4b12 | -5.493 | -39.50697 | 2025-10-05 03:51:00 | NOAA-20 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 340e8e3d-3be2-3728-9814-db29d1733808 | -4.43351 | -43.23576 | 2025-10-05 03:51:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| a89bf944-9d7a-3bee-9755-f1e8029efc5c | -5.26934 | -39.266 | 2025-10-05 03:51:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0211e233-c477-3837-a329-2c44a9b8f57e | -4.27058 | -46.75305 | 2025-10-05 03:51:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 1ab7ca10-6192-36e3-9c9b-1e616d5be598 | -3.08782 | -47.79417 | 2025-10-05 03:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 972bb4f9-3701-34c5-9da2-5cd0ec43750b | -4.26999 | -46.75642 | 2025-10-05 03:51:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8a8c785f-a51d-3635-9fc4-d1d874aa05fa | -4.6384 | -43.18101 | 2025-10-05 03:51:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6a3cb000-6eac-3f7e-9437-6b1ac72a15bd | -3.67311 | -41.76664 | 2025-10-05 03:51:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 4f9889d8-d21a-305b-85fb-1a4f21848d86 | -3.47672 | -39.04693 | 2025-10-05 03:51:00 | NOAA-20 | PARACURU | CEARÁ | Brasil | 2310209 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 20652f1e-ab3b-312c-b84c-f5360855ef33 | -3.09073 | -47.0248 | 2025-10-05 03:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f521ef2c-deea-3765-9d01-d4b2cf0ed014 | -4.65012 | -43.18679 | 2025-10-05 03:51:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| d74996e5-0656-3b83-8452-e65b55fa6b04 | -3.33205 | -43.1552 | 2025-10-05 03:51:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ca768368-a59c-3614-901b-a49ace5bfa95 | -5.26992 | -39.26243 | 2025-10-05 03:51:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 239e4868-e4ea-312b-816e-0d0d2d3e6541 | -5.26541 | -39.26904 | 2025-10-05 03:51:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4f92d8e5-1014-3843-a9c2-44af94e4a316 | -2.68608 | -48.40279 | 2025-10-05 03:51:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 06ec98c8-bf93-3548-95f0-a815e488ec94 | -4.22621 | -46.76515 | 2025-10-05 03:51:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 317cffc3-0c06-365c-abbc-949a9c36b926 | -2.68086 | -48.39703 | 2025-10-05 03:51:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 006d6125-9681-3b00-9934-9f3db1fd63fb | -2.29317 | -47.99289 | 2025-10-05 03:51:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0b32eb92-298a-350a-9276-97021cfad4d7 | -4.44533 | -43.24151 | 2025-10-05 03:51:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 05542c7e-3888-3398-803f-fe0c653c59b8 | -4.64189 | -43.1854 | 2025-10-05 03:51:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| cd7f8f1b-7803-31fa-af00-5d167664177b | -2.68767 | -48.39349 | 2025-10-05 03:51:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 16696b41-8389-3d3f-b3c8-280315dd0888 | -5.26611 | -37.92174 | 2025-10-05 03:51:00 | NOAA-20 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e4e24f09-f681-35ba-be72-88345ff2e3da | -3.67234 | -41.76442 | 2025-10-05 03:51:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 70082eba-6eec-35da-9cd3-510411d7f115 | -4.64126 | -43.18912 | 2025-10-05 03:51:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| e0ebbf94-88b3-3c7f-ac71-caf5231ef817 | -2.89723 | -48.07922 | 2025-10-05 03:51:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 67b93047-9979-38ab-b346-6c76323622a4 | -2.68051 | -48.39035 | 2025-10-05 03:51:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 12144cfe-5ea7-3bdc-aadc-5b7fe049ee1c | -4.88718 | -37.50156 | 2025-10-05 03:51:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1f7d73c1-8348-321f-869b-8e8b0c3a3d05 | -5.06579 | -40.46992 | 2025-10-05 03:51:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 452ad656-336d-3be9-95c3-8be8f9931108 | -5.06868 | -40.47441 | 2025-10-05 03:51:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f68cd54f-b858-3eb5-b25c-7d1a074971ee | -4.64251 | -43.1817 | 2025-10-05 03:51:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 42d7d747-9c6c-31ae-a094-9d1755f31998 | -4.8289 | -42.76689 | 2025-10-05 03:51:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c64a72a4-665d-31e8-8d80-288a388b38a3 | -5.73442 | -35.30429 | 2025-10-05 03:51:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1e8537be-a549-3479-b53b-26426be74638 | -3.35838 | -42.83125 | 2025-10-05 03:51:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 88504a99-7db3-3aa3-9f5d-e08d0ce11eb7 | -4.27116 | -46.74962 | 2025-10-05 03:51:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 92e9f204-7189-3353-9148-674b423b0655 | -4.64601 | -43.18609 | 2025-10-05 03:51:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 31063493-c2e5-3676-88fc-afa10b89ffba | -2.29839 | -47.9981 | 2025-10-05 03:51:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e6d83ee3-9bb2-3f88-9db8-4eeb20f5a9eb | -2.29248 | -47.99708 | 2025-10-05 03:51:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 222c0281-5370-3752-b492-664ac2fb05a1 | -0.91231 | -47.55449 | 2025-10-05 03:51:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4727a863-1eb9-3276-bd9f-237644807cfe | -4.22731 | -46.75862 | 2025-10-05 03:51:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 630a36fa-6794-3f8e-bd84-a3c63e152f60 | -5.26303 | -39.27251 | 2025-10-05 03:51:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| af25a4b1-af7a-3dc5-a4fb-8754aae99794 | -3.67385 | -41.76194 | 2025-10-05 03:51:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 4aab8ff8-f420-38e2-a6d3-8575f64da5f0 | -2.68581 | -48.39583 | 2025-10-05 03:51:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 664dd172-ef06-362f-8de1-6bb05e764400 | -3.84105 | -44.5546 | 2025-10-05 03:51:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b3e3ddbf-b974-383c-b388-3cc6add2d2e6 | -4.6305 | -43.18792 | 2025-10-05 03:51:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a2a85346-eb97-36a8-ae18-4bc057d06943 | -0.90642 | -47.55365 | 2025-10-05 03:51:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| dc346220-ff84-366e-819a-01c672b141da | -3.64654 | -48.32309 | 2025-10-05 03:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e353f66d-60f0-3c8d-8f78-dc523bbd9cfd | -3.08203 | -47.7933 | 2025-10-05 03:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5aa3fe18-e628-37c3-85b2-92f3314ec9b6 | -5.26416 | -39.26537 | 2025-10-05 03:51:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 04f5713a-8113-37c1-8a81-74207f064711 | -3.67615 | -41.76508 | 2025-10-05 03:51:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| c734d502-6a5d-37a1-a136-f890cb8c6ee8 | -3.33272 | -43.1544 | 2025-10-05 03:51:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f94f9115-657e-3144-b418-0fac34e33180 | -4.44119 | -43.24083 | 2025-10-05 03:51:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 9a6e53be-1d27-3b7d-b4d5-05336063e8f6 | -4.63714 | -43.18844 | 2025-10-05 03:51:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| a1071fbc-e7b1-3c69-a252-74281362242f | -4.44181 | -43.23708 | 2025-10-05 03:51:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 6b111835-cf35-32c3-8e30-35d61a50d6e7 | -2.67901 | -48.39948 | 2025-10-05 03:51:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2c1f27d0-abbb-3d0d-8ee1-d35ba7ed3a32 | -5.26023 | -39.26841 | 2025-10-05 03:51:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c94587ab-dcaf-334f-86d7-d49f6207646f | -4.82546 | -42.76287 | 2025-10-05 03:51:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b73970b9-1684-318c-bd77-9d3670d45c43 | -3.84823 | -41.56726 | 2025-10-05 03:51:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 69824afb-cf04-3308-9004-e1feefa8e944 | -4.88772 | -37.4981 | 2025-10-05 03:51:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 134ad4ad-dd78-3058-bbf5-a7938825d18b | -4.42497 | -40.76051 | 2025-10-05 03:51:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 935dcdb9-ee82-361c-accc-eca4f4a58bc6 | -3.84749 | -41.57183 | 2025-10-05 03:51:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 68367924-b4d4-33a7-9add-fab2f3c3b78a | -3.84898 | -41.56268 | 2025-10-05 03:51:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| c68e0782-ea98-32f2-93a4-299d1a25058a | -2.91111 | -40.46484 | 2025-10-05 03:51:00 | NOAA-20 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| ed54709e-4766-3959-9ba9-329c22ff6117 | -3.73557 | -40.83207 | 2025-10-05 03:51:00 | NOAA-20 | FRECHEIRINHA | CEARÁ | Brasil | 2304509 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| eab6fb86-8b70-3f29-a9d0-7b73ff33ae46 | -4.90107 | -37.28385 | 2025-10-05 03:51:00 | NOAA-20 | TIBAU | RIO GRANDE DO NORTE | Brasil | 2411056 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f60d21f5-4808-3ddb-9a81-0c7a628b47ce | -3.84522 | -41.56207 | 2025-10-05 03:51:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e3b55f65-3626-3a94-9467-7408fc1ed7b7 | -4.42079 | -40.76368 | 2025-10-05 03:51:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3ec40c3a-249e-32ac-b588-95d2eae80ae6 | -0.90282 | -47.54859 | 2025-10-05 03:51:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 79c0cc17-ba12-3947-9cc9-cfdb38d69fa7 | -4.63777 | -43.18472 | 2025-10-05 03:51:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| efea6ca3-eb27-3d6b-9fc7-487b2906c305 | -0.90804 | -47.55374 | 2025-10-05 03:51:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README38.md)
