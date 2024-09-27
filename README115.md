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

## Dados Diários - Página 115

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c2dc4633-ea54-3bbb-8f8c-bc03ab801c46 | -8.92138 | -54.75068 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 91cce799-04f3-3f79-859f-a71742ff134d | -8.91246 | -54.74341 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f6835f61-9aac-39af-910d-308679988133 | -8.89937 | -54.73028 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5368a5a5-5a81-36d4-9ac4-23641cc9868a | -8.71414 | -54.80486 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 07178d86-c379-3b58-97bd-97df0c83d457 | -8.7134 | -54.81014 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef505d6c-61f7-3b99-a156-8913651e36a6 | -8.70864 | -54.80899 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e7837e7-2d2f-3a2b-b382-b7f141a55044 | -8.69642 | -54.79049 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 316e37b7-5a59-3c7f-9805-390d00a3e0a6 | -8.51473 | -54.69486 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e11b1a3-20b5-39e5-a35d-91a28492aabd | -8.50988 | -54.69418 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81886098-c143-3d85-b4fd-1789cd00ff2a | -8.42669 | -54.68784 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 37f5f53d-3e72-314a-9814-43e54827e68a | -8.42386 | -54.70916 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e4957b6-37f4-30db-92af-b19d09af34da | -8.42342 | -54.68717 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 472ac6a8-bb8b-328b-899f-6e03ff3c5f80 | -8.42265 | -54.69263 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 29ab9e6b-759d-3294-a55f-f5ce9ec5464f | -8.42115 | -54.70333 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bfb5c785-51e0-38d2-8b6d-9b73bda2ae2d | -8.4197 | -54.70328 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3b032ddd-4ba8-39b5-bb03-028425452ecf | -8.57778 | -53.33787 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9f8f8bb1-a885-322f-b55b-5f27e341a3b7 | -8.57732 | -53.34129 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3f480bba-4ec1-3115-a8e4-2cc932b40501 | -8.57601 | -53.35109 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 81d41e60-2c66-3f1f-a0d5-52daa5e61a4c | -8.57559 | -53.3542 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 10677965-4668-33d8-97e3-ad8ce891ba9e | -8.57196 | -53.34081 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cc7e2fde-68dd-3502-8392-068c0a371587 | -8.57152 | -53.34415 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c7b1b9da-ed66-3a4b-9152-910adae7f515 | -8.57109 | -53.34731 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| da5681b0-151c-3b3f-a48e-721952e7f0ef | -8.57069 | -53.35032 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 19e33712-0ec2-37b6-bd22-1f00e218246b | -8.91654 | -54.74983 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2f96a0bc-6c8e-30e2-b161-9af05003c30c | -8.90352 | -54.73626 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6664f637-7c67-3979-83d4-dcce7eee90c2 | -8.75057 | -54.74611 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 09b7ba98-85db-39d5-946f-0803cc597873 | -8.70932 | -54.80407 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3c552d9c-c6b0-3135-a2df-543531a5f484 | -8.70451 | -54.80325 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6216ce9d-a912-34d4-b992-478a5849da66 | -8.70045 | -54.79699 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 73afa67e-9e74-39ec-9010-243b6b8ecacd | -8.69569 | -54.79577 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| de36234c-da5a-3eb9-8a2e-fe2473c66675 | -8.69166 | -54.78922 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4438b1bb-af21-3900-acbc-f31d3ac0e1e9 | -9.81766 | -54.10909 | 2024-09-27 05:27:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd16b0eb-e5ac-339a-9ca0-b5a3af040ec5 | -9.58611 | -54.20545 | 2024-09-27 05:27:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fd2cf2db-2bad-342a-96b2-36f775d1dbdb | -10.6243 | -54.60869 | 2024-09-27 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e0bd28ec-d9e1-3730-b865-f65a546b019c | -10.6189 | -54.61082 | 2024-09-27 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2ada24cc-c54c-34fd-b5f3-ac3657746ae6 | -10.38358 | -54.49715 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 55f3d630-9991-3726-8eec-9dedb3803e71 | -10.23113 | -54.1251 | 2024-09-27 05:27:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c093ed1-bcd8-3934-91fd-9cdd6a9f197a | -10.22773 | -54.12208 | 2024-09-27 05:27:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dd937c0d-905f-3827-809e-47847fcb6c50 | -10.22596 | -54.1244 | 2024-09-27 05:27:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1d6649cf-1475-35e1-abe1-98d742ff1d53 | -10.22295 | -54.11822 | 2024-09-27 05:27:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 40b28388-cd38-38ab-8ff1-cedb5413ff3a | -10.22217 | -54.12437 | 2024-09-27 05:27:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 64541e73-ebd1-3942-a866-ce733fc0d20b | -10.17928 | -54.62164 | 2024-09-27 05:27:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b50515f6-152a-349d-9cba-10eee8c8fb54 | -10.37379 | -53.7765 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 47b3dbb0-07fe-3422-99c8-3f14fe70daf8 | -10.37335 | -53.77985 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a6a2c38-df1a-3a5e-a197-bd67f0ce10a3 | -10.37266 | -53.77717 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 84c2ecff-3bb4-35f6-bfe5-ad83dce1303c | -10.37224 | -53.78052 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b3a18cb-426a-3860-9b07-6865801516fd | -10.37158 | -53.79321 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 84ee8065-caaf-3850-8566-b6cfab90ece3 | -10.371 | -53.79051 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 069d023e-71f7-3119-a377-92525a23c295 | -10.37058 | -53.79389 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 05ece276-82f7-34bb-a2e1-48c203ef35c5 | -10.36804 | -53.77915 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e83d0e1-900a-32c9-ae50-4909bc92be09 | -10.36761 | -53.78246 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c6604737-8247-347f-a281-23d18be6ec3e | -10.36717 | -53.78577 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 01436d0c-04bc-38ae-bc70-532210053497 | -10.36694 | -53.77976 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cbcfa695-b609-34f6-9148-ae974d1da1cc | -10.36673 | -53.7891 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 158267d6-670c-39ae-9787-3f6a5b361e74 | -10.36653 | -53.78309 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bbd5eed3-fb02-359e-a29b-321d45171ef6 | -10.36629 | -53.79243 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9e83049f-1f52-38be-adff-e5b9e8cbe307 | -10.36611 | -53.78642 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 09087d45-f7c3-3022-a33a-07ca7d8f937d | -10.36585 | -53.79575 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 37b61f9a-bb28-3596-9266-8855f0bbd2f6 | -10.3657 | -53.78976 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2e6a69c3-d341-3e52-94d7-30bc265e590a | -10.36528 | -53.79309 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 937468be-6eed-3b1b-8b93-ed9a15e54848 | -10.36487 | -53.7964 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c0a8dffe-f22e-3626-bf4e-05d1b70bc693 | -10.36187 | -53.78503 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| de1b7849-e326-3f57-80b3-3c3338ae9b8b | -10.36143 | -53.78837 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c3442f38-88e6-393d-9e74-7212d0949a3b | -10.361 | -53.79167 | 2024-09-27 05:27:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 689750e6-eb60-39c7-8731-5bba92474ddd | -10.22734 | -54.12516 | 2024-09-27 05:27:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 57a4e49e-f1ab-36ec-a451-f0dba18dc529 | -10.22256 | -54.12129 | 2024-09-27 05:27:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30937678-3f4c-36b4-b8e2-018ceca936a2 | -10.2212 | -54.12057 | 2024-09-27 05:27:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d4242148-e9b0-3f68-b8e4-b4ddb169c861 | -10.12287 | -54.19004 | 2024-09-27 05:27:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 21b8114a-66d8-34ea-8569-dc83473f594d | -10.11773 | -54.18932 | 2024-09-27 05:27:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3b7e7902-f853-3104-b9da-91995f96cfff | -11.67793 | -54.43927 | 2024-09-27 05:27:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9e69eaf-8244-38cd-952a-b58d0a828be1 | -11.67625 | -54.44004 | 2024-09-27 05:27:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d497977b-7583-3a35-8d3d-9e7bf2d7cf15 | -11.67584 | -54.44315 | 2024-09-27 05:27:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ecd008da-cab8-3340-9777-c8dc1f48d86c | -11.67544 | -54.44626 | 2024-09-27 05:27:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f871624-4dd9-3aa7-a546-8e5988d5a3d6 | -11.67504 | -54.44934 | 2024-09-27 05:27:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68c82980-6c7d-3cbb-8879-7f67ffff1ee5 | -11.67463 | -54.45243 | 2024-09-27 05:27:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 267d8620-dea2-3c13-94ff-ed488c68e569 | -11.67276 | -54.4386 | 2024-09-27 05:27:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| edc52479-553e-3160-97e1-9590343be7bb | -11.672 | -54.44484 | 2024-09-27 05:27:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 08ac8674-eae4-36a9-8b4d-0f0900ed1899 | -11.67068 | -54.44249 | 2024-09-27 05:27:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ee74138-a92c-3d8e-80c4-dd095045e554 | -11.1385 | -54.17941 | 2024-09-27 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e08d56c-1ced-3e01-b17e-20590483bfe7 | -11.13205 | -54.18834 | 2024-09-27 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 69f4a953-d798-3eda-b6ca-8553a1ad1c74 | -10.93452 | -54.26707 | 2024-09-27 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 79ecdf62-dddd-3790-91a2-d7adce2bccda | -10.92935 | -54.26641 | 2024-09-27 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| cd285403-cc5b-325c-8fee-9d1c2cfca4e5 | -10.925 | -54.25932 | 2024-09-27 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 04ba632d-b1e8-389d-96a0-6452977ab51b | -10.92064 | -54.25234 | 2024-09-27 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e3e2a39a-77fe-35b7-b26a-531907e164e4 | -10.91943 | -54.26172 | 2024-09-27 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 30c8c79c-7b3a-3a90-89cf-ed505cad2548 | -11.23391 | -54.7802 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f9aaf59a-c9ed-3b8a-a270-2c09db6a4de5 | -11.22961 | -54.77383 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 872fd9b3-238d-30e5-80d4-e6e24cc7a314 | -11.22815 | -54.78535 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| fc090793-ec25-36fb-9aba-a353b1036671 | -11.22385 | -54.77902 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 35b53f4b-e088-33c2-8c48-5aead2d8d200 | -11.21488 | -54.76915 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d7a1fc4-0ed2-3c85-8518-14f66062cece | -11.21452 | -54.77206 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4bd427fb-9df9-3027-a30b-72535945f4c8 | -11.21387 | -54.77991 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0bc02560-97ca-301a-a93f-c175b1702e47 | -11.21379 | -54.77782 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1be85e5e-b22c-37d6-82d1-4bfd56ab4b9c | -11.21343 | -54.78069 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7f0a093-f7fb-3ecc-8634-8fb4794b46f2 | -11.21115 | -54.76193 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b17cdf57-17ce-3ced-b3b4-af94d365c8be | -11.21037 | -54.76776 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31b1a1e0-f040-3923-98eb-d2bffafb83bb | -11.21022 | -54.76559 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c2d2e07-5973-343f-b9b6-c8d94c45e96d | -11.20999 | -54.77066 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a6db607-505c-3602-ace2-13daa29f2635 | -11.20961 | -54.77354 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f8bc443a-b361-3855-b83c-46738fa3a3db | -11.20913 | -54.77429 | 2024-09-27 05:27:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README116.md)
