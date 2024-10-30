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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0cfe46a7-03c6-3031-827b-e107b3be26c3 | -19.633699 | -56.699402 | 2024-10-30 01:43:54 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 58b3d56c-3e0c-36c3-a41d-13ce7a3c0fc1 | -19.6359 | -56.708401 | 2024-10-30 01:43:54 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 0925a5ba-ad7e-3a14-aa49-b520ebe76d21 | -19.590401 | -56.692001 | 2024-10-30 01:43:55 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e015b69f-3c10-39c4-8ae8-e77b3df4c1e7 | -19.592501 | -56.701 | 2024-10-30 01:43:55 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8e968b7e-d52d-37b4-aca8-829a1bf89c25 | -19.5947 | -56.7099 | 2024-10-30 01:43:55 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 869bf490-4e25-3b4b-aa81-11f88c50fc52 | -19.596901 | -56.7188 | 2024-10-30 01:43:55 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1d412ad9-91e9-3332-8501-9d8ab42211cb | -19.5305 | -56.573601 | 2024-10-30 01:43:55 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9715c82a-fc25-3b98-ba0a-61e6ac8d7b40 | -19.5327 | -56.582699 | 2024-10-30 01:43:55 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 2e3ca4c0-45f2-3c10-98d1-f34a9a9adb5f | -19.559 | -56.690899 | 2024-10-30 01:43:55 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ff193db6-9f70-37bf-8117-d52269e8bb66 | -19.561199 | -56.699799 | 2024-10-30 01:43:55 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 5bfd7bc2-484f-3be8-baab-40e38f7df7ab | -19.563299 | -56.708801 | 2024-10-30 01:43:55 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 443656f7-b7c9-3a61-9eef-015cf1f0d54f | -19.5208 | -56.576199 | 2024-10-30 01:43:55 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 76b9111b-4532-39cf-b0b8-0491e70d1c9f | -19.523001 | -56.5853 | 2024-10-30 01:43:55 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 978d4d7a-5078-3860-8480-cfabc9733c54 | -19.5471 | -56.684502 | 2024-10-30 01:43:55 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f8a91a97-3007-3e0e-aae9-e81e79a43887 | -19.549299 | -56.693501 | 2024-10-30 01:43:55 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f78a62ad-0499-3623-b6f9-fe00c89ab2dc | -19.5515 | -56.7024 | 2024-10-30 01:43:55 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| bbe0b1b9-64e6-3648-ae59-d300a945d59f | -19.5331 | -56.669201 | 2024-10-30 01:43:55 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 797a9cd8-702c-36e6-b4df-259351cc8f2a | -19.5352 | -56.678101 | 2024-10-30 01:43:55 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| cedf1ad9-4c29-3156-b7fa-56986e97bb86 | -19.5233 | -56.671799 | 2024-10-30 01:43:56 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 30d7cf34-2b53-327d-b947-193e0e546cc4 | -19.5254 | -56.680698 | 2024-10-30 01:43:56 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 52e98f29-96b1-34b9-8adb-8afbb705d8f6 | -19.515699 | -56.683399 | 2024-10-30 01:43:56 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d5575d6f-22c2-3cdd-a8bd-3416650bb722 | -19.5179 | -56.692402 | 2024-10-30 01:43:56 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 784e33c4-71f1-3779-8294-7d414387c774 | -19.4995 | -56.6591 | 2024-10-30 01:43:56 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e4ffcadf-dc12-321f-9631-068b90d46040 | -19.501699 | -56.668098 | 2024-10-30 01:43:56 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9b32947e-ad45-33bb-85e7-22566bd513d1 | -18.2784 | -55.953098 | 2024-10-30 01:44:13 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| af5855e9-5ed0-3222-9d42-21e94ed9cf83 | -18.280899 | -55.9631 | 2024-10-30 01:44:13 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 773c6aa3-57e6-36cd-adab-7784a751b3b9 | -18.2834 | -55.973202 | 2024-10-30 01:44:13 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 03b6846f-eb41-3268-bf41-49909e2c4f12 | -18.2687 | -55.955799 | 2024-10-30 01:44:13 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 18f1b903-7e9a-3beb-9e30-d9652460ef6c | -18.2712 | -55.965801 | 2024-10-30 01:44:13 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7fd16c3d-aa36-3142-8342-675b9a1bf988 | -18.273701 | -55.975899 | 2024-10-30 01:44:13 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 0b48e2f7-34b7-3c46-b14e-ab25cab1272e | -17.7668 | -57.507599 | 2024-10-30 01:44:27 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f2befe3a-68a8-3629-8537-6ddd0d0f34d9 | -17.763201 | -57.535702 | 2024-10-30 01:44:27 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e6bcdb26-b1bf-32c8-8acf-9e8c07969897 | -17.747299 | -57.5126 | 2024-10-30 01:44:27 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0d811f9a-27a0-371e-b2bb-4e06bdf50fb6 | -17.753401 | -57.5382 | 2024-10-30 01:44:27 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5a9b5ba1-6efd-3874-8ce0-4c859b726cf4 | -2.3906 | -48.9337 | 2024-10-30 01:45:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 21c762fe-3ccc-3d2d-adb7-0bacfbb3bfe6 | -2.833 | -49.2413 | 2024-10-30 01:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 123.6 |
| 4bbd5994-2533-3a9c-9fb9-a4b3ebb9efe5 | -2.8331 | -49.22 | 2024-10-30 01:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| d74e1399-590e-34ef-9021-88c1f24ea06b | -2.8515 | -49.2408 | 2024-10-30 01:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 4153aa86-bd99-355f-a2f3-d13b2cb102d6 | -3.0734 | -54.167 | 2024-10-30 01:45:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 934f728e-e2b1-3398-bfc1-5d2e06503c99 | -3.1028 | -51.1041 | 2024-10-30 01:45:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 37.4 |
| 71e3f33c-0d77-369b-8e44-73f02a896bdf | -3.1281 | -54.266 | 2024-10-30 01:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 32263efe-4387-32c3-968e-78ae75ebd107 | -3.1601 | -50.6021 | 2024-10-30 01:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 0f3b603b-ae2a-3903-93ff-051a42849e6d | -3.1602 | -50.5812 | 2024-10-30 01:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| b3eea6e9-638d-36c5-a121-ae13761c18a5 | -3.1786 | -50.6016 | 2024-10-30 01:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 126.6 |
| 37cc91d1-cf82-365b-b7f3-6d921a663329 | -3.1787 | -50.5807 | 2024-10-30 01:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 110.2 |
| bd9518a1-ce51-31ae-a1aa-c0c4db6643ce | -3.234 | -50.5999 | 2024-10-30 01:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 126fa4be-bf1f-3511-ad26-77c6ff870983 | -3.234 | -50.5789 | 2024-10-30 01:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| a83a08e2-7278-335a-81fa-39e5724298b5 | -3.2535 | -50.3479 | 2024-10-30 01:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 132.8 |
| a49158ff-668d-39b0-8c2c-40f7ce483743 | -3.2719 | -50.3473 | 2024-10-30 01:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 255c34b9-f612-3ed5-86e5-33f2306406ad | -3.563 | -47.4066 | 2024-10-30 01:45:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 2f5fc23e-d8ad-3d80-89b0-d03b40ad7339 | -3.5631 | -47.3847 | 2024-10-30 01:45:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 313.4 |
| ff20e862-700f-3175-9981-3aafd9a62259 | -3.5632 | -47.3629 | 2024-10-30 01:45:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 166.6 |
| 400a089d-299c-3806-99ad-ba878a637d3c | -3.5688 | -50.043 | 2024-10-30 01:45:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 20bd4fcf-91ea-3f42-bdb0-dc9298a57c5c | -3.5817 | -47.384 | 2024-10-30 01:45:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 224.8 |
| 645f3912-04ec-33a2-bbe6-e84f929d06b1 | -3.5818 | -47.3621 | 2024-10-30 01:45:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 121.9 |
| 421fff07-17f9-38a3-9a86-3ec70c190344 | -3.8037 | -51.1644 | 2024-10-30 01:45:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 3e78e4b5-2887-351d-82a0-b316eb237e9d | -3.9326 | -41.4957 | 2024-10-30 01:45:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 60.6 |
| 08602522-8c06-347e-8447-34391cccc371 | -4.2563 | -43.4368 | 2024-10-30 01:45:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 987863f4-b6d4-30df-afc8-8313bf362faa | -4.2748 | -43.4589 | 2024-10-30 01:45:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 4b87eb8b-2b07-3ec1-8c41-81c1cbf6acef | -4.2749 | -43.4357 | 2024-10-30 01:45:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 104.7 |
| bd423375-4774-3676-8259-288a44211aa4 | -4.3473 | -43.779 | 2024-10-30 01:45:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 56.8 |
| fabccb9f-8374-3f0d-b0b8-e084f860d38b | -4.2681 | -50.6669 | 2024-10-30 01:45:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| eb3c22eb-8f05-339f-ad93-b98e9290ab30 | -4.4269 | -45.8199 | 2024-10-30 01:45:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 55.6 |
| ed336acf-f382-3646-86f4-34c8c372ce4a | -4.4971 | -46.4618 | 2024-10-30 01:45:31 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 106.3 |
| 3f2a487c-8ffe-35e7-af69-d8fef2dba1fb | -4.4972 | -46.4396 | 2024-10-30 01:45:31 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 3370b970-0462-3c90-94fe-e290b3e1ca3a | -5.2306 | -47.9566 | 2024-10-30 01:45:35 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 104.1 |
| 17c30e09-6a52-36e5-aef5-3d6952e80ecd | -5.2308 | -47.9349 | 2024-10-30 01:45:35 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 93.5 |
| debd38ea-0562-3696-a635-ce04e1f1e00c | -5.9788 | -45.3621 | 2024-10-30 01:45:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 9082a8b1-2688-3fcd-8404-01d3e185357d | -6.5631 | -51.1126 | 2024-10-30 01:45:43 | GOES-16 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 08e7488f-7633-3d32-b93c-4e561b3f3a42 | -6.8593 | -59.0318 | 2024-10-30 01:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.0 |
| c1cc589c-3b6b-3621-a49b-e58078eab817 | -6.8408 | -59.0519 | 2024-10-30 01:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| f92e4127-4ad8-3752-8307-5a016b8d41a7 | -6.8592 | -59.0511 | 2024-10-30 01:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 1f30ccff-9166-37b3-a7b5-7b4635c697c6 | -10.3245 | -49.6556 | 2024-10-30 01:46:04 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 56.9 |
| c8f23bf9-c9ec-3d82-9ff8-bc8487569534 | -10.3434 | -49.6536 | 2024-10-30 01:46:04 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 02d31a88-51a0-34f7-ba7e-afcbd5567eef | -10.3437 | -49.6321 | 2024-10-30 01:46:04 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 7efd2b4b-d280-35e3-a9f9-50a31a45bb29 | -10.6984 | -44.9186 | 2024-10-30 01:46:06 | GOES-16 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 1d6a7904-829c-374a-80d4-f2f1be71c4da | -10.7171 | -44.9391 | 2024-10-30 01:46:06 | GOES-16 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 8d54c76e-1ee0-37cd-a25d-34bab421f09f | -10.7175 | -44.916 | 2024-10-30 01:46:06 | GOES-16 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 146.1 |
| c8d671f6-4665-3306-94ce-20a1d59dcc5a | -12.35 | -63.967701 | 2024-10-30 01:46:18 | METOP-C | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e5355c03-77cc-37ac-a281-e8c97f7ceb58 | -11.9338 | -63.6647 | 2024-10-30 01:46:24 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7e36057e-74b2-3909-8fdd-3b0d7baf24e3 | -18.2652 | -55.9766 | 2024-10-30 01:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.8 |
| 76ecb9f6-8e7d-32a1-bc47-0ce5582a9f10 | -10.1132 | -62.164902 | 2024-10-30 01:46:48 | METOP-C | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 88451da3-0731-396b-b11d-4b46c60057db | -10.7139 | -64.9897 | 2024-10-30 01:46:49 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1e48feed-a9d5-3802-850f-99f63cb0194a | -10.7041 | -64.991898 | 2024-10-30 01:46:49 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e53099b5-b021-3e71-b5d1-62bad9a4e519 | -19.5662 | -56.7164 | 2024-10-30 01:46:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 101.4 |
| 42b23a57-72de-3f2d-9726-c1d43e9d8a53 | -19.5862 | -56.7136 | 2024-10-30 01:46:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 139.7 |
| 207c3c26-3264-3854-be8b-912fdfac9c48 | -19.6063 | -56.7108 | 2024-10-30 01:46:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 177.9 |
| 246acfef-f211-3e8e-9807-0fcfb0b0ed9c | -19.6067 | -56.6898 | 2024-10-30 01:46:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 94.1 |
| cf8ec272-74e5-33c5-87c2-958035e4805d | -19.6264 | -56.7079 | 2024-10-30 01:46:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 111.6 |
| e75861b2-e9bc-3a97-8961-27e978826296 | -19.6268 | -56.6869 | 2024-10-30 01:46:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 82.2 |
| 35fc401a-2db2-359a-b016-876cece972a9 | -9.8333 | -62.701599 | 2024-10-30 01:46:55 | METOP-C | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0d5d6355-f3d7-3426-a6c2-36a7f32f0ece | -9.5783 | -63.123001 | 2024-10-30 01:47:00 | METOP-C | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fab75267-e2a6-3e4f-8407-a75c91d2f315 | -9.5799 | -63.129902 | 2024-10-30 01:47:00 | METOP-C | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5296439c-9e00-39f5-9ae0-0ab721c9cfa2 | -9.5105 | -64.427299 | 2024-10-30 01:47:06 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2233e05f-dc57-362a-a4bb-4e9ab6597c47 | -8.8787 | -64.225197 | 2024-10-30 01:47:16 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d3b95746-7186-3b76-89bf-03571ef169bf | -8.8803 | -64.232399 | 2024-10-30 01:47:16 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 57306ff8-f564-3047-a494-21469bd412d5 | -8.8819 | -64.239601 | 2024-10-30 01:47:16 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1beb297d-cdba-3fae-9fdb-3ed579846c70 | -8.6197 | -63.8512 | 2024-10-30 01:47:18 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 80991787-6306-3a98-8817-89ab98dd5716 | -6.8831 | -59.037201 | 2024-10-30 01:47:28 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| df04e25a-efc3-301a-b4d7-fecad69a88ff | -6.8854 | -59.0466 | 2024-10-30 01:47:28 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README22.md)
