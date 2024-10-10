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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 190fb6fc-daf4-36c0-928f-059893a3a767 | -4.4776 | -46.5956 | 2024-10-10 01:15:32 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 4a5c461b-f98f-3941-ba6c-10cbc5f74205 | -5.9036 | -45.4127 | 2024-10-10 01:15:40 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| a7bdddc5-02d3-309d-9bc0-7b5374b1a6c9 | -5.9223 | -45.4114 | 2024-10-10 01:15:40 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 8214a4e4-0365-37ce-99c3-ab7050f322c5 | -6.5218 | -60.0649 | 2024-10-10 01:15:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 1f043631-ba6f-3ac1-b738-7df69013196c | -6.747 | -59.3259 | 2024-10-10 01:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 5c0061ab-4db3-304e-9556-acc1d5503a38 | -6.7654 | -59.3252 | 2024-10-10 01:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 124.5 |
| e2e6eece-76e7-3cf7-ab56-b995e5123d05 | -6.7655 | -59.3059 | 2024-10-10 01:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.7 |
| f5f27d6c-c3e1-3c4a-a7a4-b144a700d904 | -6.7798 | -60.0552 | 2024-10-10 01:15:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 38.3 |
| 5b970328-c809-373d-9212-a2ec4fefe8a2 | -6.7839 | -59.3245 | 2024-10-10 01:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 112.2 |
| dae0bb95-8e20-3d1f-ab01-a87697e9ac6d | -6.784 | -59.3052 | 2024-10-10 01:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 1383a889-da05-3c71-a9ad-8040eb0ddb92 | -7.1346 | -59.3099 | 2024-10-10 01:15:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 45f752d1-dd54-3419-bdd0-67b9b9cac830 | -8.2325 | -61.1823 | 2024-10-10 01:15:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 1b30c49f-4dbb-3685-865c-c9e43446ce31 | -8.6843 | -63.1009 | 2024-10-10 01:15:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 50.9 |
| fe9752c2-9149-3e9a-8b40-12f558fdb1d5 | -8.6844 | -63.082 | 2024-10-10 01:15:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 54.7 |
| ad8b38f1-17f4-3754-9cb8-7a9e6dce9952 | -8.7028 | -63.1002 | 2024-10-10 01:15:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 48.9 |
| a4364a8a-1c83-3e47-9e2f-bd8f20cc5d1f | -8.7029 | -63.0813 | 2024-10-10 01:15:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 9e12a8c9-8593-3c14-a3a3-340d17a8fcbe | -8.9111 | -62.353 | 2024-10-10 01:15:57 | GOES-16 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 58.6 |
| c9b2ccf6-bcfd-3649-8873-45a9ff143dee | -8.9898 | -61.6261 | 2024-10-10 01:15:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 4f1dbe70-d322-3414-961f-cc8880810612 | -8.9899 | -61.607 | 2024-10-10 01:15:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 16d95da5-6828-3a82-8d00-a2b5b28c6d4c | -9.0084 | -61.6253 | 2024-10-10 01:15:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 296daf41-9091-3281-adb9-bd364b07e105 | -9.0085 | -61.6062 | 2024-10-10 01:15:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 51.3 |
| a05bd82f-7f94-314c-ae29-ba3aee454349 | -9.027 | -61.6244 | 2024-10-10 01:15:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 6401122c-b13e-3bcc-9144-4899e350d2cc | -9.0271 | -61.6053 | 2024-10-10 01:15:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 3d490123-3f12-3c32-a967-2e0387d4af0c | -9.0656 | -61.3934 | 2024-10-10 01:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.1 |
| c3055452-a977-393a-919f-3e5d196535a8 | -9.0841 | -61.4117 | 2024-10-10 01:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| fe4e5b5d-ba21-3fab-a707-cce95968525c | -9.0842 | -61.3925 | 2024-10-10 01:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 103.9 |
| d9dfe428-a039-3403-8de7-606c7877192b | -9.0857 | -61.1629 | 2024-10-10 01:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 226b8145-d82c-39b6-bbce-1044d47f51fb | -9.1028 | -61.3917 | 2024-10-10 01:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 20284248-10dd-3325-a06d-b3380fb55584 | -9.1035 | -61.2769 | 2024-10-10 01:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 7c3974a8-b881-3b12-bb7b-6c9b004fd8f7 | -9.122 | -61.2951 | 2024-10-10 01:15:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| e0e3c9ad-9641-3945-8b74-fc658bc4ac52 | -9.1221 | -61.276 | 2024-10-10 01:15:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 130.8 |
| e270f218-8258-3e04-90db-6052f4c4a26c | -9.9105 | -58.1313 | 2024-10-10 01:16:03 | GOES-16 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 9061c74e-c3ea-3c4f-a04b-ffd7be9786db | -10.3632 | -55.8554 | 2024-10-10 01:16:05 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 24.1 |
| a86ec34e-87df-3c66-8198-c64ac03292fa | -10.3707 | -61.2513 | 2024-10-10 01:16:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 07c2a3dd-5137-35c6-8b93-0b717c8bb7a3 | -10.3894 | -61.2502 | 2024-10-10 01:16:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 49.3 |
| f1bb8b5f-16d3-31bf-b8df-fe7760bb9463 | -11.0445 | -57.2023 | 2024-10-10 01:16:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 186.3 |
| b7e657b3-92a2-3498-8909-bd3969e71f20 | -11.0252 | -57.2436 | 2024-10-10 01:16:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 92ec3882-2fb1-3b05-a358-3346ffbbecd7 | -11.0254 | -57.2237 | 2024-10-10 01:16:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 167.3 |
| f8bb58d6-769c-3417-8f68-e7af80fea542 | -11.0256 | -57.2038 | 2024-10-10 01:16:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 171.6 |
| a07cb5da-8e51-3f9d-85b2-1a6490f97a9d | -11.0441 | -57.2421 | 2024-10-10 01:16:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 66b89d08-06f6-338d-bd07-22008663a4af | -11.0443 | -57.2222 | 2024-10-10 01:16:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 215.2 |
| 9749c51b-2c57-3e0f-9c55-1e304a4064cc | -11.2582 | -60.4079 | 2024-10-10 01:16:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 30e82477-1942-31c8-8bdd-ad1b5e878c8e | -11.2583 | -60.3885 | 2024-10-10 01:16:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 15809942-d395-3130-bac7-54a26b3eb235 | -11.8188 | -58.8459 | 2024-10-10 01:16:14 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 805849b0-b504-3f41-8ca7-51fb923d4c28 | -12.2888 | -43.7495 | 2024-10-10 01:16:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 09e06b9d-d5c1-32ee-b496-a3c4d02af05c | -12.2893 | -43.7258 | 2024-10-10 01:16:15 | GOES-16 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 146.5 |
| 658ec039-5efa-394c-8b08-562734e0fba6 | -12.4177 | -54.5797 | 2024-10-10 01:16:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 102.7 |
| 187f67e4-13fa-3e73-91b2-bc72f419d9ee | -12.418 | -54.5592 | 2024-10-10 01:16:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 76.2 |
| ae77e2f6-3d18-32d6-9cbe-6a9efc287004 | -12.9255 | -51.1361 | 2024-10-10 01:16:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 136.7 |
| 995fce80-f41a-3075-8cf3-fdf99c87a3c1 | -12.9447 | -51.1337 | 2024-10-10 01:16:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 127.0 |
| 1e3c7bcb-c02e-37d5-b98c-579239dfd019 | -13.1845 | -51.7004 | 2024-10-10 01:16:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 6253868c-6e95-3f72-a801-7cb0e311163a | -13.8374 | -44.5455 | 2024-10-10 01:16:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 83.0 |
| ded632c5-48bb-3099-a992-25eb625c3d95 | -13.8379 | -44.522 | 2024-10-10 01:16:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 84.8 |
| e2f3c10e-031f-37dc-80bb-426679c91f1e | -13.8574 | -44.5185 | 2024-10-10 01:16:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 83.4 |
| e99690ed-43e3-3a48-8f20-bb4f9c651e0d | -17.0549 | -45.2808 | 2024-10-10 01:16:41 | GOES-16 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 08bdc66f-7551-3deb-aa29-950f7b0d67dc | -17.0555 | -45.2571 | 2024-10-10 01:16:41 | GOES-16 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 91.5 |
| fc4754b3-6d78-361d-9349-9421e555bdd0 | -2.6533 | -53.3506 | 2024-10-10 01:25:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 139.3 |
| d7c2e9c7-4f19-34d8-8de6-dccb3801c642 | -2.6716 | -53.3704 | 2024-10-10 01:25:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 56128c1e-2624-3189-8d56-d99264fdd401 | -2.6716 | -53.3502 | 2024-10-10 01:25:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 437.2 |
| 34adf130-35e6-362d-813c-e810907c322c | -2.6717 | -53.3299 | 2024-10-10 01:25:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 148.9 |
| 60e66e85-eda1-33e6-a21e-14810a320a30 | -2.69 | -53.3497 | 2024-10-10 01:25:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 141.7 |
| 4dd83595-d68e-39f7-a7e8-e76f726a0efd | -2.6901 | -53.3295 | 2024-10-10 01:25:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 2f4bc432-6a4f-3347-9f3f-38e587db9c3e | -3.3341 | -53.232 | 2024-10-10 01:25:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 4b75cd60-c948-31a5-8b18-6c24610aaa38 | -3.3342 | -53.2117 | 2024-10-10 01:25:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| f0205af0-37cb-35fe-8059-a6cad5ca9e76 | -3.7247 | -44.9547 | 2024-10-10 01:25:27 | GOES-16 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 61.7 |
| ae473d3a-33da-31e1-a918-ec25cdcc1de3 | -3.7961 | -45.4927 | 2024-10-10 01:25:28 | GOES-16 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 51.1 |
| e20afda2-d905-373a-816e-b4b1fe990f15 | -3.8147 | -45.4918 | 2024-10-10 01:25:28 | GOES-16 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 107.2 |
| 190a347c-a4a6-3464-b47b-211cf1eb5a84 | -4.0814 | -51.0292 | 2024-10-10 01:25:29 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 9df6cfdd-23f8-3638-98fe-1b9db88f3c24 | -4.0961 | -48.2739 | 2024-10-10 01:25:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 167.4 |
| aaaca06c-17a6-30fb-8834-a560d91b4ead | -4.0962 | -48.2523 | 2024-10-10 01:25:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 147.5 |
| 798c78c9-0087-3395-aebc-fb0122949c65 | -4.1146 | -48.2731 | 2024-10-10 01:25:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 165.5 |
| b86bdd0a-396d-38da-afb3-1b13770d5a03 | -4.1148 | -48.2515 | 2024-10-10 01:25:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 129.3 |
| 98ff4513-f831-32b3-abec-9240dec1944f | -4.4776 | -46.5956 | 2024-10-10 01:25:32 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 73e6909f-c6f3-3d97-8292-d2e13230c307 | -5.9036 | -45.4127 | 2024-10-10 01:25:40 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 3bfb6551-9cbd-32a4-89d5-8dd243805254 | -5.9223 | -45.4114 | 2024-10-10 01:25:40 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 903db7a3-3cad-3627-89f9-ee201f0bb7ed | -6.5218 | -60.0649 | 2024-10-10 01:25:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 7a6af05f-4de7-3acd-af53-d2c0b4e782a0 | -6.5219 | -60.0457 | 2024-10-10 01:25:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 1711f536-e207-3981-aba2-1adf129000f2 | -6.747 | -59.3259 | 2024-10-10 01:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| efc02578-0cf2-3876-ba2f-bc218c33c9d0 | -6.7654 | -59.3252 | 2024-10-10 01:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 138.3 |
| 50b3cecc-31eb-3041-8b24-8e7e47c606d3 | -6.7655 | -59.3059 | 2024-10-10 01:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.9 |
| a6bb3198-3f33-3f35-bb52-8c2344fe53b1 | -6.7839 | -59.3245 | 2024-10-10 01:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 111.5 |
| 1bad3e47-e126-3811-ac9f-17cb3d3f998f | -6.784 | -59.3052 | 2024-10-10 01:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.9 |
| a3278164-0959-331c-88f8-1d4005d961d5 | -7.1346 | -59.3099 | 2024-10-10 01:25:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 62c31002-5aec-3001-b4bd-44b5efd18085 | -8.2325 | -61.1823 | 2024-10-10 01:25:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| d71c493a-01b1-35a1-bdc6-408f87402db0 | -8.7029 | -63.0813 | 2024-10-10 01:25:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 198c4ec2-7666-3850-b27f-fd41e6f0e74c | -8.9111 | -62.353 | 2024-10-10 01:25:57 | GOES-16 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 22a0f9d8-28fc-3107-b524-2524ffc7f48f | -8.9898 | -61.6261 | 2024-10-10 01:25:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 68230982-fbb5-3bf5-8732-e87a4800a6f7 | -8.9899 | -61.607 | 2024-10-10 01:25:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 3145b606-7175-3466-b7ac-9ae5d1c44bd3 | -9.0084 | -61.6253 | 2024-10-10 01:25:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 87fa52ae-877c-3e54-bea8-a7252a9e84b9 | -9.0085 | -61.6062 | 2024-10-10 01:25:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 52.5 |
| f7a87d4b-b25b-3528-b276-973b53eb4ba2 | -9.027 | -61.6244 | 2024-10-10 01:25:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 11b39891-0146-30da-989e-9e5722492048 | -9.0271 | -61.6053 | 2024-10-10 01:25:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 48c9f171-be48-3e51-a7eb-36d136003f6c | -9.0656 | -61.3934 | 2024-10-10 01:25:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 4c8814a6-de9a-3328-b0c1-b29f2a93f074 | -9.0841 | -61.4117 | 2024-10-10 01:25:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.7 |
| cbde131f-6886-30e0-85b8-1482f8ab38ac | -9.0842 | -61.3925 | 2024-10-10 01:25:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 108.9 |
| f87fd0a1-b16c-3c68-b531-9b18fee18d7a | -9.1028 | -61.3917 | 2024-10-10 01:25:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| c113e0c5-87d5-33c2-a842-c08dcb6d6772 | -9.122 | -61.2951 | 2024-10-10 01:25:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 9c84b686-c17b-353b-875f-a3d1f0378368 | -9.1221 | -61.276 | 2024-10-10 01:25:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 122.3 |
| 06a0d2d4-27bc-3d51-b90a-a085f75643a1 | -9.4818 | -63.1632 | 2024-10-10 01:26:01 | GOES-16 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 10f533c6-7d58-39bf-8147-6dade22a2b8b | -9.4819 | -63.1443 | 2024-10-10 01:26:01 | GOES-16 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 112.6 |


[Clique aqui para ver as próximas entradas](README29.md)
