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

## Dados Diários - Página 109

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dba41942-f1d8-36f8-a9a8-2ed0318497d2 | -2.6499 | -48.7772 | 2024-11-29 10:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 101.7 |
| a461590e-401c-37fe-b4ab-cc02263607e3 | -2.6683 | -48.7981 | 2024-11-29 10:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 356.5 |
| 0e4f47ee-0bfd-3ca2-95c0-645c30f265e4 | -2.6499 | -48.7772 | 2024-11-29 10:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 121.8 |
| b79d84f7-e227-3dc4-8849-b992810beaf7 | -2.6498 | -48.7986 | 2024-11-29 10:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 197.2 |
| 61567776-b38e-3782-ac75-81a11b0d0e73 | -2.6684 | -48.7767 | 2024-11-29 10:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 203.0 |
| 167fab82-b803-31a1-ad5c-97425484a23d | -2.6684 | -48.7767 | 2024-11-29 10:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 113.5 |
| 5609e7ac-89a6-34a2-ab3b-5ec9b7875251 | -2.6498 | -48.7986 | 2024-11-29 10:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 244.4 |
| 31a62f53-cab1-3176-8802-684b6c023b71 | -2.2299 | -53.6219 | 2024-11-29 10:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 158bd2ed-1aaa-31f8-b67f-164ab7389d22 | -2.6499 | -48.7772 | 2024-11-29 10:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 129.5 |
| 45cbbca9-eee9-3472-bf5a-14c6b3b89f90 | -2.6498 | -48.7986 | 2024-11-29 10:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 120.1 |
| c1cea468-51d3-3e3c-bad6-6f838ba22b92 | -2.6684 | -48.7767 | 2024-11-29 10:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 556543ef-e2b4-3c53-b85c-c258f7716fd8 | -2.2299 | -53.6219 | 2024-11-29 11:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 920e29b1-79b1-382a-ae43-ca73bf5ecb27 | -2.6499 | -48.7772 | 2024-11-29 11:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 558d494a-f9b3-3a50-a6d3-6a3f8250f379 | -2.6684 | -48.7767 | 2024-11-29 11:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 3d296215-1682-3354-86ab-8317e41b76cf | -2.6498 | -48.7986 | 2024-11-29 11:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 148.1 |
| 6c23aa11-da1a-39e8-978b-47e9e8487c99 | -2.6498 | -48.7986 | 2024-11-29 11:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 151.6 |
| c53e8ec3-418d-35c9-b7bb-e66110a967eb | -2.6499 | -48.7772 | 2024-11-29 11:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |
| bc689bea-51e6-3d9c-9987-1d88bb9542b4 | -2.6684 | -48.7767 | 2024-11-29 11:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 72c51bdf-d057-3bc2-915f-e0b42ca6202d | -2.2299 | -53.6219 | 2024-11-29 11:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 98.8 |
| f11ff78d-3427-3095-b4d0-df35517f96f6 | -2.6499 | -48.7772 | 2024-11-29 11:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 09a0d526-fa53-3504-a9a6-c73fb0b4bf1f | -2.6498 | -48.7986 | 2024-11-29 11:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 134.8 |
| 73717178-eea7-3931-a136-9268a3e86959 | -3.7968 | -42.2424 | 2024-11-29 11:30:00 | GOES-16 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 86.6 |
| 99e6877e-bcf9-3ce1-a381-6e7f69eef228 | -6.15595 | -36.82193 | 2024-11-29 11:34:00 | TERRA_M-M | FLORÂNIA | RIO GRANDE DO NORTE | Brasil | 2403806 | 24 | 33 | nan | nan | nan | Caatinga | 32.1 |
| 08ea03f7-1b05-36c7-bdd7-e43b4170ee5f | -8.23581 | -37.55689 | 2024-11-29 11:36:00 | TERRA_M-M | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 27.4 |
| 6963f621-3243-3213-8793-b318b59de1a3 | -2.6498 | -48.7986 | 2024-11-29 11:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 105.9 |
| 43a7c43c-f3a8-315d-9030-4856f1c84ebf | -2.6684 | -48.7767 | 2024-11-29 11:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 110.2 |
| 96f9ad1b-55e3-3d7d-aac7-1195ef0b78b7 | -1.9531 | -46.7778 | 2024-11-29 11:50:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| eb93b53a-80d0-3261-908f-dc986d224363 | -1.7108 | -47.3959 | 2024-11-29 11:50:00 | GOES-16 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| f1054a05-96a9-396f-986c-12982ad9bbf0 | -2.6498 | -48.7986 | 2024-11-29 11:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 02c4fdfe-a62d-386f-9f90-1116ba93d1c4 | -2.6684 | -48.7767 | 2024-11-29 11:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| b9f200e0-007a-30a6-a131-bdcd1cf0bd54 | -2.6683 | -48.7981 | 2024-11-29 11:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 130.8 |
| 0938dd7b-d0d9-35c4-bb53-d78195e3b48f | -2.6498 | -48.7986 | 2024-11-29 12:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 71df168f-c06a-3691-877b-c2909c4891ab | -3.4233 | -42.1901 | 2024-11-29 12:00:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 84.3 |
| 97ec2cc0-98d0-3fe8-83f3-dbdc193afbce | -6.9422 | -42.8362 | 2024-11-29 12:00:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 97.8 |
| 4c92fd26-b119-37d0-a26e-777ff842fa70 | -2.6683 | -48.7981 | 2024-11-29 12:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 107.2 |
| 575311b1-3472-384d-b097-a8f6a1df3f57 | -2.6684 | -48.7767 | 2024-11-29 12:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| f63c2e9c-504b-3ceb-befd-296e2f26b5af | -3.4046 | -42.191 | 2024-11-29 12:00:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 100.5 |
| fe475b57-4258-3140-9320-5157acbd39cc | -3.34 | -42.05 | 2024-11-29 12:00:00 | MSG-03 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 242e1c44-13e6-35be-8efd-5ee36c6e35ff | -3.34 | -42.09 | 2024-11-29 12:00:00 | MSG-03 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c2d3e32f-a71a-3e74-acbf-6e4f89d76664 | -3.4046 | -42.191 | 2024-11-29 12:10:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 107.1 |
| a5b5568a-f8b4-3efb-92ac-68ae22e50c66 | -6.9422 | -42.8362 | 2024-11-29 12:10:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 119.7 |
| 79a0bd58-969a-3642-9a3f-5e36ab03bf9b | -2.6498 | -48.7986 | 2024-11-29 12:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| ef7a9f63-6670-3c3b-80da-d659f309bebd | -5.4546 | -43.2659 | 2024-11-29 12:10:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 918fdbf2-b7fc-39f5-9bec-7c709309ec2d | -3.5012 | -41.6385 | 2024-11-29 12:10:00 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 192.5 |
| 0822b818-ae0e-3ebe-80e7-4cec203b8d84 | -2.6684 | -48.7767 | 2024-11-29 12:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 6cfa71d4-d754-393d-a1f2-0f945b94a230 | -6.9424 | -42.8126 | 2024-11-29 12:10:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 83.4 |
| bf3a1ade-57e7-324f-a2ca-ca2797decc7c | -2.6683 | -48.7981 | 2024-11-29 12:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 165.3 |
| 0c9d7c9a-c1e3-3a19-b554-b820e6f6dcef | -6.9424 | -42.8126 | 2024-11-29 12:20:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 85.0 |
| 9778cf1b-eec2-3318-8ec6-42c29b1de231 | -2.9844 | -53.2819 | 2024-11-29 12:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| bf7a4d8b-e689-37d3-a1c3-bb185d3aa25d | -2.6499 | -48.7772 | 2024-11-29 12:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 08239b18-81e9-3dd7-b40e-2496bab82e20 | -4.1761 | -44.2716 | 2024-11-29 12:20:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 164fad7f-479e-3ab7-b4ae-bece8b0ff2dd | -2.6684 | -48.7767 | 2024-11-29 12:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| fd7d6270-78b8-3ffc-a66f-449706531b90 | -2.6498 | -48.7986 | 2024-11-29 12:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 106.4 |
| 7f9cf50d-8aaa-3bd7-9dbe-269be6caea09 | -2.6683 | -48.7981 | 2024-11-29 12:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 2b1631a2-3890-3288-a48a-a5ab1fd543f2 | -6.9422 | -42.8362 | 2024-11-29 12:20:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 133.0 |
| 316b7d24-51b2-31d5-9f84-9fe5a69bf2ea | -3.4233 | -42.1901 | 2024-11-29 12:20:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 76.3 |
| c59a54f6-bcb5-337f-8466-3d66d32a27f5 | -4.1761 | -44.2716 | 2024-11-29 12:30:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 388d40e1-73a0-3688-8288-eef833545f9c | 1.4552 | -55.9053 | 2024-11-29 12:30:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 125e253c-0d68-383a-920a-f52a36f9424e | -1.7693 | -46.252 | 2024-11-29 12:30:00 | GOES-16 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 13479940-0450-3d89-9242-e44627be63f5 | -2.6683 | -48.7981 | 2024-11-29 12:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 126.4 |
| f26b2c0d-d005-3104-866b-647f475785f2 | -6.9424 | -42.8126 | 2024-11-29 12:30:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 78.9 |
| a0939395-a972-300c-bbab-a51afd9b9dd6 | -2.3059 | -46.5488 | 2024-11-29 12:30:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| ad00825d-703b-3011-9c4f-a10359568cab | -2.6498 | -48.7986 | 2024-11-29 12:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 130.0 |
| 8dcd090e-df90-3881-8731-f7154b57de36 | -2.6684 | -48.7767 | 2024-11-29 12:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| b81dd596-ca7b-3a30-ad20-2316b602097a | -6.9422 | -42.8362 | 2024-11-29 12:30:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 129.9 |
| 44048d6b-8acc-3249-8238-5cfedac884b8 | -5.0399 | -43.6205 | 2024-11-29 12:30:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 980bc81e-33ea-3ae2-b35f-2ce428de74de | -2.6499 | -48.7772 | 2024-11-29 12:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 74fa7136-21b3-3924-a095-026744c02eaf | -2.8611 | -46.8186 | 2024-11-29 12:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 2a6edd92-1ac8-3648-866a-c60e11a986aa | -5.4546 | -43.2659 | 2024-11-29 12:40:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| cc32eab1-9ed6-3143-a449-12b32d849619 | -2.9844 | -53.2819 | 2024-11-29 12:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| f816be62-1b86-3fea-90c0-b895e4c19978 | -5.0399 | -43.6205 | 2024-11-29 12:40:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 142.1 |
| bac4a701-77c0-37b2-bb79-4d10298412ce | -6.9422 | -42.8362 | 2024-11-29 12:40:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 149.0 |
| 37465c6e-a472-31b1-bad5-f99916fb93fc | -2.6684 | -48.7767 | 2024-11-29 12:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 38eae1ef-430f-3833-93ee-9512c96f384c | -6.9424 | -42.8126 | 2024-11-29 12:40:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 102.8 |
| 99fdfce8-d3bc-3745-94ba-a6856b3f1303 | -2.6498 | -48.7986 | 2024-11-29 12:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 109.7 |
| 79718526-f4a8-31e3-a308-7c98f4bf14bb | -2.2298 | -53.6421 | 2024-11-29 12:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 117.9 |
| 2bd67193-e810-32b4-b331-e6fbaa67104e | -2.6683 | -48.7981 | 2024-11-29 12:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 116.1 |
| f508d510-a36f-3b48-8847-742770f8b40c | -5.4546 | -43.2659 | 2024-11-29 12:50:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 543d502e-c127-3a30-bc55-7d97d5a6f579 | -3.7601 | -42.1257 | 2024-11-29 12:50:00 | GOES-16 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 90.6 |
| 1be13975-8711-3dcc-bc4f-854676ecb737 | -2.6683 | -48.7981 | 2024-11-29 12:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 106.3 |
| 0b124764-21b3-3859-8544-e86453c4b8e1 | -2.6498 | -48.7986 | 2024-11-29 12:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 142.5 |
| cb2d0abd-72dd-3199-b2a8-e8fbb30b3ef9 | -2.2298 | -53.6421 | 2024-11-29 12:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 130.2 |
| 682df6f8-8ba7-3067-aeb6-1ae8fbc0de77 | -6.9424 | -42.8126 | 2024-11-29 12:50:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 98.5 |
| b232e77a-13fc-3dc2-889d-93c1e4321d06 | -2.2299 | -53.6219 | 2024-11-29 12:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 227.5 |
| 55ca3b3a-1048-375d-a044-d1051dbe583d | -2.6684 | -48.7767 | 2024-11-29 12:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 5a050162-53f2-386b-b754-923dbb493f0b | -6.9613 | -42.8108 | 2024-11-29 12:50:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 80.0 |
| ec885162-6fa0-3154-9455-5fe0fc06a30e | -4.1761 | -44.2716 | 2024-11-29 12:50:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 125.7 |
| 79c842f3-e21d-333a-af98-4c37536a626a | -2.6499 | -48.7772 | 2024-11-29 12:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 102.1 |
| b2fcc3c3-ae56-3851-b4fb-8ad25bcd77e4 | -5.0586 | -43.6193 | 2024-11-29 12:50:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 43fb3ab6-7a98-300b-aa50-e2e22c423a6b | -5.0399 | -43.6205 | 2024-11-29 12:50:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 147.3 |
| b98b4ba2-5d4b-3cda-957a-ea4b7cc84293 | -2.9844 | -53.2819 | 2024-11-29 12:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 60b3df9e-eab5-3af8-97a3-9326b9c1cb02 | -6.9422 | -42.8362 | 2024-11-29 12:50:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 140.0 |
| 2d75b736-bc44-316c-954b-99d29572c0bf | -2.2298 | -53.6421 | 2024-11-29 13:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| be0b13d3-a38c-34a9-bd6f-f782a641a785 | -4.1761 | -44.2716 | 2024-11-29 13:00:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 32d17737-f350-30dd-89be-22184de7c2c0 | -2.9844 | -53.3022 | 2024-11-29 13:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 11ca67d7-c1d7-3086-9706-fc96f2ec409f | -3.7601 | -42.1257 | 2024-11-29 13:00:00 | GOES-16 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 331.5 |
| 6a15e0c1-7a2f-30a3-bd5f-93915788e8b6 | 1.4552 | -55.925 | 2024-11-29 13:00:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 652c4bc8-d3cc-34e9-9858-97e11c052a89 | -2.3059 | -46.5488 | 2024-11-29 13:00:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| d0a8a05e-ff2d-3bb7-8225-62946ad0619d | -1.6732 | -47.6577 | 2024-11-29 13:00:00 | GOES-16 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 6e4c9d27-ea48-35cf-859b-ad38f44c0b2c | -2.6684 | -48.7767 | 2024-11-29 13:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 111.2 |


[Clique aqui para ver as próximas entradas](README110.md)
