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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d3d6e66e-9fa8-31b2-ae66-76d4de453000 | -10.45179 | -46.58004 | 2026-06-04 05:01:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e77ad4ec-e988-3791-a7b5-f545bb5d3725 | -11.7578 | -47.07208 | 2026-06-04 05:01:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| af244cd6-beda-3e90-9f56-44424bce319a | -9.79772 | -56.61019 | 2026-06-04 05:01:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 311513f5-359c-3703-8c80-63da461d39a6 | -10.86057 | -53.74737 | 2026-06-04 05:01:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b368cd20-5715-3d6a-8953-9fece72a6868 | -11.75742 | -47.07505 | 2026-06-04 05:01:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 06a8c057-9e7e-3000-86d9-d8368b83741d | -14.04994 | -46.33965 | 2026-06-04 05:01:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d64c99ce-86c1-3809-bd1f-ced49d24bdfe | -11.95276 | -54.09493 | 2026-06-04 05:01:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c00cff6f-6aa6-3bd4-a813-06bd8ba75c78 | -12.215 | -57.2772 | 2026-06-04 05:01:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5258dd56-519c-31c8-ac0c-9f3165836b64 | -10.25855 | -52.07959 | 2026-06-04 05:01:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc6b8dc1-139e-378b-b660-569067d4b851 | -15.32014 | -55.73519 | 2026-06-04 05:04:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 80092df1-8149-3509-a4eb-faa91084fa2f | -14.7679 | -52.67152 | 2026-06-04 05:04:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f46d3bbe-c618-3332-9115-1a934d6be244 | -14.65428 | -55.62973 | 2026-06-04 05:04:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c4fdc000-d907-35c0-874b-ba9c6e06562a | -14.09296 | -59.38719 | 2026-06-04 05:04:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7978fa63-2f28-3560-8c09-f0b7fb6aa484 | -16.19111 | -58.47034 | 2026-06-04 05:04:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 52868a48-bce5-3ea6-b0dd-99474af3cb2a | -14.08703 | -53.38802 | 2026-06-04 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 880cb328-4971-33f0-aa15-9d2a760c5bdf | -14.0765 | -53.38639 | 2026-06-04 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f2c90a3a-42da-3a7b-b680-008259955bb5 | -14.08569 | -59.38588 | 2026-06-04 05:04:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cd1200b4-4b4e-3150-8d9e-7a0382a25be9 | -13.516 | -54.31467 | 2026-06-04 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3d84f9a8-93bc-3d69-93c8-5d06b78cb689 | -14.09083 | -59.37796 | 2026-06-04 05:04:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ced91360-d321-363e-9682-5167ddd163c8 | -14.08678 | -59.37903 | 2026-06-04 05:04:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b015c736-cb5f-39a6-9f3f-1596a9986d0d | -21.55366 | -48.59704 | 2026-06-04 05:04:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b6a7b587-df6c-37d5-b855-ea3f42415452 | -14.07708 | -53.38239 | 2026-06-04 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 782045b1-bf05-34e0-820e-d8503ad4cf82 | -18.23545 | -54.59644 | 2026-06-04 05:04:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5ccbb1b5-c745-3862-afce-72dd38a5cdcd | -14.09371 | -59.38289 | 2026-06-04 05:04:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d51e54d0-1f18-34fd-97c0-869e56a0ef5f | -17.46536 | -55.19667 | 2026-06-04 05:04:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| c4801654-c743-359e-8050-d51d9f762b9f | -21.54951 | -49.86901 | 2026-06-04 05:04:00 | NOAA-20 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| e64d8739-f9d2-3d14-9417-609e78cfe79b | -21.55551 | -48.59482 | 2026-06-04 05:04:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ed3a3638-9d9d-3671-b2ed-6226529e6092 | -14.09259 | -59.38895 | 2026-06-04 05:04:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3e28219f-0d35-302d-82e7-15e5a7a721b4 | -14.0872 | -59.37729 | 2026-06-04 05:04:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7b77eccf-0054-3491-aaf8-1a788dcdbede | -14.09042 | -59.37968 | 2026-06-04 05:04:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1fdf2b19-069f-31a6-bf15-3f56ef3229c7 | -16.26853 | -59.72557 | 2026-06-04 05:04:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a7c8ace-9bbf-3ca3-9915-a8f771c71b4b | -16.59516 | -58.23774 | 2026-06-04 05:04:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 3ac01f07-3f17-3985-9acb-8cb954ff1446 | -14.16323 | -58.98368 | 2026-06-04 05:04:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d83507b2-820f-3633-812d-6e24538cabd4 | -14.08001 | -53.38693 | 2026-06-04 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f53c7daa-b70e-3c33-93ad-a72cd61c32eb | -19.72749 | -54.65173 | 2026-06-04 05:04:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bbe3a0ed-2ee2-33de-a775-6993c8583f4a | -13.50924 | -54.31358 | 2026-06-04 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 543aaf8f-44c3-3078-a423-398306d9b2af | -17.46141 | -55.19988 | 2026-06-04 05:04:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 20363ad7-7a37-3ee5-acb2-743f58f9b22e | -16.18704 | -58.47356 | 2026-06-04 05:04:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 9933f393-d063-319b-8406-5cf84e6db5b2 | -19.16656 | -55.18624 | 2026-06-04 05:04:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| b741ff89-7271-39dc-be51-6758f0d43661 | -16.13132 | -58.5112 | 2026-06-04 05:04:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 5b40d58c-ce05-335c-89f0-1ade95fd5b72 | -16.12234 | -58.50164 | 2026-06-04 05:04:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 5a9478e8-b986-319c-b3e1-39030f00d5fb | -16.43839 | -57.26907 | 2026-06-04 05:04:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| ce3c4d89-1bf7-34d8-ba30-d5bd2e9c875d | -14.07943 | -53.39093 | 2026-06-04 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d0ad9b04-6c19-3213-8ff1-a311fbb58585 | -14.0922 | -59.39151 | 2026-06-04 05:04:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9e187ed0-eaf4-32fd-a226-fb6ce57a680a | -16.60469 | -58.24336 | 2026-06-04 05:04:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 381b1d81-6594-3ba1-9982-032762095c6f | -19.73455 | -53.55082 | 2026-06-04 05:04:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a95eb085-8ab5-3817-bffb-5bdd904edcb6 | -15.81127 | -59.09177 | 2026-06-04 05:04:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fc70f782-515d-32b2-a075-200dd4996594 | -14.08822 | -59.3926 | 2026-06-04 05:04:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1388a0da-ae7d-3dbf-baec-67cf3311664c | -20.64664 | -55.41057 | 2026-06-04 05:04:00 | NOAA-20 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 422482ea-a688-30c7-be4b-c002aead0c9e | -14.09405 | -59.38034 | 2026-06-04 05:04:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 56a3ba48-7be2-3a93-ad86-dbca07aec5a1 | -19.78778 | -50.96266 | 2026-06-04 05:04:00 | NOAA-20 | CARNEIRINHO | MINAS GERAIS | Brasil | 3114550 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5a001ce4-7c64-31d5-a6c3-c5ec599199cf | -16.11891 | -58.50102 | 2026-06-04 05:04:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| b92adc04-af42-3766-8f73-82b9faca344c | -14.0598 | -53.39675 | 2026-06-04 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 21513df2-9613-3b77-bdbc-9d42b116b0bd | -13.70839 | -59.24425 | 2026-06-04 05:04:00 | NOAA-20 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 794e35dc-29c3-312a-8ede-0b8d7448d2d8 | -15.23665 | -48.56478 | 2026-06-04 05:04:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8b53a272-5ddb-32d2-919c-8ce8f23c0910 | -16.60067 | -58.24655 | 2026-06-04 05:04:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| ea362376-e31e-33c6-aac3-60a105171982 | -14.08352 | -53.38748 | 2026-06-04 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5121af1d-8485-302b-b857-270804fa63c2 | -16.59113 | -58.24094 | 2026-06-04 05:04:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 69c0bcd8-770a-394a-89be-8c934d5fba1b | -16.18769 | -58.46971 | 2026-06-04 05:04:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 4e9073f9-5420-3a0f-82ff-b560d1948567 | -16.18833 | -58.46587 | 2026-06-04 05:04:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| c77eeccd-4d47-3151-be7d-62ec0e8a0e2d | -14.76665 | -52.68028 | 2026-06-04 05:04:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 91e17170-c53b-3866-9aa4-343714e2b888 | -14.09734 | -59.38356 | 2026-06-04 05:04:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 68289639-8141-3bb0-abcb-e1c5f4d3c113 | -15.50157 | -56.02932 | 2026-06-04 05:04:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e71491a2-c734-3dd7-adb5-f21374c01809 | -14.44298 | -48.9048 | 2026-06-04 05:04:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2051f1f6-ece5-3185-907c-0323fb1aecf1 | -20.55646 | -46.36241 | 2026-06-04 05:04:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d90bce48-c0a9-363f-98a6-1d4c909ef811 | -16.12577 | -58.50224 | 2026-06-04 05:04:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| a2a3d2a6-b4f2-3ce1-a467-f7968302f0e8 | -14.09186 | -59.39328 | 2026-06-04 05:04:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1ed0a61f-0052-3452-9e41-ca35fc580714 | -19.72397 | -54.65119 | 2026-06-04 05:04:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0112ef49-dfb6-352f-b35c-79d3793d1251 | -21.54851 | -48.59616 | 2026-06-04 05:04:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 55b63668-4872-3025-970a-1cec548782fc | -18.46481 | -54.70412 | 2026-06-04 05:04:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1716d17d-1fda-38c0-8085-18b21690cae0 | -14.0633 | -53.39729 | 2026-06-04 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e5a3a760-70e9-3fa4-ac7c-fb7f4e39f309 | -21.55401 | -48.5937 | 2026-06-04 05:04:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 00da3535-eeb3-3849-a97e-bf26f0e2f955 | -14.16776 | -58.94293 | 2026-06-04 05:04:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 70cfc528-3f63-3ea8-9dc3-b37de61bb351 | -18.39701 | -51.45547 | 2026-06-04 05:04:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d0919ad6-b062-32d6-ac94-a2bc88c2612c | -16.1864 | -58.47742 | 2026-06-04 05:04:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 681d9783-e17b-34c8-abba-7b50e658e07e | -19.16713 | -55.18233 | 2026-06-04 05:04:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| d85c2f4b-48d5-3c7a-a8e7-4d3663146a18 | -18.3975 | -51.4517 | 2026-06-04 05:04:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 322b439d-48d2-3162-abe8-3513095c350a | -14.77156 | -52.67204 | 2026-06-04 05:04:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 22663e1b-0b4b-344b-9e22-4d97940699ce | -21.55002 | -48.59732 | 2026-06-04 05:04:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 01b28a50-9f39-34b9-afa5-8712d4a988fc | -16.19046 | -58.47419 | 2026-06-04 05:04:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 1bc9eeb2-9a19-3984-a3be-1eb010f08f2e | -17.46198 | -55.19611 | 2026-06-04 05:04:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| d8d1ef87-4dcb-3412-ae29-69767c2faf6e | -14.08644 | -53.39202 | 2026-06-04 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c9d90bf1-01f5-38ed-8d02-6f00dfc3f89a | -15.49772 | -55.72755 | 2026-06-04 05:04:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cceb0582-ba24-3759-b600-6e8f883bdd5e | -14.09809 | -59.37927 | 2026-06-04 05:04:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3162f227-f43f-37be-b277-a0a8094bbb05 | -14.16679 | -58.98434 | 2026-06-04 05:04:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 79eac60e-62a7-3a8d-aa93-149f65221b13 | -16.80299 | -54.16887 | 2026-06-04 05:04:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7862e231-e279-3828-82f6-097be4a67e49 | -14.09332 | -59.38465 | 2026-06-04 05:04:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b3362bd0-c05c-33ec-ba1f-28255351624b | -13.96682 | -53.85151 | 2026-06-04 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3d58f9a2-4f18-3482-8dfc-4619d7786991 | -13.9783 | -53.84546 | 2026-06-04 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c1d0b360-13a8-3ae5-a1de-52e5dba93f61 | -13.98174 | -53.84599 | 2026-06-04 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 29af1dd3-8994-3af1-846a-9c9cc787d052 | -13.70402 | -59.24789 | 2026-06-04 05:04:00 | NOAA-20 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 11def457-9089-3d6e-9594-c26df1f6d925 | -16.7995 | -54.16832 | 2026-06-04 05:04:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eed48b18-2496-3bb3-9648-bd2226e7e979 | -14.29538 | -49.14474 | 2026-06-04 05:04:00 | NOAA-20 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 78f614d7-f2ce-3918-a6aa-0aee111aa004 | -14.08969 | -59.38399 | 2026-06-04 05:04:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 164d2ead-4586-301a-9863-dd41ac3ea6d5 | -13.49231 | -56.57127 | 2026-06-04 05:04:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d0e7aa9c-9543-38c5-a3c2-3d9aefc99780 | -16.12724 | -58.51446 | 2026-06-04 05:04:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 07b8c2ac-af14-3fb9-adf6-e2132c341b5b | -21.55035 | -48.59399 | 2026-06-04 05:04:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 57af69dc-46fc-3c00-a1a8-c54fd035c8dc | -14.08294 | -53.39148 | 2026-06-04 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| eaaea800-1043-3159-b97d-c102422e5d4a | -14.08532 | -59.38763 | 2026-06-04 05:04:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 646bc8f3-f920-330c-ac33-a91f0365e436 | -14.76727 | -52.67591 | 2026-06-04 05:04:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README15.md)
