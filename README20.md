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
| df54b22b-3533-3225-8bf2-09c456c9be2e | -11.7698 | -50.070202 | 2026-09-23 00:36:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fccce374-ef26-3bdb-bec1-840f4d544148 | -5.4102 | -60.209801 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2d15e0d6-d4e5-3d60-8dbb-21379896bb28 | -12.7667 | -50.858398 | 2026-09-23 00:36:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2e2c5a42-efe8-3e4b-8772-17d5b2097604 | -6.7295 | -59.437 | 2026-09-23 00:36:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b346b065-2265-360b-a983-3038eb982e87 | -6.1103 | -57.662399 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 38ea3b42-86dc-3dfe-a643-b25cddfe569e | -8.145 | -49.553799 | 2026-09-23 00:36:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11197c0e-c4e3-3195-9312-3072d8072304 | -5.2205 | -60.0485 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 55f3f867-da09-34ea-bdb5-284369a2bc4d | -3.7343 | -59.421398 | 2026-09-23 00:36:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f18a1a57-187f-329a-bd0d-98432f644c3b | -6.1272 | -59.921501 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8f0bb497-74f7-3c8e-8ac1-db6186421d7f | -9.9546 | -53.9702 | 2026-09-23 00:36:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ed12e2ca-18e7-36c6-827b-b33bc489c471 | -9.9465 | -53.979801 | 2026-09-23 00:36:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9a993740-182b-31cb-ada2-27a482e5c959 | -5.2186 | -60.040199 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8a3375ee-90ee-3247-9ae4-ea8b8691f3f2 | -3.3318 | -59.830502 | 2026-09-23 00:36:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| aa20712a-e068-3369-abfe-35e92e16dbcd | -10.8682 | -50.1436 | 2026-09-23 00:36:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f2da3453-537b-32c3-9689-b72cf44caf56 | -4.6654 | -55.9165 | 2026-09-23 00:36:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 380c4953-3f99-3a8a-bf2c-7046f6b84a19 | -6.2907 | -57.732899 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4cf702d8-00a5-3a6f-a03c-ba8a560a8855 | -3.8166 | -58.869202 | 2026-09-23 00:36:00 | METOP-B | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fc9014a7-5e75-3dc1-89db-3a8cec54e3fe | -3.5434 | -59.074299 | 2026-09-23 00:36:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f8812f05-4d01-3c19-a0db-0459cff21104 | -2.8593 | -60.248001 | 2026-09-23 00:36:00 | METOP-B | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 280bf7a4-6b0d-32fc-b9e7-ef500994ab70 | -8.1781 | -54.815601 | 2026-09-23 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43c2f641-9cef-3e80-bbfb-f628d6f76292 | -3.6109 | -60.574902 | 2026-09-23 00:36:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c080086f-2d39-3edd-8324-283bac4970ef | -2.4584 | -57.9137 | 2026-09-23 00:36:00 | METOP-B | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cce14a2c-0ecd-3e93-bec7-30468c1aa8da | -3.4455 | -58.179199 | 2026-09-23 00:36:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 61a2c640-97ea-3c0f-842f-cc6e4f490851 | -6.4257 | -59.971901 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7a314144-63c6-37b5-a449-13691fc2f568 | -6.6101 | -59.9231 | 2026-09-23 00:36:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fe78fb91-f4e5-3e73-811c-f7bfe829edb7 | -3.8988 | -59.698002 | 2026-09-23 00:36:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0950b070-5809-3e77-a937-b33c0cc240af | 1.5667 | -55.880001 | 2026-09-23 00:36:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8c58ed58-e3dd-3307-a531-637aa50bb15a | -5.2752 | -60.203602 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dfaf2929-22cf-3d60-a4fa-d54044abd3c9 | -4.0421 | -58.9109 | 2026-09-23 00:36:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a8034b3c-5821-3726-aef1-1fab84dfa5dc | -11.1106 | -48.320301 | 2026-09-23 00:36:00 | METOP-B | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4331be23-ba9f-3b03-9e76-ed21f933b1e2 | 1.1713 | -60.363701 | 2026-09-23 00:36:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| fb6df466-4795-3123-b73b-4cd52d957081 | -6.4607 | -59.991001 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 206a63f4-33a2-3f37-98f6-90de5963109a | 2.8737 | -60.673698 | 2026-09-23 00:36:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| f202e393-7dd2-3ac4-964b-532a03a6765a | -7.0994 | -52.737999 | 2026-09-23 00:36:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99db4721-a81f-352e-a159-e6bad2cef8d8 | -12.4117 | -46.974201 | 2026-09-23 00:36:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e3e6e1a3-7117-3e8f-8d51-715651df75bf | -12.7878 | -50.903599 | 2026-09-23 00:36:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| dc4b1358-86b5-3a09-82f9-97cd14d95c81 | -9.71 | -58.128601 | 2026-09-23 00:36:00 | METOP-B | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7505e256-9f07-3b4e-9bcb-37793730af9b | -6.8826 | -59.855099 | 2026-09-23 00:36:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f0f78cfc-9314-319a-851e-0346846ddcba | -8.5879 | -54.623501 | 2026-09-23 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5f781f8-594f-33f9-9a0d-fcfa252f86c4 | -8.23 | -62.807598 | 2026-09-23 00:36:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f465c304-05f3-3236-9025-70fe1a034cc7 | -2.4066 | -58.278301 | 2026-09-23 00:36:00 | METOP-B | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a37c13da-f593-383d-a3c3-dd7f54770a7e | -10.7148 | -54.001301 | 2026-09-23 00:36:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1f7a5eed-fece-331b-adf3-9eaacdfe7b0f | -6.137 | -59.9193 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a0816d93-6c96-378f-a6f4-005cced30a76 | -7.876 | -61.181 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f5201706-3aaa-301e-b488-59fdbd768aeb | -3.7839 | -60.752602 | 2026-09-23 00:36:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dba764ff-9df3-39ee-b554-f1935bfdee4f | -6.4448 | -54.992699 | 2026-09-23 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85b14a86-67d3-3058-8e3d-eeae890de398 | -10.6085 | -53.987701 | 2026-09-23 00:36:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 08c4ad3c-41c1-36e7-b9c1-89ae855a2adc | -3.4698 | -59.527 | 2026-09-23 00:36:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 71b63266-2511-3ed8-96d1-86ac573128ed | -6.6775 | -58.5748 | 2026-09-23 00:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 062f98e3-98d4-33a1-a748-6678dbd25ff3 | -3.2314 | -46.9376 | 2026-09-23 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 247.2 |
| cd9779dd-8ed3-3691-b863-bff4dea9451b | -3.2313 | -46.9596 | 2026-09-23 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 127.5 |
| 56c80697-8342-379a-9b9e-21d223219c8c | -12.4216 | -46.9551 | 2026-09-23 00:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 01feb6dc-4fbf-3561-9f11-d274623f693c | -6.6315 | -43.7533 | 2026-09-23 00:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 4371e692-6677-3e8b-8890-2971dc978228 | -3.2579 | -53.9613 | 2026-09-23 00:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 79f8523c-755f-3a6b-a867-0a0bc8ecd14c | -6.6816 | -55.0502 | 2026-09-23 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 0d000802-473e-34a3-9384-39c998564cd2 | -8.9164 | -61.4958 | 2026-09-23 00:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 63.6 |
| be455afa-5e54-3e6a-bdd3-d47eb3df445d | -6.1289 | -57.7613 | 2026-09-23 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 00ed1bf7-222c-3cb5-b383-3cbb97fd9361 | -6.3105 | -43.9426 | 2026-09-23 00:40:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| ecb5323b-fe06-36de-89ce-b6ac7a452c11 | -11.6895 | -50.9406 | 2026-09-23 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 5b1e5718-f8c5-3c2c-a99f-3ee816747abe | -8.2062 | -54.7207 | 2026-09-23 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 075d4229-6876-31df-b3bb-8db55d4a7413 | -11.8675 | -45.788 | 2026-09-23 00:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 513f3b3f-b071-38fe-be63-b27967bad80e | -8.935 | -61.495 | 2026-09-23 00:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 9dc220b0-5424-3503-9f03-65c60b42e28e | -12.402 | -46.9804 | 2026-09-23 00:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 8b523376-7f85-38ca-a884-f7811fe7784b | -6.5939 | -43.7565 | 2026-09-23 00:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 255.5 |
| 5bd804f8-951c-3b46-950e-29d75c3a4ee8 | -7.8811 | -61.1779 | 2026-09-23 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 2dfb3cd8-82b8-3cda-83ad-a316eb583b11 | -6.728 | -59.423 | 2026-09-23 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 37.8 |
| c2fd032b-51f5-32c3-98a2-5542e7481b20 | -5.2475 | -48.1941 | 2026-09-23 00:40:00 | GOES-19 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 45.3 |
| a5dd86a3-0c93-3890-a9a8-f086180a2078 | -6.6148 | -59.908 | 2026-09-23 00:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 0665664a-7ad7-313a-850c-7712f22f431c | -6.5962 | -59.9279 | 2026-09-23 00:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 0cd5be21-1fdc-38f2-9c20-bb6fbbcbf1d3 | -6.6331 | -59.9265 | 2026-09-23 00:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 262f6f7f-6021-380a-8746-90f8de4d21bf | -8.4726 | -48.6927 | 2026-09-23 00:40:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 94.4 |
| ff4ea99e-d6c2-3860-8730-1a0437ebb210 | -4.0925 | -62.0874 | 2026-09-23 00:40:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 0dd403d5-9ff2-32d3-951e-2a750f813dc1 | -4.4488 | -55.0662 | 2026-09-23 00:40:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 3a82b437-f9d2-3ec3-8d07-cc055ce3b70a | -8.4538 | -48.6944 | 2026-09-23 00:40:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 101.8 |
| c6d9ce9d-b05a-3c69-a679-841c39ca24b4 | -5.7567 | -45.1067 | 2026-09-23 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 128.7 |
| 9ad24d10-0be2-35f1-aa3a-a5c652e7d21b | -6.6815 | -55.0703 | 2026-09-23 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 3c95f6d9-9dc5-329a-99d9-757e1de9e970 | -12.4212 | -46.9777 | 2026-09-23 00:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 136.2 |
| cb342c7e-ec56-33bb-8769-b2daa0cdce0e | -3.6947 | -60.5455 | 2026-09-23 00:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 42.0 |
| a041ab85-d363-3f29-9c39-6c35b76d0341 | -11.7082 | -50.9598 | 2026-09-23 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 111.7 |
| f4a98890-8b2f-3b06-aa72-0f27b2e7e2c0 | -6.5941 | -43.7333 | 2026-09-23 00:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 200.2 |
| 9b2b1dbc-b395-3053-a79b-fb2a2b558c5d | -10.2604 | -50.2196 | 2026-09-23 00:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 9937633a-ccb3-38a3-bd2c-923dbffce41f | -8.1876 | -54.7219 | 2026-09-23 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 2dc5667d-9aa4-374c-953d-63d357fbae78 | -8.791 | -60.8127 | 2026-09-23 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.6 |
| deec608c-1d3d-3a7f-82f4-7f8b7a0a9afb | -6.6127 | -43.7549 | 2026-09-23 00:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 658.4 |
| d0e3804a-0c50-3739-9da9-5794a3321cd9 | -6.6129 | -43.7317 | 2026-09-23 00:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 507.9 |
| f6fa90f7-ceb8-3063-bd1c-b1e527efdb02 | -11.8871 | -45.7623 | 2026-09-23 00:40:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 143.6 |
| b5b69c4e-a6d5-3518-bfe6-f01c7666fc5e | -7.0349 | -44.6625 | 2026-09-23 00:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 35.5 |
| e2b1b0b6-900c-37f5-92a9-13eeffe4e987 | -6.0925 | -57.6847 | 2026-09-23 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 31b25666-ed7a-3f35-a7f8-a5ba2f4a8bdf | -3.6946 | -60.5835 | 2026-09-23 00:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 74.4 |
| dc649b9d-c16d-3fd6-a56b-0cb6e5713981 | -10.6094 | -53.9902 | 2026-09-23 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 57ad2bd0-420e-3191-ab93-4d996e5a67cb | -6.6146 | -59.9272 | 2026-09-23 00:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 535f93df-458c-339d-b6f3-714634d5b7c5 | -6.3293 | -43.9411 | 2026-09-23 00:40:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 0d5c8e1a-5855-3104-9e8c-68f7b15cdd96 | -3.6947 | -60.5645 | 2026-09-23 00:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 965ee497-fd53-36b0-8119-ff15b824b59c | -8.9351 | -61.4759 | 2026-09-23 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 0f953c24-3a8a-353a-bfa9-458fb1f89ee3 | -5.3453 | -45.1576 | 2026-09-23 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 49126ac3-00da-3267-b35a-ac3aba6ed3cc | -8.9165 | -61.4767 | 2026-09-23 00:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 732f5686-899e-33f3-a3c5-b6b8af9dbc44 | -8.5982 | -54.6341 | 2026-09-23 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 05395939-2c8a-341c-8891-6f10ff8439a4 | -12.4024 | -46.9579 | 2026-09-23 00:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 64e5f13e-8119-32a1-99d4-10b9a5ea7c92 | -11.8867 | -45.7852 | 2026-09-23 00:40:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 181.9 |
| 73a28b36-111f-35a1-988c-70830ba1af43 | -5.7565 | -45.1293 | 2026-09-23 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |


[Clique aqui para ver as próximas entradas](README21.md)
