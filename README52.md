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
| 7f322a15-05ba-3817-99f2-66b3c8dfadf6 | -2.29495 | -48.41658 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 15301528-5f7b-3eba-81be-33cfdc1d286c | -2.98598 | -53.35439 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 36fee3ff-0660-3da5-a119-32c4435d410a | -3.33144 | -50.05368 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c630c654-e929-3e4e-aacc-4c25f34b750e | -2.96853 | -48.04311 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ebbf87b4-41a7-3ffb-9663-d7bd8403ec4a | -2.88302 | -51.78675 | 2024-11-30 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8dd767ab-7078-3e8b-9b1a-4bc5f2f98cc9 | -2.19421 | -48.40754 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a460e615-3a64-3aa0-8210-f26442118478 | -3.62236 | -42.73894 | 2024-11-30 04:40:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 02969e34-4ea3-359c-9f23-d2b4aec1ae3f | -3.27419 | -50.61451 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a1f8707-b9cd-34ec-8225-e27e0c50641d | -2.95375 | -48.33573 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 78807fc1-3c91-35be-ae56-a58e094e6c36 | -3.22254 | -50.44786 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a7e1b6fa-7c61-3f4f-b0d7-b7d233c8c72b | -2.11536 | -50.59676 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2a40af98-6a6c-3033-8058-5379ab67fbd8 | -4.11371 | -48.53034 | 2024-11-30 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 35706f82-8231-3257-8844-63640c662c67 | -2.61274 | -46.57182 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9a3ad0fb-ed1f-318f-be68-882209ab159a | -2.58648 | -48.20374 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a5291cbd-1b02-3754-be22-cef1e9f31bfe | -1.02138 | -50.87696 | 2024-11-30 04:40:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f8dc5513-58b1-3fae-a40a-611c99483f6b | -3.97801 | -46.74514 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a645e13-3768-30c8-9bd5-6dee73b1fc29 | -3.6806 | -47.12869 | 2024-11-30 04:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 778bfe0d-bd42-34c6-bd9a-43a0ef925857 | -2.62198 | -54.21397 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| beb415eb-f123-3a47-a16e-c95a7483b4c1 | -3.26737 | -51.62757 | 2024-11-30 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0fa1df6d-e0ce-39bf-a0b7-2ce8672b3850 | -4.11289 | -54.41338 | 2024-11-30 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f53da9bc-bb64-3fcd-ac3c-23a7475356bf | -2.80226 | -48.56595 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 43b20797-2058-3af7-804d-523afe107a60 | -3.34218 | -50.52191 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c1ed2490-a54b-37a5-89b8-b5ff2b6cd97a | -2.25493 | -48.45618 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 70cac379-8686-3897-b683-c8db4d3b1394 | -1.68412 | -45.78252 | 2024-11-30 04:40:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d323637d-1647-3330-8742-daaf796a5065 | -2.00865 | -47.85157 | 2024-11-30 04:40:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8ce2f81-a765-3ce1-aa57-8b49e9e8418a | -4.41765 | -46.14603 | 2024-11-30 04:40:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 93f27a67-3e01-3339-a54f-6af257ae8f9f | -3.09399 | -54.02907 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 096457f7-9b73-3269-8c60-869c8886a69a | -1.97122 | -52.89338 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1faed5d7-4c1a-38f0-ae43-837f954845ec | -4.62314 | -48.0276 | 2024-11-30 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5f566a32-67da-3426-90d9-0bce43db6bbf | -3.24246 | -50.14462 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f839eae2-14d3-3f82-a45c-53849d735deb | -3.58537 | -50.36145 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa722ad1-d1fc-3fa3-b2c0-745aae2bf611 | -2.55706 | -47.29551 | 2024-11-30 04:40:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e73ece97-43da-3e90-b541-19ada8cf9412 | -1.50331 | -47.47251 | 2024-11-30 04:40:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 80574cb6-4bcc-321f-a02c-513e9470a690 | -3.78983 | -46.69414 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 78e7c758-0cbe-3b94-af6c-72b585e21c84 | -3.49418 | -46.40409 | 2024-11-30 04:40:00 | NOAA-21 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c8ff2950-722d-31f2-bee8-0ea795e3c9b8 | -3.5943 | -49.98365 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 30921093-38d0-3df8-9e65-ad733e8862f8 | -4.06142 | -49.06249 | 2024-11-30 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 35399e83-c314-3816-8b8c-8edc486afb12 | -2.58436 | -49.22167 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42c09e01-950b-32bf-bc3b-5c31401a926b | -2.83436 | -54.03104 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9464dbd1-6912-32fe-b889-0da8c6be3409 | -3.60598 | -49.99624 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1744391c-1937-364d-b219-38fc0fa1d1bd | -3.33603 | -50.22062 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 37af6b6f-7a58-3581-bcec-15ec69544383 | -3.28603 | -50.62748 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7219d5d9-c790-3e86-b63e-763784da8a3b | -3.94986 | -49.95013 | 2024-11-30 04:40:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5c25f0ca-5f89-3ea1-8086-34aa21b0bce0 | -3.10005 | -50.35918 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2dd0bbae-fc95-37c6-b86f-7aea5e45aaf9 | -3.48653 | -50.21184 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b104ddf1-9923-38bd-87d3-d7b84c150ee8 | -4.07576 | -47.02362 | 2024-11-30 04:40:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b88206ec-4b9d-350e-8e77-b79609b08663 | -7.89849 | -46.67035 | 2024-11-30 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0cf1ff70-db2b-3c39-a14d-ddb55206c949 | -3.23169 | -50.44541 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 47210265-719a-365b-96a4-805312d2330c | -2.93035 | -48.00462 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 935f53ef-f110-3790-8a7b-1fee897cfc96 | -3.25464 | -53.63898 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 747ab63e-7a58-3c0e-be78-fe42f2865609 | -3.33451 | -44.00606 | 2024-11-30 04:40:00 | NOAA-21 | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d32ef805-2547-3f71-9f84-cd82c453dbe9 | -1.68557 | -46.78039 | 2024-11-30 04:40:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 1aa1a1df-9d14-3025-9dfb-d917c4b3f5d3 | -2.67108 | -46.26558 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40885348-f43a-3b90-8eae-acd1be179056 | -3.14572 | -53.72026 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b2b28154-1ea8-3ed6-99d5-a4a13d52a47a | -3.25541 | -53.85733 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c291dfbc-dd88-3a61-b436-930bcf82f828 | -1.24372 | -51.62918 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d0fce48a-d094-375e-8659-0748899c039e | -2.1999 | -52.24448 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cf54e77b-9a97-3546-98ad-0b717b6293f4 | -2.94367 | -51.58694 | 2024-11-30 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 31612fc2-9e89-34fe-8170-328918c62b7c | -6.08543 | -48.0487 | 2024-11-30 04:40:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a3ca254f-d6fc-343b-8953-7f5d8c921044 | -1.91072 | -52.91066 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da4e42de-d09c-3b6f-8305-bd198ce5c3f5 | -1.85557 | -50.8202 | 2024-11-30 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a613f993-74c1-3825-b015-b4f1e1714009 | -4.8509 | -45.56669 | 2024-11-30 04:40:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d21ef0c6-0617-3a4d-aab4-05d5107cd2d0 | -2.28129 | -46.44494 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bef7b83c-610d-3a34-a118-89fc0f326e25 | -0.99704 | -51.72056 | 2024-11-30 04:40:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ab3b139f-124a-356c-a031-abdeefadd6fc | -2.5989 | -46.56969 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8251cc5f-723f-3306-a0cc-d2b39716c01e | -3.33548 | -50.49878 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96a0cd5f-dc37-3ae9-a2c4-cad22332d835 | -2.35138 | -49.01236 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 3f65dd03-656f-3e09-bbe5-e388c4e7fdc5 | -1.3304 | -51.42573 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 072804d4-931a-3248-b0ee-b68eea5268a3 | -2.17555 | -51.42053 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e5de8b8e-a660-3d47-8c6f-a27e762273eb | -2.19903 | -50.57578 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3f6ac57-4adb-3eb7-a6d3-380441d17bd3 | -2.18823 | -50.57787 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62b91282-2abd-3cf0-a3c5-6be698d0c830 | -2.88281 | -53.98737 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9c0730cb-9399-32e5-a385-9c69f4f521de | -2.24246 | -50.48177 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1b395f3d-31ea-3bed-9339-46a13d1b53c2 | -2.20788 | -48.38499 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8c783674-e732-330e-a6de-272e09a8e9a7 | -4.34134 | -43.12076 | 2024-11-30 04:40:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e6092aa-1f3b-38c4-ad3c-d3fb9f6135f1 | -2.11551 | -46.56315 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e6f85c40-3455-3fff-83b0-7bb45aea3b30 | -3.06344 | -43.02468 | 2024-11-30 04:40:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 952e52a4-41f9-34ec-adca-4f8f842bc550 | -3.21239 | -50.27066 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 60dcf863-570b-3612-929d-c369d4f5ef1c | -2.00551 | -51.16301 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 43d8008a-5d06-3578-b216-ae69abc37982 | -3.38793 | -50.32013 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4644624a-d305-34af-af7e-074976e39191 | -2.07926 | -46.52762 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4dd99b61-6034-3be4-b7e2-6573c234d6bf | -1.67662 | -52.50139 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2520b9ae-e25e-3f66-a27d-0756aea73fa9 | -2.98771 | -53.35191 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aedd0f13-70f1-3c76-8732-118a2af8d423 | -3.78577 | -58.9758 | 2024-11-30 04:40:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a8e15649-e3ef-3e70-a425-fce948dbdafd | -2.71688 | -48.65474 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fa59b7de-aa41-3c55-9f9f-27b70453a7f2 | -1.14194 | -53.78498 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dc55d6bc-e134-34ba-8af0-929d2398954a | -3.83714 | -46.65271 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d44289d-46b2-33e8-adc6-e1d0c78288f1 | -2.66932 | -49.87164 | 2024-11-30 04:40:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e3e5c939-1457-3536-a16a-fd4b9f23b69b | -2.57485 | -49.99701 | 2024-11-30 04:40:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5952ede6-56f2-3237-af2d-fe02d98b09b4 | -3.24527 | -50.66583 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 764c7c6c-a6f8-33ca-8601-c2d43ac6e4d5 | -2.1909 | -48.40702 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c843e7c-8c90-3fa0-ad18-9911b4456790 | -4.13092 | -54.89963 | 2024-11-30 04:40:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b38380ac-7568-325c-88cb-81c4e7c54c55 | -0.72271 | -51.69873 | 2024-11-30 04:40:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c922c8a7-a9c9-3641-a41c-87506ff331bf | -3.19986 | -46.57969 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c1805f2f-d2f8-3d19-833b-6e267fcadf14 | -4.17699 | -50.66277 | 2024-11-30 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bb84a026-981e-3ee5-a49b-8e67a07af9f0 | -1.62314 | -48.53653 | 2024-11-30 04:40:00 | NOAA-21 | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b04108fa-ff01-3bed-8ea5-eabf77ecfb48 | -1.23847 | -51.61574 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c08d3803-0b6c-346b-9744-5b35cf9f8021 | -1.39849 | -52.56876 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 371d6d2c-6f27-3e02-98a4-7113eb50e47a | -3.39241 | -50.31354 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 77915eef-cb67-389a-8c3b-4da5431104d7 | -1.65334 | -52.40584 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README53.md)
