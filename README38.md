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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3d87d031-ad89-386a-9530-ca5afac322ed | -14.75178 | -45.60355 | 2026-09-24 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fb054947-bf60-3d58-b51a-93a9a7d1cadc | -13.07212 | -43.28551 | 2026-09-24 04:10:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e2cc02a0-bd4e-32ce-ba23-0e51cfa977ce | -14.7533 | -45.61556 | 2026-09-24 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 90fafb70-a00c-3d32-97f0-708cf5a827d3 | -11.91882 | -50.73048 | 2026-09-24 04:10:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 62b293e0-92e1-3da7-b8e5-c256ba38f9cd | -13.81805 | -51.85841 | 2026-09-24 04:10:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e17d0b7a-c873-3d97-91df-638346639cff | -12.16518 | -47.36893 | 2026-09-24 04:10:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9a9d1367-0c0c-3548-ab34-9633c9f599ea | -11.69926 | -44.49168 | 2026-09-24 04:10:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 997efb76-0996-3599-a32d-8198992381d2 | -10.97655 | -54.09639 | 2026-09-24 04:10:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 063c4852-0093-336a-adbc-6a2a9273cb66 | -12.04691 | -50.2881 | 2026-09-24 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0af592f7-a4f8-3385-a0cf-f56910621f3c | -10.27252 | -49.96112 | 2026-09-24 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 90f7cee2-1c2e-3f1e-a488-0d499581ce5d | -11.40242 | -47.39071 | 2026-09-24 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 687ab92d-0485-3f68-9951-57527c14f2ea | -10.65175 | -51.32338 | 2026-09-24 04:10:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08445851-81ae-363d-b868-bb1a7cdd36e1 | -10.08129 | -46.06208 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bb43d803-e686-362c-8950-b4beaf7e9402 | -10.08055 | -46.02235 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4d9660fb-df2b-3843-b3a8-ca87e326dd9f | -11.65111 | -43.49374 | 2026-09-24 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 707f7bbf-b2dd-3dbf-8dcc-3022d546cc82 | -10.11504 | -46.01806 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 920645b7-7f82-34d5-ac4a-46019e97716c | -11.93973 | -38.29682 | 2026-09-24 04:10:00 | NOAA-21 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| a539c377-44d2-385e-8d91-70d863cc32a7 | -11.36319 | -43.37804 | 2026-09-24 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d68174ef-b8ce-3e96-b726-e1f77f37543c | -11.30932 | -44.03611 | 2026-09-24 04:10:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35a2d1d9-3b45-3214-a79e-fb06f60684b2 | -11.4132 | -47.39761 | 2026-09-24 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| e3145c18-0eac-396c-9e11-3eb37852caf3 | -15.35486 | -48.12697 | 2026-09-24 04:10:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0a601725-ab36-3a0c-a817-91bf267c52c3 | -10.4344 | -46.26546 | 2026-09-24 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 67bcefa2-8b9e-37f1-9dbf-3fd83532b9e5 | -9.58043 | -47.96915 | 2026-09-24 04:10:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5826be99-dea3-391a-b2b6-5f68528c87bb | -11.70058 | -43.46199 | 2026-09-24 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c9ce6b85-37df-3f71-a451-d562e7b9a49e | -13.73311 | -48.97459 | 2026-09-24 04:10:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 80941d7a-2349-3bfb-af59-eac9b866f752 | -13.82353 | -51.85792 | 2026-09-24 04:10:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 12489673-a5ac-30d6-8ff5-ac85c189b07d | -11.49252 | -42.33236 | 2026-09-24 04:10:00 | NOAA-21 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 5b0a057b-cd2b-3f41-856c-dffea6e3d60f | -10.56248 | -44.61068 | 2026-09-24 04:10:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c519a62d-ea91-395f-a2bd-677144081ed6 | -11.48633 | -47.3295 | 2026-09-24 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0de500f9-0052-31dd-b9d9-aea05af2ecfa | -10.4619 | -44.95054 | 2026-09-24 04:10:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| af726c61-52b6-3cf4-8265-d0f44190777a | -13.08208 | -47.40349 | 2026-09-24 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ad9507f8-332b-3d43-8e48-72b5ada40039 | -10.07464 | -46.01267 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 9cda5df0-eeb8-3349-8348-3ec1fc12f98c | -14.75115 | -45.60737 | 2026-09-24 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4c6dec58-7ea4-3f1c-9ee0-e4d7bb39d0b8 | -11.24288 | -51.36317 | 2026-09-24 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b1624439-b138-3aea-ae03-d9707a0beee0 | -11.16511 | -42.84291 | 2026-09-24 04:10:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 1af024ac-b2c1-32e5-b23c-abe87bf40b49 | -12.14333 | -50.74511 | 2026-09-24 04:10:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 683a4294-5af6-3fee-a1f7-32960be2511f | -10.08491 | -46.01865 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 5f8d823e-e5c4-36cb-9afb-796b61b55986 | -11.28813 | -51.31603 | 2026-09-24 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d4501e27-d1a7-3bcf-85ff-711a7e35eca4 | -11.64727 | -43.47506 | 2026-09-24 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3b09eab2-4ea5-30bd-b43e-769c859a8a9b | -10.07761 | -46.01745 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| a9ce67b5-16db-33f0-901d-49a051f692cf | -10.11432 | -50.20429 | 2026-09-24 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6c26d89b-b5e5-3d60-b8b3-4e5efae43b64 | -10.07162 | -46.0082 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a4979832-176d-3fd7-b85d-864b59c868d6 | -13.1796 | -51.54235 | 2026-09-24 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 1d8ee33c-f2e2-3470-969f-7d4face3bbde | -11.24062 | -51.4031 | 2026-09-24 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1b0e1fba-a42c-3684-8efc-4ed41e24899d | -11.4909 | -42.34286 | 2026-09-24 04:10:00 | NOAA-21 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| fab42d72-06a1-3d1d-bef9-fd9433e8ff34 | -12.85303 | -44.39037 | 2026-09-24 04:10:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e3e1616f-979d-37f9-8c85-a95b3de9aadd | -10.66258 | -42.61864 | 2026-09-24 04:10:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 38faa844-125f-3201-9abe-47cc6633b810 | -12.13852 | -45.6278 | 2026-09-24 04:10:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| efd0c7e0-f472-3684-bf87-5e631c4ae6c7 | -10.41568 | -49.35359 | 2026-09-24 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 570fb710-b1fd-339c-becd-97f74dc3f0ce | -9.98998 | -50.23611 | 2026-09-24 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0ed1f4da-6fc0-3395-8269-345d5f1796ae | -10.07471 | -46.05647 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d5915b5e-18ab-355c-bbef-83f45e7bbab5 | -10.41404 | -49.36272 | 2026-09-24 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 0f5c2a7d-8527-3360-9f35-f42a9a018b68 | -10.41935 | -49.35887 | 2026-09-24 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 3659db4e-4c58-3594-9b41-3868bfc2833c | -11.95925 | -50.75225 | 2026-09-24 04:10:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3265078b-533c-31fd-bcbb-7493de6e4f89 | -15.24791 | -43.26671 | 2026-09-24 04:10:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 4.3 |
| f61344cc-8712-31dd-bcdf-e290c71d0739 | -10.94321 | -43.85833 | 2026-09-24 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| fde5ac84-65de-30fb-9598-a47d885e8552 | -11.11325 | -48.29827 | 2026-09-24 04:10:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dccc4631-2a19-3d21-8c90-054b9c3bcf14 | -10.884 | -45.07788 | 2026-09-24 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8b23d61a-0d30-3430-b945-7de443e0c246 | -12.14268 | -45.62443 | 2026-09-24 04:10:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0bcbc37d-85cf-3415-adf4-e498ed73410d | -9.86106 | -48.51073 | 2026-09-24 04:10:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 6544ff75-b4ba-3251-a4b0-383b6c79f628 | -11.12935 | -48.32751 | 2026-09-24 04:10:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bd07b58e-fda0-32b8-9992-ab079f666ac7 | -13.78893 | -54.06213 | 2026-09-24 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ba255579-f38d-3c4f-99b6-55e8f890affd | -9.87249 | -48.31725 | 2026-09-24 04:10:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 49a26cab-5f05-34f8-acd0-87dd3cf2c817 | -14.75204 | -45.62316 | 2026-09-24 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d69357da-1595-359b-a699-7d5fcf2bb473 | -10.61421 | -54.00514 | 2026-09-24 04:10:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9c857692-d123-353e-8c2e-758b4aabc93e | -11.79207 | -50.05629 | 2026-09-24 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e5a5335b-2902-387b-9ea0-7629ce5b2dff | -10.10019 | -50.19848 | 2026-09-24 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 080da5a1-4ab8-3989-83ea-74df217f0b25 | -11.12382 | -48.33467 | 2026-09-24 04:10:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9fc89b37-dac6-32cd-898c-23b3ec52a32c | -12.1507 | -47.36143 | 2026-09-24 04:10:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3e3a9159-9557-377a-982c-70007acb83f2 | -9.9704 | -47.98569 | 2026-09-24 04:10:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d3ffe4a4-32d1-3daf-9150-13197c9f8f1c | -11.25072 | -51.34914 | 2026-09-24 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3825a152-afab-3a66-8f75-0add6e35da05 | -12.41534 | -46.95229 | 2026-09-24 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 449b00be-fe47-30b9-9fb0-c55c82b40e49 | -11.12978 | -48.30103 | 2026-09-24 04:10:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 42540c2b-e52f-330a-abb5-d050c7f9a6ff | -11.64616 | -43.4821 | 2026-09-24 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1da0d32c-42d3-36a3-afd9-0e88f9832c77 | -10.08442 | -46.02152 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e2124838-f0aa-37ed-b17d-9de3c0d2404c | -10.09312 | -46.05896 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7d6556cc-38b5-3cc9-bdf6-05ed0d6b6f82 | -12.0386 | -50.28815 | 2026-09-24 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6f493506-2448-3576-85ee-50fcdbf27b35 | -10.08288 | -46.05276 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| e0f6bd5c-1d10-3087-a0c8-cbac3bb7d7e2 | -11.68 | -41.45457 | 2026-09-24 04:10:00 | NOAA-21 | CAFARNAUM | BAHIA | Brasil | 2905305 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 50643586-5a6c-3222-9a8f-0caa18ffb667 | -11.42875 | -44.18507 | 2026-09-24 04:10:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3c0c59c2-b20c-35ab-af4d-13bcfba54d63 | -11.43165 | -47.40643 | 2026-09-24 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7db4468e-2ee5-3714-9c30-56b4c94697c7 | -10.08511 | -46.0396 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ad41cccc-4087-311c-b08a-405ccd200909 | -12.13856 | -50.74421 | 2026-09-24 04:10:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 7022e374-5bc4-383d-bfd2-845e8a7b1788 | -12.15453 | -47.36211 | 2026-09-24 04:10:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 59fb66e6-38e3-338a-acc1-bf4b184482dc | -11.24568 | -51.40405 | 2026-09-24 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad3e2374-077c-3880-86b5-acaeefe8799f | -11.40931 | -47.397 | 2026-09-24 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 08a85d71-996f-39c8-a682-37583edf69b7 | -12.77617 | -51.29701 | 2026-09-24 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b2248813-5f6b-35eb-adff-80ed6bbfaad0 | -10.08586 | -46.0352 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cf21fe15-289d-3ccd-aa58-50ced49d370b | -11.48777 | -47.35774 | 2026-09-24 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0c3a8782-ec74-3d2a-8cf3-a70b7016a824 | -11.30701 | -51.37667 | 2026-09-24 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e0bd907-137b-3213-aba8-f4b2b7655567 | -12.85558 | -44.39051 | 2026-09-24 04:10:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 29636246-aaa0-3ac0-a019-e3e704e6df8e | -12.14809 | -50.74601 | 2026-09-24 04:10:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fed18034-79e3-372d-83af-50c22acfde17 | -10.28086 | -49.95512 | 2026-09-24 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a5a6df63-7079-3f74-b6fb-4b6dd7dd98e0 | -13.4597 | -46.28696 | 2026-09-24 04:10:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0fcccbff-c26d-36ed-9701-f378f02479f4 | -9.8446 | -48.47872 | 2026-09-24 04:10:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c570545f-9f06-3e39-9d1c-fc47721282c6 | -16.4061 | -43.36 | 2026-09-24 04:10:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1b070411-4dab-3eff-8b92-cb0c82e87f43 | -10.12534 | -46.04624 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ea378080-a0ec-32ab-bca8-e644de967b06 | -12.13953 | -50.73896 | 2026-09-24 04:10:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 6f728a37-1e97-33c5-8fce-65e8af5c72dd | -11.79577 | -50.06192 | 2026-09-24 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1c394b71-f13d-32df-ab5d-87c794ea9782 | -10.20618 | -44.1426 | 2026-09-24 04:10:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README39.md)
