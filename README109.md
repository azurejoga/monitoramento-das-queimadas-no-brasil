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

## Dados Diários - Página 109

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dd377365-b69e-3e51-ad58-87f8de1bad8c | -6.76837 | -59.32403 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c3a4249c-40fe-3eb5-ab93-2dde278e53f0 | -6.76556 | -59.31995 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4f03bb4f-45f7-3bd4-9ab6-aca878db0176 | -6.765 | -59.32351 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3db5f067-4d80-314b-8c31-62530e33b9d1 | -6.76445 | -59.32706 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c4391751-62a2-355d-a00a-2c6da6806d85 | -6.76219 | -59.31943 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb12c5ea-f504-3a80-8f0a-fb69bc3225f9 | -6.76164 | -59.32299 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b0a8968-cfe2-3842-8d1e-caa6150b93e9 | -6.75883 | -59.31891 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e439dcc2-8dc9-3549-85cd-c8d5a7580b39 | -6.75607 | -59.3367 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec99332d-9e10-3d41-a2f6-f4dd2f9bcba3 | -6.75599 | -59.0906 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bafa3686-67fb-3acc-acdf-12eba26d6ec2 | -6.75491 | -59.32195 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 17dc4d81-7178-3545-a338-e6d8f19132bd | -6.75326 | -59.33262 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 954cd419-035b-366d-83b9-35612fa6de82 | -6.75271 | -59.33619 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e09dd57b-cbd4-31b9-a65f-f42d12e752b8 | -6.75155 | -59.32142 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5928af17-8540-3394-a611-e07c3b9cf133 | -6.751 | -59.32499 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 20c64dc3-5190-310e-b09a-7b0894c4dafe | -6.75045 | -59.32854 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 35529d5c-a062-314d-b1b4-231c8d89ddcf | -6.7499 | -59.33211 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| eab74975-1bd5-3a45-85d1-acc09e6c28f3 | -6.74934 | -59.33568 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e8442298-6aa2-3b88-9755-516218ad01c1 | -6.74818 | -59.3209 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 68017e90-5218-3717-ad21-9873a4fe650b | -6.74763 | -59.32446 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4390ce6d-4667-3c1b-8aa5-5c8d5945a63e | -6.74708 | -59.32803 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 94a787d7-cbc8-365d-ac80-6e0d7757acc8 | -6.74653 | -59.33159 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c4bf03e8-e7cb-3913-bb78-d23905eb7f09 | -6.74598 | -59.33516 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6c630dc7-8e22-39f1-a4a4-d12a798f712d | -6.74427 | -59.32394 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 9a3886fb-a59a-3a89-8159-aa43f12e5bb3 | -6.74372 | -59.3275 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| f7975f94-0e6f-3ce7-8328-247b1a2f7e66 | -6.74317 | -59.33107 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| b440ef8a-4be3-34f1-9c91-a3c4f2afa8ea | -6.74262 | -59.33463 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 50c5c82a-0dcc-3d64-8129-58c57e200e2c | -6.73858 | -59.29383 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 779eac79-9706-399a-93a7-ad5ccc665aa5 | -6.73803 | -59.2974 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b9c03718-c9c1-386c-9322-f818706e9b2d | -6.73748 | -59.30096 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1a8abcc7-cb18-3603-9666-36a2a750f042 | -6.73521 | -59.29332 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1797dcb9-1894-3efc-8e80-cc9ac0a2396c | -6.73466 | -59.29688 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 50aecad7-bfb4-3e85-a3df-d1c27d65f3ed | -7.40452 | -59.71619 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 43664b55-9bec-36de-b1b7-776d2a831e3b | -7.40173 | -59.71214 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8bf878b6-a896-30a7-b26a-5b06a9cd517f | -7.40118 | -59.71568 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 46b28aea-543a-3c5d-8eb5-40f259cdd0b6 | -7.40062 | -59.71921 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bf69ce2b-946d-318a-914e-4259c1bd60fd | -7.39448 | -59.71464 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12e0e23f-b463-30b6-88d0-5baea7d67bc8 | -7.36924 | -59.65635 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cac2cd1b-e063-398f-811f-ca87fb3696ee | -7.34825 | -59.74728 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4068e785-b368-3182-92b0-a40552b91d19 | -7.18619 | -59.76193 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc12a30c-0b0e-3b5b-92e9-d1766adffd84 | -7.11358 | -59.77613 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a23a55c-d1a3-3cc2-bc02-786ce87b8dbe | -7.11133 | -59.76858 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 015033fc-a003-3d37-8439-9e14444cbefc | -7.10465 | -59.76754 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b56b2f42-9444-3a2a-a2c0-d1a8437989a1 | -7.04641 | -59.26422 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1cd4b13-6503-3991-80f4-6f42b4066fbc | -7.03048 | -59.36806 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 62c4beae-3106-3496-91a6-742c47165064 | -7.02789 | -59.42971 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 704a7ad9-eb3c-3e4f-8f53-a0e589abacf7 | -7.02734 | -59.43327 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 78cbb685-7ee3-35fd-b9e3-714b4fbdc161 | -6.92364 | -59.7823 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed4238d3-9331-3e52-9bf5-3717316429f3 | -6.91975 | -59.78531 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 39033b0c-a4b4-3450-9fd3-5001caa18753 | -6.90918 | -59.78728 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08688f45-6c44-3514-b8e7-64db5445ca8b | -6.89643 | -59.80326 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f6ad7732-05d8-3b21-ab83-e8ce32ad4515 | -6.8948 | -59.81378 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a54e2b34-75f7-3c60-8187-1bf801b6f129 | -6.8931 | -59.80274 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 66fb2f1f-e6f0-3fe6-ba55-b7cfdf396662 | -6.89201 | -59.80975 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fda47669-b1f6-3fbc-99c7-36c59fe006d7 | -6.8336 | -59.59893 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d80b891c-e2f5-35f2-8642-2277c6c653e6 | -6.82773 | -59.70264 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d4097b22-aa52-3aad-a4d4-2fba2771422f | -6.824 | -59.37245 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d26059a3-37e7-3abf-9e48-e7c543578cf4 | -6.82246 | -60.12432 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b1716340-cfc5-365e-860f-de832a89a672 | -6.82192 | -60.12781 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 83e015be-183f-3729-a38b-17dab46f1a9b | -6.81995 | -59.70864 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 46985569-4a99-3c0a-bc2e-4f9a681de6ad | -6.81715 | -59.70461 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bfcd4733-5ac5-358c-9fe6-980b6155ae09 | -6.81661 | -59.70812 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2a8606ff-87f7-3ca0-ab72-fc1373d608a9 | -6.81473 | -60.13024 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aa1cab79-9f57-39a6-a258-554658e4a895 | -6.81194 | -60.12624 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 43ff9f13-9690-3a44-a1a3-709ab2834f38 | -6.8114 | -60.12972 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cd56b6ac-25d1-3b5a-a6d9-8d28cabf2abc | -6.81086 | -60.13315 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 40eaff5a-b3a0-3180-985a-5fc0d9a16601 | -6.80807 | -60.1292 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b321ea54-b8e8-3533-bb72-8d9277d327cf | -6.80484 | -60.11084 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21646975-826a-348a-bc46-3a50b9c1391b | -6.80206 | -60.10683 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 265fdfc3-10bf-3097-a40a-621c02b4e9b2 | -6.80151 | -60.11031 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9e2935f0-b883-3cb2-b76b-335994a5a3cc | -6.80097 | -60.11379 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63a05217-4978-3969-86ac-b32516d70eae | -6.79071 | -59.61027 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4886280e-fac6-3c95-980b-04b4fdf9d940 | -6.78736 | -59.60975 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 24f989dd-bd92-3027-9c1a-5f0abb2f9e47 | -6.77396 | -59.59704 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ab41c2c-e902-3ae9-92b6-7fbf4d9e8c2e | -6.76704 | -59.69677 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a8db2665-fd33-362d-8f70-23c9ce8bd9c7 | -6.76282 | -59.76807 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a594678-83d0-358b-b888-e150229cada6 | -6.76228 | -59.77159 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f8e4f9c-80f0-35b7-b4f4-84632690d4c7 | -6.75956 | -59.78909 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e00ebc59-d1f1-3292-addc-723e9df38749 | -6.75676 | -59.78506 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2803d697-2e58-3803-891a-7474c0c8939d | -6.74426 | -59.78685 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f9e0e82-81af-3895-9655-9386f33b9b5b | -6.74421 | -59.76529 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c54dc477-0f84-3550-9981-7c0bbd60211c | -6.74092 | -59.78632 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| dce3de1c-fca0-3054-a001-1eaa93b658bf | -6.74037 | -59.78982 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a5f475f0-21e9-3e76-adca-0550f08717b5 | -6.73978 | -59.77177 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 046d354a-03af-34cd-a528-768840d7126f | -6.73923 | -59.77528 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07b08b3d-24b9-3297-abef-6e58a9b6a025 | -6.7378 | -59.63114 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ad2dfc5-2879-3bd1-b316-a785c01fdd28 | -6.73649 | -59.79279 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| be714dee-75b1-366b-9561-8f4b4081e64e | -6.7351 | -59.67036 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0dca67c9-3123-320a-aaa8-2b814b2131bb | -6.73455 | -59.67387 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b9cb5833-a502-3e04-8fa0-5e1114aaeece | -6.73445 | -59.63063 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe694256-12ee-30ea-9c68-ea11c2aea053 | -6.7339 | -59.63415 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 91717048-d952-31bd-8f66-31f7dc6605e7 | -6.73286 | -59.66281 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 88371848-3ec7-37ab-b1ad-ec9fd2bb48e5 | -6.73121 | -59.67335 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3187bc24-04ad-3c02-9edc-a352c72d8938 | -6.73006 | -59.65878 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 16df2c67-9533-3f5f-ba9c-5fb73192ea41 | -6.72897 | -59.66579 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a6160f83-8886-38de-a3e8-10e533ed1e48 | -6.71193 | -59.75306 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99cccab4-7518-3c34-b17a-fcd192f97255 | -6.70498 | -59.46699 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eb34fd72-0cd9-33b0-a416-a1324ff687c0 | -6.7047 | -59.97395 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d7282ac-25b9-310b-9955-5f6c9448cc27 | -6.70416 | -59.75903 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f14a2470-0ef4-3989-9ac4-3b046706799f | -9.3494 | -60.57526 | 2024-10-12 05:23:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3459ac4f-f1c0-31db-9bdf-88e4d074f766 | -9.34885 | -60.57877 | 2024-10-12 05:23:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README110.md)
