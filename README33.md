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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ec3c6656-a4a0-3da0-9f8b-37f1bcc8be0a | -3.32739 | -46.69925 | 2024-11-29 04:04:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9cc92ac1-dcc3-375f-820a-1c964a938042 | -2.15037 | -50.61182 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb5b363b-1c56-3664-8c58-012927d8fea0 | -5.22258 | -44.91624 | 2024-11-29 04:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 417789b3-097d-3ca1-8768-ff7ee3c5bb23 | -3.71102 | -47.14303 | 2024-11-29 04:04:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 722550f1-c913-3c28-99ef-f170c4f80874 | -4.10453 | -50.98305 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8653e457-0f26-3327-b144-4c3f9096fc9a | -2.85705 | -46.87693 | 2024-11-29 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7a52ff1a-efd8-388b-81a5-806baf49d3ee | -3.67798 | -44.70601 | 2024-11-29 04:04:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b659314-33b3-354b-bcaf-4320614f8d6c | -2.56664 | -49.07964 | 2024-11-29 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d9524139-873f-31ee-8f57-c21f87036d17 | -2.9844 | -51.33448 | 2024-11-29 04:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 85ee5a3b-bc1a-3270-9437-72b27cfded8e | -3.81616 | -44.04848 | 2024-11-29 04:04:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 94c73dab-41cd-373f-9c4d-edd91b7f2cba | -2.83285 | -48.09238 | 2024-11-29 04:04:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 514f1b7b-0fc8-3f31-bac5-58cae5b063b7 | -4.04566 | -48.33308 | 2024-11-29 04:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2e46b4e8-124a-3078-8dde-4f40f2db865b | -3.30605 | -50.7609 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 46d881dc-2c1b-3253-9e9b-32a32b356ae9 | 1.64577 | -50.92329 | 2024-11-29 04:04:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e61bfa9f-4beb-3022-93d6-23e0622349fb | -3.49648 | -50.46516 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c4dd5dd3-359e-35e8-a0fb-3f6d79cf024a | -4.07311 | -47.02982 | 2024-11-29 04:04:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1c9851ff-bcdf-3f40-8f7e-5df6b5fc5618 | -4.26123 | -47.61228 | 2024-11-29 04:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3a94abca-0867-399d-85fc-f3b01b5bd353 | -2.72993 | -48.90127 | 2024-11-29 04:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84d16049-45c4-3a1e-9270-f73dcab9289c | -3.1895 | -50.30356 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04040281-6514-3757-9b2b-1440e53f2a26 | -3.81322 | -44.04374 | 2024-11-29 04:04:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 620d1259-60b7-38e4-9a2b-841b93274bbb | -2.85844 | -45.54448 | 2024-11-29 04:04:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d98078a-683d-38ee-be02-dffda3bc77af | -2.85203 | -46.688 | 2024-11-29 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3129c407-6f13-36b7-8575-cda02502a23a | -3.32804 | -46.69519 | 2024-11-29 04:04:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 264ca138-e211-387b-b55f-5ef462a63183 | -4.20284 | -46.2021 | 2024-11-29 04:04:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a24cdb98-3c28-3500-85c7-254e14e1434f | -3.7795 | -46.68927 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 337d5c5a-7a3a-3029-8843-c90945529fa4 | -3.10531 | -50.36714 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c74b3262-56ce-3b71-ba51-19b2e3abd2ac | -2.85948 | -46.83408 | 2024-11-29 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a7b4a847-833f-391f-9a41-803d56d44935 | -1.52611 | -52.69241 | 2024-11-29 04:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 133d3be2-184f-30a2-84f3-8236ccf18b41 | -2.58546 | -47.48284 | 2024-11-29 04:04:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4ffed6e5-a43d-35aa-a90e-d8053fc03776 | -3.80102 | -44.05034 | 2024-11-29 04:04:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 15a27370-7a8f-3d3a-b952-101bf5911cb3 | -1.79008 | -52.74223 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d3f6742f-77ed-309d-a279-a18c9c156c82 | -5.14963 | -37.74346 | 2024-11-29 04:04:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 78fdae72-ef3d-35d0-8d46-7c6b3040d4fd | -1.96671 | -48.38446 | 2024-11-29 04:04:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 791235e3-bcea-35b8-9ba6-5712c26a18d9 | -5.81176 | -39.54925 | 2024-11-29 04:04:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 96dea4b6-d225-39b5-8033-0851e584172e | -3.16756 | -48.43911 | 2024-11-29 04:04:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8f0bb467-7e04-34e1-bf5f-843491fc35b4 | -1.53704 | -52.66608 | 2024-11-29 04:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4c884cd0-88ee-39f6-8277-98c30320488e | -5.75298 | -46.26609 | 2024-11-29 04:04:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c3a53be9-5f8a-31e4-ab35-4779856718f5 | -4.31651 | -46.04328 | 2024-11-29 04:04:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 23342ac6-ea42-331a-92ff-e200d834a0f5 | -4.21004 | -43.28657 | 2024-11-29 04:04:00 | NOAA-20 | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cc6c0f10-8f2c-3101-a15b-3b2293f817aa | -3.26465 | -50.62822 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 295c5943-ee8f-3c3a-9f6f-3622e95e3418 | -6.35727 | -39.78167 | 2024-11-29 04:04:00 | NOAA-20 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 67767b1f-447d-35f6-a65b-e9c622045d61 | -2.84161 | -46.86146 | 2024-11-29 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 866d6841-9641-3c92-a383-548b5358a1ed | -3.02081 | -54.03036 | 2024-11-29 04:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d97a9a33-82d5-3e5d-aad8-c915fac1b44a | -3.24266 | -50.59903 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56bc796f-41ab-35fa-969b-7cc9009c55a0 | -2.14402 | -50.61485 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b5ba5f02-c496-34e3-b01d-3d9cbd866213 | -2.68006 | -46.28188 | 2024-11-29 04:04:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a0029f9b-52d8-364d-bdb6-3f58e3cd6082 | -3.84934 | -43.93457 | 2024-11-29 04:04:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 106ec56b-4ccc-3b34-a58f-7a94924dd711 | -5.54634 | -41.41115 | 2024-11-29 04:04:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3db8d408-8589-30f3-b0b5-5c170d2576fa | -1.6313 | -53.8719 | 2024-11-29 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e5e1e903-5cf5-35e0-9b1e-4f8a3728e1e4 | -2.33612 | -46.86503 | 2024-11-29 04:04:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 44522335-54be-37af-acd7-2245febb4676 | -3.24515 | -50.61902 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7bae3c54-9831-3f62-9c19-d4507584f267 | -1.14302 | -48.33604 | 2024-11-29 04:04:00 | NOAA-20 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a91b1b1c-a427-35e8-829d-e24652d0b750 | -2.87589 | -46.87132 | 2024-11-29 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c08b712b-8eb0-3b48-977c-4c2d12f78db8 | -4.92238 | -44.52737 | 2024-11-29 04:04:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 09583825-173e-3c0a-adcd-8970cf22ca31 | -4.66096 | -44.064 | 2024-11-29 04:04:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5186a5c7-7718-3199-bf74-f209b83a8527 | -2.87656 | -46.86715 | 2024-11-29 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ba8a9fe-7094-364e-9ab3-ef6946ad24da | -3.70456 | -50.43838 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76a04427-bc1e-3b94-a686-a6dbbc06ec6b | -2.863 | -45.54163 | 2024-11-29 04:04:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 11a18dd3-f8a8-3d86-a27b-a2b744e6c973 | -4.04427 | -48.33555 | 2024-11-29 04:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| edd9b21d-b54a-32e4-bea6-c5846f667eeb | -3.18583 | -46.6062 | 2024-11-29 04:04:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ac34b61d-ca59-3be4-9486-529e2943b4ef | -1.7042 | -45.83009 | 2024-11-29 04:04:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8ac6c79f-6001-32b2-abc1-6da299249f17 | -2.83201 | -48.09752 | 2024-11-29 04:04:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5bb84f7c-eea1-3b07-af79-531b050aded8 | -3.79642 | -46.68686 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ed0f4af2-7299-3f9a-beb0-651a7da20aa3 | -3.70713 | -47.13981 | 2024-11-29 04:04:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 37c78fe9-817b-31b4-98c2-50cc65fb07ee | -4.66557 | -45.95707 | 2024-11-29 04:04:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e5fd2ff3-2c83-3b76-8b75-0c423249ec6b | -1.65783 | -52.73579 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f6d0d93d-9420-3910-9a34-dec8acfea8cd | -4.06946 | -46.68893 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a4c82fbf-6dfa-3abb-a581-82fc0b8b7751 | -1.71433 | -52.63713 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 87ebe009-81c5-3f0c-b5a9-0db3d3797e10 | -3.66861 | -54.4569 | 2024-11-29 04:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9f2ed536-891f-3f85-8170-c71b1a58e469 | -2.97731 | -53.28611 | 2024-11-29 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 0d414137-4de2-3899-a5be-0df14629d854 | -2.02707 | -53.50134 | 2024-11-29 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 594f781e-fab3-35e6-8205-cdb8cf6acf3e | -2.22418 | -46.31253 | 2024-11-29 04:04:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ba5965fe-f1f5-334f-8e58-8c33b514d539 | -2.66229 | -48.78088 | 2024-11-29 04:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6a849fcb-8e3a-3e1d-a352-152742bc8265 | -3.16145 | -51.09436 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4737304c-bc33-308e-b223-2bfa2a28698b | -3.28477 | -42.3322 | 2024-11-29 04:04:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c4c6b8c8-a862-3c71-992c-cc5aa9460c82 | -4.46821 | -46.31654 | 2024-11-29 04:04:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe0428b9-ad75-3426-8751-1367592e830b | -4.83136 | -41.24874 | 2024-11-29 04:04:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 069e2d2e-985a-31b3-86d0-5571ca79f0e8 | -1.91955 | -52.89172 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 615e0269-e915-3262-8722-59df2ab51333 | -2.65587 | -48.78878 | 2024-11-29 04:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 37adec34-baab-3147-8be9-ce23c775d087 | -3.6698 | -54.45021 | 2024-11-29 04:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 281b22a2-aa5c-32af-962c-adde33bdba1f | -3.68954 | -47.13708 | 2024-11-29 04:04:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| abd02465-3c5f-3caf-9248-59597ceb779c | -0.26421 | -51.62981 | 2024-11-29 04:04:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 03bff833-9b85-3edc-932c-dce636275fbd | -5.97665 | -45.35764 | 2024-11-29 04:04:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 53bf2ff1-a2ad-38b4-baf1-27e6de7bd908 | -2.64429 | -47.12787 | 2024-11-29 04:04:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| ff7951e2-7adf-3f25-81c3-e677e961bf11 | -2.60192 | -46.83871 | 2024-11-29 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c4f16117-750a-3204-8e58-563aa1526574 | -4.86776 | -41.27562 | 2024-11-29 04:04:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| c8bf6bde-c26e-366f-84d4-16363ec0ee10 | -3.98023 | -46.98989 | 2024-11-29 04:04:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c561ea96-cf8f-38d6-94bd-d3232de71ceb | 0.94234 | -50.7485 | 2024-11-29 04:04:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 39fb3991-6a45-3cca-a642-b924bc7b921e | -5.89392 | -35.41812 | 2024-11-29 04:04:00 | NOAA-20 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ba93d477-042b-3d70-a214-15884ab51806 | -5.40428 | -41.55855 | 2024-11-29 04:04:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 73aab30f-915d-3882-981b-6e8c35a3daa3 | -3.28338 | -50.61974 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a238be2d-8691-3216-abc3-fca1208769e4 | -3.68245 | -44.70209 | 2024-11-29 04:04:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cd540baf-339f-3abc-8a92-6f10f50cc7a6 | -5.46811 | -46.14399 | 2024-11-29 04:04:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c489786-aceb-373c-b9eb-c9c5b174a159 | -4.67642 | -42.38007 | 2024-11-29 04:04:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 197c7a0e-64d3-3f9a-ab52-dcde6a9da4bf | -4.0713 | -50.03784 | 2024-11-29 04:04:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 60bbb292-ca37-3e33-8492-5c6edbaa2090 | -3.57477 | -50.33445 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| aedfb3a0-ccd7-3db8-8faf-617d9ee7cfae | -5.44848 | -46.33963 | 2024-11-29 04:04:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| af83b605-c191-33e8-9cee-556c96a4791f | -2.0626 | -46.37799 | 2024-11-29 04:04:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1bb6b076-2630-3bea-9a1a-49775c34aaed | -3.96957 | -47.2438 | 2024-11-29 04:04:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8de08b56-95d5-304e-8d5f-83d5b00b4b90 | -6.46066 | -39.29202 | 2024-11-29 04:04:00 | NOAA-20 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |


[Clique aqui para ver as próximas entradas](README34.md)
