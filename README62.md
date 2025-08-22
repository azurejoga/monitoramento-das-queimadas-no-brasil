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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e3c9d7b6-a55f-33c4-8679-7ac574005a89 | -8.55012 | -66.94347 | 2025-08-22 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 80199b16-8443-3375-a9c1-4c8a5d563507 | -8.66176 | -70.03832 | 2025-08-22 06:01:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 16cb43e6-c2ec-3e4c-99b1-5e465639a0d1 | -8.66231 | -70.03482 | 2025-08-22 06:01:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a7f3c0bb-8778-38a6-8feb-95b3edbe7a49 | -9.20775 | -59.46585 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4ba51edf-ffed-3dc3-ac27-90385b71c00b | -9.17066 | -59.60494 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f5f4dca7-3fd2-34e6-95a4-878e2917683a | -14.7886 | -59.65958 | 2025-08-22 06:01:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6092adcb-d845-3120-9298-d4729d4bf7df | -9.20102 | -59.46984 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aaccdbf2-d13f-3a0c-afa0-1acae4f3e7ce | -9.16043 | -59.59719 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 184f57cf-4a44-3810-b6f1-7bc20edf41c6 | -9.184 | -59.59753 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 072ffc08-7681-3251-b967-14aabef7084b | -14.78922 | -59.6539 | 2025-08-22 06:01:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 07b9c5be-1b64-30dc-aaaf-4a024303d242 | -8.66544 | -70.03465 | 2025-08-22 06:01:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 817c741d-c033-32c9-a69d-d5b60ee620b4 | -8.88712 | -62.42459 | 2025-08-22 06:01:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 906d9291-f648-31ba-9c01-6d616aba3131 | -8.87444 | -62.40501 | 2025-08-22 06:01:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a4a81313-3dce-3006-aef1-768675877168 | -8.86662 | -62.4248 | 2025-08-22 06:01:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 523127fe-09d4-3603-b37a-0c7845f8079d | -9.88303 | -60.29395 | 2025-08-22 06:01:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a35ad2e4-1ba5-382c-85ae-9535dc47ddfb | -7.62679 | -69.94628 | 2025-08-22 06:01:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc8db2ff-b8be-3992-be47-d71f36e538ed | -9.17149 | -59.70667 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8beac449-d40d-32a8-8f0e-b109abd07896 | -14.78801 | -59.66501 | 2025-08-22 06:01:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 2d0d1218-1093-3f4a-b9ce-05b5254fd69a | -9.51438 | -60.54644 | 2025-08-22 06:01:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f0c24f13-31c6-3aeb-8dec-224f90850ecc | -9.21059 | -59.78497 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f07f158d-2e86-3eb3-ab58-9978b33de0fc | -9.17006 | -59.60951 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 30b19831-d62e-303c-824a-76c82ef0a05b | -9.17144 | -59.6081 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8971d795-4fb0-3176-954b-d45d884e6da8 | -9.17087 | -59.61271 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8695fe8f-310e-3651-8bf0-9dec7ade571c | -9.94922 | -60.18357 | 2025-08-22 06:01:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c5d1c873-579b-376b-9324-3fe4e0050343 | -9.23096 | -59.76938 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 02204a66-2610-3a18-a08c-877bf90b51f0 | -8.60597 | -62.61552 | 2025-08-22 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 58686755-9fab-3f49-9d66-19ce3390c0fe | -14.78858 | -59.66065 | 2025-08-22 06:01:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 772da977-9389-36d7-b015-721a09290cd1 | -10.97164 | -61.5635 | 2025-08-22 06:01:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 430555ec-0863-3460-a1b0-ac7a8c0ce37e | -8.88129 | -62.42977 | 2025-08-22 06:01:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b8116b13-3a67-3054-88db-1e056bbbbc4d | -10.10035 | -68.96114 | 2025-08-22 06:01:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c9872db9-c291-39c4-a4e4-24108c1cc247 | -8.88169 | -62.42684 | 2025-08-22 06:01:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 93fcb733-dfe1-325f-ba06-7a277d733747 | -9.74813 | -62.77377 | 2025-08-22 06:01:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c3111b7-2064-363a-8bc0-8897a7baadfc | -7.77884 | -66.95728 | 2025-08-22 06:01:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 38ad3d48-e975-3acc-9c58-d6eeddbc8c12 | -8.87364 | -62.41085 | 2025-08-22 06:01:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75041cac-87bc-3cfb-900c-42015a74a55f | -9.20903 | -60.79277 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a8bee85d-0636-3260-9197-3140c1b5a66c | -9.52116 | -60.53915 | 2025-08-22 06:01:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5617583b-2d77-37ee-ab9c-c66167219433 | -8.55078 | -66.93903 | 2025-08-22 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cedc059c-d0e9-330f-a7dd-f542fc4c1e66 | -9.31584 | -57.01835 | 2025-08-22 06:01:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 948159a4-dae8-3f69-b6dc-2ffb46da3556 | -8.66876 | -70.03517 | 2025-08-22 06:01:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c443d68b-9b48-37cf-8799-52265a9c7a96 | -9.21013 | -59.44677 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0de82bc1-27a6-3f0c-9737-3effb1e998b8 | -9.18586 | -59.59156 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fe507e3b-2d2c-3e94-9d68-ff76c0c062f1 | -9.20716 | -59.47055 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ecd32713-2229-3ec5-897d-af9cd5497671 | -9.52536 | -60.55201 | 2025-08-22 06:01:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 44a10bf6-8267-3775-81ae-51b6d467439c | -9.52068 | -68.46911 | 2025-08-22 06:01:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| acb73052-9d94-3bb6-817f-18005104ffab | -9.52639 | -60.54399 | 2025-08-22 06:01:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3dc14458-7974-3f97-bf78-4bad42262f1e | -8.85775 | -62.41469 | 2025-08-22 06:01:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5059806b-38af-3ab7-b6ae-368c778f96b2 | -8.25625 | -70.24178 | 2025-08-22 06:01:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a98d356-2fc5-3d88-8e78-42d9c619e88c | -8.86781 | -62.41602 | 2025-08-22 06:01:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 89a747cb-9dc6-3808-a452-6d26e5e40674 | -9.1846 | -59.59297 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d2c9176d-1848-36e1-b7ff-34be8f8deb94 | -9.82093 | -64.27322 | 2025-08-22 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d3e5b53-0b66-36b1-805d-883dd0d7a984 | -8.43858 | -63.86234 | 2025-08-22 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4396446e-376a-3c24-93e1-f93c310f0dba | -9.20923 | -59.45329 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5a3e8453-0033-3e1a-8fd7-21d33bd3aa73 | -9.20797 | -59.46286 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 29223066-0358-3179-bcab-880127b06c06 | -9.5172 | -68.46859 | 2025-08-22 06:01:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ca42692-3e35-38ec-acb5-d10ef91e9961 | -8.54575 | -66.94735 | 2025-08-22 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a346a697-9d3a-34dc-b924-d9f750114169 | -9.22377 | -59.77766 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5df7e659-a8ce-3c6b-ae52-bf3a05d70755 | -8.8698 | -62.40143 | 2025-08-22 06:01:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1fd4eb4a-7554-31f4-bde2-32433085252c | -8.89307 | -72.7087 | 2025-08-22 06:01:00 | NOAA-20 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1ce17462-e8e0-3012-9f0b-abce74b11287 | -8.54946 | -66.9479 | 2025-08-22 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df284584-cc69-30a2-a03b-0c56acdfd050 | -9.17977 | -59.6296 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| db905266-2808-3a5f-a5d1-709eab866b8a | -8.86741 | -62.41896 | 2025-08-22 06:01:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d837cd7b-de65-3048-afde-311ff68187ab | -9.17792 | -59.59668 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 266e8590-4bdb-3478-8a0d-d0c030d6070e | -8.89214 | -62.42531 | 2025-08-22 06:01:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 24689963-6ef7-394e-8b68-1ecffc7aa80a | -9.88355 | -60.28987 | 2025-08-22 06:01:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 19e7760d-7055-3074-8f70-9b6c8988a327 | -8.87164 | -62.42548 | 2025-08-22 06:01:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1e32cb9d-a52c-3271-9326-98d909ea25f1 | -9.21448 | -59.46186 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 32400549-0486-3627-8e67-be92400bc28b | -8.58438 | -70.63924 | 2025-08-22 06:01:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 032eb3de-c839-318e-8328-e699af47c7a2 | -9.20852 | -60.7966 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d2b8187a-74f1-39a4-89a1-9ce5f54c7534 | -8.29073 | -70.08668 | 2025-08-22 06:01:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6d9facdf-a3c2-3a8a-9d3a-06b893bbf231 | -8.46554 | -64.04679 | 2025-08-22 06:01:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7bc5b133-3efd-361d-bf9a-cbf530580fe8 | -8.87484 | -62.4021 | 2025-08-22 06:01:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ceb5eec4-d1e6-33d4-bb58-2d23d1cf036f | -9.50695 | -60.51283 | 2025-08-22 06:01:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fabe6482-63ab-34d8-9443-275da5f61aa6 | -9.18529 | -59.59615 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3051e0c5-c5e3-3f82-ac79-cfdb8e030711 | -9.20182 | -59.46213 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 99a6aa81-a655-3d75-95ab-c27515e29fa5 | -9.10236 | -61.42772 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 26887d37-fb63-3cc9-b68a-8e38c173f88e | -9.2016 | -59.46512 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 73caf62c-ede4-333f-80a8-d5e3f43c2298 | -8.75134 | -69.58942 | 2025-08-22 06:01:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3ca6f8d-58a9-36a0-938c-d67f15b6a2a6 | -7.63674 | -69.94785 | 2025-08-22 06:01:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 491cf570-b887-3a56-a740-61aa45063435 | -9.75385 | -62.76878 | 2025-08-22 06:01:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 7.6 |
| da79bd37-b71d-3afa-809d-0f1145f12f43 | -8.67623 | -69.72728 | 2025-08-22 06:01:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 455bb5b0-83d5-3097-99b5-62ade23fe72a | -9.18582 | -59.63053 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0a45aee7-a37c-3f57-9a1b-2a95bdd992dd | -9.17922 | -59.59526 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7efdc907-abdf-3156-8204-70db4c4e5c20 | -8.8821 | -62.4239 | 2025-08-22 06:01:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 48d647a7-fe36-3b22-bda8-4a744e3bf41f | -9.20802 | -60.8004 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b4cc53ad-6c01-33ec-94d2-efbcd1a24a88 | -7.75038 | -70.15473 | 2025-08-22 06:01:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b36fc3e7-4f19-326c-83e5-77a5cf70e5bf | -7.62348 | -69.94576 | 2025-08-22 06:01:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 94bc6e8f-135b-3969-b47b-36f6d03bbe30 | -8.86515 | -62.39792 | 2025-08-22 06:01:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a9e686af-032a-33ce-a10e-ce865c8b3f65 | -8.90839 | -69.43105 | 2025-08-22 06:01:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f447ed0c-0924-31ac-8a1a-b39c04322f83 | -7.72755 | -66.92292 | 2025-08-22 06:01:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 43ca9ff0-d835-3eb0-b708-59f1b6484913 | -9.22436 | -59.77311 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 790c0536-a6e7-3303-b548-9845cb96c3fe | -14.78803 | -59.66604 | 2025-08-22 06:01:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 7b773cb1-7ff0-3f55-ad26-eb332f107a61 | -8.87324 | -62.41378 | 2025-08-22 06:01:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4aa5e245-f5b4-3605-804d-4bb9ab495a2b | -7.62734 | -69.9428 | 2025-08-22 06:01:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02fa39b9-a005-3b00-ae92-a08fe2eeaa33 | -9.18037 | -59.62506 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 059636f4-52fa-3a03-b38f-0fb6fb575690 | -9.1585 | -59.60332 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 465e7eed-e4ac-3491-8824-87a6a2c61876 | -9.61387 | -67.29964 | 2025-08-22 06:01:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 027bbe7b-35af-37fb-905e-fc975bd6b4ca | -8.87867 | -62.41154 | 2025-08-22 06:01:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 25d1e4c1-03ac-3457-8752-51ed7f147325 | -9.20834 | -59.46113 | 2025-08-22 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6c4538d0-605a-333b-bd1a-9cb8d5e0c023 | -8.86555 | -62.39502 | 2025-08-22 06:01:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a6c2a52-f1ab-3ffa-b42a-a81fe71e33f6 | -8.8702 | -62.39854 | 2025-08-22 06:01:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README63.md)
