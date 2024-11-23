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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7f8f0616-bfb0-3ed9-a7f3-0299ff37530a | -3.3336 | -42.09396 | 2024-11-23 12:29:00 | TERRA_M-T | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| cf18c67b-9c8d-3423-809b-5939c3d038d9 | -5.4698 | -43.21965 | 2024-11-23 12:29:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 1da7d2c1-6bab-3133-8300-cc2d4bcd3f72 | -4.54522 | -42.91098 | 2024-11-23 12:29:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 6ab7bfdd-5dfd-30e8-b665-812db1308225 | -4.34322 | -41.87615 | 2024-11-23 12:29:00 | TERRA_M-T | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 466bfd7e-c407-3fce-85a1-a7fc3bc31ef9 | -3.38137 | -42.02226 | 2024-11-23 12:29:00 | TERRA_M-T | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 386.9 |
| e3792073-e41b-333f-b7de-f6561f277f2f | -3.64918 | -42.40385 | 2024-11-23 12:29:00 | TERRA_M-T | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 29.5 |
| d25557f1-03b1-30ae-a2ee-68fa8c05e911 | -3.56646 | -42.14829 | 2024-11-23 12:29:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| fe5b4f8a-bf35-34bf-8147-82f8189a76f5 | -3.67578 | -44.90836 | 2024-11-23 12:29:00 | TERRA_M-T | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 180cd14b-b5c3-376b-bae3-854b800e1bd3 | -4.12094 | -43.23289 | 2024-11-23 12:29:00 | TERRA_M-T | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| b295b2d1-2496-3ff0-b29c-e55a3565021e | -3.46958 | -40.8275 | 2024-11-23 12:29:00 | TERRA_M-T | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 45676ca5-da77-3b64-8783-892c0ea45b63 | -5.11026 | -43.15395 | 2024-11-23 12:29:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 8420b637-67c3-3b2b-b907-5731610c4adc | -5.25155 | -43.00246 | 2024-11-23 12:29:00 | TERRA_M-T | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 50fd6623-cb05-308a-bc09-51b20374225e | -4.28917 | -43.73642 | 2024-11-23 12:29:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 7b040236-3d52-31ab-864e-d903eb59e3f4 | -3.9084 | -46.52832 | 2024-11-23 12:29:00 | TERRA_M-T | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 0c7372ec-332d-3421-9762-7c8650fd7916 | -3.23327 | -41.56696 | 2024-11-23 12:29:00 | TERRA_M-T | BOM PRINCÍPIO DO PIAUÍ | PIAUÍ | Brasil | 2201919 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 315c2cc4-8d91-36c4-b96c-5049841af591 | -2.96894 | -44.94355 | 2024-11-23 12:29:00 | TERRA_M-T | SÃO JOÃO BATISTA | MARANHÃO | Brasil | 2111003 | 21 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 6a9cd90a-fba7-3bc2-9513-2646e3d29fb7 | -3.55357 | -42.10745 | 2024-11-23 12:29:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 60061532-fbfa-3b75-b0de-f368bda9a590 | -5.45464 | -42.14997 | 2024-11-23 12:29:00 | TERRA_M-T | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 27.9 |
| 89697236-ccb5-31f7-89af-ba736450d685 | -3.71481 | -42.65599 | 2024-11-23 12:29:00 | TERRA_M-T | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Cerrado | 74.2 |
| fb74202c-8f85-33e2-80a8-0e5e74f9f18e | -3.74696 | -42.17595 | 2024-11-23 12:29:00 | TERRA_M-T | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 71.1 |
| 4dd8b276-c853-345a-a92f-0980f88bdfa1 | -1.9989 | -46.27568 | 2024-11-23 12:29:00 | TERRA_M-T | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 0e971a42-b06c-36da-9c04-b0b13aa121d5 | -3.19075 | -41.93398 | 2024-11-23 12:29:00 | TERRA_M-T | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 46.1 |
| e0012b76-8893-3828-ae97-d28ff78a51bc | -4.52985 | -42.8901 | 2024-11-23 12:29:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 4889baf0-5917-3cba-b6de-19be52f9bc94 | -3.65183 | -42.38514 | 2024-11-23 12:29:00 | TERRA_M-T | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 15.0 |
| a9dcf2ca-e5a4-3392-91de-c838b62e6c3f | -2.95432 | -43.7699 | 2024-11-23 12:29:00 | TERRA_M-T | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 9f560b52-4ee2-34ef-b1a7-1383adb9f43a | -3.51504 | -46.39862 | 2024-11-23 12:29:00 | TERRA_M-T | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 4c8b3f7c-aec7-3a63-8c8a-f292238272aa | -3.7745 | -45.6216 | 2024-11-23 12:29:00 | TERRA_M-T | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 002585c8-9102-309b-b2aa-6d091a1bb2af | -3.47073 | -43.32596 | 2024-11-23 12:29:00 | TERRA_M-T | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 32a86de4-f6f8-34b3-adfc-c68bcfe46255 | -3.79045 | -42.18843 | 2024-11-23 12:29:00 | TERRA_M-T | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 116.9 |
| 8b41c9aa-cd0b-3854-9d84-dc633949caad | -4.58833 | -43.70664 | 2024-11-23 12:29:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 9f9f6f22-20a6-3868-b2c3-d29c5750f96a | -3.68235 | -42.23516 | 2024-11-23 12:29:00 | TERRA_M-T | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 164.6 |
| 35cae226-eace-32b2-8a22-5bc8d4d812c6 | -3.19572 | -41.76527 | 2024-11-23 12:29:00 | TERRA_M-T | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 0aad4506-91bf-3862-a814-c4b8027c3f22 | -2.97384 | -40.86366 | 2024-11-23 12:29:00 | TERRA_M-T | CAMOCIM | CEARÁ | Brasil | 2302602 | 23 | 33 | nan | nan | nan | Caatinga | 7.1 |
| ebbc1a41-317c-394e-916e-8b15c7f1420c | -2.42292 | -46.03217 | 2024-11-23 12:29:00 | TERRA_M-T | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 5b08d9bc-f736-3f24-a5c5-1291240076c4 | -3.44335 | -41.45268 | 2024-11-23 12:29:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 18.1 |
| fe1528ad-975c-3576-9c3f-d8975a553371 | -4.09346 | -42.0013 | 2024-11-23 12:29:00 | TERRA_M-T | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 19.2 |
| ce931171-702d-3e83-9b5d-98290fbba864 | -4.48055 | -48.11436 | 2024-11-23 12:29:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| f76f5cb9-9d2d-33b3-8487-07a3c43e21c1 | -3.4975 | -53.8137 | 2024-11-23 12:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 4d770dbc-738d-302a-8c1d-391779eba4fb | -3.5922 | -42.0632 | 2024-11-23 12:30:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 80.4 |
| a9e190c6-53e6-3638-8142-ecc154bbe2d8 | -3.5921 | -42.0869 | 2024-11-23 12:30:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 262.8 |
| 8956de04-12fd-3895-b039-91f0b9c6a733 | -4.5216 | -42.9078 | 2024-11-23 12:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 243.1 |
| 3bb4759b-69ac-35d3-a534-ed0c6ca3fbb3 | -4.2606 | -48.6755 | 2024-11-23 12:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 273.0 |
| 7f5fad99-7159-3f90-8440-d907d149342d | -4.242 | -48.6978 | 2024-11-23 12:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 79c89831-3171-3149-906d-e3e2a6607dd9 | 1.2428 | -50.7264 | 2024-11-23 12:30:00 | GOES-16 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 53a12e9e-8e30-3821-b8a2-f0088f8e7799 | -4.6083 | -46.5223 | 2024-11-23 12:30:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 34ecb3a8-aa17-382b-adbf-536d8831a808 | -4.2605 | -48.697 | 2024-11-23 12:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 466.7 |
| 51c89a90-dfb8-3ac8-a15f-88897884c6cb | -6.52561 | -38.09619 | 2024-11-23 12:31:00 | TERRA_M-T | SANTA CRUZ | PARAÍBA | Brasil | 2513208 | 25 | 33 | nan | nan | nan | Caatinga | 15.9 |
| 1fe42644-3613-334c-8a30-375f768a60f4 | -7.38181 | -39.98371 | 2024-11-23 12:31:00 | TERRA_M-T | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 22.4 |
| 10cdf0d8-c21a-3fe0-a959-27316029766d | -9.83001 | -37.0216 | 2024-11-23 12:31:00 | TERRA_M-T | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 63.6 |
| 4012acbd-a5ba-3ff4-a709-4d953a1d315b | -5.36644 | -47.74689 | 2024-11-23 12:31:00 | TERRA_M-T | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |
| a505880d-e8e0-36e7-a3ad-32d20c36e777 | -6.08549 | -44.01334 | 2024-11-23 12:31:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 9d01f3ef-a0b6-3e25-9730-40c5d656c339 | -7.82124 | -44.19352 | 2024-11-23 12:31:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 16.1 |
| e0cc072f-c5aa-34c0-98fa-7c19e339c836 | -6.18301 | -45.17595 | 2024-11-23 12:31:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 6cef9a6e-41e4-33a3-86c7-525d58e8cc04 | -7.3799 | -39.9984 | 2024-11-23 12:31:00 | TERRA_M-T | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 10.7 |
| f4bf5f47-4ee2-384b-af85-a2cbb2d04aef | -6.06039 | -44.04849 | 2024-11-23 12:31:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| e2f92a88-c2f3-323a-94bb-a66ae3d23791 | -5.93431 | -43.78027 | 2024-11-23 12:31:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 118dc9cb-8bdb-3150-b447-52197fff1d0e | -7.14649 | -41.75635 | 2024-11-23 12:31:00 | TERRA_M-T | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 17.9 |
| d71d7c96-40f9-36e5-840b-c0d20778ef6d | -8.18583 | -39.61706 | 2024-11-23 12:31:00 | TERRA_M-T | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 16.2 |
| f161b8d3-57a4-31c8-9e39-6e4f40051974 | -6.5238 | -38.11025 | 2024-11-23 12:31:00 | TERRA_M-T | SANTA CRUZ | PARAÍBA | Brasil | 2513208 | 25 | 33 | nan | nan | nan | Caatinga | 18.7 |
| 3ba17a30-6b7e-34dc-8017-50b497311860 | -9.19847 | -44.42581 | 2024-11-23 12:31:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7ce273a5-b6c5-3ef7-829d-c1dcbcaf7565 | -7.54619 | -41.14536 | 2024-11-23 12:31:00 | TERRA_M-T | MASSAPÊ DO PIAUÍ | PIAUÍ | Brasil | 2206050 | 22 | 33 | nan | nan | nan | Caatinga | 25.8 |
| 732716a5-9a84-3719-9e00-7b0bfb64f69a | -7.39107 | -39.99986 | 2024-11-23 12:31:00 | TERRA_M-T | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 29.9 |
| 2bcfba05-aa4b-3273-9f46-396e05441925 | -7.68852 | -42.98228 | 2024-11-23 12:31:00 | TERRA_M-T | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| b0eb5b63-3cfd-3847-8622-bf84066e1e2f | -7.90312 | -37.24956 | 2024-11-23 12:31:00 | TERRA_M-T | MONTEIRO | PARAÍBA | Brasil | 2509701 | 25 | 33 | nan | nan | nan | Caatinga | 139.3 |
| 53e4ab14-83fe-33d1-ab30-e93312ed2cf4 | -5.62451 | -43.42904 | 2024-11-23 12:31:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 7522320a-2edb-347f-9338-1c56245ef977 | -6.54842 | -41.71078 | 2024-11-23 12:31:00 | TERRA_M-T | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 88429781-ddff-34d9-83e6-572cf17a06f6 | -8.93774 | -44.25073 | 2024-11-23 12:31:00 | TERRA_M-T | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 3ca07fe7-be0a-3f6b-b4b2-fd142b52a254 | -7.81237 | -44.19227 | 2024-11-23 12:31:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 1a54ef14-1047-3ffe-b989-5bdaf0f523a3 | -5.53727 | -42.9381 | 2024-11-23 12:31:00 | TERRA_M-T | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 968f9203-f246-3edb-9f24-1b0177d9563b | -9.83027 | -37.02727 | 2024-11-23 12:31:00 | TERRA_M-T | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 46.2 |
| dfbb9af9-be72-3079-ba54-03ea521aad48 | -7.39299 | -39.98517 | 2024-11-23 12:31:00 | TERRA_M-T | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 45.3 |
| 456378cf-c7c2-3220-bbbc-3d4ee84f87ba | -6.22325 | -43.94805 | 2024-11-23 12:31:00 | TERRA_M-T | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| cd6b030c-0d13-3520-b2b4-0dfd5c75f571 | -7.69786 | -37.36589 | 2024-11-23 12:31:00 | TERRA_M-T | INGAZEIRA | PERNAMBUCO | Brasil | 2607109 | 26 | 33 | nan | nan | nan | Caatinga | 35.8 |
| f669707b-24c5-3a6e-98d8-fc41b592ab70 | -7.37992 | -39.99181 | 2024-11-23 12:31:00 | TERRA_M-T | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 17.2 |
| d79af4c8-5ad5-3f57-9a48-30de3f3f9d8d | -11.03347 | -44.68076 | 2024-11-23 12:31:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 906c4c7a-0dd5-31cc-91aa-c9bbf7887379 | -8.04993 | -39.95854 | 2024-11-23 12:31:00 | TERRA_M-T | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 17.0 |
| 2b2988bd-d5f0-3372-9aa0-d61437e4e7cd | -7.8964 | -37.23055 | 2024-11-23 12:31:00 | TERRA_M-T | MONTEIRO | PARAÍBA | Brasil | 2509701 | 25 | 33 | nan | nan | nan | Caatinga | 46.4 |
| 7339bb66-a6b3-36f5-a5e0-daf896681f38 | -6.35941 | -42.92614 | 2024-11-23 12:31:00 | TERRA_M-T | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 11.3 |
| eecea6a5-5898-3cf5-a91d-1eff60dbfdf7 | -6.21439 | -43.94681 | 2024-11-23 12:31:00 | TERRA_M-T | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7378caeb-4031-3b38-b4e3-dfd3f443fa8a | -7.695 | -37.38949 | 2024-11-23 12:31:00 | TERRA_M-T | INGAZEIRA | PERNAMBUCO | Brasil | 2607109 | 26 | 33 | nan | nan | nan | Caatinga | 111.5 |
| 737d69a0-c28e-3114-8cb1-f1c7e4261093 | -7.82251 | -44.18455 | 2024-11-23 12:31:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 8a2a3e9a-affb-3710-9a98-42627fadeab2 | -7.68939 | -37.38211 | 2024-11-23 12:31:00 | TERRA_M-T | INGAZEIRA | PERNAMBUCO | Brasil | 2607109 | 26 | 33 | nan | nan | nan | Caatinga | 141.7 |
| c901d67a-7402-3134-b12b-22fe422ad28e | -7.81364 | -44.18332 | 2024-11-23 12:31:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 9fbd7545-a125-3df0-b6e6-c3f88b62bcdb | -7.8934 | -37.25548 | 2024-11-23 12:31:00 | TERRA_M-T | MONTEIRO | PARAÍBA | Brasil | 2509701 | 25 | 33 | nan | nan | nan | Caatinga | 74.6 |
| 88f94dc2-2db1-3152-a563-d75c94f545cd | -6.21723 | -43.27965 | 2024-11-23 12:31:00 | TERRA_M-T | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 82132d5e-9f3e-3429-acf7-b26f58a7d7b9 | -6.01232 | -43.03461 | 2024-11-23 12:31:00 | TERRA_M-T | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 534a0cdd-da36-32b7-bfa8-ea4c4f91f73d | -5.29694 | -44.86061 | 2024-11-23 12:31:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 2d7397dd-d944-3332-97c3-c84aff6dea96 | -7.94229 | -37.60504 | 2024-11-23 12:31:00 | TERRA_M-T | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 52.0 |
| 34eb1a70-2898-3b8d-aee4-aa680fa1227f | -29.8883 | -52.05685 | 2024-11-23 12:38:00 | TERRA_M-T | VALE VERDE | RIO GRANDE DO SUL | Brasil | 4322525 | 43 | 33 | nan | nan | nan | Pampa | 6.6 |
| f73dc64a-253d-39a1-8fc4-000cb824a037 | -4.2606 | -48.6755 | 2024-11-23 12:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 258.8 |
| 2fb54975-9905-398d-8c0f-4ea6299e1959 | -1.6245 | -53.3084 | 2024-11-23 12:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 92768de5-304e-36a7-9ffc-ca3b99188f06 | -3.6659 | -42.2492 | 2024-11-23 12:40:00 | GOES-16 | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 88.3 |
| c9e04a40-673a-3ac0-bc2a-096ab0fa48fa | -4.242 | -48.6978 | 2024-11-23 12:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 4f9d80b0-f559-3bbf-b388-ef218c043129 | -5.4548 | -43.2426 | 2024-11-23 12:40:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| a7b870f5-b940-3d0a-ad80-e152370356e0 | -1.5493 | -54.3357 | 2024-11-23 12:40:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| ea2dc245-0e29-322a-9259-89d5ed2bb2ce | -5.4738 | -43.2178 | 2024-11-23 12:40:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 0dd952d2-0598-3a44-aee9-f2a33dd3f04e | -3.5921 | -42.0869 | 2024-11-23 12:40:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 147.7 |
| 5c872a77-1e0d-33be-86df-b87eb0a2368f | -3.4975 | -53.8137 | 2024-11-23 12:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 348f0792-4a52-35c7-ad1c-1765b7fa123a | -1.5493 | -54.3357 | 2024-11-23 12:50:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| bd32d480-b164-382e-be69-7e35a33198a9 | -3.5159 | -53.8132 | 2024-11-23 12:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |


[Clique aqui para ver as próximas entradas](README71.md)
