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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f596f119-84d8-3327-9971-8454b1ffc033 | -2.36749 | -53.65429 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21d7a83c-b9a5-3f05-9832-abb19f03fac2 | -3.29358 | -54.72377 | 2024-11-24 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ce3add9d-0b33-3a02-abc5-82e24a7fa024 | -4.38428 | -55.07309 | 2024-11-24 04:53:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e54b5040-5119-350a-9bdc-4a9a2023e8c8 | -4.95226 | -48.64406 | 2024-11-24 04:53:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 66ae06b0-db8c-3d84-a699-e00a81280ba5 | -2.24776 | -46.86768 | 2024-11-24 04:53:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c91bd50d-aafb-31b0-9110-75854b1097b2 | -2.11088 | -45.89691 | 2024-11-24 04:53:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec9ca247-5b1f-31e4-88db-07b1d722d15d | -2.60083 | -54.02156 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2c01f406-5c01-3c35-8e6b-42f31a626452 | -3.57647 | -54.51437 | 2024-11-24 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 027e8c39-eeb2-3c9b-a65b-e7d3fcf9d326 | -2.15347 | -50.45438 | 2024-11-24 04:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2acc0d25-4167-30e5-b65b-a241bb6750ee | -1.68095 | -48.62701 | 2024-11-24 04:53:00 | NOAA-21 | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cf8cd1b5-99c1-3957-893b-590bc58064cc | -2.30552 | -51.26899 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 36da0609-b0f6-3307-a091-3b22ae9f2638 | -3.9833 | -49.99327 | 2024-11-24 04:53:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5260809c-2cf0-311e-88b1-866784aa5246 | -2.1389 | -46.43967 | 2024-11-24 04:53:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 677c1ee2-f9dd-329e-ae63-23d1d1e748c5 | -4.37693 | -49.74837 | 2024-11-24 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 473e4f81-63d1-3582-80b6-dc1dce6e3ce0 | -11.31951 | -54.02963 | 2024-11-24 04:53:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2a90bfd7-37cb-3c27-99f2-53cf15ffae27 | -3.34463 | -51.21288 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a4bfd68b-b5f6-3404-8f80-d0429e65a8e8 | -3.75198 | -54.78107 | 2024-11-24 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 343753f4-c2bf-37c9-a3c9-679781ded194 | -1.85187 | -52.27906 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63e92775-5e5e-30f5-8fb6-55fce5e60371 | -3.54092 | -53.07229 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c46e161-f87a-3c2e-a876-9a4fe83376d2 | -3.02539 | -51.36307 | 2024-11-24 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3bd32d11-cbc4-3b09-ae17-baad06fa61f4 | -3.50595 | -53.80753 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b51349a-983b-3994-8b5a-ebb4f3c3a71f | -4.0968 | -51.07606 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 800d829d-dc7d-3d3e-a8e5-8449d2aeb597 | -2.261 | -50.46317 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 51327688-0971-392e-95a6-6209f9672ee2 | -2.457 | -49.08739 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9cf58567-41ef-3225-a97d-b55151701bbc | -2.24376 | -49.22375 | 2024-11-24 04:53:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 433648b6-5fa2-369a-9a1b-de6e262edb44 | -2.87062 | -45.8315 | 2024-11-24 04:53:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 837889d1-366c-3ac2-817f-ae780b5f66c4 | -1.46525 | -51.11675 | 2024-11-24 04:53:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9f1f39ad-a846-334e-8460-2e57ffa1402f | -2.54211 | -53.99379 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b298d7f8-f662-397d-a06a-29dccc73c18a | -3.6334 | -51.52093 | 2024-11-24 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b676946b-ec32-3612-a940-af72927e7d0f | -4.91924 | -48.42831 | 2024-11-24 04:53:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a56bf0ae-9561-39a8-b98b-7d4302de1972 | -2.91832 | -50.32256 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5a1dcb2b-a560-3bcb-8a66-2740fcb64f0a | -3.43143 | -49.97762 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c6a93c7-9ac1-37eb-8ba2-513dbf421f3b | -4.14312 | -51.06514 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd48de63-bb6d-39e6-adda-5723598fd331 | -1.24518 | -51.78657 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 85fb0c3b-756c-3c0b-ac83-86bccc515775 | -2.12598 | -46.71068 | 2024-11-24 04:53:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a9bace74-b851-3be8-915c-5d5926042845 | -4.55104 | -44.0167 | 2024-11-24 04:53:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0575f12d-bd70-3570-b8c4-834b0975828d | -4.69993 | -45.85032 | 2024-11-24 04:53:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f9d40c0b-5042-3561-bb86-a5a35c805e20 | -2.6658 | -46.60761 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0d53e70b-24cf-3e57-9a27-245c94e29640 | -2.01072 | -51.17353 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9626e0ed-fce2-3ed1-affc-6dd7330c53b7 | -1.23474 | -51.78848 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91a6aaa9-d8df-3767-bfb6-c9dd198f2351 | -1.73439 | -52.7257 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dca7c91e-bd2e-3118-8695-e1555c12a311 | -1.11627 | -53.39436 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c404ed6a-eef1-3d70-9928-4cfa17439a07 | -1.42719 | -51.12152 | 2024-11-24 04:53:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 43132828-4617-301b-93a9-071c954a46cc | -2.14878 | -50.92029 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| bb3557f7-ba12-384c-9a5b-533a67b7054d | -3.28294 | -53.84034 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 00c4fd75-5e75-3002-a99b-7629ab75d49a | -0.39864 | -51.4573 | 2024-11-24 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 28453259-a6a0-390a-acbc-d0a8b968491b | -4.05636 | -53.6477 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 796e4d9e-2164-3555-b61a-2396077011f7 | -2.77985 | -54.20252 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 412ca756-0e08-308f-9891-e145709008dd | -2.46665 | -54.77043 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 045f8e5d-22e8-3a78-926c-bf0b2492d266 | -1.46424 | -46.04403 | 2024-11-24 04:53:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 106fc306-c680-3bc5-992b-69356694a9df | -3.32072 | -54.08665 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2b0c5d65-6253-3c92-bbed-81a88a590fb6 | -2.21518 | -50.8228 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4de95ab2-a642-314d-8f32-4db591ee9d11 | -4.00011 | -49.94392 | 2024-11-24 04:53:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8fb3e5a7-6e22-34b2-b26f-df5a2b93f77b | -1.31575 | -49.38947 | 2024-11-24 04:53:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 4c67be28-158e-31dd-bde3-75a70dc2f6f2 | -1.73553 | -52.74017 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e82f23c-10e1-32b7-a1a2-d07f24720aab | -2.63658 | -51.89537 | 2024-11-24 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a346de1f-54ab-3cbc-8703-643e77bf35b2 | -2.56823 | -54.05136 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 013217cf-93cf-3ada-8abb-5f5ca47fbee5 | -2.10018 | -48.88293 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8456a6d4-694c-3a19-b7f2-532b77c27c3d | -3.9978 | -49.95924 | 2024-11-24 04:53:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d356ebf5-5542-3359-8121-1f1856435b17 | -4.37282 | -49.75176 | 2024-11-24 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dbcdf786-301a-3a25-ae10-a2b795b06350 | -2.28308 | -51.04101 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 23f7d7fe-61ed-3fb2-b247-9b30305c2076 | -1.2055 | -51.75515 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 403c5069-49ff-3b06-87be-98d857ed8e03 | -2.71244 | -46.2631 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7edf9bdf-f8ed-32d6-a10b-70bdb277183d | -3.29138 | -53.85282 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c75506de-f58b-365c-9859-80418277534a | -5.00219 | -42.9464 | 2024-11-24 04:53:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6fc0ce82-61c0-303b-bc9c-d990cc915f7e | -2.58598 | -54.05032 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5cb6f035-4c5c-388b-bf06-cc21972beace | -2.43799 | -54.14289 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0228c0c-c75c-316d-b661-e7ca6a8485e4 | -2.26437 | -50.46369 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 226d9607-6404-3b16-b4d7-b32004d0ce8d | -4.26405 | -49.82442 | 2024-11-24 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 224f50e4-9cfa-30c6-952a-854301ea926e | -1.93731 | -48.67081 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4147b1b2-3332-382d-bad5-084009d633a3 | -3.18042 | -54.33295 | 2024-11-24 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| af9746bc-4df0-3fa0-a53b-51d12470c24e | -3.93925 | -48.1478 | 2024-11-24 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| be71c360-ccc9-3f9b-9f3f-6441dc4cec89 | -4.43549 | -50.61068 | 2024-11-24 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b23a1de4-986e-3eb2-ae00-e27108c1a9c2 | -1.37552 | -55.39995 | 2024-11-24 04:53:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ed4a0500-753f-37e6-ad56-cd2343791ff0 | -3.66084 | -54.42212 | 2024-11-24 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9eaf1e7c-3f3e-36d9-b99d-ab18bb8188f0 | -1.05894 | -53.64841 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b41dfa69-e219-3951-96b8-844adce23c2a | -3.38806 | -51.03951 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76d12d97-7596-3166-a0bc-ce119e3b0a2e | -1.75809 | -52.66153 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e8e4edf2-f993-3b7c-bc84-6292d4cc6810 | -1.38302 | -52.42803 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d1ce9157-a90b-39d8-8f05-038204aeaeda | -2.84734 | -53.99501 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a17f777f-1e26-3291-a4f2-b58d6d9257f4 | -3.28467 | -53.82946 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| abea6339-22ff-36b5-b3e8-1d166d954e34 | -1.25989 | -51.75724 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2ab0cd9a-0146-3568-a082-df31375cdd7e | -2.50111 | -50.48503 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9afbe83c-0bcc-358e-9909-899e4881e3a7 | -3.28799 | -53.8523 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff4833f6-2d2f-3046-8759-fc0daf3e77cc | -3.62323 | -54.79367 | 2024-11-24 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 29927c8b-2b21-3d6f-aac4-30e997465f85 | -4.37985 | -49.75286 | 2024-11-24 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6bcfe648-0573-31dd-96f0-e410e6ba813c | -2.76887 | -54.06998 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0c3b44d9-2ced-3754-a00a-b28d878f9b3e | -3.32049 | -53.28511 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 289fc32b-4b4d-39de-857b-e943067c1b25 | -2.88555 | -53.99712 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3028143e-b751-380b-aa58-ddf55451809f | -2.35132 | -49.04379 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1be746cf-d0a7-346b-add2-6c3bb8d9a7a6 | -1.18331 | -47.79422 | 2024-11-24 04:53:00 | NOAA-21 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b63a5e0-3052-3c76-aacb-40a4afac0318 | -4.97959 | -48.8515 | 2024-11-24 04:53:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d92010b4-d708-307b-bb13-62213434786a | -3.31672 | -54.08982 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9bacc141-7b75-36f0-8e6c-048ad4edf62d | -2.7574 | -54.07584 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b18e0b90-b1bf-3e8b-afd9-2529695edafe | -4.08149 | -46.83316 | 2024-11-24 04:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1b30f979-15cc-3b0c-86c3-ea0abb164598 | -2.47186 | -53.97147 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 18f6696d-584a-3987-8223-d27ff54d23b0 | -2.21071 | -48.91919 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 55a174ac-23f4-3394-b7bd-a70fc0cfad9e | -3.12108 | -53.1032 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0536531f-5ae7-3454-9964-0dd35b74aeb4 | -5.071 | -43.69824 | 2024-11-24 04:53:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a9a25d33-41b8-3713-85d0-28badaf847fd | -3.21976 | -53.83762 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README54.md)
