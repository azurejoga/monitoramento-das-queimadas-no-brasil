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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c400f7f0-514d-3b5b-ba1d-595d1e1b2ef3 | -4.2951 | -49.1234 | 2026-09-26 02:20:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 35e037ad-3b84-3441-8a56-1b90aa3605ca | -4.295 | -49.1448 | 2026-09-26 02:20:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 2136d07c-4201-348a-87fd-629dfd28240f | -5.7754 | -45.1053 | 2026-09-26 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 51.3 |
| fa9ed744-89d2-317e-9953-cc1e4355aaa8 | -4.3137 | -49.1226 | 2026-09-26 02:20:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 9b24e6d6-cef6-3fa8-9d52-190bb9a2d0c0 | -12.0362 | -50.6448 | 2026-09-26 02:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 98.4 |
| a1b60bd1-4c46-3ce4-a4a3-735646fbfd58 | -1.8421 | -54.7113 | 2026-09-26 02:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 10b4e952-c09c-30c6-980b-ffb8a186e830 | -12.0171 | -50.647 | 2026-09-26 02:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 53.9 |
| f2f7cb2d-affc-3369-b06e-83ab5ec79d09 | -11.904 | -50.5746 | 2026-09-26 02:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 26de55bb-c993-3ff3-a664-f72e35274696 | -5.7756 | -45.0826 | 2026-09-26 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 5d641bda-64c7-3656-9776-70f5ced4490b | -3.2728 | -50.1372 | 2026-09-26 02:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 101.6 |
| 31ebc399-56e9-346e-9c38-9b4e6b22d66e | -15.2314 | -43.2784 | 2026-09-26 02:30:00 | GOES-19 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 69.5 |
| c4ccfef2-ad14-3f8d-90da-d534a3f6d984 | -11.9231 | -50.5724 | 2026-09-26 02:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 61.2 |
| cd66244c-f754-3e69-a889-5f5c7ca2116f | -4.2951 | -49.1234 | 2026-09-26 02:30:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 41054d30-b608-3808-8445-061bddfe7ac5 | -5.7756 | -45.0826 | 2026-09-26 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 6e5602aa-a11f-391f-a9f6-a76cdb23446a | -11.9228 | -50.5938 | 2026-09-26 02:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 55.7 |
| f43946e8-469c-395a-ab79-5fd7c2c002dd | -11.904 | -50.5746 | 2026-09-26 02:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 1b573f3b-9613-3ea6-8e39-e52b73fc5778 | -4.3137 | -49.1226 | 2026-09-26 02:30:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 45aa1655-7b78-3cfc-bd24-3064d49da38e | -12.9457 | -51.0695 | 2026-09-26 02:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 3d4244d7-82d1-3e12-bdd2-6371f9c7291a | -15.2511 | -43.2743 | 2026-09-26 02:30:00 | GOES-19 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 68.1 |
| 3f6bad43-0f28-3eee-be7c-b15a3cd1632c | -4.295 | -49.1448 | 2026-09-26 02:30:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| f7d52210-2ce4-3424-a89e-a378492323d6 | -5.7384 | -45.0626 | 2026-09-26 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 1394b6ee-cf60-322c-815b-42531eaf074c | -3.2727 | -50.1583 | 2026-09-26 02:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 05576986-f836-3fed-8936-9d635b437a3f | -5.7382 | -45.0853 | 2026-09-26 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 64.4 |
| e2b8e3ca-8eb0-3078-bf3f-8478593579ce | -15.2314 | -43.2784 | 2026-09-26 02:40:00 | GOES-19 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 94.7 |
| 0dc4207a-4daa-3595-af60-a626742433f9 | -11.9231 | -50.5724 | 2026-09-26 02:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 04c6c436-cb30-3e50-b608-80080ba71e9f | -5.7384 | -45.0626 | 2026-09-26 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 140.0 |
| 08f56535-7e1a-33d1-8870-15737cacaa82 | -5.7756 | -45.0826 | 2026-09-26 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 03877553-f5df-3aae-8246-781687b5e2de | -11.9228 | -50.5938 | 2026-09-26 02:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 54.5 |
| bdbecb1b-9155-3de8-ba3c-559e23c6f08f | -15.2511 | -43.2743 | 2026-09-26 02:40:00 | GOES-19 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 103.3 |
| 4a6a41f9-4c00-3156-b96d-a2b043b6fb6a | -3.2728 | -50.1372 | 2026-09-26 02:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| ee2e0374-dab1-3672-953b-3e0de4e51e66 | -5.7754 | -45.1053 | 2026-09-26 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| a0197b92-c74b-36e5-8fab-be15c8e160fe | -15.2517 | -43.2501 | 2026-09-26 02:40:00 | GOES-19 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 69.8 |
| 49e131d6-708f-30b2-b05a-95798f18c7f2 | -5.7571 | -45.0613 | 2026-09-26 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 56.1 |
| ec644031-5897-38bd-9ac9-aefa5da59329 | -5.7756 | -45.0826 | 2026-09-26 02:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 91.1 |
| ad175a91-5464-3d7c-ac2a-65e3809d87a9 | -5.7571 | -45.0613 | 2026-09-26 02:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 727a1913-5a5f-3154-861b-f5371abeadad | -5.7754 | -45.1053 | 2026-09-26 02:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 0c2a6767-346d-36b6-ae34-51bdbea8502a | -3.2728 | -50.1372 | 2026-09-26 02:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| ce592fcf-cf4b-37f5-9442-1d5d035ed5d3 | -15.2511 | -43.2743 | 2026-09-26 02:50:00 | GOES-19 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 61.2 |
| e83961ea-cec3-3e0d-96ec-a0332ce38c03 | -15.2314 | -43.2784 | 2026-09-26 02:50:00 | GOES-19 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 60.6 |
| bdf350ab-5b6c-3268-97dc-1d25c6312794 | -5.7382 | -45.0853 | 2026-09-26 02:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 664aa63e-3e44-31da-b4f9-c3471c75327d | -5.7384 | -45.0626 | 2026-09-26 02:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 128.2 |
| 5a01caf0-c5fa-3dd1-b983-6dc9ab19cfe9 | -12.9457 | -51.0695 | 2026-09-26 02:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 4ce3776b-3ed9-338a-8a2d-693fb86378d3 | -5.7384 | -45.0626 | 2026-09-26 03:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 133.1 |
| 35bffec7-6cbb-3fc4-8c70-954e1c3245b6 | -5.7571 | -45.0613 | 2026-09-26 03:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 32ef4b3d-0d1f-3ca3-a302-7b70b062408a | -3.2728 | -50.1372 | 2026-09-26 03:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| ee29535b-3e4f-3648-90d2-90831caebd61 | -11.9231 | -50.5724 | 2026-09-26 03:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 819fae7c-0437-345e-871e-648ec806ef77 | -5.7382 | -45.0853 | 2026-09-26 03:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 9eb90a6a-7945-32c0-a26c-efa6cfb52686 | -5.7756 | -45.0826 | 2026-09-26 03:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 85.7 |
| a493a78d-4c00-3e53-bfba-61cf9f939ea4 | -5.7754 | -45.1053 | 2026-09-26 03:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 9a71bc55-dd1b-3015-ae80-2271741606cd | -12.9461 | -51.0481 | 2026-09-26 03:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 88bfdb35-a68d-33fb-afac-ce52e5b26b46 | -3.2728 | -50.1372 | 2026-09-26 03:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| ce9483c6-3ae9-3237-a9d6-45bb5eba397f | -11.9228 | -50.5938 | 2026-09-26 03:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 51.0 |
| fcd731b4-af6a-385f-a097-b9aa66c04939 | -5.7571 | -45.0613 | 2026-09-26 03:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| f80bccc2-f11b-3c78-8460-91b981eeb6a2 | -15.232 | -43.2541 | 2026-09-26 03:10:00 | GOES-19 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 63.2 |
| 0ce8e4d0-82cc-30d5-80ac-809b757742b3 | -5.7384 | -45.0626 | 2026-09-26 03:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 1763b8b8-b196-34cf-bce6-5b1e6d07bcdc | -11.9231 | -50.5724 | 2026-09-26 03:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 5ee05a51-3423-3b52-ac87-f7514382627e | -5.7756 | -45.0826 | 2026-09-26 03:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 29f4e35b-2cef-3f27-aa95-7603abcef93c | -5.7754 | -45.1053 | 2026-09-26 03:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 081ee20d-8643-3fad-9089-faef31923495 | -12.9457 | -51.0695 | 2026-09-26 03:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 106.4 |
| b1c8df7c-340b-3287-a397-ee1db5138270 | -5.7357 | -43.2682 | 2026-09-26 03:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 063a218d-1cc1-380a-9a16-c2537e1e0d0f | -5.7382 | -45.0853 | 2026-09-26 03:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 57.2 |
| a915dcf9-b200-3671-93fb-264c6581966e | -15.2314 | -43.2784 | 2026-09-26 03:10:00 | GOES-19 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 85.2 |
| cdf632c6-5f0a-3c9d-8ea7-2d1cd833c81f | -9.4773 | -40.3116 | 2026-09-26 03:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 88.3 |
| 2da753bf-13cb-3875-ae8c-eb81385a8b7a | -5.7382 | -45.0853 | 2026-09-26 03:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 1e463c98-f1ab-35af-bebe-67b56a9a63cc | -9.4769 | -40.3365 | 2026-09-26 03:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 147.5 |
| 608fafbb-ddbd-3f20-9f80-967106cec38a | -12.9461 | -51.0481 | 2026-09-26 03:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 120.1 |
| b96ed5d8-3e77-317b-b367-b34a2fd0cd69 | -5.7357 | -43.2682 | 2026-09-26 03:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 54.0 |
| ac7b3d94-9896-3a5e-8d01-71d12ef1e44b | -9.4578 | -40.3392 | 2026-09-26 03:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 105.1 |
| 0af7c87e-e087-3c3d-bcf5-afd5065135b9 | -11.9228 | -50.5938 | 2026-09-26 03:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 6965c779-6d69-39dd-aa35-79d2bceb67c2 | -11.9231 | -50.5724 | 2026-09-26 03:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 06fb12a7-881d-3357-8f47-612640f6c0a7 | -3.2728 | -50.1372 | 2026-09-26 03:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| dd140193-7c21-3373-8076-3951b0108b9c | -12.9457 | -51.0695 | 2026-09-26 03:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 151.6 |
| 42422494-2a6c-30c7-ad7a-bcf0658737cb | -11.904 | -50.5746 | 2026-09-26 03:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 96407d74-0a00-3c7b-a87d-7a9cd9490f26 | -5.7384 | -45.0626 | 2026-09-26 03:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 39b5b7b5-0dba-3310-86a0-ea15b30983bf | -9.4773 | -40.3116 | 2026-09-26 03:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 118.5 |
| 91427f1d-cfc3-3df7-8c22-3b70a202c62a | -11.8662 | -50.5576 | 2026-09-26 03:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 8db8e718-9bc3-3bc4-8a52-914ad6be9fd6 | -9.4582 | -40.3143 | 2026-09-26 03:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 90.3 |
| cdd7fa44-d125-393b-81fe-ee3f3cb83c9a | -9.4578 | -40.3392 | 2026-09-26 03:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 191.8 |
| 2e6e0008-7904-3ff3-90bb-44c4f2fe6e66 | -12.9457 | -51.0695 | 2026-09-26 03:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 106.5 |
| c250f3ef-0871-3949-bd50-b4082042576a | -5.7384 | -45.0626 | 2026-09-26 03:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 462b0ddd-1c05-3b5a-8ece-43e2cd297337 | -9.4769 | -40.3365 | 2026-09-26 03:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 259.4 |
| 2aeb133a-2769-3825-b4a3-c2359c4667ad | -5.73236 | -45.07055 | 2026-09-26 03:30:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| c64a49a3-7f72-3142-971d-13a003fd05ec | -7.10471 | -35.11518 | 2026-09-26 03:30:00 | NOAA-21 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f3f4e619-d4ad-398e-9075-49b0106f2c00 | -7.27724 | -43.29168 | 2026-09-26 03:30:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c86f0269-7a4b-37ab-af76-6be5cb4a6437 | -5.77649 | -45.097 | 2026-09-26 03:30:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| cb253122-1f01-3154-9ebb-9b5d8d4e7891 | -4.60429 | -44.65401 | 2026-09-26 03:30:00 | NOAA-21 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1d1867b2-d4bc-360f-9674-e6e75b76c015 | -3.42306 | -40.03688 | 2026-09-26 03:30:00 | NOAA-21 | SANTANA DO ACARAÚ | CEARÁ | Brasil | 2312007 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 07171d55-07aa-328b-9450-1e059eba1cbb | -5.77835 | -45.09823 | 2026-09-26 03:30:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 5cf5cf08-f138-3ce0-bcee-ddef84c75767 | -5.52207 | -39.86484 | 2026-09-26 03:30:00 | NOAA-21 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b4807c76-1f6a-31a9-b5c3-c1c0f0147351 | -4.37601 | -42.98866 | 2026-09-26 03:30:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2960096d-09d1-3e27-8667-cdbe243bc213 | -5.74584 | -45.07326 | 2026-09-26 03:30:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 2c5f34ed-03bc-3290-94f5-cb4efdd94af6 | -5.77717 | -45.10458 | 2026-09-26 03:30:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 7c9ca576-a1ba-329e-9037-0537c65d28b1 | -5.73468 | -45.05781 | 2026-09-26 03:30:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 592ce75b-5398-3ea7-bb1e-8be03fbef2d7 | -7.25818 | -43.31015 | 2026-09-26 03:30:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 36ce29f4-f50f-3fc4-a331-47d328686f00 | -7.40282 | -39.78936 | 2026-09-26 03:30:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 27.1 |
| 6ac0030b-fa4e-353b-9248-bff6ab30f4d1 | -7.27644 | -43.29594 | 2026-09-26 03:30:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2fbb3242-945f-3ca7-8b96-11efac0bc827 | -5.77417 | -45.10995 | 2026-09-26 03:30:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 982d3171-f279-34a7-8426-0924cf4c4275 | -5.7833 | -45.09802 | 2026-09-26 03:30:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 671492b6-6777-34da-bdbd-eaa4114ab9a8 | -5.52433 | -39.86354 | 2026-09-26 03:30:00 | NOAA-21 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cfbfc7f9-48b8-3cb3-a26d-1e105b27ef4e | -5.12873 | -42.87864 | 2026-09-26 03:30:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |


[Clique aqui para ver as próximas entradas](README6.md)
