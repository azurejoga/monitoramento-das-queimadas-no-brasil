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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 126273d0-397b-36e8-820c-1efd69e7224c | -21.51422 | -45.11775 | 2026-09-28 03:34:00 | NPP-375D | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 7c8f7ca2-a113-3218-b478-2ee7efcab21f | -21.52044 | -45.11953 | 2026-09-28 03:34:00 | NPP-375D | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| c1355439-4fe1-3ac6-804e-5f5d63602c58 | -21.51554 | -45.11227 | 2026-09-28 03:34:00 | NPP-375D | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 5c0ff52f-6b8c-35a2-9f26-ec1bba57cb5c | -11.1775 | -44.7832 | 2026-09-28 03:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 79e6e027-74d0-3da0-b851-930fcb05ff46 | -11.1958 | -44.8269 | 2026-09-28 03:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 124.4 |
| b6f5d370-b61e-378e-8635-7d2f4ae8f1c1 | -11.7135 | -50.5966 | 2026-09-28 03:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 8fec299c-cf47-33fb-8dc1-d9d519d2d649 | -3.4102 | -48.3448 | 2026-09-28 03:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| d0793235-5b5c-357a-8b05-aab258e859d2 | -9.177 | -61.4073 | 2026-09-28 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 54e51974-0829-35b1-bd56-b80a70e2d729 | -3.4287 | -48.3441 | 2026-09-28 03:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 1dbbb987-3ffe-36cd-b3f0-5ffeef81a8ae | -18.1151 | -44.3745 | 2026-09-28 03:40:00 | GOES-19 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 57114bc8-0f9c-3fca-9b63-ac2cb1715e2f | -11.1771 | -44.8064 | 2026-09-28 03:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 333.3 |
| cbffd416-5b58-369f-a1c5-ac283447ef3f | -11.1966 | -44.7805 | 2026-09-28 03:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 15bedf8d-b542-318b-a773-a0bb0d1f968f | -6.7064 | -45.599 | 2026-09-28 03:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 93878afa-ffe9-35ac-a526-587f2d82dec7 | -3.1471 | -54.0849 | 2026-09-28 03:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 6109a70d-1348-3edc-baa5-bb6b2ad4097c | -11.1962 | -44.8037 | 2026-09-28 03:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 449.6 |
| 53e9477b-9e30-3860-8015-e8ac29bcccd0 | -11.1767 | -44.8296 | 2026-09-28 03:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 01b21695-410b-36a1-9c1a-855949a07354 | -2.998 | -54.7492 | 2026-09-28 03:40:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 7cb4ca3d-7996-3262-a662-96c48ba6f8c7 | -11.6945 | -50.5988 | 2026-09-28 03:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 1cffdd7c-21fb-3182-a542-ea26d098d634 | -10.9156 | -50.6845 | 2026-09-28 03:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 62.7 |
| dd804915-3377-302a-9407-40a18bc9afd2 | -6.19302 | -35.24812 | 2026-09-28 03:47:00 | NOAA-20 | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c721d622-d462-33f9-bdc6-373faa5688a7 | -6.92401 | -41.60937 | 2026-09-28 03:47:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| db126421-14e5-3973-91a6-cba77d18523b | -6.94054 | -41.61681 | 2026-09-28 03:47:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 5f0fc2e0-b188-3f4c-84dd-041385af2565 | -5.84582 | -45.17443 | 2026-09-28 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3bd67293-f352-3c44-a6af-0ca823a98b42 | -5.2476 | -44.93877 | 2026-09-28 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8082c954-1d23-30aa-ba34-30d03c6bd588 | -5.24369 | -44.93594 | 2026-09-28 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a160787e-a657-315a-9622-11ef3c7d51a9 | -5.12254 | -45.77463 | 2026-09-28 03:47:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 98687679-5b2d-38d9-b49a-732bedd0378c | -5.8451 | -45.17839 | 2026-09-28 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f99b849f-e2c6-3a97-a44b-6c9e91d15418 | -5.72486 | -43.28049 | 2026-09-28 03:47:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 9ced8c90-e058-33fe-aa90-8fc76c0d1fd8 | -3.97414 | -44.51337 | 2026-09-28 03:47:00 | NOAA-20 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f70d5f83-c140-3d35-bc55-b57a1a3dd4b1 | -6.93983 | -41.62095 | 2026-09-28 03:47:00 | NOAA-20 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 9a5d7793-4109-348b-a91d-e122b5a4316e | -4.37142 | -42.99038 | 2026-09-28 03:47:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 51c12692-5bf3-3533-a04c-46cb85f4ee25 | -6.311 | -43.61132 | 2026-09-28 03:47:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e3cecdc6-9ec7-3b97-aff5-eb0402963b22 | -5.84709 | -45.17854 | 2026-09-28 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 54b103e2-472f-3395-9881-f3850ea42f50 | -6.69752 | -42.14641 | 2026-09-28 03:47:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0e1cac92-8287-3264-88ac-2f7d807b91a0 | -5.63337 | -43.72535 | 2026-09-28 03:47:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| df399602-f066-3dfe-9f62-35277dbe2347 | -5.84778 | -45.17456 | 2026-09-28 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f4b833c-fe1e-31a0-b546-e72dd3a47467 | -3.36995 | -44.37315 | 2026-09-28 03:47:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e6350b42-b0b9-313c-a788-dae5cab3daaa | -5.72668 | -43.27711 | 2026-09-28 03:47:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 6921a5c9-9a2c-3cab-81fe-f84242b6c017 | -6.94625 | -41.60944 | 2026-09-28 03:47:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 23.2 |
| 614bab60-d068-3a75-ad9c-e6c154901314 | -7.0676 | -41.74258 | 2026-09-28 03:47:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 0.2 |
| 738ead17-93d0-3ae3-9722-1b9c6912d6bd | -3.4137 | -48.34188 | 2026-09-28 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 3a6f6717-aec5-3105-bd82-c528672bb2ff | -6.00171 | -47.39847 | 2026-09-28 03:47:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 7ec211ea-714c-3e5e-ad8b-139463a36ca1 | -3.93304 | -42.55567 | 2026-09-28 03:47:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| adc7a7ad-24db-3879-b6be-bde07bb2d990 | -3.81358 | -44.09371 | 2026-09-28 03:47:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 92f76826-6e08-301e-ab75-ef33a3e08c5a | -3.94078 | -42.55936 | 2026-09-28 03:47:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 13.0 |
| dc4a16b4-ed07-3ad7-9f2f-5734a00fc9db | -5.73161 | -43.27803 | 2026-09-28 03:47:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 458d9eb6-8c78-3917-b902-3af6c9cdabf7 | -3.37608 | -44.37049 | 2026-09-28 03:47:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3f6d7fd7-2e5b-30f2-a32d-69f8117a7a19 | -3.81299 | -44.09717 | 2026-09-28 03:47:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cdbab24c-7017-396c-8b96-b42405911d15 | -2.98717 | -47.45561 | 2026-09-28 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 851c9d5c-708c-38e5-b8b7-5ad56c5488d1 | -5.24989 | -44.93321 | 2026-09-28 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 11fe703f-94cf-3d77-867c-372b59cbc638 | -3.82437 | -44.09551 | 2026-09-28 03:47:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b4621146-9743-355e-9cb0-f90f8be3a246 | -5.12333 | -45.77018 | 2026-09-28 03:47:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 79e7f549-e54e-3422-bcbb-87990f236aa3 | -5.7257 | -43.28265 | 2026-09-28 03:47:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 52aa86a7-7f8b-3c48-90f6-2d9b3d48199a | -3.36503 | -44.36856 | 2026-09-28 03:47:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0bdd56c4-a874-355c-bbfc-10cb9fdcfa94 | -6.13948 | -44.1362 | 2026-09-28 03:47:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3a69316c-834a-319c-a75c-010d8b596ec3 | -3.93594 | -42.55849 | 2026-09-28 03:47:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 37335cf3-f1d4-3c46-b044-a3695c9dacb0 | -6.18971 | -35.2476 | 2026-09-28 03:47:00 | NOAA-20 | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0a793646-2e2c-3ba2-9ad6-db89090905ef | -4.07769 | -40.51594 | 2026-09-28 03:47:00 | NOAA-20 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 01cbe78f-d583-33b2-ace1-7c54bff8f02e | -5.11741 | -45.76936 | 2026-09-28 03:47:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 96f5b2d1-6d2b-308d-9916-464a3939da48 | -3.8076 | -44.09626 | 2026-09-28 03:47:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9311f49f-e200-357b-b35a-db5043743886 | -6.09373 | -37.62608 | 2026-09-28 03:47:00 | NOAA-20 | PATU | RIO GRANDE DO NORTE | Brasil | 2409308 | 24 | 33 | nan | nan | nan | Caatinga | 3.2 |
| ddec13f2-ee78-36dc-aa29-2460e5ea2bf0 | -5.24925 | -44.93698 | 2026-09-28 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6cd34371-8877-32ae-bc9d-3b66a65619ad | -3.81897 | -44.09463 | 2026-09-28 03:47:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b18ea4b0-963b-3383-8bc8-eae09aa790cc | -3.82379 | -44.09893 | 2026-09-28 03:47:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1a1a8014-afd4-3368-a5bd-a6e467b62bc6 | -6.00115 | -47.39731 | 2026-09-28 03:47:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 02baa0c8-efae-3889-bb14-d69d8618b8a8 | -3.97351 | -44.51705 | 2026-09-28 03:47:00 | NOAA-20 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c42c0ab8-1900-3b6f-945d-9d89eeb79f86 | -5.89399 | -42.43985 | 2026-09-28 03:47:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| dd55961c-ff7b-36c9-a3dd-0d3407584ffb | -5.89245 | -42.43189 | 2026-09-28 03:47:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| eacda3fc-aad6-3e6f-9901-7151e2e504a9 | -5.24269 | -44.93411 | 2026-09-28 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3dc1f613-3d14-3bfb-8790-d64084419c57 | -6.31053 | -43.61407 | 2026-09-28 03:47:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f4f745bd-926a-31c1-83a9-7564d0e77a50 | -6.14003 | -44.13297 | 2026-09-28 03:47:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0133cdb9-66ab-3aac-a0a3-69caad476e0e | -5.11818 | -45.76501 | 2026-09-28 03:47:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 953db4ba-2317-3ca2-b47f-30e5fe526c49 | -5.63443 | -43.71916 | 2026-09-28 03:47:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d1726b67-3f3b-3c81-b95d-850addcf2f80 | -3.82014 | -44.08774 | 2026-09-28 03:47:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 71f3b84f-a207-36f4-a8bd-71e01fb771f8 | -5.24202 | -44.93785 | 2026-09-28 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a3f0c96-81b1-3483-b88d-c24fa5115f65 | -3.80819 | -44.0928 | 2026-09-28 03:47:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 854a4c06-964c-3482-926a-7e60d7245bec | -5.73474 | -43.28227 | 2026-09-28 03:47:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| a9ca5a7e-a0a4-3b5c-a2af-de4f13fb2aaa | -5.63954 | -43.72002 | 2026-09-28 03:47:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b82d2245-fb66-3aca-9351-c4d43ef438fa | -7.06903 | -41.73417 | 2026-09-28 03:47:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 24cd32f2-10ed-31d5-b090-85abbc30cf35 | -3.41246 | -48.34897 | 2026-09-28 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 7c0bd56c-d6fe-3d79-b41e-c38041197505 | -5.73064 | -43.28353 | 2026-09-28 03:47:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| a395435a-0687-3be8-b51b-67179535081b | -5.89163 | -42.43679 | 2026-09-28 03:47:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 232aad0d-ca6c-3c41-86fd-e4fd3d386ead | -5.24826 | -44.93505 | 2026-09-28 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4725a4ef-d2ba-3e78-8374-2977e272e282 | -3.81417 | -44.09026 | 2026-09-28 03:47:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b0a2756f-409b-34b7-a933-707db5314e81 | -2.9919 | -47.45595 | 2026-09-28 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d9015bb0-2ea0-31f1-a7dc-94d1cbc6aa6a | -5.89485 | -42.43493 | 2026-09-28 03:47:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 21b59be2-1d4c-3d0f-aad9-2b4fa9b5dfe0 | -3.37548 | -44.37411 | 2026-09-28 03:47:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 642ec2ae-eb09-3475-9fe5-86beb1b62438 | -7.1586 | -39.31682 | 2026-09-28 03:47:00 | NOAA-20 | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 634d32a6-939f-3a64-af3e-36085c66141b | -5.11664 | -45.77369 | 2026-09-28 03:47:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 99da54e2-6d4e-3734-8abe-0a7c8846b907 | -3.37056 | -44.36952 | 2026-09-28 03:47:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 23a7857e-178c-386a-a03c-5769b9387583 | -3.93686 | -42.55308 | 2026-09-28 03:47:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 1f0bd49d-8255-3d47-8f9e-ffc1b3b8f303 | -6.31146 | -43.6087 | 2026-09-28 03:47:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a46aa9dc-d731-303d-b6dc-386a58b1b054 | -6.0027 | -47.39314 | 2026-09-28 03:47:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| f198512d-986b-34dd-a566-67dcaf5e89bf | -4.0819 | -40.51662 | 2026-09-28 03:47:00 | NOAA-20 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 85b04779-2e34-3d19-adf6-1812a34af3f1 | -3.81839 | -44.09806 | 2026-09-28 03:47:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4a062dee-7fc3-3adf-9da7-20abb083035a | -5.89547 | -42.44249 | 2026-09-28 03:47:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| fb2f0e17-47e5-316d-a6db-5f8cafdffd90 | -3.80701 | -44.09969 | 2026-09-28 03:47:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a42ea5b-8923-3587-99a3-d2a48f4dc68e | -6.30553 | -43.61315 | 2026-09-28 03:47:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3a0aa375-622d-32e4-ac72-d03e4a2bf990 | -6.14456 | -44.14088 | 2026-09-28 03:47:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8c07c6d8-51da-3634-acd8-d3dbdecba021 | -3.97903 | -44.51805 | 2026-09-28 03:47:00 | NOAA-20 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README17.md)
