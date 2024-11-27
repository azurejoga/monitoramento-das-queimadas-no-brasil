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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4582466f-ff8d-3136-b1d9-997df4faf976 | -4.70271 | -44.97152 | 2024-11-27 01:09:00 | TERRA_M-M | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 7f92f439-4190-3fe4-b8af-288362c3a2e7 | -3.81404 | -44.32962 | 2024-11-27 01:09:00 | TERRA_M-M | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 6164531d-118e-3cfd-94d0-061a0f2296b0 | -4.71651 | -46.56797 | 2024-11-27 01:09:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 69.9 |
| ed9efdef-d2f0-35d6-bc53-4b38d65fa1c6 | -4.54133 | -46.79393 | 2024-11-27 01:09:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 8e0981d9-0da3-3a15-98c2-d4099fecd478 | -3.92776 | -45.8638 | 2024-11-27 01:09:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 941274d8-edc0-395a-9aec-d5606c73e369 | -5.99116 | -45.38209 | 2024-11-27 01:09:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 2d128ce7-7338-38f2-a209-5769c1338dbd | -3.89731 | -45.62195 | 2024-11-27 01:09:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 16.9 |
| c8a44e61-c0cf-374d-9aa2-095af7ce70e5 | -9.17595 | -47.83269 | 2024-11-27 01:09:00 | TERRA_M-M | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f2e812da-7ec4-35e6-a389-d06cdd51915a | -3.96696 | -48.10162 | 2024-11-27 01:09:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| a7960f17-0b54-3e67-83fb-13425e1321d2 | -3.97379 | -48.07083 | 2024-11-27 01:09:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 6c93a750-d939-3c99-babb-60ca75c7aefe | -9.8396 | -48.1456 | 2024-11-27 01:09:00 | TERRA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c944c904-49ac-32a6-b306-66e199afda7b | -3.65484 | -44.48453 | 2024-11-27 01:09:00 | TERRA_M-M | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 930cff09-0aac-3d9d-930d-3b830b44dc7c | -4.14934 | -43.81878 | 2024-11-27 01:09:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 204.2 |
| df128937-6aa4-37d1-bf0e-f6f991ac86cd | -4.72906 | -46.56639 | 2024-11-27 01:09:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 60.5 |
| ccbb57e8-b718-3fa5-9e09-71ffc4eef624 | -4.73184 | -46.58518 | 2024-11-27 01:09:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 7e3d5bd3-056f-333c-8e70-37e261c16319 | -4.13826 | -43.78305 | 2024-11-27 01:09:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 77535570-5775-3900-a11a-239e04b26118 | -9.81104 | -48.16228 | 2024-11-27 01:09:00 | TERRA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 09a9d5a6-2e46-32ba-992a-6dd02589b22d | -9.92344 | -49.60162 | 2024-11-27 01:09:00 | TERRA_M-M | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 4b00934e-70a3-3cf5-94db-5297e1efaf9f | -8.57561 | -49.21175 | 2024-11-27 01:09:00 | TERRA_M-M | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3b78d08e-6023-3eaf-bdfb-a606b924bc34 | -4.14322 | -43.81434 | 2024-11-27 01:09:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 295.3 |
| f6f9a469-bb4b-3c9e-8ccf-bd42d3994280 | -5.02577 | -43.61435 | 2024-11-27 01:09:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 30.7 |
| a22e9cb9-e10a-3f1a-917f-74b244f09d56 | -7.26697 | -49.51169 | 2024-11-27 01:09:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4b093747-f174-3b78-80d8-7a8d971adf95 | -3.97598 | -48.08548 | 2024-11-27 01:09:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 33b3d7cc-7ee6-361a-8ac7-e6824b0e77dc | -8.05813 | -47.08973 | 2024-11-27 01:09:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| c9b4299d-509d-34fc-be94-ecc81f4bbcd0 | -3.9244 | -45.84182 | 2024-11-27 01:09:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 44.1 |
| ccb4fc69-dea7-352b-b636-3d73549f3020 | -7.85519 | -48.70629 | 2024-11-27 01:09:00 | TERRA_M-M | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a5f66d2c-e8f9-3330-9301-a465073b7ada | -5.03169 | -43.61861 | 2024-11-27 01:09:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 41328a68-9524-34c4-89e9-6e3546bfc076 | -4.65098 | -43.83112 | 2024-11-27 01:09:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 40.0 |
| d0447f7e-1dfa-3418-905c-8c26192d8aac | -7.70152 | -42.99422 | 2024-11-27 01:09:00 | TERRA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 19.5 |
| 0ccf175f-60c8-3208-afa7-9eff24202e3f | -9.72815 | -50.35046 | 2024-11-27 01:09:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b7a55e25-f461-3108-9f90-e17d99b2d24f | -7.8569 | -48.71774 | 2024-11-27 01:09:00 | TERRA_M-M | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 79886692-25e6-3a89-975c-c25b9d3b53a0 | -5.98776 | -45.36018 | 2024-11-27 01:09:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 1c258b67-2894-3560-a8b9-e2f58ec40920 | -4.01505 | -47.65553 | 2024-11-27 01:09:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 5f2300cc-f4d1-38ef-98bc-33e96612a8da | -4.02669 | -45.54286 | 2024-11-27 01:09:00 | TERRA_M-M | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 6c5f20d8-2118-3cc9-a909-df183fd7a708 | -3.92984 | -45.84664 | 2024-11-27 01:09:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 1edee108-ee4b-35fa-8d78-62e3d6230a22 | -7.69623 | -42.96234 | 2024-11-27 01:09:00 | TERRA_M-M | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 22.8 |
| 74d39a4c-13ac-3bfc-aed3-652bff40403f | -4.14461 | -43.78743 | 2024-11-27 01:09:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 2c4b3c16-f1af-33c6-8191-9fd8fc905e58 | -9.81283 | -48.17415 | 2024-11-27 01:09:00 | TERRA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5e6f2d15-8d44-39f2-aa01-025c2a61a195 | -8.57403 | -49.20111 | 2024-11-27 01:09:00 | TERRA_M-M | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 9a8eae30-c493-3f58-8d85-ec04aec888c3 | -5.19833 | -48.18509 | 2024-11-27 01:09:00 | TERRA_M-M | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 10.7 |
| ec2260c9-5b35-324e-9197-85344d9f887b | -4.71936 | -46.58709 | 2024-11-27 01:09:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 915da0cf-4b60-3a72-9936-29eef9948fc8 | -3.96253 | -48.07218 | 2024-11-27 01:09:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| b33c70a9-6e67-3042-abf8-e9d831afc237 | -8.55446 | -47.77441 | 2024-11-27 01:09:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| db8038cf-25c5-3603-827e-8f4f80347ff9 | -3.96476 | -48.08696 | 2024-11-27 01:09:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 163.9 |
| 5c79cac2-d145-31b6-8c7f-b8a15d1e0dec | -7.68678 | -42.96937 | 2024-11-27 01:09:00 | TERRA_M-M | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 30.2 |
| 06b65df2-40a8-3ffd-919c-a4ae5b66989c | -10.52655 | -49.05386 | 2024-11-27 01:09:00 | TERRA_M-M | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 55dee845-c459-3e26-afc1-81de8c19594b | -3.3935 | -44.17521 | 2024-11-27 01:09:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 661f2fd8-b062-3ef1-93fd-503151eb1917 | -3.07379 | -50.97051 | 2024-11-27 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 83c187e5-56c2-351a-9a8e-405a039361aa | -1.719 | -52.34863 | 2024-11-27 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 16c9da0b-55e1-3273-ba4f-e89951b015b4 | -2.42104 | -54.14839 | 2024-11-27 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f1f8ae91-eb04-387b-9649-8913e79ce22e | -1.638 | -52.49485 | 2024-11-27 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 38.3 |
| 9aa4ee5f-3773-35db-a421-12b2dc4d2a37 | -3.71441 | -51.79535 | 2024-11-27 01:09:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f97ce58e-0925-3c2a-8526-dd3f02e6b4f2 | -1.59262 | -52.23428 | 2024-11-27 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 52e487bf-e2ca-35e7-a3ba-7fb81758e025 | -3.09174 | -54.13526 | 2024-11-27 01:09:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 4d54125e-1163-3eb6-829c-bad8f4a41095 | -2.95153 | -53.71927 | 2024-11-27 01:09:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5d728c7e-5edd-3cc6-831a-732b5df0b9a9 | -2.83988 | -46.82383 | 2024-11-27 01:09:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 4656a4e9-944e-3d10-9e6b-fe1c12caa720 | -3.96297 | -48.07882 | 2024-11-27 01:09:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 159.0 |
| c101d643-e7a3-366c-bc32-9780d2adbf57 | -3.09812 | -53.25241 | 2024-11-27 01:09:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 347.1 |
| 26a094a1-bc78-335d-ab24-1479b3487f76 | -1.20228 | -51.74968 | 2024-11-27 01:09:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| a2a1280d-759e-3071-9f77-7fe1cf3635f9 | -2.89532 | -54.18083 | 2024-11-27 01:09:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| fc41865f-db49-360d-800b-3cc03920fa25 | -2.99436 | -51.45941 | 2024-11-27 01:09:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0741b1b1-942f-3475-ae0f-ac738c363fec | -3.52224 | -53.78525 | 2024-11-27 01:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| cc93ba78-4722-3668-a391-95faf2d3a2d8 | -3.78449 | -50.13256 | 2024-11-27 01:09:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 552a4eeb-286f-39fa-b29e-9a65f1c3a887 | -3.27281 | -50.62691 | 2024-11-27 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 8b403ae7-ae56-3578-a68f-1bee7d72abb7 | -1.66115 | -52.52179 | 2024-11-27 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 2ae6206d-9d6d-37eb-a5c6-34b8da0710c5 | -3.50217 | -50.5024 | 2024-11-27 01:09:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 431fabe5-00f2-34a8-ac0e-62bfd0ee8c1c | -4.22262 | -50.89536 | 2024-11-27 01:09:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 8741ed2a-5689-3439-b118-41fe571ce7ed | -3.12841 | -50.25967 | 2024-11-27 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 01738e39-6eb6-348a-a4e0-c5811d97ed2f | -3.58695 | -53.26132 | 2024-11-27 01:09:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| c28083ba-03fb-3435-aa7e-a8070fa59ed7 | -2.2078 | -53.79998 | 2024-11-27 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 9d7408e5-9086-3fea-8109-564ad23a2cda | -1.63346 | -52.72302 | 2024-11-27 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 5139936a-ac8e-3caa-9a87-96c4395f24ca | -2.66536 | -54.04951 | 2024-11-27 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 30a54996-cd56-3825-9527-f1c0b6755e94 | -2.25547 | -53.62133 | 2024-11-27 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 3a26be30-4542-3f83-bf7a-ef9bf01b27c6 | -1.6271 | -53.86998 | 2024-11-27 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 5fc94c8a-c58b-389b-bde5-6f226fc56b32 | -2.60231 | -54.25904 | 2024-11-27 01:09:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| a48868ec-1b27-32fc-a694-7d879feb2884 | -2.83122 | -54.11547 | 2024-11-27 01:09:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 1556c627-0b66-34b1-80c1-ddbc94908128 | -3.01936 | -53.41393 | 2024-11-27 01:09:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 35207fce-2eb3-33e5-91ac-f0d595a34e14 | -3.21291 | -54.47694 | 2024-11-27 01:09:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 46c43648-68ea-3e10-ad4e-d00450029306 | -3.08926 | -53.25365 | 2024-11-27 01:09:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 29021836-5927-3873-bda9-e09f19008d4a | -3.25239 | -50.61942 | 2024-11-27 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| a4a92086-3f23-38b4-890b-d4c7fda0fff4 | -3.59436 | -50.36663 | 2024-11-27 01:09:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 9b5bbec1-f1a3-3497-a3f2-fbb040c0924f | -3.16534 | -48.44194 | 2024-11-27 01:09:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| a3da2f6b-917b-3bfb-b459-2fb4120c9dce | -2.82997 | -54.10637 | 2024-11-27 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 47a2854d-be38-36eb-a10c-1829e34b9488 | -1.18735 | -51.96899 | 2024-11-27 01:09:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| eb8650a5-10a5-3396-a61f-01bcc27f1df1 | -2.80216 | -52.91732 | 2024-11-27 01:09:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 22040fe6-ab29-39b7-97e0-b87d9f295314 | -2.67307 | -53.04028 | 2024-11-27 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0a2033f4-4973-38f1-8ecb-bb0c1d184d09 | -1.07958 | -53.37483 | 2024-11-27 01:09:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| a30c0c10-6ab5-374b-8cf4-d6b13ce8c556 | -1.90849 | -50.60732 | 2024-11-27 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 55a91f3b-2130-3544-9023-e6289dd019ab | -1.907 | -50.59672 | 2024-11-27 01:09:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| ce5baf22-6b75-3a5e-9a89-de71ac9cc275 | -1.6347 | -52.73191 | 2024-11-27 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c8ba6b66-9e38-3777-8871-09125629a8b3 | -3.45928 | -50.84407 | 2024-11-27 01:09:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 881788d6-ea48-3908-a51b-57d3f84e4918 | -2.86491 | -53.96305 | 2024-11-27 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| a27f2ad4-9349-318e-9c28-d09219bcf1a2 | -3.69601 | -50.22795 | 2024-11-27 01:09:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| d8d1d379-2ea4-3003-9ffa-bf601ecdbada | -1.18617 | -53.88079 | 2024-11-27 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d5a8d115-329a-35ba-972c-f5b67ebe8dfa | -1.50126 | -52.04183 | 2024-11-27 01:09:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 44654c74-1028-3b4d-bd38-9e1a2b5995e5 | -1.66927 | -52.25416 | 2024-11-27 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1caf6ba8-09a9-30b1-95c5-908666c81cd7 | -3.786 | -50.14324 | 2024-11-27 01:09:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| bb1bac06-d3da-39e1-ae46-55003314ad38 | -3.52356 | -52.1447 | 2024-11-27 01:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 25.4 |
| de00ef00-cb00-3b66-9dca-1c2595e75708 | -2.73271 | -54.13565 | 2024-11-27 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| e65e13e6-c565-3747-8745-817d7373ef5c | -1.88297 | -52.66011 | 2024-11-27 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |


[Clique aqui para ver as próximas entradas](README13.md)
