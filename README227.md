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

## Dados Diários - Página 227

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cc839419-73e5-3353-a68e-2d7bf5aed724 | -3.73346 | -59.46103 | 2026-10-09 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| af61e07a-786c-30ed-a359-a69118272941 | -8.52471 | -67.02952 | 2026-10-09 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 57bbf77d-4a5d-3a19-8480-5e8bda136519 | -4.0793 | -59.83871 | 2026-10-09 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c988f2d6-2ade-3db9-8e4c-cfa78e0b7714 | -6.92961 | -59.26352 | 2026-10-09 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 96ca34ee-a2af-386f-bac7-360584a3efa1 | -9.10952 | -67.71003 | 2026-10-09 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 773bca3f-07f7-3e14-8db6-bdc484ff7a6b | -7.00145 | -59.10571 | 2026-10-09 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f9f8611d-6615-321e-af1b-f97de514d9da | -6.6723 | -63.03072 | 2026-10-09 06:08:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96d052f6-a806-3d9c-ac96-1d2ec776cbb4 | -3.43429 | -59.54124 | 2026-10-09 06:08:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8d355a54-52a6-3297-beea-3f96ae6ebb22 | -3.7794 | -58.58087 | 2026-10-09 06:08:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6a814ab5-3070-378b-a798-5c847582dbe2 | -3.39908 | -60.85074 | 2026-10-09 06:08:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d6e510bd-40b4-3e62-878b-1a64b73be47b | -3.76934 | -58.84478 | 2026-10-09 06:08:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| be0e02d4-f3e1-31c0-991d-714129475a32 | -3.08553 | -58.09401 | 2026-10-09 06:08:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f00506ce-c453-3de2-93d6-d76cf1517a37 | -3.63262 | -60.63329 | 2026-10-09 06:08:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b04d3b63-3259-3ccf-9467-5f8532a914f3 | -3.79402 | -59.37467 | 2026-10-09 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| eef841bf-cff9-3c28-b261-da6d4e843a09 | -4.07862 | -59.84346 | 2026-10-09 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 64d3fea6-be96-3542-af1b-d16699c2288c | -3.47234 | -59.25397 | 2026-10-09 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cbf186b3-35c4-3f9a-9031-436cf987939b | -8.7113 | -62.42142 | 2026-10-09 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40d7ceba-f9d8-3c81-80a8-9179b71d174d | -9.25572 | -60.87993 | 2026-10-09 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d9ec9b00-2a49-36db-a1ef-cebf72372c49 | -3.71185 | -60.54486 | 2026-10-09 06:08:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 92f44817-8829-38c5-842f-98bdf5e09d77 | -8.54756 | -67.07401 | 2026-10-09 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cfcd8c2c-d29a-35c6-9887-3024f426b5cf | -3.73347 | -59.46102 | 2026-10-09 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 1ab13d96-7af9-3034-9855-6f514ffc27fc | -3.18733 | -58.64874 | 2026-10-09 06:08:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 251c8655-9fe5-3b1b-a743-f17a2d8ee75a | -3.15724 | -59.08914 | 2026-10-09 06:08:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ffab7fc2-729b-3efc-94db-d866d3536963 | -3.17915 | -60.39496 | 2026-10-09 06:08:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 752ddf6c-962a-3a40-97ea-5326d109940f | -3.39967 | -60.84669 | 2026-10-09 06:08:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0d22fc43-6cb7-37f9-9304-0a6c2208bcc0 | -8.44932 | -67.69954 | 2026-10-09 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86fa3ab3-7051-3ca6-9c65-5af07b0d9713 | -3.43793 | -59.54205 | 2026-10-09 06:08:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 474c8b94-1821-38be-8fc5-b66bf64e7510 | -3.89844 | -58.96086 | 2026-10-09 06:08:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5ab62763-778c-39a4-a5ac-5557dd16d475 | -9.10952 | -67.71002 | 2026-10-09 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f990cef2-07ab-3dff-a286-370cba50833b | -3.90006 | -58.95564 | 2026-10-09 06:08:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 717c3c23-ea27-3d59-bed1-12dad08ef5c9 | -3.52753 | -59.34177 | 2026-10-09 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 079c0279-a7de-351e-831c-d7338786c81b | -3.73987 | -59.37245 | 2026-10-09 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| fd4a8b8e-fafb-3086-9d9f-0554b7d81888 | -3.54427 | -59.40775 | 2026-10-09 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9b37c531-cba9-3cfc-88a3-dea09ce0707a | -3.98449 | -59.34771 | 2026-10-09 06:08:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0a2d6579-fbbc-3152-ba45-e5169b879160 | -3.53793 | -59.40674 | 2026-10-09 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 71188a1f-c6e7-3031-a11a-7cdb7eccc5fa | -3.5412 | -59.40754 | 2026-10-09 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 56f359be-b69d-394a-801d-7d06dda12543 | -3.47584 | -59.50161 | 2026-10-09 06:08:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 627e2348-7f2a-3a0d-9c40-cc40c54385a2 | -3.73722 | -59.4557 | 2026-10-09 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1f10d4fc-5fe2-34c8-adb3-005b2a82188f | -3.46907 | -59.26416 | 2026-10-09 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ee1106c1-1ae3-3282-aecb-18c8621f5e3e | -4.0793 | -59.8387 | 2026-10-09 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fbcd000a-1eb2-37bb-82a1-6e737f4791f1 | -7.57496 | -61.54247 | 2026-10-09 06:08:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 13b7f214-3e9d-39aa-b07b-f178209c75cb | -3.74234 | -59.37198 | 2026-10-09 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 00f31263-3c86-3ad2-b06a-bbb8f028462f | -3.67115 | -60.60588 | 2026-10-09 06:08:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 58691025-0cc8-384a-aed1-48f00038a498 | -3.39139 | -61.07709 | 2026-10-09 06:08:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a50ec2f3-edbd-3352-a486-5babeaf61d02 | -6.6723 | -63.03071 | 2026-10-09 06:08:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 76c90f75-52f3-34cd-bbf7-c3b2d0cd9a35 | -3.73651 | -59.46082 | 2026-10-09 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 65a2bdd7-d083-3ee1-a137-d50f5240bb9a | -3.48639 | -59.3835 | 2026-10-09 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 971064f7-f733-33f5-808c-d8f463f3c938 | -3.53398 | -59.57203 | 2026-10-09 06:08:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| bcff12a6-8ecf-39d6-b5f2-2ce8f86d4090 | -3.77855 | -58.58694 | 2026-10-09 06:08:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d0ad5066-b9e4-37ac-ae85-2cc49c92b578 | -6.49147 | -62.86601 | 2026-10-09 06:08:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f9ab5521-56ce-3fd8-8421-dd0f6263242c | -7.50174 | -70.05283 | 2026-10-09 06:08:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e39f2566-4aba-3936-b139-566af0a7b97e | -7.5744 | -61.54666 | 2026-10-09 06:08:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a9c22ad7-1650-30be-bd12-92f4c8f498d2 | -3.46804 | -60.25245 | 2026-10-09 06:08:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cbb4416b-dda0-344f-83e7-7a47d471ce40 | -8.34985 | -62.82188 | 2026-10-09 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ffd4dc95-8805-3771-9b89-bba2121fdd2e | -3.18093 | -60.39686 | 2026-10-09 06:08:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d0826514-bfb2-3833-bebd-4d8ea1f27c82 | -6.48663 | -62.86195 | 2026-10-09 06:08:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 26e65c7c-ab9c-3664-8095-32142e3d51a0 | -3.77551 | -58.58404 | 2026-10-09 06:08:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5ce3d5da-cb6a-33f1-bd1e-c9bf6d39b98f | -3.67055 | -60.61019 | 2026-10-09 06:08:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8cb6f96e-2d59-3e2d-8ff1-69187301c1ca | -5.22112 | -60.04861 | 2026-10-09 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5e6ac160-445d-3e97-8478-4e515de577ac | -6.08374 | -62.51092 | 2026-10-09 06:08:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b0b9756b-6c89-3a09-8ce7-0f9aece7448d | -10.46612 | -68.86967 | 2026-10-09 06:10:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a8ea067-080d-3af8-b391-f3866ab7ae23 | -11.75098 | -61.06045 | 2026-10-09 06:10:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 744c17b0-0379-305a-bdb8-0a8fd71ef116 | -10.36806 | -61.22346 | 2026-10-09 06:10:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8d9f1767-9cb1-3a25-82ce-cb4aae3c4d9e | -10.38545 | -68.89952 | 2026-10-09 06:10:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 6f0497f8-2451-3ea1-a44c-98756e45c57f | -10.19519 | -69.05954 | 2026-10-09 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9ccb624f-e37e-35dd-99bb-4b53c41eeb01 | -10.13482 | -68.59152 | 2026-10-09 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 2a68f92c-ea81-3fda-ae32-b9b35c069c15 | -11.75674 | -61.06662 | 2026-10-09 06:10:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 65037d1a-8873-3d2d-ba6b-869b4fbc14e5 | -11.75038 | -61.06571 | 2026-10-09 06:10:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0fd00f93-0c84-3f5e-b1cf-b9d177fae39c | -11.75734 | -61.06134 | 2026-10-09 06:10:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e5f8157a-ceda-31bd-9823-74cba8e2c5ad | -9.71842 | -67.47266 | 2026-10-09 06:10:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 86fe95f1-2cb2-32af-93c4-3fa729811a03 | -10.38481 | -68.90406 | 2026-10-09 06:10:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 42bdaa68-22ff-357d-a6c4-46c2891dce22 | -11.75098 | -61.06044 | 2026-10-09 06:10:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7988fff4-a7f4-3de7-ad37-22e136daf427 | -10.38335 | -68.90302 | 2026-10-09 06:46:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c7344701-40ee-3897-82cf-5577f477ab09 | -10.13469 | -68.59364 | 2026-10-09 06:46:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 03aed65f-2d17-3b06-8a25-1ca828dd65d5 | -10.13519 | -68.58981 | 2026-10-09 06:46:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d46b8e54-0980-3301-aea6-a85a5cd2be51 | -10.38946 | -68.90005 | 2026-10-09 06:46:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 72413a4a-5ceb-36fc-8db1-6ebff69e09fb | -9.33194 | -68.78339 | 2026-10-09 06:46:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 292590a5-c136-36d8-9ef4-ea0591f7f594 | -10.38384 | -68.89925 | 2026-10-09 06:46:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 84b7027d-fb6c-3878-ab81-68797e20a29a | -10.38384 | -68.89924 | 2026-10-09 06:46:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40f3df0b-6220-3880-92be-14813abe07a5 | -5.10503 | -46.22358 | 2026-10-09 06:57:00 | AQUA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| fff7efab-3dd0-381a-b4b8-a5778a01bf4a | -2.49647 | -56.04159 | 2026-10-09 06:57:00 | AQUA_M-M | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| d089e14a-44de-3f62-9849-8557118d6683 | -7.39372 | -44.73883 | 2026-10-09 06:57:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 82edd654-70b4-3ea6-a62b-d4346cd6af75 | -6.87502 | -45.89489 | 2026-10-09 06:57:00 | AQUA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 68c5a6b4-3787-3d81-b99a-f9f13d49bcb7 | -3.00527 | -51.01642 | 2026-10-09 06:57:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 5f07134b-fcd2-36b5-a9df-b8682c6f8512 | -4.64077 | -50.95813 | 2026-10-09 06:57:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 725dd107-5166-3a16-a005-f06e428d495f | -2.8045 | -58.27922 | 2026-10-09 06:57:00 | AQUA_M-M | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 117.3 |
| c3a58eb4-9af9-3b80-8ec9-8b5201e985df | -3.09959 | -53.94284 | 2026-10-09 06:57:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 30.1 |
| 84383e18-2a59-3930-9f0c-14af78522a51 | -4.73485 | -55.67266 | 2026-10-09 06:57:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 9b51ed16-72bb-3b0e-a51e-ce4b91e6e1e1 | -5.44254 | -43.43576 | 2026-10-09 06:57:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 70652d84-d6f6-3b8e-8468-0f61afa2ab46 | -3.34685 | -50.40693 | 2026-10-09 06:57:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| cf352b97-2536-3b9d-b9f1-612981ddbc49 | -4.63157 | -50.95676 | 2026-10-09 06:57:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 5ea8fb40-2d0a-34ea-bc9c-4a9682c6722d | -8.27587 | -45.75164 | 2026-10-09 06:57:00 | AQUA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 134.3 |
| d674ab1e-eefc-34e3-bd39-8c28e0f9b3ec | -2.82307 | -51.27964 | 2026-10-09 06:57:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 02701cf8-186d-3ef6-9552-f556c9af6659 | -3.10445 | -54.18654 | 2026-10-09 06:57:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 376b07e5-a081-3d1a-8b58-416639ea3b15 | -3.56789 | -54.67027 | 2026-10-09 06:57:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 4878b64e-3f9d-3dcb-ade5-27d5f0f05828 | -1.73852 | -52.24021 | 2026-10-09 06:57:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c7630e1d-93d0-3b13-b865-b9bf59995e97 | -6.03332 | -44.02767 | 2026-10-09 06:57:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| e77844de-f7e9-3213-89e8-f4e63b97dc7f | -3.16539 | -50.44498 | 2026-10-09 06:57:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ef4c185d-b7b5-3ef8-a6eb-972558a9135e | -3.1816 | -50.58438 | 2026-10-09 06:57:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 67bfbf98-69cb-3fd6-b47c-0063de9fba7b | -3.29864 | -54.00231 | 2026-10-09 06:57:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |


[Clique aqui para ver as próximas entradas](README228.md)
