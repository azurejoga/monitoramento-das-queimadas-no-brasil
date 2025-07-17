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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c67ec722-5863-30e2-b898-15fdc4a97de1 | -7.34033 | -44.20576 | 2025-07-17 03:53:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 79741f41-9e9a-363d-91b3-8c842eced8b5 | -6.13761 | -47.30464 | 2025-07-17 03:53:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 402e2f6a-ee8b-3111-b229-10e4b8dfed49 | -4.59238 | -43.32035 | 2025-07-17 03:53:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 53ca0f5b-60e1-35e4-ae61-c09f2d421a74 | -7.94139 | -43.86441 | 2025-07-17 03:53:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c1a8acba-f84c-3fe7-b17e-38d773fc8c31 | -3.04582 | -49.42986 | 2025-07-17 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a489b499-a71a-3463-88bc-bd91987d66dd | -5.9071 | -45.58345 | 2025-07-17 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bf67cbc5-eb10-3093-adc3-17b77317477c | -7.21669 | -35.77593 | 2025-07-17 03:53:00 | NOAA-20 | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5b4fe7b2-0fd2-3882-bab0-4ba57ab7dc86 | -7.62025 | -44.32289 | 2025-07-17 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5e8ee227-7ec8-3f7a-ba0a-18fbb6446e60 | -6.13241 | -47.30363 | 2025-07-17 03:53:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dd642ade-18d2-331b-bb6a-bf4deb7818d4 | -5.93344 | -43.36523 | 2025-07-17 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ea791071-d52f-3663-b996-90c316dab356 | -3.58479 | -47.53193 | 2025-07-17 03:53:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bb5e25bd-1a93-3d1e-bab9-9e873226c980 | -6.88696 | -47.24123 | 2025-07-17 03:53:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2a6d5bbe-d7e5-317a-b328-4b169cecd77c | -7.18602 | -43.12041 | 2025-07-17 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| d827933a-504b-3bcc-a0f2-bdc87d1b3da7 | -5.79418 | -45.08649 | 2025-07-17 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0d3ce19d-c477-36a6-8c29-2c159bbbf2c3 | -6.61212 | -45.70611 | 2025-07-17 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 26d74174-bef6-34e3-97b3-81fd2e2beb33 | -6.67337 | -43.03349 | 2025-07-17 03:53:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2fe2aa24-1a5c-3662-903f-d60d1ff3eb98 | -8.5352 | -47.85085 | 2025-07-17 03:53:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1c47cf99-3be7-3489-86b7-940ea595428e | -3.5852 | -47.53271 | 2025-07-17 03:53:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5e3e65d9-197b-33f0-b857-36d05c863d92 | -5.53217 | -43.88662 | 2025-07-17 03:53:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5e033fae-5d4e-3576-b348-03ef67fc0396 | -7.04147 | -40.36254 | 2025-07-17 03:53:00 | NOAA-20 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 82add6c3-bb54-3bf9-8c82-dbee3f6019f6 | -6.32842 | -43.74615 | 2025-07-17 03:53:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4fc95364-cd0f-3325-88b4-88a6e6ab7b74 | -5.66144 | -43.71404 | 2025-07-17 03:53:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 22afc35c-4fdd-32ec-a264-e3c7aab09876 | -3.3784 | -47.48374 | 2025-07-17 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a0df9a00-4e9e-383c-a2bc-3eb789417f7b | -5.52799 | -43.88597 | 2025-07-17 03:53:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 25c63de3-b189-3789-9cd1-aeb22cb62bf0 | -5.51557 | -41.32967 | 2025-07-17 03:53:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8daaf28c-a18a-3f82-90a6-b9be7f74b7d6 | -4.77728 | -45.34082 | 2025-07-17 03:53:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 09fd3208-6af6-3897-9b9a-9b84ac8293c6 | -6.82274 | -43.78538 | 2025-07-17 03:53:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1384a1c2-1a7e-3298-8e03-5d24a40cf3d6 | -6.40474 | -42.4553 | 2025-07-17 03:53:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| afa24ad9-6873-3716-91da-771d181f5f6b | -8.53982 | -47.85497 | 2025-07-17 03:53:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 94b5b329-b877-372d-838c-665b4863b875 | -6.87559 | -42.75331 | 2025-07-17 03:53:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 6917f4cc-98cf-36b7-bed8-dab785e3fc30 | -6.82742 | -43.78374 | 2025-07-17 03:53:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0be85ec9-a59b-3322-a887-ed9fc6005f17 | -6.72917 | -44.32748 | 2025-07-17 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| fb1684b9-8757-3d48-b109-b15ccf1563d7 | -6.72073 | -44.32607 | 2025-07-17 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 87d5d392-366b-395f-834e-89080cfcfa05 | -5.87968 | -43.4578 | 2025-07-17 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7f63bbed-f19a-38eb-98ef-898cad490193 | -6.98095 | -43.76441 | 2025-07-17 03:53:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| efc1d736-297e-35d5-bb8b-2152d1ec37eb | -3.03865 | -49.43381 | 2025-07-17 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fa278f1e-2cd0-3a7e-bdf9-9c9a3c8dd4b7 | -3.25389 | -43.26442 | 2025-07-17 03:53:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a5699a08-b8d9-3e70-b316-82e53c9097a9 | -3.38332 | -47.48837 | 2025-07-17 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 7404564b-7016-320d-90cd-52d8ff94bf01 | -2.65714 | -47.40108 | 2025-07-17 03:53:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d3c1c96b-1976-3370-976d-e5fdf0d2e318 | -5.66494 | -43.71838 | 2025-07-17 03:53:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 28.0 |
| dcd2d40c-0d58-3848-9bf7-9cfcff9f0fe5 | -4.29659 | -48.10396 | 2025-07-17 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| adcf83e7-c168-3929-b235-86adf79a5986 | -5.48148 | -42.14883 | 2025-07-17 03:53:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 230c6347-41f0-3f4e-9470-514d2da4f4a2 | -7.46525 | -44.71835 | 2025-07-17 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2a557da9-8ee1-3959-9383-dcb5bd1fedfc | -7.34575 | -44.19893 | 2025-07-17 03:53:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3ce49973-1679-3617-af0c-f795cfb45d46 | -4.10465 | -48.21032 | 2025-07-17 03:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9f37a0e5-bdfa-36d1-b40b-5c57dc309331 | -6.8751 | -41.7262 | 2025-07-17 03:53:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 7af48079-f722-316a-91ae-f6eb50c16469 | -4.51101 | -44.12843 | 2025-07-17 03:53:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7a6b334c-ac7e-354f-8d3a-751b357f3026 | -3.37779 | -47.48744 | 2025-07-17 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| efba6563-418b-34b4-b78f-fe62758a5573 | -7.93735 | -43.86388 | 2025-07-17 03:53:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e2b0282b-19b8-3620-8eaa-03cbb422bb2d | -5.91428 | -43.4785 | 2025-07-17 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 28e47244-7387-3eef-a1f1-3a238c0696e1 | -6.9755 | -42.80688 | 2025-07-17 03:53:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 911a6f37-dba3-3b46-a1d5-9ae478194d48 | -8.10979 | -43.14948 | 2025-07-17 03:53:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| cb925ede-d974-3e03-bb60-43f59b0b13e1 | -3.38905 | -47.4848 | 2025-07-17 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d2b411c2-997c-361e-b1c7-f17bf031b872 | -3.38514 | -47.47734 | 2025-07-17 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 63158f43-4252-3bc9-b513-3a525fbf16c2 | -7.14877 | -43.00242 | 2025-07-17 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 79bc3bb4-5e75-39d1-b46d-e9c387b46efc | -7.89458 | -44.49098 | 2025-07-17 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ed46bf47-4d48-3e0b-8e5b-a6884dfa2808 | -6.97854 | -42.81226 | 2025-07-17 03:53:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| d2ded4c6-25b3-3bac-b02e-16157aa817b7 | -4.80465 | -43.22142 | 2025-07-17 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c9dc8cbf-6c4a-3f72-aa8a-4590506d28fd | -7.59197 | -46.33639 | 2025-07-17 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5980afe5-e669-3074-9742-a187332c65fc | -6.71944 | -44.33385 | 2025-07-17 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 87c1ba75-3d2b-394d-bc1f-534a0e859115 | -8.0975 | -43.15231 | 2025-07-17 03:53:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 747a3133-1af0-3ed3-9377-cd3ab47e85b5 | -5.01494 | -38.53305 | 2025-07-17 03:53:00 | NOAA-20 | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| c8f1c21c-58d0-3504-bcb9-961daf112253 | -6.9471 | -42.3726 | 2025-07-17 03:53:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 959dae64-3d2c-317f-9726-c15923ea7f60 | -5.66432 | -43.72206 | 2025-07-17 03:53:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| aae31dfd-d3a7-3a94-89e2-97db79952078 | -6.9961 | -43.74863 | 2025-07-17 03:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9d9671ee-11ae-32b9-9e3d-58e35e0405c6 | -5.59402 | -45.80153 | 2025-07-17 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 23b748db-bcf9-397c-9ca7-dbe595ec9568 | -5.52734 | -43.88981 | 2025-07-17 03:53:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5493cbfb-7eda-3a8c-b8e2-61574c95aff8 | -7.34511 | -44.20269 | 2025-07-17 03:53:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1c37bdbf-77e2-3001-ae1b-5cbdb02aa0da | -3.66391 | -48.31395 | 2025-07-17 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1dc7e486-aff9-3c77-9ce4-96e3d768db87 | -6.42864 | -45.31412 | 2025-07-17 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7f46de40-8fc1-3f15-b4a8-b4e8dd5731ae | -6.66784 | -43.04266 | 2025-07-17 03:53:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ab86f85b-d1d0-3cda-b282-a8049816e71e | -6.99206 | -43.74793 | 2025-07-17 03:53:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 87002f3a-0143-3b1c-a1ad-1c14c94042bc | -3.84179 | -47.75473 | 2025-07-17 03:53:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fdfc98a1-e1f4-30a7-a0d2-cfb65b8728e6 | -4.97528 | -37.1624 | 2025-07-17 03:53:00 | NOAA-20 | GROSSOS | RIO GRANDE DO NORTE | Brasil | 2404408 | 24 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 2a3a81c5-b9c5-3017-a182-0aa6afcee267 | -3.03953 | -49.42881 | 2025-07-17 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec80c4fc-a3b5-32b8-a467-e255a45ee12a | -8.54097 | -47.84865 | 2025-07-17 03:53:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4c923544-cebd-339d-94e9-e9a9328e653f | -6.84126 | -42.74797 | 2025-07-17 03:53:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| caa858dd-2935-3061-9cb6-683cba0a3123 | -5.79261 | -45.09571 | 2025-07-17 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d4922523-153e-386b-9d98-58f417246dc1 | -7.61461 | -44.30602 | 2025-07-17 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 232e9fc6-4592-382b-9e70-c77a6d82c93a | -6.1391 | -43.96197 | 2025-07-17 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5c809382-ca88-3851-8e2a-e3e1326fa13b | -5.2993 | -43.90396 | 2025-07-17 03:53:00 | NOAA-20 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7e85a8be-380c-3e1b-931a-8cc8dcfe42fe | -5.91177 | -45.58418 | 2025-07-17 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0121c6f4-fd9f-3916-8d81-76296697c4b1 | -3.39005 | -47.48199 | 2025-07-17 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| c45d3d10-b0e9-33f0-b2ff-573b0ac83322 | -6.87149 | -41.72565 | 2025-07-17 03:53:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 699a3774-a93e-3fdd-9e05-f04aff70404c | -6.5706 | -43.47559 | 2025-07-17 03:53:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8f92547d-4976-3cfc-89c7-234936e8f2c4 | -6.13705 | -47.30784 | 2025-07-17 03:53:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 8a2eb13b-e940-397a-a423-baf80f3eb158 | -5.91488 | -43.47491 | 2025-07-17 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5d736026-9ce4-3364-8d39-6b2880432c56 | -8.7542 | -46.58574 | 2025-07-17 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8153d0a8-2d4d-38b9-a435-5df8491e26a2 | -3.66321 | -48.31809 | 2025-07-17 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 075900d8-f0ad-3c03-875e-b6887ad94350 | -5.7948 | -45.11027 | 2025-07-17 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a33729d5-21b7-3d35-b233-e18d21c06366 | -5.66019 | -43.7214 | 2025-07-17 03:53:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 0d695e92-6b3d-3ca0-8dea-470970cd6f39 | -5.59488 | -45.79641 | 2025-07-17 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8f3b99ef-8ee5-32c6-8a64-413af7bb683b | -8.87614 | -44.79542 | 2025-07-17 03:53:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 673a3c3b-0b5c-37ba-b35d-2c5339d26d74 | -6.81463 | -43.78529 | 2025-07-17 03:53:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cd818599-fe5d-3c3a-87eb-f0481d938f5d | -7.13155 | -43.29972 | 2025-07-17 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 78993b70-edc7-3c35-bd81-11b9c7335450 | -7.61114 | -44.30144 | 2025-07-17 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b4d8ec44-7085-3036-be99-7476bcc93b7f | -3.39204 | -47.5005 | 2025-07-17 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 88023a66-b22f-38b0-8667-c83e2390c49e | -8.87683 | -44.79142 | 2025-07-17 03:53:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a32600b8-108b-34ab-b269-9c76c94256f8 | -6.72788 | -44.33529 | 2025-07-17 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 5e08c128-85f4-3bab-aefb-a216910d30fd | -6.84889 | -42.74914 | 2025-07-17 03:53:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |


[Clique aqui para ver as próximas entradas](README14.md)
