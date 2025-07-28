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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6bae78dd-9405-35aa-b417-bb1d7ff222a6 | -3.21894 | -48.81839 | 2025-07-28 05:04:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| aff1af6e-d54a-3af6-8ca4-137269091ac3 | -4.16863 | -46.82027 | 2025-07-28 05:04:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 14f0b3aa-81df-3a39-827e-baf11db6f8a0 | -3.29777 | -49.19258 | 2025-07-28 05:04:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cb818dbd-a973-3aa6-a7a9-f25c66f7fa05 | -3.90955 | -47.82403 | 2025-07-28 05:04:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98922e95-2860-3d85-91a8-f9269161bc24 | -4.16395 | -46.8167 | 2025-07-28 05:04:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 72f0ff7f-5103-3c92-a602-72e709bea104 | -3.52831 | -52.86944 | 2025-07-28 05:04:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00964c87-1904-31e5-b225-8ca46764a575 | -3.13965 | -47.01413 | 2025-07-28 05:04:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 272584f9-96f5-398b-aa9d-11e8f1be0c33 | -4.10836 | -47.93238 | 2025-07-28 05:04:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 41f6d536-ca23-351a-9706-399cdb003119 | -3.61978 | -49.54519 | 2025-07-28 05:04:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 795e56ee-da86-3dca-8c4b-dd2ae2e65645 | -4.11337 | -47.92657 | 2025-07-28 05:04:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 700e4169-4034-3841-9748-ddb6fbbd5364 | -4.10986 | -47.92195 | 2025-07-28 05:04:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2942d18d-4170-30ee-b9cd-66a3d1977518 | -4.15375 | -46.81514 | 2025-07-28 05:04:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a8f140e1-9c31-36b9-a1f9-6d299548bdd5 | -3.62037 | -49.54134 | 2025-07-28 05:04:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13be2ea3-43d6-3754-8630-afbb5f447992 | -3.36313 | -49.16569 | 2025-07-28 05:04:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bbf88e2d-c2ad-33f2-b190-e23e3cc664cb | -4.10868 | -47.92567 | 2025-07-28 05:04:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 065e07c1-9dde-33ed-b8c8-c816481d796f | -7.10944 | -44.91619 | 2025-07-28 05:06:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 0f348870-e6ee-323e-9f3d-795fe1819fd3 | -7.07792 | -44.92146 | 2025-07-28 05:06:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9b8820d3-41af-3fa2-b366-9824e5695ec2 | -10.521 | -42.55601 | 2025-07-28 05:06:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 0234f455-b7a4-3b51-acce-8b620e73b898 | -10.45428 | -46.51279 | 2025-07-28 05:06:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1445bd15-d1b1-3631-857e-8fbcad337860 | -7.10932 | -44.92185 | 2025-07-28 05:06:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7e96ca3e-d79a-34c8-b991-5c8a67b70b46 | -7.69739 | -46.05094 | 2025-07-28 05:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cc8555c0-2037-3042-917a-1022f83b974e | -6.49816 | -56.19958 | 2025-07-28 05:06:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 16287b67-6672-30b5-a8b5-2ce1c9a293d6 | -6.53655 | -56.18821 | 2025-07-28 05:06:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b9c1a95-586b-3681-9d00-49a813207cb4 | -7.09788 | -44.95515 | 2025-07-28 05:06:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a0379f36-1541-35e0-a821-0f9f8fb7ce6f | -6.25855 | -42.83348 | 2025-07-28 05:06:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 83b4d181-d3f4-3da4-beb1-2e51374d24d6 | -6.40353 | -53.36521 | 2025-07-28 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2f9c71a3-07c8-3f72-89b4-976c2e8625de | -6.90155 | -52.86788 | 2025-07-28 05:06:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4558b0a9-672e-32f4-9f2c-d624a19fa428 | -6.49706 | -56.20654 | 2025-07-28 05:06:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 78282e50-1c67-3006-9f23-8c2a4fabb88f | -7.09915 | -44.95239 | 2025-07-28 05:06:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 479ac46b-50ab-33c4-ac7e-4f5b0c73c44b | -6.49871 | -56.1961 | 2025-07-28 05:06:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 308adff0-8d67-3608-9545-70a6636d483d | -7.07378 | -44.90665 | 2025-07-28 05:06:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 830d4040-f0c4-3042-9fd3-646f932c755d | -6.49318 | -56.20948 | 2025-07-28 05:06:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4fe24908-a6cf-30ed-9c11-b41db1a9fb33 | -6.25997 | -44.96413 | 2025-07-28 05:06:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1385e572-aece-3b54-a74a-5c0cb3496ea1 | -6.44657 | -53.34795 | 2025-07-28 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9b8db72-2e39-3962-ab71-3e41fb07f2c2 | -4.15843 | -50.22495 | 2025-07-28 05:06:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c553831-d6db-3087-899b-40e55c6dc68a | -4.86118 | -47.75037 | 2025-07-28 05:06:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb4b08d3-cf3e-3f5d-a568-b87793bc57c3 | -6.99069 | -47.07825 | 2025-07-28 05:06:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2f032ade-c833-3fe4-80a1-1da604d6981b | -7.21406 | -44.1703 | 2025-07-28 05:06:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3dcf7608-8296-3708-9f86-7fcefb5789c4 | -6.55426 | -56.1839 | 2025-07-28 05:06:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5de81e5e-c950-396d-be38-42da9efbbd6e | -6.40412 | -53.36136 | 2025-07-28 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 11938c35-e547-330e-8bab-0bb454a2b224 | -6.39893 | -53.3487 | 2025-07-28 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b427a1b2-8fc6-3b81-a751-d90fa188f0c0 | -7.6664 | -44.80524 | 2025-07-28 05:06:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f850f2a6-8973-3afa-8d24-46c5ef7931ac | -6.91967 | -44.24833 | 2025-07-28 05:06:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 478a202f-aca7-3e8b-aa5c-9887322d064e | -6.39833 | -53.35255 | 2025-07-28 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 94eb31ac-6bf4-33d6-a6f8-c4cf88501342 | -7.09607 | -44.92903 | 2025-07-28 05:06:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bbf90991-45b9-3844-9073-c20c4023c487 | -7.24864 | -45.39624 | 2025-07-28 05:06:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3a3edcbc-3fac-380b-a0d3-452ea5a63f6b | -7.65421 | -44.80304 | 2025-07-28 05:06:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 15285514-0689-3d04-b30f-46261aa19cee | -7.6543 | -44.80227 | 2025-07-28 05:06:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2434d3ec-a173-3422-ab23-1381c9be4441 | -3.82943 | -54.12189 | 2025-07-28 05:06:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1bfc8c17-fb85-3569-bdd6-162dfa80ff3a | -7.10432 | -44.91305 | 2025-07-28 05:06:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6b07be77-e470-30b0-b95c-71e04440de72 | -7.53589 | -44.42928 | 2025-07-28 05:06:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ba55eb2c-97c7-391b-847b-33c3e779d49e | -7.11548 | -44.91706 | 2025-07-28 05:06:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5395da61-e822-35af-b1d2-df7b7d28deb4 | -7.53346 | -44.39921 | 2025-07-28 05:06:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d3befeee-4d04-3e84-bbd7-67d514bb2cf8 | -7.08338 | -44.92649 | 2025-07-28 05:06:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5c1114ea-48a9-357c-b2ef-66c364417cac | -4.30302 | -48.10194 | 2025-07-28 05:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 1363e369-0dbc-3e6f-86c2-e1df6585ecce | -7.24278 | -45.39537 | 2025-07-28 05:06:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a98f296a-303a-32f1-a0f2-c0a818cac23b | -7.24393 | -45.38704 | 2025-07-28 05:06:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 887ead2f-c8cc-31a0-8d4b-b052eefb7015 | -6.3873 | -43.68969 | 2025-07-28 05:06:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3977dcb1-3349-3d76-b550-c6da7e425ee4 | -6.99024 | -47.08146 | 2025-07-28 05:06:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ae52843-34bf-3f38-80c8-4b54353b3b71 | -7.10108 | -44.93204 | 2025-07-28 05:06:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 05c734d8-a995-381e-a5fa-fb9a266493f0 | -6.40063 | -53.36082 | 2025-07-28 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a4db3577-fe63-382b-9300-953af4138e19 | -7.11094 | -44.90955 | 2025-07-28 05:06:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 27c82566-8d41-3a4d-af6d-7b8500f16af4 | -6.50038 | -56.20707 | 2025-07-28 05:06:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 50ba3b7f-ced4-3d86-956f-543ed173acf6 | -7.10833 | -44.92416 | 2025-07-28 05:06:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4730b6c6-c976-3087-90ec-5a6c3c61cf67 | -6.4965 | -56.21001 | 2025-07-28 05:06:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f6017164-289e-3d90-8fe2-54b34ce0cc9c | -6.4019 | -53.32941 | 2025-07-28 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3c6cc17f-b045-3865-bdb3-16adf8b74018 | -6.89796 | -52.86733 | 2025-07-28 05:06:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4ad55131-e982-3a28-8dd5-67347767adc0 | -7.69274 | -46.04247 | 2025-07-28 05:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1668330a-f910-3b06-897d-4f1a8c367f14 | -7.24335 | -45.39121 | 2025-07-28 05:06:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bb4cfc29-2d24-37b9-b880-b407cdadecce | -7.09854 | -44.95034 | 2025-07-28 05:06:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1f4d356b-2b86-3cd4-bec0-811572779996 | -7.08445 | -44.92379 | 2025-07-28 05:06:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a3f69366-bb8a-334c-a215-bfedf6eb943d | -6.41708 | -53.32381 | 2025-07-28 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7463b5c8-19b1-3c73-8b9f-a0184e1be41c | -7.08504 | -44.91927 | 2025-07-28 05:06:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 61d4d26a-fc13-370c-bc68-53122267e840 | -6.89438 | -52.86678 | 2025-07-28 05:06:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5ae87d01-37d4-3c63-b25b-0168ad6e9aad | -6.39381 | -43.69028 | 2025-07-28 05:06:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ffa679f9-2559-38f9-9101-19b41694c3dd | -7.0943 | -44.94254 | 2025-07-28 05:06:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 847950d9-2ec8-392b-a830-78f06c0e6a50 | -6.49928 | -56.21402 | 2025-07-28 05:06:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| e256c2ec-210b-30a8-98a9-5d20c19b79e5 | -6.49151 | -56.19853 | 2025-07-28 05:06:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b495bb8e-7ff0-3eac-a3b9-636473b2ac45 | -7.66093 | -44.79928 | 2025-07-28 05:06:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 68738a8f-dc18-3165-a227-2117b4d61cf1 | -7.10158 | -44.93388 | 2025-07-28 05:06:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b6e70f73-fb84-368f-aa47-951f242109d4 | -7.14621 | -48.2058 | 2025-07-28 05:06:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 137b878f-c1f9-369c-a835-8653f88d04b9 | -7.66148 | -44.79557 | 2025-07-28 05:06:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 30a227d0-5867-3fd6-9413-e84324cffdbb | -7.09308 | -44.94539 | 2025-07-28 05:06:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| db834c13-6ec3-3e58-be55-6f968b38a4d2 | -6.53599 | -56.19168 | 2025-07-28 05:06:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea71fbef-0a1c-351a-a5da-d47b500c79ba | -3.88372 | -54.21311 | 2025-07-28 05:06:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f60dd7d5-b538-35b4-a5d2-22450df25195 | -6.88659 | -52.86971 | 2025-07-28 05:06:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f449e56f-18dc-3352-b903-3c8b351dd308 | -7.66026 | -44.80443 | 2025-07-28 05:06:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4dcf9f2e-0b1d-3ec1-ab3d-43e365998c3a | -4.30701 | -48.09588 | 2025-07-28 05:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c26ea920-9db7-33fa-afc8-ded4c185d14a | -4.30159 | -48.10009 | 2025-07-28 05:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 4ca552a0-2b86-3b92-94b2-6c4343f3ade8 | -6.54541 | -56.19674 | 2025-07-28 05:06:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 54028f09-085e-35c7-8cf4-4fbd7f19960a | -7.10878 | -44.92593 | 2025-07-28 05:06:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1fc98ffb-cc7c-32b8-b2c8-ad63fa3c3f22 | -7.66649 | -44.80456 | 2025-07-28 05:06:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ac0bb2dd-a64b-3d38-b588-dabfc8b56a65 | -6.44307 | -53.34741 | 2025-07-28 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0fde585b-963c-31b7-b1ed-8f6027fa5b11 | -7.09923 | -44.94542 | 2025-07-28 05:06:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4106e8c7-b3bc-3247-a392-2031d4939460 | -6.92733 | -44.239 | 2025-07-28 05:06:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3ab2f691-39d8-34be-b811-d5dc4607f03a | -6.39774 | -53.35641 | 2025-07-28 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a66e8df8-517b-3039-b72a-c95fec12a992 | -6.5026 | -56.21454 | 2025-07-28 05:06:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3e400ccf-566a-381e-b24e-e657005d7a52 | -6.40123 | -53.35696 | 2025-07-28 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 85b74240-ec50-3d53-8211-686bcc5008ff | -7.21471 | -44.16531 | 2025-07-28 05:06:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9acf546c-e537-32ac-bc17-4f4b13dd532b | -7.66087 | -44.80003 | 2025-07-28 05:06:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README16.md)
