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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 397eddb4-741d-31b3-a8ba-d42e6170faf0 | -10.14563 | -52.13651 | 2025-06-01 04:08:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 736468c8-016c-3217-a4c8-fbe0ad1697f7 | -7.21725 | -43.13123 | 2025-06-01 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| fcac3eec-31bd-3290-ace1-057cde95007e | -10.47064 | -47.94973 | 2025-06-01 04:08:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 5869252e-4a39-353f-9c9d-8b3ca69ef771 | -10.67253 | -44.41073 | 2025-06-01 04:08:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1458ceee-d180-3dd3-9871-fdb35fc46818 | -6.26902 | -44.20122 | 2025-06-01 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2004678e-fec3-34a0-a5db-685770c5af3f | -11.90546 | -47.45163 | 2025-06-01 04:08:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 063c5c60-8e25-364f-8881-7fb263a8cef1 | -11.01097 | -40.32172 | 2025-06-01 04:08:00 | NOAA-21 | CALDEIRÃO GRANDE | BAHIA | Brasil | 2905503 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 2b47e48d-feed-364a-91da-addf951fdb6e | -10.6564 | -49.42889 | 2025-06-01 04:08:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a6a443ea-35c3-3924-b3fe-403b354bb87a | -8.6717 | -46.63969 | 2025-06-01 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9924c703-c0ad-3935-9a04-48ddeccb0d70 | -8.3425 | -46.91604 | 2025-06-01 04:08:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 11e8e5bf-bcea-39bf-ac7b-7a1f2c08719b | -10.46719 | -47.9453 | 2025-06-01 04:08:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a8770834-8a2c-3b9f-8f40-4c4c98ad5712 | -7.23648 | -46.966 | 2025-06-01 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f1d094aa-273a-3206-9951-0a6dddc3d08e | -10.67314 | -44.407 | 2025-06-01 04:08:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c156b305-03cb-3143-b16c-48a41b824558 | -7.5797 | -45.86489 | 2025-06-01 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e7ec7520-b9f4-3196-947b-f62458b5fd7b | -8.67478 | -46.64521 | 2025-06-01 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 36fc82a4-8e17-33a0-a9c3-e0ae103bada1 | -7.24701 | -43.24651 | 2025-06-01 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 8951ab03-2d15-3882-b34e-aeec513391a8 | -11.57707 | -47.62688 | 2025-06-01 04:08:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bdfeda93-74b5-3068-ad71-0bd3a250290c | -5.06023 | -43.25404 | 2025-06-01 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 094f306d-9156-3824-acbe-cb1a8aa622dc | -7.2184 | -43.12407 | 2025-06-01 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 757eb7c7-1ef6-3f1b-8dd5-0ef8470709cc | -10.14425 | -52.14378 | 2025-06-01 04:08:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 240717a0-b59c-3743-9603-58c7c8a00dd5 | -7.01007 | -44.62629 | 2025-06-01 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fc613350-4a7f-3a14-ad9f-273a6ff5495c | -10.47472 | -47.95057 | 2025-06-01 04:08:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 6cb2a719-a3df-358d-917d-3f2c83934bd3 | -7.09944 | -43.16432 | 2025-06-01 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 230a3314-a9a4-36bb-91a6-303c7de2df22 | -6.27541 | -44.20634 | 2025-06-01 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| e839e109-d67a-3390-8f2b-2b851b81dd02 | -10.67747 | -47.2011 | 2025-06-01 04:08:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d44d5d14-34e2-392f-b991-01b12fbaf35e | -8.68336 | -46.64165 | 2025-06-01 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cbc4356d-e9e8-3ee1-bc47-7c74c8fa07d6 | -8.72676 | -50.26739 | 2025-06-01 04:08:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5a21167-c998-3f65-b7a2-fd1f520998c2 | -11.79852 | -41.19444 | 2025-06-01 04:08:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 10.0 |
| f09f7aa9-cfd6-3364-a5d7-a53c2a38fdcc | -10.75919 | -48.56322 | 2025-06-01 04:08:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 10c58c45-1268-34a7-9a7a-c6cbc012aee0 | -11.11127 | -44.63279 | 2025-06-01 04:08:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ebcd660f-22bc-3846-a2a1-10e6336a42ce | -9.40302 | -48.42502 | 2025-06-01 04:08:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4fa791a9-cbf9-3599-b526-aa4b6fe32daf | -10.05235 | -49.65889 | 2025-06-01 04:08:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 93270260-2712-31be-b2c8-396ec89113d8 | -10.15912 | -47.19023 | 2025-06-01 04:08:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ca13b2a9-4ece-3914-8ce0-742cd4fd24e7 | -6.86603 | -47.84239 | 2025-06-01 04:08:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| db0a1ea3-4a6a-389d-b6f8-a02c5b865fb9 | -10.45962 | -47.94025 | 2025-06-01 04:08:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6585a5d7-ba09-3046-b7f4-ef0e0f3c64d4 | -7.09608 | -43.16379 | 2025-06-01 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bc425553-0dd2-31be-981d-53d9f7c26728 | -6.29118 | -51.11521 | 2025-06-01 04:08:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57bef812-a81c-332f-8bc9-5a215486089e | -7.01074 | -44.62224 | 2025-06-01 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b1171a56-e744-34d2-8660-05f0d85811b7 | -6.49556 | -47.48344 | 2025-06-01 04:08:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 729b2628-5987-3287-945b-3fd7d99360cf | -7.22061 | -43.13176 | 2025-06-01 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 110a62cc-1b03-39cd-af88-b470a2aa5372 | -8.72922 | -36.41339 | 2025-06-01 04:08:00 | NOAA-21 | JUPI | PERNAMBUCO | Brasil | 2608305 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 1822a213-39c4-37dd-8ff3-ae2266dcb941 | -5.85022 | -47.88879 | 2025-06-01 04:08:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5521b577-5582-3c4a-819c-a7d910a48ec4 | -7.08151 | -46.56015 | 2025-06-01 04:08:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dbf5695d-01d1-376f-ab8b-511ad5e0df29 | -8.67948 | -46.64097 | 2025-06-01 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fe62bce0-9713-3ec4-b359-ab18c110bbfd | -6.63595 | -47.34717 | 2025-06-01 04:08:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d9778344-ee57-3ff6-959b-979a1b8e2344 | -11.31248 | -41.88866 | 2025-06-01 04:08:00 | NOAA-21 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| a9d2d3bd-356d-3369-92ca-dfcc4d30e5b4 | -9.3424 | -48.94911 | 2025-06-01 04:08:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bd792ff7-f238-3d2c-a316-6ae64082a1d7 | -10.73266 | -49.2868 | 2025-06-01 04:08:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 31a5a9b3-130e-311b-8c02-06b9b433e231 | -10.47129 | -47.946 | 2025-06-01 04:08:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 46d47865-17aa-33ee-9242-b7224842b155 | -10.6822 | -47.19988 | 2025-06-01 04:08:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 66e62435-03ec-38cb-9b48-bee6cc3d531b | -7.85615 | -41.9142 | 2025-06-01 04:08:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a8bfdf0c-dab8-398d-bcdf-777a5db39646 | -6.80785 | -41.74052 | 2025-06-01 04:08:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 308f4db1-3b6a-32d3-937c-4d5aba0379d9 | -8.40082 | -43.85036 | 2025-06-01 04:08:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ba4734ff-f87e-31fe-ab8a-f44e985038bd | -10.76253 | -48.56417 | 2025-06-01 04:08:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 87a0fbde-6a60-3d53-8d8b-ab6b326cdf50 | -6.27253 | -44.20181 | 2025-06-01 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| f57510b8-8a5c-3d85-ae34-c55752e7416e | -10.46999 | -47.95344 | 2025-06-01 04:08:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b923aed3-3868-386e-95ff-e04a5b1b6e4c | -6.29244 | -51.11557 | 2025-06-01 04:08:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 87f2b4a6-949d-383e-bfb8-c49f68d3b72c | -4.48607 | -48.86359 | 2025-06-01 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 748561dd-9dbb-3e63-a660-7a7f4a87a48d | -9.70949 | -49.46571 | 2025-06-01 04:08:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cfd59ce6-d6cf-3847-aeb7-fec6e11f6632 | -10.14016 | -52.13558 | 2025-06-01 04:08:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dcbf0eac-c165-3814-ae60-1d68d8ba1138 | -6.27343 | -44.20122 | 2025-06-01 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3c110bde-1f62-3428-83ee-2b9d91608e0a | -8.67089 | -46.64458 | 2025-06-01 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5199e89b-8196-3284-9459-28549097b63c | -6.26839 | -44.20518 | 2025-06-01 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c0b4abc5-a5b4-3657-ae84-84ff26ae0143 | -7.6356 | -46.11319 | 2025-06-01 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7351c9ae-436d-3d9f-b5e3-ebd035ce11bf | -7.22396 | -43.13229 | 2025-06-01 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 5273729d-e7c4-3232-ae38-8648adc31c5c | -8.67867 | -46.64584 | 2025-06-01 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9398e288-55ae-3a5d-ab21-bf980d5f0e86 | -8.73131 | -47.98626 | 2025-06-01 04:08:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6a25a14c-7bdf-3363-8314-8919987f67bf | -10.73345 | -49.28228 | 2025-06-01 04:08:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cd532e72-21e6-3b0b-b349-26ad4f80e533 | -9.13236 | -47.57999 | 2025-06-01 04:08:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 845fd8ba-96e2-3688-a12b-4f783030204f | -10.45897 | -47.94395 | 2025-06-01 04:08:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2212ba44-3fee-3586-866a-e1aabbe38297 | -8.67007 | -46.64948 | 2025-06-01 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2aa6bb78-3f09-34c9-ba08-b89b9be59519 | -10.46307 | -47.94464 | 2025-06-01 04:08:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1db34058-18fa-305b-afc5-56509853465a | -4.6451 | -47.9625 | 2025-06-01 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 159084d4-6ae6-3db5-97f5-3f1c5a67d019 | -4.48517 | -48.869 | 2025-06-01 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 52795ce8-d022-3c1f-8737-d2729d6692f2 | -8.40176 | -43.85018 | 2025-06-01 04:08:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2234db97-79ac-3e5b-b9d5-09577e4ddea7 | -6.44465 | -45.72384 | 2025-06-01 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 34798a58-dd79-3d56-91c1-e2cc120131d5 | -10.12194 | -47.19744 | 2025-06-01 04:08:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 66846d87-f8ea-3c63-9b3c-c6e601400767 | -10.6783 | -47.19919 | 2025-06-01 04:08:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c12ad056-519f-39ec-9670-a2be1bb65353 | -6.27278 | -44.20516 | 2025-06-01 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| e3e83551-0a9b-3fef-8f0d-a2dfae5542ce | -10.67653 | -44.40762 | 2025-06-01 04:08:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 25ac4e88-43ea-3a1b-bb3e-a8cabc6b53fb | -11.57838 | -47.45365 | 2025-06-01 04:08:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6e3cfb8c-3967-35fb-928a-0c25a2477c3a | -8.68255 | -46.6465 | 2025-06-01 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ca17bf45-4e93-323a-bcc2-6b2bb88ad697 | -9.13645 | -47.58075 | 2025-06-01 04:08:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ff5fef9a-8c36-317d-b0c2-1dfac583d616 | -10.22322 | -47.16994 | 2025-06-01 04:08:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 32733900-7e61-36d0-913d-ff6163702c8e | -11.90632 | -47.44659 | 2025-06-01 04:08:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| abb11c78-92f7-3f25-b007-8806b536a02b | -10.12496 | -47.20026 | 2025-06-01 04:08:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 279dedd6-bd5a-32c3-bfcb-a1f63564b24b | -6.86813 | -47.84162 | 2025-06-01 04:08:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 170cbc2f-91ae-3923-912e-6f593aebece6 | -8.40115 | -43.85388 | 2025-06-01 04:08:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 42d7eac1-ad2a-3045-81bf-6d7f2790951f | -7.22569 | -43.12155 | 2025-06-01 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 97f86669-79fd-3e79-bc11-f1e4bb24e915 | -14.64738 | -45.41097 | 2025-06-01 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9ea7f07f-d825-3e19-a5f7-d98044e0bb70 | -14.69936 | -45.11466 | 2025-06-01 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a774be97-dbe5-3761-a09b-f29aa6c57ee5 | -12.71736 | -54.97195 | 2025-06-01 04:10:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0c7af600-9f4a-35d2-b623-5cb1c3ddc324 | -14.61135 | -47.96097 | 2025-06-01 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4ebb08aa-296f-36e0-9889-c9a8543e231d | -11.43278 | -55.00321 | 2025-06-01 04:10:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3893b4d9-0767-3f43-9035-36cfd09fe987 | -13.09534 | -45.26794 | 2025-06-01 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8c12fc38-700c-3ac9-8bc4-4ca60cdcc937 | -14.68302 | -52.69092 | 2025-06-01 04:10:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7121ad7b-f918-36d8-9e21-2d7b865e1e7d | -14.68495 | -52.68343 | 2025-06-01 04:10:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c2356aa3-4a4d-3dfa-8aa4-a581999103c0 | -11.08625 | -54.77859 | 2025-06-01 04:10:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bf414eb3-1fc1-391b-aa78-f8344ab87303 | -13.64102 | -52.18452 | 2025-06-01 04:10:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a37a1545-cf1d-356e-8619-43903676b5ac | -14.69201 | -45.11721 | 2025-06-01 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README5.md)
