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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4b39f848-ec89-3e9d-ae1d-b862b28b326f | -3.06182 | -53.22404 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35507c42-0079-3222-9588-314a69e0106e | -3.22975 | -53.62527 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11974a71-aceb-3733-b955-92267b77d6ef | -3.38649 | -50.1076 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 0f630c10-6b1f-3d3d-a95d-ce42e3d67ff9 | -2.95634 | -51.28575 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2ae91760-62f3-39c2-9749-0ec44aba21e6 | -3.59468 | -50.36466 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 74c03145-819e-35b0-8e09-bb377e353291 | -3.38229 | -50.10073 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5213a73-273c-31d3-9862-8be2d71e17b7 | -3.57845 | -50.33572 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 97545ffd-fba0-3fdf-b935-83574bea23cf | -2.24772 | -53.61156 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ecba1d42-2d06-3374-ba4c-5ca5befb2eb8 | -3.33097 | -52.76345 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fe1689e1-d74a-3118-8de7-5cabd4d69fe9 | -3.11572 | -54.47089 | 2024-11-28 05:18:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 095a659b-c0c4-38b4-9ab0-fbd6eb121bde | -3.32889 | -50.21953 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 677c6dbb-c6d4-3687-9e58-c871513dd291 | -2.25442 | -53.46249 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 70c5cc4c-93c2-35fb-b1c6-95aa18da76ba | -3.23309 | -50.78197 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1bb8f300-38e3-3f03-b582-9183222aa0d2 | -3.10304 | -54.03798 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d865e27a-74cf-3035-a1f3-8d0ea64e5f45 | -3.26745 | -45.37315 | 2024-11-28 05:18:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 66979625-d7be-34ea-99d5-b361c0d1b07f | -2.80172 | -51.58832 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ce8cad25-1f4b-35dc-a391-53b8f7db37b0 | -3.52978 | -52.15643 | 2024-11-28 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2329042b-ef55-3eb6-9e08-552b8644fc17 | -3.34474 | -53.74083 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d5105cc-f3dc-3a0a-aec1-f2eeca41c8d6 | -3.24674 | -50.76556 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 275e1998-483b-30d4-b78c-4b625277fa35 | -3.35096 | -50.52214 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f44fffe0-e35a-3349-a7ac-506f3e160290 | -3.69192 | -50.22561 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3d143b31-9647-35a3-840c-073274dd9fe9 | -3.7412 | -51.83504 | 2024-11-28 05:18:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f9b904bd-9b62-3c6c-b049-932955435b83 | -3.20858 | -53.84227 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02b97d94-d2cd-3ead-afee-36f8bb515fbb | -3.38517 | -50.11657 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| ec28fdc6-129c-39aa-b05b-6c33eecf4761 | -3.49932 | -50.45934 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 667aa9d2-a7d0-3fc2-a1e9-2f1f19d11de4 | -3.68275 | -51.85416 | 2024-11-28 05:18:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 66f482e2-f8a6-3870-a1b8-065112d197fd | -5.75431 | -46.26044 | 2024-11-28 05:18:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9ad20554-7540-369b-800d-76e585a5071b | -2.17118 | -52.14032 | 2024-11-28 05:18:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e187eeae-27c3-3121-a5c5-c09088894da9 | -2.26387 | -55.85687 | 2024-11-28 05:18:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40b4d7c2-5b66-3305-a936-ec2a07631538 | -3.43921 | -50.03292 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a2a0e98b-9c85-3196-a957-6adc8b405ec2 | -2.37117 | -56.12167 | 2024-11-28 05:18:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9cb1c33e-99f1-3d8e-8526-64dc70691c2f | -3.08548 | -53.98804 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 529ac4fa-393e-3809-b95d-8ab9d4803572 | -4.0389 | -46.54202 | 2024-11-28 05:18:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fa66b908-f1d9-3b2b-874b-6531323ffd79 | -3.17179 | -48.43904 | 2024-11-28 05:18:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1cbe378-22d2-3975-8852-32397e5de0f3 | -3.50358 | -50.45946 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c12148bf-0406-3b3f-b777-85e16bf89e24 | -1.86616 | -53.94963 | 2024-11-28 05:18:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| adab8787-74cc-3bc3-84ee-a402e2dd54c2 | -1.98837 | -53.29027 | 2024-11-28 05:18:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c65d0a4-fe21-38b0-90a8-1d2282e2d2d4 | -3.10474 | -53.81084 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| b4aaa06a-2a45-3c96-bb89-4e7c3d68b57e | -3.7405 | -51.83964 | 2024-11-28 05:18:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 61a9f652-c2fd-30b5-9944-e4d37fb663de | -3.10953 | -53.1042 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ae6051ad-ad84-3660-a3c2-4627b32c01f2 | -2.61434 | -51.80704 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 291e5266-8dfb-346f-957b-082d614ec35d | -2.4283 | -55.37356 | 2024-11-28 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| debcf3bf-9c7a-3dc0-ac91-653a8fc431d8 | -4.00033 | -47.91382 | 2024-11-28 05:18:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2800880-3a97-3fdf-b830-d14ea0cd8d44 | -2.58198 | -54.23421 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 340ae9cd-cdf0-3ab8-a58c-a53c4988d90f | -2.8495 | -54.00814 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 047d7125-a3dd-3971-98dd-9c303b6fc550 | -3.07839 | -50.25324 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 27bc07b9-0d83-3bfb-9096-1580f0585274 | -7.79736 | -49.99944 | 2024-11-28 05:18:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42461851-ccd5-358a-a1c0-348d7cd4b780 | -3.44232 | -50.01204 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7267412f-5746-3d7c-9d50-db5782d52c45 | -2.20294 | -53.74685 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 799da26f-420a-3fae-a84e-46a3ef412c0a | -2.23405 | -55.90006 | 2024-11-28 05:18:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| d13420fd-3146-36df-a6ac-ec8d405558d5 | -3.27058 | -53.30363 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ec749a72-3ecd-3ef9-8ac7-a93df4666e8a | -3.15657 | -54.48186 | 2024-11-28 05:18:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 23c1efb6-9af3-3420-a806-1352a993c58f | -3.23418 | -54.22686 | 2024-11-28 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 69f519de-46ad-3c99-89af-965ecc980056 | -2.8603 | -54.02625 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b7ffaaf9-5208-3274-981e-d65846e8c62c | -1.99236 | -53.29089 | 2024-11-28 05:18:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8e56beaf-9dc2-3c64-b5a8-7d80e690dc87 | -3.68697 | -54.20637 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| de513071-7494-3f01-85dc-3e646bd14239 | -3.96767 | -48.06768 | 2024-11-28 05:18:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 33e95ee2-ef5f-326d-a718-e7b9587137d0 | -2.87421 | -54.00208 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 34c63a14-cb5e-3b7c-a4b3-887a7d152285 | -7.79689 | -50.00303 | 2024-11-28 05:18:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0c7035d3-5c2c-3f0b-8ada-2fa2ca0cb7c3 | -3.68686 | -50.22488 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e985b356-1ce9-3ef2-b27a-b11fbf8b23d9 | -3.54337 | -50.18628 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca394672-7dad-315f-9b15-38d09fa12d93 | -3.69237 | -50.22258 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1613fc17-d8bd-3e8d-9462-9ce9fb50c40a | -3.31471 | -53.75162 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b99413d2-fb1b-3e43-89b5-3d2cc6e9f9ec | -2.74088 | -54.11123 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0cd6464a-cf14-330a-9a51-670d2b94e07d | -3.06055 | -51.29971 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9da0093a-9994-3d04-b601-b85fffa9396f | -3.15076 | -50.14285 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c5988912-4f50-3020-9512-1444b4bdec3a | -3.27293 | -50.62616 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b6bb5139-1600-3aea-9819-11e3698cd92f | -3.08796 | -49.21193 | 2024-11-28 05:18:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3153495b-77b3-377e-b303-b7ffca96e297 | -2.58429 | -54.06553 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fcfa400e-03fc-3423-9e10-5d9404a6decd | -2.73962 | -54.10894 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 2a5f6a1d-72be-3408-a5f1-7ed8e764c528 | -3.10366 | -53.81861 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| c82d27ce-e750-3aae-95ae-469358c2c983 | -3.43836 | -54.53843 | 2024-11-28 05:18:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2476fc6e-90a6-34f5-9f89-3da7c35016c1 | -2.77482 | -54.03121 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c54a433f-16a8-3311-9b8b-837773c80680 | -2.80312 | -51.58652 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 617ce7f7-5782-31ff-87b4-e184da4274f7 | -3.22763 | -54.08811 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6420ce12-07fd-334a-9ab3-7fd81bbe33ef | -2.25325 | -53.62789 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 28ac22e7-5625-3950-9c0b-b6a83ce3befa | -3.50464 | -53.79505 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0bf28a4c-26c6-377a-ab9d-02f27e2e2638 | -3.06001 | -51.05999 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d3de93d9-a33c-3e06-b041-d6fd5e89a250 | -3.36847 | -50.83023 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| e37ce2fe-a6b9-3ada-9b5e-53d41434f7cb | -3.04477 | -48.51397 | 2024-11-28 05:18:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 52e0004f-efd6-3eed-9038-6637e05ac77d | -3.09455 | -53.25442 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 11050f3f-dde6-37a7-a92a-d0a379dfd657 | -5.98033 | -45.35592 | 2024-11-28 05:18:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 9f1dd065-a003-3d43-a53a-6ed266486b5a | -2.85575 | -54.01896 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d9fbeb13-aae6-3575-a87e-0e4fe8d0aaa0 | -2.98733 | -51.44946 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| d12737da-99d8-38c3-8d6f-179e11c5cd54 | -3.92021 | -53.66805 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 9c2f1310-c3f2-38cf-a22e-a4554395c1a0 | -2.88248 | -51.58478 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 753373da-705f-3872-bf50-54b84c5043b3 | -3.48589 | -49.89681 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be0c8a30-267b-31e3-9177-e9faca0c4d08 | -3.73957 | -54.07612 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4307697d-c3b4-3918-9d06-9eaf25632464 | -2.23754 | -53.62547 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9a3ae773-a388-3d52-82ac-5b491383e0ff | -3.29016 | -50.27668 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee876338-3054-3763-9aec-3fce717e2f32 | -2.31641 | -51.95875 | 2024-11-28 05:18:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 94536f4c-23e1-3ef7-9854-973006e3bae7 | -3.62805 | -51.49487 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a57dbddf-c5b3-30cf-b83e-551b9ce304d0 | -2.58117 | -54.06021 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 10ba39be-eb86-385b-82c9-2495541bfa30 | -2.60735 | -54.27128 | 2024-11-28 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b8920383-3aa3-3a1c-97a9-8f1d5a7675b9 | -3.29057 | -53.85703 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 768bbd4d-2a51-3a9c-b948-1952edb99c92 | -3.41232 | -50.24754 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87b60536-2c0c-3650-a7c8-c96087c93e19 | -2.91187 | -54.18081 | 2024-11-28 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a30714bc-64bc-3d33-95ba-c0730de14352 | -3.25419 | -50.61766 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bcd9fb58-557e-36d7-a754-43a1abcc7f0f | -3.24085 | -48.4814 | 2024-11-28 05:18:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93ce3fd7-3249-3f1a-970c-6627cff3d622 | -2.27139 | -52.83617 | 2024-11-28 05:18:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README81.md)
