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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fddc5a87-37f6-3ebb-8177-23f31c0b3c53 | -3.04197 | -49.43867 | 2025-08-20 04:34:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ced9bcb5-0b45-3d11-aa96-7a288f99fe7d | -6.52739 | -45.47296 | 2025-08-20 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ac6605ba-08a0-3827-9b48-acff944194f3 | -6.06589 | -44.11716 | 2025-08-20 04:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e4c48b6e-137f-3a26-9dca-8647760271b8 | -5.65674 | -43.36714 | 2025-08-20 04:34:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 17c2f67d-0f3c-369a-89e7-8fd51ebfca24 | -9.81085 | -46.88881 | 2025-08-20 04:34:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 34a31da6-7564-336a-b98b-81a21f75610a | -9.8597 | -44.69144 | 2025-08-20 04:34:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f99903fd-b70f-38b4-b8aa-97e7aae42f30 | -7.66295 | -45.25599 | 2025-08-20 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2036502c-882b-31bc-8198-6f12321439dd | -6.26674 | -52.82669 | 2025-08-20 04:34:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2a50e6a7-ed4c-319e-aaea-e801b0dc48a7 | -7.64753 | -45.28639 | 2025-08-20 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3b48fb8e-470b-3ff3-88e9-3c125b97982b | -4.6061 | -43.3256 | 2025-08-20 04:34:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3dfbbf1a-99b0-3dfe-bb64-80693b70f3d3 | -6.92519 | -46.99611 | 2025-08-20 04:34:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6fb5df94-87cc-3e58-b7e6-1092712e2f66 | -7.64339 | -45.28983 | 2025-08-20 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ba73ffc3-19cc-323e-a9e4-7f87d65766bd | -7.66235 | -45.26 | 2025-08-20 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| daf644c3-5146-3f67-815f-b5174108e4c2 | -6.05394 | -44.14604 | 2025-08-20 04:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c87601d6-8451-39c7-97f9-46d8a4b76573 | -7.64104 | -45.28128 | 2025-08-20 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a68cc5d7-7a12-399f-b237-2fa0434fc0ca | -6.75017 | -43.79922 | 2025-08-20 04:34:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1813a097-941d-3c7f-b318-902d7dab3f88 | -4.42642 | -47.75972 | 2025-08-20 04:34:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 37f14bb7-efb0-3815-aec6-39340e6d9f0c | -8.29651 | -46.34657 | 2025-08-20 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 18495988-131c-3022-b80d-6a439f837841 | -5.86125 | -43.44071 | 2025-08-20 04:34:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3c318abb-aa95-397c-b258-3c38ffd72904 | -8.21216 | -47.30492 | 2025-08-20 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3777ae8d-7d44-3249-80fe-0c2097b1f647 | -5.98692 | -44.14051 | 2025-08-20 04:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3c75475e-6240-3991-9656-96f46cbc6f64 | -5.48678 | -42.16594 | 2025-08-20 04:34:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 239e8d7e-0aed-3b34-9525-a6913a202de8 | -5.69041 | -43.54568 | 2025-08-20 04:34:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c923aa30-08f2-34aa-b348-b6c7dd38afc6 | -5.98629 | -44.1447 | 2025-08-20 04:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 25e84840-f73f-38be-a956-2a4d600cca96 | -5.7549 | -43.98544 | 2025-08-20 04:34:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b6e5a3e5-a3a0-322b-953d-ab7ef402a6b7 | -9.31625 | -48.93263 | 2025-08-20 04:34:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8b22e8a4-c5d0-337f-bd8c-f4ef9c0ff93c | -7.63619 | -45.26932 | 2025-08-20 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 58852fbd-3692-3851-8147-d12223047e51 | -9.26709 | -44.53281 | 2025-08-20 04:34:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e74705f0-4a9d-37cb-8387-3a9ff83b1dc7 | -5.5414 | -45.3738 | 2025-08-20 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d8f730b8-ea31-33d3-9afe-2543ac988a4e | -6.05485 | -44.11529 | 2025-08-20 04:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b043e37d-2fd8-3faa-9c76-16d4556342c5 | -5.87226 | -48.11683 | 2025-08-20 04:34:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4b09461c-1489-3908-a354-4e50c714dc9f | -3.81789 | -41.55422 | 2025-08-20 04:34:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7ee0bcf6-a3e1-3d8c-bb02-614099af4fa0 | -6.08821 | -44.41145 | 2025-08-20 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4d070b47-bad2-3480-8ee1-97aa066642f4 | -5.64763 | -43.37541 | 2025-08-20 04:34:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d024c6fe-33c1-3d70-8365-00daf3929640 | -5.68788 | -46.47168 | 2025-08-20 04:34:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2c1469cc-7675-3e75-85fe-d17183550481 | -5.07136 | -37.71573 | 2025-08-20 04:34:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6f827c09-a464-3ce2-a7d5-fff4abc94da6 | -6.00607 | -44.28815 | 2025-08-20 04:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dba7b6c3-0344-373d-b886-40a638011aed | -3.74719 | -53.80426 | 2025-08-20 04:34:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f2feb277-8f2c-34ac-9c3a-66b8b973f677 | -6.46736 | -53.37844 | 2025-08-20 04:34:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 801628ef-d61a-3503-8b62-bbd35f8176f6 | -6.95186 | -42.86912 | 2025-08-20 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| d0e35352-86eb-32d8-ae03-179c0bd6e517 | -3.68975 | -44.2072 | 2025-08-20 04:34:00 | NPP-375D | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 70ffd1f6-9f6e-3b16-9f09-6123631ca4c5 | -7.64373 | -45.29107 | 2025-08-20 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 22482462-3d0d-37f6-b468-2d865125c50d | -5.99737 | -42.82568 | 2025-08-20 04:34:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| af7bb70c-56a4-31e7-b381-39b66cb8fce2 | -6.15011 | -57.72101 | 2025-08-20 04:34:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c4ddb43e-c6b0-3a07-9167-ad67e5ee1baf | -7.64619 | -45.27508 | 2025-08-20 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ac49404f-2e6b-3a2a-8778-e255c79aebc3 | -5.65601 | -43.37189 | 2025-08-20 04:34:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4fc1e0ab-4cdf-3ea5-80af-8ba6f7956b73 | -6.9224 | -46.99207 | 2025-08-20 04:34:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| de0a44ae-73b6-37ad-8d68-40c279ec9be0 | -3.03908 | -49.43422 | 2025-08-20 04:34:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c23d1a02-d27c-34ae-9bdb-00c9704914b4 | -3.51159 | -48.44598 | 2025-08-20 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c03a86ff-cb4c-307b-9645-dbfd56652304 | -7.21518 | -46.25578 | 2025-08-20 04:34:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 23fd2bea-b2cc-3ed9-abee-1329a6266bf7 | -8.03352 | -47.66798 | 2025-08-20 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 191774e5-3dd7-35dc-a5c6-ee1bd0893860 | -6.8588 | -43.61265 | 2025-08-20 04:34:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b23ffd02-282a-33aa-b9e4-ed148469dd07 | -6.86546 | -43.59424 | 2025-08-20 04:34:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 606ad6ae-621c-3670-9a42-868433b2daec | -7.57721 | -45.4186 | 2025-08-20 04:34:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 24c7662c-d6f9-36dd-ae79-8c958958851a | -6.63471 | -48.68371 | 2025-08-20 04:34:00 | NPP-375D | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6bd8043c-9149-3a94-9df5-2380ba179ea9 | -7.63269 | -46.2168 | 2025-08-20 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| da390ee7-dfe1-30ff-8d4f-1647dfb187a2 | -6.85426 | -43.61679 | 2025-08-20 04:34:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c99c59a2-11c8-3e3a-be4b-73914650214d | -2.91649 | -48.29825 | 2025-08-20 04:34:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 97ffa375-1414-38b4-a2f1-f8b75b4dcaf7 | -6.44047 | -45.50622 | 2025-08-20 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 532a4499-30d1-35a0-9f74-bac04b27b80b | -6.03785 | -44.34927 | 2025-08-20 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a0fd8da1-ab69-37be-8071-5925d7767454 | -9.85355 | -44.68118 | 2025-08-20 04:34:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aed2625b-f5f0-34a6-82f9-8c496077068d | -6.22955 | -45.28059 | 2025-08-20 04:34:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 98d8dbf4-bcd6-37b4-b007-a93a58141ab3 | -7.30417 | -43.70185 | 2025-08-20 04:34:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9d5653b4-5c60-3734-8049-01f5f009e9fc | -6.00862 | -42.83225 | 2025-08-20 04:34:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| fdaf4d71-655a-3c15-a311-c11cdc51ac64 | -3.98179 | -51.06669 | 2025-08-20 04:34:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 93f4e070-6e61-38c9-bc95-7d9d7ddd75e5 | -6.61939 | -43.87621 | 2025-08-20 04:34:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 203c7609-57dc-3e39-b263-17f001e33f00 | -7.64928 | -45.25502 | 2025-08-20 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cb4c6fd3-735c-3918-b611-c096c81dfd4c | -5.00305 | -56.03572 | 2025-08-20 04:34:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df0e305d-f887-3065-ad4d-e6fae7e36e11 | -7.26044 | -50.17975 | 2025-08-20 04:34:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 643196d7-dcc4-38d5-8f48-314794e13c17 | -3.48416 | -47.67889 | 2025-08-20 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 79539ab8-2e25-373b-a465-7c2db3318560 | -5.9783 | -44.14779 | 2025-08-20 04:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 41d0afa0-9bb6-3460-9e29-f60972a4583b | -6.94346 | -43.87098 | 2025-08-20 04:34:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d1104a87-8b49-3da7-bd83-331d8eb33360 | -6.13052 | -42.95639 | 2025-08-20 04:34:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 6f47fc48-b910-3233-a869-ec6dbc4c8596 | -5.40338 | -45.15019 | 2025-08-20 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fc117a14-4326-3653-b978-687968828621 | -5.79261 | -43.61053 | 2025-08-20 04:34:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a1cfcf9-4cf6-3f99-a8a3-c02ee86895e8 | -7.05246 | -59.2331 | 2025-08-20 04:34:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b8588b2-1929-39e2-b73a-09d6ed169d57 | -7.22378 | -44.70476 | 2025-08-20 04:34:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd541389-fd56-3307-acff-4114f3e5fb5d | -6.75396 | -43.79982 | 2025-08-20 04:34:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 46f33937-b656-321a-b7cc-a3d15383bd60 | -5.99265 | -42.83009 | 2025-08-20 04:34:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| aa911642-1d3a-37b1-9bd2-8a41d02eee36 | -7.65466 | -45.26286 | 2025-08-20 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bde5fe05-92d7-362f-8830-1a7c32d051f2 | -5.11719 | -43.21169 | 2025-08-20 04:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7c89be12-6270-3a07-b1ce-2a8f231241f0 | -6.86334 | -43.60855 | 2025-08-20 04:34:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 32921481-6bf7-3d17-a446-2c9ddf512f3c | -8.29773 | -47.62402 | 2025-08-20 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f9ec9079-b4c7-382d-8e9a-75650621eeb4 | -6.85356 | -43.62155 | 2025-08-20 04:34:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a3e75c36-ddb0-3232-8e74-68895f191261 | -7.52344 | -44.94143 | 2025-08-20 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2f8c75f4-904f-3be0-a8c9-032832418493 | -3.38696 | -47.61032 | 2025-08-20 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| d566354b-e793-30f4-841d-b274aaeaf46a | -3.97792 | -42.50739 | 2025-08-20 04:34:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| f6702df5-cb1f-3248-bcbb-7791646e26ba | -4.59312 | -48.781 | 2025-08-20 04:34:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ac140ff7-5690-313e-9a19-287f29c46587 | -6.95537 | -42.87328 | 2025-08-20 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 20.5 |
| d6f79346-d0fc-3f96-9861-b840c516047c | -5.70156 | -45.87014 | 2025-08-20 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6eadf7c1-b517-3704-a920-024054d37b96 | -4.91757 | -43.23441 | 2025-08-20 04:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 4fbb0e69-6120-38d6-a459-81c7d8d4f05f | -3.83466 | -47.73426 | 2025-08-20 04:34:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db8cd35d-3762-3462-babe-7672f959e376 | -3.23153 | -46.79613 | 2025-08-20 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 77e22ec2-4f5b-3d6d-92ca-9053cd6a9133 | -4.02278 | -48.06434 | 2025-08-20 04:34:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 565e29fe-b167-3e87-9266-b49253e7205b | -3.98506 | -42.51366 | 2025-08-20 04:34:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cc10b2e6-4a91-367f-8386-685401cab597 | -9.2711 | -44.53575 | 2025-08-20 04:34:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5901dfac-4ad9-3024-8070-c51e72769a39 | -6.73751 | -50.95815 | 2025-08-20 04:34:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1cfaecc3-7e42-33f0-91cc-f2eac7750963 | -6.36766 | -43.26266 | 2025-08-20 04:34:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 72fbf825-9ac1-3024-b172-b0af00a88291 | -8.2155 | -47.30546 | 2025-08-20 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| abd1587c-1ca3-3c98-9f0b-045696fb93ed | -3.40055 | -46.90371 | 2025-08-20 04:34:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README30.md)
