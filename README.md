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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e900e04-c870-37a3-abff-ed50a3f2f9ac | -17.45446 | -39.28068 | 2025-02-10 00:05:00 | TERRA_M-M | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 5a9aa7bb-3175-3790-832f-08b57df88af8 | -17.45591 | -39.29268 | 2025-02-10 00:05:00 | TERRA_M-M | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.6 |
| 1612f4cf-b383-3d2a-9cab-837123dbd4c3 | -6.99848 | -35.24642 | 2025-02-10 00:07:00 | TERRA_M-M | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 18.2 |
| ee23294d-c082-3437-b91c-84de530d50fb | -6.98344 | -42.99768 | 2025-02-10 00:09:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.8 |
| cd6a849a-502e-3cc5-b6ea-c6277cfc1cc3 | -6.985 | -43.000198 | 2025-02-10 00:11:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a53f491b-6261-39a5-bb37-51baaf2461e5 | -6.9831 | -42.991901 | 2025-02-10 00:11:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 658621f2-0d60-3171-9a89-4a6aa192ad22 | -6.9811 | -42.983501 | 2025-02-10 00:11:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5f88b019-c0e0-31f6-9b13-551be8a8962a | -17.454 | -39.268299 | 2025-02-10 00:14:00 | METOP-B | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4c990060-a71b-3571-85fb-e7af928b7701 | -17.4564 | -39.278301 | 2025-02-10 00:14:00 | METOP-B | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 31fc4fd6-b5e5-3fe6-b7ac-b29736a871ec | -21.481501 | -51.366699 | 2025-02-10 01:08:00 | METOP-C | IRAPURU | SÃO PAULO | Brasil | 3521606 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a077fed9-203b-3756-9742-f1c578c6e337 | -29.8895 | -51.7174 | 2025-02-10 01:08:00 | METOP-C | TRIUNFO | RIO GRANDE DO SUL | Brasil | 4322004 | 43 | 33 | nan | nan | nan | Pampa | nan |
| 123c9f1b-c210-3e68-bb7c-d0747c27c61d | -20.9091 | -56.538502 | 2025-02-10 01:08:00 | METOP-C | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 91947d8c-4938-3f78-9b7a-a6ddb2cb16ac | -21.471701 | -51.369202 | 2025-02-10 01:08:00 | METOP-C | JUNQUEIRÓPOLIS | SÃO PAULO | Brasil | 3526001 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 445355d7-5b73-3109-b040-4640319d56c0 | -20.917 | -56.526402 | 2025-02-10 01:08:00 | METOP-C | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| efe9ba7f-3d88-3925-90d6-62fc4829c192 | -20.9072 | -56.5285 | 2025-02-10 01:08:00 | METOP-C | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| cf292725-3642-307b-b672-8fd20dcd65a7 | -22.2742 | -48.494801 | 2025-02-10 01:08:00 | METOP-C | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 48b9a34e-a136-3d60-9964-5c608e49dc83 | -20.9053 | -56.5186 | 2025-02-10 01:08:00 | METOP-C | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 5851e4fe-5486-3c84-9916-c4508f605325 | -6.9784 | -35.2465 | 2025-02-10 01:30:00 | GOES-16 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 52.8 |
| 001a00a0-4a1d-3675-9148-4611caab084f | -29.64304 | -55.57887 | 2025-02-10 01:38:00 | TERRA_M-M | ALEGRETE | RIO GRANDE DO SUL | Brasil | 4300406 | 43 | 33 | nan | nan | nan | Pampa | 9.5 |
| f9471c8b-5a3a-387a-b6d6-4bc1c0a4d48d | -20.91182 | -56.52959 | 2025-02-10 01:41:00 | TERRA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 36b6e425-4eb9-3500-87b5-1dd6742e3f94 | -20.91375 | -56.54175 | 2025-02-10 01:41:00 | TERRA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 5eeb6fe3-5a26-398d-bfa3-563273a47985 | 3.24686 | -60.20076 | 2025-02-10 01:49:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 00b85fa0-aa38-354d-a5c2-99414e38310b | -6.5851 | -35.20122 | 2025-02-10 02:55:00 | NOAA-20 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| f7117dae-ea74-36fe-b5a2-225d3009d93a | -6.59106 | -35.20251 | 2025-02-10 02:55:00 | NOAA-20 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| b3352918-3fae-3133-a567-2c73ed0c044b | -22.67434 | -42.86631 | 2025-02-10 03:02:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6a80a0b3-6148-30b9-a2bd-aa248dd9c34b | -22.67617 | -42.85918 | 2025-02-10 03:02:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 09c48af9-c688-381d-8409-37bbdade63c5 | -6.97706 | -43.00697 | 2025-02-10 03:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 309ea5a9-1d67-3bcc-9ce9-8ae673f4f0d0 | -6.97917 | -42.99432 | 2025-02-10 03:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9aa8447b-08d0-3c6b-9a37-c183de3c1e16 | -7.54931 | -37.54409 | 2025-02-10 03:46:00 | NOAA-21 | TABIRA | PERNAMBUCO | Brasil | 2614600 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9a7e2ccf-d535-32a4-a7b9-7f3ea6a42357 | -6.98349 | -42.99506 | 2025-02-10 03:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| aa628e27-fe6e-328a-b4e2-14b6c210d4ca | -6.58777 | -35.19411 | 2025-02-10 03:46:00 | NOAA-21 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| f0955396-0c9e-3672-ad4a-47595cf3a664 | -7.54986 | -37.54063 | 2025-02-10 03:46:00 | NOAA-21 | TABIRA | PERNAMBUCO | Brasil | 2614600 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| ab1114a6-4f88-324c-a7b1-d11e94cdd802 | -6.98138 | -43.0077 | 2025-02-10 03:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| baf76412-a737-366b-b59c-3f808816bc53 | -8.11705 | -38.95575 | 2025-02-10 03:46:00 | NOAA-21 | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 28414003-e2cb-3a3b-bf7a-625a8cc4014f | -6.58722 | -35.19774 | 2025-02-10 03:46:00 | NOAA-21 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 39bf59e1-1a22-3482-95c2-03e93cf77068 | -6.59059 | -35.19826 | 2025-02-10 03:46:00 | NOAA-21 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 709654eb-abb3-3a81-8b72-dffa43e77ba0 | -6.59115 | -35.19464 | 2025-02-10 03:46:00 | NOAA-21 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 862266c4-44c9-3b34-8253-8f9e310cded3 | -6.98209 | -43.00348 | 2025-02-10 03:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 239123e6-bc36-36ec-82c6-541bc161fea1 | -8.38466 | -42.26242 | 2025-02-10 03:46:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 178c5a21-cc77-3fb0-9096-6f8a1c522722 | -12.41684 | -43.80082 | 2025-02-10 03:49:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5801caec-177b-38fa-995f-f86d75105913 | -12.42029 | -43.8055 | 2025-02-10 03:49:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f92f0f58-2e91-3581-add0-e451968c6279 | -12.41614 | -43.80471 | 2025-02-10 03:49:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb699304-3276-3e32-a7d0-e1d875593537 | -13.89173 | -44.01475 | 2025-02-10 03:49:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc7fe131-5e7c-359f-a55d-d5ffa61f6820 | -16.40699 | -39.10456 | 2025-02-10 03:49:00 | NOAA-21 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 72e96f03-fe27-3dc5-ad37-746e7468f6cc | -9.87734 | -41.80059 | 2025-02-10 03:49:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| d1c5a9ac-94a8-343a-9288-4271f76968b4 | -22.67654 | -42.85413 | 2025-02-10 03:51:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| d6f1a555-c64f-321f-8cb9-59aa44f75d5f | -21.35822 | -48.57499 | 2025-02-10 03:51:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 013a8a5f-cdb1-3bcd-8c62-a45a0c33dc38 | -20.5534 | -40.9193 | 2025-02-10 03:51:00 | NOAA-21 | ALFREDO CHAVES | ESPÍRITO SANTO | Brasil | 3200300 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 76bcde7a-3293-3fd8-814e-10d8941bc355 | -20.20297 | -41.78458 | 2025-02-10 03:51:00 | NOAA-21 | DURANDÉ | MINAS GERAIS | Brasil | 3123528 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 76a999f7-11e1-398e-a8c5-53fcb70b0dd8 | -21.60197 | -48.45525 | 2025-02-10 03:51:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6ffae3e3-7cbf-35c9-8d0e-f8a91570ca3b | -17.09614 | -43.80644 | 2025-02-10 03:51:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b3341c9-967e-3440-80db-7401a1a2eb39 | -21.61508 | -48.46396 | 2025-02-10 03:51:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 16460886-a341-32c8-96a5-24534473d4b5 | -19.82637 | -40.1001 | 2025-02-10 03:51:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6fb6af50-52d2-3ade-9c1c-9acda41e9112 | -21.60672 | -48.45631 | 2025-02-10 03:51:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e4c0d620-afbf-3b84-a569-fad804011c7c | -19.83917 | -40.08358 | 2025-02-10 03:51:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 0580748f-6903-38ee-8866-6f176589e3d3 | -21.47129 | -51.37415 | 2025-02-10 03:51:00 | NOAA-21 | JUNQUEIRÓPOLIS | SÃO PAULO | Brasil | 3526001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 5fd2bc97-3cc1-36b9-9617-50a56c43b812 | -21.47306 | -51.37294 | 2025-02-10 03:51:00 | NOAA-21 | JUNQUEIRÓPOLIS | SÃO PAULO | Brasil | 3526001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 91deed22-9ad6-3a15-9908-230fd8eed5c1 | -16.68101 | -43.88591 | 2025-02-10 03:51:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c119e972-8553-3e3e-bbb1-da8c6a2ead33 | -22.85564 | -42.97975 | 2025-02-10 03:51:00 | NOAA-21 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0f4bfb22-6b48-36f7-8d15-e80dfe5649ab | -23.98329 | -48.91878 | 2025-02-10 03:53:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4e5992a8-93e7-3c0a-b399-c2859e646de4 | -28.58619 | -49.44101 | 2025-02-10 03:53:00 | NOAA-21 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 85b3c0b7-ea93-3f80-ab0f-2c94f873429e | -23.40793 | -46.55476 | 2025-02-10 03:53:00 | NOAA-21 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0c2f3a21-6a81-30d5-9f40-84843eec07c6 | -23.4072 | -46.55853 | 2025-02-10 03:53:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ca362946-0baf-31da-b26f-0791e8299598 | -23.33905 | -46.77456 | 2025-02-10 03:53:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c16dce7a-576c-3f68-88cd-469d369fa048 | -23.59341 | -47.43745 | 2025-02-10 03:53:00 | NOAA-21 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4324c869-9d6a-3666-87f7-ccdec8cb0b8f | -23.98601 | -48.91567 | 2025-02-10 03:53:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 639b4dca-0b9f-37b2-97a4-c075e2d26cdd | -28.58647 | -49.44373 | 2025-02-10 03:53:00 | NOAA-21 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| cd1d7ffd-1adb-33da-9c55-472698f562fe | -6.93628 | -39.15309 | 2025-02-10 04:14:00 | NPP-375D | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d31c6dc7-a5c6-35b5-a854-4758d045d924 | -6.98317 | -42.99449 | 2025-02-10 04:14:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| cef0138a-2f01-3b7c-85dc-d63c62072cd6 | -9.0476 | -42.66809 | 2025-02-10 04:14:00 | NPP-375D | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 489ed8dd-0d12-3374-985e-38ee4124009d | -6.53116 | -43.56754 | 2025-02-10 04:14:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3c6ba42c-e0e8-3bed-8649-7743d86dec5d | -6.98208 | -43.00145 | 2025-02-10 04:14:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7ec2d53c-e382-3416-a328-d53cba3e397a | -6.97984 | -42.99397 | 2025-02-10 04:14:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b1abc858-e3b9-3f00-939c-5da3593ed60a | -8.3879 | -42.26313 | 2025-02-10 04:14:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a9340613-ac49-3a48-a527-f5be693304fa | -8.11812 | -38.95366 | 2025-02-10 04:14:00 | NPP-375D | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c7c9a2b0-09c0-3249-ba3a-2ecfb1b78cc7 | -6.9782 | -43.00441 | 2025-02-10 04:14:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| abefd833-b1db-3bbb-8470-388e427536ed | -7.89821 | -43.91878 | 2025-02-10 04:14:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b22e802e-b672-39e5-8480-cbbd0ed9198c | -6.98153 | -43.00493 | 2025-02-10 04:14:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f8d43226-f45b-3c59-be7d-a02ae5f7274d | -12.60469 | -43.31801 | 2025-02-10 04:16:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 557fdb49-3c5b-3feb-ac61-bad51ae008b5 | -12.17931 | -43.95282 | 2025-02-10 04:16:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 06deb080-7c48-31b4-8f73-2aeff41c5dca | -12.41844 | -43.8041 | 2025-02-10 04:16:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6ae2e9d6-1c51-3f02-bb42-247a0e5f09df | -21.36023 | -48.57674 | 2025-02-10 04:18:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 555e617e-e4b5-3dfe-adbe-c9a18e183089 | -22.67898 | -42.85213 | 2025-02-10 04:18:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8bd7e2ee-4297-348f-b333-e77c446bb5fd | -21.35747 | -48.57217 | 2025-02-10 04:18:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8b541ecc-f7e0-389f-8862-8d8eabbacb95 | -21.47378 | -51.36956 | 2025-02-10 04:18:00 | NPP-375D | JUNQUEIRÓPOLIS | SÃO PAULO | Brasil | 3526001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3ecc54d1-53be-304d-b5c2-a31f3ba0eb1f | -19.73322 | -54.83676 | 2025-02-10 04:18:00 | NPP-375D | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25c0bc73-bbdb-3a56-bc64-0c27f878aa82 | -21.36088 | -48.57284 | 2025-02-10 04:18:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f6d7e1cc-a4c7-3a5e-b071-9dbee2f92658 | -22.2711 | -48.49969 | 2025-02-10 04:18:00 | NPP-375D | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 77661ae0-8bb7-379a-b8eb-b41d93a3de67 | -21.47283 | -51.37473 | 2025-02-10 04:18:00 | NPP-375D | JUNQUEIRÓPOLIS | SÃO PAULO | Brasil | 3526001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 88d9385f-91f7-34f8-a496-67877dcc0106 | -18.54333 | -40.50478 | 2025-02-10 04:18:00 | NPP-375D | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| bbf15fb3-06bb-3fe9-ba59-a323930b5ab7 | -22.67518 | -42.85157 | 2025-02-10 04:18:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 55ebabdc-54ce-39f6-b522-ddfce52f7aa6 | -24.24282 | -50.74079 | 2025-02-10 04:21:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3c0fdd9a-b71d-3e85-8137-24764bd4f25d | -27.79532 | -50.38371 | 2025-02-10 04:21:00 | NPP-375D | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7f24c786-3b29-3a5f-8af3-d9c58a9b7575 | -23.40599 | -46.55606 | 2025-02-10 04:21:00 | NPP-375D | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e30be64f-9e13-3b78-89f7-3d3199bd1e59 | -27.79603 | -50.37953 | 2025-02-10 04:21:00 | NPP-375D | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3a7df3c5-b788-3f91-b4cb-29dcbc4f6f69 | -29.90221 | -51.047 | 2025-02-10 04:21:00 | NPP-375D | GRAVATAÍ | RIO GRANDE DO SUL | Brasil | 4309209 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| c71a5293-3417-3f70-8e53-bda54e77c801 | -23.33824 | -46.77352 | 2025-02-10 04:21:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6d30e3ba-3416-36e9-ba7f-159f862d88ad | -28.58603 | -49.44189 | 2025-02-10 04:21:00 | NPP-375D | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 745cc610-d9ec-37bd-87fe-6a96144fe34d | -23.59273 | -47.43906 | 2025-02-10 04:21:00 | NPP-375D | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a7815c96-5e11-3d88-99f4-a2e91d1fb35d | -27.7976 | -50.38319 | 2025-02-10 04:21:00 | NPP-375D | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |


[Clique aqui para ver as próximas entradas](README2.md)
