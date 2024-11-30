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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b63fb949-0fd1-3d75-9b42-f5a92d593692 | -6.51344 | -47.79782 | 2024-11-30 04:40:00 | NOAA-21 | SANTA TEREZINHA DO TOCANTINS | TOCANTINS | Brasil | 1720002 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e7ff2c26-f911-317a-9a15-747904111760 | -3.32837 | -49.61769 | 2024-11-30 04:40:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e687fdf2-a9d8-36f4-ae68-d0ef90567894 | -2.86493 | -53.99555 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6f7be46f-6987-3cb2-8a59-925774160260 | -1.60033 | -52.29424 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3dbb3c85-217c-3e00-ba93-fe0625e60029 | -3.12838 | -46.05106 | 2024-11-30 04:40:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 0637b070-74a1-33e9-b59e-9ced538edbc3 | -2.23348 | -53.68927 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b9fc0fb3-ad6d-376f-9a05-f5e6c0926ae4 | -3.32767 | -50.252 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 11cf8cfc-fb6b-3c8f-b3fc-b54e3b653859 | -2.74593 | -46.11069 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e0c80f1d-4460-39e5-8fb3-5954bcbc6580 | -2.30521 | -46.54192 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 98998e79-e4bd-3c66-95b2-62ae3b1f60ce | -2.60236 | -46.57024 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f49b7149-0f99-36e2-8ed8-97cacfa3442f | -3.91138 | -47.20138 | 2024-11-30 04:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4dd1e8e7-e7db-346f-b461-f4038a3988b0 | -2.93613 | -48.60126 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7bdb7642-b9ae-3ad7-8f8b-568dfbd56236 | -3.95999 | -48.09557 | 2024-11-30 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e68845a0-715f-3cd1-87cf-1adab0e5201e | -2.30694 | -47.28289 | 2024-11-30 04:40:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7dc31918-2620-34ea-b7bd-d0bb357f2627 | -2.84731 | -46.6836 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a183b43f-6d1e-3139-a67c-b0edd631ec82 | -3.06672 | -50.57166 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 98dccad9-26df-3d31-ad81-b69b3929c84a | -2.5995 | -51.94908 | 2024-11-30 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 75f0b71c-ac6e-379d-af46-21bc8adcfb40 | -1.35698 | -54.97261 | 2024-11-30 04:40:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9275a1e9-f76b-3eac-8a92-1a7b23818f5d | -1.23912 | -51.61163 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1d73824f-8c65-35a3-a04d-160e14018641 | -3.67687 | -50.17266 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ca296393-ffae-3c13-aba2-919433556ab6 | -3.2305 | -53.39106 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2921c91b-d5d5-3adb-951e-bef83c230f01 | -3.31329 | -54.09255 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a446ce69-997b-33b0-841f-a0ee3210ea14 | -4.08138 | -46.82661 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 29408e31-0272-3d03-924d-ead3efe82d03 | -2.36603 | -50.43352 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| df4717f0-af4c-37eb-8388-06448e953000 | -2.66885 | -46.54462 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac3b34ba-c683-3dcb-8bff-8e6db48a7721 | -2.70286 | -48.59278 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d2ba621-f406-3b9c-aead-82f4d8c43308 | -4.11425 | -48.52687 | 2024-11-30 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e92c378f-d1b2-3074-a6dd-15d5ca5f290a | -3.40737 | -50.65792 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e74b3d4e-11f3-3125-85a1-db4ac486b9b7 | -4.14395 | -48.22481 | 2024-11-30 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 78803204-aaa5-3abb-b0eb-1498a70379ea | -1.69535 | -52.43063 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 39c011df-099c-3562-9d48-f27b96d7ca19 | -3.07803 | -49.50092 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| de8038ea-938c-36f6-aec0-f6eb133c86f6 | -1.685 | -46.78405 | 2024-11-30 04:40:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| b62d9387-dd03-320b-bc27-7ea43093dacb | -3.33994 | -50.51421 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb2147f7-bd30-3ad8-867c-7ca6638bbe41 | -1.23141 | -51.80193 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 198ebfe7-4938-3967-adc4-fb129a0fae94 | -3.85398 | -46.65943 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8bdf54f9-5b4f-3170-949a-d7f871db666c | -4.08609 | -47.02522 | 2024-11-30 04:40:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 59d39a0d-dd7d-315c-b0a3-2e6b1a82da04 | -1.92218 | -47.90536 | 2024-11-30 04:40:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2f321d48-7d9f-3b39-aa3e-483f0d1f1d38 | -3.8466 | -46.51894 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 4635dd51-3b7c-3a23-95b8-5bba882fb31d | -3.83122 | -46.56542 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9f17c92a-f7cc-3a2d-8008-0f016b6b411d | -2.13119 | -46.41431 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2917cdb4-9771-3317-b863-602b801af0b3 | -1.04286 | -51.73617 | 2024-11-30 04:40:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5d44e3d7-6b11-36e7-b6a7-f2663a762cb5 | -2.72572 | -48.66313 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c7781a3e-18b4-3457-9a7b-d15042daa90a | -2.3626 | -48.55022 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b7969f98-1e00-32b0-9797-21c9e1033e2c | -3.91583 | -50.10234 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8d9d57b8-9b88-3026-a8bf-fad971441e97 | -2.64252 | -46.24128 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aba157c8-4d57-32f9-9d21-32924995e9e7 | -2.83931 | -46.85133 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 164b0340-ba54-3b6f-a09d-c365b9a14bde | -4.08899 | -47.02498 | 2024-11-30 04:40:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b5ddf65a-2003-3ffa-9ed4-966b67189578 | -1.13756 | -48.35495 | 2024-11-30 04:40:00 | NOAA-21 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 02c0381a-e1b4-3865-a3df-0b3936dfbe87 | -3.90144 | -49.82504 | 2024-11-30 04:40:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7f9108e1-026d-305d-9810-4af69105dfcc | -6.91311 | -43.53065 | 2024-11-30 04:40:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a59cd1d5-2d52-3094-b6c6-015c895b9199 | -2.118 | -45.78679 | 2024-11-30 04:40:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76227497-243f-3b4b-b291-5cf074f1be49 | -2.6888 | -46.15182 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 113f6a07-a7f1-315f-96a5-f67639a4e518 | -1.57276 | -51.21797 | 2024-11-30 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9755f8f-bde7-3152-8e65-b5b1f03bc0f5 | -2.09685 | -48.3994 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 837a5ab1-501d-3c1b-9a6b-ceabc81e987b | -1.8877 | -48.65184 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| faadd6be-7fef-3098-9342-6bb4133e239c | -4.85768 | -41.30694 | 2024-11-30 04:40:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 94a9048b-e9ce-3cf8-8267-9372092a3afe | -3.74974 | -45.26931 | 2024-11-30 04:40:00 | NOAA-21 | BELA VISTA DO MARANHÃO | MARANHÃO | Brasil | 2101772 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 19480af8-d581-3a0c-87b6-4117c6c4efd7 | -1.15463 | -51.69292 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ca767512-8975-3133-bbf3-26495c3e90c4 | -1.56253 | -51.26068 | 2024-11-30 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f605ed17-c108-3d4b-b8c1-4dcd804ae978 | -3.64061 | -54.44315 | 2024-11-30 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 897a9a8a-c2a6-3ae0-8bcf-3db685fd79a0 | -4.1159 | -46.87023 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 915b55ea-9a85-3c81-9cce-b94449d8ded4 | -5.1258 | -45.15426 | 2024-11-30 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eeae78ec-deba-39fd-936d-732ef0b3a81e | -3.20209 | -51.25342 | 2024-11-30 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 574fd70f-3072-3d0f-8aef-6242a1202b69 | -6.00476 | -57.83593 | 2024-11-30 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bae72986-0994-3507-a082-4e2f971bd6e1 | -2.80786 | -53.04943 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 0dd844c5-c3dd-30c1-a3bd-0ef68c751185 | -2.19877 | -53.75201 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d3dbbf1e-b154-336d-a1fc-b83a279b16f5 | -2.89444 | -51.57606 | 2024-11-30 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cddef3f0-18ea-35a1-a65f-272d5d6bf94b | -2.91632 | -53.07473 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7aa96e25-7e24-3ecd-a774-1dc083bd19ac | -3.1749 | -53.63492 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 12d5a9d4-6bfd-3de5-ad18-d82dc711b155 | -1.99163 | -53.28782 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 556c306d-2141-3316-95cb-b3e12bd5e3c0 | -3.82576 | -46.60057 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 02a5e804-583f-37aa-89c8-e2834eacb504 | -4.08264 | -47.02469 | 2024-11-30 04:40:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fda9652e-bab2-34d3-a691-7efdb78f0175 | -2.49869 | -46.23574 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 96a529c4-a7cf-3616-ae75-7803253dc606 | -2.71757 | -49.80378 | 2024-11-30 04:40:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7173fde2-3d21-3542-92d5-1c2a7b5ab813 | -2.40114 | -50.38703 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 676abc5e-fdbc-34ec-9b8d-8312ed7b2e0d | -3.07068 | -50.56852 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e9d83ed-09eb-3d93-ab34-3a576084aec5 | -1.35247 | -54.62803 | 2024-11-30 04:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 96fab1fe-64b0-3d81-a419-151dbea0411a | -2.35983 | -48.54628 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d0ae95e-1094-3039-a6a5-2252759d4f55 | -5.38964 | -44.82685 | 2024-11-30 04:40:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9cddc17b-8826-378c-a897-222ef72e337b | -2.71974 | -48.67979 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 172e909e-95b2-3388-a5d1-03a40d35925c | -3.23956 | -53.63434 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 745a8937-4b35-324d-a5db-cc239da0e5af | -2.29757 | -50.6857 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6237bceb-7d54-36c1-aac6-ab4e76b01d33 | -2.74302 | -54.13433 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 087a0200-f312-35de-9717-faece0842e45 | -2.60571 | -54.35657 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8a1150e7-5ea5-3c1b-8417-4e38994cc194 | -3.76527 | -50.17244 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 26fbeb6a-3529-3e59-a893-3f5335353c3c | -2.9503 | -49.4486 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b6b2afb6-ede0-347f-95ab-cb70ee814ff0 | -3.10621 | -50.31988 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8feeae1-af1c-3e31-af31-b4d837d6bb38 | -1.64186 | -53.86766 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 48e8804f-d32c-30b3-b8c4-d15622404012 | -2.71938 | -48.59532 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e3ee8767-f9a4-32d5-821b-99776cc7265d | -3.40285 | -50.66466 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 441464aa-a8bf-32de-9b76-8b55cb48825a | -2.84613 | -54.08814 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5b88b0af-a885-3d7f-b518-d6e4d773ab92 | -2.9576 | -48.33279 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e7bf4bd0-3bc3-3b1c-b8a3-5aa531c2b06e | -2.66987 | -49.86813 | 2024-11-30 04:40:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 941c75ce-15ba-3d0c-abb4-ad4c487644f0 | -2.55022 | -47.97788 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eda1544b-4871-340f-8e25-1890bdc3d0d8 | -3.26024 | -48.76822 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2a11ff38-dec3-3dd0-82a4-46131469a730 | -1.11806 | -53.21928 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 60b5cb84-06c1-3db7-9211-0df05d2af68e | -1.69795 | -52.63796 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 036ff8d7-d208-3122-9439-a7228e88f7cc | -2.19934 | -53.74846 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 684afa91-5ff3-3d5f-bb4f-d88fe40eeff2 | -4.00869 | -50.35185 | 2024-11-30 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ea24fdd8-0b6e-36fa-b897-f9bb7e2ee2ba | -1.26397 | -51.75975 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |


[Clique aqui para ver as próximas entradas](README64.md)
