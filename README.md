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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 117d34b1-357f-3335-a4f8-671a6b9b05dc | -16.0613 | -47.219 | 2026-05-17 00:00:00 | GOES-19 | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 120.4 |
| e37b5ad3-d7d9-36d2-9d80-218d9eed6265 | -16.0415 | -47.2226 | 2026-05-17 00:00:00 | GOES-19 | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 469aac2b-1d8b-3873-8aff-3f782ae126fd | -16.0415 | -47.2226 | 2026-05-17 00:10:00 | GOES-19 | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 2261ad64-c4cd-3b2f-9f5a-726b15784a7d | -16.0613 | -47.219 | 2026-05-17 00:10:00 | GOES-19 | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 034af8b3-f500-3368-9e04-8d3cc41acd09 | -16.0415 | -47.2226 | 2026-05-17 00:20:00 | GOES-19 | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 4d3c8464-6298-3f99-9cf1-d574694b3193 | -16.0613 | -47.219 | 2026-05-17 00:20:00 | GOES-19 | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 69.4 |
| c6d8996d-ea82-3733-a0e3-a72868dc5e74 | -12.5177 | -57.2031 | 2026-05-17 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 073f4c3d-f29c-3f4b-b8f8-a31651d65444 | -16.0415 | -47.2226 | 2026-05-17 00:30:00 | GOES-19 | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 70436164-629b-3118-bbe7-193808aa0242 | -12.4988 | -57.2047 | 2026-05-17 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 67cb8bfa-92ca-3527-a260-e7dd74ff59e3 | -16.0613 | -47.219 | 2026-05-17 00:30:00 | GOES-19 | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 07f718a9-e916-33a7-bbe5-992133ab19b5 | -12.5177 | -57.2031 | 2026-05-17 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 62.7 |
| d1b8a756-dee7-3a99-b980-011cd2484cd5 | -12.4988 | -57.2047 | 2026-05-17 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 8015f6da-04f1-3036-b55c-7b8c6f05ace2 | -16.0415 | -47.2226 | 2026-05-17 00:40:00 | GOES-19 | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 0590d1ba-1013-3b5a-b11b-c5530ccb6492 | -12.5177 | -57.2031 | 2026-05-17 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 1c53f8df-9f3b-3d72-9ba7-ec248bb73a17 | -12.4988 | -57.2047 | 2026-05-17 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| a09b503e-2ae4-34e4-bbf6-97ce02b7ad8e | -16.0613 | -47.219 | 2026-05-17 00:50:00 | GOES-19 | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 3ef0f268-257e-350e-af09-88a2124cb1c3 | -12.4988 | -57.2047 | 2026-05-17 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 35482d53-2e11-37d9-9e42-822d16b2db19 | -16.0613 | -47.219 | 2026-05-17 01:00:00 | GOES-19 | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 2ba9c7d1-fc7a-3804-8dfc-cbf4eb07ace5 | -12.5177 | -57.2031 | 2026-05-17 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 6313fb9e-515b-3d0a-b14b-3e68932a8fe0 | -12.5023 | -57.20959 | 2026-05-17 01:09:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 4fd7c176-a891-32d5-88a1-f9c76072aedc | -12.50862 | -57.21413 | 2026-05-17 01:09:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 40.7 |
| db228f0e-4de5-309b-81fd-7c447fbc70b9 | -12.52887 | -57.22277 | 2026-05-17 01:09:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 21.9 |
| a9a5a52a-bb9d-31eb-83ee-cf46aaec658b | -12.49404 | -57.19898 | 2026-05-17 01:09:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 083dde53-0e43-31b2-8b6e-40a26c7cd4a1 | -11.85906 | -63.72255 | 2026-05-17 01:09:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 422eefd8-339f-3579-a5fb-60a9221632a9 | -12.49673 | -57.21611 | 2026-05-17 01:09:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 1068cbaa-bd01-3b54-9fb2-c9f0bc56a438 | -12.50594 | -57.19691 | 2026-05-17 01:09:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 28.1 |
| a4fd60be-5ceb-36c0-bb39-fa5c349ac4a1 | -12.51419 | -57.2076 | 2026-05-17 01:09:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 959d84ef-3945-33ea-b6fe-e5c7b4f10241 | -12.4988 | -57.2047 | 2026-05-17 01:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| c4ef34bf-7f5c-3da7-815e-69678e6d87e6 | -12.5177 | -57.2031 | 2026-05-17 01:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| e6076837-3bd5-3bd1-993e-2c9e53e97e22 | -16.0613 | -47.219 | 2026-05-17 01:10:00 | GOES-19 | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 73d3dcf5-03b7-3662-b80a-3ed2da6db600 | -12.4988 | -57.2047 | 2026-05-17 01:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 64.7 |
| e1ee9d5e-5bb4-353b-a4a2-9e134f881369 | -12.4988 | -57.2047 | 2026-05-17 01:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| f149edf8-0908-34ca-8ace-7b2a337e0500 | -9.5725 | -40.3227 | 2026-05-17 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 77.1 |
| 3ea131f1-094b-33dd-bddc-419cc3e4c4a0 | -9.5721 | -40.3475 | 2026-05-17 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 109.4 |
| 84bf0327-892a-3394-8ba8-7045b93ff43d | -12.13722 | -39.76697 | 2026-05-17 03:06:00 | NOAA-21 | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b7666d78-9b2a-333f-86dc-fcc23af5e6bf | -12.13596 | -39.77289 | 2026-05-17 03:06:00 | NOAA-21 | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 71daa31f-2541-30da-b335-cf7540c9e18c | -9.9148 | -37.10019 | 2026-05-17 03:06:00 | NOAA-21 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 13f22f2d-1639-3934-b11e-73fc5d901168 | -12.13194 | -39.77025 | 2026-05-17 03:06:00 | NOAA-21 | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 41b86bae-0db2-3ddd-b436-e03c4960dab2 | -5.91726 | -43.49714 | 2026-05-17 03:38:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| da910922-2b27-3f9b-beba-2f3a4f5547b6 | -7.48366 | -37.21001 | 2026-05-17 03:38:00 | NPP-375D | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fc6692f9-464f-3364-a069-b5b638ba0ab6 | -6.29982 | -43.63755 | 2026-05-17 03:38:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b1d881f6-5bf3-351b-a887-f6d180ed0ad5 | -6.29362 | -43.63644 | 2026-05-17 03:38:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9c2b4796-433a-3dcb-bb58-1dc01481b322 | -8.09524 | -43.15277 | 2026-05-17 03:40:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 36693985-70b6-37af-8bb2-9ae5b6b2fa1c | -9.45651 | -46.1137 | 2026-05-17 03:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f140d625-0201-33fb-9801-5b5afc9b8c48 | -12.26272 | -43.51132 | 2026-05-17 03:40:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| fdc0f83d-1d51-36bf-b52d-d9c7ff8aeceb | -11.88381 | -43.81072 | 2026-05-17 03:40:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| b2eb91f8-8be1-381f-8fae-ab3f90fd4e0e | -12.1338 | -39.76793 | 2026-05-17 03:40:00 | NPP-375D | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| e740cd8f-601a-39d5-b3ef-92bc8bc98d3c | -9.45777 | -46.1074 | 2026-05-17 03:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 66ffbfd0-5d68-3f3a-9020-04ab6df81d34 | -11.87853 | -43.81149 | 2026-05-17 03:40:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 40668189-0b53-3bf7-b351-d7dacf96e707 | -12.18413 | -39.15891 | 2026-05-17 03:40:00 | NPP-375D | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c85a5815-6550-36b0-ab9c-2d61f2077d44 | -9.45102 | -46.10575 | 2026-05-17 03:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f2961620-e09f-3f67-99a1-3dbbb0fbf62a | -12.27041 | -43.50964 | 2026-05-17 03:40:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e7617d7d-94ce-3186-9f2c-aa5b06db223c | -8.10612 | -43.15918 | 2026-05-17 03:40:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 487a1bf7-7be9-365d-88c4-098986e12a5a | -12.26825 | -43.51252 | 2026-05-17 03:40:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 10865800-eeaa-372a-8fdb-217d7cf6940a | -11.88422 | -43.81264 | 2026-05-17 03:40:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0e749459-7efe-3244-a388-15dac3f943a9 | -11.61063 | -47.09648 | 2026-05-17 03:40:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bc92bd06-0330-3b27-8916-64ae7d1c84ea | -11.88459 | -43.80669 | 2026-05-17 03:40:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| e60b2988-c9c4-39df-8879-e41893df54e7 | -9.91703 | -37.09739 | 2026-05-17 03:40:00 | NPP-375D | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| ed1b4c61-a323-3835-9c2d-24962ae2fea9 | -12.26347 | -43.5076 | 2026-05-17 03:40:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1ab1d210-2930-3543-a169-b67881021af0 | -9.47006 | -46.11684 | 2026-05-17 03:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5fbe3ec8-ff4a-3892-bbd6-38c8dca99127 | -8.10029 | -43.15806 | 2026-05-17 03:40:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 954a23cb-7d7d-3252-997b-8c38f30b02a8 | -11.87812 | -43.80954 | 2026-05-17 03:40:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 66fd442e-d3ef-3a47-9fc3-a6e51fc157e9 | -12.26488 | -43.50842 | 2026-05-17 03:40:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 200ff8ce-5bcc-3725-8171-002697be7d0c | -11.87934 | -43.80746 | 2026-05-17 03:40:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 2095428d-b29f-3edb-aacc-a41e3806691a | -12.26416 | -43.51215 | 2026-05-17 03:40:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 944ea3b3-a60f-3bdf-861b-0159a313a0e1 | -12.269 | -43.5088 | 2026-05-17 03:40:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 206fda13-cdeb-3c2a-83bd-020a3d5d493a | -12.2656 | -43.5047 | 2026-05-17 03:40:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 836f4239-815c-3351-9592-2ed3bf886af5 | -11.60928 | -47.10293 | 2026-05-17 03:40:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 14205567-4800-3143-8313-82166793218b | -12.27113 | -43.50592 | 2026-05-17 03:40:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 924cf601-3962-3033-b1a1-1a72e82a9521 | -9.44975 | -46.11211 | 2026-05-17 03:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9547919a-416c-3316-9c93-114e458e2160 | -12.26422 | -43.50387 | 2026-05-17 03:40:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1380590e-b09c-3f86-ac3a-d5874bd2709d | -11.88503 | -43.80862 | 2026-05-17 03:40:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a70540ee-f8a4-3877-b263-423e89f7eae4 | -13.5495 | -47.49671 | 2026-05-17 03:40:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4a688b77-9a01-311f-930d-9064d1badb2d | -9.46329 | -46.11525 | 2026-05-17 03:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3a974073-5875-3454-9587-b0ea7267aacf | -12.26974 | -43.50508 | 2026-05-17 03:40:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| cd2ed5b7-09f4-3402-8aef-372fe401dad2 | -16.04464 | -47.2331 | 2026-05-17 03:42:00 | NPP-375D | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 713623f3-0f60-322f-a89d-166bdc085bc7 | -16.04336 | -47.23898 | 2026-05-17 03:42:00 | NPP-375D | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3eb077cc-8b0c-3a11-90c4-f4a3b7b49ced | -16.05157 | -47.22878 | 2026-05-17 03:42:00 | NPP-375D | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| dbe6fddd-b1e9-3c5b-8739-d0df4b3b20f1 | -17.58064 | -44.94617 | 2026-05-17 03:42:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8bbcd2e2-b4f9-3144-88bd-2484fd35991b | -17.56416 | -44.94239 | 2026-05-17 03:42:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 451a44ea-c0c4-3a72-b0bc-c8bcf07240e8 | -17.56338 | -44.94609 | 2026-05-17 03:42:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d08555a9-8694-3860-a16b-de0fab0b039c | -17.56966 | -44.94363 | 2026-05-17 03:42:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ff36ae23-ba9b-3625-97cf-6c8d0d7a6afc | -17.56887 | -44.94736 | 2026-05-17 03:42:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d99fc961-2c18-3d81-8f84-8c328e75fcdf | -16.05025 | -47.2347 | 2026-05-17 03:42:00 | NPP-375D | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 2e77610d-a3d0-3b3c-a749-d9f2b3992e7c | -16.04594 | -47.22708 | 2026-05-17 03:42:00 | NPP-375D | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6bfb2d7a-35f1-3b5d-98a0-daa5ca737814 | -17.56259 | -44.94987 | 2026-05-17 03:42:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| dd61c088-17bd-398d-8a42-7e1f24f8894b | -17.56808 | -44.95113 | 2026-05-17 03:42:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a6b6cee9-76a9-30d3-8e0a-5be63af6f56c | -16.04377 | -47.23325 | 2026-05-17 03:42:00 | NPP-375D | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 100dd256-61c7-3381-b7e4-75c333a8927a | -16.04511 | -47.22725 | 2026-05-17 03:42:00 | NPP-375D | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 84061911-5b59-3657-8f6a-c4df1619976a | -17.57985 | -44.94992 | 2026-05-17 03:42:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 21879cc1-8913-3958-aaff-fa606e65db17 | -4.3699 | -37.89632 | 2026-05-17 03:55:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e82a9797-94bf-3f3b-b7de-8939cc8fa4b8 | -11.02513 | -48.93151 | 2026-05-17 03:57:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0a172550-9742-3290-94f8-c1c35efed93f | -12.18256 | -39.15767 | 2026-05-17 03:57:00 | NOAA-20 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 18296e6c-bfbc-37b7-bb8a-5611a840939e | -9.44323 | -46.12005 | 2026-05-17 03:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 919ccb9d-a6c8-3109-950f-955642ecb147 | -8.1049 | -43.1573 | 2026-05-17 03:57:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 71262663-756c-30bb-8f0e-9749c4e91982 | -11.87905 | -43.80646 | 2026-05-17 03:57:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9fa08d8a-516b-361a-aae9-83831a72eaf6 | -13.22304 | -41.32938 | 2026-05-17 03:57:00 | NOAA-20 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 463f6be8-1dc8-3035-b941-7d0b32b0b58f | -8.47691 | -46.41048 | 2026-05-17 03:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6350c2e0-a322-3e7f-9b3d-6b307bdbd9c1 | -11.60815 | -47.09929 | 2026-05-17 03:57:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c3d0905d-8b14-302b-96f4-57f0c73816bc | -10.40815 | -44.93877 | 2026-05-17 03:57:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |


[Clique aqui para ver as próximas entradas](README2.md)
