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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d575da8-df67-3854-be6d-4f07884ff049 | -16.3552 | -49.9256 | 2024-09-27 00:56:38 | GOES-16 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 01ffdcac-c0c1-3b96-a437-15d4d8268cd7 | -16.3749 | -49.9223 | 2024-09-27 00:56:38 | GOES-16 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 1d037dac-eb1e-3035-8885-09ecb9884cb7 | -16.5735 | -56.0091 | 2024-09-27 00:56:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 51.0 |
| 04a51d10-c9df-3feb-8b88-275d4b2b3b27 | -16.5738 | -55.9884 | 2024-09-27 00:56:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 54.0 |
| 148f819f-f37d-3956-b031-161ad0913072 | -19.6136 | -42.8159 | 2024-09-27 00:56:54 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 66.3 |
| d617b230-39d4-384f-8899-301de1def1ae | -19.5266 | -47.8952 | 2024-09-27 00:56:54 | GOES-16 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 75.4 |
| d1385b50-1f3d-3d4a-95ca-1cb639b9a716 | -19.5272 | -47.872 | 2024-09-27 00:56:54 | GOES-16 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 64e49b0b-19ac-38d8-bc46-9a80100360c3 | -19.5469 | -47.8907 | 2024-09-27 00:56:54 | GOES-16 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 7ee288ad-526f-3b93-81c1-aa6a9574dfb0 | -19.5476 | -47.8675 | 2024-09-27 00:56:54 | GOES-16 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 481b31d5-a726-39a4-97ec-7ad9aac136bd | -22.7645 | -44.7973 | 2024-09-27 00:57:10 | GOES-16 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 78.1 |
| f7039350-8bb1-38c0-b93d-bb4fe5258010 | -22.7433 | -44.8035 | 2024-09-27 00:57:10 | GOES-16 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 293.5 |
| 5eac0325-41ec-3119-ba2e-135be371ec91 | -22.7442 | -44.7785 | 2024-09-27 00:57:10 | GOES-16 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 196.1 |
| 09754487-54f3-344c-92be-725468c932cb | -23.5816 | -47.3408 | 2024-09-27 00:57:15 | GOES-16 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 130.1 |
| f695ac4d-9ce9-3639-80b1-655247a4a9ce | -12.15 | -50.8 | 2024-09-27 01:04:14 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 792fe989-5140-398c-ae67-fd18b488ce02 | -12.19 | -50.86 | 2024-09-27 01:04:14 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b3393622-ee86-3321-910e-9bbf53814d94 | -12.19 | -50.81 | 2024-09-27 01:04:14 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c8e25970-b201-3860-af5e-236d3e372b1c | -10.93 | -54.28 | 2024-09-27 01:04:22 | MSG-03 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0ddfa755-272a-369c-8deb-0c4cdffb9b02 | -2.6783 | -57.5893 | 2024-09-27 01:05:22 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 74.4 |
| b2873068-74ba-3a3d-a751-d5113ebed5ad | -2.8611 | -51.6699 | 2024-09-27 01:05:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 58b84d49-66f0-3fd0-83e8-058630af430c | -2.8795 | -51.6695 | 2024-09-27 01:05:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 23a45394-43a4-390d-b750-7212d9c948f4 | -3.0107 | -51.0652 | 2024-09-27 01:05:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 63b29b4a-0d2a-3197-aa0b-6043df39d275 | -3.2136 | -46.7843 | 2024-09-27 01:05:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 2f08f235-8a9c-3f3a-b202-f4dd5993f4a6 | -4.5614 | -48.0141 | 2024-09-27 01:05:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 6e246a63-b2da-3969-a09a-f9fc3c2be1cd | -6.1173 | -51.1185 | 2024-09-27 01:05:41 | GOES-16 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 7908a0e2-0e80-34ff-9dab-d2cc966c7f5e | -6.8015 | -63.1656 | 2024-09-27 01:05:45 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 1c8f2fe8-5921-3228-afab-e7936daf683f | -6.8016 | -63.1468 | 2024-09-27 01:05:45 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 29f9df51-7160-3c99-a39c-8fb5ae6090b3 | -6.8199 | -63.1651 | 2024-09-27 01:05:45 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 280.4 |
| 8185bdf5-dbee-3b7d-94bf-8fdb20296279 | -6.82 | -63.1463 | 2024-09-27 01:05:45 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 167.9 |
| be7ed60b-5d40-3312-af81-e3c0c0a6a999 | -6.8383 | -63.1645 | 2024-09-27 01:05:46 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 153.4 |
| f77ebdb9-ffe5-3cb4-8989-5526d023f61b | -6.8384 | -63.1457 | 2024-09-27 01:05:46 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 89ff054c-dd31-3654-b321-72dd6f53aa4a | -7.0912 | -46.4412 | 2024-09-27 01:05:46 | GOES-16 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 17c55d0a-62d7-37e5-a20c-b544bd2df3f7 | -7.1097 | -46.4619 | 2024-09-27 01:05:46 | GOES-16 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 56.8 |
| eb271cfb-f6b1-31d8-9f79-82d6fc142aa9 | -7.1099 | -46.4396 | 2024-09-27 01:05:46 | GOES-16 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 103.6 |
| e047309c-3609-31fe-a9e4-974ff2e6501a | -7.309 | -61.0862 | 2024-09-27 01:05:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.1 |
| aeb22ef1-6a04-3874-a619-9d32b1c26370 | -7.4605 | -60.4114 | 2024-09-27 01:05:49 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.5 |
| debded9b-950a-3918-8409-3a1377786225 | -7.4606 | -60.3923 | 2024-09-27 01:05:49 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 4129f1ec-9dd7-3d6e-9d9c-a8782f406252 | -7.479 | -60.4107 | 2024-09-27 01:05:49 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.0 |
| e3d85c71-9f26-3e53-9170-0e8f214c54b5 | -7.4791 | -60.3915 | 2024-09-27 01:05:49 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 4d7df979-bfaf-3348-bb5f-7a3822e1476c | -7.5289 | -61.3825 | 2024-09-27 01:05:49 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 4b300a19-eda4-38e5-8b73-c5d4a8f8d456 | -7.529 | -61.3635 | 2024-09-27 01:05:49 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 530ee92a-b778-343d-8e95-e9fd84ba819c | -7.5703 | -60.5984 | 2024-09-27 01:05:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 97e6fc4b-4c05-3c1f-89db-9b84bf81dd4f | -7.5704 | -60.5793 | 2024-09-27 01:05:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 66d3d5fb-7e65-3bd6-b1ab-14d687c7f295 | -7.5887 | -60.5976 | 2024-09-27 01:05:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.7 |
| bcad6e3c-c7c0-3cde-8d45-18d01b524018 | -7.5888 | -60.5785 | 2024-09-27 01:05:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 89956c43-6171-3c9b-8edf-1c1d6b63320c | -7.77 | -61.2015 | 2024-09-27 01:05:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 2de717e8-c328-3f1e-90e5-ff9dc59dc91d | -7.7701 | -61.1825 | 2024-09-27 01:05:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 104.8 |
| ea854f18-f0e4-3239-b3a8-73e6810a3584 | -7.8156 | -54.7252 | 2024-09-27 01:05:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 159.1 |
| 9f365d6b-4814-3a90-af80-9d023a68370b | -7.7885 | -61.2008 | 2024-09-27 01:05:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 31e453b1-e53f-351a-b603-8487dbbc12f8 | -7.7886 | -61.1817 | 2024-09-27 01:05:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 7ca1ab5a-5fb3-32af-b331-5c3e3512aa93 | -7.9081 | -62.9976 | 2024-09-27 01:05:52 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| aad4c9b4-c7a4-386d-b74e-557782274a57 | -7.9174 | -61.2909 | 2024-09-27 01:05:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 8280d154-0597-30e6-9cd2-dadd427685ac | -7.9175 | -61.2718 | 2024-09-27 01:05:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 93f360b6-0c20-383e-b2a5-564e0b8a5dc9 | -7.9359 | -61.2901 | 2024-09-27 01:05:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.2 |
| e44860eb-1eca-3a30-b669-c894fbff58ee | -7.936 | -61.271 | 2024-09-27 01:05:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 20fe6294-beef-367b-851e-64ccf7f44d1d | -8.1394 | -61.2817 | 2024-09-27 01:05:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 73.4 |
| f1f57039-3be4-3294-9214-ec5527c79096 | -8.3153 | -55.0157 | 2024-09-27 01:05:54 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 7e6e811a-ea24-308c-be37-6b48cfd07c3c | -8.556 | -49.6112 | 2024-09-27 01:05:55 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 129.9 |
| bb0f7131-865c-35d5-b7ce-51925ec84e71 | -8.5562 | -49.5897 | 2024-09-27 01:05:55 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| e1d0d22f-e1d0-3353-8f4c-afd2eb008aeb | -8.5748 | -49.6095 | 2024-09-27 01:05:55 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 0858e8ba-d7f0-38c4-9a04-d3362ab21df0 | -8.61 | -63.1415 | 2024-09-27 01:05:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 5e51fea3-ba2a-30b8-bef7-f2ef3a1e3543 | -8.6101 | -63.1226 | 2024-09-27 01:05:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 117.6 |
| 6cdbfee7-3c50-31eb-86c7-789fc7fec3dd | -8.6285 | -63.1408 | 2024-09-27 01:05:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 73.0 |
| c808698e-d321-3409-a2e0-7b32171d74e4 | -8.6286 | -63.1219 | 2024-09-27 01:05:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 2c093046-01b1-3fe7-bae5-ed83e594bb0a | -8.7032 | -66.9907 | 2024-09-27 01:05:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 880a5480-8aeb-3ce5-a6b7-dee4397436ad | -8.7033 | -66.9721 | 2024-09-27 01:05:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 6b399bea-cb59-3eec-b403-15a04a1e5294 | -8.7034 | -66.9536 | 2024-09-27 01:05:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 26d50768-01ea-3541-8bc5-902f33fe769f | -8.7218 | -66.9716 | 2024-09-27 01:05:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 77267090-ec26-3298-8193-fd0df21172c1 | -8.7219 | -66.9531 | 2024-09-27 01:05:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| b5faeef7-6442-3f14-b5df-fd462bb84f36 | -8.8116 | -67.6917 | 2024-09-27 01:05:57 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 97.1 |
| d5732853-28d1-315f-afb3-d7e3cf4a962a | -8.8117 | -67.6732 | 2024-09-27 01:05:57 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 125.3 |
| 60d4fbbe-efba-3d3b-ab22-24a8ac51e6b2 | -8.9977 | -67.3909 | 2024-09-27 01:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 4d062db1-d014-3182-88c0-e162729af997 | -8.9978 | -67.3724 | 2024-09-27 01:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 163.7 |
| a3ecfc9f-2ec8-306e-aa7a-93775fa510d3 | -8.9978 | -67.3538 | 2024-09-27 01:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 8c321829-42d9-3fa5-a874-4aa8fcec5be4 | -9.0163 | -67.3719 | 2024-09-27 01:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 118.1 |
| e48a3180-a67e-3f11-bca4-f7b9a5df879a | -9.0163 | -67.3534 | 2024-09-27 01:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 74.8 |
| e0cacb94-dc27-3bac-b04d-a667afaa3214 | -9.047 | -61.3943 | 2024-09-27 01:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.9 |
| f0976951-dd8e-3376-a36f-b7598a6f9c1a | -9.0472 | -61.3752 | 2024-09-27 01:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 60401839-dc52-37db-a312-6c1af37284b1 | -9.0656 | -61.3934 | 2024-09-27 01:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 42e73b33-fba8-3ef6-a4f9-036a65c8edf6 | -9.0657 | -61.3743 | 2024-09-27 01:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 2bdab397-7601-31e7-8c58-e37ffdfb1b96 | -9.086 | -61.1245 | 2024-09-27 01:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.8 |
| acc1b4c0-7505-3334-9911-f74a1e75c588 | -9.107 | -67.8881 | 2024-09-27 01:05:59 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 4a2d113f-a487-3410-a608-cf2f493b5735 | -9.1255 | -67.8877 | 2024-09-27 01:05:59 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 66517b32-a602-36e2-a32d-0d8d23ecb260 | -9.3381 | -65.7255 | 2024-09-27 01:06:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.6 |
| e356daa0-4a78-349f-8fc1-005d6a03995a | -9.3763 | -65.5 | 2024-09-27 01:06:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 99b76f30-4ac0-3a43-8e36-50b6edda0e18 | -9.6018 | -50.1352 | 2024-09-27 01:06:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 31f96c1f-d286-3b33-9060-6dd5bccda4a9 | -10.3672 | -53.7858 | 2024-09-27 01:06:05 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 136.0 |
| c5f79152-1565-3edc-bb42-f2bc1c16e973 | -10.9076 | -54.2709 | 2024-09-27 01:06:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 83.1 |
| ce6a976b-a6e9-3c7a-9473-7d868f3ab25b | -10.9078 | -54.2504 | 2024-09-27 01:06:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 9494844d-306a-316c-9563-5bbd9a94a96e | -10.9264 | -54.2692 | 2024-09-27 01:06:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 291.3 |
| bf76c33f-4655-38f4-a7ed-ae31c503ff43 | -10.9267 | -54.2488 | 2024-09-27 01:06:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 352.4 |
| ed879030-18de-3b77-a9e2-f4ba897b4bf9 | -10.9453 | -54.2676 | 2024-09-27 01:06:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 106.0 |
| 6d6e324b-4ddc-3440-bcfc-5dead1065a83 | -10.9456 | -54.2471 | 2024-09-27 01:06:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 106.1 |
| 20e12fbf-cf33-3c6e-bdad-12ac56fe3b83 | -11.0379 | -51.4348 | 2024-09-27 01:06:09 | GOES-16 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 32d89204-6c4d-3f3b-a717-d5076ebc41f1 | -11.1219 | -50.8328 | 2024-09-27 01:06:09 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 0e59fb35-3417-31de-a8f9-ebf4fcd83777 | -11.5872 | -63.9596 | 2024-09-27 01:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 75.4 |
| d918fe1f-f9dc-34b5-bf41-3713a7e25dfb | -11.5874 | -63.9406 | 2024-09-27 01:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 1a2b96d8-913c-3a85-8eb8-f3dd455456c5 | -11.606 | -63.9587 | 2024-09-27 01:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 53.3 |
| f2fea1f3-a52a-319d-9470-bbc2cd7dccd8 | -12.844 | -54.0215 | 2024-09-27 01:06:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 95.8 |
| e059b68b-ee93-38b6-817f-36765322ab6b | -12.8628 | -54.0402 | 2024-09-27 01:06:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 132.4 |
| 33835472-0c48-353c-a8c2-8da557ed4761 | -12.8631 | -54.0195 | 2024-09-27 01:06:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 111.5 |


[Clique aqui para ver as próximas entradas](README21.md)
