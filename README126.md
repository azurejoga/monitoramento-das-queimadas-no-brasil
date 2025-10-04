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

## Dados Diários - Página 126

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f5bdad8a-e79f-36be-938d-64ab45050675 | -3.85003 | -41.55939 | 2025-10-04 05:31:00 | AQUA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 36.1 |
| e61eb981-d195-3441-bc2f-432ae1b7ad49 | -8.11178 | -55.07848 | 2025-10-04 05:31:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3aced47d-9189-33aa-826e-18790c747cee | -6.93848 | -63.12494 | 2025-10-04 05:31:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a94be81-bcb0-3806-95e7-d51d8433d231 | -2.89234 | -50.72563 | 2025-10-04 05:31:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 36aac882-eec3-3d2e-966f-4055d0850bf7 | -2.90357 | -50.73175 | 2025-10-04 05:31:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2d6ce60d-9a2d-3907-ae2e-8f4f32851659 | -1.53909 | -60.10872 | 2025-10-04 05:31:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f763491-cd2f-3261-a218-ae6e866f87a4 | -3.82146 | -51.9142 | 2025-10-04 05:31:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 54b3cb94-e141-396c-87bd-e064d2895e39 | -3.39647 | -50.26958 | 2025-10-04 05:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 795f9d8d-8387-386b-b28b-c7254a1b1dc4 | -8.52345 | -50.03284 | 2025-10-04 05:31:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7beac576-82b2-3361-973d-44fb7ae27970 | -3.69319 | -50.89251 | 2025-10-04 05:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b08e8a3-1541-38df-80a4-70e232728509 | -4.55084 | -50.47512 | 2025-10-04 05:31:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e42b6755-ccdd-3f7d-8715-d2993db9ec30 | -2.69231 | -48.39692 | 2025-10-04 05:31:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1eb4096d-6afa-3431-88f0-c3ab73aecae1 | -8.04473 | -54.89726 | 2025-10-04 05:31:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e5210593-a244-3ac8-a5fe-228201f90739 | -7.75849 | -54.9637 | 2025-10-04 05:31:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c183ca8c-8c54-3b30-a2db-54db38b46391 | -2.69267 | -48.39625 | 2025-10-04 05:31:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 39d7fd85-a5e7-372f-a0bd-89df7b104f59 | -2.75116 | -54.59241 | 2025-10-04 05:31:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 085de5bf-2fb3-3242-a801-454ce6032d16 | -3.04966 | -51.09916 | 2025-10-04 05:31:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd7dacf9-e154-38b8-b25a-c20db8902477 | -6.2229 | -55.63847 | 2025-10-04 05:31:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 15aec094-32d7-3f27-82fa-0d769f2b2633 | -7.93456 | -55.02465 | 2025-10-04 05:31:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 00c1b06a-eca6-3d63-8a30-1b913a7b2074 | -2.69325 | -48.3908 | 2025-10-04 05:31:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7b63d7e-b90c-31e8-8f64-c940bbc07934 | -4.8942 | -49.96679 | 2025-10-04 05:31:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1125df5-bdf2-316d-81c6-3736b191fd46 | -2.6799 | -48.38797 | 2025-10-04 05:31:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f5260edf-2147-38dc-b991-fddd909a8120 | -3.68723 | -50.89175 | 2025-10-04 05:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 355f38c1-cf7d-3369-a539-60373343a446 | -8.107 | -55.07774 | 2025-10-04 05:31:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44ddfb31-76d3-3c4e-b045-753fab398074 | -4.89496 | -49.96155 | 2025-10-04 05:31:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1b5432fb-38eb-3caf-bf86-82b3349ae346 | -3.39578 | -50.27433 | 2025-10-04 05:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6241d7ab-3cdb-37a7-8c65-b36b2af2a5a6 | -6.8704 | -63.13245 | 2025-10-04 05:31:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9da9d86-12b9-3256-b1e3-d43522e8bc58 | -2.897 | -50.73513 | 2025-10-04 05:31:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 2c3d9f62-08ba-362d-aae0-c6763c3aaa43 | -8.10788 | -55.07662 | 2025-10-04 05:31:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4bb8ae0a-6c48-3fc8-b6b7-a9a0fdbd13ca | -7.29862 | -55.31963 | 2025-10-04 05:31:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d2037bea-5f00-3a94-83d0-66456ad51f6c | -2.89764 | -50.73084 | 2025-10-04 05:31:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 450bddd5-a655-33ce-be60-36a5f2c19fe2 | -2.8917 | -50.72993 | 2025-10-04 05:31:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c295b5af-f24c-3ef9-a739-d7c4967790fe | -5.68945 | -49.30589 | 2025-10-04 05:31:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2227d85d-9e46-32f0-94f1-b48a93a287c9 | -4.55702 | -50.47602 | 2025-10-04 05:31:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f75065fb-8235-3b57-8229-a8b6e08b8031 | -7.92977 | -55.02391 | 2025-10-04 05:31:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 610e726b-3173-3633-bfde-3ed9a40ba73f | -4.31116 | -48.08862 | 2025-10-04 05:31:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c7b91427-1724-3b0e-8c41-af3d740055ab | -5.69406 | -49.31039 | 2025-10-04 05:31:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bfd8c64f-16b4-32f3-9d79-7cab5421e065 | -2.90294 | -50.73603 | 2025-10-04 05:31:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 41294578-798f-3018-a5e9-9b3acdb05f6f | -6.94576 | -63.10083 | 2025-10-04 05:31:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c9c5a568-e053-314a-94f0-b59a9455092c | -2.68544 | -48.39614 | 2025-10-04 05:31:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 29e01af0-9319-3351-8a05-892426ed74b2 | -8.11037 | -55.08885 | 2025-10-04 05:31:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 86136c4c-7d94-3373-84ab-a8b9ba9c3da5 | -7.29397 | -55.31894 | 2025-10-04 05:31:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ffad5c66-bd1c-314f-8d22-327f1f1d3bc6 | -5.69618 | -49.30692 | 2025-10-04 05:31:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| df8af87b-52ae-395c-9d5d-209e1c8eaa5e | -2.89107 | -50.73423 | 2025-10-04 05:31:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 6fa61ed9-190e-33f9-a5c0-fe91c866713d | -6.86705 | -63.13191 | 2025-10-04 05:31:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3fbeccc5-6565-3c6c-b2d9-240c1bdaa1e0 | -5.6949 | -49.3044 | 2025-10-04 05:31:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 744901bb-72e4-33c2-ba76-b5e0d739e69d | -2.67861 | -48.39503 | 2025-10-04 05:31:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d3cddcf5-52fa-309e-bae0-bef9bb47368e | -2.68638 | -48.39 | 2025-10-04 05:31:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd1a8d21-1945-324c-985e-fb5d1ce8162b | -4.3152 | -48.08857 | 2025-10-04 05:31:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5c2b0007-8c3d-30ca-86fc-8c83cfd540e8 | -5.70163 | -49.30544 | 2025-10-04 05:31:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 52506937-7ab5-3e7e-af1a-aad13bf3cec9 | -3.11761 | -59.11428 | 2025-10-04 05:31:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 018b2036-afea-3b53-ad34-a2be7de5b518 | -3.04908 | -51.1031 | 2025-10-04 05:31:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9aa74e23-31a0-3e5e-8c85-2dd6da89317b | -3.86542 | -53.38434 | 2025-10-04 05:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c167c9c3-71bd-3f19-809b-95c170db39f5 | -2.69357 | -48.39009 | 2025-10-04 05:31:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5811e9dc-6c63-3838-a09d-d9302a12b261 | -2.67898 | -48.39425 | 2025-10-04 05:31:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c9304c1f-5277-3eb8-90e5-18ab2537cca4 | -3.865 | -53.38722 | 2025-10-04 05:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0d605cac-c9fc-3560-9349-7853415c050e | -7.91561 | -49.64273 | 2025-10-04 05:31:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0bfc062c-1098-364c-95b2-56c6332b32a0 | -4.31424 | -48.09545 | 2025-10-04 05:31:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ba1b6983-efa6-3b48-ad5b-1b6bef17709c | -4.31728 | -48.09641 | 2025-10-04 05:31:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a5e1fdf1-85db-3b6b-a86d-5705a208ed11 | -8.11107 | -55.08368 | 2025-10-04 05:31:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a4ee5d6d-56fa-30d7-859f-c81fa76a4bf9 | -3.7759 | -54.22927 | 2025-10-04 05:31:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b511f020-cd4d-3a0d-8cea-14ce2f75267c | -8.11117 | -55.08771 | 2025-10-04 05:31:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5833a00f-54d3-3b13-8c46-86214151ea78 | -5.69538 | -49.31289 | 2025-10-04 05:31:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4f94b1c9-b588-3b31-ad68-5a447b93c58c | -3.82703 | -51.91502 | 2025-10-04 05:31:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| add99ed8-3008-3c04-b774-1e4a947ba837 | -2.89827 | -50.72656 | 2025-10-04 05:31:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| da171164-c87a-3e99-9ad7-da368904df2d | -6.93904 | -63.12142 | 2025-10-04 05:31:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 593a444d-f4b2-352c-9076-8156dbda393d | -6.71646 | -42.81372 | 2025-10-04 05:33:00 | AQUA_M-M | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 14f250c8-074d-35ce-99a6-f195c047303d | -6.6665 | -42.82652 | 2025-10-04 05:33:00 | AQUA_M-M | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 5c7acc07-f1d7-3952-8906-a2f5dfa49ee5 | -6.35127 | -43.448 | 2025-10-04 05:33:00 | AQUA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7bd71944-7514-3c2b-804b-b6ad0a3e5910 | -9.32487 | -45.74147 | 2025-10-04 05:33:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 47e7e4e9-388c-3c8b-bf9f-1e2f076eb114 | -6.88346 | -44.49799 | 2025-10-04 05:33:00 | AQUA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| e594a411-d170-3568-8bbc-cf9877c7b0ac | -6.4608 | -44.58481 | 2025-10-04 05:33:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 648d26ee-9bdb-3cff-94bd-1de33140d5aa | -9.91017 | -43.79846 | 2025-10-04 05:33:00 | AQUA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 328764a6-fac8-35b2-8336-2d3de2412fdc | -6.24998 | -45.34563 | 2025-10-04 05:33:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 41.0 |
| 7928a139-4d57-3230-82b7-1b32386b84dc | -6.65593 | -42.79773 | 2025-10-04 05:33:00 | AQUA_M-M | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| c6a26c2e-eb30-3f18-bf30-f7b98b2bf64d | -7.70747 | -42.56538 | 2025-10-04 05:33:00 | AQUA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| eeaa7059-37de-339b-9cdb-8dc9d17d6305 | -6.36433 | -43.88663 | 2025-10-04 05:33:00 | AQUA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| b4739572-6b32-34e0-810e-bbe615d319f4 | -8.17437 | -44.12871 | 2025-10-04 05:33:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 9660b04d-7a47-3e76-89f7-a1f6c60b8f57 | -5.19927 | -45.06085 | 2025-10-04 05:33:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 56.6 |
| fa5f12b6-146b-3b2d-bd2d-a7ea37c26b32 | -6.34956 | -43.459 | 2025-10-04 05:33:00 | AQUA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 2f207f73-a5ce-3470-82e3-84a2ef99a3f1 | -5.68528 | -42.84831 | 2025-10-04 05:33:00 | AQUA_M-M | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 31.0 |
| 366efe37-5cd5-3341-98c9-18115e41306c | -7.54778 | -42.40127 | 2025-10-04 05:33:00 | AQUA_M-M | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 16.9 |
| 4b00a2b4-28d9-3e64-b699-6ebe0879c7d1 | -6.64591 | -41.9522 | 2025-10-04 05:33:00 | AQUA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| e6e4d4af-bed9-3905-9d9c-7b0c2d5876ab | -7.77631 | -42.60141 | 2025-10-04 05:33:00 | AQUA_M-M | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 2d0e0faa-e69f-3d50-ae3e-05dd290ae3c3 | -9.91054 | -43.73416 | 2025-10-04 05:33:00 | AQUA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| a56df601-2ab4-3989-8dac-29c6208c97a4 | -7.7778 | -42.59175 | 2025-10-04 05:33:00 | AQUA_M-M | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 670b6c5b-b783-39e8-a7bd-f8f5eb73a51f | -7.53868 | -42.39988 | 2025-10-04 05:33:00 | AQUA_M-M | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 82049485-381e-379f-97c3-e2cb9b1c4b8d | -5.95546 | -43.48735 | 2025-10-04 05:33:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 78e9661a-9bc1-382d-a32f-67aceb69d72c | -6.55831 | -44.15463 | 2025-10-04 05:33:00 | AQUA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 09f399c1-6592-3b97-9ed4-974d18e8735c | -5.73555 | -42.92668 | 2025-10-04 05:33:00 | AQUA_M-M | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| d9de69e8-d765-327a-970f-8d20c8b38782 | -7.04595 | -42.76636 | 2025-10-04 05:33:00 | AQUA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 15.5 |
| 90821ca2-7825-300a-8d68-fc0ba534bafc | -6.37254 | -43.90001 | 2025-10-04 05:33:00 | AQUA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| e8ef7906-caa7-3668-ac4b-85aa9b0773ee | -6.17271 | -43.92979 | 2025-10-04 05:33:00 | AQUA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 55dd2b86-cbfe-353c-9209-fc4c4a628e23 | -5.19765 | -45.06732 | 2025-10-04 05:33:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 50.5 |
| cc8e86ef-813d-314c-9679-2ab99c2f7aa3 | -4.83706 | -42.75999 | 2025-10-04 05:33:00 | AQUA_M-M | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 7483609e-7275-3b53-a656-b9aec9f506e3 | -6.87169 | -47.22628 | 2025-10-04 05:33:00 | AQUA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 55.7 |
| e281dfcc-5226-3a23-be91-be13dbaec39a | -5.80244 | -43.60905 | 2025-10-04 05:33:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 7fe1e380-68fd-3526-a4f9-d49c6351a2e9 | -4.83869 | -42.7496 | 2025-10-04 05:33:00 | AQUA_M-M | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| c3f0df97-1fa1-38f9-ab32-c4b6455e7fc8 | -6.28037 | -44.03729 | 2025-10-04 05:33:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 844c1248-0e49-3966-942f-021afa2c05c6 | -6.66067 | -42.82944 | 2025-10-04 05:33:00 | AQUA_M-M | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |


[Clique aqui para ver as próximas entradas](README127.md)
