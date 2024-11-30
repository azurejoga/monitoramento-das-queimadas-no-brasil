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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cacdd2ae-54ee-3dbf-bcf2-23cc2f9ac0eb | -1.31727 | -52.79596 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 214dd60d-597d-388e-8b91-7cbb7d285888 | -1.23938 | -51.80069 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8c4f6c52-f235-3d75-8a33-075c238ba1d1 | -1.4437 | -55.1289 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 7600d981-c2c4-31c8-b659-69c65364419e | -1.60775 | -55.43964 | 2024-11-30 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab26c1ee-80b0-3f94-9aaf-12f18aac82ee | -1.44855 | -54.53969 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 50a7d210-9636-356d-bed9-f0e1ed5f3815 | -2.25771 | -53.45721 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1ea05d2c-f953-3433-b888-cb01a4be03de | -2.82333 | -52.9656 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 92cb151f-6f52-36b0-a16f-2c4b52753f24 | -1.17964 | -53.88221 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3bbf75de-55de-3d2e-babf-39e67c37dea8 | -3.58665 | -50.51302 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 12334c0a-d907-37c9-9112-866993cb901c | -3.42424 | -50.42857 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 29bc8d55-bcce-3395-a575-5b6f4bcb58d2 | 1.67287 | -50.66117 | 2024-11-30 05:01:00 | NPP-375D | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cbc4eea9-1194-38fd-b110-7201a5850513 | -3.48046 | -50.25003 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 96b62bd6-a267-3f07-be8a-c93011f9b8e0 | -4.12329 | -54.20573 | 2024-11-30 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fab501e7-4aa6-3da6-865b-6696e4ae1f2b | -1.63258 | -53.86335 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2776cb08-7fa6-392d-8635-79eb039be1a3 | -1.86147 | -50.80802 | 2024-11-30 05:01:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b7e2ac5-301e-3117-87dc-c92bad1e0842 | -3.7691 | -51.61643 | 2024-11-30 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 05bd7006-193e-3e9d-8c35-074c762a167c | -2.88214 | -52.68206 | 2024-11-30 05:01:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 409ad42d-2e8c-3974-be3d-3e7ec8bb3d58 | -3.95915 | -48.09421 | 2024-11-30 05:01:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 455276a1-7e41-38c1-9ef7-456a91bfc341 | -3.21684 | -53.61946 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec90dbf2-eea6-3837-b6c8-10b981ec026c | -3.23994 | -53.92142 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 84b1c187-975c-3cdf-8b72-6929c0c47e30 | -2.61819 | -51.75988 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| baadff47-9ce4-34fe-a5db-bba8225b0844 | -1.00206 | -51.72494 | 2024-11-30 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 8.7 |
| a5f5a847-5ee2-31bd-b22f-24cef05a90be | -1.66576 | -54.02169 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0cfda51f-cd44-3297-b34c-296088134879 | -3.40002 | -50.66214 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| fd8354ac-77f1-3a6b-b485-e9fad34d6374 | -3.99186 | -41.52082 | 2024-11-30 05:01:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 437bf0a0-1bd9-3328-bd5a-e0dc3c506ebd | -1.54687 | -51.93419 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| dd7471ea-e5c2-3582-bf41-4b605e92ef21 | -1.39376 | -51.98848 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9a4c1a44-18cb-3c76-bfe9-a0a2b3e65a8d | -2.52076 | -54.1366 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4a0bfcff-8fcf-3e60-9d80-a4a7cf4e8c48 | -3.04892 | -54.49676 | 2024-11-30 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 890bca15-fc8f-3c66-853e-efc68f3510e4 | -4.67349 | -46.37146 | 2024-11-30 05:01:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 980e4832-a776-36f2-8bc6-7024d0648b9e | -2.94607 | -51.58579 | 2024-11-30 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3907c2a-2335-3676-93d8-670aaef6e3bf | -3.33547 | -53.21762 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e296379a-a234-365e-9245-b46943755d75 | -1.99745 | -46.81351 | 2024-11-30 05:01:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9bc4865a-8551-3030-80e1-10434a5a2522 | -0.9985 | -51.72438 | 2024-11-30 05:01:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 03e17789-9b5e-315c-a906-ae10a891305f | -3.23135 | -53.41462 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 304bacd3-3cd8-3efa-bac7-b0e135a9453c | -3.48069 | -53.8093 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f1c1bc7d-718c-3116-b57a-6fce8ef81e9d | -2.59252 | -54.21537 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1fa23a54-5039-3e4c-863f-6cc93c86d797 | -2.61716 | -51.81472 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3beebb72-b0d3-32cd-b89e-9fae966d730a | -2.5171 | -48.18748 | 2024-11-30 05:01:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad0350db-8ab1-3bbf-b3a4-d9ba0c7ce894 | -2.77181 | -54.04734 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 63876c46-f677-3a80-9624-1062dfe407c8 | -1.44387 | -55.21417 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3048634-4d77-39b0-aeb3-b123b9cf880b | -3.02725 | -54.02902 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 27337210-b0a9-3aa8-877b-f906c460e61f | -3.23775 | -51.55719 | 2024-11-30 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 001ee1fb-5d01-3a83-aa21-2e3851dbb2c5 | -1.72422 | -52.48666 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 65e1c457-8c11-34c3-b45a-1531eaedadc5 | -3.09138 | -54.03532 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef98bac8-1774-35f1-b761-a4e643cd10c0 | -2.31745 | -50.65589 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7a7bd59e-9be4-346e-84c6-ed1fe0ad94ef | -1.05313 | -53.18586 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8da781ca-5163-3d56-a14a-34d59567527c | -5.07613 | -44.99224 | 2024-11-30 05:01:00 | NPP-375D | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f8b22307-88ff-306d-9fa7-86b4c27ee174 | -1.10308 | -53.40435 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1427d7b7-3449-3eee-ba55-5da8ed8b1e8a | -3.3134 | -50.50168 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c2a042e2-4eae-36bf-8678-16da89f3112b | -3.99932 | -49.97993 | 2024-11-30 05:01:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3ec36842-0bda-3652-8ecd-26309482f5ad | -2.85212 | -54.02735 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9c60c6b9-ec02-3b04-8ee1-143f3aa1dd0a | -1.74579 | -50.83364 | 2024-11-30 05:01:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ded862dc-7e74-3b5a-9a72-fdfd7da3a7e5 | -1.34882 | -51.3898 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3bbc4a28-071d-332d-8dc4-d888d1a12a5b | -3.11118 | -53.98853 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e1ffa6c5-8251-3d49-a376-b3fe37c2c8f4 | -2.98139 | -53.35833 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 538e08cb-5f62-36e4-bb2a-565bc6f3f300 | -3.02335 | -54.03201 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 448252de-7bc5-3e24-875c-88a5c480d033 | -2.1417 | -54.88826 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 8f4765c7-f234-380a-ad2a-31e3bbf32c6b | -3.14759 | -53.7219 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f60256c-520a-32e9-969e-db3f3b0d163c | -3.49758 | -53.83374 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6349c268-52f3-3ad8-b351-a14023cc57b3 | -2.69234 | -48.60233 | 2024-11-30 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c6a2eac-4e56-3e61-8ff0-c98ddbc47e5c | -2.33111 | -54.50105 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fb11acb9-9cab-3ad7-9f82-5f4ec0b935a4 | -1.36227 | -54.66039 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 52af953f-6598-3f3b-aeb3-2b92755da588 | -1.62453 | -52.4566 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bf3ca705-79cc-3fad-b0f7-72f77935d73a | 1.20121 | -55.94896 | 2024-11-30 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4395eb29-a084-3384-9ca9-9260b7883ecd | -1.62487 | -53.89078 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 81b41479-f227-39d2-bd7c-e5807e4dabeb | -2.62361 | -54.21302 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c8c62ff2-b570-3476-a8b1-6e479bda820a | -1.40144 | -53.39588 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bfb20276-f07f-32b0-8e5a-ef6263a67543 | -3.10106 | -53.33174 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe5ce834-be8f-304c-b219-995e9cd85f96 | -1.20235 | -53.86787 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 244831ad-64c2-3bd4-8101-742eba400a5f | -3.1985 | -53.42462 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e231c92-d123-3a35-bcce-aa1df2edfea6 | -0.82138 | -51.61327 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e4000025-33df-3925-9139-208f25a54511 | -1.29193 | -51.36972 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ebaea50d-d026-31ac-8839-329889f32557 | -3.29206 | -53.67472 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef8b109a-c748-300a-bc1f-a318a6501568 | -1.42679 | -55.27909 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5ddc0310-766e-38af-9fc0-59aff25b1934 | -1.1564 | -53.62144 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c160916b-3b70-3dd6-86e5-b062a3f5d3d4 | -3.44592 | -49.48055 | 2024-11-30 05:01:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b3bc434a-6530-303f-91a4-76c953734e25 | -3.22979 | -53.62519 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99c2806e-f28c-3bb7-af82-4fd557ac3e40 | -2.90364 | -54.77432 | 2024-11-30 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 221d58f1-1ccd-311f-86a8-7c9be0a35720 | -2.63458 | -51.74965 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f35b2503-7a70-3671-a71e-dfdc2d59fe50 | -1.57897 | -53.84074 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c7d215d8-a6c9-36e0-9733-6b1db4a57c57 | -3.11125 | -54.01012 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c016dc11-7e2a-345e-afe5-0ca727dc1fd7 | -2.83764 | -54.03228 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d41ad691-4e4f-3902-9a3c-bbab1de589f2 | -3.48351 | -53.81339 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 38d17352-fae5-3c07-a770-b801361a50c5 | -3.2683 | -50.56031 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b65d44f-2bf5-380f-8ec2-b22402b223c1 | -0.94862 | -51.65646 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7910e4b9-51b8-34df-bb59-bb762f2d9558 | -3.25167 | -53.28361 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a1c80ad-7dde-329c-bf03-4fc51c352ee1 | -3.12874 | -53.26441 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e789df19-7c7c-3aac-888f-2080c2c81607 | -2.30539 | -50.68282 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0d951ddc-bc59-3682-92da-9e72795fb813 | -3.49813 | -53.83021 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fdb01c9e-9043-3563-972f-0ed49ce1410f | -2.34053 | -52.72072 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 072a5aeb-6b81-3190-90ba-3ac8a648f04b | -3.30522 | -53.83377 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 86752fcf-16bd-3d42-8470-ef32189bf109 | -1.25776 | -54.54884 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dffc0003-8e41-3a25-b10d-4f87862e4e60 | -2.4647 | -53.97063 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5894215b-58bc-3c67-81c0-f68c37f18905 | -3.30173 | -50.76036 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c35ed3b-f802-32d8-b027-5322c5721093 | -2.76509 | -54.02477 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 565a7fb2-672d-30eb-aaa8-0e173d7c6aaf | -4.02871 | -54.63502 | 2024-11-30 05:01:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6927f56b-dcbd-39be-8066-1882ff63c164 | -3.46998 | -53.78942 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 07dc440b-b495-301e-9c56-9f8dc97b7a7f | -2.7661 | -54.11787 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 32366d03-c8b7-3e0b-a82b-ffb671b7cbd7 | -3.46576 | -53.88327 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README86.md)
