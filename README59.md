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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 47e4092f-561c-340f-a943-04a0ca075def | -6.73947 | -63.05731 | 2025-10-19 05:25:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 076f9b42-181e-314e-9415-e1b1f717416e | -6.64 | -62.91111 | 2025-10-19 05:25:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8cf36699-ec03-38b5-84e8-8f478d1b2346 | -7.62375 | -60.92799 | 2025-10-19 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 2aab1beb-d3b5-38be-a4e2-6a0312e6c2d1 | -9.07144 | -57.36565 | 2025-10-19 05:25:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e083ce1b-f422-393e-92e4-0b916cc9461c | -7.26487 | -59.4911 | 2025-10-19 05:25:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71b5f7ce-7a93-3f15-9a47-0ad5a461326b | -7.6205 | -60.94871 | 2025-10-19 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c8d5fd88-c592-37ca-ba07-d258169e74ac | -8.05167 | -55.09694 | 2025-10-19 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aab5ea53-98f3-3bde-91ce-133116822fe8 | -15.73981 | -44.58529 | 2025-10-19 05:25:00 | AQUA_M-M | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 096ee36c-9ac8-33f5-8fb4-1011212e2dfb | -7.62321 | -60.93144 | 2025-10-19 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| ab986c93-2c7e-3a28-b3ba-bffd8da729f1 | -16.77742 | -42.75607 | 2025-10-19 05:25:00 | AQUA_M-M | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 116ba312-f4d3-39b6-b8a8-7f9d7d717ef0 | -6.62072 | -62.87663 | 2025-10-19 05:25:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 35e53c3b-6724-3892-86a6-900d7164aace | -7.88725 | -61.17942 | 2025-10-19 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c585f0eb-ffcc-39f0-a66d-baa24f9b5885 | -7.62429 | -60.92453 | 2025-10-19 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 21.7 |
| a2263b33-26dd-3b6e-966a-da8592094af9 | -8.60306 | -64.09492 | 2025-10-19 05:25:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4aa7b616-3030-3221-85aa-6125f4273c64 | -16.8088 | -42.8263 | 2025-10-19 05:25:00 | AQUA_M-M | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 16.0 |
| dce2518a-7837-3ee1-b307-1ead3ed81685 | -7.82005 | -61.68993 | 2025-10-19 05:25:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55c99928-189f-3abd-b28e-f70992055dc8 | -7.67382 | -63.49726 | 2025-10-19 05:25:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b8204428-bb11-3b1f-997f-1aa56e56cd89 | -6.63192 | -62.80793 | 2025-10-19 05:25:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0ba18ce-cabf-3254-8083-bb4d87e9b103 | -8.60375 | -64.09079 | 2025-10-19 05:25:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 843df8e7-be07-39ca-aaa6-c3f00f2619e1 | -6.64347 | -62.91167 | 2025-10-19 05:25:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 50795fd9-c364-3748-b412-bc4a043f38d1 | -6.73472 | -63.06452 | 2025-10-19 05:25:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b38d1d4f-2f58-38b8-80e2-4d6c4d70c47f | -8.22988 | -61.48709 | 2025-10-19 05:25:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e404550f-4233-3c10-889d-f67fa7f35dad | -7.11814 | -63.04531 | 2025-10-19 05:25:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88bf768e-ddb1-3d7e-a9c6-50117206d9c0 | -6.6313 | -62.81173 | 2025-10-19 05:25:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2d04f278-f919-3531-87c9-0ffd41863592 | -7.62208 | -60.91711 | 2025-10-19 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8c55e0bf-7261-30f5-a0b8-e05b4db25073 | -9.31157 | -60.8816 | 2025-10-19 05:25:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e28bc2d0-9dc2-3e5a-9472-abbbdedf8df4 | -6.96602 | -63.02559 | 2025-10-19 05:25:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e42489c-b6bf-345b-8cd1-1f34260c9b2f | -9.23632 | -57.69222 | 2025-10-19 05:25:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4217d8b1-1525-30bd-b942-190f2ab7183e | -16.14903 | -41.14489 | 2025-10-19 05:25:00 | AQUA_M-M | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 92832643-d109-3128-8d54-22426ffda8be | -8.15823 | -61.42577 | 2025-10-19 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da88e3cd-9b02-3ea1-92ae-61e07968525f | -9.29086 | -57.54697 | 2025-10-19 05:25:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b86372b3-7335-3965-b895-2396908c0ba8 | -3.39922 | -54.06849 | 2025-10-19 05:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 699affb6-8c03-31f0-bada-0214c69d0391 | 1.7907 | -56.01875 | 2025-10-19 05:50:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2cb82156-5117-3811-9888-c7043e7e7f1b | 1.78587 | -56.0227 | 2025-10-19 05:50:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cbca5226-449a-3ed2-bfa6-c5f874f2c7cf | 1.83388 | -55.66704 | 2025-10-19 05:50:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 165d6ecb-6b3c-3f92-9dd5-81d25f6508cc | -2.9102 | -52.72334 | 2025-10-19 05:50:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| de141622-7a85-3a9f-aae8-7f17d09e86ef | 1.74302 | -55.94666 | 2025-10-19 05:50:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3abc99b-dd94-3e1c-a988-b2dd1fbe7d17 | 1.80096 | -55.70489 | 2025-10-19 05:50:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 20a8376b-b995-3650-a5c5-fd360c7dc323 | -2.91712 | -52.72514 | 2025-10-19 05:50:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a26f3f9e-aa2a-35c9-b17c-999e0a047c2b | 1.74895 | -55.93243 | 2025-10-19 05:50:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 99c1a198-6405-3c7f-98ab-78282fb93656 | 3.17118 | -60.28586 | 2025-10-19 05:50:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a64de3d3-16c9-313f-8569-20f03e4475ab | 1.74356 | -55.95004 | 2025-10-19 05:50:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 16ea928c-6254-37d3-b221-c5605c69dc4b | -2.81212 | -58.29062 | 2025-10-19 05:50:00 | NPP-375D | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d4bbdc37-9c9a-3cda-98b5-1c395dbf6670 | 1.8003 | -55.70243 | 2025-10-19 05:50:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 692b36ae-522b-3764-b3c9-7916018dda08 | -2.91376 | -52.72668 | 2025-10-19 05:50:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 44243e8e-ee84-3ec2-a992-09375624434e | 1.80086 | -55.70596 | 2025-10-19 05:50:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c06fdfff-1efd-3981-9eb6-dce5228cd7b1 | -2.32327 | -57.10917 | 2025-10-19 05:50:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b062623e-4525-31ac-b2fa-9ee5eac4b029 | -2.91479 | -52.71961 | 2025-10-19 05:50:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a1eacb41-a056-369b-a036-bb69cfa212e3 | 1.7441 | -55.95341 | 2025-10-19 05:50:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e38bb35a-4c1b-348c-927f-d64f8c97cbf9 | 1.83935 | -55.6662 | 2025-10-19 05:50:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8d671ff4-8d5a-31fd-a707-644c78189a53 | 3.16726 | -60.28649 | 2025-10-19 05:50:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9965db6f-19fc-3677-8834-daecaf2d9e13 | 1.74839 | -55.9291 | 2025-10-19 05:50:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 78cacf26-956b-390d-9cca-15d096faca84 | 1.74034 | -55.96439 | 2025-10-19 05:50:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e9868f7-bd96-37db-90d1-5c663bb99c55 | 1.80037 | -55.70138 | 2025-10-19 05:50:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9dab3e21-df05-3ce6-a058-c7daaa014f2a | 1.74463 | -55.95677 | 2025-10-19 05:50:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dd292fc3-c853-318a-b083-deb0756384b8 | -3.40003 | -54.06294 | 2025-10-19 05:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 66d96978-5df9-3a73-930c-ec2303eb5cb2 | 1.48501 | -56.05025 | 2025-10-19 05:50:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 84b0ea82-7664-37a1-811f-030d075a8ffc | 1.79016 | -56.01544 | 2025-10-19 05:50:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bdf046ec-b600-37c3-87ae-cbf313c2f9d1 | 1.75321 | -55.92488 | 2025-10-19 05:50:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eef592ab-54d3-36c6-9e49-afaf16ebd732 | 1.48447 | -56.04692 | 2025-10-19 05:50:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 609f01af-f651-3497-8a90-6d4e7c304eb2 | 1.73981 | -55.96105 | 2025-10-19 05:50:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| be42a46a-4101-3bcf-adc9-fa656054e0c4 | -8.23193 | -61.48853 | 2025-10-19 05:53:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa84fd5c-b123-38ac-8c81-d0865badf67a | -9.22184 | -61.83152 | 2025-10-19 05:53:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a09a26cd-27c0-36e1-852d-277eb1b69bcf | -9.90727 | -63.58405 | 2025-10-19 05:53:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b5f6255e-bc53-3045-a582-1084dc6bfbee | -9.73941 | -65.88666 | 2025-10-19 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 097f2aaf-6fc9-3d1b-9afe-f30a6c6486fc | -6.52594 | -60.0346 | 2025-10-19 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d7e74e21-5032-3883-acaf-dbc655fff545 | -10.0414 | -59.36695 | 2025-10-19 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cf38bbbe-cb99-3c9b-9734-b37d5b782136 | -9.1019 | -65.37431 | 2025-10-19 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1f91645-1408-3159-b7c6-974ba53edb11 | -9.96754 | -63.73228 | 2025-10-19 05:53:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d63fc6d5-582e-3be4-ac0e-30fa804b283d | -9.38301 | -68.32597 | 2025-10-19 05:53:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 381f49ed-14cd-3221-8114-caaba052e9df | -9.91463 | -64.08759 | 2025-10-19 05:53:00 | NPP-375D | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 715cf725-2d71-30d5-bc0b-70182bc4dc8a | -10.38384 | -61.25222 | 2025-10-19 05:53:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3af1a4e9-1bef-30d3-adba-1e89618d8c51 | -9.29508 | -64.22358 | 2025-10-19 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ffa4ab38-e599-364f-933e-f40295a8d1d6 | -9.90344 | -63.58347 | 2025-10-19 05:53:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b9f88e8-30d3-3764-ad8e-094546571a6c | -8.9743 | -61.97187 | 2025-10-19 05:53:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c072a2c6-be22-3adb-837f-8d3f3ac76535 | -7.88289 | -61.18258 | 2025-10-19 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5cee2b0e-6995-36ea-8c84-a4d0cf0f8acb | -9.55616 | -66.64915 | 2025-10-19 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1d6c5ec0-3687-3be0-8453-8bdd6b9322d5 | -9.75319 | -67.2563 | 2025-10-19 05:53:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 71b37bf2-ba88-3c24-9e09-7d5c86db2eed | -6.73738 | -63.06414 | 2025-10-19 05:53:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 70847862-21bd-3055-923d-6121eb7a0c77 | -9.73598 | -65.88613 | 2025-10-19 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 218c1763-7b1b-3274-8329-0ccb535a0e4b | -9.63779 | -65.2552 | 2025-10-19 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 242e055b-e2cc-3e6e-be81-243c36247393 | -9.268 | -62.4653 | 2025-10-19 05:53:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1731057a-4ccc-3950-b794-0b7c14a30b67 | -9.71844 | -67.47726 | 2025-10-19 05:53:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c03412fd-413c-37ac-9db7-4f4d5898d060 | -8.7292 | -67.05103 | 2025-10-19 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5e07d661-2f28-3e59-a1bc-50ca7888af11 | -6.52665 | -60.0298 | 2025-10-19 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c30caee4-a015-3e12-b3f1-b034eb5711cd | -8.22707 | -61.49189 | 2025-10-19 05:53:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ebce1a61-a5c3-3f10-b981-b12c781106cd | -6.64868 | -62.91128 | 2025-10-19 05:53:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c8b1b36b-c70d-3270-a244-9db20a9b42af | -9.72689 | -61.93121 | 2025-10-19 05:53:00 | NPP-375D | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 234a533a-fa1a-3b1e-8ec2-a68c12ac52a9 | -7.85886 | -61.59837 | 2025-10-19 05:53:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9af90716-f993-3088-9255-74470abcef8e | -9.18582 | -61.38614 | 2025-10-19 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 6221e308-e56c-3e34-af1f-c03fe1b53ab9 | -8.72199 | -67.05347 | 2025-10-19 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f0d0bde-6200-3950-a0a6-53db38f28683 | -10.18125 | -62.93065 | 2025-10-19 05:53:00 | NPP-375D | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1fd772e8-8d5d-329b-b873-942df28e8582 | -9.58613 | -63.50334 | 2025-10-19 05:53:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb85252d-b45f-333d-ab9c-e93135cf938b | -9.95576 | -66.77344 | 2025-10-19 05:53:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 584fc2d6-2ce1-36b0-99ad-6bee462c2b7f | -6.53054 | -60.03536 | 2025-10-19 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c59bd083-ca37-3b17-9c90-38469acbb00d | -6.65099 | -62.91364 | 2025-10-19 05:53:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab40a195-e4f4-36c2-8e7b-5d985bb9e8ef | -7.12479 | -63.04635 | 2025-10-19 05:53:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 66d8ed07-d56f-392c-af4e-fb2f9f654761 | -8.60499 | -64.08743 | 2025-10-19 05:53:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1881d0c8-02e5-31c2-851c-27b288a0471b | -4.97076 | -56.27351 | 2025-10-19 05:53:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 079aba56-be1c-36d8-aa6c-8c1513e221b5 | -9.95631 | -66.76987 | 2025-10-19 05:53:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README60.md)
