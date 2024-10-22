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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 91510b72-d052-3d29-a3a7-872bd514d3ee | -4.4169 | -42.8937 | 2024-10-22 01:12:23 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f85d7ccc-a510-3fa5-8241-90718aa9b94d | -4.4073 | -42.896099 | 2024-10-22 01:12:23 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2efc6601-df0b-305a-9ae5-d93011efef1d | -4.5065 | -45.800301 | 2024-10-22 01:12:33 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| eb285a9b-c04a-3b86-b5b2-d7a091a9f6ec | -7.771 | -61.358002 | 2024-10-22 01:12:38 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2b36860f-0ea4-3e31-8520-91ec761f0800 | -7.7741 | -61.372398 | 2024-10-22 01:12:38 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ab28f9e8-9553-38e5-b07b-b1d0b696b80b | -7.7613 | -61.360001 | 2024-10-22 01:12:38 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 80e456ca-43c2-3775-ab78-d08d75946fb6 | -3.9652 | -46.016399 | 2024-10-22 01:12:43 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b6d7f827-2f5b-3a59-8298-4dfe39e7276a | -3.9507 | -45.998798 | 2024-10-22 01:12:43 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 623a07b8-b9af-3cbe-8fe4-b29fdc20186b | -3.9556 | -46.018799 | 2024-10-22 01:12:43 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a5bf8cec-595e-344a-a8c0-78aee4de2318 | -3.9605 | -46.0387 | 2024-10-22 01:12:43 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a7a4df4b-2bc2-3a17-9f5b-6cdfbf47d10b | -3.9459 | -46.021099 | 2024-10-22 01:12:43 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3de470b7-2f79-3031-a546-6b55155fad41 | -3.2457 | -46.980099 | 2024-10-22 01:12:58 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e841bf2d-f944-3299-80b9-413c6b5f4a29 | -2.807 | -45.459801 | 2024-10-22 01:12:59 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 98d66836-3a2f-3990-a843-06761d1fd987 | -2.8125 | -45.482498 | 2024-10-22 01:12:59 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| efc4d63b-103c-3212-91ae-9b0bc57d288e | -2.7973 | -45.462101 | 2024-10-22 01:13:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 73911ead-b99d-3e81-95c5-d872800b5c32 | -2.5167 | -45.992901 | 2024-10-22 01:13:06 | METOP-C | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 49966b96-7584-3a22-934d-d8e3fa6bc552 | -2.5071 | -45.995201 | 2024-10-22 01:13:06 | METOP-C | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 039b6dbd-b398-35e9-b11d-4b25bd0de366 | -3.5923 | -51.428799 | 2024-10-22 01:13:10 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b87afdf3-d601-31fd-a445-d506b1ea2533 | -3.461 | -51.220402 | 2024-10-22 01:13:11 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17584763-a5f9-3a72-ae51-a09fe2583ca2 | -3.5306 | -51.5177 | 2024-10-22 01:13:11 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86d5a77b-352c-3781-8418-48331354d2aa | -3.5327 | -51.526501 | 2024-10-22 01:13:11 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bacb1335-9585-34e5-9eec-822ae86b4b8a | -2.7115 | -49.304901 | 2024-10-22 01:13:16 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ef345ea-8380-3c1e-9f2c-e4f8fa19d362 | -2.7144 | -49.317299 | 2024-10-22 01:13:16 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a5a95d6-fcdb-337b-8d86-9a8c6512113b | -2.7174 | -49.3297 | 2024-10-22 01:13:16 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d562936d-23d8-37e7-bce4-f51d438fcf86 | -2.7017 | -49.307201 | 2024-10-22 01:13:16 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b303657f-4a4f-3957-afdc-625be500d3af | -2.7047 | -49.319599 | 2024-10-22 01:13:16 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8fe81b3-78cd-313e-963e-c1b5563948b7 | -2.7076 | -49.331902 | 2024-10-22 01:13:16 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0acc8692-bc15-38f7-8746-54930874638a | -3.0373 | -51.259399 | 2024-10-22 01:13:18 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 938314ba-85ee-3b24-9c69-30cbba4f1cac | -3.5546 | -53.481201 | 2024-10-22 01:13:18 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69390e95-a706-36c3-8ebb-025fe80390e1 | -3.0253 | -51.2523 | 2024-10-22 01:13:18 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79e1db56-c8b2-3b18-b8ad-955be24eadfd | -3.0275 | -51.2616 | 2024-10-22 01:13:18 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0168bde8-56c6-3d61-8262-63cf61b0645c | -3.0297 | -51.270802 | 2024-10-22 01:13:18 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46a5aafc-c32a-31fe-8766-eef95254d5a3 | -3.5409 | -53.779301 | 2024-10-22 01:13:19 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82a1cc9c-29e1-325d-b7de-33b1e6c9fccc | -3.5426 | -53.786499 | 2024-10-22 01:13:19 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84602f74-c081-3ee9-a021-c6eb388618b6 | -3.5834 | -53.963501 | 2024-10-22 01:13:19 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 841976b8-141b-3007-b2d9-ef6238f63b23 | -3.5851 | -53.970501 | 2024-10-22 01:13:19 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aaf43872-7441-3368-81df-554721845060 | -2.4403 | -49.114201 | 2024-10-22 01:13:20 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c90484e7-0dbe-3293-b578-184bd7522ca5 | -2.4275 | -49.1036 | 2024-10-22 01:13:20 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76052338-f7e7-3ad1-986e-91b887085159 | -2.4306 | -49.116501 | 2024-10-22 01:13:20 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65182b28-6a60-304e-b061-90a60ac5db4c | -2.4336 | -49.129398 | 2024-10-22 01:13:20 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a07c8ef-2c78-3a65-b4ec-8131a1a70561 | -3.4543 | -54.029701 | 2024-10-22 01:13:22 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bca980df-f4e7-35c3-a764-a3c3a2be2c97 | -2.7601 | -51.352001 | 2024-10-22 01:13:23 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dcc7e595-37a2-3d32-ac0d-8517b12ed45e | -2.7622 | -51.361198 | 2024-10-22 01:13:23 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 267bae24-e440-3d2d-a55f-51f856270236 | -2.7427 | -51.3657 | 2024-10-22 01:13:23 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b13011f3-0787-34f2-8fc4-718172b50e8b | -3.217 | -53.716999 | 2024-10-22 01:13:24 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 00802010-85bb-3787-beeb-50f7e9f374fa | -3.0581 | -53.119202 | 2024-10-22 01:13:25 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56478638-3bdb-30bf-89c4-906479c35c79 | -3.0598 | -53.126801 | 2024-10-22 01:13:25 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28ede178-9e6a-3354-ad17-c314f89d53d9 | -3.0615 | -53.1343 | 2024-10-22 01:13:25 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0b347be-70ca-38fe-8686-a5392dcba161 | -3.3975 | -54.633999 | 2024-10-22 01:13:25 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58aad452-049d-3ff8-acdb-b0e873424204 | -3.3991 | -54.6408 | 2024-10-22 01:13:25 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4690ee24-ea23-36ac-a757-e698b154bee9 | -2.3667 | -50.2873 | 2024-10-22 01:13:25 | METOP-C | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ab170bd-74db-37c9-9a28-5bc83745ad0e | -2.3692 | -50.2981 | 2024-10-22 01:13:25 | METOP-C | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5fed7064-9c0d-3e3e-b1ce-2a23148bfac6 | -3.0138 | -53.239799 | 2024-10-22 01:13:26 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d2c1a2d-2b6e-3ee1-b617-dbca615d355a | -3.0155 | -53.2472 | 2024-10-22 01:13:26 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29784acc-1683-3708-aae7-13be0c5b2b5c | -3.0172 | -53.2547 | 2024-10-22 01:13:26 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fbda3431-5341-3cf4-95b8-f3004c128783 | -1.9269 | -48.6791 | 2024-10-22 01:13:26 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45efa1ed-bb59-37a3-9c32-6c02dd78cbd6 | -1.9302 | -48.693199 | 2024-10-22 01:13:26 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f38c805-44c5-39a1-bb2d-66ecffd207f3 | -3.0 | -53.893799 | 2024-10-22 01:13:29 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5f50007-0272-342d-bb92-4efb58038e67 | -3.0016 | -53.900902 | 2024-10-22 01:13:29 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 38a28d37-af94-32ab-8dfd-0d2ee1e23e31 | -3.0489 | -54.150501 | 2024-10-22 01:13:29 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90fe2517-3845-34eb-8c37-7f6d56d94727 | -3.0506 | -54.157501 | 2024-10-22 01:13:29 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20ed1629-736b-3c89-9ee0-6c2bbf3b92cf | -3.0522 | -54.164501 | 2024-10-22 01:13:29 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8710ccb-e8f6-3928-be59-5e5fc12577db | -3.0538 | -54.171501 | 2024-10-22 01:13:29 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 684de628-e901-3291-8d70-1739b1601721 | -3.0554 | -54.178501 | 2024-10-22 01:13:29 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 727e2ffc-e02d-35ab-8718-8d002520835a | -3.0408 | -54.159698 | 2024-10-22 01:13:29 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8feed704-dc70-3e0c-8d5e-5692beba7ee9 | -3.0424 | -54.166698 | 2024-10-22 01:13:29 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed85aea9-5ca2-3ed4-a5de-c2643c69bee6 | -3.044 | -54.173698 | 2024-10-22 01:13:29 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27d03cd8-6c17-302c-bcd5-1f21fcab24e5 | -3.0456 | -54.180698 | 2024-10-22 01:13:29 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cfa3d879-3a37-3beb-ba2e-ea14a39ac11f | -3.0472 | -54.187698 | 2024-10-22 01:13:29 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 084987bc-c710-386e-8de7-5853d7348592 | -3.0325 | -54.1689 | 2024-10-22 01:13:29 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0eae6962-3fb3-3c14-9e2b-fd15c4120a07 | -3.0341 | -54.1759 | 2024-10-22 01:13:29 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9becaac3-cc4f-383b-ac8d-852182b9dfb9 | -3.0357 | -54.182899 | 2024-10-22 01:13:29 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5c1774a-910d-368b-9fc7-b9303369d354 | -1.4246 | -47.766201 | 2024-10-22 01:13:31 | METOP-C | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3ce77f2-e44c-3d49-8f44-f0bf83b8b092 | -1.4285 | -47.782799 | 2024-10-22 01:13:31 | METOP-C | INHANGAPI | PARÁ | Brasil | 1503408 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dbad980b-b8f0-3c8e-8435-7a5bc9f4e3d7 | -2.8158 | -54.481701 | 2024-10-22 01:13:34 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc2d469d-59c5-3353-b085-33f5f0d63af3 | -2.3592 | -53.932999 | 2024-10-22 01:13:39 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6f3a5a1-a8ec-3419-8360-92a50a6f46dc | -2.3608 | -53.940102 | 2024-10-22 01:13:39 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54c012dc-dd34-358a-bf6b-752aeec13f0b | -2.2406 | -53.731899 | 2024-10-22 01:13:40 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 380958c5-2a5a-3318-94bd-10a9755ebe51 | -2.2423 | -53.739201 | 2024-10-22 01:13:40 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e80a37b-5a36-3fb1-8fef-ec58d4aba0d7 | -2.0419 | -53.2295 | 2024-10-22 01:13:42 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6201de94-8249-3d51-98cb-d6a9b6d9443d | -2.0437 | -53.237099 | 2024-10-22 01:13:42 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc9b2554-12b9-3753-9e19-2f0c3c739e03 | -2.0321 | -53.231701 | 2024-10-22 01:13:42 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3475fdb8-1e52-37f5-acd1-3e482c5454f8 | -2.0339 | -53.2393 | 2024-10-22 01:13:42 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b927c31-7887-3aa7-b133-1a9b1f049a4c | -2.2856 | -54.329498 | 2024-10-22 01:13:42 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a65cd460-4d6f-3842-82c4-04b15bcf4873 | -1.4086 | -52.319401 | 2024-10-22 01:13:48 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc6f07e0-15f1-32e7-9331-cced995289aa | -2.7354 | -58.142601 | 2024-10-22 01:13:49 | METOP-C | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a99e3568-e6ff-3228-84fd-64ac1f05badd | -1.3988 | -52.321602 | 2024-10-22 01:13:49 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b52a8a2c-a5ac-3ccf-aefa-efd15b361f2a | -1.8736 | -55.678101 | 2024-10-22 01:13:53 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95f2c8a2-b77c-35c3-8a2d-d0b6639f6928 | -1.6522 | -55.118801 | 2024-10-22 01:13:55 | METOP-C | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb72634c-fa88-3d9f-a6de-091f7d9abdc6 | -1.1902 | -53.381302 | 2024-10-22 01:13:56 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47b77350-c6c9-371e-a7ea-a1564c1b088d | -1.1236 | -53.673599 | 2024-10-22 01:13:58 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4817538-ea9d-36a5-a028-fa2dc0d7fab9 | -1.1219 | -53.6661 | 2024-10-22 01:13:58 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62c85a67-8642-3c15-9da1-cc39a10c96ca | -1.1201 | -53.658699 | 2024-10-22 01:13:58 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 269cfda1-4187-3704-8972-e1c0d34db22c | -1.1317 | -53.663898 | 2024-10-22 01:13:58 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f5739962-9f72-38fb-8f35-b66d34f80fad | 1.8882 | -50.502399 | 2024-10-22 01:14:35 | METOP-C | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 8c0e61e5-a73c-314a-a537-98b581f4ad6f | 1.891 | -50.490299 | 2024-10-22 01:14:35 | METOP-C | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 7f359f6a-5e9f-313f-a0eb-35e00d534119 | -1.1834 | -53.6569 | 2024-10-22 01:15:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 8ddff2d0-f392-3ac7-b5d6-f07114aab9e3 | -2.4824 | -49.1233 | 2024-10-22 01:15:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 125.2 |
| 9ccf7316-998d-3abc-a12f-0cd61c042c4b | -2.4824 | -49.102 | 2024-10-22 01:15:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 103.8 |
| 5936e7f3-bdae-3a1b-898c-af3eac2bc012 | -2.7588 | -49.3285 | 2024-10-22 01:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |


[Clique aqui para ver as próximas entradas](README9.md)
