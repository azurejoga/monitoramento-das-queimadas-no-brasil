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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d2596ebc-22ea-333d-8699-2259e8cb2137 | -13.79497 | -44.08202 | 2025-10-04 04:14:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f1a5ba5f-478a-34b2-8a07-52bbda2c8e95 | -9.33629 | -54.52325 | 2025-10-04 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 216f92f9-eb89-332c-8ab3-8577232d8315 | -15.36429 | -46.28111 | 2025-10-04 04:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 03d6a7f1-8bed-3a1e-83ff-f84f6fa13a24 | -11.78382 | -46.81755 | 2025-10-04 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 35a73bc7-c9b4-3574-8420-ad5df8a5231c | -13.33977 | -47.61235 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c08ae612-8b09-3f69-853c-c0b07fb5a018 | -12.78987 | -56.96775 | 2025-10-04 04:14:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e2b0e4a2-45fb-3a8b-9f45-6b3a5c12f859 | -12.22403 | -43.77139 | 2025-10-04 04:14:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3c2121d7-a2f5-3c25-bf11-9de2bbde7f6e | -9.32802 | -54.53465 | 2025-10-04 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 05fabf7c-5ac2-3cad-8e74-087199ad65c2 | -10.3437 | -48.16753 | 2025-10-04 04:14:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fcdaa557-3685-31a6-a933-eb5055b93472 | -11.45217 | -49.7201 | 2025-10-04 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac7277e7-d85b-3201-b5a8-f38cbcee7d35 | -14.63951 | -44.73739 | 2025-10-04 04:14:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d5147acd-6dfb-3f5a-995d-4cac9d42680c | -12.52448 | -45.96907 | 2025-10-04 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 88c99b81-65fa-36f9-8885-241ec53ec0d9 | -13.96476 | -48.10122 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6cecd458-24da-3b11-8528-a0a364c516cd | -11.99595 | -47.19384 | 2025-10-04 04:14:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 87d501fa-899c-3079-b744-db1f28c051d4 | -14.28134 | -45.91364 | 2025-10-04 04:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2f3eaf6a-e743-3648-a4e0-cf44815d044d | -14.63389 | -48.24753 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cced592b-1320-32ac-bca3-413fe19b39dd | -13.3266 | -50.94312 | 2025-10-04 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 46609f9a-f04c-303e-aafe-6add65f8491c | -13.32403 | -47.19389 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 123a2ffe-de2e-3b5a-a1c3-fb25709423ed | -12.082 | -45.18481 | 2025-10-04 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eab01951-4167-3f76-8d53-151363da567c | -13.65455 | -47.29924 | 2025-10-04 04:14:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0d071c9c-42a0-3ec2-b3ac-795a232a315e | -13.08619 | -48.12553 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ef638cbe-b009-3704-a507-71aa006df752 | -13.40444 | -43.68979 | 2025-10-04 04:14:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0004c3ee-1633-3070-9b71-0b88e657ec5b | -12.86938 | -47.28601 | 2025-10-04 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b1bf3d32-c83f-3b91-a983-a4c8da437160 | -12.52881 | -45.98499 | 2025-10-04 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b0afae19-f56b-36dd-90d7-8a44fdf48b77 | -15.32119 | -46.37585 | 2025-10-04 04:14:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d09c17d5-5883-3394-9d12-8c0d51fc038a | -13.7406 | -48.05158 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 54cdf61a-a30d-320b-9d7e-477cc11af192 | -10.26765 | -44.33341 | 2025-10-04 04:14:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0a03537f-e2d0-3bc3-be7f-6fce8fdbf7b3 | -12.03306 | -45.19133 | 2025-10-04 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad89cba6-5af8-3f7d-933a-e3dcb5f79acf | -13.26342 | -47.20841 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0d80f339-5752-3acd-81cd-40cea7180927 | -11.2542 | -41.90752 | 2025-10-04 04:14:00 | NOAA-20 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 63ce8c2f-389d-3ef1-8ba5-561a16f874fd | -14.92247 | -46.89726 | 2025-10-04 04:14:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4ed3c2bf-5f97-3ca7-b359-9d4e6995d943 | -14.92224 | -46.87748 | 2025-10-04 04:14:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 49e05110-79c0-3d69-97c8-0c532cc25891 | -10.02065 | -44.02776 | 2025-10-04 04:14:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0a802267-29d6-30fe-8006-57af8fdba226 | -9.98947 | -43.6005 | 2025-10-04 04:14:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d85ab595-c343-314d-843e-b212dba9aa0f | -11.69784 | -47.5081 | 2025-10-04 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1258db11-08e7-3360-a0d9-7b029143ebf1 | -7.77216 | -46.26352 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ca1b9927-6733-33c5-8a4c-5f43b659f843 | -12.28809 | -45.36256 | 2025-10-04 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 606b7394-6549-3f0f-94a7-96822a9a6393 | -9.32202 | -45.76515 | 2025-10-04 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cef91d8a-05ad-3a75-bbb4-0d6c786ac772 | -13.74459 | -51.30725 | 2025-10-04 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d8e7a8fd-89fa-3034-a479-600cdfca5009 | -9.34458 | -45.80025 | 2025-10-04 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e1835a99-bb8b-3c05-8fdf-0cb566b5ea18 | -14.09927 | -44.3065 | 2025-10-04 04:14:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a037e09d-2993-30c6-b4c6-09b976a7ca20 | -11.92152 | -46.3866 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 26.6 |
| c30c1604-17e9-326b-86cb-aca07b197038 | -14.88596 | -46.98936 | 2025-10-04 04:14:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aef14570-0b76-3139-a783-87dc23e8c82f | -9.94076 | -50.24238 | 2025-10-04 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ce2480c6-5f72-3126-914a-ecd2f4bf2e1a | -12.72132 | -48.57511 | 2025-10-04 04:14:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 03cbbb75-a410-3085-8aa9-e6ca0ba80207 | -14.74367 | -48.08796 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 419b441b-19bf-3d88-8797-9c34a59847ea | -11.34677 | -55.08546 | 2025-10-04 04:14:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d75795d9-8074-3ad6-8ce9-6b3c48ef836d | -9.33262 | -45.65776 | 2025-10-04 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bd91cebf-50a4-3ed0-9a88-528037f87895 | -11.31306 | -47.83382 | 2025-10-04 04:14:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9a15b227-ca65-36be-bb7d-790bb31a2e5b | -13.992 | -48.20381 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 56003245-3f23-3d8a-8c81-f3be71a21f5c | -11.91282 | -46.35395 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f8ffc054-00ce-3558-bfbf-bc9e5abcdf05 | -13.60486 | -48.18541 | 2025-10-04 04:14:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fc6967c6-64b7-3728-b923-1bbf2e29b7df | -11.80067 | -45.02922 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9920a51b-a7e1-3e4b-bb4b-06b6b62ab12a | -14.92289 | -46.8736 | 2025-10-04 04:14:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 75fbaa84-d254-373d-8fb0-39ccb1996b4f | -11.49881 | -45.00446 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b4069dd0-5016-3630-99d5-a05d21e0c7d1 | -12.64302 | -46.99276 | 2025-10-04 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 504a8217-d286-3836-8bf8-733089a466ab | -9.34301 | -45.78823 | 2025-10-04 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eee83830-8742-34df-a721-8c244074bed1 | -13.46743 | -47.2682 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 29e12b51-e197-39e9-9457-4fbeb9d8be72 | -11.90114 | -46.34447 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d665540b-8612-3ed6-b6f5-7db10b00c995 | -11.1282 | -47.85433 | 2025-10-04 04:14:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fb4baf79-db53-3dd5-94b9-3fa5f93b067f | -11.54607 | -47.65194 | 2025-10-04 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e5ee37ad-3f9c-303b-91f1-90283b25759e | -13.22356 | -47.82701 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f3fdf7c4-a37e-301a-a9b4-713d05e920b8 | -9.34771 | -45.78107 | 2025-10-04 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 39a74fb2-0869-3d6a-9e4f-71f7314ba72d | -14.23868 | -46.08991 | 2025-10-04 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 209cfade-91f5-35ac-96b1-41d29cc517a0 | -12.29044 | -45.36269 | 2025-10-04 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 11766704-d0cf-32f7-b650-e034fdc458b0 | -11.12117 | -44.90274 | 2025-10-04 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 676b0ada-c5a0-326b-af50-9da62db9ef0b | -13.23013 | -48.48651 | 2025-10-04 04:14:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 01227e81-a6d2-3748-bcef-21944c7b3aec | -12.07487 | -45.16533 | 2025-10-04 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ac8ce2dc-75a4-39fd-ac0d-7a972e153703 | -14.84931 | -48.28502 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7f34db18-d604-3d3b-bf96-172552dddb2a | -11.85981 | -44.95863 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 17fdf492-eecb-310d-b4d4-3946a2e21550 | -12.08981 | -45.17879 | 2025-10-04 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| bd325eca-f05b-3234-906b-2fd2410e387b | -10.91625 | -48.93798 | 2025-10-04 04:14:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cbbfca4d-bbfe-38ab-8051-f0799687f145 | -9.91283 | -43.80694 | 2025-10-04 04:14:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dd6ae19c-3d98-32f1-9cdb-79be69d0d82e | -12.10855 | -43.44446 | 2025-10-04 04:14:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3c103357-4409-3ecc-967a-2831dd1d66ec | -9.6569 | -46.80161 | 2025-10-04 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7e625f09-d4b7-3b44-afb2-f693f71d51a4 | -12.65684 | -46.97458 | 2025-10-04 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f3c931a0-a8f0-3476-b7cb-85391d4958fa | -7.8799 | -47.35732 | 2025-10-04 04:14:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cb7d74ec-1c5d-35e5-ac69-5df78b3b543a | -9.3261 | -45.76189 | 2025-10-04 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 66271d0a-729c-352a-9f1f-a10c82fb34bc | -11.62455 | -45.0693 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 98eccd59-3fae-3c77-bda8-881033515559 | -8.62329 | -54.97997 | 2025-10-04 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78ff66d1-1f5e-3f4b-afeb-b2d0a6cac23f | -15.31783 | -46.37531 | 2025-10-04 04:14:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d482d404-a5c6-35a4-89ec-3cc05e7427d4 | -8.35322 | -46.83531 | 2025-10-04 04:14:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5f1fca0d-a4d2-314e-a818-33e67f19eccb | -14.29452 | -45.87494 | 2025-10-04 04:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ccc5d23-983c-3a2b-8c76-83e072cd66ef | -11.84219 | -45.04713 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b7c232f6-54f8-3b26-a4fd-e7f8aebc396f | -8.82942 | -46.76719 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 74c34377-be6d-3ae3-bede-a9830839558d | -11.44834 | -43.49937 | 2025-10-04 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 541d0aa7-c285-3e5e-a968-d61b555c856f | -14.69125 | -48.09113 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6bd938e2-99f5-3908-8193-64da0ac73a47 | -14.46142 | -48.39962 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 65d0a45e-c718-360c-8878-b2f7054fb319 | -11.91743 | -46.38989 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 94394a0d-b6be-31e3-91fb-812bfaf6fc27 | -13.33867 | -48.07613 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 92f8dae0-4ecc-3c89-928f-67b6fa6ab45c | -12.8705 | -44.628 | 2025-10-04 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7ef63fb0-34af-3409-aa49-0b7e43f69330 | -11.17351 | -47.74613 | 2025-10-04 04:14:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ec02df3c-5d42-3c81-bfe1-c1d2d48a8fc6 | -14.885 | -48.27309 | 2025-10-04 04:14:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5054b53d-e3ac-3dfb-a042-032a22d82dc4 | -14.85094 | -47.21914 | 2025-10-04 04:14:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5ce73fdf-646e-3bef-b517-268bc72ed544 | -12.3984 | -51.08517 | 2025-10-04 04:14:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 567488ef-93b6-31b6-bdbf-b1bf8b876ebb | -8.61528 | -54.98843 | 2025-10-04 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4f231be7-de05-39b8-bf62-d70592bf1a8a | -13.57029 | -47.58096 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8de3de4b-87c7-38c9-8653-b1e81edbd63c | -13.51712 | -47.27531 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b41dd071-1a4e-3928-8ec3-d95b09941a52 | -8.5214 | -50.03556 | 2025-10-04 04:14:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a20f0701-8e4b-355b-860d-90c541f31d51 | -13.68058 | -48.02823 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README86.md)
