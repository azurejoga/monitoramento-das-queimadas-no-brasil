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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1d0cbc21-188d-3953-b8ed-3ac88795f10d | -23.36589 | -47.17587 | 2025-07-24 04:46:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 58e7b45d-f970-3c28-ae71-d2eeaffa4954 | -23.3664 | -47.17165 | 2025-07-24 04:46:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| fdae054b-2d16-329a-ac8f-f343cbc862eb | -21.59359 | -57.60368 | 2025-07-24 04:46:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ea6eccaf-48b7-3065-86a0-8df115b1774a | -21.4797 | -57.10792 | 2025-07-24 04:46:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7ef2fd85-0588-3173-917e-7dc68b5aa266 | -23.01541 | -48.90944 | 2025-07-24 04:46:00 | NPP-375D | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 54a8dc81-725b-3b21-a75a-77d46cd7c079 | -24.1108 | -48.57318 | 2025-07-24 04:46:00 | NPP-375D | GUAPIARA | SÃO PAULO | Brasil | 3517604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 48555570-624d-3031-ad78-391aedeb685a | -23.01157 | -48.90893 | 2025-07-24 04:46:00 | NPP-375D | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7b87a3e6-3a77-3d57-bc9b-53675e5ea66c | -23.48159 | -47.0267 | 2025-07-24 04:46:00 | NPP-375D | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0b026371-92d7-3f69-bda1-e6cd09e6b58f | -23.06596 | -49.69105 | 2025-07-24 04:46:00 | NPP-375D | CHAVANTES | SÃO PAULO | Brasil | 3557204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 65cf9168-e759-3cae-9ebc-df5eff2c9e68 | -23.299 | -46.1285 | 2025-07-24 04:46:00 | NPP-375D | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| c0a54510-c5c9-344e-a1b9-867fc3403cf8 | -21.76761 | -52.75419 | 2025-07-24 04:46:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c6f11ce1-0563-3f8c-afa9-0d53755073f6 | -23.36839 | -47.17387 | 2025-07-24 04:46:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 049e75d4-31e4-3a78-8946-ef0910edcb07 | -22.25836 | -49.5797 | 2025-07-24 04:46:00 | NPP-375D | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| fc6b5f91-ff1c-3d47-b5ac-63a852588061 | -22.26203 | -49.58024 | 2025-07-24 04:46:00 | NPP-375D | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 138e025a-02d4-3cd6-a745-dc57a1b3c647 | -23.06657 | -49.68642 | 2025-07-24 04:46:00 | NPP-375D | CHAVANTES | SÃO PAULO | Brasil | 3557204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 5c040ea4-658e-3ce3-bc98-81781bb91794 | -21.75763 | -52.7524 | 2025-07-24 04:46:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a3fc864-28c9-359b-91f5-657acc311d9f | -23.3679 | -47.17809 | 2025-07-24 04:46:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 84348318-1136-3c2f-9088-772ba5161983 | -22.25898 | -49.57508 | 2025-07-24 04:46:00 | NPP-375D | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 76d43042-7807-3bfa-a932-80678e836c17 | -23.35977 | -50.82609 | 2025-07-24 04:46:00 | NPP-375D | ASSAÍ | PARANÁ | Brasil | 4101903 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| dd48160d-f8cd-3a25-ad80-e366da61831f | -22.39636 | -49.79226 | 2025-07-24 04:46:00 | NPP-375D | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8493c416-ce52-3f11-b1a0-47cb6a3e0075 | -23.7815 | -45.35415 | 2025-07-24 04:46:00 | NPP-375D | ILHABELA | SÃO PAULO | Brasil | 3520400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| db397c17-cdb6-397e-ac66-98d17de8c8f4 | -23.07026 | -49.68694 | 2025-07-24 04:46:00 | NPP-375D | CHAVANTES | SÃO PAULO | Brasil | 3557204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e63a53f0-59f0-320f-a779-5728d80ba4d9 | -23.78354 | -45.35269 | 2025-07-24 04:46:00 | NPP-375D | ILHABELA | SÃO PAULO | Brasil | 3520400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 40930a00-84bb-3881-9ce2-7390c84fdb8a | -23.0109 | -48.914 | 2025-07-24 04:46:00 | NPP-375D | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 580cfbed-19be-3d15-ae1e-7c80a8e663ff | -23.02388 | -46.72381 | 2025-07-24 04:46:00 | NPP-375D | JARINU | SÃO PAULO | Brasil | 3525201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5063146e-1588-35a6-b424-0b5a43b077bc | -7.2594 | -43.0881 | 2025-07-24 04:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 73.7 |
| 06fcbf2f-c450-3c1c-8dc6-10f5aa0e05cd | -7.2597 | -43.0645 | 2025-07-24 04:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 103.0 |
| 31ba21a9-596b-3c03-8e04-5df1f8435edc | -3.1649 | -49.4435 | 2025-07-24 04:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 44f8239a-34a7-3a9c-bb2f-1021521d7263 | -3.1648 | -49.4648 | 2025-07-24 04:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 8fdd8492-61d3-3ed5-842c-1f25900c65a9 | -3.1832 | -49.4642 | 2025-07-24 04:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| c6242aa8-7572-3958-a1ed-5c59c5e1ba9e | -3.1833 | -49.4429 | 2025-07-24 04:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 75e397a9-0146-3328-bad1-a42b0db03a3b | -4.05125 | -42.52332 | 2025-07-24 04:55:00 | AQUA_M-M | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 48.2 |
| aa695fa1-2783-3102-b735-7fd35226e285 | -4.04616 | -42.51747 | 2025-07-24 04:55:00 | AQUA_M-M | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 73.3 |
| 47ef7150-541e-3848-8b41-f88aca55093e | -7.24845 | -43.05351 | 2025-07-24 04:57:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 144.8 |
| 9a7cfdf2-d999-3a24-988d-1a4ae2e20f85 | -7.24222 | -43.09017 | 2025-07-24 04:57:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 57.6 |
| 9a6a043d-f974-3c20-9200-411819fcaaa0 | -7.25488 | -43.05964 | 2025-07-24 04:57:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 168.7 |
| 260649e0-194e-39da-b8f2-bfdd4276cf83 | -7.23827 | -43.05684 | 2025-07-24 04:57:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 53.9 |
| e578d258-10b3-36e6-a1b3-50ef81bee14d | -7.26504 | -43.05642 | 2025-07-24 04:57:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 40.4 |
| f86602aa-72ce-3e05-b13e-aed41314931f | -7.2594 | -43.0881 | 2025-07-24 05:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 66.3 |
| 67afa9eb-4604-360d-b270-c6c7729c74d8 | -3.1833 | -49.4429 | 2025-07-24 05:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 6d947d40-e45e-34ff-af91-478a5f88a676 | -3.1648 | -49.4648 | 2025-07-24 05:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 27707f3b-44fb-301e-8b0f-6e70915c1ed5 | -7.2408 | -43.0664 | 2025-07-24 05:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 62.8 |
| 8d9b7826-c650-3a0a-a94b-022de6206eef | -3.1832 | -49.4642 | 2025-07-24 05:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 656f1c80-96dd-3cf1-b6ed-428558e7a534 | -7.2597 | -43.0645 | 2025-07-24 05:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 115.0 |
| 7eb9244a-4023-3ffc-9677-36ecb2bb1959 | -3.1649 | -49.4435 | 2025-07-24 05:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| f95ca89f-86c8-3b91-ac02-0663f9ad49fe | -4.04031 | -42.52354 | 2025-07-24 05:01:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7b685b89-f7d2-3203-bd15-11a9153b43ad | -3.35665 | -47.16374 | 2025-07-24 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2cc11bb6-9448-3a0b-9f2c-6b0f10e5650b | -4.78035 | -45.33162 | 2025-07-24 05:01:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a8e3dbc1-0943-3878-848a-1008187034bd | -4.04384 | -42.51239 | 2025-07-24 05:01:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 93da2f33-e31c-3771-893f-0c29ec71dbf4 | -3.174 | -49.45604 | 2025-07-24 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 5a7d0996-319b-3e05-abd3-25416b50f6da | -3.56924 | -49.50058 | 2025-07-24 05:01:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f9d23231-e9ce-3302-8442-0d17c3db76c7 | -3.3572 | -47.16511 | 2025-07-24 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a1cb1f43-525d-3080-9ab7-e5a621760184 | -3.18247 | -49.45726 | 2025-07-24 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 411335f8-1c37-35d7-96d1-455645944fbd | -3.65053 | -48.32467 | 2025-07-24 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e3ba8729-2489-313a-90fb-6745aebdd8ac | -4.04796 | -42.5186 | 2025-07-24 05:01:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| a038a44c-cfcd-34fa-9eb6-f6fb05696f96 | -3.03902 | -49.43305 | 2025-07-24 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6650b84c-fe89-3381-a694-ba91c2f3d3e8 | -5.67575 | -43.67285 | 2025-07-24 05:01:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 839da4d6-c1a5-3178-ba93-bab9b2e8c52b | -4.0574 | -42.51433 | 2025-07-24 05:01:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 16.9 |
| edb27909-291b-3e0e-8c99-6ca10cde00e4 | -3.04245 | -47.38427 | 2025-07-24 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f7f42604-cbf1-3db4-9c95-5f7d5e6d4707 | -4.05473 | -42.5196 | 2025-07-24 05:01:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| d676a487-5bcc-35c4-817d-070f61759e19 | -4.05563 | -42.51349 | 2025-07-24 05:01:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 4a39932f-9db3-3166-897a-24877b7c7134 | -3.2282 | -46.79181 | 2025-07-24 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d87690aa-8da7-383c-8077-58add028dcf7 | -5.6777 | -43.66497 | 2025-07-24 05:01:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b998b68f-6346-3cd4-96f2-6be78247f148 | -4.88584 | -44.96007 | 2025-07-24 05:01:00 | NOAA-20 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d6dab5da-db96-39ac-a68f-91888c032dae | -4.04891 | -42.52545 | 2025-07-24 05:01:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e81d4eef-8c18-32a5-9f73-a228b5d711d7 | -3.03487 | -47.86123 | 2025-07-24 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e0306d3-a19e-376f-9e01-710bb9f956e7 | -4.05653 | -42.52044 | 2025-07-24 05:01:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| ab36418b-8bdd-3567-859c-d1217b67a057 | -5.68339 | -43.67153 | 2025-07-24 05:01:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 21d8888f-23eb-317a-ab37-cfa89c1a0523 | -4.04215 | -42.5244 | 2025-07-24 05:01:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 02cedb8f-c2b1-381e-a717-04fb0ee7d611 | -2.45766 | -48.15324 | 2025-07-24 05:01:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dbc058b1-b230-32dc-b575-9bbe340c2830 | -3.03175 | -49.42393 | 2025-07-24 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4dd20421-ec42-348b-9379-5f15fec51bb4 | -4.05062 | -42.51338 | 2025-07-24 05:01:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| a66ac614-dbc3-3a90-b454-376373a103d2 | -4.30108 | -48.10086 | 2025-07-24 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 8578a48a-7ee9-326d-ab11-9c21a70f2257 | -4.78437 | -45.33455 | 2025-07-24 05:01:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 22925870-778a-3cb8-bcfc-4667e935a1e8 | -3.04207 | -49.44146 | 2025-07-24 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| de49da6e-f4be-3690-ba63-3ad463f3c2a5 | -3.48471 | -51.18876 | 2025-07-24 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6c7018f7-9b83-3d79-b09d-ddfe6c6f3030 | -3.22355 | -46.78807 | 2025-07-24 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 84672c12-3a61-31f0-b3de-b8124d9b2624 | -3.22864 | -46.78883 | 2025-07-24 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5ab816ce-e2d2-370a-b45e-0c2625e05d06 | -4.04976 | -42.51946 | 2025-07-24 05:01:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| f280ab76-b4c1-36da-8518-d8e86555a4a5 | -3.18365 | -49.4495 | 2025-07-24 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| bac9e26d-40d3-3911-85ec-bb820c861981 | -3.05379 | -47.37512 | 2025-07-24 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0219a61f-8fac-31be-85d0-f9d58dd4c848 | -3.03539 | -49.4285 | 2025-07-24 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0a18cc7d-a165-3ff1-8bf1-5d6fa77f23cd | -3.224 | -46.78509 | 2025-07-24 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 485211d8-401c-33a9-a3de-74bb0fd36049 | -3.1746 | -49.45216 | 2025-07-24 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 165cfd9e-f231-3263-a351-00533f8d31f7 | -3.04323 | -47.37905 | 2025-07-24 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 67bc33f1-6085-3f92-bf3f-4897299d98a7 | -3.17341 | -49.45991 | 2025-07-24 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| d891b08b-af2e-381c-8df5-045f20c9e9cc | -5.67697 | -43.67033 | 2025-07-24 05:01:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b681add6-8877-35d5-9872-449343e1007b | -3.97566 | -47.88213 | 2025-07-24 05:01:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 715d7d8f-1791-3be3-9a2e-c145fe06e939 | -4.04707 | -42.52456 | 2025-07-24 05:01:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| acd747cb-b9d8-3b75-af6c-8a0eb437b65b | -3.9272 | -52.1699 | 2025-07-24 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1126a869-08f0-3397-989c-08060baad3d4 | -3.17823 | -49.45666 | 2025-07-24 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 7596a110-0c10-3a67-83bc-8430c3717959 | -3.16978 | -49.45542 | 2025-07-24 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| cbd4c519-3f64-37ca-ac69-e29be8667ab4 | -3.20876 | -54.96079 | 2025-07-24 05:01:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ad42bfe-dac8-3126-92e0-eae5874f7109 | -4.8055 | -43.2168 | 2025-07-24 05:01:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9d65812c-175a-37df-923b-73b1f76c982b | -4.10356 | -48.20851 | 2025-07-24 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dae2abd2-70ae-36ea-bf51-208b1c5b8fea | -3.15594 | -58.97941 | 2025-07-24 05:01:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e59c4bb2-8cd8-3b08-b990-b87b6ca14c63 | -3.56983 | -49.49664 | 2025-07-24 05:01:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 06c38963-807f-3eba-966d-34a39166dff8 | -4.10426 | -48.20378 | 2025-07-24 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8abefe99-1f0f-31bc-a2bf-0ba54d5368fa | -3.88537 | -54.24483 | 2025-07-24 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a96be861-cbc1-3172-bcdc-f044acf81b66 | -3.22311 | -46.79107 | 2025-07-24 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |


[Clique aqui para ver as próximas entradas](README21.md)
