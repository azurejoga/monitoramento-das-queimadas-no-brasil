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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6e03c0a9-063c-3b42-a953-914e3a7a0ba9 | -4.88413 | -41.40189 | 2024-12-19 04:06:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a9dd3098-e670-3e62-bcc6-dacbfcab0b73 | -4.47722 | -45.42375 | 2024-12-19 04:06:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 19996b6a-6538-3153-9363-aa3027b5cb4c | -2.4443 | -47.48601 | 2024-12-19 04:06:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 95e65828-68bf-3004-89f3-5a4658f98360 | -4.92243 | -41.32621 | 2024-12-19 04:06:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 029c7b94-4a28-3021-8996-343b311e98ff | -1.56465 | -53.78359 | 2024-12-19 04:06:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fc411bd7-b537-33e6-92c7-f94dbb84afc8 | -2.55713 | -46.87824 | 2024-12-19 04:06:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e3dd5f3-c6ee-3619-8dad-a62f81577159 | -1.61675 | -45.83829 | 2024-12-19 04:06:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa69db81-7bfe-3aaa-84e5-851c00e70eee | -4.11672 | -43.56088 | 2024-12-19 04:06:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fd09952f-4fc4-35d6-8843-da6b2953cdcd | -1.56578 | -53.77671 | 2024-12-19 04:06:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5814b7b0-491c-34a8-ab4e-36ca00dfdd80 | -4.88746 | -41.40241 | 2024-12-19 04:06:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c093b60a-b033-363a-9c6a-c01ca9976146 | -1.4723 | -45.93347 | 2024-12-19 04:06:00 | NPP-375D | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4bfb48c8-0ca9-3afb-a65b-d40083f06162 | -5.1789 | -37.58533 | 2024-12-19 04:06:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0ae16f86-7bd8-310b-ba16-83e64ab90bdf | -2.51657 | -47.2697 | 2024-12-19 04:06:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5643d77f-09a6-35ba-8c1c-0b14a4e6fc30 | -2.47147 | -47.20773 | 2024-12-19 04:06:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e08adb23-f338-3ee7-9912-27649671f555 | -2.86937 | -45.24657 | 2024-12-19 04:06:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 26d66fcf-3c51-3f60-b71f-7596ed4e1db3 | -2.44354 | -47.49064 | 2024-12-19 04:06:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f9d892d7-2dc7-3ffb-be5a-ad7b32f07a98 | -4.67116 | -43.29597 | 2024-12-19 04:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1093a2e4-2316-37f6-9192-1cce65811b1d | -1.60487 | -47.17962 | 2024-12-19 04:06:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb2b79d6-9480-3e8c-8e21-763be7fd8ae0 | -1.75591 | -45.82955 | 2024-12-19 04:06:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 504a15ee-5c16-342f-9c20-629c19924d3d | -4.12375 | -43.56199 | 2024-12-19 04:06:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e4c5fb90-07a9-38f6-bebd-4fed62bc3cd4 | -3.98659 | -48.39808 | 2024-12-19 04:06:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1bdb1d58-65a9-3e16-b634-d696f74c0d0a | -4.53144 | -44.05439 | 2024-12-19 04:06:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2d1d8a1a-d910-3574-a885-2703d9b9650a | -2.52106 | -47.27044 | 2024-12-19 04:06:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b918aa8b-97e9-375d-8771-3f9e05a839b7 | -4.47783 | -45.42575 | 2024-12-19 04:06:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0ff39f1f-a18e-3a51-a982-f715831e31f7 | -4.90943 | -41.32791 | 2024-12-19 04:06:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d72ef5fc-6d95-3341-945f-cefe855b07d9 | -1.46766 | -45.73948 | 2024-12-19 04:06:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f35d59c-8f73-3b09-8239-566062ddf746 | -4.87134 | -41.37506 | 2024-12-19 04:06:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 74a31e72-a185-38fd-a313-b0c19a99f309 | -1.47107 | -45.93393 | 2024-12-19 04:06:00 | NPP-375D | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 19cc5f35-236d-3a71-88c2-8d88e4678713 | -3.73892 | -46.06788 | 2024-12-19 04:06:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 00dd5ea6-ce89-38e4-8b0d-3ad7cbf7215b | -1.5562 | -53.78114 | 2024-12-19 04:06:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4fb4518c-4cd1-33ff-a0a3-d96948cf5af9 | -3.97728 | -40.56105 | 2024-12-19 04:06:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 249d0c20-bbe1-361e-887d-a6969133c9eb | -1.75179 | -45.82887 | 2024-12-19 04:06:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c9d27dc7-d3d1-38d4-9b15-47efb9c681f6 | -5.82679 | -35.48126 | 2024-12-19 04:06:00 | NPP-375D | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 3.8 |
| a42ba119-7f86-394c-bc1b-e609a668feed | -4.99423 | -37.09925 | 2024-12-19 04:06:00 | NPP-375D | AREIA BRANCA | RIO GRANDE DO NORTE | Brasil | 2401107 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bf6d242f-3476-383c-ac3b-a7d541339fdc | -4.86738 | -42.63659 | 2024-12-19 04:06:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d63803d3-7765-301e-ab24-daa7afdfa8aa | -3.20917 | -42.69558 | 2024-12-19 04:06:00 | NPP-375D | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5269806d-705e-35e9-b42d-438546e97b98 | -1.75696 | -45.58941 | 2024-12-19 04:06:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c713d6a1-5b48-3509-a8d2-3bb9fe1bce52 | -3.0151 | -44.39641 | 2024-12-19 04:06:00 | NPP-375D | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7dbd5995-c3ac-3f73-9ad8-28a65b86718c | -4.86802 | -41.37454 | 2024-12-19 04:06:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8b4babca-1fbd-3808-8e8a-89f432484f04 | -3.43009 | -41.94791 | 2024-12-19 04:06:00 | NPP-375D | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 66f4a887-4897-39d5-80ed-e9a580a3b3d9 | -5.01206 | -40.01604 | 2024-12-19 04:06:00 | NPP-375D | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| f582e9eb-fd51-3c45-8f9e-227df1d209ff | -4.67401 | -43.30031 | 2024-12-19 04:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e43c9aef-e08f-3777-aea3-3871158ed3b3 | -3.2237 | -42.07933 | 2024-12-19 04:06:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3c2eccf6-1434-3718-8414-073d6cf996b9 | -4.83015 | -40.3251 | 2024-12-19 04:06:00 | NPP-375D | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c2a906da-87ab-317b-a08c-69a3c81899d2 | -2.72813 | -45.20499 | 2024-12-19 04:06:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c7eee11-bb63-37d9-9b96-a3a9338293b6 | -5.20154 | -37.68877 | 2024-12-19 04:06:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 350c3e7c-52c9-3cc6-84e1-539f503d7db7 | -4.11908 | -43.56812 | 2024-12-19 04:06:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0eeff706-740a-3455-939e-a1d42498f415 | -4.71063 | -38.44796 | 2024-12-19 04:06:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cf785fbc-c6d2-359e-96bb-5a8bcdad4413 | -1.76159 | -45.58652 | 2024-12-19 04:06:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a8391f30-0511-3b9c-aa0c-188bf934ebe2 | -4.67056 | -43.29974 | 2024-12-19 04:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ee307b46-2096-331e-9af4-7efb016d7460 | -3.93973 | -47.96272 | 2024-12-19 04:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c1063be-72ce-343d-94c2-6f3826e5607c | -5.02885 | -40.95279 | 2024-12-19 04:06:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3cbb944e-ec80-360e-be2b-83a925278847 | -1.61262 | -45.83764 | 2024-12-19 04:06:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 654b8813-a457-388f-b9f7-52b8b1b8fcb2 | -3.39776 | -41.64096 | 2024-12-19 04:06:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f05d3392-a977-3b43-a60c-18d10a67a84d | -3.957 | -46.54781 | 2024-12-19 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7b10636-7961-3dc4-9e33-7c0f322c4f77 | -2.89215 | -41.86027 | 2024-12-19 04:06:00 | NPP-375D | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8e702444-38ad-3072-9ff8-abaeb36859be | -1.78242 | -46.81053 | 2024-12-19 04:06:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3805704d-e010-30d6-a9c6-dee1eb1b14bb | -1.5632 | -53.78202 | 2024-12-19 04:06:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6210fd99-d5b4-3868-9d1a-e3a609dd3758 | -4.85865 | -41.39081 | 2024-12-19 04:06:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6443cab8-07e3-3847-8694-e4fda22adca7 | -4.12323 | -43.5648 | 2024-12-19 04:06:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9d8267f8-4aae-3db7-a195-5ea72bb57208 | -3.07263 | -40.05321 | 2024-12-19 04:06:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 25d43d39-85e0-3bd4-980a-d78309896ac7 | -3.67307 | -39.58022 | 2024-12-19 04:06:00 | NPP-375D | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| bc4c7853-45d4-3f8a-96c5-49a4f5658c2a | -4.88359 | -41.40535 | 2024-12-19 04:06:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c1d6ec02-6c28-3e74-900b-bd081192f9f8 | -4.00046 | -46.54981 | 2024-12-19 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d3d51248-057d-3398-9d7c-cd17a9c35771 | -4.87918 | -41.41176 | 2024-12-19 04:06:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 65b3b0bf-72f1-3432-9b4b-7323bbf0cf1a | -2.87327 | -45.24721 | 2024-12-19 04:06:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e26e6c27-7e76-394f-92a1-9c62407d068a | -3.99024 | -44.17171 | 2024-12-19 04:06:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 04e8c8b7-b452-3ac2-a44e-03bbc9652b3e | -3.74221 | -43.12585 | 2024-12-19 04:06:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 60756da7-23ed-3de0-ac00-303db189e982 | -1.75709 | -45.82221 | 2024-12-19 04:06:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d7ed2410-0452-30cd-b0a8-9e880cf994fa | -1.83232 | -47.10718 | 2024-12-19 04:06:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 58eabe25-653b-31ef-9753-2fccdecaabb4 | -4.88468 | -41.39842 | 2024-12-19 04:06:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e70f3595-6eeb-3ed4-a345-c09533e46a64 | -1.7565 | -45.82588 | 2024-12-19 04:06:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dcc931c7-969c-3f06-b250-235aae5ec4ae | -4.91247 | -41.32465 | 2024-12-19 04:06:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5db4c556-2dad-356f-8071-212f53677f22 | -4.11733 | -43.557 | 2024-12-19 04:06:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 336e7921-9f16-30da-a7e8-194cc088f37a | -4.88691 | -41.40587 | 2024-12-19 04:06:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b049d970-fdac-36c1-8f91-9f0f6b126624 | -5.41314 | -36.78322 | 2024-12-19 04:06:00 | NPP-375D | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3cf8b81f-5d6b-30c0-b736-b5e230554ea5 | -5.93137 | -35.62386 | 2024-12-19 04:06:00 | NPP-375D | SÃO PEDRO | RIO GRANDE DO NORTE | Brasil | 2412708 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f0052fb8-54c5-39c5-b00c-dda6dfa48f9d | -3.94433 | -47.96349 | 2024-12-19 04:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 927cc0e3-010c-3325-a487-872c59b4691b | -11.96295 | -41.32918 | 2024-12-19 04:08:00 | NPP-375D | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 230e051f-f920-3159-abc7-64932fcccd9d | -9.68734 | -36.19668 | 2024-12-19 04:08:00 | NPP-375D | BOCA DA MATA | ALAGOAS | Brasil | 2701001 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 3270d47c-bb6b-3bcf-b560-6197e3895e8c | -5.44087 | -43.266 | 2024-12-19 04:08:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 63b0fc53-433e-3a77-88b2-bcb18d3654f1 | -4.35111 | -48.47236 | 2024-12-19 04:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 755a1f1b-f631-3313-aebf-c454c1aceb04 | -5.62523 | -46.96233 | 2024-12-19 04:08:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d476d4d1-f570-3530-b092-adea17af21b2 | -4.32915 | -48.30315 | 2024-12-19 04:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 77d26205-0fd5-3903-99f8-acb3410d6f18 | -8.84001 | -35.70328 | 2024-12-19 04:08:00 | NPP-375D | MARAIAL | PERNAMBUCO | Brasil | 2609204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c2a2de3d-c898-3904-9fa0-47b247f6e703 | -5.62435 | -46.96284 | 2024-12-19 04:08:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 77d84ac0-f7ed-3c96-9413-a9dd19f69750 | -4.15821 | -48.62729 | 2024-12-19 04:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b9c00f02-4ecc-3819-b0bf-14119fedb76a | -9.35582 | -37.96733 | 2024-12-19 04:08:00 | NPP-375D | DELMIRO GOUVEIA | ALAGOAS | Brasil | 2702405 | 27 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 4686fa0d-cac4-3ba7-9e38-ebe7501c5c29 | -12.41798 | -41.08355 | 2024-12-19 04:08:00 | NPP-375D | LAJEDINHO | BAHIA | Brasil | 2919009 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| a2d6e45e-7289-3dc5-877d-6e10f1e26d7e | -6.06828 | -44.63434 | 2024-12-19 04:08:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a5bb98b3-d2b2-3174-adfb-cd3dfcef7aa9 | -9.73632 | -36.1643 | 2024-12-19 04:08:00 | NPP-375D | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9570eb0b-f0bf-3b3f-a10c-67a871aa574c | -6.68311 | -41.0403 | 2024-12-19 04:08:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3c3e9548-c0ea-37a1-8b89-4f01d4bc2d27 | -4.33083 | -48.30547 | 2024-12-19 04:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| dda24afe-d70a-35b7-9c5a-59ac935218cc | -8.25636 | -40.62192 | 2024-12-19 04:08:00 | NPP-375D | SANTA FILOMENA | PERNAMBUCO | Brasil | 2612554 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 210aab8d-4bc3-3c42-b14c-526a8f9b713a | -6.07289 | -46.12345 | 2024-12-19 04:08:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 59eb79e9-cd73-35f0-a2c5-30963ea5ed3c | -7.68662 | -35.2622 | 2024-12-19 04:08:00 | NPP-375D | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 65a6c8e0-9293-3741-942f-b59e2666dbc8 | -6.49268 | -41.6019 | 2024-12-19 04:08:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| f2615d89-db06-338b-863a-c1de470577c0 | -5.9632 | -38.26236 | 2024-12-19 04:08:00 | NPP-375D | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 824e8c7f-3911-3d22-a9cd-3435bc45cc3b | -5.21556 | -43.29945 | 2024-12-19 04:08:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bf7d673d-2f1d-3155-bf21-ee5897db9f57 | -7.92948 | -35.19004 | 2024-12-19 04:08:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |


[Clique aqui para ver as próximas entradas](README8.md)
