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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7b8f1100-4a01-335c-8544-0093937f6a62 | -2.76577 | -45.87081 | 2024-12-03 04:29:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe0facc1-90b2-34d5-8c72-d83b81d3b853 | -3.81113 | -46.54669 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 26b0e04f-5495-3a74-af88-89fb8c72ae9f | -6.03629 | -42.52137 | 2024-12-03 04:29:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 156d34d2-3fc4-3b69-ad51-3ff60c303827 | -2.7338 | -46.24817 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 74d09ac1-cd7c-3016-adc4-6188caabfe5a | -2.88515 | -54.16203 | 2024-12-03 04:29:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 807fb9a7-79a2-3e43-a0a8-27ecfe00c595 | -3.70402 | -51.82511 | 2024-12-03 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8de4e161-f050-3cb8-b023-a0c4c2e7647a | -3.16514 | -46.63745 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b410180-2d18-39b9-925d-6eb1f7340e22 | -5.27782 | -47.78432 | 2024-12-03 04:29:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 632bd21e-71e8-36cb-aca4-bdf88327a5f8 | -4.081 | -46.68837 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2181923e-104b-3aad-98d3-496ddee4f0f4 | -3.76111 | -52.66636 | 2024-12-03 04:29:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f2e2c2d6-e766-3fbe-82f6-43fde9a20ee1 | -3.85526 | -46.52518 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0a464312-5696-35b7-b1c2-374de6b01f08 | -2.80085 | -45.94744 | 2024-12-03 04:29:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf032ee5-f367-3444-bfca-dfd25fe5b726 | -2.66115 | -46.10502 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2bf32f35-627f-35fe-bcf0-d3ad63df5800 | -3.23734 | -46.41518 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef7a474c-4f47-35b9-b05b-a768eb9129e6 | -3.76052 | -52.66995 | 2024-12-03 04:29:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c0a318e7-952f-33b6-b50b-2c4f7e89b11d | -1.61168 | -54.24385 | 2024-12-03 04:29:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0cc9832f-e3cd-395a-8445-ce71c68152ac | -3.17708 | -54.34118 | 2024-12-03 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b3c3dad2-9b23-3328-8117-abb2f3cbabd0 | -4.04617 | -46.86688 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ec68ef41-f16b-3925-a150-3bd7fa537388 | -5.22117 | -44.90798 | 2024-12-03 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 655e11a3-2d6d-3b09-918b-61ffc48ca5e5 | -1.73333 | -52.77469 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8677b906-b213-30e6-8c4f-e91c8bd55ccd | -3.02934 | -53.42579 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 06e884cb-a1d1-312c-9d2f-c22f7d3598e8 | -2.81285 | -53.06662 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 289dd78a-86ea-3ee1-abda-49012d749fe2 | -4.31308 | -48.21214 | 2024-12-03 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0a0e181d-453d-3dbe-8e42-648e620e802e | -3.89994 | -46.67436 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 71244299-6ecb-34a3-af2c-cfc43810f7bd | -3.8176 | -46.67889 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8f868e07-0ee6-35bc-9f07-ef1fb5e38eb1 | -1.74102 | -52.64632 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4dfaa082-449e-39e5-a981-093e35d4ecab | -2.25922 | -51.23843 | 2024-12-03 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c97bef2-0e6b-3ff9-8c8b-ce9366651295 | -3.95321 | -46.91948 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0a75ad4-53d1-3812-a655-3be8aff62d1f | -4.15041 | -48.233 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a94952ce-ad8c-3b7c-b4d4-39a515c022e5 | -3.25897 | -46.45044 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58d363cc-14ad-39bf-aad9-caaa1c4cfb6c | -3.51771 | -51.65968 | 2024-12-03 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66f26f37-0d2c-3984-a896-48c7d093f195 | -2.58492 | -46.56769 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 86b9dad3-5928-3438-94b7-4c44e91edf60 | -3.90157 | -46.66398 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0a804c13-594f-3985-91c6-7ada9b06c9d4 | -2.97477 | -46.94248 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cb251d9a-a68d-3730-bb01-26b0ce69b5ca | -3.78348 | -46.70189 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d0c19392-5281-3364-9b39-e6bf3b990718 | -3.4627 | -49.96964 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e5c5a53-71b0-3687-a3ce-aeedc3e5c0ba | -3.27131 | -50.21302 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e1a446c0-51ae-331f-b4fc-50585b2512c4 | -2.66817 | -46.12424 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 50be8bc5-aeb8-355c-8a99-c45a16ccc569 | -5.14133 | -43.23783 | 2024-12-03 04:29:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 94805755-424b-3439-8e2b-c69669523d1c | -2.64367 | -46.58426 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d2de8ada-8daa-3263-8061-eefd70046901 | -2.57289 | -46.407 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 695813b5-49e7-3fd8-956e-49caaabbdbae | -2.63406 | -46.12576 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47e1f9ab-5167-301e-b4fe-4a4e76d7a9de | -3.93197 | -47.98056 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 632252f3-1ad9-3fb4-ab04-324221a59556 | -2.36076 | -47.41002 | 2024-12-03 04:29:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 92ca8d49-ffeb-3335-af0f-7afda306c5a2 | -6.98911 | -43.51387 | 2024-12-03 04:29:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ceb6b558-9ee2-33db-9ef0-7d27df8a75b9 | -1.36769 | -51.97688 | 2024-12-03 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 36865f2b-0ac7-3580-afe5-7f14994287b9 | -3.26168 | -53.83535 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dde5378a-64bf-35ce-898d-9b58dc47383b | -3.22196 | -46.44826 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dee072a8-69c3-3115-bd1b-f0bebeb25394 | -1.73673 | -52.64563 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6cb842e5-3a11-3597-8f13-1ae91b4bf9c0 | -3.35345 | -44.35321 | 2024-12-03 04:29:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3663b332-e17c-366b-b1fb-fe201f32cf34 | -2.5935 | -46.27577 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 23cab617-cfc4-3d9d-b223-b6262fe08c88 | -3.85803 | -46.52919 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| be8cee8b-6913-323a-bc5f-12c5c148bad1 | -3.60349 | -45.59819 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f4ea42c6-73e3-34c8-acbb-d5316d4368dc | -5.10895 | -43.21851 | 2024-12-03 04:29:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 3c5a557f-6815-351b-b140-fc94800e6057 | -3.93542 | -46.92366 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b7576f4-94bc-302d-8f86-117dd0c36468 | -4.29973 | -48.2316 | 2024-12-03 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dbdaf817-f139-32d4-a199-6c9ac82832b1 | -3.55148 | -50.19929 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ffa092f7-40c5-3ed6-8299-573d9ea25414 | -3.75423 | -48.15656 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bf68b360-e7d8-3366-8a2f-cd0dd2abcbe8 | -6.03172 | -42.52433 | 2024-12-03 04:29:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9630772e-1d47-31c2-a677-2827aed72dfe | -2.63428 | -46.57928 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98178204-7813-3103-b547-162f495db01d | -3.89711 | -46.64909 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3c046e33-7ae5-37ba-a94e-e4fb67f31529 | -5.45469 | -44.82487 | 2024-12-03 04:29:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1ffde3fb-0f67-3fef-98e5-21167449370b | -2.81218 | -53.07077 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 621c03b1-972c-3ab3-b4d6-7632c5407ef9 | -4.02369 | -49.94662 | 2024-12-03 04:29:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9bdbe516-8ce9-3460-8726-9945ba944f70 | -3.99918 | -46.64724 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fbc195e9-78cb-39ac-a949-a9c51cfdfd7d | -2.58459 | -51.92094 | 2024-12-03 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72aeb594-9e5a-3ff0-b5c5-137b30e54904 | -3.34663 | -51.22038 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ad4b6f8d-a6a3-386d-8692-cf188dc6ce3b | -2.56904 | -46.40993 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 95b4f84c-4854-3e14-9908-bc8c0cabe97f | -5.69554 | -46.59293 | 2024-12-03 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f8e29f8e-b86f-3bcb-8ad6-304249f64056 | -4.11577 | -48.5393 | 2024-12-03 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8a31f314-8099-363b-9401-50df4a92918b | -3.05197 | -54.50006 | 2024-12-03 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d0149363-0538-374b-a986-f400115967ee | -1.90407 | -52.85649 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 19bdaac9-aebd-3dff-9525-d42d9f3fcb51 | -3.99148 | -46.63179 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 44b2888e-f66a-31ec-a847-08c681d1378c | -3.93205 | -46.70768 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d0b36be1-3b84-33e8-a4da-5f543f4d9d59 | -5.41691 | -47.56943 | 2024-12-03 04:29:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b786f03-6c0c-3e86-b490-7f86aca025cb | -3.89555 | -46.68076 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7cc80174-6703-3678-8c2d-ea0f3e2f2c25 | -5.79457 | -46.478 | 2024-12-03 04:29:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7f386727-e86d-386f-af67-4c662d6f5451 | -5.1135 | -43.21434 | 2024-12-03 04:29:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 22.8 |
| da2a2985-4d0a-3f34-aa54-d8c742f4bc30 | -2.47127 | -46.57814 | 2024-12-03 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5bcb5f88-b647-3785-a817-71f86b6a84cb | -4.14596 | -48.2395 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9453cf87-6fff-3647-884a-d45a83ebd45c | -2.59406 | -46.07684 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4defa07a-e1a6-354d-bd03-b8376882514b | -1.36055 | -53.64894 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c193c44a-4ad5-34ec-9fcf-65548464f28a | -4.10962 | -48.53468 | 2024-12-03 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 03b41796-1238-368f-8898-4bae688c9508 | -3.33269 | -45.6088 | 2024-12-03 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eeee31a2-3bb8-3434-817e-4777b61aa9d2 | -4.04275 | -46.82395 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87ace4f6-acf6-3e37-ad12-4c9127a017e6 | -1.94649 | -53.34586 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 611d3873-c450-3a6e-9ef8-ef1b7751ea4f | -6.81731 | -46.77703 | 2024-12-03 04:29:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 15e977ef-6b6e-322d-88a4-4d50dcd244ef | -3.25795 | -53.62971 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9f28408b-abe5-3cc4-b126-3596022d30a7 | -3.33085 | -50.07027 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9260f5d3-6937-31be-927e-90244b05e825 | -3.07558 | -47.80993 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 242b318b-468d-3470-bf80-e8596f7d10d2 | -4.00396 | -46.94149 | 2024-12-03 04:29:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 321942be-84c9-30be-9a3d-02cd1947c714 | -7.23572 | -46.74708 | 2024-12-03 04:29:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 25f9ba4a-5894-31c3-8d78-3397cbb880fd | -4.39644 | -49.7697 | 2024-12-03 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 59778a08-4041-3622-883e-2862ba473ef3 | -3.92989 | -46.91574 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c935ebef-0edd-3e7c-b739-945d1a999c8b | -5.22783 | -44.2352 | 2024-12-03 04:29:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 18bf7fe6-6835-398e-ad81-d2704b1046c4 | -4.01462 | -47.00305 | 2024-12-03 04:29:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ff5a138f-4a11-33f0-844a-725761332c6c | -2.48576 | -46.57346 | 2024-12-03 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4b95b189-f9ad-3975-878c-0c3b02fb3145 | -3.26505 | -46.93124 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f6e591a-e9f2-311a-a78e-86e60ec3bb69 | -3.08996 | -54.30311 | 2024-12-03 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e74ed225-3dc8-3dd4-8dac-ed00598b6534 | -1.99822 | -52.09788 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README53.md)
