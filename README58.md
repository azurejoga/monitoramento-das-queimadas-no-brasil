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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bd458e3e-6939-3966-9635-7a980b34faa3 | -10.81981 | -51.13822 | 2024-10-14 04:21:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2485c73f-0e88-3c27-8554-dfa9df2b6a54 | -10.81916 | -51.14196 | 2024-10-14 04:21:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 311fd0ef-d7e3-3b14-860e-a66229f5566b | -10.8157 | -51.1375 | 2024-10-14 04:21:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c950828f-b2d7-33b9-ba2f-5a096e46482d | -10.54928 | -50.83969 | 2024-10-14 04:21:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 865262ff-95b7-3401-8702-37bdba885ef5 | -10.54524 | -50.83893 | 2024-10-14 04:21:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8245f5ef-485f-3312-8576-74e4b8bfe07e | -10.54367 | -52.09406 | 2024-10-14 04:21:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 243c8ff5-29f6-319d-8fc6-749c61599965 | -10.42899 | -50.83295 | 2024-10-14 04:21:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5003e224-9e09-36ff-a4ff-b3663791f59a | -11.40558 | -51.23511 | 2024-10-14 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a7b239f8-ba8b-3c7f-bc0c-b5de3abf8326 | -11.40492 | -51.23882 | 2024-10-14 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 45dadd66-ebdb-36d4-a4b1-aee3ccc54d68 | -11.40149 | -51.23438 | 2024-10-14 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 61544f8c-a17c-3e08-9c97-0f6f026887b6 | -11.27169 | -51.32748 | 2024-10-14 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e3e40137-02e6-3eab-a485-6c58cc2f21bc | -11.26756 | -51.32676 | 2024-10-14 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 106f568f-3735-3a67-aea2-2ab4012253b0 | -11.26344 | -51.32604 | 2024-10-14 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 165b7bbb-c3c0-3fd4-a83e-05bce65fe794 | -11.26147 | -51.32226 | 2024-10-14 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 384678a2-2d7f-3782-90d1-dd53b3ca6487 | -11.26081 | -51.32605 | 2024-10-14 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 348d3276-c1ed-3e06-b20e-87cdc5aff305 | -11.25931 | -51.3253 | 2024-10-14 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 34c47377-a398-3d2d-a6e6-82f7e016df8e | -11.25734 | -51.32152 | 2024-10-14 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d6af2a93-328c-3a7b-b788-cac37677d9cf | -11.25669 | -51.32531 | 2024-10-14 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b6a653ac-aa61-3e65-b263-7e6cd14e8155 | -11.25519 | -51.32457 | 2024-10-14 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1c4ea24f-d875-3ce0-a40e-d6ff9748d19a | -11.25256 | -51.32457 | 2024-10-14 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 82c5509c-2d5a-30d3-94d9-673a8b955cac | -11.24844 | -51.32383 | 2024-10-14 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| e25ddff2-2974-3615-858a-634889d88bae | -11.24778 | -51.32763 | 2024-10-14 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 90a9e26f-1a75-30e2-acf4-2ee841d91580 | -11.23953 | -51.32615 | 2024-10-14 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6e6f5f89-b2ff-30e2-85ee-a30cd3eac530 | -11.23606 | -51.32162 | 2024-10-14 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 59a3101e-1a41-3929-abf9-c3016b168fb7 | -11.23541 | -51.32541 | 2024-10-14 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 750b0159-b944-3e09-b759-99afdea845e9 | -11.23475 | -51.3292 | 2024-10-14 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 30e4cdd9-23cc-301d-b07a-ec79d5e451ce | -11.23194 | -51.32088 | 2024-10-14 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 651996fd-b3a2-389a-8aed-ea81419b8602 | -11.23128 | -51.32467 | 2024-10-14 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b0600f3b-502b-3d07-98a4-c8e3d0faf299 | -11.23062 | -51.32846 | 2024-10-14 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5727c552-b447-3309-b39c-bc99dde00904 | -11.22649 | -51.32773 | 2024-10-14 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b7e1d142-f060-381b-babc-2ac61ec96f41 | -11.22236 | -51.327 | 2024-10-14 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 055057d4-e617-3afd-ad39-a046b4ef9000 | -11.2217 | -51.33079 | 2024-10-14 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| efded5f3-e0a6-3d3e-a297-01ca8abad704 | -11.21691 | -51.33385 | 2024-10-14 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 6a674345-e3e2-30ee-b66d-fc4b74f4ff65 | -9.33817 | -52.85072 | 2024-10-14 04:21:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 09873563-0136-3a77-b4c1-2b4f375450c1 | -9.33445 | -52.84424 | 2024-10-14 04:21:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 55f33709-80dc-35c9-ba8b-9c77313a3a04 | -9.3335 | -52.8496 | 2024-10-14 04:21:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 238116e7-713b-322c-b03b-60ab1658621b | -9.88363 | -52.28136 | 2024-10-14 04:21:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 433bcfa7-fe20-3319-a070-99a4256f69c9 | -9.88224 | -52.27835 | 2024-10-14 04:21:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 16304443-9222-39c0-b298-a76a783c497b | -9.88145 | -52.28289 | 2024-10-14 04:21:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 631a7071-6564-32e3-b50f-8bb4b9b491d7 | -9.73376 | -52.84904 | 2024-10-14 04:21:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9dd234ac-86f5-391f-bfde-61907861dd5c | -9.73288 | -52.85397 | 2024-10-14 04:21:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 50b03dad-7208-3620-ae49-35bcf789a2aa | -9.73201 | -52.85879 | 2024-10-14 04:21:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| feeef966-4a8f-3a4b-8af3-6f563f8be9ed | -9.72998 | -52.8432 | 2024-10-14 04:21:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 246afee2-a301-3c0e-ac4c-4e05743a5b92 | -9.72729 | -52.85815 | 2024-10-14 04:21:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 987c07ab-0550-3d77-9f58-99df90567afc | -9.72514 | -52.81644 | 2024-10-14 04:21:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6ad154cd-0ef3-39fd-87d9-ca46d6f426d1 | -9.7205 | -52.81541 | 2024-10-14 04:21:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 57cff69c-42d3-3487-b453-ad6807069154 | -9.71695 | -52.86178 | 2024-10-14 04:21:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bda777de-5d64-3efa-b17e-06cb138766b1 | -9.7159 | -52.81419 | 2024-10-14 04:21:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c4940a01-7728-337f-ab39-9837c74dc332 | -9.71231 | -52.86063 | 2024-10-14 04:21:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d7becc03-ead8-3c40-8826-e3553b60381a | -9.71034 | -52.81824 | 2024-10-14 04:21:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1d0d26bb-e112-3fdf-831e-7606e71b0d74 | -9.70555 | -52.81797 | 2024-10-14 04:21:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c6657674-20c2-39b7-974e-0f955ec0c549 | -9.70373 | -52.82799 | 2024-10-14 04:21:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1e292809-0fd2-3819-b8e1-564ef09e5b08 | -10.87081 | -52.36576 | 2024-10-14 04:21:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c3d57118-3979-3bb7-b15d-0737df14ae54 | -10.86475 | -52.37377 | 2024-10-14 04:21:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e68154c6-3b7b-30a6-ae18-4214c5076c9d | -10.20799 | -52.33161 | 2024-10-14 04:21:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| acb36843-5209-3c78-8c5b-20261176d0c9 | -10.20607 | -52.32933 | 2024-10-14 04:21:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 62a43687-fd74-3e58-882a-f22489876c6b | -10.20525 | -52.33384 | 2024-10-14 04:21:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 01dafea9-c942-35b5-9ad2-2234f38821f3 | -10.20429 | -52.32631 | 2024-10-14 04:21:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 831887c0-c860-37ee-a006-d6947ff68c34 | -10.2035 | -52.33083 | 2024-10-14 04:21:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| de7b6be5-1b58-32e8-adc4-1674013fccae | -10.16075 | -52.38911 | 2024-10-14 04:21:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7489a4c0-e55d-3b68-a716-4a159d523030 | -10.15624 | -52.38828 | 2024-10-14 04:21:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef899d38-acb3-3816-aae6-c423e547a860 | -12.88477 | -53.53126 | 2024-10-14 04:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 328eb979-3050-339d-9d81-b8abdc5e0835 | -12.88385 | -53.53626 | 2024-10-14 04:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fc55a065-0915-34eb-801d-ab2a4df67856 | -12.88292 | -53.54129 | 2024-10-14 04:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e26aee53-184a-3da7-9110-ecb16ad858ae | -12.88013 | -53.53042 | 2024-10-14 04:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8228d48d-538c-32b6-b886-c239b1caaa77 | -12.8792 | -53.53542 | 2024-10-14 04:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a0edd4d-d3f5-39a2-9b5e-4ed9e0219052 | -12.87827 | -53.54044 | 2024-10-14 04:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a467beb1-f15d-3ca5-b9c1-94de73c54d41 | -12.87548 | -53.52961 | 2024-10-14 04:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81989407-45d4-31f0-ae1c-c698785bb6ff | -12.87455 | -53.5346 | 2024-10-14 04:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28dc9553-b71e-34c3-a832-0cfa83dfaa19 | -9.00871 | -54.51201 | 2024-10-14 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 392dac13-8d95-31c2-b926-1f84eb4732ca | -9.0081 | -54.51533 | 2024-10-14 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1cef135a-c57e-3d02-93e5-bd1ee7fd21f0 | -8.63873 | -53.65123 | 2024-10-14 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c528f9c2-2f74-3e8a-a66e-036c1239ab0b | -8.63422 | -53.64736 | 2024-10-14 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7779cd14-c2d4-3ff9-b303-57a0a72f3899 | -11.63248 | -54.99575 | 2024-10-14 04:21:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0f37dadf-4c9b-37f5-8810-dda05b2c53bc | -11.62726 | -54.99469 | 2024-10-14 04:21:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4789e57a-f1e4-3116-8db9-692a873659ff | -11.62665 | -54.99788 | 2024-10-14 04:21:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 93f79ed8-eb2c-3b20-8101-17fad8bc4fa5 | -12.50006 | -54.50843 | 2024-10-14 04:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ce309d3-6700-38e7-bbd4-88e93e7f6445 | -12.49951 | -54.51139 | 2024-10-14 04:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b806be45-1b22-360c-83e3-2e6197b7199d | -12.49895 | -54.51437 | 2024-10-14 04:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cebe0e61-fa18-356c-9786-ba9160504115 | -12.46284 | -54.56852 | 2024-10-14 04:21:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 549b3caf-0ea4-32b5-a779-8b468795fa4e | -12.46229 | -54.57145 | 2024-10-14 04:21:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3971ca61-17ac-30c0-b15f-4f0b284da4f4 | -12.46173 | -54.57439 | 2024-10-14 04:21:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 98896200-36b4-3586-a6a8-7f05520ce284 | -12.45842 | -54.56449 | 2024-10-14 04:21:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43757d1c-8139-34d6-ab0a-78b87638b60f | -12.45786 | -54.56741 | 2024-10-14 04:21:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7573fc42-b257-3e5d-9814-89f2d1d1cc70 | -12.45731 | -54.57033 | 2024-10-14 04:21:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c0de6331-806c-342c-b206-2717cdb29cfa | -12.45675 | -54.57328 | 2024-10-14 04:21:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59cdfaec-cd55-36eb-90e4-0656a922326b | -12.45509 | -54.55472 | 2024-10-14 04:21:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 06aa4169-31ab-39fc-b376-0c7ca21cb70a | -12.45177 | -54.57217 | 2024-10-14 04:21:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb532119-33b0-341c-87e4-e62525432719 | -12.4501 | -54.5537 | 2024-10-14 04:21:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff87e2ac-e067-3415-99d8-e53a83106636 | -9.75961 | -55.3471 | 2024-10-14 04:21:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d1acfadd-899c-3f45-afad-7478152a6988 | -9.75927 | -55.34502 | 2024-10-14 04:21:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 515b781a-3034-3ffa-938a-d834728e36a8 | -9.75893 | -55.35078 | 2024-10-14 04:21:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9d340a29-1301-37f5-b839-5550449370dd | -9.75857 | -55.34868 | 2024-10-14 04:21:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 28ad7a20-730d-3aa7-8fcd-5cf3efc22607 | -9.75342 | -55.34963 | 2024-10-14 04:21:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f99c6249-67fe-34f6-a7d8-66f81dd77490 | -9.75306 | -55.34755 | 2024-10-14 04:21:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 67a7f3ad-add3-3bef-9e24-fbb686465b0b | -10.11241 | -55.19921 | 2024-10-14 04:21:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f9bdb515-f611-3ee1-8b6d-4ac08aab2c8e | -10.1063 | -55.20168 | 2024-10-14 04:21:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ad913a6-e7b6-302e-9266-f490ce83ee97 | -20.99793 | -45.93834 | 2024-10-14 04:23:00 | NOAA-21 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fda92d2b-9441-3228-8701-e04b40789f3b | -20.99449 | -45.93775 | 2024-10-14 04:23:00 | NOAA-21 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0872bb7d-ebfe-33e2-8a11-905c97da24f8 | -21.5638 | -48.01408 | 2024-10-14 04:23:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |


[Clique aqui para ver as próximas entradas](README59.md)
