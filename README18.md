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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d11666ca-f54e-30da-8118-672e82f23d6a | -9.91741 | -67.04636 | 2026-07-29 06:14:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4c381306-5756-3cc8-b389-48a22f27925a | -12.36501 | -63.44852 | 2026-07-29 06:14:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bda9d25a-2ded-33f9-83ff-d45f59e4a5ec | -12.36547 | -63.44485 | 2026-07-29 06:14:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d6aedf9b-e38c-3506-9e73-4769d57ec8ee | -8.82419 | -66.75905 | 2026-07-29 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 460d398e-3ad2-33ab-80f7-8ee74fc50ee6 | -12.3653 | -63.44603 | 2026-07-29 06:14:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ee06dbd7-2fc4-374b-b0da-b6141f617ca0 | -9.92158 | -67.04695 | 2026-07-29 06:14:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8219501c-33d8-320e-937f-2d51454a86e1 | -12.35979 | -63.44534 | 2026-07-29 06:14:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 91a61e03-0fc2-3ab8-b8e3-2081353f3f9a | -12.37126 | -63.44307 | 2026-07-29 06:14:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d1d9ec59-466d-353d-828f-4aa46dc4f199 | -12.37082 | -63.44674 | 2026-07-29 06:14:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0ceb7805-2532-314d-8839-d4fd2a300b22 | -8.82 | -66.75847 | 2026-07-29 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 69eb793f-447f-3a68-afb3-edf16f1b91a5 | -8.82473 | -66.7552 | 2026-07-29 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ace018c9-ceb3-3597-bdd6-38c13a62bba9 | -10.9397 | -43.0593 | 2026-07-29 06:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 2c480885-d928-3d35-bc01-6b61d05dbdde | -14.031 | -53.9728 | 2026-07-29 06:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 66.0 |
| a00b56ec-f6ac-328b-9576-5d80e63bc82e | -14.0117 | -53.975 | 2026-07-29 06:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 56.0 |
| e2bb7ef7-66b3-3488-a7e8-2057f7ba8ed0 | -14.0117 | -53.975 | 2026-07-29 07:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 60.0 |
| b2bfe219-0c0e-3238-8885-1e74225d657b | -14.031 | -53.9728 | 2026-07-29 07:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 45bfc821-2a02-37f7-800d-1cc5694921af | -15.40267 | -55.93113 | 2026-07-29 07:14:00 | AQUA_M-M | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 9974b549-4797-3a13-9590-b73dc2b4558d | -14.02645 | -53.97253 | 2026-07-29 07:14:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 43.2 |
| ab3dd929-088b-3ad9-a80d-74dc9a3a3bb6 | -14.33018 | -58.94806 | 2026-07-29 07:14:00 | AQUA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 6faaf646-d26b-3797-84dc-445a8e05ae42 | -12.35584 | -63.44527 | 2026-07-29 07:14:00 | AQUA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 4fb71c27-6b69-3782-9bf8-8f86f808e33c | -14.06653 | -53.97823 | 2026-07-29 07:14:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| ee5a29f8-b623-31c5-a1b3-6480180d16d0 | -14.34067 | -58.94001 | 2026-07-29 07:14:00 | AQUA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| a1bc548d-204e-3507-90d5-78cdffd7307c | -14.00802 | -53.95778 | 2026-07-29 07:14:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| cc5eebe2-98b6-35c6-9deb-295cb5966071 | -14.01644 | -53.97107 | 2026-07-29 07:14:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| f2805519-24b2-3749-905b-532672718075 | -14.33168 | -58.93846 | 2026-07-29 07:14:00 | AQUA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 8bd3a9ec-55d4-30ce-818e-96626db45a94 | -15.4013 | -55.94076 | 2026-07-29 07:14:00 | AQUA_M-M | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1b1acfa5-6ac3-3aed-a5de-4a9c3e1292f9 | -14.0117 | -53.975 | 2026-07-29 07:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 49.2 |
| ab4e3b84-144a-329c-a0c9-0d1d15d43de9 | -14.031 | -53.9728 | 2026-07-29 07:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 1a9f57eb-3088-3bc6-a031-b00c4e2300f5 | -14.0695 | -53.9683 | 2026-07-29 11:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 98.8 |
| cf9ae73b-2600-3a73-ae90-ea38d6d0462e | -10.73106 | -45.69548 | 2026-07-29 12:00:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 68f79860-584b-39df-a92d-b25a1fa8ab89 | -6.86872 | -46.0059 | 2026-07-29 12:00:00 | TERRA_M-T | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 89f4b7fe-4e87-3075-a14c-258a87d3cb2f | -4.03893 | -43.27352 | 2026-07-29 12:00:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 970087f6-df6c-39c1-b202-6dee95be296d | -7.99534 | -44.15273 | 2026-07-29 12:00:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 38.5 |
| cdf5456a-c2f7-3698-b713-5e434c09e0ab | -7.33841 | -45.85225 | 2026-07-29 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| aafa352b-bf6d-3559-becb-a19c7150f920 | -10.72917 | -45.71055 | 2026-07-29 12:00:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 904c51d8-da33-38bd-95be-5a3090747c28 | -7.30116 | -45.27397 | 2026-07-29 12:00:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 5d920561-8c47-38fb-96c6-2d74684e2dd4 | -10.93711 | -43.06122 | 2026-07-29 12:00:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 57639eab-ea0f-39a5-aecc-64fc4b57fbaa | -4.04194 | -43.28017 | 2026-07-29 12:00:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 85867be6-d0e6-3556-a719-7fd55b6ca44f | -9.24831 | -49.25148 | 2026-07-29 12:00:00 | TERRA_M-T | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 1d1c3678-bc03-31f2-a7a9-097787c5fa69 | -8.43905 | -51.54502 | 2026-07-29 12:00:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 824d02a0-3302-3fbb-835a-35bc2b6a53f9 | -6.87906 | -46.00743 | 2026-07-29 12:00:00 | TERRA_M-T | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 310512fd-c370-3d3e-a25c-ff3b621c4221 | -10.32682 | -49.70757 | 2026-07-29 12:00:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| e0c14bb4-871e-3d53-b73c-4cb9aaa2a8ea | -4.04426 | -43.2623 | 2026-07-29 12:00:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 54.4 |
| f39dddff-b489-38ee-bcc9-db2f0caaf15d | -7.35248 | -45.82761 | 2026-07-29 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 098d808d-b43b-3035-8129-8a34267784a2 | -7.35073 | -45.84058 | 2026-07-29 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 74d3b20f-637d-3860-b60a-89197bcb97dd | -4.0414 | -43.25556 | 2026-07-29 12:00:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 07b4a33e-73e9-33ab-8721-b213fc03bc7b | -5.61561 | -42.93848 | 2026-07-29 12:00:00 | TERRA_M-T | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 29.1 |
| e410d746-fad4-3a13-bae9-7e8ec367517e | -6.87736 | -46.01992 | 2026-07-29 12:00:00 | TERRA_M-T | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 25.8 |
| ac70d263-f4a4-3b7e-be37-dd1df5bfee16 | -7.29929 | -45.28828 | 2026-07-29 12:00:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 108875c9-04b3-394e-ad36-4c0ce616355e | -5.6183 | -42.91804 | 2026-07-29 12:00:00 | TERRA_M-T | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 15.5 |
| aa1eca24-820d-37a6-a41f-eec82c36291c | -14.39103 | -48.02237 | 2026-07-29 12:02:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 24.4 |
| f7d32410-1db1-319f-90d5-09dad59b4843 | -12.20517 | -45.26557 | 2026-07-29 12:02:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| bfa36805-e580-3eba-9e1a-e373452b8b37 | -16.29547 | -45.64743 | 2026-07-29 12:02:00 | TERRA_M-T | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 13.1 |
| a7813751-057b-3f63-9353-0bda500f22da | -16.28311 | -45.64594 | 2026-07-29 12:02:00 | TERRA_M-T | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 18bde710-2cce-3fad-bda9-efd4808127b8 | -16.33813 | -43.10043 | 2026-07-29 12:02:00 | TERRA_M-T | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 0db80ba1-4a70-3496-af32-e831658726f6 | -16.78058 | -46.54892 | 2026-07-29 12:02:00 | TERRA_M-T | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 16.7 |
| fd3afffb-bd30-33b7-916f-b8f4479e9182 | -16.28604 | -45.65192 | 2026-07-29 12:02:00 | TERRA_M-T | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 15.6 |
| e65dbc1a-1e52-3b74-8f01-2df5cfd08fac | -16.77864 | -46.56548 | 2026-07-29 12:02:00 | TERRA_M-T | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 4fb5a536-3d08-3ce9-9ab8-04aa6a508630 | -14.19095 | -51.91162 | 2026-07-29 12:02:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 43da5200-82af-361c-a0ff-e6630e4e60b9 | -14.06606 | -53.95635 | 2026-07-29 12:02:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 285700d0-a55d-30c4-8870-2130dee3a8a6 | -14.01968 | -53.97596 | 2026-07-29 12:02:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 129e142b-d478-33b9-b8ac-d9c90e851696 | -13.74022 | -45.52304 | 2026-07-29 12:02:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 18.4 |
| aadd95a2-00ad-378f-8a92-9de9d67648d4 | -14.01008 | -53.97449 | 2026-07-29 12:02:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 93a3c28b-7d41-3801-8b35-a3250aae8717 | -14.4135 | -45.49197 | 2026-07-29 12:02:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 42706895-eb83-3695-ba32-00edb434a451 | -14.18961 | -51.92075 | 2026-07-29 12:02:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 7673a845-dd0b-3eea-ae46-9d1291e67d78 | -13.90126 | -42.00388 | 2026-07-29 12:02:00 | TERRA_M-T | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 29.2 |
| 97ef598b-c33c-34dd-9422-6ec5e0b66447 | -14.07397 | -53.96854 | 2026-07-29 12:02:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 0a5baa84-b20f-39e6-8762-190e7db3d34e | -17.56883 | -46.53051 | 2026-07-29 12:02:00 | TERRA_M-T | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 4f5a77bf-e107-37ff-94c0-72f0e4dbe544 | -11.41358 | -46.82359 | 2026-07-29 12:02:00 | TERRA_M-T | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 4c3449cc-b2da-373b-83ef-524782aff2f7 | -14.07228 | -53.97932 | 2026-07-29 12:02:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 5b25a715-0752-3b3c-957b-d4c4ae52e70f | -13.95255 | -46.02661 | 2026-07-29 12:02:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 47654908-5a18-3325-9425-e71707c976ee | -13.74776 | -45.51164 | 2026-07-29 12:02:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 63780f63-d09d-3720-8367-1e77c2dc284f | -14.33263 | -58.94921 | 2026-07-29 12:02:00 | TERRA_M-T | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 0588a9ef-e974-34de-85de-d45b79f37fde | -16.28811 | -45.63303 | 2026-07-29 12:02:00 | TERRA_M-T | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 36.7 |
| bf6fcf79-10b6-39c5-983e-c3bc2dcad011 | -11.18037 | -49.93554 | 2026-07-29 12:02:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 9250def1-9211-3f04-90f1-e0cf37012d11 | -13.30986 | -45.7563 | 2026-07-29 12:02:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 1a55a8d5-4d5b-3326-99f2-7f792b1fa2d7 | -13.72915 | -51.91406 | 2026-07-29 12:02:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 431b64fb-bfd2-31db-9e0d-12da9d9ba3e4 | -14.06292 | -53.9498 | 2026-07-29 12:02:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 3cf6cf12-1f30-38ae-8e7a-a3f60421ded5 | -11.54463 | -50.28785 | 2026-07-29 12:02:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 07f5fbd6-f3c7-3811-b818-78c0e0300b34 | -14.3271 | -58.94141 | 2026-07-29 12:02:00 | TERRA_M-T | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 4179e61c-3e0c-3e37-995a-686fd1b5f0ed | -11.65437 | -49.03674 | 2026-07-29 12:02:00 | TERRA_M-T | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| f78a53d4-443c-3673-8497-bb59677b07fa | -14.0613 | -53.96046 | 2026-07-29 12:02:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 45cc9d2f-3a1b-3003-88b8-522e40df0b38 | -14.06439 | -53.96704 | 2026-07-29 12:02:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 6575e8ea-51b4-321b-86c8-85528981d33b | -16.28531 | -45.62705 | 2026-07-29 12:02:00 | TERRA_M-T | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 11.6 |
| b4973f50-61b3-3066-9855-49fce610299f | -14.41559 | -45.47386 | 2026-07-29 12:02:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 20e09c30-3859-3234-9905-6959b9984ba1 | -16.29769 | -45.62854 | 2026-07-29 12:02:00 | TERRA_M-T | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 11.6 |
| b69a3be3-7385-3ce2-9f0b-25cd304908e7 | -13.73049 | -51.90494 | 2026-07-29 12:02:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 80f7fc41-3f3a-3a5a-9290-480c0dccf913 | -12.45079 | -50.54088 | 2026-07-29 12:02:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a574959d-cbad-3f5c-a090-a89185bbf60f | -11.41196 | -46.83625 | 2026-07-29 12:02:00 | TERRA_M-T | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 694fb43c-409d-3344-abc0-b729ed053a60 | -21.89357 | -56.25311 | 2026-07-29 12:04:00 | TERRA_M-T | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ad0cb2de-03af-357b-b461-5d61ddd71fc7 | -21.89167 | -56.26488 | 2026-07-29 12:04:00 | TERRA_M-T | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 9c31ae6e-d1de-3bba-89f7-91065b66ccab | -20.61965 | -48.71154 | 2026-07-29 12:04:00 | TERRA_M-T | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 12.1 |
| d83a0458-dd40-3c76-9b97-e2656819778c | -19.90681 | -54.30998 | 2026-07-29 12:04:00 | TERRA_M-T | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d77ac40c-892f-3695-9b49-5317e48e8384 | -19.07294 | -53.46953 | 2026-07-29 12:04:00 | TERRA_M-T | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 14.4 |
| c093dfc9-4ee6-3f8a-a8e6-888c6bced9b2 | -6.8708 | -46.0126 | 2026-07-29 12:10:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 9420b940-0461-3b2d-b68d-9271d1a90726 | -6.8708 | -46.0126 | 2026-07-29 12:20:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 0d3db10b-c6d8-3a12-8230-dd38ab82609d | -6.8708 | -46.0126 | 2026-07-29 12:30:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 36cd0171-d2e4-33ee-8075-34c498d5efd8 | -6.8708 | -46.0126 | 2026-07-29 12:40:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 0099530f-91bd-3410-b3ef-40cc8e0a4cba | -14.346 | -58.9388 | 2026-07-29 12:40:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 796343f2-fd65-3f59-be63-3db1d1dcdf9c | -14.346 | -58.9388 | 2026-07-29 12:50:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 83.7 |


[Clique aqui para ver as próximas entradas](README19.md)
