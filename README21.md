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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bf6ae011-7ee0-3dc3-8cf2-974be359870a | -7.14879 | -44.19345 | 2025-08-19 04:25:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c9904934-8bfb-35be-adfb-0d2a64b3b78a | -5.87062 | -48.11929 | 2025-08-19 04:25:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b3348b41-b6ae-3438-b44f-bcdb85270ab7 | -4.49032 | -47.68099 | 2025-08-19 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0af8a109-def0-3c0f-864e-bfa27785823c | -5.57704 | -44.0838 | 2025-08-19 04:25:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| d2afbb59-7f6c-3068-a332-7e7e1325fba4 | -5.9256 | -46.00088 | 2025-08-19 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 73305fe9-5922-33e2-8b95-c0cc5f8d122f | -4.60401 | -43.30896 | 2025-08-19 04:25:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 58145b16-3967-3d8d-b29c-bc3102896b5b | -6.95094 | -43.6082 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0f6379ec-2330-3681-9d10-7ae0ea1e428a | -3.97711 | -42.52082 | 2025-08-19 04:25:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| fb083c98-af9a-3f34-b1f7-06a7c95232d6 | -4.54563 | -46.68829 | 2025-08-19 04:25:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4f08613f-d181-3eb2-a39b-e1e06804dbe6 | -4.66416 | -42.84838 | 2025-08-19 04:25:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5655bb60-3836-3bf9-8f9c-17a8e2dfa3c6 | -5.89912 | -45.5347 | 2025-08-19 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.2 |
| d93521df-365c-3bc3-8dc5-e3d882e73111 | -6.14234 | -42.70206 | 2025-08-19 04:25:00 | NOAA-21 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1ec924c8-34f0-38ff-84b4-d41ff110bb91 | -6.42111 | -42.49213 | 2025-08-19 04:25:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c37aeea1-d34d-3a91-8ec2-0cbe0e2ecf8a | -6.96287 | -43.60167 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 5f4899f7-a6ce-3c37-89fa-9c7b9e8ddef1 | -6.09269 | -44.58819 | 2025-08-19 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5354fe6e-7860-3d14-a0ce-0d6d6b215ba9 | -6.93906 | -43.58969 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 17049666-fa53-3692-90e3-7ac9def15a62 | -6.16714 | -47.27762 | 2025-08-19 04:25:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e1f0a7cc-404f-3989-bf20-2b159dc44e65 | -4.15071 | -46.45227 | 2025-08-19 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3913e021-dda9-3dba-bb5b-1e3b0d4b08be | -6.93785 | -43.59789 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 00e2ddfe-85e1-3b4e-9fe0-64235747c624 | -6.9456 | -43.59488 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| daaab01e-3cdb-36fb-ba15-a88243822dfe | -5.97523 | -44.11998 | 2025-08-19 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 01f6c013-b40d-35fd-9902-eca14ff96813 | -5.42767 | -42.35273 | 2025-08-19 04:25:00 | NOAA-21 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 72306466-49f8-3aa1-9936-f96d39df269a | -5.63726 | -41.266 | 2025-08-19 04:25:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a8a7a059-ed38-3f19-97c5-21f12df1138a | -5.88366 | -48.12506 | 2025-08-19 04:25:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cf8b458d-0d00-3b6a-8c6c-cd39158ad634 | -5.9742 | -44.28496 | 2025-08-19 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1e82ad80-ba82-3fdb-9fde-bdc77c069307 | -3.48329 | -48.44278 | 2025-08-19 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1cd24b35-2855-3b49-8099-000fe0169511 | -7.57975 | -45.43681 | 2025-08-19 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4490be4d-c626-35b2-b497-dec0d5fd99aa | -7.38043 | -44.27409 | 2025-08-19 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 33c05a3f-11af-3744-a73a-04467fc99dd6 | -3.9844 | -43.24023 | 2025-08-19 04:25:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 27c868fc-9d81-36cb-82b2-1ac5cf6350fc | -6.65666 | -41.76838 | 2025-08-19 04:25:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5dd93016-1f1e-3228-aa7b-7c7fd0cb7b87 | -7.65162 | -45.26028 | 2025-08-19 04:25:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e4c2bebe-55ce-3012-b652-a3d64e3b7016 | -6.94143 | -43.59842 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a0adefb7-7172-384e-9332-8fe1261f13d5 | -6.65767 | -41.76702 | 2025-08-19 04:25:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e81f918e-95fa-3efc-9301-3d9726baf4c6 | -3.04294 | -49.4324 | 2025-08-19 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 69c2f279-a1af-3fed-afbf-70aeabf291b1 | -6.93726 | -43.60195 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4b826097-37ff-304f-a157-16bc6ff5dfc4 | -6.85467 | -44.41976 | 2025-08-19 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b6f3b566-1801-399a-a839-344f86217d42 | -6.93963 | -43.61062 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dbe72c40-fab9-3bb0-9ede-232885b19577 | -6.93856 | -43.59965 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 480eacac-6c40-3028-be13-b0889a047de5 | -5.98542 | -44.13997 | 2025-08-19 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 85ea8368-a51f-3a98-9529-f3cd621b498e | -6.93546 | -43.61996 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 02dca620-72a3-343b-bb0c-89cec02f7f5b | -6.6365 | -52.23248 | 2025-08-19 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1761242-e5e3-37d5-89ff-d25f66a0ac21 | -6.56439 | -43.0083 | 2025-08-19 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a8582aed-3d71-30d0-bdf5-d2b5f17247de | -5.7856 | -43.72887 | 2025-08-19 04:25:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c46d5624-b834-39d5-b02d-78ef4e5c80ca | -6.87491 | -45.20398 | 2025-08-19 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5bd4523a-9d7a-376d-86dc-97d0a2ac9f40 | -2.90796 | -48.29597 | 2025-08-19 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| db8049d4-fe4b-3bd0-940d-9d0798f08d2b | -4.00252 | -43.26315 | 2025-08-19 04:25:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e4671dcb-8a58-36ac-85a8-7fca9e97f358 | -5.87344 | -48.12349 | 2025-08-19 04:25:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 28f5b5c1-43c9-31c3-9955-bad930174e32 | -4.93327 | -47.74318 | 2025-08-19 04:25:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 37c2a6c0-b938-320b-ad61-09e615048d70 | -5.54373 | -44.05243 | 2025-08-19 04:25:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b10c328e-44a3-3798-95b8-601c215f2f58 | -5.65444 | -43.37769 | 2025-08-19 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5710df05-f6ce-3371-835e-706aa29dd574 | -5.34427 | -43.53645 | 2025-08-19 04:25:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a48679a3-b6e6-3063-89c1-c6751cd0c50a | -6.15415 | -42.69924 | 2025-08-19 04:25:00 | NOAA-21 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 0ed3eea7-4c3e-3d31-bad4-1fa7f608ce24 | -6.95155 | -43.60409 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 088504f1-daed-3d91-a715-dbfe37256409 | -6.94918 | -43.59542 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4a635084-ca73-381e-bc7c-cf829c26eb51 | -3.98713 | -47.88593 | 2025-08-19 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ab315bea-1430-3971-9d15-182496d61e90 | -6.77873 | -44.34306 | 2025-08-19 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 14f2858b-5c1c-3830-bcec-aa0bbd478926 | -6.94798 | -43.60355 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 31f552da-7395-3b23-ad8a-af6900e9d5f7 | -4.2918 | -48.06631 | 2025-08-19 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f8b5f073-1969-38dc-978c-022b68834df8 | -3.47003 | -47.69176 | 2025-08-19 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 025192c6-a3f4-37a4-8b8f-097dabf03b16 | -6.37349 | -43.31024 | 2025-08-19 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3d4fbc91-97f3-3b0e-aa6f-db9ebf33c52a | -3.25772 | -43.27493 | 2025-08-19 04:25:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5554b76f-350e-3d53-ab2c-778eccc7a583 | -7.3903 | -44.27951 | 2025-08-19 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e0698ef3-3464-3edb-a71e-cda83be235d8 | -6.75178 | -41.5594 | 2025-08-19 04:25:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 02d6267f-c7eb-3235-8617-909727220e00 | -6.14605 | -42.70263 | 2025-08-19 04:25:00 | NOAA-21 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 40669322-496e-3d04-a668-6e4e80e90790 | -3.48362 | -47.67461 | 2025-08-19 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f652b000-addd-38ce-8f44-b0b83232194b | -3.97474 | -42.51174 | 2025-08-19 04:25:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 4fdf7237-2914-33c0-bf4e-f8986706b918 | -6.45413 | -44.5635 | 2025-08-19 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4cddebfa-232f-35bb-8149-1e23c01421d9 | -6.06204 | -44.12455 | 2025-08-19 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 504832b7-1b02-3692-8605-2693cbbacc85 | -7.01342 | -41.12971 | 2025-08-19 04:25:00 | NOAA-21 | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3477c048-ba13-3a50-b95b-7b6c7e5fc712 | -6.93546 | -43.61414 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f79875cb-11dd-3109-8cee-35e447b5ff55 | -4.66205 | -42.84692 | 2025-08-19 04:25:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 21b04b55-10f9-3a5f-b6d5-aafe1ad78efe | -3.08683 | -48.85477 | 2025-08-19 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4bce91ac-a1fa-3183-a8eb-eedded74f436 | -4.1588 | -50.22402 | 2025-08-19 04:25:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| afb1beeb-c388-36d4-9fa5-92f76772f2cd | -5.98944 | -44.13675 | 2025-08-19 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8eb456cb-008c-3bc1-ad91-14765e8a9988 | -6.95335 | -43.59188 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a5a12398-0cf4-37ae-a813-691f535149c0 | -6.9599 | -43.59706 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86841ed1-f649-389e-acbd-644405330df7 | -6.05836 | -43.74753 | 2025-08-19 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| b15ba8c8-849e-320c-b0ec-e18f90606449 | -4.91756 | -43.24785 | 2025-08-19 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 348c01d7-92db-351f-9025-c17ca125a75f | -4.01518 | -48.06239 | 2025-08-19 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b5a5903-d186-3c55-ae50-a2126095bd86 | -5.25451 | -44.47272 | 2025-08-19 04:25:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f1f45490-ee5f-3534-b3d4-659ab2c63f78 | -6.52042 | -43.44504 | 2025-08-19 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 3.1 |
| af168841-4cc1-3512-b4b6-48a3b0337124 | -6.07683 | -44.60079 | 2025-08-19 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c0fa97f6-11e2-38cb-8149-33e460f37abc | -5.88026 | -48.12453 | 2025-08-19 04:25:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 72a99cf2-dcb3-3197-b47d-a7ceb4e86120 | -6.19652 | -53.51713 | 2025-08-19 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6c8c9318-9cda-368d-86d8-2a6b2eafe904 | -6.02806 | -44.34667 | 2025-08-19 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 246194db-ef46-3e0d-be05-62fa30055869 | -5.86284 | -43.43561 | 2025-08-19 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 80ed17bc-dc6c-34bc-9e02-e5ac8c19994e | -6.93606 | -43.61007 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 52eae304-e5aa-380b-84cc-aa21a777b6fd | -6.66845 | -43.66031 | 2025-08-19 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ddd04c7-dfc4-38f8-9c68-4ff4811cbf37 | -7.29644 | -43.69445 | 2025-08-19 04:25:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| bfe81c71-48b9-3095-bc4f-5d0ff9bf4652 | -5.65738 | -43.38229 | 2025-08-19 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| da123298-fb31-3ac6-91c3-b337799da8e3 | -5.64363 | -43.40076 | 2025-08-19 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 45257b88-1f40-30e6-975f-f4ccbec6ab00 | -7.16793 | -43.50816 | 2025-08-19 04:25:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 22b8e75b-54d7-3475-a32f-919bdc002291 | -7.59662 | -44.39989 | 2025-08-19 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 741906a5-313e-3025-b895-9f7c864f4d76 | -6.94083 | -43.60248 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1610212d-966e-38df-b132-bdfb01aebf79 | -6.32801 | -44.72095 | 2025-08-19 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e197645c-5793-38ac-a845-9d0af281b390 | -2.90423 | -48.25119 | 2025-08-19 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 474627bf-5044-36ae-be25-dee273841419 | -6.96468 | -43.58944 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 0e405411-df31-3645-82aa-d354fe8abe89 | -6.03492 | -44.34772 | 2025-08-19 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9e8f668b-9201-3b4a-8ccb-444a7a39231c | -6.94139 | -43.62342 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| eebf38f8-b627-3383-8f4f-968637596fbf | -6.9367 | -43.61182 | 2025-08-19 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README22.md)
