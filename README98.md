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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f2939b7d-a3fc-3c9c-9cf0-5a11f9a41bd0 | -14.1456 | -52.8082 | 2026-08-31 15:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 7ecb84ef-1f96-3a76-a7ca-ccd45142cf24 | -9.196 | -64.4568 | 2026-08-31 15:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 88.2 |
| a1102bfa-a447-361d-b752-1173b4d41b3b | -6.9368 | -55.6161 | 2026-08-31 15:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| f4198356-7870-3621-8d5e-a76c57228a6b | -13.4324 | -51.776 | 2026-08-31 15:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 3af3a9c1-7273-3d86-933c-f4747c1d2b7b | -9.4342 | -45.6704 | 2026-08-31 15:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 128.3 |
| 4c21db49-afb3-3a04-854d-af70fb986238 | -14.4201 | -52.5201 | 2026-08-31 15:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 470.5 |
| 830dd348-7c90-3059-ba04-9857ebd1bc11 | -5.8967 | -59.9719 | 2026-08-31 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 848a1595-d04b-3fbb-94f5-0d343f8a790a | -5.2363 | -55.8914 | 2026-08-31 15:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 199e853b-a9f6-3987-8dca-9fedfefeb966 | -6.912 | -59.4927 | 2026-08-31 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.5 |
| e03c02ed-d0ff-3eea-98df-43e6d204c594 | -11.0933 | -51.5345 | 2026-08-31 15:00:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 111.5 |
| ba0d0c2d-08dd-3748-a280-afa63fef9381 | -9.6942 | -65.0582 | 2026-08-31 15:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 6b1d3e6f-63d2-347a-9f6d-780b27dc6689 | -15.2669 | -53.8851 | 2026-08-31 15:00:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 319.0 |
| cc37cd27-f9c1-3faf-bf85-f3559336582c | -6.1109 | -57.684 | 2026-08-31 15:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 252.8 |
| d470a80e-4cc5-3f14-94a0-cffcb8046ab2 | -10.9399 | -50.2979 | 2026-08-31 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| e34aa1b2-45e7-3643-8da5-35441760424b | -8.9481 | -62.3704 | 2026-08-31 15:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 61.3 |
| ab51e57c-5c9d-309f-90ae-a064ac0df9e6 | -6.9177 | -55.6967 | 2026-08-31 15:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 6ded8202-b1ed-37fb-bb7f-59e95c43d29d | -10.8209 | -50.6945 | 2026-08-31 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 93.2 |
| efa935e7-35b4-3473-89b0-5b7a4fcd46a1 | -11.0569 | -51.4328 | 2026-08-31 15:00:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 65.6 |
| c6fcdf92-7721-35dd-9f59-23e8ca4b3438 | -10.8046 | -50.5046 | 2026-08-31 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 3ece6a46-ecde-38dc-9f3c-bb65ac7df205 | -10.7457 | -50.6599 | 2026-08-31 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 09924361-8bec-3b99-9d75-5b26e9073a74 | -8.7631 | -46.4418 | 2026-08-31 15:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 218.4 |
| 7069b93b-8990-39a7-bfae-3fb99a297fe2 | -10.7409 | -54.0196 | 2026-08-31 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 65fa0abe-5c20-3292-a62e-25bdce00143e | -10.8444 | -45.3126 | 2026-08-31 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 129.9 |
| 1e6ccaf2-e08d-3097-a028-343895bff55e | -10.8463 | -50.2224 | 2026-08-31 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 95.4 |
| e44f9bae-f55f-379d-88c0-b4b28577e778 | -7.9907 | -46.5177 | 2026-08-31 15:00:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 136.4 |
| db21046f-8c3c-3407-99d5-a60ee1f7de33 | -8.799 | -62.4905 | 2026-08-31 15:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 121.7 |
| 6118c3db-6ba2-3571-839e-05861a284f1a | -11.172 | -51.3151 | 2026-08-31 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 67.2 |
| bd04a399-a659-315a-aeee-83ea3958f04f | -10.8043 | -50.5259 | 2026-08-31 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 706e39a4-de03-3128-9bc3-e67149cada7c | -11.8211 | -51.0322 | 2026-08-31 15:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 506582dc-dacb-39d3-811f-b6b6101e4eff | -12.0925 | -47.1587 | 2026-08-31 15:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 61b7b7a4-fab5-3f1e-8b4d-44b7ea3d9d80 | -6.2847 | -53.5792 | 2026-08-31 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| f0445f89-383c-3d14-a238-9541dbb8b640 | -7.0982 | -45.7689 | 2026-08-31 15:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 797302af-6531-3cc0-b365-95461d617659 | -11.0936 | -51.5134 | 2026-08-31 15:00:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 8e6aa2e7-4a4c-3d29-a2c5-2b7fb558a0aa | -15.2465 | -56.39 | 2026-08-31 15:00:00 | GOES-19 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 80.3 |
| bdc101b0-6293-3820-98b8-87e64ca24771 | -11.3615 | -45.1955 | 2026-08-31 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 123.8 |
| b454f76f-a72a-30a0-88e8-059d653c4cc0 | -6.1108 | -57.7035 | 2026-08-31 15:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| b14acd9e-15f9-3f08-ab9e-30a74f843267 | -7.9236 | -44.2558 | 2026-08-31 15:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 130.9 |
| 171bd3e6-c178-3481-b1e9-266b8f2c8c7d | -3.4167 | -43.3867 | 2026-08-31 15:00:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 88.0 |
| a1399afa-2a7b-3941-a638-e1926100410f | -11.1726 | -51.2728 | 2026-08-31 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 50.4 |
| b7d9ad05-7e5c-37fe-a677-e981a3d9685e | -13.4707 | -57.0574 | 2026-08-31 15:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 34e4ee54-83bb-35b8-b712-c5454ac6dba5 | -11.6247 | -50.1783 | 2026-08-31 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| dedb8b28-f34b-3746-9d5c-634ca29777a1 | -6.49184 | -35.13702 | 2026-08-31 15:09:00 | NOAA-20 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| beccfbf2-c17c-3a18-afe9-d8535a1282e3 | -15.2081 | -56.3738 | 2026-08-31 15:10:00 | GOES-19 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 2884a319-dfc5-3dc4-b220-651665cd0389 | -6.9367 | -55.636 | 2026-08-31 15:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 107.7 |
| c5d55ede-594b-3cab-b1a7-f6ca08db6612 | -3.6215 | -60.566 | 2026-08-31 15:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 176.4 |
| 0679359d-d31c-30d1-bb02-37d8d3727ad1 | -12.9032 | -45.8382 | 2026-08-31 15:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 166.1 |
| f78ba0eb-88e5-3224-91f2-32fed8a74618 | -14.1456 | -52.8082 | 2026-08-31 15:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 37d1b4cd-4308-3a4e-9e71-9e00d9f42863 | -5.2362 | -55.9112 | 2026-08-31 15:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 116.4 |
| 4f648eb7-7053-3257-9e69-8bece6d70793 | -9.5967 | -47.5983 | 2026-08-31 15:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 143.0 |
| 0808c81c-a76e-325a-adb3-35bcd091c71f | -14.1459 | -52.7871 | 2026-08-31 15:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 2f65656e-0133-3ee8-82a0-748f0e0c5b7c | -9.1906 | -51.546 | 2026-08-31 15:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 2c2bfc46-59ac-3f43-b396-6e10c59d0176 | -10.7405 | -54.0606 | 2026-08-31 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 11c2f65d-4aa2-3f3f-aa12-19c52f594489 | -10.1321 | -45.8825 | 2026-08-31 15:10:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 812ba883-1c79-35c3-a6b7-07f4a720f16e | -10.7428 | -50.8727 | 2026-08-31 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 236e274c-2283-3c09-8e59-cb8050751812 | -10.7409 | -54.0196 | 2026-08-31 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 683add45-0123-3499-95fc-598712f85b26 | -11.6975 | -54.5467 | 2026-08-31 15:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 2f371385-39d4-3399-99ab-20124c1fd683 | -11.3806 | -45.1928 | 2026-08-31 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 6772d71f-13c6-397b-97c5-0376b619174d | -5.9636 | -57.6704 | 2026-08-31 15:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| a6a3df30-873e-3986-a0b4-10af1979999f | -11.0744 | -51.5365 | 2026-08-31 15:10:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 96.8 |
| b2e586bc-99c6-3518-af07-aac2dab57f77 | -12.9221 | -45.8582 | 2026-08-31 15:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 165.5 |
| 4d897937-1c61-3121-bec2-af4b70211ef6 | -6.2471 | -53.6623 | 2026-08-31 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| b90239db-6aa0-344d-999c-65c85cc0bfe0 | -6.912 | -59.4927 | 2026-08-31 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 6b171354-2006-3307-a44c-a4f8920687e4 | -11.6786 | -54.5484 | 2026-08-31 15:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 165.5 |
| 36717184-dd8b-31fd-a5dc-19024683639c | -15.6336 | -56.3876 | 2026-08-31 15:10:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 267.5 |
| cc7727cd-9f1d-395b-bb75-ce6e4b046e47 | -10.8444 | -45.3126 | 2026-08-31 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 07bf3e23-7602-3e4a-86a1-da43695b9eac | -18.2899 | -52.7035 | 2026-08-31 15:10:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 7d29034a-c035-3cac-942c-5cee38403f6c | -10.7407 | -54.0401 | 2026-08-31 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 243.0 |
| 4fa3e788-7105-3746-b85e-7c30a776e9ab | -8.1858 | -54.9234 | 2026-08-31 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 3a3b670f-7c3d-3795-a179-3f8f166cd14b | -10.8807 | -50.4751 | 2026-08-31 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |
| ad5b0259-6df5-3f29-a4a3-5d9b1efe0bf9 | -15.2275 | -56.3716 | 2026-08-31 15:10:00 | GOES-19 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 75e21f2b-8586-3775-8c48-4fd5eb8177e0 | -11.1726 | -51.2728 | 2026-08-31 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 509e95aa-1996-36d9-8003-0cc93282d774 | -10.8425 | -50.5005 | 2026-08-31 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 988d6600-dff4-3e99-ae2c-f8bf5b4f5ef8 | -11.0247 | -49.6656 | 2026-08-31 15:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 46.1 |
| cbf52598-8c8a-30a3-a3a8-71febad8ae71 | -12.9054 | -59.8857 | 2026-08-31 15:10:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 6525920b-69b6-318d-8ad7-84d4190f6810 | -7.5649 | -44.3376 | 2026-08-31 15:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 71e8cda8-99e1-3bc2-ac20-b392ded7cfca | -11.1349 | -49.9117 | 2026-08-31 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| d358de63-cf40-36d7-bef7-cf5b06b1a55d | -10.3391 | -49.9762 | 2026-08-31 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 681b100d-fc23-38ce-8249-9e5a19fff8be | -9.173 | -59.3659 | 2026-08-31 15:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 556bc0ed-e0f4-3992-8986-a7d9d51f7670 | -8.6156 | -54.7743 | 2026-08-31 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 11490746-47ce-30bd-b294-764d80a2f985 | -13.8371 | -54.0989 | 2026-08-31 15:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 149.8 |
| c12f49bc-0383-3750-a543-e6d9bdbf34bf | -13.9667 | -54.4157 | 2026-08-31 15:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 152.3 |
| f0af6e33-4c31-3095-baeb-0e03ae6af2d9 | -14.2792 | -52.8758 | 2026-08-31 15:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 192.4 |
| 556b5b0c-c88b-35b2-978c-a5bd7123212f | -3.6398 | -60.5656 | 2026-08-31 15:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 0577cdd9-8763-3a78-8349-8b336b228a52 | 0.1914 | -60.5067 | 2026-08-31 15:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 69.0 |
| a6323975-5275-3060-b2f9-d5d71cfeff88 | -11.3615 | -45.1955 | 2026-08-31 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 127.6 |
| 5e4413e9-cdb0-35f6-9020-ac7a1e586f00 | -14.5868 | -54.1153 | 2026-08-31 15:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 237.5 |
| b2789877-7574-3db3-b2f3-a672128a0e72 | -11.2103 | -45.1017 | 2026-08-31 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 90da51d7-f6b8-3e7e-b3ec-69074c8b6ea9 | -13.9474 | -54.4179 | 2026-08-31 15:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 129.4 |
| 0e4e61ad-ccea-3440-84ae-ca9e2d2bb192 | -6.2847 | -53.5792 | 2026-08-31 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 50addcf4-5af2-3aa9-a492-edf9e9e834c9 | -10.8617 | -50.4772 | 2026-08-31 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 2c1a4073-a1e2-3507-8ede-200b6f35aa2d | -8.5602 | -54.7175 | 2026-08-31 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 9e900530-f5c4-3878-b085-3d43e7fb7321 | -10.7593 | -54.0589 | 2026-08-31 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 2d01572c-fbcf-352d-81ab-87347f3aab57 | 0.1914 | -60.4878 | 2026-08-31 15:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 60.8 |
| c6116c4e-8f1d-325b-ad51-65dcef9d1433 | -14.2599 | -52.8782 | 2026-08-31 15:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 117.4 |
| ed0591f4-c64a-30a3-8b42-c670a8855faf | -11.5479 | -45.4676 | 2026-08-31 15:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 018f896f-f986-3fbe-9faa-acaedcb9ec84 | -10.5601 | -50.4022 | 2026-08-31 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| afa1fcc1-4f94-3e5d-bbc5-8dc7c4d8afec | -10.918 | -50.5138 | 2026-08-31 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 51dc6f34-42b7-36d9-aa6e-31c9ab16429b | -6.2469 | -53.6826 | 2026-08-31 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 95.0 |
| b4936545-9c47-3d3f-a7e7-63dacd5001a7 | -9.5964 | -47.6204 | 2026-08-31 15:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 227.0 |
| 388ff51b-1b96-32ff-bd45-28bd82d727ee | -9.6942 | -65.0582 | 2026-08-31 15:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 49.0 |


[Clique aqui para ver as próximas entradas](README99.md)
