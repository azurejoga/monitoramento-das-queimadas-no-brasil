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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 06d19f8f-ff5b-339a-b920-bc03589679f1 | -6.23666 | -44.14995 | 2025-10-20 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7069e7b6-9158-3ee2-b7d7-889f18d053a0 | -5.42567 | -40.8972 | 2025-10-20 04:12:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ce34b6b7-fca1-30f3-a224-b7880e172e1d | -7.41746 | -46.71399 | 2025-10-20 04:12:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3a3ce57c-f6e7-39d3-9578-e4020b9ffc27 | -4.42672 | -40.18109 | 2025-10-20 04:12:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c3124c64-c287-3154-a5c1-913152607783 | -6.88927 | -43.59856 | 2025-10-20 04:12:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 608491d8-4e48-318d-9016-5266c2e91e75 | -5.62439 | -43.64723 | 2025-10-20 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3a69b5e2-90b6-3c2d-9340-0d116617702b | -7.13317 | -44.24192 | 2025-10-20 04:12:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 58f13fc9-7e8d-3b5a-b6ba-21eb75a7071c | -7.14188 | -46.51923 | 2025-10-20 04:12:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e33347d6-2c8b-3b2c-80d7-44a57be67064 | -7.12755 | -44.25561 | 2025-10-20 04:12:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 70c41667-8e09-3b94-a677-f80598e2e556 | -7.21043 | -45.42023 | 2025-10-20 04:12:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5fdcdf74-21a4-3068-8161-8b622f04a705 | -3.14426 | -49.51731 | 2025-10-20 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 560b5614-7a48-3b82-afec-7693ca8f3551 | -3.1934 | -45.6644 | 2025-10-20 04:12:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3c27c22c-64ce-317f-b36c-0a4573a5d224 | -6.13409 | -41.72755 | 2025-10-20 04:12:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| af2852a9-b47a-3fda-9169-a8e8bad1d0c5 | -2.24833 | -51.92474 | 2025-10-20 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| dd798789-23e4-36c3-aaa7-54ab4e644560 | -4.40273 | -43.31359 | 2025-10-20 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 444ba9ed-1fe6-3cf4-9eaa-a5db77b04ebc | -5.42508 | -40.90093 | 2025-10-20 04:12:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 43cb5a47-49d4-36a7-811c-4a29dc0d5a09 | -7.49768 | -43.8962 | 2025-10-20 04:12:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 47df14fd-f9c6-3657-accf-a1e0d04b6f5f | -7.14241 | -46.51738 | 2025-10-20 04:12:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 301f7820-322b-367e-b8df-5b1469347750 | -2.24392 | -51.91622 | 2025-10-20 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 4179363e-2214-32d6-a7db-2ba132284aeb | -5.83863 | -47.56486 | 2025-10-20 04:12:00 | NOAA-20 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| de290c29-fe47-346a-91bc-cf4fa1a9eae9 | -5.08959 | -45.89433 | 2025-10-20 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 36157afd-633e-3f90-badb-b24f9b9339cc | -4.8572 | -45.11772 | 2025-10-20 04:12:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6c7f62b1-e7cb-3a58-bf6e-a1c984da82cd | -7.13987 | -44.24297 | 2025-10-20 04:12:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fefa34fb-4eb8-3dba-b507-5149964e36b8 | -6.0992 | -44.015 | 2025-10-20 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3e2ff6a9-a657-3327-b173-2e07ec109c8c | -5.38276 | -43.15575 | 2025-10-20 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 76b3c837-b16a-3d47-be6a-599d2f646b5a | -4.95618 | -45.08905 | 2025-10-20 04:12:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ae989166-9aa7-330a-b941-e0f4059b6392 | -4.83983 | -42.74451 | 2025-10-20 04:12:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f376510-8e1c-3796-817b-40618e1c25cf | -4.83165 | -45.79619 | 2025-10-20 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 37c48fcd-d899-3a10-b814-6905577393ac | -5.15529 | -42.7905 | 2025-10-20 04:12:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1b235c6a-c322-39e7-ab1c-6aecb4153fec | -7.07049 | -46.19818 | 2025-10-20 04:12:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5e48e2ff-5345-3a95-917a-650a94833fc8 | -6.96271 | -46.98349 | 2025-10-20 04:12:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 53c636fb-5ae5-37d6-8274-fece43889039 | -4.83804 | -43.01288 | 2025-10-20 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 96e46d77-5a30-34c3-bcb0-43f62ef45d5f | -6.10476 | -44.02314 | 2025-10-20 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 83537a92-f260-314d-b1fe-8db3f3bab6d3 | -4.48337 | -45.30468 | 2025-10-20 04:12:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1fa93979-dc3b-3648-9f97-65555d324ef5 | -5.29995 | -44.45132 | 2025-10-20 04:12:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aaa36c3f-e939-397a-b260-d4923782d721 | -5.62383 | -43.65074 | 2025-10-20 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 587c2443-d8e2-3696-be48-3f1dee2ddf5a | -4.49349 | -43.12819 | 2025-10-20 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 408bdae7-f27d-3be4-be11-b200fbff290b | -6.56343 | -44.42631 | 2025-10-20 04:12:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a5ad8c52-6cdb-3117-b1a2-9076a4723b7b | -6.09585 | -44.01445 | 2025-10-20 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 76d469c5-18d8-3df7-abc8-c4f1207c3b8c | -6.21279 | -40.97413 | 2025-10-20 04:12:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4aace1fd-2f13-3536-83b2-ebb989be8498 | -6.20424 | -40.96146 | 2025-10-20 04:12:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 636e005d-dc80-378a-a600-da053acd9664 | -3.59458 | -41.65463 | 2025-10-20 04:12:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| a73e4efe-34e0-3d18-aaa3-03ebac137eb5 | -8.27947 | -42.94888 | 2025-10-20 04:12:00 | NOAA-20 | TAMBORIL DO PIAUÍ | PIAUÍ | Brasil | 2210953 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ab639fc2-a151-3426-87b9-6474f35fc1f3 | -6.36543 | -46.15934 | 2025-10-20 04:12:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 034775dd-1251-32ec-b970-91a7c979a7eb | -4.34201 | -43.61428 | 2025-10-20 04:12:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0841e12e-f095-35f6-ad2c-4ece1b1d404d | -7.07409 | -46.19878 | 2025-10-20 04:12:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eac6b359-b489-31a7-9add-1945eea32a87 | -5.60607 | -43.65512 | 2025-10-20 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b4165dfe-f51a-31f7-a85b-1cc8938d9ff9 | -2.30515 | -50.53772 | 2025-10-20 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b1f748e9-4ba4-394e-a4d6-a9034c4ece1b | -6.41068 | -43.76526 | 2025-10-20 04:12:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c39c6931-ddd0-32b3-a4a7-7a665d724495 | -5.36152 | -43.7392 | 2025-10-20 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f8e918ae-215c-39d0-a137-9359abca4613 | -7.07122 | -45.2142 | 2025-10-20 04:12:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 37963103-ef5c-37c1-a191-2e4d69e5dfdf | -4.83322 | -42.74347 | 2025-10-20 04:12:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 33.5 |
| d574db09-f3f7-3633-9dee-2c23538b1cfa | -6.00298 | -44.18607 | 2025-10-20 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ebda1171-eb9d-3c6e-91fb-381cdd36310c | -6.34384 | -41.55523 | 2025-10-20 04:12:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ad9d4bd3-224d-3a57-978a-65143e070250 | -5.34003 | -42.93316 | 2025-10-20 04:12:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 22227df4-bcf2-31f2-ae3f-bef84f69d75a | -5.58759 | -42.69993 | 2025-10-20 04:12:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| db86e0d6-ce12-3a96-844d-874828c7d15c | -4.89597 | -42.94769 | 2025-10-20 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e8eb9460-30b4-3286-94b4-82b821eaf97c | -6.10633 | -44.84625 | 2025-10-20 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 690578d3-4e81-3e24-a20b-1fad1fc76254 | -8.15631 | -38.62953 | 2025-10-20 04:12:00 | NOAA-20 | MIRANDIBA | PERNAMBUCO | Brasil | 2609303 | 26 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 47d7e167-fc4e-3856-a6c0-fe119ca72eae | -4.83598 | -42.74744 | 2025-10-20 04:12:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 06c38b95-9b59-3575-9e14-73e9a08f686d | -7.50356 | -38.81998 | 2025-10-20 04:12:00 | NOAA-20 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 86b55079-37c1-335a-a57b-736fe6117e94 | -5.09029 | -45.8901 | 2025-10-20 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0de8939e-6fb6-3a6d-ac8f-12a119825a6b | -7.13374 | -44.2384 | 2025-10-20 04:12:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 68871b59-6be1-347e-b6f5-c378ea54f73c | -4.3994 | -43.31306 | 2025-10-20 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d5c52cc7-e2a0-335e-80e5-9f67d08199cc | -6.20398 | -41.5341 | 2025-10-20 04:12:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b967f4f8-e7c0-3d14-b369-d388ef3161fb | -4.85369 | -45.11718 | 2025-10-20 04:12:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 96c101de-c1f4-305f-8562-4641f53168ac | -6.1508 | -44.28692 | 2025-10-20 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8359faf7-6186-33df-8073-668a58177a7c | -6.4004 | -38.28609 | 2025-10-20 04:12:00 | NOAA-20 | PARANÁ | RIO GRANDE DO NORTE | Brasil | 2408607 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 74384f86-e63a-3d77-908e-dea2188c2e16 | -4.48401 | -45.30067 | 2025-10-20 04:12:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5cd014f9-c265-394f-8e34-2a0aecd7ebe6 | -5.88492 | -43.93047 | 2025-10-20 04:12:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f51d55cf-7267-3936-b6e7-d4ff35109dca | -6.88983 | -43.59509 | 2025-10-20 04:12:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 57820b2a-7aa2-3f41-977d-cf396379bae5 | -7.06044 | -45.45573 | 2025-10-20 04:12:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5265da32-31d3-38c5-9765-41aa6acf4c8a | -5.61829 | -43.64267 | 2025-10-20 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9ff44e51-1e0e-318e-af36-ca90a7f49607 | -5.28566 | -42.54662 | 2025-10-20 04:12:00 | NOAA-20 | PAU D'ARCO DO PIAUÍ | PIAUÍ | Brasil | 2207793 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d0d4d1a3-d2a4-3768-9d64-3cccab8ef119 | -7.54307 | -46.09448 | 2025-10-20 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0734fbf1-b308-3596-a598-7d55a7ef7ed2 | -3.59072 | -41.65758 | 2025-10-20 04:12:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 79fe9973-b916-3544-9859-62fc00e28e36 | -5.33617 | -42.93609 | 2025-10-20 04:12:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7a4eeb02-b3bb-315f-9db4-ef539633ce0b | -6.42752 | -42.99596 | 2025-10-20 04:12:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f46c4122-3364-3109-8afe-177a1db7c652 | -5.10781 | -43.19714 | 2025-10-20 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 61d7abe4-ba6b-3089-9847-d17e2b386ff2 | -4.8932 | -45.52788 | 2025-10-20 04:12:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 14100f2f-b276-385e-8390-6e507f55f5e2 | -5.30057 | -44.45037 | 2025-10-20 04:12:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 14e7fc72-54a9-3a3d-bffa-748c799dc2c4 | -6.142 | -41.80831 | 2025-10-20 04:12:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2672960d-4b65-36bd-afd4-39a038b03ee0 | -7.13652 | -44.24244 | 2025-10-20 04:12:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b572fb72-6b76-3834-a53c-d625546df612 | -5.03906 | -45.1376 | 2025-10-20 04:12:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e9a80367-66fb-366a-9792-5ef72d1e1912 | -7.46251 | -44.76985 | 2025-10-20 04:12:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 76c75bec-858f-3209-85c2-18415a80de46 | -5.24265 | -46.14784 | 2025-10-20 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 07c3af35-7c2c-386b-91ff-9e5435d45a8e | -5.16516 | -43.13517 | 2025-10-20 04:12:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 975e2246-572b-3b66-9e8e-942a0c113805 | -5.08615 | -42.75482 | 2025-10-20 04:12:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dd8be45d-98d7-323d-b94d-39d17e374aeb | -6.55215 | -41.65724 | 2025-10-20 04:12:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 7ff734f8-08f2-35e6-aca4-92de438ef715 | -8.33853 | -39.74275 | 2025-10-20 04:12:00 | NOAA-20 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a6789dbe-a3c9-31b8-9fcc-e684fb5dc74e | -5.28236 | -42.5461 | 2025-10-20 04:12:00 | NOAA-20 | PAU D'ARCO DO PIAUÍ | PIAUÍ | Brasil | 2207793 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 2dbdeabb-b505-3765-9da3-4da9aaac65e1 | -5.52819 | -44.53899 | 2025-10-20 04:12:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6625a9d9-48fc-3d0d-a2cd-502fba832002 | -6.09139 | -44.0209 | 2025-10-20 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7777147f-749f-3082-8238-a35d426b4ffc | -5.59035 | -42.7039 | 2025-10-20 04:12:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b052a7b8-8b46-3d4a-9b38-0839f6ce623f | -5.26462 | -43.12999 | 2025-10-20 04:12:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2cc30a79-cdec-3cbd-af4c-db49a69b49c2 | -6.93726 | -45.04635 | 2025-10-20 04:12:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 13156039-8f61-3aa1-b10a-8fc640d38fea | -7.11148 | -39.43351 | 2025-10-20 04:12:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1878d181-b35a-37e4-83fb-c3cfbecfcee5 | -4.4537 | -43.4652 | 2025-10-20 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 283d5846-df4c-3a3e-ab2f-b693302ae309 | -2.25419 | -51.91006 | 2025-10-20 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 4a57f655-0f2e-3539-9746-ee22c1f773f8 | -5.54462 | -43.03597 | 2025-10-20 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README13.md)
