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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8ed8d0b4-b96e-3e68-a151-60a63e060446 | -13.22583 | -51.20752 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.4 |
| c007a3ea-e2e5-3ee1-b8e1-ce63a1b44137 | -13.22501 | -51.21196 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 1cb62e11-02f4-3935-b972-ed1876d57eef | -13.22058 | -51.21109 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 454e531b-d46d-3fbd-8cb2-01477abb8eee | -13.21615 | -51.21024 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 7bb4aa92-92ca-3f09-9663-b483694cb1d5 | -13.21172 | -51.20939 | 2024-10-01 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 431a6e9b-a0ab-3472-af35-538b08d9acee | -12.78498 | -50.59616 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f27679ad-456e-3c48-8b42-854ff2232590 | -12.78423 | -50.60032 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d6647589-8afa-3f6f-b73a-2d9ff605996f | -13.63687 | -51.16485 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d1d03a78-2aa1-3ce0-8606-34a43ffb9b65 | -13.63441 | -51.17797 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6c8d876d-8aea-3924-86a3-cc9959ea91b2 | -13.6336 | -51.18236 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 35895109-8025-31ce-a197-2b5ce44ad941 | -13.63317 | -51.16096 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| b5d398c8-1901-3aa0-bc88-64010f3a2a7e | -13.63248 | -51.164 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6a0bf6ce-2e9e-30b4-8567-853b3616ece2 | -13.63239 | -51.16535 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 27b29a14-e947-3b93-a301-6696c0524009 | -13.63167 | -51.16837 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ad3a04d7-cb76-33f9-8515-5f4179f889a3 | -13.6316 | -51.16972 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3d03ccea-d29e-3309-9b51-85a4726f3418 | -13.63085 | -51.17274 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c7618967-e08a-3df6-bdac-6851e59e3f5b | -13.63082 | -51.17412 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| d07c948d-aa66-3645-b178-ee728dd5e8d2 | -13.63055 | -51.15003 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 24b14a08-ad4c-3936-8e61-880480eb3ae6 | -13.63036 | -51.15134 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |
| fa73b96d-2846-3579-97e7-fc818eb4f1da | -13.63003 | -51.17851 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| df5057f5-bf5b-33cd-82f8-be947866e48f | -13.63003 | -51.17712 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 5d2c4bfe-e4d8-391d-aa54-0b28e53ebd2e | -13.62974 | -51.1544 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 84a721ce-6524-3469-9285-f2fe2876710f | -13.62958 | -51.15572 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 813897a5-5844-3e78-8f8f-d1221ea65d75 | -13.62924 | -51.1829 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 72cb84f9-ef00-3213-b4d5-39ad434709a9 | -13.62921 | -51.18151 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c4d4e68e-464b-333a-8537-eeff3716b2fc | -13.62722 | -51.16887 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8fc55ab4-d276-36c8-b87e-34f2aff45408 | -13.62646 | -51.17189 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 45710a67-7120-392e-b152-d18e6492d7d3 | -13.62643 | -51.17326 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| dafc6c1a-665e-367c-a22a-ed75c086db56 | -13.62617 | -51.14919 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7996ba7c-952e-3738-91a2-0a849d1bab25 | -13.62598 | -51.15049 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c00beee7-b7f1-3f55-84b4-90d36c3ab138 | -13.62535 | -51.15355 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 904b51d6-8a25-30dd-9868-fea41f7d4982 | -16.07463 | -50.35139 | 2024-10-01 04:14:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 28c65a62-1d0b-3c9e-88c5-a697e42470ba | -13.62482 | -51.18066 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9f8c8d22-4209-3eb7-b84e-04c5d7b6df24 | -13.62125 | -51.17681 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 53ec8e4e-4d1e-3bbc-8bc4-18d42f6b9fc0 | -13.62125 | -51.17543 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3d5cbba6-5b8c-3fd6-b885-74fe6a26c968 | -13.62043 | -51.17982 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff8bf579-96a4-3657-a404-06262bb876fc | -13.61765 | -51.17155 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0b53531b-5b82-3d63-84f8-add692839483 | -13.59213 | -51.16198 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 824ec782-9ac6-307c-9cec-8056077d5922 | -13.59133 | -51.16637 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5f681d96-48a4-3e0b-af79-5e7b8ed06cca | -13.59053 | -51.17077 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 974d4659-f42c-3a18-99fa-0629c47ba6e0 | -13.58973 | -51.17518 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bab96308-5ac3-3f58-8c55-e14497b2c1da | -13.58774 | -51.16113 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ad52b57d-239b-3d08-afa7-71831322a080 | -13.58694 | -51.16553 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 95ca2d85-b9ac-3bc6-8c58-ddca0b823039 | -13.58614 | -51.16993 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 06e3e34d-8a59-3f7c-bec0-778788e2aff5 | -13.58255 | -51.16467 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2a6470b3-4113-3879-8120-ba0101e38eba | -13.57817 | -51.16382 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ca747442-afc3-30af-b558-4702891a2482 | -13.57619 | -51.1498 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 74a3a5f3-ef1d-32bc-b0f4-ec6f5761c388 | -13.57261 | -51.14456 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ef41da3c-a40f-3ceb-8891-8921afea96ff | -13.56903 | -51.13933 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| cc464e2e-1c37-36a7-ad37-55a88455011a | -13.56787 | -51.121 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| ef6998e1-e16b-3a5a-9d37-74a06aa0aa81 | -13.56546 | -51.1341 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8a060a22-a352-369b-98e7-69e489c5a3bf | -13.5635 | -51.12014 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 830778de-c084-3a5a-9cbf-48f437eaafa3 | -13.56269 | -51.1245 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 42ed0929-9e43-35be-9d43-7fd03e9782eb | -13.56189 | -51.12887 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6ee27801-31f8-3803-aa53-cfcb7a5228fd | -13.56061 | -51.1604 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6f431570-0ced-363b-ad59-3c6ade3b1d93 | -13.55832 | -51.12364 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9d7683fd-7626-3def-bfcc-93cc0e68cba8 | -13.55704 | -51.15515 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 00902566-c1d0-34f6-9cc8-014e2852a880 | -13.55589 | -51.13678 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 518183ac-fdae-39ad-b1e9-e67040ee6778 | -13.55508 | -51.14116 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a29f441b-a100-3de1-af7e-8e15fe5b7d09 | -16.07455 | -50.37435 | 2024-10-01 04:14:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 33975838-dacc-333b-9a1a-d82ef5693f67 | -13.55427 | -51.14553 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b83c5d82-c85d-3554-a811-581824bb5812 | -13.54956 | -51.12193 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0df82e39-0edd-3822-b0c3-f0cfb35974f0 | -13.54519 | -51.12108 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a7c031e0-d19b-32e8-b9d2-cfa16337f3ca | -13.93146 | -50.87051 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6c4d4e22-c6c5-369c-b112-0f2c346aa65b | -13.71072 | -50.96051 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 71983bd0-e94e-3c1a-b58e-0aa98f356469 | -13.69775 | -50.95803 | 2024-10-01 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 32f92051-83cd-3413-b4b7-5a2b091ad1c9 | -16.66591 | -50.6011 | 2024-10-01 04:14:00 | NOAA-20 | AURILÂNDIA | GOIÁS | Brasil | 5202601 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 93482111-acc0-3c57-9223-924db4d76e1f | -16.66579 | -50.59771 | 2024-10-01 04:14:00 | NOAA-20 | AURILÂNDIA | GOIÁS | Brasil | 5202601 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9b9b9f6d-4cb6-3adb-bf63-3088fe9e774c | -16.66512 | -50.60144 | 2024-10-01 04:14:00 | NOAA-20 | AURILÂNDIA | GOIÁS | Brasil | 5202601 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d5c7675a-363f-35a8-a8bb-b78e23151fb2 | -16.11571 | -50.37557 | 2024-10-01 04:14:00 | NOAA-20 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 647880ac-179c-345d-930f-7f29c2184cc9 | -16.1124 | -50.37101 | 2024-10-01 04:14:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 178d4e41-cb41-38e2-8a27-2a54550bfba0 | -16.10114 | -50.34196 | 2024-10-01 04:14:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1bf06ddc-0cdb-3233-bf58-cad025a6adca | -16.1005 | -50.34549 | 2024-10-01 04:14:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 600b36ca-c572-353b-b1d0-8f4734ca3eb6 | -16.09786 | -50.33728 | 2024-10-01 04:14:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4eb2d164-f0cc-30cc-98fb-38a38ce7bae4 | -16.09723 | -50.34078 | 2024-10-01 04:14:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fbb0582d-d7d7-3f9d-ac20-d05885861666 | -16.09656 | -50.41264 | 2024-10-01 04:14:00 | NOAA-20 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6bbdbbe0-e885-306b-bc8f-8e5751f73570 | -16.09323 | -50.40812 | 2024-10-01 04:14:00 | NOAA-20 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 136cf902-c430-37a0-9444-5687e059dc98 | -16.09258 | -50.41173 | 2024-10-01 04:14:00 | NOAA-20 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 95d529b1-377d-3ef3-ae7e-f00ef548e61e | -16.08997 | -50.3353 | 2024-10-01 04:14:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 408763d9-845b-3595-97c7-202e55865fb1 | -16.08995 | -50.40338 | 2024-10-01 04:14:00 | NOAA-20 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5f9d7549-f01c-3a5b-be95-3d25576139a0 | -16.08928 | -50.40703 | 2024-10-01 04:14:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0cf01432-1b32-3218-a7ee-01428c1eb60b | -16.0886 | -50.41077 | 2024-10-01 04:14:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 261c37f8-ef64-3eec-ad54-91fd43098bac | -16.08794 | -50.4144 | 2024-10-01 04:14:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1cc0d28f-d4b6-3581-8ac6-cf64bf506a5b | -16.08784 | -50.36958 | 2024-10-01 04:14:00 | NOAA-20 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 46624905-5121-3421-bc89-7a0b1fff741b | -16.08651 | -50.37685 | 2024-10-01 04:14:00 | NOAA-20 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c8865ef4-0251-3dce-b644-37dd4ec675a9 | -16.08585 | -50.38043 | 2024-10-01 04:14:00 | NOAA-20 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8d46be5f-569d-3ffc-8b8b-e91198f70e5f | -16.0819 | -50.37942 | 2024-10-01 04:14:00 | NOAA-20 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1d7e941e-1abc-3b12-a14c-ba236c98e9d8 | -16.08122 | -50.40575 | 2024-10-01 04:14:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a7f9ea32-9a4e-358d-9a03-26b140825c7e | -16.0792 | -50.39412 | 2024-10-01 04:14:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9f2bc199-9e73-3ac9-aaf8-773a512888a4 | -16.07786 | -50.40148 | 2024-10-01 04:14:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 42f24e49-d363-31f1-9060-e4e6dcf31c4e | -16.07652 | -50.38614 | 2024-10-01 04:14:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f22cc22a-9889-3027-bc29-d32c70bdc1b3 | -16.07385 | -50.37815 | 2024-10-01 04:14:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 08fd93ed-7304-359c-a657-5770f2552881 | -16.07315 | -50.38194 | 2024-10-01 04:14:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 902c2df2-f6fe-338f-8af6-ad80f0fe975e | -16.07246 | -50.38571 | 2024-10-01 04:14:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5773b1b6-00cf-3cb2-9176-8bb09f6f4fe1 | -16.0719 | -50.36621 | 2024-10-01 04:14:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bcd9659f-fb70-32d4-9837-6a3f655a43e4 | -16.07119 | -50.37007 | 2024-10-01 04:14:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a17d0c1a-618f-3419-a886-4cf84df0ee39 | -16.06989 | -50.35467 | 2024-10-01 04:14:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1cf1e94f-667e-35a8-9eac-a6c26fbe0a0e | -16.06854 | -50.362 | 2024-10-01 04:14:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bbba3dcf-4432-357d-97bb-90859cf75339 | -16.06784 | -50.3658 | 2024-10-01 04:14:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| aea1a123-3c2f-3f88-9530-154047ae0397 | -10.52754 | -51.08852 | 2024-10-01 04:14:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README81.md)
