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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1c4f2645-2914-3afc-ba4e-c65ed9d9873a | -3.51767 | -54.66048 | 2024-10-14 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a66d8c9a-3395-3de7-8c2e-e284278ea6ab | -3.5169 | -54.66536 | 2024-10-14 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bca3eb60-04bc-37c6-b609-49ae843d0a80 | -3.513 | -54.66474 | 2024-10-14 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8d7c80a3-02e5-365d-9a4b-8d17cfe26ae6 | -3.48282 | -54.15453 | 2024-10-14 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 59b28775-b904-3696-8db4-f65e71620234 | -3.48208 | -54.15914 | 2024-10-14 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5648f9d6-b234-3315-9db1-048cd92e7058 | -3.42842 | -54.17891 | 2024-10-14 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6020f170-013b-316a-a287-f642cb4905e7 | -4.51362 | -54.86327 | 2024-10-14 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2e87b2c9-e2ae-3a3c-ae53-a2b0736b3105 | -4.49765 | -54.9604 | 2024-10-14 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 09265403-e16b-3c66-b2a3-447b2cbcb928 | -4.49685 | -54.96525 | 2024-10-14 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 82e5c610-4463-30b3-a2e9-aca23e44b69b | -4.49256 | -54.86995 | 2024-10-14 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 41f67cd3-3f60-3a97-9b0b-486a4ffe12ac | -4.46305 | -55.07223 | 2024-10-14 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9d2f2fe4-d4c9-3152-8479-7560fe2128c3 | -4.45912 | -55.07157 | 2024-10-14 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fe54d942-bb87-3c0d-8b2d-d20bad0c49c1 | -4.45141 | -55.00211 | 2024-10-14 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a80c5f45-7bc9-35f5-8bfd-6c4d276a6a04 | -4.43886 | -54.97999 | 2024-10-14 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 55c1b2f4-97a0-34db-88e7-175ba82c9221 | -4.4106 | -54.98061 | 2024-10-14 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42486dd3-d8b0-382b-b671-110e1152ab8b | -4.40667 | -54.98003 | 2024-10-14 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 83993391-0663-3582-869a-2fdf3dc11d4f | -4.36512 | -54.96342 | 2024-10-14 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c0364a5b-dab0-346d-996f-57bad0e1ae4e | -4.36068 | -55.13716 | 2024-10-14 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| d80f6c65-c69f-3a00-94fd-9474de513c6b | -2.6119 | -49.0772 | 2024-10-14 04:45:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 555091d7-ebf7-36d4-8513-eddf561788b8 | -2.6118 | -49.0985 | 2024-10-14 04:45:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 795be906-f201-3de4-854e-ce7ea32d433a | -3.2889 | -42.8561 | 2024-10-14 04:45:22 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 6c5b59f4-49b9-3c22-80af-256eb2bc6672 | -3.3077 | -42.8318 | 2024-10-14 04:45:22 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 198.9 |
| d0e20095-b973-3363-b8aa-af82d93947b5 | -3.3076 | -42.8553 | 2024-10-14 04:45:22 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| d9da757e-5743-313c-9015-8b96798a4a6d | -3.289 | -42.8327 | 2024-10-14 04:45:22 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 126532fd-a373-3e99-9099-3e2df8475b1e | -3.9103 | -48.3466 | 2024-10-14 04:45:26 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 96e99bf8-30b5-35b5-a152-d920d9789ce9 | -4.1148 | -48.2515 | 2024-10-14 04:45:27 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| db1b7270-2d81-3212-b708-ea736bed659e | -4.1149 | -48.2299 | 2024-10-14 04:45:27 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 3c701610-fe38-33d1-803e-a01bea4d2b2b | -7.9418 | -63.6365 | 2024-10-14 04:45:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| a6000d89-4fe4-3dcf-be33-6d28fbd3587a | -7.9419 | -63.6177 | 2024-10-14 04:45:49 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 6b10e9b9-d14c-33f8-8318-c0b058d8d192 | -9.1043 | -61.162 | 2024-10-14 04:45:56 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 69b66f86-212d-31b3-b9d7-28c1405443ee | -10.0813 | -44.2366 | 2024-10-14 04:46:00 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 290211e0-3cc3-331d-a4f5-64ee98f3139a | -10.0809 | -44.2599 | 2024-10-14 04:46:00 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 03bf7bd9-ba58-3ecc-8acb-5c3ca04675fc | -10.0622 | -44.2391 | 2024-10-14 04:46:00 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 103.2 |
| df976be7-47de-323b-91e9-95a33b7219a0 | -10.0619 | -44.2624 | 2024-10-14 04:46:00 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 159.3 |
| e394e814-e7c2-3b5a-be79-0c8596a2e5b9 | -10.65377 | -56.05367 | 2024-10-14 04:46:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a700c6e-f64e-3b6e-a93d-5eee77a30606 | -10.1196 | -55.18016 | 2024-10-14 04:46:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7523bc74-d9bc-3420-a9e5-780f554e270e | -10.11453 | -55.21048 | 2024-10-14 04:46:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aa577d4c-0322-32c9-b56c-bc4e41711cb2 | -10.11303 | -55.19684 | 2024-10-14 04:46:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ce38ef0-7b0c-3662-bfd5-02524218e252 | -10.11231 | -55.20118 | 2024-10-14 04:46:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1cb16a8c-dd66-34c2-8f49-456d25a7804a | -10.10936 | -55.19621 | 2024-10-14 04:46:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c09872b-12eb-31f8-a161-0465c60a69f3 | -10.10864 | -55.20053 | 2024-10-14 04:46:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4359695d-4c98-3a10-9ab7-9c38636a8b74 | -10.10497 | -55.19989 | 2024-10-14 04:46:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa2a8a7c-adb5-3ca3-8f88-7b7f696b47f2 | -10.10424 | -55.20423 | 2024-10-14 04:46:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b3e4b2f-5911-3ddf-ac0c-a40386f87a59 | -9.98112 | -55.18072 | 2024-10-14 04:46:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26230d56-04bf-3368-a09d-386766d85ada | -9.92227 | -55.39306 | 2024-10-14 04:46:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e7f8745b-00e0-3e5c-9c8e-217fc3076b5a | -9.75966 | -55.34531 | 2024-10-14 04:46:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 78191f79-906e-360d-8a55-dbbfe639bd09 | -9.75891 | -55.34975 | 2024-10-14 04:46:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f72da629-8c72-383f-8c1e-f5ee78d536de | -9.7552 | -55.34909 | 2024-10-14 04:46:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c709cbea-efec-3717-91ab-b25a7c90cc84 | -14.45731 | -56.83723 | 2024-10-14 04:46:00 | NPP-375D | ARENÁPOLIS | MATO GROSSO | Brasil | 5101308 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b9f7eafa-c45a-3014-ab27-7312a4945e29 | -9.8971 | -58.13609 | 2024-10-14 04:46:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5baa7403-d5fe-36f0-b139-e8a3e6b7f663 | -9.89347 | -58.13083 | 2024-10-14 04:46:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e916175f-a07a-3427-ada7-4172b27052f8 | -9.89268 | -58.13524 | 2024-10-14 04:46:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 327c0af7-9e78-3b7f-a8da-e9e242faa526 | -9.70525 | -56.64893 | 2024-10-14 04:46:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| a826e7fd-67f7-3202-893b-750cbe03f5b4 | -9.10849 | -61.17415 | 2024-10-14 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 013bbf32-62b0-3b96-86ac-c3a9e8c27f2c | -9.10839 | -61.17377 | 2024-10-14 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 27716fd0-8e1d-3a3b-addc-e769c029a647 | -9.10783 | -61.17777 | 2024-10-14 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ef84464-9819-3dcb-882a-ed4fb233ded9 | -9.10771 | -61.17738 | 2024-10-14 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 244f82c9-17d2-3033-ac96-fbfecd4f5563 | -9.10433 | -61.1658 | 2024-10-14 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 19b94cfe-aa5b-33bf-a539-2ec786f8048b | -9.10427 | -61.16545 | 2024-10-14 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ab3bf6a-7ad4-334d-9a20-51d64e3e89ff | -9.10367 | -61.16941 | 2024-10-14 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d84272e-ff63-3db2-8590-b7e2ac59592f | -9.1036 | -61.16904 | 2024-10-14 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 07f02051-e84a-3c86-8b8b-9e7aec561358 | -9.10302 | -61.17302 | 2024-10-14 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b23597e-9375-3da2-923b-f15e7f135fb3 | -9.10292 | -61.17264 | 2024-10-14 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 681e86df-8b6f-3668-86d8-5c9f14d9ff24 | -9.10236 | -61.17664 | 2024-10-14 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 51ecd427-fcf0-3d28-90ed-0a81ce8beec2 | -9.10223 | -61.17625 | 2024-10-14 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 82caf411-df6d-331b-89f5-fb2f3b44aed4 | -9.09688 | -61.17553 | 2024-10-14 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 498a431c-3060-39d3-acb7-f1d47cf2241d | -9.09676 | -61.17517 | 2024-10-14 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7ba9bee8-e383-3ee7-983a-192ce6d601ce | -9.0914 | -61.17448 | 2024-10-14 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1574839a-060e-3be9-86e4-8b931d05b5d4 | -9.08591 | -61.17343 | 2024-10-14 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 914c466d-b056-35d7-9918-e870060107ba | -7.95478 | -63.63524 | 2024-10-14 04:46:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| af75530f-6276-3c88-89b1-6684422aa34f | -7.94933 | -63.6284 | 2024-10-14 04:46:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cd372648-6ccf-3cac-af64-389b1e5bf1b8 | -7.94827 | -63.63398 | 2024-10-14 04:46:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8751e905-14b3-3ef7-b535-8694d6707468 | -7.94281 | -63.62717 | 2024-10-14 04:46:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ebfcbb34-b109-3995-bc35-d699db267993 | -7.94176 | -63.63268 | 2024-10-14 04:46:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4d086bd5-8eba-3cb7-a2f9-d39efb213bf3 | -14.68466 | -48.31303 | 2024-10-14 04:46:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| baaebedb-4288-3329-b2a9-9e51fd8f7493 | -15.57021 | -47.85595 | 2024-10-14 04:46:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 80480afe-1165-3daf-8330-57916ba150b4 | -11.92081 | -45.7744 | 2024-10-14 04:46:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bdbcaecd-bb6a-3876-a32d-eb4e1a29beae | -13.0673 | -48.88838 | 2024-10-14 04:46:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9341b1ac-50cd-38a3-a66e-5fdcf8fca1d9 | -14.55558 | -43.13396 | 2024-10-14 04:46:00 | NPP-375D | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8016efbb-d126-3252-882b-1e186d2c2b0a | -15.31804 | -41.89857 | 2024-10-14 04:46:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 47e6cf60-d39b-30e7-8a84-8e3d78c6c41f | -15.31207 | -41.89777 | 2024-10-14 04:46:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3a6fa342-93fb-3b69-8279-683276a7e9d5 | -12.10092 | -43.19597 | 2024-10-14 04:46:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 93ea97a0-b385-3951-9b26-c0b7a23eefd3 | -12.09729 | -43.18214 | 2024-10-14 04:46:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1d77a15c-af10-345a-9c28-1f1fb2cadc6f | -12.09684 | -43.18573 | 2024-10-14 04:46:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 10e27592-831d-3705-8f45-13f14c286c49 | -12.09641 | -43.18916 | 2024-10-14 04:46:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 05cea39c-674f-3534-97eb-11c7846b267d | -12.09522 | -43.19865 | 2024-10-14 04:46:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2de9e356-ad56-3515-8663-bd5a5a657a84 | -12.09118 | -43.18807 | 2024-10-14 04:46:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a3f394f4-04ae-32f6-9709-f6e3d201906f | -14.55011 | -43.13327 | 2024-10-14 04:46:00 | NPP-375D | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 100b62fe-a471-35e5-bb68-974cb47a199b | -11.49045 | -43.23284 | 2024-10-14 04:46:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2ccfb23e-8ced-3a11-83c3-22d57cdbabab | -11.48983 | -43.23286 | 2024-10-14 04:46:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8123cde5-5d1e-389d-a87c-41e824b43457 | -11.11074 | -43.33085 | 2024-10-14 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| d1230ede-b926-3cf7-915c-81ec04b3d1a9 | -11.11034 | -43.334 | 2024-10-14 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 02c99113-090f-3ad0-bfaf-37e162f44569 | -11.10993 | -43.33714 | 2024-10-14 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 6a3edc6b-a974-30ee-9bcb-5c594bdcf9cc | -11.10518 | -43.33331 | 2024-10-14 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 50adfb17-3e2e-3b05-82f0-d48fc384bc0f | -11.10478 | -43.33646 | 2024-10-14 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 387fa5b8-7ac8-3205-9ad0-d4a941275eae | -11.10438 | -43.33959 | 2024-10-14 04:46:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 12.3 |
| ea11b9e1-fade-374d-bbbf-4719aa95b281 | -12.11224 | -44.73036 | 2024-10-14 04:46:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e4cfb67d-47c2-3933-85e0-0c544a0eb0b0 | -11.89663 | -43.8867 | 2024-10-14 04:46:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 83cff8ba-58b5-3fab-bde3-b6e8fe498936 | -11.89588 | -43.89255 | 2024-10-14 04:46:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d9f568ed-93b9-36e8-81ed-5ad50a6c3e11 | -11.89161 | -43.88602 | 2024-10-14 04:46:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README88.md)
