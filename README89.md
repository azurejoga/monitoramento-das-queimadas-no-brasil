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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 102b3b93-9dd0-3eae-833e-d3e5b69e87f0 | -3.5833 | -43.6108 | 2025-10-28 12:40:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 409f2a57-0e71-3889-8012-961179c0c50b | -3.5646 | -43.6117 | 2025-10-28 12:40:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 530dc01c-d683-337a-8509-dbb6ce756cd7 | -12.7786 | -47.3752 | 2025-10-28 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 9e7617c6-0215-37c4-8e80-451517c2c4c0 | -13.2262 | -47.084 | 2025-10-28 12:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 05ce340f-04ac-3c9e-9962-0c855afb095d | -3.0946 | -44.4362 | 2025-10-28 12:50:00 | GOES-19 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 7e94ab7f-71d6-38c5-8210-fe5e5727639b | -13.9337 | -48.4305 | 2025-10-28 12:50:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 20296ff5-779d-3101-bec9-a7cf693ed81e | -3.5646 | -43.6117 | 2025-10-28 12:50:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 7e1a234d-5bad-3fc2-9375-bbb4736007c6 | -12.8303 | -47.7031 | 2025-10-28 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 177c7873-0e74-34b6-854e-18add5ad0e16 | -3.0758 | -44.4598 | 2025-10-28 12:50:00 | GOES-19 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 124.7 |
| 0cbda440-69b0-3441-9754-42736b84c915 | -3.7074 | -41.58 | 2025-10-28 12:50:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 125.7 |
| 52a73319-6572-3e04-8205-0527583ef267 | -3.5833 | -43.6108 | 2025-10-28 12:50:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 122.0 |
| f2ace56d-792d-338a-b91a-3acff3b475a9 | -12.7786 | -47.3752 | 2025-10-28 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 0350fa54-d1ff-3b67-8a3f-a2d136af281b | -3.0945 | -44.459 | 2025-10-28 12:50:00 | GOES-19 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 103.1 |
| fe1ffc1f-5bc4-3d79-bcd5-f3275a26000f | -15.1964 | -47.3964 | 2025-10-28 12:50:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 78.2 |
| dd3ccb7b-d79b-3a48-bf62-b96a71c67bd9 | -14.1206 | -44.0222 | 2025-10-28 12:50:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 3895d930-68b8-3790-b3dd-defa78d1009d | -13.9465 | -47.7595 | 2025-10-28 12:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 59.8 |
| e24ff58f-4007-369c-a7e8-8acb7e27597f | -12.8299 | -47.7254 | 2025-10-28 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 144.7 |
| 442c481d-98cc-3e2a-9f22-a8d316240253 | -3.5831 | -43.634 | 2025-10-28 12:50:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 58845f9d-4def-31bc-bb51-95e09669a914 | -3.0759 | -44.4369 | 2025-10-28 12:50:00 | GOES-19 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 1ca8fb93-4de4-3c41-bade-bb170d618cd3 | -12.8303 | -47.7031 | 2025-10-28 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 51f68ba0-5ec3-3bf2-99d4-300e3c521f97 | -15.1964 | -47.3964 | 2025-10-28 13:00:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 9cb1baef-5980-3e58-9a57-1c274d4802e6 | -3.5646 | -43.6117 | 2025-10-28 13:00:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 7e7942fd-f7fc-3e3d-b87a-e9b41c55ec10 | -3.7075 | -41.556 | 2025-10-28 13:00:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 82.9 |
| bb62914d-fc74-3e6b-885a-1fa9067d82ee | -14.7625 | -44.94 | 2025-10-28 13:00:00 | GOES-19 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 76fd57a8-15c8-338b-981b-f40510a103ed | -3.0946 | -44.4362 | 2025-10-28 13:00:00 | GOES-19 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 19e7258e-5791-3ed1-9707-172f8491cde8 | -3.0945 | -44.459 | 2025-10-28 13:00:00 | GOES-19 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 86.4 |
| d134b580-e950-355c-a32a-2abb18defa55 | -3.5833 | -43.6108 | 2025-10-28 13:00:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 122.6 |
| ce30a76f-6fff-3d6a-8159-de1dcb89e5b9 | -3.5831 | -43.634 | 2025-10-28 13:00:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 1a61292d-0b2b-3fd6-960e-481620a20966 | -14.762 | -44.9636 | 2025-10-28 13:00:00 | GOES-19 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 51583a0e-122a-3f5c-863a-ff7ea3026f40 | -13.9623 | -43.2649 | 2025-10-28 13:00:00 | GOES-19 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 112.2 |
| d060560c-b5bb-3c0e-85d2-8feab6f49acb | -12.8299 | -47.7254 | 2025-10-28 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 81318a51-e5a4-389b-b17d-b5a8d53f3491 | -13.9465 | -47.7595 | 2025-10-28 13:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 6f2a1953-4d70-3e33-b996-79c28779b446 | -12.7786 | -47.3752 | 2025-10-28 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 7b79f7c9-6034-3963-abad-4584e21a9e47 | -4.4604 | -43.6337 | 2025-10-28 13:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 38fe92d4-a332-3445-90fe-c4ceb694a01e | -5.7583 | -38.9751 | 2025-10-28 13:00:00 | GOES-19 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 111.7 |
| 47c860b0-9e67-3e60-a163-93de54dd9f3e | -3.7074 | -41.58 | 2025-10-28 13:00:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 152.3 |
| 002736a2-b3d5-3b6e-8ff0-62046aa05056 | -14.1206 | -44.0222 | 2025-10-28 13:00:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 81.8 |
| b44bc60e-3514-34b5-81fe-aa662defe924 | -13.9337 | -48.4305 | 2025-10-28 13:00:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 28e6d2ff-3c15-3bac-93e0-c803d70636a5 | -13.9337 | -48.4305 | 2025-10-28 13:10:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 83.6 |
| dae72b3d-2951-3f09-bdc3-7d62a0fb205f | -4.4602 | -43.6569 | 2025-10-28 13:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 19cf1c2f-9927-36ea-988f-f7dc5170a580 | -3.7075 | -41.556 | 2025-10-28 13:10:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 110.0 |
| e05919cf-e7a9-3a1b-85f8-11ed7e3a4989 | -12.7786 | -47.3752 | 2025-10-28 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |
| d3914875-cf80-34f5-8bef-8c43808ec2b7 | -12.9135 | -43.3596 | 2025-10-28 13:10:00 | GOES-19 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 579e7483-244e-387d-a0bd-42b29c281c43 | -3.5831 | -43.634 | 2025-10-28 13:10:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 100.9 |
| efb7cb75-5b86-3e14-b4b1-1796397924f4 | -13.9275 | -47.7401 | 2025-10-28 13:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 67.0 |
| fa6edebf-d71e-3418-a9c8-aca19a726c86 | -14.762 | -44.9636 | 2025-10-28 13:10:00 | GOES-19 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 3f4cc883-4337-3b64-9b44-9bee63f9a646 | -13.9465 | -47.7595 | 2025-10-28 13:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 2e2ce455-3748-30ea-bf19-0d9d57705745 | -14.7625 | -44.94 | 2025-10-28 13:10:00 | GOES-19 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 102.4 |
| f3594b44-9cc9-3356-83f4-a930abc861f3 | -3.7261 | -41.579 | 2025-10-28 13:10:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 78.4 |
| 7ee0131e-fa54-39ce-87ec-db5e11070494 | -12.8299 | -47.7254 | 2025-10-28 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 8e0b2682-7a7f-3eb5-8a97-e8473a654ccf | -3.5833 | -43.6108 | 2025-10-28 13:10:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 130.7 |
| e9e0c26d-9e4d-370b-b85b-b21e15547af7 | -13.2258 | -47.1066 | 2025-10-28 13:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 74.3 |
| edd03dbf-41a7-3f6c-afbd-e6c32cc58d72 | -3.5646 | -43.6117 | 2025-10-28 13:10:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 5bbb9ba1-9cba-3079-9d1f-f9cda03af9cf | -4.4604 | -43.6337 | 2025-10-28 13:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 95.8 |
| a0329dee-7c36-36f3-af98-55c66c951d46 | -15.1964 | -47.3964 | 2025-10-28 13:10:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 36da38eb-3693-378e-b15e-c7c3d25c36e6 | -12.8941 | -43.363 | 2025-10-28 13:10:00 | GOES-19 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 136.7 |
| 3311f864-c9b9-33d6-afb4-8032038f8805 | -13.2262 | -47.084 | 2025-10-28 13:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 7895a748-30c5-3678-b0b7-1fa2e754a626 | -3.7074 | -41.58 | 2025-10-28 13:10:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 268.4 |
| a883334b-f1bd-323b-aa36-8d163fbcc51c | -3.0758 | -44.4598 | 2025-10-28 13:20:00 | GOES-19 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 83.4 |
| c4c1c358-f29f-326d-9082-63a5ddc484e0 | -12.8303 | -47.7031 | 2025-10-28 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 83d1a64a-797b-361e-9e3a-8ff049772993 | -13.9465 | -47.7595 | 2025-10-28 13:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 90.1 |
| f5fa72ba-46e6-3169-9759-d8e7818e0fd9 | -12.7786 | -47.3752 | 2025-10-28 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 426ef2f8-27b7-3c41-b3df-198c08e3651f | -12.3484 | -50.1779 | 2025-10-28 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 60.8 |
| b5f21c1c-f368-3aa7-b64b-87cbb6fb86b9 | -13.2262 | -47.084 | 2025-10-28 13:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 60.5 |
| aad70bf1-a31b-377d-a3bd-0caed38e587b | -13.038 | -45.8399 | 2025-10-28 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 135.1 |
| 82bfbf34-011c-3d6e-988f-6547f1f897d4 | -13.9275 | -47.7401 | 2025-10-28 13:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 78.9 |
| aa0a9eff-bf56-39e6-a809-7fbb33ffe737 | -13.2258 | -47.1066 | 2025-10-28 13:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 726fbbc7-6e6e-3926-92c8-b68bd9b53271 | -15.1964 | -47.3964 | 2025-10-28 13:20:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 66.5 |
| a352de17-0a11-3b6f-a0b8-8e434417b6db | -3.5646 | -43.6117 | 2025-10-28 13:20:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 324a7995-c512-3f03-b22b-02c77e38e6e0 | -3.5833 | -43.6108 | 2025-10-28 13:20:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 162.4 |
| c19c95d6-b200-3fc5-be0f-4fe4ee9077ab | -12.8941 | -43.363 | 2025-10-28 13:20:00 | GOES-19 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 141.4 |
| 9b069b6e-64bd-3fe5-aa6e-b4096ce30556 | -12.8299 | -47.7254 | 2025-10-28 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 196.3 |
| 22c7cb94-d548-3af8-8e41-3247d08b905c | -3.0759 | -44.4369 | 2025-10-28 13:20:00 | GOES-19 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 78.5 |
| f4b12987-5c07-308b-8a80-4d60f7297584 | -14.63 | -48.4561 | 2025-10-28 13:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 94.5 |
| e000a1da-43a2-3d37-b25a-259e7b1ce023 | -3.5831 | -43.634 | 2025-10-28 13:20:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 108.1 |
| c59e26e5-45cc-3d6a-aade-bf07af1cdcbb | -3.7074 | -41.58 | 2025-10-28 13:20:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 246.7 |
| d996aa6f-0bd7-30c8-ba6e-65872b0193fa | -3.7261 | -41.579 | 2025-10-28 13:20:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 88.3 |
| 88d8691b-e851-3aae-b25c-69df52f995dd | -13.9337 | -48.4305 | 2025-10-28 13:20:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 60.3 |
| b75bf956-9585-30b5-a0b8-21ac2b444751 | -3.7075 | -41.556 | 2025-10-28 13:20:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 109.6 |
| ce04d0f1-e2fd-37d0-9157-6a6496fe9a1c | -12.8941 | -43.363 | 2025-10-28 13:30:00 | GOES-19 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 179.0 |
| 5185af89-8707-387f-a2bb-9e8589940211 | -3.7074 | -41.58 | 2025-10-28 13:30:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 295.1 |
| 89775ccb-1ed3-38d5-8fff-1bc6190238b4 | -11.7045 | -51.2152 | 2025-10-28 13:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 23cc2f28-c021-3ceb-9d02-b45c2855121e | -5.6617 | -41.1341 | 2025-10-28 13:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 83.8 |
| a75846a8-db7b-31f8-8a99-b0a0f7fa807c | -3.2232 | -48.7594 | 2025-10-28 13:30:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 1382e016-06eb-3e0e-9e16-c1cc86ec08aa | -12.3488 | -50.1563 | 2025-10-28 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |
| b848e3b5-c95c-35eb-8f4b-e598aa07960d | -13.2262 | -47.084 | 2025-10-28 13:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 68.1 |
| f1501b45-852f-3a8c-a663-bd58e3c92495 | -3.5833 | -43.6108 | 2025-10-28 13:30:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 196.9 |
| d52f7372-1ff8-396d-8b9b-a4121c8f8744 | -5.5878 | -45.1865 | 2025-10-28 13:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 60.2 |
| f8c817fe-e147-3012-9128-57191974ec54 | -3.7261 | -41.579 | 2025-10-28 13:30:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 91.8 |
| c3b00764-1f9e-36b3-9e2a-163bd320a802 | -12.3484 | -50.1779 | 2025-10-28 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 8fc19aeb-277a-3125-aa24-000c8f4b10da | -15.1964 | -47.3964 | 2025-10-28 13:30:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 75.5 |
| b667b056-e345-3311-bfc3-0f2656b57727 | -13.9465 | -47.7595 | 2025-10-28 13:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 375ace24-6ed4-3a45-8cab-af8edce09d17 | 1.8872 | -50.8417 | 2025-10-28 13:30:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 3d28d5a2-2ad6-30ec-9427-ff7c1332c717 | -12.7786 | -47.3752 | 2025-10-28 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 638b78dd-a098-30f5-8269-9ea196d88f07 | -4.7346 | -44.4457 | 2025-10-28 13:30:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 72.7 |
| f6faa7cb-a00e-3a88-adba-6cc70994eae7 | -6.5605 | -41.5859 | 2025-10-28 13:30:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 67.7 |
| b3f1bbd8-2729-3d21-9ca5-9cee0882801f | -13.9275 | -47.7401 | 2025-10-28 13:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 1ee62f62-c7c7-3bd5-8708-ab8278978c05 | -3.0946 | -44.4362 | 2025-10-28 13:30:00 | GOES-19 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 77.0 |
| a453e8a7-e45b-365b-891c-fe6a7d09e7e9 | -3.5831 | -43.634 | 2025-10-28 13:30:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 0aa8f7c2-1ee0-36e1-a1fb-8822835fa7e9 | -13.9337 | -48.4305 | 2025-10-28 13:30:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 76.6 |


[Clique aqui para ver as próximas entradas](README90.md)
