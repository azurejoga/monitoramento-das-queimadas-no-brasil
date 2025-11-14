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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf445323-8e84-37a5-8afd-2180e3e31b61 | -6.89 | -42.85345 | 2025-11-14 05:42:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 19.4 |
| aa3770b6-cb19-35f9-8ec5-73286d52ca16 | -3.34061 | -45.30269 | 2025-11-14 05:42:00 | AQUA_M-M | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 81f058be-a0bf-3340-ad62-bc9013aea6bc | -3.34039 | -45.29567 | 2025-11-14 05:42:00 | AQUA_M-M | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 5e2da2b6-e3a4-32c3-b39d-2f0b24290be9 | -7.1552 | -38.78189 | 2025-11-14 05:42:00 | AQUA_M-M | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 02825a1f-799d-3040-ad79-abc1f2db62bc | -4.6181 | -43.37786 | 2025-11-14 05:42:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5e469880-b538-394a-8c66-6454a76d30a4 | -6.89067 | -41.57972 | 2025-11-14 05:42:00 | AQUA_M-M | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 30fdbe1e-919f-3efc-9b7a-b1a0da52e066 | -2.88211 | -45.28851 | 2025-11-14 05:42:00 | AQUA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| ec6d03e9-3b1f-378e-a748-949a0d128737 | -5.3376 | -43.0334 | 2025-11-14 05:42:00 | AQUA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 29.8 |
| 09bd522f-8587-3997-8450-4d4a34440f4c | -2.9487 | -49.33532 | 2025-11-14 05:42:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 7bb5bd00-7466-355e-bfed-d969349d93ee | -5.97811 | -42.5905 | 2025-11-14 05:42:00 | AQUA_M-M | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 2cea46cd-3819-30e1-ad90-b3352a614faf | -2.83823 | -45.48618 | 2025-11-14 05:42:00 | AQUA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 8160ed4f-1b8d-3aa7-ad01-4ee47dd2a42c | -5.36496 | -46.28983 | 2025-11-14 05:42:00 | AQUA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 7473c1ba-9f6a-3ef9-b1eb-23926a121288 | -5.36736 | -46.27472 | 2025-11-14 05:42:00 | AQUA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 63469fbb-5161-3a60-8ccc-c362f58d32e7 | -7.47058 | -42.56831 | 2025-11-14 05:42:00 | AQUA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 08769b3d-6adc-30e7-a5ec-5c38aa2eabfd | -10.1064 | -40.88853 | 2025-11-14 05:42:00 | AQUA_M-M | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 14.8 |
| b26823a0-2270-36ea-b779-4c984ad9e5c4 | -7.00329 | -42.7822 | 2025-11-14 05:42:00 | AQUA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| e52fb658-e817-3f7a-b8bc-40afbf5ebd1c | -7.4692 | -42.57729 | 2025-11-14 05:42:00 | AQUA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| c5e6cd8f-5fed-3ada-8d1c-45cb42fff774 | -4.12924 | -43.01078 | 2025-11-14 05:42:00 | AQUA_M-M | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| cff2becc-f98e-34a7-96e1-33b256a1f21b | -12.00966 | -46.76106 | 2025-11-14 05:44:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| e7469255-d338-31ed-a4a8-13f95f1955df | -11.8559 | -49.19815 | 2025-11-14 05:44:00 | AQUA_M-M | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 6521412f-636b-3eaf-850c-647f12f0844d | -11.85591 | -49.20329 | 2025-11-14 05:44:00 | AQUA_M-M | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 5f838346-bd9c-3a96-98d0-d967ee9fc94d | -12.65934 | -46.75401 | 2025-11-14 05:44:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 244705f0-6c47-3063-a8e5-7bc7bec091e1 | -14.69788 | -46.61845 | 2025-11-14 05:44:00 | AQUA_M-M | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| ca91be00-6f47-3de0-9783-516a4953f0e7 | -11.85232 | -49.22355 | 2025-11-14 05:44:00 | AQUA_M-M | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 9fa50be7-acd2-3881-b3b2-0a74b60a1e3c | -14.69997 | -46.60606 | 2025-11-14 05:44:00 | AQUA_M-M | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 332762d7-68a1-3fa0-9554-9839b07ccfcf | -12.06603 | -48.21266 | 2025-11-14 05:44:00 | AQUA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 55cd2fdc-36b9-38bf-ae59-e8203f025822 | -12.72276 | -45.41979 | 2025-11-14 05:44:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 38.9 |
| d84d9b5b-38f7-397e-8ce2-b26fd13d3d49 | -12.71324 | -45.41819 | 2025-11-14 05:44:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 16.9 |
| a35f2382-f35e-3fd2-b7e2-b59b58f3d2a2 | -12.66148 | -46.74116 | 2025-11-14 05:44:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 354debdf-4b6f-3546-b1ba-ecfa7680342c | -12.66977 | -46.75574 | 2025-11-14 05:44:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 7c5dd5ec-7720-38d4-b092-84ce2c66caa4 | -12.14406 | -48.0113 | 2025-11-14 05:44:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 7ad8c70f-20b9-3af2-9a41-efacf2478720 | -12.14626 | -48.02168 | 2025-11-14 05:44:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 212fc834-7c1f-3e0b-a66a-eab3d58fc0cc | -12.06889 | -48.19585 | 2025-11-14 05:44:00 | AQUA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 2e6eb23a-dda9-3ca4-9c5a-9c182cd809e6 | -12.69246 | -45.42569 | 2025-11-14 05:44:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 6545a3ce-e894-3a40-b364-23554e27d281 | -17.79785 | -44.97437 | 2025-11-14 05:44:00 | AQUA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 24c8365d-f412-3828-846b-f03d8a7e1d91 | -12.69073 | -45.4364 | 2025-11-14 05:44:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 69dafa81-e9fd-3b90-add6-5f7918504b0b | -12.6719 | -46.74289 | 2025-11-14 05:44:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 32.1 |
| d89c1e06-b219-3b31-9a0e-f7d28caa93f1 | -12.71153 | -45.42883 | 2025-11-14 05:44:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 59bbb714-95cd-3d79-b240-166a986b2641 | -11.85248 | -49.21835 | 2025-11-14 05:44:00 | AQUA_M-M | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 168.0 |
| 15fd3898-58c5-3832-a284-6d85d7b2a824 | -11.93706 | -43.94381 | 2025-11-14 05:44:00 | AQUA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 3625f097-8018-312a-8c51-54725d957c90 | 3.0911 | -60.7653 | 2025-11-14 05:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 59.4 |
| a98c734c-fa45-3628-b95c-bd3294787b30 | 3.1094 | -60.765 | 2025-11-14 05:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 2dbef896-9df4-3b09-b973-5fc2946f6701 | 3.1094 | -60.765 | 2025-11-14 06:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 65eebac5-59d8-3301-9a2d-35ab8e77fde5 | 3.1377 | -60.71481 | 2025-11-14 06:01:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 9618ec60-a02f-3422-bda5-0c67c9f9ddd4 | 3.15407 | -60.27737 | 2025-11-14 06:01:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e2730c0a-9c93-3626-ae56-bcce74e8c3b8 | 3.13898 | -60.71324 | 2025-11-14 06:01:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 77cfc963-30a1-3824-8d6e-9c837fba3eae | 3.16459 | -60.28104 | 2025-11-14 06:01:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e38b8e2c-fe9d-3b80-9657-2fd185839f8c | 3.10668 | -60.7601 | 2025-11-14 06:01:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2981c6a1-d5c8-3f6d-8b93-0392c8524a0d | 3.10281 | -60.76574 | 2025-11-14 06:01:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 2b3fdb31-0dc5-3b50-89a6-7632b3406d0f | 3.10748 | -60.76499 | 2025-11-14 06:01:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9b2dab0b-d355-3b0e-81fc-84c85d7bda91 | 3.10201 | -60.76086 | 2025-11-14 06:01:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 21.8 |
| eaf86c39-f205-3f42-914a-53e440b4f8cd | 3.09814 | -60.76651 | 2025-11-14 06:01:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 92c8e647-0ad3-323a-b749-d7dc2a906fbe | 3.09895 | -60.77138 | 2025-11-14 06:01:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 16b0e593-a498-3af2-bd99-5a03d9ecfea3 | 3.29337 | -60.12067 | 2025-11-14 06:01:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c458750e-8587-377a-889d-3552cc748a85 | 2.75312 | -60.36644 | 2025-11-14 06:01:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 0d404931-93f1-3df5-8518-e462322d4074 | 2.63412 | -61.62644 | 2025-11-14 06:01:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 183cdad7-c4f0-3f2c-9430-d12fa7920d15 | 3.16373 | -60.2758 | 2025-11-14 06:01:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74e2adee-1f17-3a38-9747-9dd1f900b89a | 3.15493 | -60.28261 | 2025-11-14 06:01:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 73f362ac-7e0c-396c-aef4-3b6ea598ae80 | 3.13691 | -60.70991 | 2025-11-14 06:01:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 763fea8f-fe2d-3eb6-a638-3558522060a7 | 2.63856 | -61.62574 | 2025-11-14 06:01:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fc86519b-0faf-3929-8aa1-0168fe702174 | 3.2925 | -60.11547 | 2025-11-14 06:01:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 731fd108-0961-3626-b7f9-8dae9d2ff9b6 | 3.1589 | -60.27659 | 2025-11-14 06:01:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7bd7fa6e-ef6f-3603-8e18-6835cc0199dc | 2.74829 | -60.36724 | 2025-11-14 06:01:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 689d95fe-2e6e-3083-bd3e-37fafa3fefe4 | 3.16544 | -60.28625 | 2025-11-14 06:01:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 11074cdb-bf36-3f38-852d-31585f1bee91 | 3.13301 | -60.71558 | 2025-11-14 06:01:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 749ef20c-2eee-36d5-97af-1ee75a575401 | 3.0911 | -60.7653 | 2025-11-14 06:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 17b483d9-cac6-36fe-babd-18652584d25c | 3.1094 | -60.765 | 2025-11-14 06:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 031032b7-2030-3a35-94c0-25cff6034f4c | 3.13646 | -60.72115 | 2025-11-14 06:24:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| dc827200-eb85-31dd-9170-4b305c5ff94b | 3.14232 | -60.71333 | 2025-11-14 06:24:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e4699b77-75a8-338f-be6c-f24a2c91b8ca | 3.10842 | -60.76715 | 2025-11-14 06:24:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 7f598c4b-bb73-3e4c-a2b4-7e74755898b4 | 3.10259 | -60.77497 | 2025-11-14 06:24:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 10.7 |
| ddba8f46-c9c9-3cc2-a57a-fbf7eec6d5bb | 3.1353 | -60.71447 | 2025-11-14 06:24:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| e99e3d4b-88c8-3ccf-a31c-a247106029c4 | 3.14157 | -60.71859 | 2025-11-14 06:24:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 11f0ff1a-0007-38da-b708-834ce099ed97 | 3.10143 | -60.76831 | 2025-11-14 06:24:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 17.9 |
| f9d7d85b-8264-3bc9-9e3d-0215b6de6288 | 3.13456 | -60.71975 | 2025-11-14 06:24:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e82149fa-95e3-3d15-9710-980758dfc3d5 | 3.1094 | -60.765 | 2025-11-14 06:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 65.8 |
| b09f2b9d-4330-3a15-9d58-b8f3adc68a24 | 3.1094 | -60.765 | 2025-11-14 06:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 56.8 |
| e642d713-2e9c-3e18-8fd7-2ff8237eed78 | 3.0911 | -60.7653 | 2025-11-14 06:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 68280c50-043b-3946-a45d-5602fd47aed0 | -3.536 | -45.4369 | 2025-11-14 06:50:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 6fdd8bac-b2d7-3428-a039-1a94c95a83d0 | 3.1094 | -60.765 | 2025-11-14 06:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 271b8c60-21ca-3259-9252-721c5f872403 | -3.5359 | -45.4594 | 2025-11-14 06:50:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 122af16b-ef4f-3987-9e90-82f271133ae5 | -3.5545 | -45.4586 | 2025-11-14 07:00:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 43.8 |
| db4d839d-16ff-3f3d-888c-8e3e1081b58d | -3.5359 | -45.4594 | 2025-11-14 07:00:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 21b8d7c3-9ff2-30ae-be4a-e64152618042 | -3.536 | -45.4369 | 2025-11-14 07:00:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 07301f20-b80f-3760-ae62-3e3f43910359 | -3.5359 | -45.4594 | 2025-11-14 07:10:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 43.4 |
| d142186f-4654-3a78-a1a5-2fc6f7d4d22c | 3.10222 | -60.76423 | 2025-11-14 07:18:00 | AQUA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 2dabadc4-7ecd-3324-b03d-8f87b5c4a98b | 3.10051 | -60.75287 | 2025-11-14 07:18:00 | AQUA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 7de1ec95-e277-3b6b-849c-3714790040f4 | 3.13734 | -60.71828 | 2025-11-14 07:18:00 | AQUA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 7.7 |
| b7d16b58-f96f-3d2d-9946-9774800defbd | 2.74521 | -60.3677 | 2025-11-14 07:18:00 | AQUA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 0e090b88-6b88-3c4e-a986-a608a40075d7 | 3.09231 | -60.76571 | 2025-11-14 07:18:00 | AQUA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 8.1 |
| dc87f5eb-4b53-323b-9dff-3cc4709da166 | 3.13558 | -60.70689 | 2025-11-14 07:18:00 | AQUA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 75c9f9ea-92f3-37a7-ba71-51f85170bc33 | 3.1094 | -60.765 | 2025-11-14 07:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 230fc3b9-6aab-3800-9968-b6a8709bc0ce | 3.0911 | -60.7653 | 2025-11-14 07:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 52e0ed32-df54-3e78-8f3c-b9e936c3f4a0 | -3.5359 | -45.4594 | 2025-11-14 07:20:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 56.9 |
| a9bcfa85-a3e7-388b-b851-94d3908682e4 | -3.5359 | -45.4594 | 2025-11-14 07:30:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 74cd2245-d927-32dd-9b62-9e1dc864f818 | -3.536 | -45.4369 | 2025-11-14 07:30:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 45.5 |
| f8f0de2c-ec85-30cd-bba8-0d3060bbbc66 | 3.1094 | -60.765 | 2025-11-14 07:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 43910852-2c58-3d46-bb6c-88e3e84fc935 | 3.0911 | -60.7653 | 2025-11-14 07:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 40217452-b0d0-33f0-bad5-a723c9456601 | 3.1094 | -60.765 | 2025-11-14 07:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 59.0 |
| d1b1360d-3be2-3f98-a722-00da1ae2dbc7 | -3.39806 | -41.4693 | 2025-11-14 11:17:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 137.9 |


[Clique aqui para ver as próximas entradas](README52.md)
