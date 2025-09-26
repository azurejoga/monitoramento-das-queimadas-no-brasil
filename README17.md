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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2e8dbf79-b86b-39c4-bdeb-44e7223d7cb6 | -5.73649 | -44.96981 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 344e1426-0070-3c8e-9ad7-0e07f708cecc | -7.38208 | -48.16312 | 2025-09-26 04:14:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 83fd82db-1900-3eb2-ae22-ef4dcbcc5964 | -4.17522 | -44.27216 | 2025-09-26 04:14:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 72ebcbd7-d9b5-3908-ae11-b621e803d900 | -6.80826 | -43.765 | 2025-09-26 04:14:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 002cc7b6-368f-30db-a5bf-11cc199c1c8b | -5.73918 | -44.99702 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7668aeb1-9508-32f6-872f-029dc1f7297c | -3.80686 | -41.56545 | 2025-09-26 04:14:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 4a6eaeed-7748-3f12-8b26-6ad18c1cbab6 | -10.40687 | -46.17072 | 2025-09-26 04:14:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 71f52c21-5fd1-308b-96a5-deb8908958e0 | -7.13025 | -42.20175 | 2025-09-26 04:14:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9490211b-c0f7-3330-bb4f-365af2741eea | -7.67112 | -47.42652 | 2025-09-26 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cc268a3b-58ff-35a6-bf12-48f28eda664b | -4.06273 | -41.78012 | 2025-09-26 04:14:00 | NOAA-21 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5be6062a-5b43-3647-a5fd-ce6a3d3fc393 | -9.87402 | -48.87519 | 2025-09-26 04:14:00 | NOAA-21 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6eeb515e-4aa6-33e7-b36d-e363a1249d8a | -8.65617 | -44.02906 | 2025-09-26 04:14:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 33ae092e-81e1-3e07-9b31-990393a81dcd | -5.46457 | -43.06757 | 2025-09-26 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 14ab83da-8001-3b85-bb6a-dbc9917be07e | -5.73025 | -44.96505 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 55f3d952-1862-36f4-a3e6-846a6f0858ae | -4.1758 | -44.26855 | 2025-09-26 04:14:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9a92ad8d-2cf1-3a20-911d-851b42be197a | -5.21978 | -44.48787 | 2025-09-26 04:14:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 76a9852e-d6e1-341e-aac5-9dd5fc4c4052 | -8.03092 | -42.07231 | 2025-09-26 04:14:00 | NOAA-21 | NOVA SANTA RITA | PIAUÍ | Brasil | 2207959 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c3fbcef9-9682-3478-985c-d79f6dcf8b24 | -3.51764 | -44.03663 | 2025-09-26 04:14:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 41e58d0d-0e8e-36f3-afbe-3f9b43d0be65 | -5.07863 | -41.19032 | 2025-09-26 04:14:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 01274df1-5486-3e81-b385-168fed805082 | -7.77672 | -47.39993 | 2025-09-26 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c3dcbff2-47a9-31fc-894a-4065f8aba358 | -3.81406 | -41.56298 | 2025-09-26 04:14:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 901560c9-6eef-319c-a33b-c1294ccdb52b | -8.28104 | -44.95276 | 2025-09-26 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a33cb6b4-44de-3e41-8bc0-627afe98b8b0 | -4.42785 | -47.26793 | 2025-09-26 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 605c8aed-142c-3275-8456-bfe8f3af785d | -8.8502 | -46.25172 | 2025-09-26 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ff4a510c-2b6d-351d-8ff4-dcbbfd6b3c33 | -10.93085 | -44.29966 | 2025-09-26 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fad1b0bd-82fa-398c-be28-2f96ee4984fd | -5.77695 | -42.81401 | 2025-09-26 04:14:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c74d3b8a-d472-3337-a173-3158e9647548 | -4.26268 | -48.55404 | 2025-09-26 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b40890ef-f5a0-3773-8444-ca386fb8009f | -5.79996 | -42.79644 | 2025-09-26 04:14:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| a4129ab5-e1d1-39c7-a12c-215dc4048ff3 | -5.20719 | -43.73149 | 2025-09-26 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eb3ec3ea-f39c-329f-b8c7-54dcca463620 | -7.19961 | -45.35658 | 2025-09-26 04:14:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d99d4b8b-e3ba-333f-8ba6-632e40163796 | -4.74626 | -42.32734 | 2025-09-26 04:14:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d08eb12c-3369-344c-b320-f0594a11c16e | -5.78937 | -42.75599 | 2025-09-26 04:14:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 5dab958b-8814-3321-841b-43928c57f0ac | -10.40625 | -46.17451 | 2025-09-26 04:14:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad5f77d4-91bf-3b75-81ad-0ee023490862 | -10.31079 | -45.22633 | 2025-09-26 04:14:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e3203da6-c2a1-3a23-8289-668be81172e4 | -6.962 | -43.24165 | 2025-09-26 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| e02450cc-8ac4-3a74-8899-0cd3e80396f1 | -5.74049 | -44.96664 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| b9d9829b-d8b8-34b4-9f45-9ec3af69ff02 | -4.82123 | -42.74422 | 2025-09-26 04:14:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 16.4 |
| fa425632-8ae8-391d-b622-7e781be5da75 | -6.42284 | -43.07821 | 2025-09-26 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 171ea35f-c633-3a82-b5b2-2e38effda843 | -6.71656 | -42.74275 | 2025-09-26 04:14:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ab49d1a1-282c-36eb-ada5-f980ae2d8974 | -7.05214 | -46.40538 | 2025-09-26 04:14:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 50a497dc-3d00-30bc-a446-cc53050a2a54 | -5.03075 | -42.8619 | 2025-09-26 04:14:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0e591677-c4e7-3e1f-9bc6-913b8aad68ec | -7.54761 | -46.39892 | 2025-09-26 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d18bc0a4-1538-31b3-aa00-0f97552112ed | -5.20497 | -43.724 | 2025-09-26 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a51066b3-215e-3105-8686-7ae6d41ae9e1 | -9.0078 | -44.10685 | 2025-09-26 04:14:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| aeed1644-dc41-3abc-98b8-1186fba89297 | -8.6644 | -43.99833 | 2025-09-26 04:14:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9a1a8fcc-89e0-3f5f-887d-19748734c683 | -3.80631 | -41.56896 | 2025-09-26 04:14:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 454b2780-2431-3e28-be83-23151a536525 | -7.27927 | -42.97695 | 2025-09-26 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7fc7d3da-8c91-3ea8-87e9-39d38df582af | -8.72794 | -45.42238 | 2025-09-26 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 75198a34-59ae-37c5-9682-388de8a25da0 | -4.75248 | -43.26871 | 2025-09-26 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9daa7d02-79fe-3a9e-8fd5-c4d5423eb0e1 | -5.72106 | -44.97888 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9247cc29-1eb0-30e7-9392-553e1f012600 | -5.54171 | -42.81195 | 2025-09-26 04:14:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| dd7a1fa4-757f-383f-b1d7-a49460049a98 | -7.11091 | -43.74593 | 2025-09-26 04:14:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8f62d0d4-2512-31cc-b46e-64c026032341 | -7.28258 | -42.97746 | 2025-09-26 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 68aad827-80a1-3d2f-b965-eb3a6b2684b7 | -6.11899 | -44.22827 | 2025-09-26 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2336d513-f308-3766-9c8e-a1d1a7118746 | -5.94391 | -42.93935 | 2025-09-26 04:14:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f5307ff2-7ab8-3a32-9577-db2521b93846 | -5.72507 | -44.97567 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c7e92c82-7d0e-3319-877f-08d20e99c6b1 | -5.74498 | -42.55833 | 2025-09-26 04:14:00 | NOAA-21 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 83eb7741-7bf4-3e78-ac87-b02fa907b3dd | -3.83939 | -50.96842 | 2025-09-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7e0274b9-ad94-317f-89c2-2917cc3d1599 | -9.24567 | -44.26299 | 2025-09-26 04:14:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e71205b-81b6-3652-92a1-42edf9baffd1 | -5.74319 | -44.99383 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 99bea08e-5977-3b8a-be47-a06bd6d66f55 | -6.2318 | -44.65845 | 2025-09-26 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c05e03fd-653e-350d-a8dc-b75e60c51e5f | -5.79728 | -42.81367 | 2025-09-26 04:14:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 45957675-75f5-333b-9f83-3fcffaf42c2b | -5.79528 | -42.86973 | 2025-09-26 04:14:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 9d487573-4b59-3889-aba1-fc57807114fd | -5.37525 | -42.28777 | 2025-09-26 04:14:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b2018b7b-6b9e-3f3d-845a-854769e1727d | -5.73942 | -44.95135 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3d15fd84-f6f8-3a32-9bbe-cdc82d845360 | -5.72743 | -44.96083 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7fdf2c3a-06e9-31b9-bf31-75529efbe749 | -5.74259 | -44.99756 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 10d8016e-3ba7-30ba-8b10-14548aacdd7d | -6.31952 | -41.88024 | 2025-09-26 04:14:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 542f09c7-df31-35e9-8403-3035853b0567 | -5.64339 | -43.92203 | 2025-09-26 04:14:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d978fbbd-d6a7-3b3c-9c4a-5bbd13aec17b | -5.30762 | -42.76488 | 2025-09-26 04:14:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f3645e51-2271-31fb-9f3b-654f41eb2276 | -4.95566 | -42.64602 | 2025-09-26 04:14:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7c00fb5e-53cf-3371-ae6b-69a9075a76d3 | -9.75688 | -45.9534 | 2025-09-26 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7a57941a-15c9-3a69-a4d7-9b8e2c4c3e62 | -5.39254 | -45.85258 | 2025-09-26 04:14:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| de2458a9-9e66-3400-a340-feaecaa2a704 | -2.96363 | -48.59238 | 2025-09-26 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c856e658-f0db-3ae7-b0d9-bb3706e40c62 | -5.64505 | -43.93304 | 2025-09-26 04:14:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 351a220e-67ff-37d2-9a9a-2ed1e72a803c | -3.0581 | -48.7064 | 2025-09-26 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ebed9af3-5a4a-3d30-aecf-41ec1bb6a151 | -5.64007 | -43.92149 | 2025-09-26 04:14:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 7d3d32c7-0642-3ceb-9971-dcceeb0c4700 | -4.0061 | -43.27451 | 2025-09-26 04:14:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cc7fd289-7ece-3b27-af70-8ea23750ea26 | -7.04718 | -46.42174 | 2025-09-26 04:14:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2deaf0c0-b7e0-33c8-9fc5-703837a2df04 | -5.74378 | -44.99009 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| df90f2ec-e091-302d-a1e5-933f04f975a7 | -2.79201 | -49.5994 | 2025-09-26 04:14:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2dae0b48-c89d-3a4b-9bbb-1862f547cf9f | -5.38464 | -42.29278 | 2025-09-26 04:14:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1d06f741-9291-3dc2-9977-3a6b73f1787d | -6.12232 | -44.2288 | 2025-09-26 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 23c74097-2dea-3d66-b846-7fdf555ae255 | -5.78485 | -42.87164 | 2025-09-26 04:14:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 454853cb-a664-31dc-b5dc-c97093f99f62 | -5.629 | -43.92689 | 2025-09-26 04:14:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 033d0f68-94d7-303b-96cd-e62c794a1e40 | -3.05372 | -48.70575 | 2025-09-26 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e798a442-c55c-399e-9771-514b659339eb | -7.28588 | -42.97798 | 2025-09-26 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b9c797d7-4fae-38d4-8b6f-a0a57fbb9466 | -6.26095 | -42.47977 | 2025-09-26 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 675c9991-336f-3291-9ee2-2ea8404c54f6 | -8.79466 | -46.58901 | 2025-09-26 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 68f864fd-9a9a-345b-8f65-facef8245c99 | -5.75072 | -44.96827 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 45198599-4669-3e8c-920e-142764c0d95a | -10.0082 | -44.17175 | 2025-09-26 04:14:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2902a824-6d1e-31e5-8b19-b5f5ffd964b7 | -8.79061 | -43.05824 | 2025-09-26 04:14:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| aed42162-79b9-3f7a-b8f1-ca37bb7ffe7c | -5.77856 | -42.80368 | 2025-09-26 04:14:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1f79ec83-048e-3f53-abc6-8393c4591220 | -8.3271 | -49.53005 | 2025-09-26 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c38eef12-2944-3110-bdce-2ff089c7e970 | -7.04943 | -46.42173 | 2025-09-26 04:14:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7bed267d-c20b-398b-8ebc-c2c0f00a4138 | -2.19635 | -54.46569 | 2025-09-26 04:14:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 547c6d59-5a95-3c95-b9e9-e4ab47bdc2a3 | -10.94294 | -44.28729 | 2025-09-26 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2d32e95d-f17c-33a7-90dd-a7bda5dc88d2 | -7.31465 | -45.75492 | 2025-09-26 04:14:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 50257e18-cc2d-3483-a1a4-3a3acd7681f5 | -5.78248 | -42.82195 | 2025-09-26 04:14:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 64d552ea-0c43-35e8-b834-00c9da32512b | -5.73531 | -44.97724 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |


[Clique aqui para ver as próximas entradas](README18.md)
