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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8c3179ae-1a8d-39c2-b99b-013db422ad60 | -15.3789 | -47.33327 | 2025-07-17 12:51:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 86.7 |
| ef7a18d6-a4c5-3691-9b25-e1b48cdaf9a1 | -14.72563 | -45.11934 | 2025-07-17 12:51:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 264.2 |
| c86d03ec-27dd-3fe9-83db-138c7ccd1349 | -15.63155 | -46.33627 | 2025-07-17 12:51:00 | TERRA_M-T | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 75b87c69-477a-318e-b5bb-0ea9782400bc | -21.7012 | -57.67343 | 2025-07-17 12:53:00 | TERRA_M-T | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 7de919d1-7e0a-3b44-a4ad-e3229ce28030 | -21.69977 | -57.68307 | 2025-07-17 12:53:00 | TERRA_M-T | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8d635872-4859-3435-a1d9-f83d8c9df9e7 | -20.29169 | -55.48721 | 2025-07-17 12:53:00 | TERRA_M-T | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f153375a-3d67-3c7c-b800-43ff50d265e1 | -24.87871 | -52.27129 | 2025-07-17 12:53:00 | TERRA_M-T | PALMITAL | PARANÁ | Brasil | 4117800 | 41 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| ec75810b-3a51-3d57-aece-932183b87342 | -24.87775 | -52.27734 | 2025-07-17 12:53:00 | TERRA_M-T | PALMITAL | PARANÁ | Brasil | 4117800 | 41 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| 7a242862-ca59-34b0-ae74-021b39548df1 | -20.20639 | -56.61484 | 2025-07-17 12:53:00 | TERRA_M-T | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 30.4 |
| 956c7eaf-05fc-3324-a4df-1f31b941d8b8 | -21.4835 | -53.05326 | 2025-07-17 12:53:00 | TERRA_M-T | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 5c621bd8-017b-368a-98fa-da0f2c1172b3 | -20.20775 | -56.60548 | 2025-07-17 12:53:00 | TERRA_M-T | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 23.1 |
| 6543d09e-61f4-36dd-bc7c-c046470f40e6 | -12.4011 | -50.4725 | 2025-07-17 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| b02102d6-b01a-3c4d-b853-d025b6a8ba4a | -12.427 | -50.0387 | 2025-07-17 13:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 177.8 |
| d84271de-2019-3326-9db5-afe04f11f001 | -12.4862 | -44.4928 | 2025-07-17 13:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 176.7 |
| c7b3db57-5dbc-3815-aa33-eb75080e4e07 | -12.3642 | -50.3911 | 2025-07-17 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 409707e8-3e9a-3142-adf2-982746501826 | -12.4079 | -50.0411 | 2025-07-17 13:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 27272e90-1cfe-35a6-a531-50a7fb7ad326 | -7.2275 | -44.2315 | 2025-07-17 13:00:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 2068b3ca-1a48-3a07-ab19-aadd87f38291 | -12.4669 | -44.4959 | 2025-07-17 13:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 92.3 |
| e269368f-75de-3641-8f4f-e117e385ab94 | -12.4011 | -50.4725 | 2025-07-17 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 71025a18-aeb3-3f45-990a-3cb68de0461d | -12.4862 | -44.4928 | 2025-07-17 13:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 113.7 |
| f59ad850-d2b1-313f-af84-621730c665df | -12.427 | -50.0387 | 2025-07-17 13:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 196.2 |
| 68d475e7-3a17-3e27-9786-a5a517cc5407 | -18.588 | -51.806 | 2025-07-17 13:10:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 97.4 |
| e87dabea-0ed2-31ac-be4a-888abb5b4c0c | -6.9883 | -43.7678 | 2025-07-17 13:20:00 | GOES-19 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 950ea50b-d8a6-343b-a447-306d7e7fe295 | -12.427 | -50.0387 | 2025-07-17 13:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 165.4 |
| 000d9f94-be7b-3ad3-9e9f-4197c1aaaf57 | -6.9885 | -43.7445 | 2025-07-17 13:20:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 125.6 |
| 13ae2ea5-afd3-336d-b110-81eae037b4e9 | -7.0074 | -43.7428 | 2025-07-17 13:20:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 95.0 |
| e6b29137-4ba1-313d-b71b-f5c459204f57 | -12.4079 | -50.0411 | 2025-07-17 13:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 879566fe-14cb-38f0-871b-4ab013352a48 | -18.588 | -51.806 | 2025-07-17 13:20:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 316.5 |
| 152b18bd-746c-3cbf-876e-1920856eb9c3 | -18.5875 | -51.8279 | 2025-07-17 13:20:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 115.7 |
| c53e1892-596b-3bb0-95f1-3acf0d3beaea | -12.4862 | -44.4928 | 2025-07-17 13:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 151.3 |
| 2595e6e3-a8fd-3daf-bf11-106ad7c1ea24 | -12.3642 | -50.3911 | 2025-07-17 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| ce516146-154a-3deb-a380-275e65156d90 | -12.4011 | -50.4725 | 2025-07-17 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 8478adf6-f24b-3848-8b4b-62ad28f2fa5f | -12.4862 | -44.4928 | 2025-07-17 13:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 154.2 |
| 23103cd1-7bd2-3ee8-ada2-f9d95ee31b75 | -12.427 | -50.0387 | 2025-07-17 13:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 167.0 |
| 91800425-8072-3798-a685-24943aaa988e | -12.4669 | -44.4959 | 2025-07-17 13:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 72.8 |
| d9557eca-06e5-33ae-93f7-c9ac1923b356 | -12.3642 | -50.3911 | 2025-07-17 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 74d8f595-491a-35d8-9b98-e88367703213 | -12.4011 | -50.4725 | 2025-07-17 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 93.7 |
| e719cfd0-7bff-3011-b7a3-f4cffc9333a6 | -12.3642 | -50.3911 | 2025-07-17 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 9ecad942-511b-3317-868d-a49614d43e4c | -12.427 | -50.0387 | 2025-07-17 13:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 143.3 |
| f9c793a5-a0a3-3fbc-9945-93f80fd99888 | -10.9246 | -50.0424 | 2025-07-17 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 28c81da7-e851-3ebd-8d4a-edf5a542f89b | -4.3179 | -48.3932 | 2025-07-17 13:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 62eac54e-c83e-3e24-a9c1-b957d16706aa | -18.588 | -51.806 | 2025-07-17 13:40:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 16d1c3aa-c237-3636-8920-8977fec75f13 | -12.4862 | -44.4928 | 2025-07-17 13:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 133.3 |
| 5817a7e6-2a73-3440-b2bc-05be014d354b | -12.4797 | -46.9243 | 2025-07-17 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 92.3 |
| cbc3ef80-7b03-361b-992b-4bcab5dec817 | -12.4011 | -50.4725 | 2025-07-17 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 5df69ee9-9bed-30af-8d63-6677b4dc508c | -12.3833 | -50.3888 | 2025-07-17 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 158.8 |
| d7c8c3aa-36e8-3491-80e5-85a1b72e02c3 | -18.588 | -51.806 | 2025-07-17 13:50:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 130.0 |
| b02b75dc-49f1-3b37-a880-c91b3f10f2ec | -12.4669 | -44.4959 | 2025-07-17 13:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 1a623499-dd24-3f38-b860-3c87ed4f0475 | -12.3836 | -50.3672 | 2025-07-17 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.7 |
| f559d76a-ea77-3416-b526-33b6befe2c4f | -10.9246 | -50.0424 | 2025-07-17 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 160.2 |
| dcd95bad-f9ec-3f55-ae67-77f4e3745f88 | -14.7202 | -45.0884 | 2025-07-17 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 147.6 |
| 5ed8783c-0754-3565-af3c-a2deefd38c6c | -12.427 | -50.0387 | 2025-07-17 13:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 184.9 |
| 9acc1b84-130c-3c02-9fad-f2f12b635f91 | -14.7197 | -45.1119 | 2025-07-17 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 263.3 |
| e007b174-dd0d-3083-ad62-450158171b43 | -4.3179 | -48.3932 | 2025-07-17 13:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 94eb8d04-582f-35b7-87f3-faf518ea0fb2 | -6.1683 | -45.0989 | 2025-07-17 13:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 14ec9e7e-7583-30b5-a0ef-64406d92a3aa | -12.4862 | -44.4928 | 2025-07-17 13:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 8df2485a-ed47-392b-8707-5f8bd7d7d658 | -12.3642 | -50.3911 | 2025-07-17 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 138.3 |
| c075c6f2-f6a0-3543-aad4-088a6a20a720 | -10.9246 | -50.0424 | 2025-07-17 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 3be35d54-243a-315e-a943-d31fbd7a0adf | -12.4989 | -46.9215 | 2025-07-17 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 97897d5c-0bca-336d-b5c3-85372486f6db | -12.3833 | -50.3888 | 2025-07-17 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 296.2 |
| b9912e93-5743-31f3-b668-e8047deed1b9 | -12.427 | -50.0387 | 2025-07-17 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 168.8 |
| 8127c236-2830-3244-8f5b-d228275a22c8 | -12.4862 | -44.4928 | 2025-07-17 14:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 113.1 |
| e226f9bd-edaf-3c27-b38b-77cc73456bf8 | -4.3179 | -48.3932 | 2025-07-17 14:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 84.7 |
| b8805701-f54b-38f9-8fad-9227e27fad03 | -12.4011 | -50.4725 | 2025-07-17 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.7 |
| b56733dc-c93c-3b6d-b503-51d21cd1f266 | -14.7202 | -45.0884 | 2025-07-17 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 143.2 |
| 4f5b711f-307c-369f-ac8a-40f264c3f036 | -14.7197 | -45.1119 | 2025-07-17 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 283.9 |
| a74a3358-afec-32e9-8fc4-428f842674a1 | -6.1683 | -45.0989 | 2025-07-17 14:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 125.0 |
| 91e5062c-de3d-39db-b563-ef919cf65940 | -12.3836 | -50.3672 | 2025-07-17 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 147.9 |
| 8e8b601e-7203-3122-9c13-8c16a764dd7b | -12.3642 | -50.3911 | 2025-07-17 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 176.2 |
| 6dbebd99-5922-335e-95d6-71c2a8df2109 | -12.4669 | -44.4959 | 2025-07-17 14:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 939cb9c8-8003-351c-a326-b907aa7e6e27 | -12.4797 | -46.9243 | 2025-07-17 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 108.9 |
| f6a03a48-418f-3648-bd39-2613d2de4dc8 | -10.9246 | -50.0424 | 2025-07-17 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 2ddf19a2-ae04-3496-8d8b-31558237beed | -12.427 | -50.0387 | 2025-07-17 14:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 134.0 |
| 10b02d1c-abf3-36d8-9072-9989d8fb0d9b | -12.4862 | -44.4928 | 2025-07-17 14:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 134.1 |
| 526b165f-9088-3d23-bfb9-d71089a4c5b9 | -5.8716 | -44.8029 | 2025-07-17 14:10:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| bfeda3c0-865b-3467-a7d0-c2882ec2de7d | -6.1683 | -45.0989 | 2025-07-17 14:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 1d0f2b35-cae2-32f1-8a6b-3da0659a1cb1 | -14.7202 | -45.0884 | 2025-07-17 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 131.6 |
| 9f93922d-0e1d-3655-a3e9-877cfd6d89ea | -12.4669 | -44.4959 | 2025-07-17 14:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 83.8 |
| ebc00656-ae8b-3a50-afe4-7d9658a6d85c | -12.3642 | -50.3911 | 2025-07-17 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 165.3 |
| 089a544e-06c7-341f-b59a-bf9acbe80925 | -12.4989 | -46.9215 | 2025-07-17 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 238ba9d7-1876-304f-a333-8a992bec5e5a | -10.9246 | -50.0424 | 2025-07-17 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 104.3 |
| b071cdb5-2e3e-3665-9ba3-0aa6ac7211b6 | -6.849 | -42.7506 | 2025-07-17 14:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 92.0 |
| d47b9974-e511-3643-b887-4eff444c8fbe | -12.4862 | -44.4928 | 2025-07-17 14:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 55dccf3c-0553-3bfa-a98e-c8094eee5498 | -12.4797 | -46.9243 | 2025-07-17 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 98.2 |
| f99c2c97-db42-3ed1-ad88-912fa59492ea | -12.3836 | -50.3672 | 2025-07-17 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 9a9fe528-8682-3209-a2b5-8f9b2761f6d4 | -6.1683 | -45.0989 | 2025-07-17 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 110.9 |
| cc329291-58ca-3144-8459-18a5808b1c0b | -14.7202 | -45.0884 | 2025-07-17 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 139.1 |
| e058dcb6-a374-3157-8627-dee88ed74a49 | -12.427 | -50.0387 | 2025-07-17 14:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 145.4 |
| 92686a12-9f72-3acf-8abe-e7f661e55ce9 | -12.3833 | -50.3888 | 2025-07-17 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 241.3 |
| 88da4a81-6c3e-357d-a29b-f3031f4a82c5 | -14.7197 | -45.1119 | 2025-07-17 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 230.0 |
| 0d89b28a-be2a-3c8d-b7c7-e3c42498fc71 | -6.4493 | -45.0768 | 2025-07-17 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| d1e5e57a-c9f7-3f5e-aaac-f323b26ba386 | -12.3836 | -50.3672 | 2025-07-17 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| aaaa4bb7-04f3-3642-8253-1f876dbec46a | -12.427 | -50.0387 | 2025-07-17 14:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 1d1fdb41-06ec-3041-9bee-8a27e5f2db3b | -14.7202 | -45.0884 | 2025-07-17 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 142.3 |
| 87e9852b-0f26-3954-aeb1-09f17a9300a9 | -12.4011 | -50.4725 | 2025-07-17 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 170.3 |
| e8f95286-8fec-3c3c-af5f-f2eb00e11c02 | -14.7197 | -45.1119 | 2025-07-17 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 198.2 |
| e0d7e5bb-9ed3-3c8c-9b19-4513d073439b | -12.4797 | -46.9243 | 2025-07-17 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 474f0cd2-8aaf-3eaa-b636-e1bb4ff6cf23 | -12.4862 | -44.4928 | 2025-07-17 14:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 107.5 |
| d2b60af5-58c9-3069-a178-cd718fd01478 | -2.9557 | -42.3056 | 2025-07-17 14:30:00 | GOES-19 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 90.8 |
| a28d5ac1-3032-3dce-a8eb-ddcb246fe993 | -2.9373 | -42.2354 | 2025-07-17 14:30:00 | GOES-19 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 88.8 |


[Clique aqui para ver as próximas entradas](README34.md)
