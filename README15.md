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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c612b54c-2c2c-3f46-93e8-ad71a0c44b45 | -3.17583 | -53.96075 | 2024-12-22 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 735cb687-01d9-3e90-a08a-9b7c24a3fbbb | -2.67485 | -46.93453 | 2024-12-22 04:50:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5fabc24a-e613-3522-9af3-addbd6f0bc89 | -1.15373 | -53.59805 | 2024-12-22 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 48a2b512-6032-34e3-a786-4d4542ca9b51 | -1.09289 | -53.66934 | 2024-12-22 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42ea597a-57ff-3164-815b-143f9b4160ca | -3.78287 | -47.11489 | 2024-12-22 04:50:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 46c35c0c-3afa-3920-b376-2a78ae5cf49d | -4.32665 | -47.77903 | 2024-12-22 04:50:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 88a3969e-9a3e-351f-a0fa-0c909d4dfb7b | -3.65354 | -53.44022 | 2024-12-22 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45af28cc-fd17-3790-9187-942c568aba6e | -2.50624 | -49.06363 | 2024-12-22 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f78b3a4d-d93a-3206-84a1-f25f4bcd5bf2 | -2.49493 | -49.06597 | 2024-12-22 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3aeac370-f8d1-344a-a099-8bdcf988facd | -2.50372 | -51.82794 | 2024-12-22 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 047201d3-23f2-3e4e-a9aa-4fc8a3337097 | -2.57091 | -49.45739 | 2024-12-22 04:50:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 84a455c2-3092-3d8e-89ba-6c2eb84868c8 | -2.56755 | -49.45396 | 2024-12-22 04:50:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 47e231f2-fcf2-30c1-a7e0-b5b746839485 | 0.64315 | -60.3042 | 2024-12-22 04:50:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.3 |
| db37a766-f29b-327e-8e64-950c97c8f163 | -2.58142 | -49.459 | 2024-12-22 04:50:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 871ab46c-87bb-3b22-8893-0ec9f2440f0e | -2.63265 | -48.03847 | 2024-12-22 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 37eae664-391f-3a6b-bf92-1eea4c6fe956 | -0.92737 | -47.62086 | 2024-12-22 04:50:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 77fdf5e8-9e58-3a20-b9b1-4ad8f3236840 | -2.56273 | -49.46405 | 2024-12-22 04:50:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 755d6689-1735-31d4-909d-5d30b5363398 | -2.58023 | -49.46672 | 2024-12-22 04:50:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a54401f9-08a7-345f-92ef-c93e9e674a65 | -4.03542 | -50.05186 | 2024-12-22 04:50:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f603030b-33f7-379a-be7e-3b038dfd7503 | -2.44495 | -51.79051 | 2024-12-22 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cff81780-262f-3b13-b03e-107e138398c2 | -3.31904 | -44.1528 | 2024-12-22 04:50:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c30e3fb3-0d66-3059-9dc5-22ce2f4d4a75 | -3.92114 | -46.9158 | 2024-12-22 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 77307c92-992d-3843-968f-18a5d86188f6 | -3.07021 | -52.84768 | 2024-12-22 04:50:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 18adf757-760b-310d-b670-2ec21ec3e731 | -4.01656 | -47.05161 | 2024-12-22 04:50:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2c017281-f246-3121-a8a1-5424c8706b3e | -4.01601 | -47.05516 | 2024-12-22 04:50:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1dce7f07-efab-37de-9694-6671633e606c | -2.56332 | -49.46018 | 2024-12-22 04:50:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00160eb5-2264-3073-b52d-f99241301c0d | -3.0877 | -46.56635 | 2024-12-22 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 713f0fa6-68a6-3eb3-9f07-cc9c731fbb67 | -3.54796 | -51.0795 | 2024-12-22 04:50:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 295726a1-74b7-3e3c-a8b5-e3597b7cf312 | -4.08237 | -46.79909 | 2024-12-22 04:50:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 646e651c-d1c6-3704-922c-5aa3e2472152 | -2.22342 | -46.49928 | 2024-12-22 04:50:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73b30a95-991d-334a-8611-9f98ceca840d | -1.3681 | -53.69228 | 2024-12-22 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1f45e7ac-89ba-3b2e-8726-5defd8e258f0 | -1.30075 | -52.82192 | 2024-12-22 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5ab0e0e6-c41e-3876-949b-3f73bb4583fd | -4.07864 | -48.20863 | 2024-12-22 04:50:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f8fc4bd5-c1ad-33ee-b8a9-fca2b4ee8440 | -3.75075 | -47.18922 | 2024-12-22 04:50:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5becab05-d56a-3d28-aca2-4916175e25bc | -2.97814 | -48.07507 | 2024-12-22 04:50:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 15828053-de10-3a8e-9cda-aa2c54d1fb1a | -3.90882 | -46.99553 | 2024-12-22 04:50:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1e102e8c-24be-35f9-8664-be6c19414d78 | -4.09973 | -46.73974 | 2024-12-22 04:50:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5d63d47b-6aac-340a-aaf9-61f2e26db030 | -2.77344 | -54.35506 | 2024-12-22 04:50:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| fd514fae-acac-342b-94e6-6f154c3e98c2 | -3.76525 | -47.20206 | 2024-12-22 04:50:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a81c289e-95d4-3db4-b567-7712767790af | -1.10061 | -54.16879 | 2024-12-22 04:50:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 63a3987c-f2c6-32c9-bf6c-3e000ff78e31 | -2.05347 | -45.48086 | 2024-12-22 04:50:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 12.2 |
| a2c783b4-565e-3caa-a310-60bf0d829c39 | -1.2914 | -53.09975 | 2024-12-22 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6484ab2-e259-3d55-b2e8-435455652f9c | -1.93882 | -45.64022 | 2024-12-22 04:50:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea5ebaf4-2cb0-3565-bc3e-55d23e077371 | -1.72279 | -52.57591 | 2024-12-22 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b496e19d-3be0-3ee2-afb6-e99e71affa57 | -2.80271 | -46.7458 | 2024-12-22 04:50:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e4b28d8-2b2a-3a07-b1f5-609e87802034 | -2.51125 | -47.50481 | 2024-12-22 04:50:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 02050940-3a71-3f18-9f97-4cfd900e6b7a | -3.38019 | -52.81002 | 2024-12-22 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5f728f9f-890e-363d-ac91-21ce4c29920a | -2.57495 | -49.47775 | 2024-12-22 04:50:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b715e85f-fbf9-3a95-830d-4a57838d938b | -1.36463 | -53.69175 | 2024-12-22 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 39da46f7-1c3a-37c6-bf27-148baf5360dd | -1.81603 | -54.06887 | 2024-12-22 04:50:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 04612a5f-803c-3d53-aed4-f60727628992 | -9.79883 | -47.97451 | 2024-12-22 04:53:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 32966da4-43e8-3f3b-8b73-c0ead2a62bda | -12.34372 | -43.67604 | 2024-12-22 04:53:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 42b0dbac-e2f7-37a4-bd8a-8eb283d48b08 | -11.15356 | -49.69368 | 2024-12-22 04:53:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 85c92af8-73d5-3c48-9a23-64d17b1c8c57 | -4.97111 | -50.8361 | 2024-12-22 04:53:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1c354545-fb76-322a-8afd-c19a23d46000 | -12.44385 | -41.44669 | 2024-12-22 04:53:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6bf87048-416d-34b5-ae81-e74e08e00f42 | -12.33164 | -43.67881 | 2024-12-22 04:53:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 905d0710-59ae-33e1-b4a2-a0ce0749bca5 | -12.43487 | -41.43788 | 2024-12-22 04:53:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 86139e31-64c5-3945-9c2e-2e883683bae7 | -12.4413 | -41.44061 | 2024-12-22 04:53:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 9a930065-56f4-3c93-8c4a-24a266fd4355 | -8.79902 | -49.79639 | 2024-12-22 04:53:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 26239cf4-0a6f-3b46-af58-b86238109ba5 | -6.16139 | -46.08833 | 2024-12-22 04:53:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1a5505c9-0e67-3429-ab0e-66def50ac887 | -11.79006 | -49.31518 | 2024-12-22 04:53:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2bee5a08-a701-3812-9817-f669043b9ee5 | -11.15738 | -49.69423 | 2024-12-22 04:53:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9703e79c-457d-3e29-ad1c-b9c28deb67d1 | -12.4487 | -41.43497 | 2024-12-22 04:53:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6a0b9ebf-5244-3b1d-ba73-56e9662c4d7c | -12.43796 | -41.43882 | 2024-12-22 04:53:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 457af909-9f7a-3e91-9547-7957f7f65710 | -3.94796 | -54.63304 | 2024-12-22 04:53:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f5f12134-8fbd-3f77-bc94-fdcd6bb8aa03 | -8.93771 | -44.2438 | 2024-12-22 04:53:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 51d1bffe-9c39-36ed-95c6-53b8f28a63df | -9.11596 | -49.49509 | 2024-12-22 04:53:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c776f37b-beed-323d-ad72-d6f52a26bb4b | -12.33793 | -43.67536 | 2024-12-22 04:53:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1b689bbf-71dc-3379-9404-c0dc4f5bda84 | -12.4373 | -41.44489 | 2024-12-22 04:53:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| cad1e12a-ee74-3d7c-9eea-888be3485148 | -12.44532 | -41.43322 | 2024-12-22 04:53:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| ddbb6e11-151d-3611-9d9e-0bd5873e39e0 | -6.00291 | -45.40736 | 2024-12-22 04:53:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6547e51e-5251-3511-9ec3-89bc4cb3d845 | -4.36767 | -50.72212 | 2024-12-22 04:53:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c84028bd-1d14-36ff-9988-ce642d27ffe3 | -12.44456 | -41.44017 | 2024-12-22 04:53:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 215afa5c-1262-3df1-b6b8-81b8d3d315fa | -10.57028 | -44.6104 | 2024-12-22 04:53:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9fce2303-6bac-3438-8dc3-196be5b93587 | -12.4406 | -41.44659 | 2024-12-22 04:53:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| dcea624a-98d6-393a-8627-c9ad949e0a83 | -11.15287 | -49.69842 | 2024-12-22 04:53:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 10a07850-d4f0-3ab8-9fea-46e3e25dd1a3 | -6.00218 | -45.41248 | 2024-12-22 04:53:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 70712e21-9b07-3745-8909-8a7e579a0ddb | -3.59014 | -55.43704 | 2024-12-22 04:53:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8cc74c3e-2fad-3e0c-b1d7-6302af72e15d | -11.15543 | -49.69583 | 2024-12-22 04:53:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8eb95957-843b-3007-aaf9-59fcc5e4d84c | -12.33743 | -43.67953 | 2024-12-22 04:53:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 312da504-86b7-328a-8834-c91fb6d09f77 | -12.44212 | -41.43346 | 2024-12-22 04:53:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 16d0a368-38bf-33b6-96d8-84772c7a1030 | -8.93728 | -44.24706 | 2024-12-22 04:53:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a7e1ee5e-411d-3ca2-ba30-c4130343050b | -9.11289 | -49.48991 | 2024-12-22 04:53:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4c85a21e-cad8-33c3-ac3c-3673f61fd6cb | -13.39828 | -42.31694 | 2024-12-22 04:55:00 | NPP-375D | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 98b4f24f-0431-3fb5-b608-9e0eb14d5b8d | -13.39772 | -42.32205 | 2024-12-22 04:55:00 | NPP-375D | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f33f8675-6ee2-3ddb-b0a6-887a8d3bad9d | -13.40355 | -42.31757 | 2024-12-22 04:55:00 | NPP-375D | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 29a8be82-cdfb-3a07-a49e-b3e0613ef59b | -13.40467 | -42.31763 | 2024-12-22 04:55:00 | NPP-375D | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2c2c8007-cfcd-3263-8f3d-a42ac65b02fd | -13.40411 | -42.3228 | 2024-12-22 04:55:00 | NPP-375D | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cc2fa077-6982-3ef8-9e8a-6e34feef0bfb | -13.39716 | -42.31689 | 2024-12-22 04:55:00 | NPP-375D | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 421160e0-d69f-3cea-b812-929c9e6919b5 | -13.40295 | -42.32272 | 2024-12-22 04:55:00 | NPP-375D | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b7f561bd-5fee-32c1-93d6-f5caffb8a0b4 | -13.39657 | -42.32199 | 2024-12-22 04:55:00 | NPP-375D | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 12eedf2f-6ba9-39ee-b6eb-6b76b7352391 | 0.98392 | -59.53261 | 2024-12-22 05:12:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bcd7ef2b-e362-30ef-b9be-59e358d84145 | 4.20562 | -60.6134 | 2024-12-22 05:12:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4f144f27-2355-31fc-afb2-1bd6f9ca5ec3 | 0.00335 | -51.19734 | 2024-12-22 05:12:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 7.6 |
| e8418f6d-5715-301e-a2bd-7d07205318fd | 1.93667 | -60.66525 | 2024-12-22 05:12:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bfe969a9-2b01-3d52-b98f-7fe1d466635a | 4.20181 | -60.61398 | 2024-12-22 05:12:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6c634fe7-28f9-305f-94ac-beeea67eb7c6 | 0.93352 | -50.78206 | 2024-12-22 05:12:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9444968f-e56c-366b-b7ce-a05e349cb0ff | 0.8987 | -59.54516 | 2024-12-22 05:12:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 49819cb2-efc1-3fdc-8289-7e793413a0d0 | 0.8981 | -59.54135 | 2024-12-22 05:12:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 90f369d4-a49f-39db-a21f-46eeffcf8a6a | 1.10921 | -59.59261 | 2024-12-22 05:12:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README16.md)
