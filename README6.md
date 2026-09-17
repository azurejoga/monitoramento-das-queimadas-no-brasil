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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 098f7c56-a2ff-329e-85cd-989d12d15f41 | -9.2766 | -60.610298 | 2026-09-17 01:00:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1d8b4436-9942-3ecf-adeb-1bf0cdd0730d | -7.2998 | -64.658997 | 2026-09-17 01:00:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3d1405a3-b3f5-373c-bb73-fb45cfa1af2f | -12.4924 | -50.802601 | 2026-09-17 01:00:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9fba8db9-1095-37fe-b9f9-4bec9a1c43ff | -8.0953 | -61.8092 | 2026-09-17 01:00:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e76a544a-fccf-30e3-aa0b-0f1490e097e9 | -1.6015 | -55.5476 | 2026-09-17 01:00:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 489c0364-b7e1-3d98-86cf-9c42d4288ab7 | -3.1231 | -59.005798 | 2026-09-17 01:00:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7f55d809-fe4f-3a71-b307-cf6edffeee55 | -8.4773 | -57.6222 | 2026-09-17 01:00:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92ba3f2b-5331-3e56-aae2-afef81ce339a | -2.6969 | -57.6106 | 2026-09-17 01:00:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c9478e08-748b-305d-820a-5739b87a989c | -9.5933 | -60.507 | 2026-09-17 01:00:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f69223d6-8a06-36b1-828f-20b2a29134c2 | -10.8737 | -61.381302 | 2026-09-17 01:00:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9118789f-385b-3b5c-9b18-f55acf3ca084 | -2.4543 | -54.647301 | 2026-09-17 01:00:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0343d2a3-3495-3bad-990e-5020385871e9 | -6.3608 | -58.266998 | 2026-09-17 01:00:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 37ee569e-ec15-34ce-bbf2-220abdb172d5 | -9.1654 | -66.0224 | 2026-09-17 01:00:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1484f190-3848-312d-be0f-38e324446d00 | -8.2287 | -61.487598 | 2026-09-17 01:00:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 22b93338-054d-3925-b5e1-4a21180364d8 | -9.1105 | -65.909302 | 2026-09-17 01:00:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 19756020-7205-34aa-9621-76b105cbf8a9 | -8.0938 | -61.8022 | 2026-09-17 01:00:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2f557d5b-316a-336f-8e7f-71e9d212f058 | -9.075 | -60.992699 | 2026-09-17 01:00:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7899814e-bba7-3031-b52f-451d4a718975 | -9.0996 | -60.964901 | 2026-09-17 01:00:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 94a83dfc-0060-3461-8e09-a2cc96c9ca70 | -10.8293 | -54.064201 | 2026-09-17 01:00:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b401f3ae-1f8e-3eb9-ac56-0d41f2ceb8cf | -9.1007 | -65.9114 | 2026-09-17 01:00:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f028c0bd-4ad4-3f4d-9d2a-a4836f7bda92 | -12.502 | -50.7999 | 2026-09-17 01:00:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c1f1b9e2-492f-3d43-91db-1f8daa7564e8 | -9.3885 | -60.287998 | 2026-09-17 01:00:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ad0d6808-d438-3c78-8eba-b8d0dd8c2e36 | -9.0964 | -60.950802 | 2026-09-17 01:00:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5959b5fb-acd6-3008-b070-d4c1438d88d9 | -9.4053 | -62.691101 | 2026-09-17 01:00:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| eb3bfeb2-f7fa-326a-8c68-a8b9143ecdcc | -13.3828 | -57.015701 | 2026-09-17 01:00:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 28a74dae-a6c4-30ca-b3bb-e12191fb08d3 | -3.1253 | -59.015301 | 2026-09-17 01:00:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c554c197-4588-36a9-8365-609f2e84a597 | -7.062 | -63.032101 | 2026-09-17 01:00:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9c976460-c1b3-3e94-b85b-6a3e4a80d79b | -9.4068 | -62.698101 | 2026-09-17 01:00:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 05feab79-377d-3137-a8b0-e2bd0b66fbae | -1.5976 | -55.530499 | 2026-09-17 01:00:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4061edb-3a0d-340f-b290-c0f49321acff | -8.4871 | -57.6199 | 2026-09-17 01:00:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee13ee1a-dcbe-3037-8df9-46062578e49d | -8.149 | -64.034203 | 2026-09-17 01:00:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 39fdb57b-1173-3d88-b256-aaa1becd533d | -10.8721 | -61.374298 | 2026-09-17 01:00:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6be43933-9cf4-3904-8dc7-93b18f879899 | -6.9319 | -63.002998 | 2026-09-17 01:00:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| de9262e2-460f-3312-b95a-391459086f6f | -12.4828 | -50.805302 | 2026-09-17 01:00:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3ef85525-d97e-32ec-9aa8-d26c9a729b17 | -13.3709 | -57.0089 | 2026-09-17 01:00:00 | METOP-B | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c767abe2-0d43-3af8-850a-92073d3d450a | -9.1062 | -60.948502 | 2026-09-17 01:00:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 728e7d1b-ffc3-3251-928b-24ef76537a3e | -6.81 | -59.174198 | 2026-09-17 01:00:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1293a43f-14be-3f9b-bfbd-c97779376902 | -6.3631 | -58.276501 | 2026-09-17 01:00:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2b67bdad-6c46-3fff-b323-6b43433099aa | -9.4099 | -60.3367 | 2026-09-17 01:00:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 95e18bc6-ab43-33ce-9e34-e58a85340873 | -6.808 | -59.165699 | 2026-09-17 01:00:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2face5fd-7323-3bb3-b4df-d09f6bff9817 | -2.6817 | -57.589199 | 2026-09-17 01:00:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d5c1fc87-f7d3-341e-87ff-f0f2e416f14b | -9.3455 | -65.906799 | 2026-09-17 01:00:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a00a30c2-0261-35a9-a45c-8845f0a9f9be | -9.2831 | -60.5937 | 2026-09-17 01:00:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 43b9b7c4-2372-3aaf-816e-d558c0300e4d | -8.8727 | -62.3801 | 2026-09-17 01:00:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 30a07649-de84-37a7-9435-01cb8e71b0e2 | -12.47 | -50.7575 | 2026-09-17 01:00:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2080cf66-3c1f-3d64-8994-4e9ea8ea54bf | -9.3787 | -60.290298 | 2026-09-17 01:00:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bac10f0b-b5b0-3219-be1d-9effafac5e3a | -6.8061 | -59.1572 | 2026-09-17 01:00:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| da931fd0-2e3d-36a2-98c3-9b0a4f1c54e0 | -13.3687 | -56.999599 | 2026-09-17 01:00:00 | METOP-B | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a8de0149-40a5-342c-88c2-00c6e3487109 | -8.4895 | -57.6297 | 2026-09-17 01:00:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 848ca4bc-a615-3447-8ed6-4965beceb23d | -9.2961 | -60.515202 | 2026-09-17 01:00:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 197996e1-1449-3a90-970d-1149d971ae94 | -10.5755 | -57.677299 | 2026-09-17 01:00:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a8580615-c6fb-31f3-9b0e-ee3fd65ce1e3 | -14.8361 | -59.526798 | 2026-09-17 01:00:00 | METOP-B | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8f7ef365-72a8-344e-adfc-b09ccd6eb5db | -6.8957 | -59.010601 | 2026-09-17 01:00:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d0f2cc55-19ec-39e4-977b-db1c7083dde3 | -9.0387 | -63.358601 | 2026-09-17 01:00:00 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a71ba478-232c-3861-ad0a-3f4439b14fb7 | -13.3806 | -57.0065 | 2026-09-17 01:00:00 | METOP-B | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fe387460-bd34-3183-945f-2a42854cc8a4 | -13.3784 | -56.9972 | 2026-09-17 01:00:00 | METOP-B | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 55c9bbb9-aac5-3ece-99a8-e89a655e7c6a | -2.7457 | -57.5994 | 2026-09-17 01:00:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4228a29a-75a5-3dd2-9ae9-dc9b05b65599 | -5.1432 | -55.9091 | 2026-09-17 01:00:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dabf65b2-f404-3c7d-9db8-86f084cda347 | -7.528 | -63.366699 | 2026-09-17 01:00:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4c6fd122-da05-346c-bad4-c55aad6e5f70 | -9.2864 | -60.608002 | 2026-09-17 01:00:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5bbb7e82-62c2-3948-b484-4f299971d3cd | -10.7052 | -53.981201 | 2026-09-17 01:00:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4f184085-21c1-3eba-ab9c-edafb98ec99e | -12.0986 | -57.177101 | 2026-09-17 01:00:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7e910d7c-3c3b-3da6-b59b-4725835ed8f6 | -7.5264 | -63.359699 | 2026-09-17 01:00:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9a8db3d0-0dcb-3e1a-b709-825d14236d0c | -9.2782 | -60.617401 | 2026-09-17 01:00:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9a1fc72e-0973-3257-bab7-d03ffc642dc6 | -9.0912 | -61.0187 | 2026-09-17 01:00:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1ebdd5cf-194e-3d84-b2ba-bba1bc062fd8 | -10.8212 | -64.997002 | 2026-09-17 01:00:00 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4edd3128-a09e-3df3-9734-767bd6e3ca59 | -9.0734 | -60.985699 | 2026-09-17 01:00:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8f50d009-4f22-36dc-b662-e6bad3e44f8e | -2.6845 | -57.601101 | 2026-09-17 01:00:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 09649d22-3269-3afa-bc36-f604d034a628 | -11.1888 | -55.009499 | 2026-09-17 01:00:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b8d76164-cea5-336b-8c87-4dd9541c1d83 | -8.0922 | -61.7953 | 2026-09-17 01:00:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| da8d88be-06ca-36ae-9eae-19800496b000 | -6.8198 | -59.171902 | 2026-09-17 01:00:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 339ed20c-2845-3edd-a51a-48b2356ea76c | -10.5733 | -57.668201 | 2026-09-17 01:00:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f3e5aa8d-8f0e-348c-b252-0065d59f115d | -10.8331 | -54.079498 | 2026-09-17 01:00:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 50f082ea-7189-3eb2-909f-c2a74d87af5c | -9.7663 | -60.4519 | 2026-09-17 01:00:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ba02c994-71fa-3a2b-a875-a8d015ec34c9 | -8.7553 | -66.547501 | 2026-09-17 01:00:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 97245c9b-c196-3ca8-a2b8-f69fd6763b00 | -3.4659 | -54.684601 | 2026-09-17 01:00:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b62ff37f-dc46-3c54-9422-5afa1a878d2b | -4.4946 | -54.957901 | 2026-09-17 01:00:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9836383b-5638-3dba-831e-c05df08df1f1 | -9.0636 | -60.987999 | 2026-09-17 01:00:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9b5e1038-2ca8-3f0a-900e-2162fe9f3029 | -12.4796 | -50.754799 | 2026-09-17 01:00:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ef0a7f36-4d60-3c27-b543-e904e083f395 | -8.8711 | -62.373199 | 2026-09-17 01:00:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cc90f5fe-292b-3af2-aecc-5e34f61e1dc5 | -10.7398 | -61.565102 | 2026-09-17 01:00:00 | METOP-B | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f3e233ef-38c8-3bdd-8084-11b234acab0a | -9.7549 | -60.446999 | 2026-09-17 01:00:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ad70cb23-8247-3412-9cb0-676286922540 | -3.4615 | -54.666302 | 2026-09-17 01:00:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64ee7bb4-a48a-39c9-9fae-0927b0510212 | -9.6193 | -61.805099 | 2026-09-17 01:00:00 | METOP-B | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 55c616c7-eafc-3ed4-a058-f2f56e50b529 | -9.0896 | -61.0116 | 2026-09-17 01:00:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 45d7dc9e-8cc4-3c38-8559-ee15081e6910 | -9.0864 | -60.997501 | 2026-09-17 01:00:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c219c389-de49-3790-91a2-51f3d230555b | -10.8234 | -54.082001 | 2026-09-17 01:00:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5a4fdf28-852f-3dc8-85ed-7c670e8ee32d | -9.0946 | -60.988201 | 2026-09-17 01:00:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| abe08cbe-7fb0-39ad-8bff-8f1cbcd8d83e | -6.7982 | -59.167999 | 2026-09-17 01:00:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0ad19248-c203-34bc-8be7-aeb28a4e85f7 | -2.8887 | -54.150501 | 2026-09-17 01:00:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29336ed3-88e1-3e99-b97d-3b0f6199a2c9 | -9.4379 | -60.368401 | 2026-09-17 01:00:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 926f2773-ba4a-3841-b439-0656f8e73b76 | -6.8178 | -59.163399 | 2026-09-17 01:00:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cd84c6ef-e360-3f75-89e6-4a84ab474946 | -8.8825 | -62.377899 | 2026-09-17 01:00:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b323eb4a-0cab-3076-bb15-56546cceb885 | -12.4987 | -50.826401 | 2026-09-17 01:00:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 670b0bfb-6806-3940-b4e9-91cd3921e335 | -6.8997 | -59.027699 | 2026-09-17 01:00:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d7fbf78b-ae28-37ad-bbd6-e75eba8998ee | -1.5879 | -55.532799 | 2026-09-17 01:00:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4da8d7b5-b0ed-3025-b418-cf7d1a3bbc32 | -9.2733 | -60.596001 | 2026-09-17 01:00:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4f95554e-a36b-361d-a5cb-574f38d5e284 | -8.6337 | -66.552902 | 2026-09-17 01:00:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7fde08f1-cc2b-3d08-b183-14f266873de7 | -10.5179 | -57.435101 | 2026-09-17 01:00:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1095e51d-b698-3424-8e6c-65f5cd89dd1b | -2.6872 | -57.6129 | 2026-09-17 01:00:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README7.md)
