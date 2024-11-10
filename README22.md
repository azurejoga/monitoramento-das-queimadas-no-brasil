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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 020da9bf-8b77-3d75-91be-d73d47791012 | -6.40889 | -42.49508 | 2024-11-10 03:21:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0ce73183-0615-3f8c-a9ef-5c9338fb079f | -8.40008 | -44.14977 | 2024-11-10 03:21:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 17.8 |
| e24c0742-879f-310e-8ce6-8f2436d76425 | -5.81619 | -44.12572 | 2024-11-10 03:21:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 31982185-c8f8-3a73-82a5-1d1b08b2ebb0 | -6.18496 | -36.55431 | 2024-11-10 03:21:00 | NOAA-20 | CURRAIS NOVOS | RIO GRANDE DO NORTE | Brasil | 2403103 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| dfc4a4e7-a4b7-35c8-9d3b-632baa2a07b5 | -8.76046 | -35.27545 | 2024-11-10 03:21:00 | NOAA-20 | TAMANDARÉ | PERNAMBUCO | Brasil | 2614857 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 11bebc25-47eb-3005-be1e-53ffe63006d1 | -4.39886 | -41.91449 | 2024-11-10 03:21:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9c5c9cf8-79e1-3b23-a32c-391231cfc95c | -8.38521 | -44.15352 | 2024-11-10 03:21:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 52de481d-8b5f-346a-905d-b935818a9354 | -9.22299 | -35.34475 | 2024-11-10 03:21:00 | NOAA-20 | PORTO DE PEDRAS | ALAGOAS | Brasil | 2707404 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 303c9222-44ef-377c-b857-928e62af09c1 | -4.12226 | -43.59915 | 2024-11-10 03:21:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 55e46bcb-2872-3154-94dc-b1fd4946225a | -9.02231 | -37.79174 | 2024-11-10 03:21:00 | NOAA-20 | MATA GRANDE | ALAGOAS | Brasil | 2705002 | 27 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e681a0af-4535-3a80-92c0-cb74ccfee2e4 | -8.39204 | -44.15482 | 2024-11-10 03:21:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 7406fb34-8ffb-3149-ac5c-e3b0090ec524 | -6.4639 | -40.78314 | 2024-11-10 03:21:00 | NOAA-20 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 614289d3-9151-36ea-a8e2-62b3fbcc6e46 | -8.38628 | -44.15266 | 2024-11-10 03:21:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 14.6 |
| f187ff79-3731-33a2-b038-815c8498d5c8 | -6.33068 | -39.62194 | 2024-11-10 03:21:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b32e848f-abc8-38cc-9af3-842f439a1ade | -8.39561 | -44.14137 | 2024-11-10 03:21:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 62454f15-2c8a-3cad-b689-ff98f2d3d41b | -6.15241 | -41.15461 | 2024-11-10 03:21:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f04435f6-c955-3c36-a77b-08471fe7b754 | -6.29841 | -39.49328 | 2024-11-10 03:21:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 33955899-2d91-3e90-85af-46a361e577b8 | -7.62899 | -43.55976 | 2024-11-10 03:21:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1950f821-b514-31cd-a687-de16cf0ce55f | -8.39887 | -44.1561 | 2024-11-10 03:21:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 17.8 |
| d5b56403-9a1b-37ff-a277-7fa110263cc6 | -7.43755 | -39.764 | 2024-11-10 03:21:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 251d7abd-47d0-37da-a6d6-0b123918747f | -4.85796 | -43.97029 | 2024-11-10 03:21:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a20825e7-6dc4-391d-a6db-a9afee437d36 | -4.11803 | -43.59888 | 2024-11-10 03:21:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 23.5 |
| d3f88137-6d87-30aa-b15e-b5e66275e3b9 | -7.14134 | -34.9955 | 2024-11-10 03:21:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| f911bae6-596b-39fb-837e-0ddfa63acf61 | -8.40691 | -44.15103 | 2024-11-10 03:21:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 22.3 |
| d6b6dac3-1a19-3202-b42e-7b7a3cd249e9 | -10.00801 | -36.01275 | 2024-11-10 03:21:00 | NOAA-20 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| bea4b5e5-3ce4-3277-a68e-4f8302c8c507 | -6.46282 | -40.78311 | 2024-11-10 03:21:00 | NOAA-20 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 9d8fc5aa-7c65-3e23-ac71-7ed08240140d | -9.16385 | -40.4889 | 2024-11-10 03:21:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8511cb09-80de-3764-bcdc-c16213b09aff | -5.26967 | -37.95488 | 2024-11-10 03:21:00 | NOAA-20 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 10d806f3-c974-3789-8f17-0c6f2068abd2 | -9.16449 | -40.48543 | 2024-11-10 03:21:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 78687403-017a-380b-8124-047d27ba6635 | -8.39325 | -44.14852 | 2024-11-10 03:21:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 17.8 |
| b260706d-7ed3-394a-8a2f-94444577148d | -10.95033 | -40.82195 | 2024-11-10 03:21:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 3cf05cdd-380d-3e21-bcf5-c28e9f710b65 | -4.01717 | -43.67326 | 2024-11-10 03:21:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 13d7bc60-225e-328c-8bd0-a957ff5ea55e | -5.56028 | -43.97974 | 2024-11-10 03:21:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 69824b15-aca1-3ad3-b294-96b4c6dd50bd | -7.11522 | -39.72532 | 2024-11-10 03:21:00 | NOAA-20 | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7fe29631-468c-3fc5-8a01-b11b6a17c681 | -7.43179 | -39.76568 | 2024-11-10 03:21:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 11734a0b-d837-348a-a8cd-c8ca83d6725a | -5.56441 | -43.98002 | 2024-11-10 03:21:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b70b0873-3116-3c40-bba5-40949934c820 | -10.9497 | -40.82534 | 2024-11-10 03:21:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 60d42e70-9073-3efb-9bc7-6fe157405e9b | -4.53384 | -43.57 | 2024-11-10 03:21:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f82dae05-7893-303d-b2f4-04964a8072d8 | -8.40678 | -44.15641 | 2024-11-10 03:21:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 6baba4ca-6c44-38ab-a456-4ee6a2409830 | -7.63477 | -43.56575 | 2024-11-10 03:21:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 209f8ee5-59d0-3271-bc05-33ed2ecd98a2 | -17.6069 | -57.5304 | 2024-11-10 03:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 401.5 |
| 73f18b68-a76a-393d-972a-971f3b8889b3 | -3.1607 | -50.4556 | 2024-11-10 03:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| ccea77fa-43ed-3482-ab74-0e04b8e5bddf | -3.1422 | -50.4562 | 2024-11-10 03:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 242.1 |
| 871d41b6-f7c3-3f33-9489-a661005d1641 | -3.4383 | -50.2999 | 2024-11-10 03:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| b9bd0c54-68a6-35a1-b4ec-9f7623bc2004 | -3.9668 | -48.1932 | 2024-11-10 03:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 8b59585d-4306-32ea-9931-04e986858fa8 | -3.9486 | -48.1291 | 2024-11-10 03:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 26912692-d189-39f4-9f4d-060f71d8aef2 | -4.4349 | -44.6229 | 2024-11-10 03:30:00 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 5e51ad21-481a-3880-b842-7d4243247463 | -17.6073 | -57.5099 | 2024-11-10 03:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 407.4 |
| 8cc2a1b5-d7e9-3627-902d-ca023e1a050c | -3.1239 | -50.4358 | 2024-11-10 03:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 375.6 |
| 7ac88a3f-0591-3b6c-8301-2552f0afb6ad | -1.2751 | -53.6963 | 2024-11-10 03:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 7382630a-ffc2-327f-9e27-333e83b7718a | -2.418 | -46.3024 | 2024-11-10 03:30:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 1799a265-7d69-3ef3-b945-b16a97c40510 | -2.9171 | -51.4825 | 2024-11-10 03:30:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 528e9124-cede-3e00-947f-aeaeb1f2019a | -1.5347 | -52.2104 | 2024-11-10 03:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 91.6 |
| cdd27669-66b4-3e64-9360-54baa74cb8f7 | -17.6266 | -57.5281 | 2024-11-10 03:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 277.8 |
| 75d5054e-81df-3d29-8afb-9bf083b00c37 | -2.7772 | -49.3492 | 2024-11-10 03:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 480764a9-7a0d-36ef-bee0-cb7f0380d1bb | -3.9483 | -48.1724 | 2024-11-10 03:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 09cfbdfe-312a-3280-af0a-66f3d5587704 | -17.627 | -57.5075 | 2024-11-10 03:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 239.2 |
| 7117a660-c0b9-3e62-8754-f59bd9310f37 | -3.3518 | -53.4139 | 2024-11-10 03:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| a75fc56b-fc57-3850-a589-195fc4a230b0 | -3.1238 | -50.4568 | 2024-11-10 03:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 183.4 |
| e442575f-0588-3d8a-8dc4-3a7e29f6f175 | -2.8802 | -51.4835 | 2024-11-10 03:30:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| f7089bfa-cb78-3577-b477-dbab124c8087 | -3.9485 | -48.1508 | 2024-11-10 03:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 105.6 |
| 363c4d9a-e1e9-3f6e-a139-87709f7cc2f3 | -3.1608 | -50.4347 | 2024-11-10 03:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 84f9a558-6e33-34bb-b585-4b83fbcd20a7 | -2.0953 | -48.8338 | 2024-11-10 03:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| e053a7cd-b339-3f87-8d22-eac9cf6b7fd4 | -2.9355 | -51.482 | 2024-11-10 03:30:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 0f9c7f4b-414b-3b44-b652-10b0047b79e9 | -17.293 | -57.5062 | 2024-11-10 03:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 95.5 |
| 85599839-5096-32c0-9a4d-b8aa6c61ef17 | -2.7587 | -49.3497 | 2024-11-10 03:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 1c66ea2f-e145-32b7-b311-367980b86647 | -3.9669 | -48.1716 | 2024-11-10 03:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 111.1 |
| 29a9e281-3aa2-3d76-b79a-25e8f55281c8 | -1.2751 | -53.7164 | 2024-11-10 03:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 98.3 |
| a97c963d-a8ec-3232-9664-886cb47b04d9 | -3.6004 | -47.3395 | 2024-11-10 03:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 368fff35-0ba2-379b-8dd3-f44801f81988 | -17.2933 | -57.4857 | 2024-11-10 03:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 142.7 |
| b27fc22b-0a80-30e4-bd96-bab9429b5f25 | -3.1423 | -50.4352 | 2024-11-10 03:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 406.2 |
| 7a9711a3-1a75-3c33-a7f3-1d5ca543f143 | -3.2428 | -53.0519 | 2024-11-10 03:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| cd291f8d-2726-3f2e-812c-fc82ae9f7e01 | -2.8802 | -51.4835 | 2024-11-10 03:40:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 468fe11c-c227-39bb-beab-fc632bab1487 | -17.6073 | -57.5099 | 2024-11-10 03:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 364.6 |
| c2b2a4ab-59e7-3fe8-a11a-cf9282670640 | -2.7587 | -49.3497 | 2024-11-10 03:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| eb36bd24-9d67-3355-9c6f-50f191a9b145 | -17.6266 | -57.5281 | 2024-11-10 03:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 270.4 |
| b485e147-d1eb-3ca6-acf1-e3ce59bc3c40 | -3.9486 | -48.1291 | 2024-11-10 03:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 2e5d1e41-ad0a-350d-8c1d-9149adefb97e | -1.2751 | -53.7164 | 2024-11-10 03:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 8b230c01-a9b3-389e-8696-bf084a956cdc | -3.1095 | -49.4241 | 2024-11-10 03:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 58eb1f4e-c023-35eb-99bc-4a7c790311c5 | -3.4383 | -50.2999 | 2024-11-10 03:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| bce33da6-b51e-3732-a041-bbade0afbb0f | -3.6004 | -47.3395 | 2024-11-10 03:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 1a3550d4-f8c3-3c04-abe7-03762a66c593 | -2.0953 | -48.8338 | 2024-11-10 03:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| be8b9ee4-9d03-3453-8639-d85a2a6d9c7a | -1.5347 | -52.2104 | 2024-11-10 03:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 101.5 |
| 4de470c1-ddfd-3665-afac-431af0774246 | -3.2427 | -53.0722 | 2024-11-10 03:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 25e80a0a-85e3-326f-9714-c2cd7f333f53 | -2.418 | -46.3024 | 2024-11-10 03:40:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 0a452e8c-2d57-377b-b591-a673d8def137 | -3.9668 | -48.1932 | 2024-11-10 03:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 5e3286ce-7136-3f80-b690-4dff9449f723 | -17.627 | -57.5075 | 2024-11-10 03:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 240.8 |
| 03960090-c14d-3c33-9780-8f32c4b7248a | -4.1099 | -49.1315 | 2024-11-10 03:40:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| c7cf76f0-3b5a-3166-af05-e59bd478652d | -4.4349 | -44.6229 | 2024-11-10 03:40:00 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 545aeddb-28eb-35de-a2a0-829e65a4f483 | -17.6069 | -57.5304 | 2024-11-10 03:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 381.0 |
| 77de7fca-aef0-3287-b4dd-3f8373e9c691 | -3.2243 | -53.0727 | 2024-11-10 03:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 522fa35c-9bd0-3f77-98e5-55ba4ab51a43 | -4.11 | -49.1102 | 2024-11-10 03:40:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| becfd9b6-376f-316d-acaf-d07f8ffe87e8 | -3.967 | -48.15 | 2024-11-10 03:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 27ae4620-893b-3f22-b3f4-a8e8f05e0d3d | -17.2933 | -57.4857 | 2024-11-10 03:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 147.6 |
| 43211608-11f7-34a6-8227-3d5396343df0 | -2.9171 | -51.4825 | 2024-11-10 03:40:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| d3b56649-adca-397d-9466-d2a9e23927ed | -3.9485 | -48.1508 | 2024-11-10 03:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 97.7 |
| e49e183b-da4a-35a6-a00d-379b1b2472e1 | -3.9483 | -48.1724 | 2024-11-10 03:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 105.8 |
| f53ba192-7032-3c80-a0ee-d5dcf51663ff | -3.525 | -44.0286 | 2024-11-10 03:40:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 49.9 |
| f7e5efc9-afa7-36f0-87e7-330dd41583d4 | -17.293 | -57.5062 | 2024-11-10 03:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 91.0 |
| 4646b6f9-c446-33c7-940b-714d3e230582 | -3.2244 | -53.0524 | 2024-11-10 03:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |


[Clique aqui para ver as próximas entradas](README23.md)
