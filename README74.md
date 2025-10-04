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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e8bb1394-1b3b-3664-b3cd-aef4ad3eda85 | -10.80334 | -48.8202 | 2025-10-04 04:14:00 | NOAA-20 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 8d5d0e1b-675b-37c4-99b5-d5029e3492eb | -11.47027 | -45.13878 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f89dfb07-5ec3-3db2-a2c9-50e7afe7f812 | -9.92564 | -50.89731 | 2025-10-04 04:14:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 414e6f2c-7d0d-3ef4-bed5-0b00eab8581c | -13.51991 | -47.28016 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5dc8c674-a969-3009-9114-c0c99ce8542a | -14.68206 | -45.17791 | 2025-10-04 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c3269010-a3f5-3e45-94cd-3ea50eb29607 | -15.7829 | -42.04683 | 2025-10-04 04:14:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5d1b4862-5514-3013-9705-8b0e0ef4f231 | -10.76464 | -46.59951 | 2025-10-04 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 899f60d3-8009-3208-9ed1-f6257a8b2d94 | -12.37933 | -54.4697 | 2025-10-04 04:14:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6c27e49d-cbec-30a7-ab60-9567b93765b9 | -11.42952 | -43.48912 | 2025-10-04 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dddfdd8f-6f80-3f91-a823-ba20e0df53a0 | -7.76677 | -46.22918 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 4ea3b04a-cfe1-3c5d-a5f1-f096b2b12601 | -13.78094 | -47.81603 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4c92bece-ea7a-3609-9027-6bfc1bc0a571 | -11.49982 | -45.01939 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ef1394b-ec85-3841-9824-1d4b505992df | -9.63251 | -54.3154 | 2025-10-04 04:14:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eaff2dd2-b231-3e6a-b590-83eedbb9ff67 | -12.2776 | -55.13905 | 2025-10-04 04:14:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20f72776-3e16-39aa-8490-963ff3d74509 | -11.86807 | -44.97095 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f1c68db8-51b0-3520-be32-8e04c4d6291e | -7.7374 | -46.27407 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 344e15d6-341f-3d2d-b32c-5db09ef3f5e1 | -10.5196 | -50.8451 | 2025-10-04 04:14:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0a10733c-a781-37cb-86f8-b5c1551df554 | -8.83304 | -46.76778 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e57a89d1-4b6f-31b7-8377-f468673588e7 | -7.77125 | -46.24666 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a9449ee6-c7c4-34bd-b1db-79dad29206f9 | -12.59414 | -47.00466 | 2025-10-04 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 380182e3-a7f4-3796-b3f9-1dca43dfb6bc | -12.72497 | -48.57386 | 2025-10-04 04:14:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 94e3af44-11f1-3c43-987f-d13c930fb542 | -11.90989 | -46.24769 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 28a93baf-c867-3eb8-b264-647797f31850 | -8.61978 | -55.00295 | 2025-10-04 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 77736c0b-225e-3b0a-b373-034703859773 | -9.94326 | -43.74323 | 2025-10-04 04:14:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 82bbb638-f371-3bfe-ad9f-e14acad47444 | -14.45699 | -48.40342 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5f661565-24fd-3cc7-bf65-f3cf39e0cda2 | -10.89005 | -53.75132 | 2025-10-04 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b4a3247f-512a-3997-9777-605ce9ad4bf0 | -14.22674 | -46.0881 | 2025-10-04 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 72289ab0-e6de-3444-8e96-52913de5520c | -12.2977 | -55.12947 | 2025-10-04 04:14:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9ede68fc-d816-30fc-a6f4-7d44ebd39fa5 | -11.96599 | -51.48207 | 2025-10-04 04:14:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| be0f2c6e-43fd-3baf-bd22-3deeeb595342 | -9.93632 | -50.23848 | 2025-10-04 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a89a9635-41af-3bea-9952-3d0493b42dcd | -13.98434 | -48.11816 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bb126f89-d489-3dea-b9ee-680f86105599 | -7.76901 | -46.2379 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c3e809cf-f6bd-39a3-86d1-d020d1ddda1a | -8.70841 | -47.97914 | 2025-10-04 04:14:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3381e554-fe96-3fee-9991-a4165bddb260 | -14.60003 | -46.7256 | 2025-10-04 04:14:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cba932e4-0f07-359c-9eca-4b776a558640 | -8.5335 | -47.21147 | 2025-10-04 04:14:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 97f68ee8-4127-316a-b857-1541a2990d1f | -13.12617 | -47.8259 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 27c5afe1-d8b2-3d17-a877-5c31da98848e | -10.34282 | -48.1727 | 2025-10-04 04:14:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 3a948de3-bba9-3555-bd75-02d124e51321 | -13.33169 | -47.62554 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9f6bda1b-3ef3-3028-9da6-0239f60100eb | -10.31518 | -50.34881 | 2025-10-04 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3fa1b5fc-9a9f-3e23-adc8-61c922be3499 | -11.67045 | -44.26968 | 2025-10-04 04:14:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7dbf35f7-49c0-301b-a578-6414351e4152 | -12.30181 | -55.13913 | 2025-10-04 04:14:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1bf210e6-6c4e-3dd4-ae2b-ff69edc938b7 | -7.74274 | -46.30867 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 8a962a3a-bf80-3eee-b5cb-f8327e449ff4 | -12.64636 | -46.97264 | 2025-10-04 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 61f58e0d-bf01-3a8a-b8a8-9997dca74618 | -12.41168 | -45.16268 | 2025-10-04 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9faba85a-c2ac-3fd9-a0c6-53831810a854 | -9.95314 | -43.65906 | 2025-10-04 04:14:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 562f87b4-07be-3c07-8d1b-d62b1d45f4b0 | -11.50213 | -45.00507 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1492c455-f7b7-3b29-9ee0-dccf68cff9e0 | -9.93711 | -50.23415 | 2025-10-04 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 16af1b8b-dcf4-340c-98cb-cc74c7c6e56c | -12.93612 | -46.38707 | 2025-10-04 04:14:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 436b6805-003e-364f-8427-aef17ba08a1f | -12.79102 | -56.96225 | 2025-10-04 04:14:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| db7196e2-7ab4-31f3-afda-70a172acc992 | -11.8006 | -48.91939 | 2025-10-04 04:14:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f042f2bb-6bd3-3649-82a1-6abf29963831 | -13.13628 | -47.81032 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c408fd28-24b6-3fbf-bef6-83e879b5a470 | -8.76036 | -49.90845 | 2025-10-04 04:14:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82f79b11-781d-3352-94c2-d16e44cd7a7e | -14.71865 | -50.03499 | 2025-10-04 04:14:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 94abae83-58fe-31c1-b493-7a276c264e17 | -11.85608 | -45.04573 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 19cc3fa5-0d52-34af-b42d-1d2ac292dfc6 | -13.32886 | -47.62037 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e8a96e28-2d63-377f-a94a-6e38defbc079 | -15.18848 | -46.39454 | 2025-10-04 04:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e29287d8-ce2d-3264-b51d-cbbd1ee83e20 | -11.61752 | -45.02802 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 833e7f6b-7744-3aad-8785-c5aedf8c9657 | -11.86038 | -44.95509 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2351270d-3929-3aac-ac65-139374ee7d75 | -11.67982 | -44.27481 | 2025-10-04 04:14:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eb6c1042-b621-359f-bb36-651a58ec88a4 | -12.47192 | -54.43024 | 2025-10-04 04:14:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a2424dfc-f1ac-3445-a1f8-21336addfba8 | -14.92096 | -46.88518 | 2025-10-04 04:14:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 24038b16-6ce1-3704-8231-2cf44b55bb54 | -13.47753 | -47.22942 | 2025-10-04 04:14:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ec7ebe88-a2fc-35bf-bdd1-d29255bc0b8d | -8.83922 | -46.84241 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cc355111-bfbb-342a-b631-8a02f1eb1909 | -10.88868 | -53.75857 | 2025-10-04 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f4f05b46-5669-3df5-9e64-cb7e9693186e | -11.2428 | -47.79835 | 2025-10-04 04:14:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f2ee80ae-98bb-3c45-bf72-e94b38fe6537 | -9.93915 | -50.248 | 2025-10-04 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 56e054a2-64ad-3ddd-afdf-3a11e5d7b402 | -14.66265 | -48.29924 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 6b93500f-b1e0-390b-8762-49244b0e3b17 | -13.70186 | -47.34179 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ae3e9e11-a038-354d-b7a2-38bb8308030a | -9.37385 | -45.85999 | 2025-10-04 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 59ac217d-3cb9-3edc-a6b1-f62bbd6ec7de | -13.74425 | -48.05217 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2b384e25-5bd3-3d95-8f81-3b66e03aa666 | -11.80124 | -45.02565 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c39032d8-2515-3011-9034-6d8d0958ebab | -11.80893 | -45.04154 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8d15547d-16f7-393a-9b94-f54c52072c70 | -9.34803 | -45.80081 | 2025-10-04 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e69c8deb-e497-32d1-bc3d-cdd039d4b72f | -14.3881 | -45.94656 | 2025-10-04 04:14:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 71b5012e-d87e-3002-a82c-bd23380d2aab | -8.62659 | -54.9958 | 2025-10-04 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 41f32648-7e4f-3e05-98ba-b0ebbfc6c421 | -11.62121 | -45.06878 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 71999396-3a4c-3705-a135-972865494334 | -13.32019 | -48.11823 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ef39e115-e170-313a-80fe-9abd770bf00f | -13.31385 | -47.80577 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d6f9dcab-98c5-3b4e-8e71-3c6b8559904e | -13.761 | -47.52871 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 92485de6-b644-3f31-b084-9df60eadcc7e | -15.30549 | -46.28231 | 2025-10-04 04:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e8963b60-9c77-31dc-b56f-cd928841caa9 | -15.36033 | -46.28424 | 2025-10-04 04:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3c5716d9-9452-354b-99f5-f34c1969a811 | -12.89003 | -47.16419 | 2025-10-04 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7433896b-8074-33c5-b2ff-1a33898caa11 | -14.74925 | -48.14251 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 878e0b7d-62c8-389e-879a-272d6e537389 | -13.7661 | -48.05576 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d2718d51-b8ad-3f8b-b9d8-b7c99aa9c054 | -13.48614 | -47.24273 | 2025-10-04 04:14:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 76120149-3bd6-3427-b23e-841ebee41548 | -9.66592 | -48.22251 | 2025-10-04 04:14:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 808ce70b-f31d-357f-85f8-509664fcd632 | -11.91968 | -46.35518 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1ac9fa1e-28ea-35d3-ad03-8bb17b885904 | -13.62521 | -48.67365 | 2025-10-04 04:14:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6d02ad6b-5c6a-316b-b73d-386165d74013 | -12.03915 | -45.196 | 2025-10-04 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1c258db0-d3fd-38ec-a8ca-82adcb7e18a2 | -11.82496 | -48.06829 | 2025-10-04 04:14:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 27072756-b56a-37ca-b8af-09f7093d3002 | -12.92936 | -45.06955 | 2025-10-04 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9f4ecc8c-9c4b-3aba-9e48-f3988b146c6f | -8.84751 | -46.77021 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 371163bf-6c79-345b-bdb9-6520b0200600 | -11.13191 | -47.85503 | 2025-10-04 04:14:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d6d8402d-24d7-3232-8d78-3d7b1bb2942c | -11.14791 | -43.37881 | 2025-10-04 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a437c518-b188-3e03-89dc-1a5f12232bad | -10.61169 | -49.15516 | 2025-10-04 04:14:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2cbdf093-7d55-37bd-a736-d01da824e403 | -15.19583 | -46.39192 | 2025-10-04 04:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9f827d37-e07b-35d0-be6f-f4f20024ee00 | -12.93446 | -50.98212 | 2025-10-04 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5b275255-9048-3e46-8ea5-2c00341d2717 | -12.81451 | -46.86097 | 2025-10-04 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a0167a07-b1cc-3d34-a0cd-b4e505de8e47 | -11.22653 | -50.79391 | 2025-10-04 04:14:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e710414e-7bfd-3bc9-845c-1919bc642e6e | -10.58612 | -48.72461 | 2025-10-04 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README75.md)
