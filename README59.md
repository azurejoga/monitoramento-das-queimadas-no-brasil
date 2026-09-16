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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f73984c7-40fc-3fb3-b1c0-6e3e8e9198cd | -8.88082 | -62.51572 | 2026-09-16 05:36:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5c3af60a-194b-34db-9602-91ed31201f25 | -8.37368 | -54.73119 | 2026-09-16 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3f0b599c-5f19-3a2d-94d0-22c94523385f | -6.75733 | -58.8111 | 2026-09-16 05:36:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 157ebb2a-bd49-3973-b52a-ea40b7fbc2fa | -9.25416 | -60.28135 | 2026-09-16 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0f2e79ef-11f6-3233-b1e6-f27729c00480 | -7.6514 | -67.17092 | 2026-09-16 05:36:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bf3dde09-d269-3681-815a-99063ed4665f | -9.05895 | -65.92924 | 2026-09-16 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 10636d75-1556-3f85-87b2-99882b97f19a | -6.69164 | -56.41594 | 2026-09-16 05:36:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be3e229c-f9f6-33f2-b5cc-6230d70f99ba | -9.49034 | -56.74723 | 2026-09-16 05:36:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ab3238ea-e1fa-31b4-9757-fe4e38ab3af2 | -10.40597 | -48.64171 | 2026-09-16 05:36:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 31c6f4d5-f252-3a80-b6f6-425672031198 | -9.05981 | -65.92411 | 2026-09-16 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2661bf95-1601-36c5-b2fa-b33000e41efd | -7.64901 | -67.16373 | 2026-09-16 05:36:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5f163186-85fe-3ddb-b602-8e8f4060cf1a | -10.89484 | -54.01778 | 2026-09-16 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 09c67e7f-cb8a-3de9-8a58-4f4b7858d706 | -10.65856 | -58.76381 | 2026-09-16 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 024b8535-b16a-3e58-99db-40ace50ffd9c | -10.14174 | -61.1815 | 2026-09-16 05:36:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a0964781-ab80-3afe-9d60-7c3456d0ad01 | -6.11834 | -59.88394 | 2026-09-16 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1c228ae4-bd24-3802-b229-cb680d479578 | -6.79506 | -58.79417 | 2026-09-16 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ec9d5c1-4de8-3d78-8698-444615e35aed | -6.13223 | -59.88254 | 2026-09-16 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2802ea38-f710-32a3-bc8a-22e6faec0db9 | -10.86609 | -50.81093 | 2026-09-16 05:36:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d4c678ca-5cd4-35da-a597-3a2eb9b6195a | -8.92523 | -62.37094 | 2026-09-16 05:36:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e01f8e37-1c5c-388e-b6cb-c78c3e0ccf90 | -10.13786 | -61.18446 | 2026-09-16 05:36:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 749a6a88-cd8c-3f97-9037-2c72edae1e97 | -9.1226 | -59.50888 | 2026-09-16 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 380b739d-6d66-320a-b382-703b1e2ced03 | -9.13679 | -65.8455 | 2026-09-16 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 636d8f56-7bae-3c27-8c68-3379e3a855fe | -9.04105 | -60.45827 | 2026-09-16 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 773acc85-83d0-30c1-9ae6-2c0535496ab1 | -9.0657 | -65.92717 | 2026-09-16 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 549acf22-9502-3d36-aed6-3c975045e9fd | -9.09442 | -61.02472 | 2026-09-16 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| cdc8c4c0-02f7-3d12-b5a3-da7d66c9fe4e | -6.34593 | -62.70391 | 2026-09-16 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a244d107-e5a6-3f89-91fd-b8977724a819 | -6.71376 | -58.80107 | 2026-09-16 05:36:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 637945a5-ce0e-3738-b185-7690461dffab | -6.91913 | -63.10973 | 2026-09-16 05:36:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f4c5ba0-e90b-3a73-879c-c1007a0e5e3c | -9.71424 | -64.97301 | 2026-09-16 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd0661c8-daec-3a18-b599-49fcc80369e0 | -6.33921 | -62.67942 | 2026-09-16 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 92e5b4a3-8bd0-3913-80c0-79964cb354b9 | -9.01735 | -61.01596 | 2026-09-16 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7cf070e6-4bb3-3175-9ff1-d2e5ba135bbe | -8.60145 | -64.10179 | 2026-09-16 05:36:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 64a9c85b-8d8c-329c-beb1-dd3e13099611 | -9.10137 | -65.9333 | 2026-09-16 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e26faa21-96cf-3813-9ec8-1e6de53bca7a | -7.65064 | -67.17521 | 2026-09-16 05:36:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dca3cd53-6878-37bd-aae6-7196e508b156 | -6.34777 | -62.69252 | 2026-09-16 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 570e9c73-4e1f-3888-8d1c-bedb53d248c9 | -8.36989 | -54.72626 | 2026-09-16 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d445b7d5-62d9-36b7-89ee-0ecee5bc960d | -11.97935 | -52.46466 | 2026-09-16 05:36:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f5c97ab9-0207-3ff7-9e41-b961355e29be | -6.77219 | -58.80581 | 2026-09-16 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bd1a3cb8-d01b-355c-9ed7-6c66691574a9 | -12.63025 | -50.76863 | 2026-09-16 05:36:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 17aeeb40-0d2d-3ef0-a957-35a251978ff7 | -8.36339 | -62.92797 | 2026-09-16 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2edb283f-73a8-3767-916c-a64dc1716f39 | -10.14507 | -61.18202 | 2026-09-16 05:36:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc3f9f41-8caa-3732-b07f-ac533932fbe6 | -6.13913 | -57.69481 | 2026-09-16 05:36:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| adfdd507-776e-3d4a-940f-303e8a7c5a0b | -9.12409 | -65.84859 | 2026-09-16 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b30b696b-8254-358a-814a-7b6efb8abdc3 | -6.93 | -63.13152 | 2026-09-16 05:36:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 59e0c055-ebe3-36cb-9bc3-1b8f51bc29e8 | -9.72547 | -64.90656 | 2026-09-16 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 0a00e815-7260-3188-b44c-b027163885a8 | -6.64729 | -59.96347 | 2026-09-16 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fac51b77-702c-3734-8baa-27c323029021 | -9.17437 | -65.60187 | 2026-09-16 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bdf6683d-fccb-33bb-8d5b-86e22f8cc994 | -6.8064 | -59.17126 | 2026-09-16 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 8a2aa313-feea-35bc-b44d-dc07597fcedb | -7.76547 | -61.35539 | 2026-09-16 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 913854c4-5b15-3438-918e-10d3b7cba7ca | -12.63079 | -50.76397 | 2026-09-16 05:36:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 8b715e44-8af1-34b2-b7b6-a6df3becc3e2 | -6.71662 | -58.80532 | 2026-09-16 05:36:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c6ed5c91-02aa-3ec4-abf4-58f2e45070c6 | -9.80818 | -67.55748 | 2026-09-16 05:36:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 29fce6a1-ccc5-3796-bf19-38ab2625d601 | -6.59156 | -59.90441 | 2026-09-16 05:36:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| cece81e8-978d-360d-a712-be1c9562a3ef | -6.11243 | -57.6784 | 2026-09-16 05:36:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ac639e56-e52a-374e-a623-3492c300f1c5 | -9.72991 | -64.90277 | 2026-09-16 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5fa481d0-96ab-305c-ac67-6e40b44219df | -9.8348 | -57.70076 | 2026-09-16 05:36:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ccb2835-0687-3384-9a7b-a2f0ddaa731b | -9.10445 | -65.9391 | 2026-09-16 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6240e2be-32fe-38f2-9e16-6988b397c10f | -11.18967 | -55.02465 | 2026-09-16 05:36:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a66ee330-fce0-35f7-bad4-b4810ec87569 | -6.3331 | -60.00333 | 2026-09-16 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2149f834-24ac-3c85-ac5f-690192426f2d | -9.72917 | -64.90719 | 2026-09-16 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| bf42d073-b09e-339f-bbf9-9e9baa7a351f | -6.71604 | -58.80901 | 2026-09-16 05:36:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0d3dc5dd-48f7-3a6b-a68e-0e32cdb20cd0 | -6.81262 | -59.17597 | 2026-09-16 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 68e269e9-2863-3c5c-8b34-24507ad453e2 | -6.76773 | -59.10622 | 2026-09-16 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 20987363-dff2-36bd-a156-8c3289fcfba1 | -9.36265 | -56.93729 | 2026-09-16 05:36:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9929ad25-4179-3e5c-98af-337081278804 | -10.9004 | -54.00944 | 2026-09-16 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ca601fe-96f5-346f-9a36-e71126773f66 | -9.0861 | -61.01263 | 2026-09-16 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f778fc2-02a9-3b0b-9710-2ae1d8cbc1e6 | -8.82751 | -62.47768 | 2026-09-16 05:36:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bde73831-c701-34d9-9385-0dd8276cc4fa | -7.80305 | -66.91754 | 2026-09-16 05:36:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 233b155a-2f9e-3f2a-bc4e-dab0feefed5b | -6.33044 | -62.68967 | 2026-09-16 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3a50304b-5791-33ad-acd9-1bcb4e49b6d8 | -6.75149 | -58.80696 | 2026-09-16 05:36:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1b4a3a90-d716-3df8-97f0-82c911ccf3b2 | -6.34654 | -62.70011 | 2026-09-16 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d5e061b-ad7f-35a2-8019-2d1aca355d7f | -9.39183 | -60.31384 | 2026-09-16 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 816525a4-aea6-37f4-8db0-bb03c418a6d6 | -11.26742 | -54.13379 | 2026-09-16 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a5d55032-f805-3597-956f-4ddb2a346642 | -9.05756 | -65.91324 | 2026-09-16 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cff253de-1cf4-34ec-b6e5-b32b534e9163 | -9.49279 | -56.75792 | 2026-09-16 05:36:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 36b8f6a2-607c-3c06-aa0b-03742d11818f | -12.1109 | -57.19531 | 2026-09-16 05:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 57a74ae1-c1d1-3562-a2a4-ccd2e8169c1c | -6.76819 | -58.80898 | 2026-09-16 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 324be552-7fb8-39d9-b8fc-3e34bfe1c277 | -7.65731 | -67.16315 | 2026-09-16 05:36:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d519899f-ffa9-3a3c-96c8-b8103e1fc0ea | -6.08838 | -57.85911 | 2026-09-16 05:36:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5b0a59a0-69b6-351b-a704-ead2efac063e | -9.39295 | -60.30671 | 2026-09-16 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 24ecd1db-5bd4-36e3-9214-49393a844141 | -7.65196 | -67.17305 | 2026-09-16 05:36:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 53e2559c-26f7-34a4-b592-d7e58ebc7540 | -10.93459 | -54.08326 | 2026-09-16 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b0c69e76-ffed-3a14-a932-41a158d8bbd7 | -6.76876 | -58.80526 | 2026-09-16 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bbdcd441-ea01-356f-b145-a7fe4e5cccde | -10.89555 | -54.01265 | 2026-09-16 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce5603a9-ef3f-3728-a9cb-e2875ccb105d | -9.09109 | -61.02419 | 2026-09-16 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7b1aab80-3c7b-34c2-9253-0d566ec1dedf | -10.88654 | -61.3907 | 2026-09-16 05:36:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9fb1f26d-a60c-3e10-886a-4378cb4685c6 | -6.34715 | -62.69632 | 2026-09-16 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 962fc177-cd2b-338b-9d1a-e352cc34b5be | -9.10048 | -65.93843 | 2026-09-16 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b8da2a21-c3f9-39b3-bac9-17533787b851 | -6.11354 | -57.69504 | 2026-09-16 05:36:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e4042823-7852-39ec-a2cb-74ac86b4b548 | -11.97893 | -52.46813 | 2026-09-16 05:36:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a41eed40-cbdc-3a2e-af3b-3388a42389c3 | -9.05499 | -65.92852 | 2026-09-16 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f634724f-6afe-3e6a-8e52-a59d857cec25 | -7.6115 | -57.6129 | 2026-09-16 05:36:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e64b07cd-0d98-37a8-ab12-87499262cf81 | -12.75522 | -52.83948 | 2026-09-16 05:36:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c4f081f3-e53a-3b00-ad2b-7f3d581d44eb | -8.37489 | -54.72268 | 2026-09-16 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 170984aa-55ec-3e66-9d86-2132cde19b41 | -6.78076 | -58.79574 | 2026-09-16 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c62902fe-65cd-3bfc-8241-26f58aa533c3 | -12.64299 | -50.7655 | 2026-09-16 05:36:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ad0d389f-fcb6-3610-97ae-89ec5570ff0b | -7.61224 | -67.24598 | 2026-09-16 05:36:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5ae256ab-5e31-380a-81f2-39647ceeb7c0 | -9.46984 | -63.44749 | 2026-09-16 05:36:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| efaf1ea4-38dd-3a59-848d-476b47bdaf0a | -9.70818 | -60.75184 | 2026-09-16 05:36:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2a26cd17-8913-38e6-918f-9b217ea86373 | -9.02123 | -61.013 | 2026-09-16 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README60.md)
