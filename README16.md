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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 04ed5197-f83a-3fb1-b0d5-a5fe7f5c203e | -13.00161 | -45.20385 | 2025-08-19 03:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 388a9ba2-963d-32a5-837c-e89d02d3bbaf | -12.99237 | -45.18843 | 2025-08-19 03:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8ab17b51-6e6d-3297-82fb-3b7b79e1dd50 | -12.49863 | -45.57025 | 2025-08-19 03:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0503b4fd-7e59-3725-b531-9bc5afeb9c72 | -13.58738 | -46.99488 | 2025-08-19 03:38:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 857e645b-ab18-3a2c-be3f-b31f237e64f9 | -17.41267 | -46.70678 | 2025-08-19 03:38:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b590ec92-154b-3e9d-be07-b5c2148ab84c | -13.62105 | -46.89375 | 2025-08-19 03:38:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dd5096e0-7da2-3e05-8ae3-3ec0442c02c8 | -13.61469 | -46.89396 | 2025-08-19 03:38:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b5a940b9-da39-332c-be03-7002cda48248 | -13.8639 | -42.62595 | 2025-08-19 03:38:00 | NOAA-20 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 9e782202-2a56-395f-a659-364a4b9e13d4 | -16.50685 | -45.0988 | 2025-08-19 03:38:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a372a3b9-100e-38ed-914a-ebd84c9c4a5a | -17.29023 | -44.89455 | 2025-08-19 03:38:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0e2b26f8-964e-3850-84d5-8cd36af9b1c4 | -13.58683 | -46.99948 | 2025-08-19 03:38:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2b836ccb-675c-3cee-b819-99ef327981bd | -12.63056 | -46.89029 | 2025-08-19 03:38:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 12576669-77e5-349a-99ec-b62404a3809f | -14.87028 | -48.05882 | 2025-08-19 03:38:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b512e2f-b352-36ff-bf9b-823b490584e0 | -15.7453 | -46.61206 | 2025-08-19 03:38:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c81596a5-4b26-3c06-a2a8-4bcfa563f4ae | -14.16512 | -45.31127 | 2025-08-19 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 548e897c-2557-3bd9-a2d7-fc88c4ee1bef | -14.50457 | -45.94465 | 2025-08-19 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 33b78fff-ad5d-3da9-a969-5185ff0fb8d6 | -15.49457 | -39.81871 | 2025-08-19 03:38:00 | NOAA-20 | PAU BRASIL | BAHIA | Brasil | 2923902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b64b2201-a146-3d39-abfa-4b5e779aa0d5 | -12.65505 | -45.81431 | 2025-08-19 03:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c12badbd-7e92-3deb-917d-f3da39d8881d | -17.28084 | -44.88932 | 2025-08-19 03:38:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ecb52317-00d0-3853-acee-3cebfee41c91 | -16.71139 | -47.62726 | 2025-08-19 03:38:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| da9f3aac-3f8c-3a6a-9e21-eb8bac7912e3 | -14.85014 | -48.05979 | 2025-08-19 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb8ca0a6-36dc-310d-a4db-0aa872a26e3c | -14.86165 | -48.07492 | 2025-08-19 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bbf0f0eb-5ea5-3740-bac5-2ce4219510ac | -13.8674 | -45.54833 | 2025-08-19 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4a3bb98d-312c-3f6f-bf5a-86d7e3853d4e | -18.94934 | -46.27238 | 2025-08-19 03:38:00 | NOAA-20 | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ed1f135-f530-32a0-ad42-767b578e5737 | -12.91436 | -46.11202 | 2025-08-19 03:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d4cf1229-3198-3776-b68a-cb72398bb7cd | -16.47938 | -45.09471 | 2025-08-19 03:38:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a486b253-01fe-3cd2-832c-2bfba72e64dd | -17.33758 | -47.17315 | 2025-08-19 03:38:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e121e89f-d6d2-3bee-b9f1-c5932659996a | -15.79934 | -48.22771 | 2025-08-19 03:38:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b35755b-0e50-3457-8ae3-711fdd06b7da | -13.8074 | -44.19535 | 2025-08-19 03:38:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a921a334-b550-3669-8688-a70e8dd10fef | -12.99086 | -45.19591 | 2025-08-19 03:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 53f1bbe8-9beb-3962-b254-bf22e8446499 | -16.19487 | -42.87953 | 2025-08-19 03:38:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 402168c1-f19e-3681-a0df-51b8f7e31eb7 | -13.85703 | -45.54232 | 2025-08-19 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 25d70384-f1eb-3c17-b015-b9a4a2ba299e | -12.49291 | -45.56914 | 2025-08-19 03:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| db3dc5da-8c3f-3421-9cdc-9e631b74bbcc | -15.79191 | -48.23155 | 2025-08-19 03:38:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 8.0 |
| ec7b65ae-3a5e-3645-8dab-f21ba210b1bb | -16.48433 | -45.10386 | 2025-08-19 03:38:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 5d9ca65f-2317-3e18-ae83-550cf3b1e601 | -13.00233 | -45.20011 | 2025-08-19 03:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 15f8d5be-fdc2-3a01-8227-160cb9ebc005 | -13.85779 | -45.53848 | 2025-08-19 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1d140a60-0f11-33a6-bf0b-ded717fa5cb5 | -17.40542 | -46.71337 | 2025-08-19 03:38:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ad7f6a7d-ae1c-3a21-b844-368e13a86841 | -14.17046 | -45.31548 | 2025-08-19 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f00cc74d-a8f5-30cd-8dfe-316968a4a8f5 | -12.62561 | -46.88958 | 2025-08-19 03:38:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0f33ec18-8ecd-3c49-9433-71fdf8722e14 | -13.58814 | -46.99305 | 2025-08-19 03:38:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9390a3a3-4eea-3683-9bef-4c5a51670f5c | -18.60751 | -46.68403 | 2025-08-19 03:38:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 58018dba-a018-34de-9f46-acf196a29608 | -19.19773 | -46.84355 | 2025-08-19 03:38:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 22b0c65c-518f-3ea5-8ea8-96570782ebec | -17.81578 | -44.48595 | 2025-08-19 03:38:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7d8eafaa-1185-3840-a0cc-706fec4ab36b | -14.86278 | -48.06983 | 2025-08-19 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eb1cc222-f72c-36ec-9de1-dd48322d05f8 | -15.81047 | -48.27846 | 2025-08-19 03:38:00 | NOAA-20 | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 02b89dcb-8d4e-3822-be9e-b01525b59a3a | -14.87131 | -48.05399 | 2025-08-19 03:38:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c4cfdf00-8e99-3c6b-8a62-8668a03a665d | -12.49514 | -45.56496 | 2025-08-19 03:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 854b7ecc-da8a-3e9e-bdd0-b37b3e406fe6 | -16.01403 | -47.79289 | 2025-08-19 03:38:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9789160b-fff0-34f5-8333-c981714349f0 | -14.5336 | -39.73512 | 2025-08-19 03:38:00 | NOAA-20 | IBICUÍ | BAHIA | Brasil | 2912301 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 3da63f1e-71b4-3af3-b507-f3ec3d3c9634 | -12.64437 | -45.0489 | 2025-08-19 03:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 35a4881c-2044-39ab-8b8e-6f94eab62dff | -13.86336 | -45.53956 | 2025-08-19 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 43964833-fb12-3d95-ba93-98036ef72690 | -12.65577 | -45.81073 | 2025-08-19 03:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 892454a8-bd30-395b-b1c5-ac43e7292542 | -12.63734 | -46.89513 | 2025-08-19 03:38:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 82b8a9eb-1d9a-3ad4-a540-7f5e92af85e3 | -17.98567 | -46.35206 | 2025-08-19 03:38:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1b81e893-8d9c-3eaf-b07d-02e4cf03b90e | -13.46064 | -47.05722 | 2025-08-19 03:38:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d9f0d486-b5d8-3599-8b38-c21dae76beda | -12.99712 | -45.19334 | 2025-08-19 03:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 46a60dc9-9136-3449-93b4-025098d01a5f | -16.47488 | -45.09037 | 2025-08-19 03:38:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b6207941-f680-3a59-a414-38ce4d887cdc | -15.40173 | -43.06735 | 2025-08-19 03:38:00 | NOAA-20 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 3.6 |
| f48d540f-2d44-300c-8410-9dee9078e217 | -16.47298 | -45.09991 | 2025-08-19 03:38:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 10490b78-e286-32a0-85a7-dfaff2ac8768 | -16.48579 | -45.08945 | 2025-08-19 03:38:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1a4c6e31-0bb0-3da0-bce1-d81c75256c71 | -17.56913 | -44.48019 | 2025-08-19 03:38:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c5491d57-9387-3695-83ff-71d55d6e4ece | -14.8664 | -48.05338 | 2025-08-19 03:38:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 378083af-4a93-3027-84d5-f67c8cd2f35d | -14.86112 | -48.03948 | 2025-08-19 03:38:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a73daceb-d081-31c4-b0fc-9fe996b453e4 | -13.00188 | -45.19826 | 2025-08-19 03:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| edb89f20-d461-3239-9871-b47998333b42 | -17.48703 | -45.85881 | 2025-08-19 03:38:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 64e88ec2-cd12-3750-824a-1396e6b312ba | -12.99487 | -45.20457 | 2025-08-19 03:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8b8d7149-8360-30e0-a9db-f9e5d688e107 | -16.48631 | -45.09424 | 2025-08-19 03:38:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 89a21a10-6a67-3ec2-939a-4e77a28ca38d | -17.344 | -47.17176 | 2025-08-19 03:38:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 167cfbe6-7b20-3ca8-a418-c41316367e4a | -13.59477 | -46.99005 | 2025-08-19 03:38:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 937b7636-2e16-379d-9299-b55b2e9a2a4f | -15.9232 | -43.51947 | 2025-08-19 03:38:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cff4775c-b4c8-3d10-99a7-9eb5ae6fe186 | -16.48001 | -45.09151 | 2025-08-19 03:38:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 829a49d1-c97e-30c7-9a29-989fbf65361d | -13.00038 | -45.20575 | 2025-08-19 03:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e2be091e-e7a2-3539-970c-5aa33af8eb2c | -17.39983 | -46.71211 | 2025-08-19 03:38:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d656ac35-326c-35ee-9da7-1636beef4e6f | -15.75148 | -46.60815 | 2025-08-19 03:38:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 70c87dba-37aa-3c8b-bc56-452531d16f8b | -12.98985 | -45.20522 | 2025-08-19 03:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 5bf34261-01ae-38dc-b422-79ffdb691d6c | -12.99161 | -45.19217 | 2025-08-19 03:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 36d763db-2c78-3efd-b90f-9f4bf2ac09ad | -12.99682 | -45.19891 | 2025-08-19 03:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 65375a6e-9e68-3216-8658-cd71a320c2d9 | -17.33097 | -47.17581 | 2025-08-19 03:38:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4224de59-f800-32df-bda5-89bb20aa143a | -14.17268 | -45.30454 | 2025-08-19 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f65990ff-c6c6-35f5-922d-e3a412c84a5d | -18.64332 | -43.66272 | 2025-08-19 03:38:00 | NOAA-20 | PRESIDENTE KUBITSCHEK | MINAS GERAIS | Brasil | 3153301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c20b42aa-83d5-3085-b35a-0f79abd97d06 | -12.92705 | -46.10943 | 2025-08-19 03:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 61ba50db-71e0-3a86-bea6-b985d91d5587 | -13.46677 | -47.05854 | 2025-08-19 03:38:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 40a26de5-e0ec-319d-be9f-42a55c6a5c29 | -17.93209 | -44.36759 | 2025-08-19 03:38:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 16770288-4e4d-3b44-b709-681177086ff4 | -17.90617 | -44.42602 | 2025-08-19 03:38:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7d0844a6-1661-31bc-95af-0e4ea1a97e54 | -13.61553 | -46.89163 | 2025-08-19 03:38:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 460afa5d-fb79-39d1-903d-2c4e5ac8349e | -12.61814 | -46.89471 | 2025-08-19 03:38:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a842ee1e-fcac-3390-94f3-7ff0f3fa768e | -14.86752 | -48.04829 | 2025-08-19 03:38:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c5a7086e-3fe1-32a9-9f53-2f913fac1af4 | -16.4825 | -45.08669 | 2025-08-19 03:38:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4ba9aa1b-9262-3ac7-8aea-3685ca5c08eb | -16.50554 | -45.1052 | 2025-08-19 03:38:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2671f51a-edb7-338c-8506-146b78f53df0 | -12.99464 | -45.21017 | 2025-08-19 03:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b944a955-9b9f-38f8-bcd7-e29b0730ebd0 | -15.75064 | -46.61225 | 2025-08-19 03:38:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 863ecf47-cb10-3df1-a7a4-03b6be3d041a | -14.86726 | -48.04185 | 2025-08-19 03:38:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e46dcb77-54fd-3025-b802-fa1179f8f208 | -14.84763 | -48.07152 | 2025-08-19 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0dce08b9-fb3c-3d86-a17f-50ea89dd2ae8 | -12.9858 | -45.19654 | 2025-08-19 03:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c5fa63d7-50f3-32fc-833e-1fed534da0a1 | -14.1665 | -45.30706 | 2025-08-19 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f27f24fc-bf85-31e0-87c3-2cd9e0fa07e7 | -15.80431 | -48.27633 | 2025-08-19 03:38:00 | NOAA-20 | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 22b1b18d-b049-3326-a9eb-dee707e5de1d | -12.99754 | -45.19517 | 2025-08-19 03:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fd1f1de5-1e73-3c2e-aa6f-d5fc7f6bf4a7 | -12.99411 | -45.20832 | 2025-08-19 03:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 347617ea-f919-303d-82db-c2307850cca2 | -12.65668 | -45.8063 | 2025-08-19 03:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README17.md)
