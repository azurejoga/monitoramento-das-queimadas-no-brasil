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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 868421a8-0b71-3e9e-822a-2a1c625cdb78 | -9.4349 | -45.625 | 2026-09-02 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 6060c05c-bf2a-310f-ab2b-afeb778aacc2 | -10.0815 | -46.7441 | 2026-09-02 13:50:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 61.8 |
| eaed0305-4d5b-3972-8dd1-63f00a4d5817 | -6.8613 | -41.6532 | 2026-09-02 13:50:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 93.4 |
| 592578f2-9ca5-336b-a67f-c9f827a75f9a | -10.4417 | -46.7459 | 2026-09-02 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| c87e7de5-fa92-3220-884b-3585091e003a | -17.0878 | -56.8534 | 2026-09-02 13:50:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.8 |
| 74893432-408d-397e-8fb9-805cadac47c0 | -11.8627 | -46.0622 | 2026-09-02 13:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 295.3 |
| 30f6babd-c66d-3a5d-aa3b-f6cd146b496e | -9.2144 | -47.99 | 2026-09-02 13:50:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 2115dfba-b085-3b82-b595-6a6d31c7a1d5 | -8.4481 | -54.7452 | 2026-09-02 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 7068ea95-2216-3a15-9b49-5c9b1465769e | -8.7819 | -46.4399 | 2026-09-02 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 56.2 |
| f3c9fb0d-6faa-36f7-8dd8-c389e4d77bae | -10.7431 | -50.8514 | 2026-09-02 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 88.1 |
| cac67d66-7788-3d66-8a18-50012f35a14d | -7.3007 | -49.8187 | 2026-09-02 13:50:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 73d9c8e9-dee0-3130-833b-6b7fa0d6f793 | -6.8422 | -41.6791 | 2026-09-02 13:50:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 134.8 |
| 20be3c10-09ca-360b-b383-c787287355ca | -10.1008 | -46.7195 | 2026-09-02 13:50:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 70aaaa33-604b-33d0-a8ef-ec52c7098cc0 | -7.2006 | -60.6706 | 2026-09-02 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 6d82f0b3-4e21-350a-8511-6c2351e55082 | -11.3044 | -45.1805 | 2026-09-02 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 583f7bff-77c9-32a7-a561-397c6e647cbf | -9.4538 | -45.6228 | 2026-09-02 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 44.3 |
| 7afce309-6535-3b02-94b4-13e5dbeec0f3 | -11.3048 | -45.1575 | 2026-09-02 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 125.7 |
| 9928dcee-f806-3c39-bd45-a6b7d550a033 | -6.6949 | -58.7485 | 2026-09-02 13:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 15427d2d-153f-3656-bee4-38727b43fc17 | -10.358 | -49.9742 | 2026-09-02 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 18f5d8fb-1741-3576-b0f7-c2b40a7425ad | -10.8815 | -45.3764 | 2026-09-02 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 263.6 |
| cd51ff8c-d6a0-35da-b45f-b51394873f64 | -6.6765 | -58.7492 | 2026-09-02 13:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 2fe8da0e-8305-358b-9ed2-e0ffa653c465 | -12.0936 | -47.0913 | 2026-09-02 13:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 24760c1d-e9ed-37cd-a8d2-514752a1f2d6 | -10.3013 | -49.9801 | 2026-09-02 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 764ca341-772a-3f0f-9f77-6e2aa9245983 | -8.4483 | -54.725 | 2026-09-02 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 120.3 |
| f7e31a34-ce00-3f91-94c2-358c1827d18e | -11.6624 | -50.1954 | 2026-09-02 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 122.2 |
| b38ae73b-e126-3bb4-9301-cf3d32b8c834 | -6.6764 | -58.7686 | 2026-09-02 13:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 76.8 |
| cbad5048-3703-3c51-9620-d28776ab469f | -13.9662 | -58.6936 | 2026-09-02 13:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 150.6 |
| 677dd6b5-1ef8-3035-a990-6b6ff72ddb55 | -11.296 | -50.5794 | 2026-09-02 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 34de53d7-c264-3141-b8be-4684477c74d3 | -6.6542 | -59.426 | 2026-09-02 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 2282cc5b-abb5-3068-9aaf-145c1981c220 | -9.1533 | -59.5027 | 2026-09-02 13:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 3a8bf80b-036b-39fd-aead-3004f1d9d7ed | -3.6215 | -60.566 | 2026-09-02 13:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 3bb3cb13-0cfb-3830-8c85-5d8a32bde606 | -10.442 | -46.7235 | 2026-09-02 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| ac1e9947-186c-3662-8975-f527d8e31cd5 | -9.4159 | -45.6271 | 2026-09-02 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 47.9 |
| e6b0d202-9383-388b-8443-41c755124a4a | -13.9853 | -58.6919 | 2026-09-02 13:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 77.3 |
| bc8d32c2-1200-3506-a394-989840004e31 | -10.0818 | -46.7217 | 2026-09-02 13:50:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 60b0cfff-b4e1-38a9-8b52-2a21fdc11a25 | -11.5287 | -45.4703 | 2026-09-02 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 73.8 |
| aef37b49-896f-3f15-a0c9-e13f1788cc45 | -12.0933 | -47.1138 | 2026-09-02 13:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 99.7 |
| d76e74b8-d5bb-38ae-9e4f-e8e4ef0422a2 | -11.2669 | -45.1398 | 2026-09-02 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 73.0 |
| bb0370ce-d641-3220-8d53-17eb60eb47ed | -8.7613 | -62.5869 | 2026-09-02 14:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 6a96a638-97ad-3bd3-a303-4737b656a585 | -3.2455 | -47.9187 | 2026-09-02 14:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 69da2458-a80c-31ff-8577-ca9fc8b7588a | -12.1504 | -47.1283 | 2026-09-02 14:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 138.2 |
| 38eb05f5-1b82-3434-a421-9c68e37889d2 | -10.1456 | -50.3379 | 2026-09-02 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 8853a750-1597-3cb0-b36e-fc8a2456da85 | -10.4145 | -49.9898 | 2026-09-02 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 2b1723d7-f016-3c65-beec-bfd23883374c | -3.2361 | -61.217 | 2026-09-02 14:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 5fd310b6-13dc-36d3-abe9-bd77090b9a9f | -10.358 | -49.9742 | 2026-09-02 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 0088f7cb-f9f1-314f-92e0-ddcfdb37eb5e | -11.2673 | -45.1167 | 2026-09-02 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 97157700-588c-32e4-bfa8-6147f3b1ccc3 | -6.1474 | -57.7605 | 2026-09-02 14:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| c1d48d09-5f97-3e65-8d2a-d3df7d008f40 | -6.857 | -59.4371 | 2026-09-02 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| cca2326b-a1a2-3b00-ad6a-08c574a6240d | -10.3769 | -49.9723 | 2026-09-02 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 27b8d524-8b3f-3186-8042-0101ccdf450a | -6.6541 | -59.4452 | 2026-09-02 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 104.3 |
| ca9c3c16-75fd-38c9-a62e-e18ca9b684ca | -10.0944 | -45.8644 | 2026-09-02 14:00:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 40.6 |
| 7c455dce-5572-357f-b018-886181e42cf0 | -10.7431 | -50.8514 | 2026-09-02 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 1e26fc34-b4db-320f-8187-98da47bffd8a | -6.6542 | -59.426 | 2026-09-02 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 6a2bd696-7b44-3fb4-983f-ecd98b30c679 | -11.3048 | -45.1575 | 2026-09-02 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 9845aa8a-ba63-3183-a904-f21d53e5039c | -12.0741 | -47.1164 | 2026-09-02 14:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 131.1 |
| eb326412-9b57-33ab-a2c0-409097e1e01c | -3.3688 | -59.4079 | 2026-09-02 14:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 8f1ddf31-2dda-3641-a398-c7573650a90e | -5.5833 | -60.1924 | 2026-09-02 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 130.7 |
| f99a8837-1126-3c63-a65e-fb710cfefa64 | -10.3959 | -49.9703 | 2026-09-02 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 6739d6a1-a986-39b7-8382-d6ad97af6cbf | -10.127 | -50.3184 | 2026-09-02 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 918ec404-b4a1-3f13-971e-e24b79bd13cd | -7.3007 | -49.8187 | 2026-09-02 14:00:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 92e4515a-4302-351e-bd7e-19ac35713cb5 | -8.4673 | -54.6833 | 2026-09-02 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| aa373bfd-e122-39ef-9fc9-91a2cf9e31e3 | -13.9855 | -58.672 | 2026-09-02 14:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 9bea208c-13cf-32d7-abf0-9ac3bc73a96e | -11.0437 | -49.6635 | 2026-09-02 14:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 43a33f7d-2ac9-3a96-abe8-fe3bf5e55678 | -6.6949 | -58.7485 | 2026-09-02 14:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 6a0b25e5-2ac2-391b-935a-b91e3fa4c9c6 | -6.7648 | -59.4408 | 2026-09-02 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| ff1ea3a8-e0d0-35e8-91b4-02374ec88163 | -3.6215 | -60.566 | 2026-09-02 14:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 3332d955-8aaa-3d61-8aa5-0be6bfcb2e20 | -11.6624 | -50.1954 | 2026-09-02 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 4b324e6f-b2e9-393d-b28f-3787bb02b2ab | -7.3486 | -60.6074 | 2026-09-02 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 33b3093b-7a13-3a7f-be95-c25e6689103d | -7.6505 | -46.7268 | 2026-09-02 14:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 82abb54a-8088-3465-afd9-23000a21085f | -6.8422 | -41.6791 | 2026-09-02 14:00:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 107.6 |
| 3abc6c67-6d04-3d21-abfe-4a679126a78f | -11.6434 | -50.1976 | 2026-09-02 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 109.4 |
| f51edc08-8146-3831-bfad-fecee044a6c4 | -13.9853 | -58.6919 | 2026-09-02 14:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 9403f4d5-7df7-356c-98fa-7ec53dcffdfe | -7.3487 | -60.5883 | 2026-09-02 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.1 |
| e2dafbb9-07af-3b2b-8f83-b66bb8205126 | -10.3193 | -50.0425 | 2026-09-02 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 132.1 |
| e65bb36b-f0c1-31e6-b654-6a3517f678df | -9.1533 | -59.5027 | 2026-09-02 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 88ded621-9a45-3c34-a7be-1ffc7980567d | -7.2191 | -60.6699 | 2026-09-02 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 80.2 |
| a35550f5-1cb9-3537-9b0a-98ae99ca196c | -11.277 | -50.5815 | 2026-09-02 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 6ceaba38-8815-320d-bb7e-d6aaa76746f0 | -8.4483 | -54.725 | 2026-09-02 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 105.8 |
| e3c1bbaf-63e9-3bc1-af1a-8eb18a323dd2 | -10.3004 | -50.0445 | 2026-09-02 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 0170322e-744e-309e-b8cf-2356748e62a7 | -12.1312 | -47.1309 | 2026-09-02 14:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 696d22ac-a9b2-3ec9-854a-ea37b014655c | -12.1704 | -47.0806 | 2026-09-02 14:00:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 110.8 |
| ccd09b65-f658-3d2a-ad9f-2e17f6cb5ec4 | -11.8208 | -51.0535 | 2026-09-02 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 36637035-0c78-3e70-89c1-b267ce906a46 | -7.2255 | -42.7616 | 2026-09-02 14:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 100.5 |
| 53d16008-e036-36ae-bb54-e81287c22b9a | -10.7618 | -50.8707 | 2026-09-02 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 83.8 |
| a17eaae5-d668-35d1-ab6f-e47f810ca6b6 | -5.5832 | -60.2116 | 2026-09-02 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 181.0 |
| e39c159e-43a9-36f3-ab72-5d773087bb80 | -3.8083 | -59.3027 | 2026-09-02 14:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 50400c80-a40f-37cd-b493-63e3115e66ed | -11.296 | -50.5794 | 2026-09-02 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 91.2 |
| f1f3c061-c825-3591-94c1-9706cce562be | -5.6016 | -60.211 | 2026-09-02 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 0842612f-f938-3785-8a5e-be929b49cb0b | -10.7774 | -44.7463 | 2026-09-02 14:00:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 52e0b13a-901c-3dea-bd7a-9b9e0a720c6d | -9.1955 | -47.9919 | 2026-09-02 14:00:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 1a3d4c42-272c-3a24-aa80-143a8e5b746d | -11.3575 | -45.4257 | 2026-09-02 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 62fd861f-6dab-3e4d-bed7-433555ed6f6f | -10.4148 | -49.9683 | 2026-09-02 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 119707cf-d2e6-3e28-9166-3261d6f7164d | -13.9662 | -58.6936 | 2026-09-02 14:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 176.4 |
| 793193dd-db16-3f05-944c-29df57705d0a | -10.202 | -50.3536 | 2026-09-02 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| ca8ff5c0-e772-3c93-b4a5-0ed3b056ff6b | -10.301 | -50.0016 | 2026-09-02 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 4f25164f-82f9-347f-b4f1-5e26741cad14 | -3.3688 | -59.3887 | 2026-09-02 14:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 89.7 |
| b55fac5f-cfff-3980-9ea4-566a23718185 | -7.2006 | -60.6706 | 2026-09-02 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 6ce80037-2ade-3ffe-bd3d-67f2dd75ead9 | -10.5788 | -47.7306 | 2026-09-02 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| d4f2d482-b825-31a2-9503-24368db85f70 | -11.0247 | -49.6656 | 2026-09-02 14:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 89.5 |
| cac1202e-97c1-33f1-8372-bba49bcae450 | -8.4298 | -54.706 | 2026-09-02 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |


[Clique aqui para ver as próximas entradas](README76.md)
