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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e017ebfc-e272-3fb4-af91-e1e45bf61297 | -6.5481 | -39.326 | 2025-12-11 03:00:00 | GOES-19 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 105.3 |
| aa3b5761-8a7b-3a21-a345-bb2932922590 | -10.56287 | -36.785 | 2025-12-11 03:00:00 | NOAA-20 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| e250b040-4229-31ab-97a9-dbbbb807afcf | -6.5481 | -39.326 | 2025-12-11 03:10:00 | GOES-19 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 83.8 |
| 4e50c330-caa6-3e79-a127-20738b432b3b | -1.8067 | -54.0516 | 2025-12-11 03:10:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| d40e8c9d-becc-3bbf-95c2-f694fad9acd0 | -6.0315 | -43.7105 | 2025-12-11 03:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| efb6014f-ee90-3b31-a435-49285c30fd6a | -3.229 | -47.4629 | 2025-12-11 03:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 3be1e697-fef3-3bb6-b4d0-75966fb0ac72 | -6.0315 | -43.7105 | 2025-12-11 03:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 7f1b4eec-d081-3388-bea9-d91604924715 | -3.229 | -47.4629 | 2025-12-11 03:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 10544250-8e90-3fc9-9d87-f46f60a2abed | -3.7589 | -45.4944 | 2025-12-11 03:30:00 | GOES-19 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 59.6 |
| beadc726-6015-30da-90a6-b4cefd6562c8 | -3.229 | -47.4629 | 2025-12-11 03:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 2a5d87ae-5507-3cd4-a2bf-5066eec2c3c7 | -6.60374 | -39.54516 | 2025-12-11 03:46:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| dd5b8aaa-bdb5-3aa3-940f-0efe6cbb7d07 | -3.63032 | -44.64717 | 2025-12-11 03:46:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d4dc3bf5-bd2a-371a-9afd-09db042f5ba1 | -6.90984 | -38.09773 | 2025-12-11 03:46:00 | NOAA-21 | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d74db69d-bfb6-3ea3-a93d-da9a35475eb9 | -4.23103 | -45.39948 | 2025-12-11 03:46:00 | NOAA-21 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 73d37403-8418-3b66-acc9-297c25e6e4f8 | -6.9425 | -38.61681 | 2025-12-11 03:46:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 26654e10-db29-36ea-91f9-556e6305322f | -3.23419 | -47.46598 | 2025-12-11 03:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 2fa29f3e-fbb4-3157-a3df-87e14991528e | -3.39418 | -42.10745 | 2025-12-11 03:46:00 | NOAA-21 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 1f3c291f-93c0-3f77-9e84-2349199e13bf | -5.35451 | -39.7107 | 2025-12-11 03:46:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1832085b-7e58-307b-b541-e1995cd98ee1 | -4.93764 | -43.96169 | 2025-12-11 03:46:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2cbaa27f-1139-3726-838f-ac731c958932 | -4.76429 | -43.40588 | 2025-12-11 03:46:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c5fd6d15-da8e-3930-a91f-c3b13292d1cf | -3.09077 | -44.89655 | 2025-12-11 03:46:00 | NOAA-21 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 147db8f3-ff55-3219-99e2-d05756d96cf1 | -3.84642 | -47.8223 | 2025-12-11 03:46:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 01a1c2d3-d4a0-3965-97b0-9a5d284cf43b | -2.08131 | -48.3682 | 2025-12-11 03:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ec8c0fe2-162d-3ff2-8f06-f529b65e498e | -3.35366 | -46.21268 | 2025-12-11 03:46:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e246215-eae9-3e74-8b63-054f9c972b31 | -4.43619 | -38.96946 | 2025-12-11 03:46:00 | NOAA-21 | CAPISTRANO | CEARÁ | Brasil | 2302909 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2cc3b1e1-f3e6-30f2-9c08-f8bd46a64a24 | -6.55209 | -39.32399 | 2025-12-11 03:46:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5878bfca-c486-32af-9f01-5097ec8c2df9 | -4.29658 | -44.63394 | 2025-12-11 03:46:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7919114d-bac6-3082-9b62-03a43c10cbac | -3.23922 | -47.4696 | 2025-12-11 03:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 2508ae7d-f7a4-391d-a846-c0ac566d02ce | -3.42506 | -41.65462 | 2025-12-11 03:46:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 326f63ea-3494-3cc2-b620-57166ae9e913 | -4.31873 | -44.50405 | 2025-12-11 03:46:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 61a615ae-fc48-3628-b038-fb231260221f | -6.9397 | -38.6126 | 2025-12-11 03:46:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 0039e0c4-285d-3ff2-99ef-c04436cb0f8b | -5.56373 | -43.80625 | 2025-12-11 03:46:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 96d3fbac-510e-37a7-9a60-a53361e389ac | -6.55714 | -35.21293 | 2025-12-11 03:46:00 | NOAA-21 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 468486ac-9dd8-32f2-acfb-2725f13c0fcf | -4.41799 | -44.80047 | 2025-12-11 03:46:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 05f51d9f-243d-3d22-9161-c2daba9f9c67 | -6.77252 | -35.08402 | 2025-12-11 03:46:00 | NOAA-21 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 31d92d20-f921-39d7-88b3-f9eac1f68214 | -3.39559 | -45.42156 | 2025-12-11 03:46:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0d59f748-97e5-33a4-8ad4-78afb5257b45 | -6.28695 | -39.88569 | 2025-12-11 03:46:00 | NOAA-21 | CATARINA | CEARÁ | Brasil | 2303600 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| f3cdb776-9c9f-3b6c-9fa3-527e2f04ebdd | -6.26822 | -43.68135 | 2025-12-11 03:46:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 203d866f-6292-3353-8a3e-a4df911dad56 | -5.35811 | -39.71129 | 2025-12-11 03:46:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| eacdff0a-4f1c-3f2d-9ee7-d52244422b4c | -3.77939 | -40.55859 | 2025-12-11 03:46:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ffc091a8-0cd9-3c9e-874d-0eaa5fa0f5c0 | -3.39848 | -42.1081 | 2025-12-11 03:46:00 | NOAA-21 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 8303079b-a3c2-368a-8557-733bd40e79f8 | -4.39082 | -45.40842 | 2025-12-11 03:46:00 | NOAA-21 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3cdce221-2417-3d58-8895-3c16cb408f28 | -5.01362 | -39.70766 | 2025-12-11 03:46:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bc2cf895-865f-3a95-a76a-de8e9b4c7d98 | -5.00859 | -41.28817 | 2025-12-11 03:46:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 28b30dfd-5bf9-3bb9-ab04-5c4207545891 | -5.55822 | -43.81052 | 2025-12-11 03:46:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 262a58ea-4618-3313-91d0-f2ec3fc508a8 | -3.0913 | -44.89337 | 2025-12-11 03:46:00 | NOAA-21 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2f69a006-f225-3150-a5be-586fd1f2fefc | -4.41849 | -44.79749 | 2025-12-11 03:46:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 72ef1e0a-23a6-3af5-b069-e35041fba6ff | -4.53954 | -44.04593 | 2025-12-11 03:46:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7b795ebf-f5bd-3cc7-90a9-da868b02e449 | -3.23342 | -47.47057 | 2025-12-11 03:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 7c16d74b-edb1-3cac-a95e-c7df1ee2bcfb | -6.19553 | -39.3769 | 2025-12-11 03:46:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 392497d6-bdb2-3a35-95c0-3b6212be5b7f | -5.32277 | -40.54997 | 2025-12-11 03:46:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| ad8fa12b-a418-3616-a437-7f41e9b5f2e6 | -6.95268 | -38.61842 | 2025-12-11 03:46:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 00dea9c3-6517-39e2-b85b-aae3aaa81fa8 | -4.21015 | -44.4761 | 2025-12-11 03:46:00 | NOAA-21 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a9de4236-6ac1-3161-b823-8b82eab8e44d | -4.21453 | -45.4003 | 2025-12-11 03:46:00 | NOAA-21 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1e3bf66b-e8a7-3657-94d4-845f2ca15824 | -3.54083 | -45.4629 | 2025-12-11 03:46:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c40cd628-bbd1-3340-bdce-c8d64af85c3c | -7.18456 | -39.29605 | 2025-12-11 03:46:00 | NOAA-21 | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cd2bf814-3cbe-39f4-8cc9-049125fca5de | -6.2549 | -35.37396 | 2025-12-11 03:46:00 | NOAA-21 | PASSAGEM | RIO GRANDE DO NORTE | Brasil | 2409209 | 24 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 84709935-1bc9-3adc-b21f-c7d083559a90 | -3.95616 | -41.51833 | 2025-12-11 03:46:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7d826c29-aad2-3f19-ab71-6459caf01bc5 | -3.75658 | -45.49384 | 2025-12-11 03:46:00 | NOAA-21 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 4a3d7848-e458-32e0-92d1-715f8a18d868 | -4.43557 | -38.97339 | 2025-12-11 03:46:00 | NOAA-21 | CAPISTRANO | CEARÁ | Brasil | 2302909 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2aea304b-5527-39d4-a3c5-be3938b61faa | -5.01171 | -41.29405 | 2025-12-11 03:46:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 41ac5558-1f7c-3077-b2e3-10fbba70137d | -3.39349 | -45.41897 | 2025-12-11 03:46:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 756978c1-8bb4-312c-83a7-91e65f44c239 | -4.12364 | -42.91628 | 2025-12-11 03:46:00 | NOAA-21 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0e177448-254e-3a3e-a931-928dfe960cfa | -7.08667 | -35.07064 | 2025-12-11 03:46:00 | NOAA-21 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 29a2a3a9-218a-3459-b0b8-0d35c0008ff4 | -5.58019 | -43.79363 | 2025-12-11 03:46:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d4ab4ca3-1c50-35a6-9e99-4f38e8c08410 | -3.42567 | -41.65083 | 2025-12-11 03:46:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 3d8ca401-2779-3003-a0b1-209fac98ff84 | -5.89334 | -38.17516 | 2025-12-11 03:46:00 | NOAA-21 | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 63456fb3-a377-3f36-8bba-4227349e114e | -3.23266 | -47.47508 | 2025-12-11 03:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| e209ed0b-47de-3d3b-bbad-c751b24bd73f | -5.98166 | -44.59302 | 2025-12-11 03:46:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 82508770-2501-341d-ae58-3aefe6cf49bc | -3.84089 | -47.82887 | 2025-12-11 03:46:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f6fef07e-9f09-3e60-8854-b1a08f59aa42 | -3.53602 | -45.45858 | 2025-12-11 03:46:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad31da0a-2f4b-3ef8-a1db-9eb4c438a4a2 | -4.19969 | -44.47733 | 2025-12-11 03:46:00 | NOAA-21 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e2a1df40-097c-3b50-8ed9-22f67b7c2033 | -3.39486 | -42.10337 | 2025-12-11 03:46:00 | NOAA-21 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| fac60c3f-ac7f-35f1-9cc8-b624eb9069dd | -6.79401 | -39.42541 | 2025-12-11 03:46:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| b9e73c62-faea-3d2c-ada6-0c263eba89ce | -3.49704 | -44.88845 | 2025-12-11 03:46:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e52f1cc-4afa-3b98-8ea8-b2bb390e42f7 | -3.23228 | -47.47307 | 2025-12-11 03:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 6352511c-8e99-3f65-bbec-750824e396d4 | -4.93673 | -43.96322 | 2025-12-11 03:46:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 267e24b2-98d1-35a1-b90c-73413fa42c80 | -3.96026 | -41.51895 | 2025-12-11 03:46:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5913bfc9-4176-3ea8-aa1b-4260361b1e2e | -4.20516 | -44.4753 | 2025-12-11 03:46:00 | NOAA-21 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bbe25fac-3182-3203-88d5-743ba52284e9 | -3.39565 | -42.10862 | 2025-12-11 03:46:00 | NOAA-21 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| f38c43fd-02b5-3a55-a6b6-7e0ab7ce518f | -4.39138 | -45.40514 | 2025-12-11 03:46:00 | NOAA-21 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 90239f4d-c09e-3f97-bc77-87f782ec636b | -3.17355 | -48.03212 | 2025-12-11 03:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 17816a76-cc40-3fa7-905a-0c9b7aa8e3a4 | -4.64793 | -40.49594 | 2025-12-11 03:46:00 | NOAA-21 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6a3c9a23-ee9f-30f8-971a-9c719504bd84 | -5.57552 | -43.79296 | 2025-12-11 03:46:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0d27dade-00a8-37a1-85ec-b9c1b424be0d | -3.39293 | -45.42239 | 2025-12-11 03:46:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35a39750-a051-3a64-bffe-ed4bf21306e8 | -6.54231 | -39.47858 | 2025-12-11 03:46:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7704b429-1804-3966-970b-8fda3e8b0f4c | -3.35076 | -46.21132 | 2025-12-11 03:46:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6eb50945-d4c6-34da-983b-1ac91feb19f3 | -5.67759 | -39.73096 | 2025-12-11 03:46:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8196d126-a3f3-374d-bdf8-6211a41575d2 | -3.53545 | -45.46199 | 2025-12-11 03:46:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5ce15abf-f410-3f48-9e69-b4be55706c9f | -3.84169 | -47.82412 | 2025-12-11 03:46:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c9d29240-b160-3ce9-ab88-415350d82bd0 | -6.2682 | -43.67865 | 2025-12-11 03:46:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9f2a973a-39a0-31dc-9f85-545eff28a234 | -3.54026 | -45.46632 | 2025-12-11 03:46:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 726b09f3-34f3-37da-a7e1-24eb4addf436 | -4.75293 | -45.77909 | 2025-12-11 03:46:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be6271a3-bd98-3e27-ade9-8b8322979df9 | -6.5999 | -39.52414 | 2025-12-11 03:46:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| d64f28cc-c4d9-33ff-9078-9720417dc178 | -5.33582 | -38.69511 | 2025-12-11 03:46:00 | NOAA-21 | JAGUARETAMA | CEARÁ | Brasil | 2306702 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c88436c9-d14c-30cf-ba54-2623e52ed7d1 | -5.98653 | -44.5939 | 2025-12-11 03:46:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 11c079c7-6796-3184-9272-53791fbfc048 | -6.55147 | -39.32788 | 2025-12-11 03:46:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b473d710-ea05-31be-b1ca-ced55a84b0e7 | -3.24362 | -44.91699 | 2025-12-11 03:46:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0daced7-61fe-310c-b0a3-bd5795d37eae | -4.20468 | -44.47813 | 2025-12-11 03:46:00 | NOAA-21 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e08dabd7-1224-3751-957f-37dbfec9680f | -3.17447 | -48.02679 | 2025-12-11 03:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README6.md)
