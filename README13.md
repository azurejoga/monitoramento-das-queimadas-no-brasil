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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9f4a3adc-8cdc-38fa-ad0f-a1bbad31f592 | -5.14848 | -50.87724 | 2025-11-10 04:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c26e65a3-e1f7-373f-95e1-6fb046518c6f | -10.49241 | -44.94178 | 2025-11-10 04:21:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d998acca-1a4f-3dfb-bd2e-fb77ca29bff4 | -9.12921 | -50.08435 | 2025-11-10 04:21:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ef9b912a-dc41-3785-a09e-79c69d63557c | -6.81176 | -34.94572 | 2025-11-10 04:21:00 | NOAA-20 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a5a4ce6f-6d98-37fe-a15c-4f121c512a9a | -5.3721 | -44.7298 | 2025-11-10 04:21:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b597d4fb-17c2-30ec-adf2-72fbf1f5399f | -3.5058 | -50.09108 | 2025-11-10 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5c96c7d-c274-305b-8493-56152a6904bc | -5.913 | -48.32137 | 2025-11-10 04:21:00 | NOAA-20 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85e8fb43-f351-3930-8562-7463b03cf969 | -3.83817 | -51.20496 | 2025-11-10 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3ea8e18c-896c-360d-bd85-339a3d7f00ea | -5.92575 | -43.9327 | 2025-11-10 04:21:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 48b423c3-df49-3344-bb03-9552c72ab660 | -7.9316 | -55.01528 | 2025-11-10 04:21:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 283e6b1b-589c-3105-ba19-c01a63aa12a2 | -4.06971 | -50.44383 | 2025-11-10 04:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f468a66-133c-380a-8cb8-8c1a50ca6bd3 | -5.64265 | -43.00318 | 2025-11-10 04:21:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| f35056e8-a3e9-332a-ada9-9283b77d895b | -4.07016 | -50.44281 | 2025-11-10 04:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f46a703c-5ca6-308c-ad2e-2a79b7a9449d | -3.49399 | -50.49015 | 2025-11-10 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4f76b839-9ee2-3d67-a5ad-253b6b6dd928 | -3.39986 | -50.45917 | 2025-11-10 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 06ae1076-d4f3-3436-8908-5031606ea394 | -4.31332 | -49.87742 | 2025-11-10 04:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a72bcf2b-7979-3112-96d9-3ab89e30e5c3 | -3.33024 | -49.92284 | 2025-11-10 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5bfdc54-220b-39e0-adfc-9413d5df8ada | -3.95503 | -51.00597 | 2025-11-10 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 83fe4179-dd46-38ce-9cfc-54b1f7fc7718 | -3.41382 | -50.26226 | 2025-11-10 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4f123278-4f6d-3825-a6f4-b53df7516a52 | -6.64287 | -44.19105 | 2025-11-10 04:21:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2d3a434d-bbd4-394b-a21f-99eb0de3eeee | -3.7766 | -52.24476 | 2025-11-10 04:21:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b7403f3-bd00-3214-b645-238b8f0ab38d | -8.20977 | -43.55032 | 2025-11-10 04:21:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3b0414b8-ee0d-3f9a-b668-ca41988a7a26 | -5.48656 | -44.39117 | 2025-11-10 04:21:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bbcf9999-7f3c-3d03-816e-6f8c9e2eeb82 | -5.07475 | -45.57621 | 2025-11-10 04:21:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8684263a-74cf-3375-aedb-1d15efbe1555 | -10.46145 | -44.94407 | 2025-11-10 04:21:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6f3dc153-ea45-32b5-a457-305390f65427 | -5.24491 | -45.10347 | 2025-11-10 04:21:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a1526f4f-666d-3772-8ca5-db4eaabbb9f7 | -3.47632 | -49.93317 | 2025-11-10 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0551326b-1f3e-33c6-b5b9-46db70132607 | -4.91702 | -46.73586 | 2025-11-10 04:21:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3cca2ddb-f92a-3cab-bc1e-ad8c19b5cf2f | -11.0265 | -44.64789 | 2025-11-10 04:21:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a4da374a-265f-38ae-a43c-72bb9e1c6a9b | -5.22167 | -45.03576 | 2025-11-10 04:21:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9a2053b0-04b1-3982-8c24-1ef90d6ca9f6 | -3.69076 | -50.1925 | 2025-11-10 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0318dd50-35b8-3295-9679-4133e1b4610d | -5.37649 | -44.72347 | 2025-11-10 04:21:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3f5eeb20-02f5-3f82-9050-ccc17b029d8c | -3.08382 | -52.92475 | 2025-11-10 04:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| df1fe8ed-f138-3696-a052-9aa4b94a61fe | -9.90905 | -44.21361 | 2025-11-10 04:21:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 96920247-c4c2-313a-87d9-75c282db62c0 | -6.55337 | -40.11595 | 2025-11-10 04:21:00 | NOAA-20 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f5b2b7b6-e23a-33c1-b1d3-b4ef710699db | -3.31077 | -50.12172 | 2025-11-10 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5c67bf8f-0fc1-31f7-83af-d98e9a0e51df | -3.3308 | -53.24792 | 2025-11-10 04:21:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3af9a9aa-8761-321d-9770-814608ae457d | -4.91221 | -44.88658 | 2025-11-10 04:21:00 | NOAA-20 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c0656a26-e168-34d7-9a23-da3cf890066f | -5.88259 | -46.1488 | 2025-11-10 04:21:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 311a7eca-bbe8-331f-9cd6-e7e1958b9b47 | -10.01715 | -44.14906 | 2025-11-10 04:21:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f694ebb3-0c5e-3ac2-8036-6b858b648399 | -5.92244 | -43.93219 | 2025-11-10 04:21:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 40f70bc9-250f-3c82-b87a-5c904a7c9cdc | -11.91085 | -43.82606 | 2025-11-10 04:21:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3f6b7de3-9b9e-3e1d-9338-0c59403c47fb | -3.97842 | -49.96202 | 2025-11-10 04:21:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d70cf30-8ed9-3dbd-bdd3-007d7e9f2b9b | -2.94264 | -51.57755 | 2025-11-10 04:21:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e4819eb5-0018-3a2d-855d-f02ee571d4ab | -4.63538 | -46.39537 | 2025-11-10 04:21:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 740b23f1-7f39-31ce-900b-2fa36dba1395 | -8.04553 | -39.69509 | 2025-11-10 04:21:00 | NOAA-20 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 3.3 |
| beff0058-5d8a-3950-b4d7-f06c01d96864 | -5.6353 | -43.92245 | 2025-11-10 04:21:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d4396095-4d0f-36a4-a15d-5def1bcaf11b | -9.57425 | -49.11715 | 2025-11-10 04:21:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e097dc6e-d4d7-3357-a94e-a0c1971ef8ad | -4.58887 | -45.55035 | 2025-11-10 04:21:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3f616af0-57d8-3677-b3cb-30edccde1f72 | -3.59619 | -55.47152 | 2025-11-10 04:21:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 18e0d847-0c55-3d39-a3ec-283c19d59913 | -4.58609 | -45.54623 | 2025-11-10 04:21:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 41bebed1-b72c-366f-9dcd-3b646dc0fb0b | -5.12806 | -44.72621 | 2025-11-10 04:21:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 841dfcaa-75d3-34aa-91e7-2dfad64fbbb9 | -4.68399 | -45.85252 | 2025-11-10 04:21:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 59b944f3-1c6d-38f3-8d89-92d2980de47c | -9.80686 | -43.946 | 2025-11-10 04:21:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4ee5b17a-1832-3f24-9509-0d449e82fc56 | -4.68061 | -45.85194 | 2025-11-10 04:21:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c9e3cd5d-06a0-3f87-b9e4-4c391b85e4dd | -5.37979 | -44.72399 | 2025-11-10 04:21:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| af8d2875-11c9-3e6f-967f-368ba80ff982 | -3.40944 | -50.26155 | 2025-11-10 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7aa89d28-632b-32c6-bed2-7124405a6f84 | -6.11662 | -48.19645 | 2025-11-10 04:21:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 827d8635-0cc2-3891-92d8-c14dee436cb0 | -3.77679 | -47.61322 | 2025-11-10 04:21:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9d97ad5c-f82b-32ad-8c75-f508bdaf11a9 | -6.57475 | -42.90944 | 2025-11-10 04:21:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 039f7225-7bc4-3ff0-9461-60e08e88b668 | -4.64736 | -46.34336 | 2025-11-10 04:21:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e91502d0-ebb7-30ca-b7f7-36baf22dab2d | -3.45194 | -49.97481 | 2025-11-10 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 86778a03-07bf-3bc0-99a5-d5b854efa91e | -11.21892 | -41.54364 | 2025-11-10 04:21:00 | NOAA-20 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 2cefa28f-22c2-39e8-8a25-fd82bfadf80b | -5.14922 | -50.87284 | 2025-11-10 04:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9ed21680-5962-3cc9-8da7-87f4f2c947c2 | -5.51706 | -45.44366 | 2025-11-10 04:21:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9a66a5bf-dc68-36d9-92cb-4e3d9db0e850 | -3.87134 | -50.97181 | 2025-11-10 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 142f8485-f89c-33b1-89a2-3f79e4b8c4e1 | -4.53472 | -45.78048 | 2025-11-10 04:21:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56ba9125-be14-368f-a9f8-f03990d826f5 | -5.20795 | -44.41395 | 2025-11-10 04:21:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 465f3aff-fccd-3236-958f-c824ee8c15b6 | -4.91354 | -46.7353 | 2025-11-10 04:21:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f49cba1a-ff57-3bd1-9b69-03ec257eb4ce | -3.58995 | -55.47081 | 2025-11-10 04:21:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| da3c33d7-6c07-335e-b948-e0d909559318 | -5.12751 | -44.72966 | 2025-11-10 04:21:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 84e8e983-2f59-33b7-82e9-3233265f11a0 | -3.97908 | -49.95807 | 2025-11-10 04:21:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 656b916c-6332-3429-8cf3-e10a1627d58f | -9.09638 | -35.41266 | 2025-11-10 04:21:00 | NOAA-20 | PORTO DE PEDRAS | ALAGOAS | Brasil | 2707404 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 29cb0629-ca94-3dea-b70e-b7e0a6d1fdbb | -4.201 | -46.19808 | 2025-11-10 04:21:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97ffc360-262f-3751-bbb4-3c823fb00c40 | -11.02984 | -44.64842 | 2025-11-10 04:21:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 97dda9a7-f9d6-3d1b-95fa-d4a01e2cbe62 | -7.88778 | -48.39198 | 2025-11-10 04:21:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6acb512e-0896-332e-8305-273c24a4b6cc | -5.19129 | -45.03448 | 2025-11-10 04:21:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8abdaa8e-1541-319b-a24a-0cfdbfd5e8b1 | -4.28541 | -50.66628 | 2025-11-10 04:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9308ec99-7e17-3c0a-8ba6-10194db7e492 | -8.18321 | -41.37096 | 2025-11-10 04:21:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| e7b0683a-79a5-3231-9294-a894d483e4b9 | -9.12526 | -50.08363 | 2025-11-10 04:21:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8753c987-60f3-3e61-a907-3dccacdddc5d | -14.69077 | -46.58305 | 2025-11-10 04:23:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 742c9130-80ab-381e-9446-13ed55c836e0 | -11.43225 | -48.17848 | 2025-11-10 04:23:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 51f95d68-acbf-3758-89c6-2f22238f043c | -13.31124 | -46.77596 | 2025-11-10 04:23:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 91e706c9-cc5a-3e74-b6cb-ed6bcf2bdd88 | -14.69901 | -46.59535 | 2025-11-10 04:23:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 176d7684-7378-30be-8eae-1ef8600d8ec7 | -13.69507 | -47.26451 | 2025-11-10 04:23:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dfb95989-8db5-3529-b22d-7161ca8e89c9 | -12.68949 | -49.11413 | 2025-11-10 04:23:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 129b2329-fbc1-3486-a968-1e8446e8d443 | -12.69305 | -49.11477 | 2025-11-10 04:23:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 29b22376-a3de-3eff-8fbe-757954333ec0 | -12.01522 | -43.85266 | 2025-11-10 04:23:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0ae4b13a-91ee-3070-8d73-f001fb7035ee | -14.49322 | -48.0165 | 2025-11-10 04:23:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 50acd1d9-36da-34e8-bfaf-b95d70ff09d2 | -13.96272 | -46.90995 | 2025-11-10 04:23:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| eb847f25-a3a5-3cd4-ad1f-45464db60dbf | -17.2168 | -46.75978 | 2025-11-10 04:23:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 23d3714f-7545-3bf1-9d30-7a131aa1b027 | -11.91775 | -44.17415 | 2025-11-10 04:23:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9db0d0df-a326-3ac2-b658-a430190e34c7 | -14.69295 | -46.5907 | 2025-11-10 04:23:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 795c976b-5858-371d-ad55-e8ee3c1f4011 | -11.5515 | -48.54752 | 2025-11-10 04:23:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3f8b8a68-75cc-3d3b-8a97-1ee826ef8949 | -17.65347 | -50.75094 | 2025-11-10 04:23:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 161a838e-8886-3cbe-8fbc-7262e267f0ad | -13.73051 | -51.45921 | 2025-11-10 04:23:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| abb62f8b-91ba-33df-8c5a-04a80e37bab2 | -14.95717 | -46.37893 | 2025-11-10 04:23:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f5cd3dca-5064-33e1-b1e4-98565405c2cb | -17.21161 | -47.6535 | 2025-11-10 04:23:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f3905f2f-a99f-3c4b-9e9a-2e9eba97a793 | -12.11269 | -43.65079 | 2025-11-10 04:23:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7294eea9-defa-3b86-b26a-b7293fbd2ac6 | -14.49384 | -48.01274 | 2025-11-10 04:23:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README14.md)
