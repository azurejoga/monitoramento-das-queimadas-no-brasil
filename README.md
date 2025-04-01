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
| afaa428c-02f9-37c2-a4ce-01aa3b13c8a6 | -13.033 | -45.1027 | 2025-04-01 00:00:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 81.6 |
| fa4a2491-5490-3292-9e40-3eb687b70dac | -13.033 | -45.1027 | 2025-04-01 00:10:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 2a8ef83e-94e9-3d1a-ba40-0a9cc740b080 | -13.033 | -45.1027 | 2025-04-01 00:20:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 494ebd0a-f890-3a72-850f-0cd670479462 | -16.65501 | -44.04316 | 2025-04-01 00:22:00 | TERRA_M-M | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 40a9d0e1-f297-3456-a26a-673643eae5ac | -9.54283 | -43.03697 | 2025-04-01 00:24:00 | TERRA_M-M | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 34ed0557-333c-3b58-aea9-cdbcbbcce83d | -13.31641 | -44.19761 | 2025-04-01 00:24:00 | TERRA_M-M | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f254d73e-a8fa-38e6-9d09-9fd0a5bbf824 | -13.02876 | -45.10351 | 2025-04-01 00:24:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 7e283ac9-3ad3-3549-a499-472329119fe3 | -9.54159 | -43.02805 | 2025-04-01 00:24:00 | TERRA_M-M | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 98bf3358-55d8-30fd-abfc-8fc2eed46bab | -12.30489 | -42.03582 | 2025-04-01 00:24:00 | TERRA_M-M | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 419c30da-2a7c-38d6-ab04-89584fdac028 | -13.58741 | -45.24675 | 2025-04-01 00:24:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 37cc5696-665d-3955-9e94-d69a7c2a3786 | -13.02732 | -45.09233 | 2025-04-01 00:24:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 49.5 |
| b7767763-a5ce-31df-acae-66d1253e6100 | -11.93818 | -43.93494 | 2025-04-01 00:24:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 19aba91a-2b9e-380f-89d9-01b6f5196327 | -7.23276 | -44.78177 | 2025-04-01 00:24:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f1ac51e4-27ab-302d-aecf-a500458be95e | -6.2074 | -48.04256 | 2025-04-01 00:24:00 | TERRA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 7adda7e2-d013-38eb-9c48-8aa9e57d241c | -7.23148 | -44.77246 | 2025-04-01 00:24:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 8b4c10a3-1693-3c00-8670-e02cfc98b0c4 | -13.03855 | -45.10218 | 2025-04-01 00:24:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 12a71465-db99-3e8f-a9f7-95a62412b088 | -13.04 | -45.11338 | 2025-04-01 00:24:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 0f2b2a10-9c93-357e-a891-9ceea0640902 | -7.24064 | -44.77441 | 2025-04-01 00:24:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 3d4833c9-d9ba-32d9-881c-9ae804cf2d7e | -13.0302 | -45.11471 | 2025-04-01 00:24:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 0989bfce-ed57-385b-8cc9-91e8c43f3e4d | -12.29029 | -43.54237 | 2025-04-01 00:24:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 4ca19086-286f-35ec-8e4f-7f1c74f806fe | 2.2333 | -60.7018 | 2025-04-01 00:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 134f0a7f-950b-3d64-81e2-3987b48be41c | -13.033 | -45.1027 | 2025-04-01 00:30:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 98f49771-8976-38c2-b9c1-e78d25dbd6c1 | 2.2515 | -60.7015 | 2025-04-01 00:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 60.9 |
| dcd3e2bd-cacc-3c45-b6ae-d76339819d94 | -13.033 | -45.1027 | 2025-04-01 00:40:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 0066e957-2c90-347e-a857-f73150951682 | -13.033 | -45.1027 | 2025-04-01 00:50:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 69.0 |
| e841e785-a977-3274-b74a-11fc2befbe17 | 2.2333 | -60.7018 | 2025-04-01 00:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 6291fcfa-23b8-3123-9ae1-a89ddcb8dc40 | -13.033 | -45.1027 | 2025-04-01 01:00:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 8e555f61-b533-3e01-8ad1-61a4e795c823 | 2.2515 | -60.7015 | 2025-04-01 01:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 48d7cafe-bf15-35ab-9974-5026d5e84221 | 2.2333 | -60.7018 | 2025-04-01 01:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 4753e449-a8ee-3141-8bae-c6f9af5d2450 | 2.2333 | -60.7018 | 2025-04-01 01:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 259f114c-10fc-339e-982f-84a9ff95d522 | -13.033 | -45.1027 | 2025-04-01 01:10:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 361fdb47-69ac-3128-9061-594a7858c514 | -13.033 | -45.1027 | 2025-04-01 01:20:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 6b35b332-ccc3-36d0-83a9-0d3eab4f5f48 | -13.033 | -45.1027 | 2025-04-01 01:30:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 10d6c2d2-3d78-3f33-bfe5-1fa62ea0e219 | 2.2515 | -60.7015 | 2025-04-01 01:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 53.6 |
| f82e4de9-0832-3235-91b9-777f9cbbd759 | 2.2333 | -60.7018 | 2025-04-01 01:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 46.2 |
| e0631dd9-fc5a-3fea-8df6-956094a6e64d | 2.23751 | -60.72146 | 2025-04-01 02:06:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 56.9 |
| b1785932-9778-3e59-9a6f-a3871b801708 | 2.24659 | -60.71743 | 2025-04-01 02:06:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 4f52e0a1-c397-3c53-a467-85a8283ed685 | 2.2333 | -60.7018 | 2025-04-01 02:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 286c7944-f03c-3a11-b542-cc0045011116 | -8.38952 | -35.02744 | 2025-04-01 03:10:00 | NOAA-21 | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| d6a663b6-39f1-35d5-8036-6d6a795f582d | -12.96661 | -41.94619 | 2025-04-01 03:13:00 | NOAA-21 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7f2403cd-e6d7-306c-b94e-3622b0dbca02 | -15.8974 | -43.46025 | 2025-04-01 03:15:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| cb62fe44-667b-3626-bff6-1fb4e1f1517d | -15.88361 | -43.45714 | 2025-04-01 03:15:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2bd861f4-eb36-3452-8b52-9b4f381b8467 | -16.09418 | -42.2825 | 2025-04-01 03:15:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 6409a93e-9dac-31e4-aa70-a478f361f6b2 | -15.89051 | -43.45868 | 2025-04-01 03:15:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 91a54011-4cf3-3bfa-880e-ab62f3439ad8 | -16.09385 | -42.28454 | 2025-04-01 03:15:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 8768ced1-71fa-3c06-af02-05efa7fc6c85 | -16.09302 | -42.28784 | 2025-04-01 03:15:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| a33cd6f3-84b8-3603-b4d8-67917a7ee1a9 | -3.89431 | -38.63961 | 2025-04-01 03:34:00 | NPP-375D | MARACANAÚ | CEARÁ | Brasil | 2307650 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 73d176b2-36c6-3b53-b95b-a842ba7be1ec | -7.4778 | -34.84301 | 2025-04-01 03:36:00 | NPP-375D | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| b5745cc9-f91d-3f71-a9d6-e83eb451c600 | -7.92716 | -35.46339 | 2025-04-01 03:36:00 | NPP-375D | LIMOEIRO | PERNAMBUCO | Brasil | 2608909 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0f90942d-9e59-33f6-afec-e962ceb95393 | -9.54136 | -43.03428 | 2025-04-01 03:36:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ed05675f-d391-3031-b6bd-d0fbae7249fa | -9.7272 | -36.91956 | 2025-04-01 03:36:00 | NPP-375D | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 301071e0-6675-33a7-804b-9d689a05f314 | -9.32907 | -37.00954 | 2025-04-01 03:36:00 | NPP-375D | IATI | PERNAMBUCO | Brasil | 2606507 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e7083067-b4cf-325f-9522-ddf2760eb640 | -7.23184 | -44.77533 | 2025-04-01 03:36:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 30574f92-e16c-3a43-be71-d8c0e9f7394c | -7.23872 | -44.77197 | 2025-04-01 03:36:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 360aa9ce-111e-38e3-8b28-21be226e231d | -7.23267 | -44.77087 | 2025-04-01 03:36:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7a1c8f8b-a355-3721-bdf6-830669ac711b | -7.47444 | -34.84247 | 2025-04-01 03:36:00 | NPP-375D | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 1c05ebab-fafb-3b38-a526-ae8eecfeb757 | -12.29373 | -43.54565 | 2025-04-01 03:38:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1c126efe-803b-3c76-ae34-756a9bb359e1 | -13.02866 | -45.09381 | 2025-04-01 03:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 740bc088-09e5-3dbe-a36f-42b1bc175b9d | -13.58404 | -45.24442 | 2025-04-01 03:38:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3a16d064-b6b5-36c2-96d1-cc3affd17495 | -16.0907 | -42.28305 | 2025-04-01 03:38:00 | NPP-375D | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| b866c588-626b-34c9-95a7-37f332e906f6 | -13.02479 | -45.11289 | 2025-04-01 03:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f635432a-5305-3c60-b690-1fe4160b9bbd | -13.58328 | -45.24817 | 2025-04-01 03:38:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 50655ac6-ae7e-3df6-a7bf-ccac0a20e4cf | -13.03594 | -45.11522 | 2025-04-01 03:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b0710a18-c55d-315f-8843-b5de4e41892e | -13.04229 | -45.11256 | 2025-04-01 03:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9e9fb8c6-d4ac-392e-83cd-aac90824fb3a | -12.28863 | -43.54459 | 2025-04-01 03:38:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6ec1d8d2-3414-3b3b-983d-acf308db73b3 | -13.02789 | -45.09763 | 2025-04-01 03:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7517c7e6-29e0-3a45-9eb0-7eed774d0770 | -13.03277 | -45.11344 | 2025-04-01 03:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f5387412-2cc8-33b1-ad9b-a0a5580c4b55 | -12.96311 | -41.94762 | 2025-04-01 03:38:00 | NPP-375D | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 74139a13-38bc-399b-a23e-5cb252a2f208 | -13.03909 | -45.11079 | 2025-04-01 03:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 105919d0-bba2-3d3f-999a-af542ad9dee8 | -13.03114 | -45.11023 | 2025-04-01 03:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| aabf20ca-452f-3cb5-92b3-6fa46512d174 | -13.03749 | -45.10758 | 2025-04-01 03:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 92515184-da5d-310c-aace-3be4df1f7e62 | -15.88664 | -43.45817 | 2025-04-01 03:38:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b29407b2-6b45-3365-9f23-5ddc8a4b28a0 | -13.03019 | -45.09695 | 2025-04-01 03:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 92285073-e020-3c15-b22f-b66d3fb60a47 | -13.02869 | -45.10459 | 2025-04-01 03:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1a5141c6-88f4-314e-af2a-d1ffe9287196 | -13.02386 | -45.09959 | 2025-04-01 03:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 98606810-bd5f-347b-9145-4ac644cb72bf | -16.6539 | -44.04097 | 2025-04-01 03:38:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 01e36f69-5407-33f9-9731-8c79c62b8098 | -13.02536 | -45.09195 | 2025-04-01 03:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5a44dab4-730d-3868-a0c5-2a7227eb5640 | -16.09508 | -42.28403 | 2025-04-01 03:38:00 | NPP-375D | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 29fe4450-1c92-34c9-884e-5cc97e83b6f2 | -13.02461 | -45.09578 | 2025-04-01 03:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 88d24ca5-fa0a-3e3d-82a8-e4a0eaae2ba3 | -15.89722 | -43.45475 | 2025-04-01 03:38:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9d2a8802-e3b7-3f15-9e85-7e4bed8d2b9b | -12.28922 | -43.54152 | 2025-04-01 03:38:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3558ae60-3d47-34b8-ad27-256f4e48d9ad | -13.04152 | -45.11639 | 2025-04-01 03:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d351d47b-4016-3dbe-a243-1e073515e63f | -13.02712 | -45.10143 | 2025-04-01 03:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 943cf435-bf8c-363f-9313-7737326e8062 | -13.02944 | -45.10077 | 2025-04-01 03:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c889a87e-031a-37e9-9236-798448c898ff | -13.02644 | -45.1161 | 2025-04-01 03:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fed5d2dd-db2c-3ead-92ba-dd2441f72765 | -13.03352 | -45.1096 | 2025-04-01 03:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ed0a4dac-8f1c-3c67-94f1-0b92fd8796b2 | -13.0376 | -45.11846 | 2025-04-01 03:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a28f379e-0423-3976-9b81-e2b33be61d2c | -13.03269 | -45.10259 | 2025-04-01 03:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4bb5ecd6-7885-3ee0-b813-7733b5f5f31c | -13.02959 | -45.11788 | 2025-04-01 03:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e8beafe9-924e-30ae-b4f3-8c2c5de87956 | -15.89617 | -43.46012 | 2025-04-01 03:38:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 92aa6cab-8ee2-365a-bd19-14ae5d04987e | -13.03984 | -45.10696 | 2025-04-01 03:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0f700f81-83c6-3f0c-9d48-f41028dd9906 | -13.03672 | -45.11139 | 2025-04-01 03:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d1f29d69-ec3f-3a8e-a231-3c28d2cac0b2 | -17.62913 | -39.69389 | 2025-04-01 03:38:00 | NPP-375D | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2b4b582d-beb8-356d-b8dd-ca4f0602c3d1 | -17.60169 | -39.70959 | 2025-04-01 03:38:00 | NPP-375D | TEIXEIRA DE FREITAS | BAHIA | Brasil | 2931350 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a1cf52a9-2aae-3d3a-8c34-9690b69ea7e7 | -13.58252 | -45.25197 | 2025-04-01 03:38:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 368fe53b-12cf-3313-9981-0136221e5a24 | -13.03202 | -45.11728 | 2025-04-01 03:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5459fb0d-48ec-3ef7-a6cf-b163242e818e | -13.03036 | -45.11406 | 2025-04-01 03:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 912248f2-7b25-3d68-a480-6439219d8594 | -13.02719 | -45.11226 | 2025-04-01 03:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5cb6b414-eb50-36ad-a284-ac975f511c98 | -13.03834 | -45.11462 | 2025-04-01 03:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e4915649-569e-3b6c-a3c6-7461800435b6 | -19.33718 | -45.00981 | 2025-04-01 03:40:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README2.md)
