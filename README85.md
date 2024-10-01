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
| 3cb67199-afd0-3576-8033-3f88b61936c4 | -20.80624 | -53.12989 | 2024-10-01 04:17:00 | NOAA-20 | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 057fceb7-4699-3c13-8c93-0e7e7dc3609b | -20.80532 | -53.13452 | 2024-10-01 04:17:00 | NOAA-20 | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a9c26c26-508d-3e9c-9b50-c4b2818c7266 | -20.80279 | -53.1243 | 2024-10-01 04:17:00 | NOAA-20 | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d5affa4a-98c6-3a7d-8d32-ca7cbbfe12f6 | -20.80187 | -53.12895 | 2024-10-01 04:17:00 | NOAA-20 | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 40a76060-01e5-3555-817e-affb37cf753a | -20.79842 | -53.1234 | 2024-10-01 04:17:00 | NOAA-20 | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8d38e6c6-3eb1-318f-9a4f-c731bf5daa56 | -20.79749 | -53.12806 | 2024-10-01 04:17:00 | NOAA-20 | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ba711f38-236d-3b37-86d8-80014163a71d | -20.79679 | -53.10867 | 2024-10-01 04:17:00 | NOAA-20 | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c4947848-819e-3dae-b817-445f8b39ce68 | -20.79589 | -53.11324 | 2024-10-01 04:17:00 | NOAA-20 | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 989a2458-cc73-35bb-a145-815f10b0824f | -20.79242 | -53.10778 | 2024-10-01 04:17:00 | NOAA-20 | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 810170f8-efce-31d0-bba8-dbeabf10c6ca | -20.78804 | -53.10692 | 2024-10-01 04:17:00 | NOAA-20 | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 65110ec2-36dc-3515-b8ae-668bb4d2c547 | -20.31837 | -53.29343 | 2024-10-01 04:17:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 153daafa-ca3d-3190-b88b-6ae5226123da | -22.00188 | -54.65088 | 2024-10-01 04:17:00 | NOAA-20 | DOURADINA | MATO GROSSO DO SUL | Brasil | 5003504 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 4cd6a3a0-25f6-3c70-886d-4e85282b78ed | -22.00098 | -54.65065 | 2024-10-01 04:17:00 | NOAA-20 | DOURADINA | MATO GROSSO DO SUL | Brasil | 5003504 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ceef8bba-fd20-387f-a1a1-4dd741c800c0 | -24.65284 | -54.09584 | 2024-10-01 04:17:00 | NOAA-20 | MARECHAL CÂNDIDO RONDON | PARANÁ | Brasil | 4114609 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| b6e56504-865d-39ae-bd1f-4c396e4fc348 | -19.97765 | -55.48804 | 2024-10-01 04:17:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 27dc1182-0433-3acc-8a0d-6d023f0e70a0 | -17.00559 | -54.06242 | 2024-10-01 04:17:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d2b51268-fa07-36df-b91d-17449cb493dc | -18.87074 | -54.50482 | 2024-10-01 04:17:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 803673c9-d025-3860-8e86-91767d146730 | -18.87052 | -54.50323 | 2024-10-01 04:17:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 15258933-81a3-304e-b326-b9da88ba9b59 | -18.86966 | -54.51002 | 2024-10-01 04:17:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a86f0817-cc30-36c7-b8c2-81fe13aa3d2d | -18.86946 | -54.50854 | 2024-10-01 04:17:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 4f16e596-dbc1-3a28-a45c-6412421038ac | -18.86836 | -54.51397 | 2024-10-01 04:17:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 60d86ac6-5d18-38b0-9c67-c89127cbcf15 | -18.86344 | -54.51508 | 2024-10-01 04:17:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e8e45cec-4e5a-357b-96be-ef7adbe6448e | -18.86334 | -54.51328 | 2024-10-01 04:17:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2ef3e67e-25c5-3889-aa86-06da63312ba3 | -19.98989 | -55.48129 | 2024-10-01 04:17:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f46a8751-bc16-33fb-8f4d-8828d2109b26 | -19.98929 | -55.48407 | 2024-10-01 04:17:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2e6cb815-c730-381e-9855-1a5b09f9d28f | -19.98411 | -55.48309 | 2024-10-01 04:17:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b85e7025-fc9a-3687-a060-86e797277ec2 | -19.98351 | -55.4859 | 2024-10-01 04:17:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dc5d079d-6688-3a57-ba33-28fbfd2b6506 | -19.97831 | -55.48497 | 2024-10-01 04:17:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d57146b2-9afb-32a8-b51a-7a235a724b35 | -19.97248 | -55.48701 | 2024-10-01 04:17:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9727e74a-e6fb-3d44-b3c8-5203536a173b | -19.97168 | -55.49072 | 2024-10-01 04:17:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c4d6edbc-aea2-3a66-8c54-b917b3b4f99e | -19.97081 | -55.4948 | 2024-10-01 04:17:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f96dccc4-93cd-3a7b-8986-d13d68b3f575 | -19.96639 | -55.49024 | 2024-10-01 04:17:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ea64aa7c-c6e0-3cb5-ad64-a5018ee38f18 | -21.69827 | -54.79655 | 2024-10-01 04:17:00 | NOAA-20 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| af375335-13f1-30f2-bf4e-08c2138a14e3 | -21.69712 | -54.80207 | 2024-10-01 04:17:00 | NOAA-20 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 019b2525-b010-35a8-9db3-345dc55a2c7f | -21.69352 | -54.79536 | 2024-10-01 04:17:00 | NOAA-20 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9cc13248-f6c7-3d40-a857-d9e6b8890c68 | -21.68793 | -54.84638 | 2024-10-01 04:17:00 | NOAA-20 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| addde2de-5b2d-360f-93db-465bc83c7620 | -21.66529 | -54.8588 | 2024-10-01 04:17:00 | NOAA-20 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ef78c786-4fda-3d78-a387-c41556e98bb9 | -21.64622 | -54.85406 | 2024-10-01 04:17:00 | NOAA-20 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 4adfd457-49ed-3129-92a2-336b3ac52be1 | -16.60119 | -55.93884 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| a5b0bd5e-3d3b-36cc-97ec-a4dca2716e86 | -16.59609 | -55.94589 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| c82ae51e-d02e-3ba0-a0ca-acae55c45b8d | -16.59953 | -55.9469 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 11e2f9d0-26aa-30a4-ac1a-37f2b2fc6850 | -16.59389 | -55.94561 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| a52d820d-a807-3024-a383-c645f9d3e7c7 | -16.72566 | -55.49908 | 2024-10-01 04:17:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 08d57ff4-e427-3236-9e85-5bb968669775 | -17.18203 | -56.16106 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 14389165-8a1f-3d32-9cae-973fcf756055 | -17.18118 | -56.16512 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 957d2099-23a5-3019-9ccf-e0ee547a9a64 | -17.18032 | -56.16919 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 5d140dc7-ed43-31e4-bbba-ffb057dab49d | -17.17862 | -56.17731 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 49c4f4f8-2152-344f-baf2-152b8bceb913 | -17.17776 | -56.18139 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| a677466f-24b7-3108-b327-cb7668101183 | -17.17724 | -56.15566 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 4041109c-3ada-365e-a3c0-3f08dc170139 | -17.1769 | -56.18547 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 9ebb4908-fdba-31ce-b6cf-d5ba6453e73a | -17.17639 | -56.15973 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 9681f8cc-2c79-33b0-8cf7-11bb617223be | -17.17553 | -56.16378 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 0fc125bd-6f3b-3d65-aca8-d2afaf7db336 | -17.17468 | -56.16785 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| f57bc7e3-a36f-3118-b49e-2be1e29f85f3 | -17.17382 | -56.17191 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 99b0c4ef-0d18-339b-bc10-7cda7a1ed28b | -17.17296 | -56.17598 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| e0ed2220-114b-34cb-87a3-3bec1434b6a8 | -17.1721 | -56.18006 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 37b5c1a9-6c20-3b17-96ea-fd8d22af5062 | -17.17124 | -56.18414 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| a91323ef-12b6-36f3-a220-a7520746332c | -17.17039 | -56.18821 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| a99428ec-87e1-3601-810a-3835de419eb3 | -17.16988 | -56.16245 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 074a5c49-520e-3415-a2bb-3900b9be3866 | -17.16903 | -56.16651 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 90216bf8-2610-34be-adb1-13297066f7af | -17.16817 | -56.17055 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| faa2e39f-3f63-3746-a5b7-ded02d47a960 | -17.16731 | -56.17462 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| cbad2548-a400-3ae3-9dba-aed793be6eb7 | -17.16645 | -56.1787 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 47481a7a-9558-3d23-aa42-ece9c93c953c | -17.16596 | -56.15296 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| eae999e2-3d16-383f-9046-a03e7556f302 | -17.16559 | -56.18278 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 32d1a319-3f8d-3064-a32b-d74ed78637b7 | -17.1651 | -56.15703 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 44e175f0-5376-3de1-9a4b-78d894903604 | -17.16473 | -56.18686 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| ea7b79fd-5f5c-3c18-9ca9-cdd017100c94 | -17.16424 | -56.1611 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 5498bcab-f5f4-3df1-ad72-680ee102613e | -17.16338 | -56.16515 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| e4f8bd2a-8545-3b4a-8b83-988bdc04e2cf | -17.16253 | -56.16919 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 7e7f6d71-576d-3c2b-9818-e665fb28cde0 | -17.16167 | -56.17325 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 3170b7a4-79d9-3cc7-8a3e-acf313bc6f41 | -17.16081 | -56.17733 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| fad45b41-0b61-3879-b28c-51f5aa8d746c | -17.15994 | -56.18141 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 72b4e451-d8f4-3117-8019-ff4357df4f04 | -17.15946 | -56.15565 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| cc54db8e-73e0-3144-92e9-e84296d877dc | -17.15908 | -56.18549 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| abde7709-d0c6-34d3-b3e8-7ed06b068ff3 | -17.1586 | -56.15971 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 890762fd-c98b-3de4-b125-f3742381acd5 | -17.15822 | -56.18956 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| f240ad7d-fe60-3576-ac9d-c57cf33e648a | -17.15774 | -56.16376 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 820a0845-38ce-3814-9763-0b997851419b | -17.15688 | -56.16782 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| ca1f89e4-2353-3541-bbb9-82ab423d74c7 | -17.15602 | -56.17188 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.8 |
| 053bd504-f7b1-3368-975f-a409e260dabd | -17.15516 | -56.17595 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.8 |
| e61d842c-8c13-3ba0-9c72-3daa36c2ab68 | -17.1543 | -56.18002 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 41b3cc81-cc86-30bc-9daf-83deefce5ff6 | -17.15343 | -56.18411 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 2e0e77a7-32d0-3bf5-abb6-b56013a84daa | -17.15257 | -56.18818 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 7d0fcb3e-d4c4-3dbd-a337-76adee6bd5a9 | -17.14863 | -56.17873 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 84d3d255-a38a-3c41-958e-66217d527514 | -17.14778 | -56.18277 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 668c48ce-d160-3087-a67c-73ccb4ce2767 | -17.14692 | -56.18682 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 85998006-dd1c-3423-8dc3-420705210f57 | -17.14212 | -56.18144 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 9323a3ae-c89a-3006-b722-324bfc056bb5 | -17.14126 | -56.18547 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 88e3644b-4a6e-3152-ae41-417b67b6db49 | -17.14039 | -56.18955 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 24f9802e-ffb8-3c64-84a6-b4d38be3e233 | -17.1356 | -56.18412 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| e93dded0-5ed5-3a10-a27b-17ce36a5b2a0 | -17.13474 | -56.18819 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| b29961e7-c2f9-3b15-9ef1-5f148be8c400 | -17.11483 | -56.13411 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 6a2c8d5e-7718-32fd-aeab-b78e005b3852 | -17.11399 | -56.13815 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 4883f41b-1454-3621-bb90-1d8ca074787b | -17.08267 | -56.11794 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 17e71498-abe3-3df2-907f-dd295eba9b1b | -17.08183 | -56.12199 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 860755e4-bf6a-31e7-8158-5b165f9c98cc | -17.06097 | -56.10853 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 63c198ff-9641-3d48-83df-698408349950 | -17.01367 | -56.08039 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 00625984-1cfc-3cab-b1c1-7be2f899df96 | -17.01156 | -56.08011 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 99391cb1-71ad-330f-8184-f570361f1c88 | -17.07606 | -56.20617 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |


[Clique aqui para ver as próximas entradas](README86.md)
