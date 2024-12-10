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
| 404df8c2-2de9-3f4a-af21-27946107195a | -3.52542 | -53.32094 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d1e88451-6e06-3fc7-9b5e-eb7e85e36bb1 | -1.54216 | -52.67348 | 2024-12-10 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0695f391-833b-3d52-bfba-e17bf08daabf | -2.61456 | -54.23521 | 2024-12-10 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a37ae552-eb55-3f1a-b7ae-ed7d8a11a243 | -11.32323 | -54.04805 | 2024-12-10 04:53:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e77fdf5b-a69c-3178-a8fe-97911fc6d614 | -3.06939 | -54.24641 | 2024-12-10 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 55e1468c-22b8-33e9-8cfd-af95326bc71f | -3.05903 | -54.24488 | 2024-12-10 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 53c48b68-8035-3b83-8b6c-d1b718efebd6 | -10.87631 | -44.33887 | 2024-12-10 04:53:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cf6145bd-649c-30f6-88a4-a3b16c8fd38c | -3.63246 | -52.68476 | 2024-12-10 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9cb8e59a-b6ee-3efe-b2f3-7d35e079873a | -3.68041 | -52.37849 | 2024-12-10 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ecf1d216-f2ae-32ba-b94f-6c0a9ccb9852 | -3.12252 | -54.04438 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 211185a4-2574-3676-855a-2b3da413023e | -2.6403 | -54.68613 | 2024-12-10 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3269e1cb-1625-3f7f-a78c-20fa99d703e0 | -3.62396 | -50.19788 | 2024-12-10 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1d1b4a3a-fba1-3a46-9dcf-a7efbbff5b8b | -4.40044 | -47.7618 | 2024-12-10 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4717c184-bef6-317c-a31f-b6781ff11deb | -4.56435 | -48.92141 | 2024-12-10 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd18ba3f-e45e-34ff-ae3f-f2c3bbabe0b8 | -2.99844 | -53.04025 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a553d691-27f3-357d-9ab0-3ffe26a5b3cb | -3.07152 | -54.0784 | 2024-12-10 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e71d70e1-0748-35d1-b644-c798bfba1b62 | -13.10577 | -43.31965 | 2024-12-10 04:53:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| da8960b7-a8c5-3024-9fbd-4da89902b192 | -2.86061 | -54.05773 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 708228be-4077-3474-a821-d4b6bbf335e7 | -4.39723 | -47.75632 | 2024-12-10 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 212625b3-333a-3900-ae9c-95e25ede7852 | -2.771 | -54.02462 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 459ce50b-f4b3-3330-88a1-b9ea7b2fca11 | -2.4622 | -53.64252 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a09422a7-1a2c-3171-9562-f968b006f04f | -3.20905 | -46.80748 | 2024-12-10 04:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 19ce3df7-5c11-3349-b8a8-d53ebc23fa27 | -2.47558 | -53.6971 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2198e244-a2ad-3a2b-972c-e56e31056e35 | -2.17311 | -53.65443 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f2cf78c9-0384-31ae-a671-3908fe1b0804 | -3.74801 | -54.74544 | 2024-12-10 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 59f5ee32-ea45-3a6b-bc22-b869485f80b8 | -2.54668 | -53.42328 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5fd2fdb-bbbd-3172-b346-51169abc1a15 | -3.12368 | -54.03701 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f1ca32db-5c74-31a2-b1eb-ce5adf3ad215 | -3.10756 | -54.07247 | 2024-12-10 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9be1e971-e129-3377-9ef5-2ffb51156f28 | -2.99063 | -53.0247 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c541b482-2504-34b3-95c6-024f330f4ebd | -3.53165 | -54.6926 | 2024-12-10 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b0ab1990-6afb-3bd1-b6d8-bbdebaa7b490 | -3.23795 | -51.33103 | 2024-12-10 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40c960f1-a4ef-3303-acf2-3eb77b925726 | -4.52567 | -47.96987 | 2024-12-10 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5b2a3348-6672-3f44-8bd6-908c0059a17a | -3.15669 | -51.32923 | 2024-12-10 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 46baf928-4939-3464-aec0-0a455833ede2 | -1.41141 | -52.42189 | 2024-12-10 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7832952c-beaa-3626-ace2-ed082825450e | -11.78564 | -55.12682 | 2024-12-10 04:53:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 646fc374-14d5-3742-b5bb-5da088137ad8 | -6.91798 | -43.5103 | 2024-12-10 04:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 6ae11246-5807-351f-942f-f164ea6b8c55 | -10.2121 | -52.68283 | 2024-12-10 04:53:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2a1b5bac-c95c-3075-aa8f-225a0823f1e5 | -3.12761 | -54.05654 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1dbc58cc-3d04-330f-a681-878ff7887a90 | -3.81647 | -51.26344 | 2024-12-10 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6086095b-76b0-3e65-b5df-827c728d1a1a | -2.46672 | -53.63582 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f7207887-efa2-32a8-be4a-46a38391509a | -3.10637 | -54.07994 | 2024-12-10 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 53f763dd-a4d1-3bdc-89e6-693a8f6e96e0 | -4.55222 | -48.00402 | 2024-12-10 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7540f491-7944-3c8a-a706-f70a24d8188f | -6.32203 | -46.92787 | 2024-12-10 04:53:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0f663d2c-b03d-3224-84bc-6450f73b910a | -2.35522 | -53.79079 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c2fd1eff-251b-3fd0-bf06-1d796601b003 | -2.46616 | -53.63943 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7044a734-8612-30bc-9ab3-6881701b7b3d | -3.11039 | -54.07673 | 2024-12-10 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 382cb2eb-1682-3efe-8f38-279201eb40ae | -2.99631 | -52.85783 | 2024-12-10 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 74d97ac1-0b61-3e4c-8cfc-3b973abf7cca | -6.73044 | -46.29044 | 2024-12-10 04:53:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2ec2e2bf-bfc6-3d3f-827f-1fd0403fffe3 | -2.46277 | -53.63889 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 10367a52-0ce0-399e-8db0-59da6d13f0da | -3.79252 | -54.64563 | 2024-12-10 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e1e44ac2-3c21-3a2d-932e-c0c4bc0a8628 | -1.66843 | -52.08387 | 2024-12-10 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb7311d7-68bd-3d7a-9bfc-e8591528501c | -3.5344 | -54.58643 | 2024-12-10 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 187a95e0-910a-329b-832f-95f076084672 | -2.46986 | -53.71115 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7a167e16-4fb9-3de5-b453-bf4c4b93257a | -2.98635 | -54.06166 | 2024-12-10 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4e9c2e4e-309a-3135-b906-d0ec5e56fb53 | -1.54107 | -52.68046 | 2024-12-10 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 40c89b45-3a23-3c07-b509-c87cda1a680f | -12.85767 | -51.94336 | 2024-12-10 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 28eb6874-4f95-39a1-b7a4-bd89453f26d8 | -2.22175 | -53.72186 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9bdd66d5-eea9-3c4c-9f9f-93e07ab22c2b | -2.74436 | -54.0815 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d9da8d2a-c8aa-3028-bc74-1d10d5b83a4c | -3.12243 | -54.06715 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 27e60286-d384-355a-98a6-0d0c738fb839 | -11.35023 | -54.28931 | 2024-12-10 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e6747c5-8db7-311e-8ec6-548f34f79e8d | -4.5479 | -48.0151 | 2024-12-10 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 998bfafd-796d-3e72-9e31-cfe796be2fc1 | -5.91896 | -48.04646 | 2024-12-10 04:53:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 55d36d4a-3ed1-381a-ade9-68c28da04200 | -10.37168 | -52.00552 | 2024-12-10 04:53:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dab209ac-75fd-321a-93a7-bbf42a59c06d | -1.26701 | -52.14793 | 2024-12-10 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f312f9f-6663-35c0-99f0-c2a14d71a6e3 | -0.73128 | -50.63258 | 2024-12-10 04:53:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df441434-f3df-3514-b3ee-ef5b2b1d2fc0 | -3.46369 | -52.71856 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4314448e-caf0-327e-949e-6961633194d2 | -3.17338 | -53.96569 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bba4c27b-3f15-3ba7-a914-d74599ab098f | -6.83711 | -44.39013 | 2024-12-10 04:53:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 12a7f11d-4aab-3bdb-bfc5-2cf807e4b30e | -2.9371 | -53.88439 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4d453ac8-6166-3708-bdc8-2b1da530a8bc | -2.6416 | -48.64129 | 2024-12-10 04:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eaee6863-203f-3b2f-8ebd-5181221978dd | -2.55678 | -53.42485 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 79df86e5-88fd-37cc-aefb-7adbdf605d95 | -4.56803 | -48.92199 | 2024-12-10 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 67edbe71-c63f-3eb7-b87c-e2e0da318f3d | -1.52877 | -54.02469 | 2024-12-10 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 954053cb-560e-3121-94f2-32e27241c26e | -1.68807 | -52.98056 | 2024-12-10 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a86e3100-cc2d-3d97-9376-e0f36919f491 | -3.10354 | -54.07569 | 2024-12-10 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a99c418a-bf8a-3dbe-abb2-e11620baba24 | -3.88517 | -54.21604 | 2024-12-10 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 23b1a486-2f98-3c38-aa51-f6ad8332779e | -2.78441 | -52.86417 | 2024-12-10 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ce67efcd-1a9f-348a-92fc-d9a7024b94fa | -3.79211 | -50.95599 | 2024-12-10 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fba1ea4f-76aa-3db7-a5a8-8649a4f8ef1a | -12.37627 | -54.16434 | 2024-12-10 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2ab9f04f-fed5-3f14-a6a9-aa026b471c3c | -3.10771 | -53.25197 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1abb3550-9889-3064-be08-2408452ecc70 | -2.98743 | -52.84936 | 2024-12-10 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 4578f0f3-82a9-3e0e-9430-cb1f000c47d0 | -9.14371 | -62.72047 | 2024-12-10 04:53:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd75ef49-10dd-3ea4-b30e-d70cab7b3545 | -2.30813 | -54.00047 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fdf5402f-ca8f-36f2-a203-e7003da1c10f | -3.09609 | -54.07837 | 2024-12-10 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6b8eabc-8dec-3f10-bcde-64a56e7d409d | -2.48121 | -53.70543 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f416440-d133-311c-acbc-453e9587a005 | -3.12535 | -54.04861 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 94efd9fa-dd99-3125-a83d-6ad2f44e2d66 | -2.8229 | -53.07405 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ddfc4658-da8b-3daf-9dea-42e04fde9adb | -1.65717 | -53.28936 | 2024-12-10 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52040874-05a1-36d3-878b-ada98c1d5aa2 | -3.53379 | -54.59024 | 2024-12-10 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 28b55ca0-ddb0-3b4e-98fa-ed967712bf35 | -2.4141 | -53.66118 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d8a8649-c29e-31bc-b16c-80142918f6a7 | -1.56534 | -46.76656 | 2024-12-10 04:53:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a1493e0b-9f98-34a5-960d-2662c5c68424 | -4.39329 | -47.75581 | 2024-12-10 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| dd8b8a63-ffe4-32c3-b933-0b29702c514c | -2.91562 | -52.95952 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 204f4a1c-a367-3835-9df4-10dd8b5f263e | -2.9195 | -52.95653 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| e96b77b1-ce9c-3e2e-ae8c-6ade9deabd70 | -3.51291 | -52.18707 | 2024-12-10 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 83c27bac-4c1a-36d5-83cc-adc4d9612a3a | -4.40118 | -47.75679 | 2024-12-10 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b06bdf5a-4edb-3ec3-8ac4-0198cee7ce49 | -2.03816 | -54.43613 | 2024-12-10 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0487bba9-5fce-3ed5-ae33-663388bb50b4 | -1.55386 | -55.80849 | 2024-12-10 04:53:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7954be3d-448f-35e8-b3a4-bed7f4a4e4b7 | -2.31467 | -54.00114 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 18daf1aa-179b-3dee-85f6-15bd16d3d1d1 | -3.10362 | -53.76024 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |


[Clique aqui para ver as próximas entradas](README27.md)
