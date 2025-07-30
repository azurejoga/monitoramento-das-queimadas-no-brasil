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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 809aa918-2d55-3833-a715-152c9141f22e | -6.42258 | -53.31623 | 2025-07-30 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5589a4bb-4924-3d3a-b06a-6b8d5e9c1360 | -3.99276 | -43.229 | 2025-07-30 04:49:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dfe35169-a244-326d-b10c-2ed078cad61e | -6.46284 | -44.56986 | 2025-07-30 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 858d8bb1-f1b8-3dc7-9a15-7a673c7dd902 | -3.85658 | -54.08062 | 2025-07-30 04:49:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fc9cf7ff-218f-30ed-85f6-f1400088fc56 | -6.37066 | -53.34365 | 2025-07-30 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 361b0b26-fc38-395e-8365-b9a21e1f9af6 | -3.47554 | -53.45217 | 2025-07-30 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a99442a5-35da-3329-8f16-99c31470441c | -3.48253 | -51.18853 | 2025-07-30 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b3fed629-9ef8-3d95-90ba-fba3b73df709 | -3.83672 | -48.95929 | 2025-07-30 04:49:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d4b96645-c1b3-3975-b269-74554e2d8ee9 | -6.39386 | -53.36872 | 2025-07-30 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b717474b-eb8d-3b4e-8c71-c1bef47d31c4 | -5.766 | -43.90375 | 2025-07-30 04:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cda64457-aee7-3f3f-8449-53d8a93d74a2 | -3.27692 | -49.13993 | 2025-07-30 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 621802a6-3b5e-36ba-bd72-d17c145888ab | -4.32261 | -48.39655 | 2025-07-30 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fa9cdbfc-b93a-3d13-9a96-9549515fc803 | -3.18671 | -48.8092 | 2025-07-30 04:49:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 01a832d5-26e5-320d-a606-2fef0c5775ce | -6.90555 | -44.72827 | 2025-07-30 04:49:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0b544f07-5798-386a-9f3c-d6a56fdb2cdf | -6.41541 | -53.36143 | 2025-07-30 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| edfa7c1b-047f-35c1-998b-0176f661a1d6 | -6.3911 | -53.32193 | 2025-07-30 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7cbfcd12-db62-326e-a1a9-75d45b56b73d | -6.40105 | -53.3663 | 2025-07-30 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c0eda0a3-5e12-3dc6-8957-8d14a814fb5a | -5.68581 | -43.6787 | 2025-07-30 04:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| db7c74a4-0122-3af9-af68-b8bfe7745e98 | -6.37895 | -53.33426 | 2025-07-30 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| de8fe5e7-5784-3d25-9a4b-1f73c0bcaa79 | -1.64248 | -55.14448 | 2025-07-30 04:49:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 213ba8c6-3592-3219-8d78-7da3b2287e0c | -5.68057 | -43.67783 | 2025-07-30 04:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b310324c-fac5-36c4-b620-a04353b98106 | -6.38779 | -53.36418 | 2025-07-30 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be7f1807-2048-331d-9df6-e24b4deaa5f9 | -2.90949 | -48.24842 | 2025-07-30 04:49:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 7c8fc397-a2cb-3c95-a92d-9fdfdb929075 | -6.45619 | -53.3608 | 2025-07-30 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43b9dce8-b157-351b-8d9b-b9750a93e129 | -3.03389 | -47.86348 | 2025-07-30 04:49:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a3094071-1587-30b3-a6e5-7cd813e06127 | -6.41928 | -53.35849 | 2025-07-30 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5ff5136-49f7-3213-8c4e-99364dadc386 | -6.41983 | -53.35501 | 2025-07-30 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 32c9ba1c-ad76-3ab5-aad7-61c9ff429519 | -6.45564 | -53.36428 | 2025-07-30 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 39434944-0698-37c9-8873-c7164e99e571 | -4.17108 | -48.58062 | 2025-07-30 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ea47fcd-3a74-3164-99d8-9fc33660b5f1 | -2.58579 | -51.9217 | 2025-07-30 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6f37593d-cee1-3d3e-85e9-910105d3c0e0 | -6.39441 | -53.32246 | 2025-07-30 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5dccb877-59c3-3396-b3f0-6f6bbe7cb026 | -5.81923 | -46.35073 | 2025-07-30 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e67200de-ef9d-3f9d-ad2f-03047f0cf4cb | -4.64718 | -43.12523 | 2025-07-30 04:49:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be9e0613-d5fb-3c69-94a6-9f8869f01428 | -3.82168 | -41.56747 | 2025-07-30 04:49:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 56b3babd-c263-3def-8631-7e98931b7758 | -5.68536 | -43.68187 | 2025-07-30 04:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6b645f4c-a225-3cdb-96c6-7efb43425b48 | -2.91923 | -48.67343 | 2025-07-30 04:49:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 085486eb-426f-3344-a176-410467a53ac7 | -7.30917 | -44.69247 | 2025-07-30 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de9a610b-bdf1-34ef-8a62-8076196c1162 | -6.25351 | -46.12167 | 2025-07-30 04:49:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2b1ebae0-2db7-3a79-b7d6-732b726cef6d | -6.39552 | -53.35829 | 2025-07-30 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d1b7018-ad41-38dd-8efa-08decd50b221 | -6.39497 | -53.36177 | 2025-07-30 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 566f7fb1-32d2-3f39-a9cf-85e4467b7b4b | -6.38723 | -53.32489 | 2025-07-30 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5e6f5d19-184b-35b6-882a-0f062fd14a4c | -6.39658 | -44.74836 | 2025-07-30 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 68089be6-6122-33a5-9d78-109d8b67b30a | -3.96984 | -50.87466 | 2025-07-30 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef519af2-15d6-3806-936d-fd0946fd8c43 | -7.06622 | -44.95783 | 2025-07-30 04:49:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| be95381a-eaff-3407-9309-868ac24e7de2 | -6.4132 | -53.35395 | 2025-07-30 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2c7e2b4-7098-3d1e-be89-8aebb9e1bed4 | -6.40657 | -53.37431 | 2025-07-30 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 47996f40-1da1-3adf-9f35-3be7f07cd812 | -6.42589 | -53.31676 | 2025-07-30 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ec513976-eee3-3368-9b4a-d468e048515f | -4.80054 | -48.56504 | 2025-07-30 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 807811aa-48c7-35ed-aae0-8a2c2be5f53e | -6.11935 | -53.68411 | 2025-07-30 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5af03ff7-f3d2-3ff6-8e4d-336cb73a0446 | -6.25158 | -44.07417 | 2025-07-30 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5d2df6d7-baff-3852-a9b5-bf42eb7beebe | -5.7608 | -43.90311 | 2025-07-30 04:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5367ea4c-bcbb-39b5-90df-f5c4913e9a9d | -4.06794 | -48.26201 | 2025-07-30 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 262e9c6f-3fb5-383d-b03f-00a480e74230 | -4.28793 | -48.06359 | 2025-07-30 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8fa06368-805f-3a3c-9473-32302081c9d9 | -6.40436 | -53.36683 | 2025-07-30 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5d9dee51-4951-39e7-8cbb-1af02d76c6cd | -6.40383 | -47.66605 | 2025-07-30 04:49:00 | NOAA-20 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| faeadf76-0e29-33c0-a9c3-7b64853fe269 | -6.41597 | -53.35796 | 2025-07-30 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd44290a-838f-310a-9efe-e0f41e0cefcc | -6.38226 | -53.33478 | 2025-07-30 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a0d316ad-066b-3f19-a7cd-fa94622dfca9 | -7.05768 | -44.96148 | 2025-07-30 04:49:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 11b63536-32f3-3444-ad6e-1e91610f0b0e | -6.41265 | -53.35743 | 2025-07-30 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 927820c0-4b9d-3ef9-8d81-743d6f4d0086 | -6.25115 | -44.07724 | 2025-07-30 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b2d7f3a5-72a1-3707-adf3-aff0d8c31120 | -6.38281 | -53.33131 | 2025-07-30 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 97b1f337-343e-336d-9be6-7f45e4ae1efc | -6.3795 | -53.33078 | 2025-07-30 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b26fd8f8-6bb7-3363-b225-5b5051f255c1 | -3.88484 | -41.03567 | 2025-07-30 04:49:00 | NOAA-20 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| df3cd431-9da1-3d4d-8df1-ac9d2016b826 | -4.65029 | -43.1248 | 2025-07-30 04:49:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a55bcf38-7848-366f-8f65-0030dc5abdb5 | -6.70807 | -44.35854 | 2025-07-30 04:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| be185f9d-8473-319c-9bb4-188c7babe1cb | -3.88553 | -41.0311 | 2025-07-30 04:49:00 | NOAA-20 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| da795948-d42f-3323-adcc-2ee48d636927 | -4.65663 | -43.11879 | 2025-07-30 04:49:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c3e91824-a2a9-3512-8738-0ed40ac775b1 | -6.7034 | -42.05005 | 2025-07-30 04:49:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| bc270d23-d17e-3760-8248-c7305be0c97c | -6.3922 | -53.35776 | 2025-07-30 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4880147c-0e57-32ad-b10e-4dc9db6fde75 | -4.65077 | -43.12139 | 2025-07-30 04:49:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 12f82e89-eec1-3b7c-82a7-fa0698c825ac | -6.69745 | -42.04928 | 2025-07-30 04:49:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0feeaf7d-a00b-398d-a9ca-4cfc7060ca7d | -3.58506 | -52.54415 | 2025-07-30 04:49:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ba8761e1-5b7c-3d21-a5a4-5ad5a926dcab | -6.11601 | -53.68357 | 2025-07-30 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0b9c20f8-9034-3aa2-b8a9-c81bccdff57b | -5.48031 | -42.15511 | 2025-07-30 04:49:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e640e57e-86ad-3d17-9373-a721b8e49931 | -5.67487 | -43.68024 | 2025-07-30 04:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ff480f28-d0dd-344e-8b33-6a3eef8a4548 | -2.60512 | -51.94933 | 2025-07-30 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f3421627-65b3-3377-99f9-348447cccdac | -7.14869 | -47.4254 | 2025-07-30 04:49:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fb261d40-5b61-329b-b348-f52c02b2f4e5 | -7.30958 | -44.68965 | 2025-07-30 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ebe52014-da9d-3233-8248-1f997b4dd961 | -5.83322 | -44.03764 | 2025-07-30 04:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1d0e2318-9291-335d-8e44-d8bd3cfb67ec | -4.65126 | -43.11799 | 2025-07-30 04:49:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| fe025ec5-74b2-3797-89db-d671b1a18d8d | -6.25177 | -46.11929 | 2025-07-30 04:49:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 15001d25-1a03-31de-996d-bcae5ed3611b | -6.46244 | -44.57273 | 2025-07-30 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7497d60b-c626-3547-8e4c-e48831093b7a | -5.67533 | -43.67701 | 2025-07-30 04:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e8cf7193-8d2d-3791-80fb-9cdc9005bf64 | -3.88563 | -41.03685 | 2025-07-30 04:49:00 | NOAA-20 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f4f8a066-cbd5-3603-811b-262be45eab37 | -6.39165 | -53.36124 | 2025-07-30 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc34170b-a729-3952-b5c2-d6d00f049b5f | -2.90454 | -52.54997 | 2025-07-30 04:49:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fa505946-2515-368e-b77e-77f376c3a0b1 | -6.40768 | -53.36735 | 2025-07-30 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 775046ba-a0f4-3ee8-afad-e25988056659 | -6.41652 | -53.35448 | 2025-07-30 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d58a187e-f82e-3f2c-9369-100dfecddf48 | -2.90578 | -48.24785 | 2025-07-30 04:49:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 0ab3f633-18a9-36ea-8278-0c63ee354310 | -3.32792 | -48.7169 | 2025-07-30 04:49:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b04a75b-bb29-35d9-ac8b-16d25a795105 | -6.71398 | -44.35361 | 2025-07-30 04:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6168057-9cda-35bc-9560-301b6c4b7bd7 | -6.37839 | -53.33773 | 2025-07-30 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 77c0f9b6-5ae8-3ee7-9385-493f5d342e35 | -1.50406 | -47.46999 | 2025-07-30 04:49:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b0c6ef02-23db-3685-9898-353573159683 | -4.85316 | -42.99517 | 2025-07-30 04:49:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e88e217-a42b-3081-8b80-c670634338a0 | -4.79975 | -48.56244 | 2025-07-30 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fbd15fd5-9973-3131-945a-fce746098641 | -3.29781 | -49.19249 | 2025-07-30 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9b95b68e-e9a0-3a1c-9a67-ce3efb76e7d0 | -3.27336 | -49.13939 | 2025-07-30 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 744cff4b-979d-346e-882f-ab599fafa1f0 | -6.41595 | -53.31518 | 2025-07-30 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 66df31dd-afd1-304d-9eb0-c15cd2e72887 | -6.40932 | -53.31413 | 2025-07-30 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 542bceb9-17bf-3438-8c00-79bff951b90b | -3.58065 | -47.52048 | 2025-07-30 04:49:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README27.md)
