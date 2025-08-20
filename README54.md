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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2334e515-7869-34ed-885e-a5d10a95a85d | -8.56438 | -66.94586 | 2025-08-20 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aa401881-365a-324d-a651-3a96b34312da | -8.56384 | -66.94935 | 2025-08-20 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 83d3163e-24a6-301e-ad1f-cdc50d4ec829 | -13.1393 | -57.15837 | 2025-08-20 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8aa8a419-1e66-36ae-998c-f284f1ced3e8 | -9.66378 | -66.25201 | 2025-08-20 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3012f4a0-d048-3a38-afd7-e740b17b4902 | -9.23915 | -59.60009 | 2025-08-20 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f890f7a2-2410-3ade-812c-6cf96afcb4e4 | -8.88049 | -62.39212 | 2025-08-20 05:50:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f1f3f0c5-858f-3fbb-a6c6-b437d6c23f5b | -8.56215 | -66.93835 | 2025-08-20 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 78a42708-64db-31e5-bf1f-4fb9c3124593 | -10.25269 | -64.48148 | 2025-08-20 05:50:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba524c0a-e0ce-37ca-9241-b1051f87afde | -12.97348 | -56.85278 | 2025-08-20 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6e796be3-8433-3a81-b5cc-f5ec7ce2b365 | -8.97303 | -69.27741 | 2025-08-20 05:50:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb20bec7-1098-33a2-99a6-d24dd172a2c2 | -10.1 | -68.45634 | 2025-08-20 05:50:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 41fe14e6-4193-3fdf-b395-9eb1a9b60218 | -9.6409 | -66.99669 | 2025-08-20 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5ff2fd41-8696-37ac-934c-c9687356f497 | -8.31693 | -70.07288 | 2025-08-20 05:50:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c53508dc-e3da-37de-b547-144110a05967 | -9.18803 | -59.63284 | 2025-08-20 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| d73c023e-7c78-33e5-a4c5-e87fa950f7fa | -8.5677 | -66.94638 | 2025-08-20 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 955fa9b4-73b2-3c09-8bd6-4326b37b6490 | -8.68922 | -62.09716 | 2025-08-20 05:50:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 715c45f6-0165-3acf-97c3-f1c87d8b79a4 | -7.78707 | -66.95928 | 2025-08-20 05:50:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ed3a06f-45c1-3b9b-aafe-9e059bdff082 | -9.17855 | -59.59116 | 2025-08-20 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ac8ac792-473f-3c05-bd7f-658be0f1aa1f | -9.8958 | -60.28298 | 2025-08-20 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a9e7f16f-32dc-36af-b58a-915fd5cf5833 | -9.51743 | -60.54155 | 2025-08-20 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4882fb07-3615-3e61-95a1-950919c5d9cf | -7.79092 | -66.95632 | 2025-08-20 05:50:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3d60c8f-7a26-3287-babb-6d62af31b4a8 | -14.61779 | -54.90508 | 2025-08-20 05:50:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| caf7388d-e1a7-3f9d-b2e7-3b9a72415bb2 | -12.97476 | -56.85751 | 2025-08-20 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 92d08bea-9f16-33b0-9ec4-eaf4308d3c2f | -8.92723 | -72.82417 | 2025-08-20 05:50:00 | NOAA-21 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 95a59781-99df-38e2-a291-6b662da38eda | -7.97033 | -55.29688 | 2025-08-20 05:50:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 759b51ab-671a-3a6b-832c-5fbf449c40a6 | -7.05003 | -59.22958 | 2025-08-20 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 00993acc-8e5e-32da-bd64-abd7d64e1735 | -12.98379 | -56.87403 | 2025-08-20 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dcabb165-fae6-3718-8f78-609857373887 | -13.14572 | -54.93771 | 2025-08-20 05:50:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 062ea388-68b1-3495-9fbd-8e0300ac1739 | -8.63656 | -67.26818 | 2025-08-20 05:50:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.1 |
| c3e06b45-f9de-3642-9060-ee1a13f28fea | -8.96658 | -60.49544 | 2025-08-20 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c0a062d6-1023-37fe-9e71-0147c8439ce1 | -8.88708 | -62.40424 | 2025-08-20 05:50:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b763133-618a-3754-925c-b4dd68d19f33 | -9.23419 | -59.59942 | 2025-08-20 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7dfbbefa-a131-33f4-9568-1e181a216fe0 | -8.56206 | -70.05962 | 2025-08-20 05:50:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3b4c7f3-a60e-3b9f-8e68-166a074b36a0 | -8.6371 | -67.26471 | 2025-08-20 05:50:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6bec089c-b8d3-3ab3-af07-b8e7b1205133 | -8.56555 | -70.06019 | 2025-08-20 05:50:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e7b2761f-8fbf-30fb-8f98-a6b9258773dc | -9.37502 | -63.50079 | 2025-08-20 05:50:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 883ab73c-4738-30ac-a449-58ae469fb572 | -9.2327 | -59.61074 | 2025-08-20 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 638909bc-1ffb-3aa5-936d-f594dfa3b05a | -12.22405 | -64.23268 | 2025-08-20 05:50:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8c08aae6-b287-3042-b3c3-304c92c98d1c | -8.34923 | -70.84965 | 2025-08-20 05:50:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3da604eb-ce0b-3af7-9d23-3bb019d58b70 | -11.74462 | -58.32654 | 2025-08-20 05:50:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dea659c8-9465-3e4c-af33-ab80fcbd27aa | -8.55775 | -66.94482 | 2025-08-20 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5547f6d1-d485-3148-90e0-d7b351ede8e2 | -9.18769 | -59.59826 | 2025-08-20 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5abb0773-e5da-333d-810f-50aa212be939 | -8.30301 | -70.74658 | 2025-08-20 05:50:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f49a42c-3861-3460-9d8b-4c6e4fb5165b | -12.22718 | -64.23799 | 2025-08-20 05:50:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d6495f1b-8a93-3843-a7e1-a2728e24e2ae | -13.1408 | -54.93211 | 2025-08-20 05:50:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| a8a5c1e3-b04a-300a-8682-92a3307ab412 | -10.25266 | -64.48276 | 2025-08-20 05:50:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 855754b7-d2d5-3754-8a40-817ef546a3f8 | -13.15337 | -54.93208 | 2025-08-20 05:50:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 8720c96f-d059-35b4-9c6f-9b4ea768c7ca | -8.88404 | -62.39637 | 2025-08-20 05:50:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 17b44012-eb1e-3077-9a39-862ae1b023f8 | -13.14919 | -54.91977 | 2025-08-20 05:50:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 4799f140-b0f1-32b0-84a8-21568e443189 | -8.63549 | -62.13165 | 2025-08-20 05:50:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f709e7e3-699b-31cb-8711-d6e429c71d90 | -10.90911 | -57.50102 | 2025-08-20 05:50:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7f5d6c6b-c2aa-38e4-a41e-0064f28d3fc3 | -8.30733 | -70.74295 | 2025-08-20 05:50:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| df4eb634-a8ec-3ddd-8dae-ab6b175f8178 | -13.14779 | -54.93305 | 2025-08-20 05:50:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| a26de7f9-da46-3602-9ec5-3c5f8298efca | -13.14708 | -54.93977 | 2025-08-20 05:50:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 15.8 |
| e5bf0ef4-afee-368d-b9b3-daa529c1d23f | -9.19788 | -59.63451 | 2025-08-20 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4742b575-34c4-3228-a0fc-135cf98d570d | -9.18693 | -59.60382 | 2025-08-20 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7328dfd5-1714-3162-9fcb-852a95abdef4 | -12.97293 | -56.85781 | 2025-08-20 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 89a9d464-620d-3e90-ac29-c9f5545c69d7 | -12.97647 | -56.88331 | 2025-08-20 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ee88ed4f-abce-3791-a820-bd5a8b53100d | -13.16106 | -54.94158 | 2025-08-20 05:50:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b28b821c-6f29-31c7-9a02-1ddda89c72d5 | -8.55498 | -66.94081 | 2025-08-20 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7d1a1157-1f92-3dcf-b28b-429f54bc6685 | -9.18647 | -59.6443 | 2025-08-20 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e427ce95-2b06-385c-ba31-0af03914204c | -9.19584 | -59.62283 | 2025-08-20 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 27e84240-05bf-350a-970d-85a1b7b52b4f | -10.44571 | -64.4148 | 2025-08-20 05:50:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c58a2257-491b-365f-a83e-286cec55959a | -12.97184 | -56.86779 | 2025-08-20 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c4117c71-b023-3956-beeb-8e6c4a080a56 | -10.249 | -64.48219 | 2025-08-20 05:50:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 08221b38-51ed-38ee-94b1-2a553d561b32 | -8.56619 | -70.05628 | 2025-08-20 05:50:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eba3b94e-5bbe-3e78-8a47-009a4cbb41e8 | -8.16406 | -70.76488 | 2025-08-20 05:50:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e65dbfaf-0581-3129-92e4-c4651ae2b190 | -9.17476 | -59.61928 | 2025-08-20 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1f96f5d7-5618-30af-bcea-8a5a794b01ac | -12.98434 | -56.8691 | 2025-08-20 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce108ae2-66b5-3ea6-82cc-e420ece5cff9 | -9.51525 | -60.54367 | 2025-08-20 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c6e7e480-c676-3df1-b95b-f0ca04a05593 | -9.73337 | -65.70328 | 2025-08-20 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b9170069-4cac-3ffd-982f-33d3bbd399ee | -12.96854 | -56.85661 | 2025-08-20 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c00c437a-7afb-35c4-952c-662e6a556231 | -9.17779 | -59.59678 | 2025-08-20 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 83bcebd9-f8c0-3fce-b6fd-7fa4f58d74e5 | -9.5172 | -60.52886 | 2025-08-20 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ea5484c3-bce0-32ad-ac3c-9ac9e9880d59 | -8.56493 | -66.94236 | 2025-08-20 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 901113f6-029f-3873-8dc4-2e72afc55631 | -8.05014 | -72.52271 | 2025-08-20 05:50:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e1987304-c46b-3364-97dc-fd3ba02aa360 | -9.21069 | -59.62489 | 2025-08-20 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 81d870a5-6689-3d09-9850-2bdf704cc5f5 | -13.15478 | -54.93404 | 2025-08-20 05:50:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d28ac166-1d1d-3b3f-932b-dc8fa285323a | -10.10056 | -68.45284 | 2025-08-20 05:50:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 590c00d8-8c27-3775-8c39-af3eab70573d | -13.15271 | -54.93869 | 2025-08-20 05:50:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 91f9134a-4d36-3405-a474-45d7b96ba5b8 | -9.21673 | -59.69423 | 2025-08-20 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| acbf1c08-dc34-301b-86f7-bec560913497 | -9.21011 | -59.61879 | 2025-08-20 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2faf97e3-3bb4-36dc-856f-34c9c6d1092a | -12.97304 | -56.87239 | 2025-08-20 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5cc71462-61d7-3b20-b427-6f44e48f452e | -8.8825 | -62.40724 | 2025-08-20 05:50:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b004d297-7ab9-3aa7-9161-d2e836b6a312 | -7.97047 | -55.30465 | 2025-08-20 05:50:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3002e9bb-6b29-3bc1-9c28-bc3ab8d933cc | -9.19217 | -59.63946 | 2025-08-20 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3ecdf588-c3dd-36d0-ab99-817c7c49a0a4 | -9.23693 | -59.61699 | 2025-08-20 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b02ae203-aaf3-329f-9ecc-a0dd19b2f333 | -10.18607 | -69.34296 | 2025-08-20 05:50:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 08bad3f4-9590-3780-87b5-8dae84102a2f | -13.15618 | -54.92077 | 2025-08-20 05:50:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 05baf613-400a-3281-bbc7-49ab7080f0e4 | -8.63379 | -67.26419 | 2025-08-20 05:50:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5302b85c-99be-3d1f-9f9d-4dbca4ca8a9c | -13.03652 | -56.85473 | 2025-08-20 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 92b58d02-68a3-3139-a583-fb696a093d78 | -8.69337 | -62.09778 | 2025-08-20 05:50:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 36b211ac-8c23-3296-86be-3ab49743e9c3 | -12.96797 | -56.8616 | 2025-08-20 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7514de54-852d-3b80-b044-20c1c9b84cc6 | -8.56053 | -66.94883 | 2025-08-20 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d7a28f08-410d-3a4f-84d3-7e8f32f574a1 | -13.14849 | -54.92643 | 2025-08-20 05:50:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 72c6c2d1-1d50-3a88-ab9c-99bd1362fd4e | -6.93474 | -62.88392 | 2025-08-20 05:50:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89a7e628-8959-36fd-bdff-1da952534f1d | -10.24534 | -64.48161 | 2025-08-20 05:50:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f2a36a16-4917-3a6f-afd5-274c902df65d | -12.97701 | -56.87833 | 2025-08-20 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 333831ad-e6ab-3bcf-a512-9c205305e79f | -8.56276 | -66.95634 | 2025-08-20 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a62e30df-fce2-358a-8ebe-1fc203a4540e | -13.15408 | -54.94063 | 2025-08-20 05:50:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README55.md)
