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
| cf7356aa-ae5c-3e4b-b14b-31ab0799cf27 | -6.10934 | -41.72958 | 2025-10-30 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 3a0fac74-5d6f-30c1-9b83-1036846c78bd | -6.20948 | -41.82565 | 2025-10-30 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a9d6a375-3fb0-3e12-814d-c0449c595249 | -6.7069 | -38.21333 | 2025-10-30 04:04:00 | NPP-375D | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 69f24dd3-4003-383b-87a7-e59d6bfb6e0f | -4.99263 | -44.15849 | 2025-10-30 04:04:00 | NPP-375D | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0301e049-f548-3d9f-adfa-68dc8a0d3198 | -4.25213 | -50.67081 | 2025-10-30 04:04:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8ee00964-8bb9-3e8a-88cb-8847f3bd4c7d | -7.28332 | -45.66358 | 2025-10-30 04:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0141613a-7e47-308f-bc18-90b81046119d | -6.12429 | -42.4427 | 2025-10-30 04:04:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 00c70e70-baa6-3c27-812c-2ea1da2db3ee | -3.9523 | -43.26213 | 2025-10-30 04:04:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 74843114-dcf3-3645-b57e-4f8155bd3369 | -6.11174 | -41.71467 | 2025-10-30 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fce158e2-2778-309f-9f18-3fba5aed6aca | -7.46974 | -38.55877 | 2025-10-30 04:04:00 | NPP-375D | CONCEIÇÃO | PARAÍBA | Brasil | 2504405 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4a450def-c591-3a20-a526-eccd4f022b8f | -7.07423 | -44.93375 | 2025-10-30 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| aa49796b-3814-36f8-b18f-df3b833e88ae | -4.47102 | -43.44777 | 2025-10-30 04:04:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 6d07cb4a-fbb5-32be-b2b3-4e67e25454e2 | -6.96904 | -39.108 | 2025-10-30 04:04:00 | NPP-375D | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b92ac3bd-63f6-382f-ab78-cec546e4742f | -6.46547 | -41.64639 | 2025-10-30 04:04:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6af65da6-c310-3eb2-9bf7-561d59f2885e | -4.98802 | -45.51926 | 2025-10-30 04:04:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| dcf0d2b3-49f0-3465-bfc8-e11cd3cae75a | -5.84382 | -45.53841 | 2025-10-30 04:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2279b7d1-6202-37ff-95da-fc3ba2d5ec2d | -6.99192 | -46.23461 | 2025-10-30 04:04:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c0ccf41b-5e3b-3750-8420-7a292f973cd4 | -2.66431 | -47.87675 | 2025-10-30 04:04:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6d983494-ead8-3dbf-b6b1-8603bf7cfbde | -3.27189 | -40.02781 | 2025-10-30 04:04:00 | NPP-375D | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0592ecdb-a2bc-38c6-b212-14b33c7ecfa9 | -5.31305 | -44.84917 | 2025-10-30 04:04:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 031e369e-e77d-3592-93bc-1593258fcd01 | -4.67597 | -45.80709 | 2025-10-30 04:04:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ad6d8253-4371-32a7-8e2e-cf186faf6ab3 | -7.77638 | -46.48937 | 2025-10-30 04:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4f9e6a66-41ff-32d5-9272-ef940b685c94 | -8.03028 | -42.51075 | 2025-10-30 04:04:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4af3fc0e-7af4-34b7-9d55-98934cd472cd | -6.15079 | -41.66801 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e5df70f2-c25d-3012-9dac-f62fa7611967 | -6.15904 | -41.61644 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 974888a8-4789-3538-b1f1-615a940128a2 | -5.8396 | -45.53765 | 2025-10-30 04:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fcfab247-dfbd-318a-b875-65c23d168754 | -6.12732 | -41.85887 | 2025-10-30 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b0ed8de6-2e9c-32a4-acb1-eb050cee6f5e | -7.34333 | -39.32923 | 2025-10-30 04:04:00 | NPP-375D | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 57fd9d4e-0466-3b1b-bb14-b1d3ff2a017a | -6.92022 | -42.25028 | 2025-10-30 04:04:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| fde2fee7-4ef8-328c-998c-84ed0ffe68d2 | -4.04411 | -47.49786 | 2025-10-30 04:04:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 14f58351-75fd-3abf-bfcf-e3f3a141782a | -3.79405 | -43.90071 | 2025-10-30 04:04:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 048a25fd-5162-3166-9f6a-134eea9ddedd | -7.1022 | -39.57487 | 2025-10-30 04:04:00 | NPP-375D | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 63fa9113-6643-34e3-b91f-04400fafebb3 | -7.86518 | -44.2332 | 2025-10-30 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cf7c9803-148b-3e78-84a5-05603d504fc4 | -5.51995 | -41.24679 | 2025-10-30 04:04:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 25d46bd0-ba37-3e3c-a2f7-f90fe26e9d1f | -4.30113 | -48.06863 | 2025-10-30 04:04:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44da2b9d-14ea-3e15-8c68-4586aff8880f | -5.41787 | -44.84135 | 2025-10-30 04:04:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 50bfebd0-5512-3cd8-8bf9-f7d558fe909d | -6.19243 | -41.58406 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4cf875a8-a775-3365-a161-0c6c1440271f | -5.63035 | -41.10521 | 2025-10-30 04:04:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 52993b67-c2d9-3ef7-9cac-98e7fd667cc1 | -4.07816 | -44.3738 | 2025-10-30 04:04:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 528d7a9b-b850-3c54-b83a-334e228f3f75 | -6.09903 | -42.44259 | 2025-10-30 04:04:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 0133db35-da67-31e7-99c2-c468a85ad62d | -4.83489 | -42.73418 | 2025-10-30 04:04:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b9055e3c-baf8-3e92-ae4f-ce888ec0485b | -6.91615 | -42.25351 | 2025-10-30 04:04:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| c1444297-f954-34ca-a9be-26ab140b45e4 | -4.49097 | -44.02209 | 2025-10-30 04:04:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 40bb2156-17d0-31b8-bfa3-cc692caec052 | -6.37005 | -40.97415 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 373ec4ee-9bb8-3ef6-9876-62ced0c2a531 | -3.43495 | -42.46235 | 2025-10-30 04:04:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| afbb730a-0440-3b32-91c9-0dacee5bf8f5 | -5.12984 | -43.81052 | 2025-10-30 04:04:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 949c26db-5388-3f64-bc1b-40baf665f92d | -5.02356 | -44.81267 | 2025-10-30 04:04:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| dd3acdb2-4e27-34ed-a710-1b4f1c28e41f | -5.79934 | -40.81115 | 2025-10-30 04:04:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e6a20355-c359-35ec-982e-895076370d75 | -3.66378 | -51.71179 | 2025-10-30 04:04:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2d13f789-ab6c-3def-94c7-a73d7d845673 | -4.15391 | -43.88046 | 2025-10-30 04:04:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 53f4d1ee-8c7c-3bd3-8bd6-53ee5c4bb75e | -7.33013 | -38.85328 | 2025-10-30 04:04:00 | NPP-375D | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ada569d8-81be-383e-9d1c-1d28a85ca6fc | -4.83128 | -42.73359 | 2025-10-30 04:04:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 87c1fa6f-1306-3632-9422-0a519296108b | -5.22588 | -46.14194 | 2025-10-30 04:04:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2ee7ee70-0769-32a0-a41f-de7623eef710 | -5.59164 | -51.1241 | 2025-10-30 04:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 016120f6-b6c1-3ab2-8b6d-7a04dca2b16a | -5.19953 | -45.6101 | 2025-10-30 04:04:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6d7dffaf-8768-3d81-beec-b1e712b5e4e1 | -6.99472 | -39.14124 | 2025-10-30 04:04:00 | NPP-375D | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 43c4aa6a-1be2-3f4d-b7dc-5e94750a699d | -6.29692 | -42.88278 | 2025-10-30 04:04:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8125119b-2785-33c7-bcab-f14ee342123f | -7.30491 | -38.92664 | 2025-10-30 04:04:00 | NPP-375D | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0f7f15fc-5699-3aff-a6e2-e025eff25776 | -7.07665 | -39.56369 | 2025-10-30 04:04:00 | NPP-375D | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ca0f28cc-f8c9-37ee-97bb-a189aff76089 | -5.22658 | -46.13782 | 2025-10-30 04:04:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3c8dbcae-b6fc-3ca6-80c9-437eca05c584 | -4.38007 | -43.29092 | 2025-10-30 04:04:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9dc766f7-cf7e-3aa3-9e8f-c81418877695 | -6.14726 | -41.58084 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bb9fd1fc-79b6-3b60-b28a-1d4001c72412 | -7.01625 | -46.43242 | 2025-10-30 04:04:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d04091c7-7707-3385-89be-0519ecf05d51 | -3.43422 | -42.46358 | 2025-10-30 04:04:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 585cb59e-dd39-3e97-bd50-7134d6f4d22d | -4.83421 | -42.73833 | 2025-10-30 04:04:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 637b40e9-25d1-3ba7-8779-789ae392d93b | -5.45794 | -40.87347 | 2025-10-30 04:04:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b1272884-5983-3967-9844-254f4ab0f117 | -5.37614 | -47.20433 | 2025-10-30 04:04:00 | NPP-375D | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dc85753a-0e6d-3793-9d6c-b3b483da5f35 | -3.00943 | -51.38639 | 2025-10-30 04:04:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 59ea48be-3a3a-3dc4-b832-86bd452a7351 | -6.47795 | -46.88495 | 2025-10-30 04:04:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7d152b8e-157a-371e-b40d-72b45bd8d385 | -7.50943 | -44.07247 | 2025-10-30 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0a71a1f6-ef84-359f-9a18-0a1b0e9a239f | -3.863 | -44.0421 | 2025-10-30 04:04:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d5d2579f-fdff-3b1e-8cfc-d3dbe3f345c0 | -7.50867 | -44.07695 | 2025-10-30 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d37eb7a-7fa2-3e63-b0af-b20dfa7ea54f | -6.85065 | -46.29648 | 2025-10-30 04:04:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 84956728-210a-306d-a8e7-cefc7672049c | -5.72558 | -44.40362 | 2025-10-30 04:04:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0e1e1472-f474-377d-9d57-8c442bbb0f81 | -6.26182 | -42.72874 | 2025-10-30 04:04:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 76bc53a3-1ece-34df-807f-55b08fb3e4b0 | -6.85501 | -46.29727 | 2025-10-30 04:04:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3b3e128a-8475-3503-aea7-ae22fa8ec45d | -3.36772 | -44.78877 | 2025-10-30 04:04:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7972b4a4-3fea-3ac4-a476-dae43dd9ffa7 | -3.36859 | -42.19632 | 2025-10-30 04:04:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 0d1a4d00-09d1-35f7-acf1-be013cfaf762 | -5.49054 | -42.07811 | 2025-10-30 04:04:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 92f8eb58-841e-3c1c-a13f-c2c538b181b3 | -7.93815 | -45.48105 | 2025-10-30 04:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0dce9038-a784-325e-82fe-52e297ed7d82 | -3.39151 | -40.83864 | 2025-10-30 04:04:00 | NPP-375D | URUOCA | CEARÁ | Brasil | 2313906 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8d02ecea-0a33-347a-9d3f-5f55308a4e2b | -5.20448 | -35.4761 | 2025-10-30 04:04:00 | NPP-375D | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| acca25da-81ab-3b46-9d6e-d645f5c14f9b | -7.92961 | -45.50625 | 2025-10-30 04:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| a217487f-e132-363c-ba9d-6dfdddd1c31e | -6.14975 | -36.71546 | 2025-10-30 04:04:00 | NPP-375D | TENENTE LAURENTINO CRUZ | RIO GRANDE DO NORTE | Brasil | 2414159 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 47e18504-f593-3c41-9034-7ca6ccd76918 | -5.80602 | -40.83381 | 2025-10-30 04:04:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5415a6e6-56a5-3b41-a46b-05098c1d5949 | -4.22398 | -45.57621 | 2025-10-30 04:04:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 807a2188-9c20-3a4d-b8a2-49d6b7fc26d5 | -6.15173 | -41.59654 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f4a0622c-050d-32cf-9621-d3ac3169a79f | -4.35461 | -48.19644 | 2025-10-30 04:04:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 38c34078-1243-341c-9fde-dc8128e1c396 | -3.10727 | -39.61342 | 2025-10-30 04:04:00 | NPP-375D | AMONTADA | CEARÁ | Brasil | 2300754 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| bc4005f3-77ea-3567-ada5-9853e7b72665 | -6.18475 | -41.69601 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4e0a9b68-0c2a-3e40-b19d-bbf9e8937281 | -6.26416 | -41.80768 | 2025-10-30 04:04:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9292918c-a281-39d0-87b4-4c7fdc0987ae | -6.14042 | -41.68898 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 37275bf9-9e37-3a7c-b864-653483002c2f | -5.79318 | -40.82815 | 2025-10-30 04:04:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| d4ef08f6-99ec-3f74-88b7-b18cd9e3a66c | -4.68955 | -45.59239 | 2025-10-30 04:04:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a13ebfe3-3bf2-309b-ac86-adb2a7e2e03f | -3.87343 | -42.7737 | 2025-10-30 04:04:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9fa11856-4be4-3ff1-898f-934361939448 | -5.00774 | -41.04425 | 2025-10-30 04:04:00 | NPP-375D | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c01f968a-41ea-3aaa-ad3f-8ada2c8b92e8 | -3.98932 | -43.4159 | 2025-10-30 04:04:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d1a3ac9d-3a4f-3de8-b95f-fbc68e043cdf | -7.17814 | -39.45501 | 2025-10-30 04:04:00 | NPP-375D | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e7b42e2b-62f8-31af-8ee4-71579a79f098 | -5.03688 | -45.16702 | 2025-10-30 04:04:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a4efe939-a011-3522-8085-d79f4ed1d95d | -7.59614 | -43.60367 | 2025-10-30 04:04:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README23.md)
