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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f1c9ac84-a13b-3f60-be2b-189786d9c126 | 2.7145 | -60.2831 | 2026-09-17 01:00:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 4f904879-ca45-31e9-a245-3b864e1af03f | -6.8422 | -62.8783 | 2026-09-17 01:00:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c857c7cb-f4f3-3e4b-82bb-465c724878a7 | -8.7709 | -61.378799 | 2026-09-17 01:00:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9b3ba309-5ca3-36b5-8bf8-44073f8d32fb | -11.8045 | -58.158199 | 2026-09-17 01:00:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d193ed04-f189-365b-b942-dca1d4b85bca | -6.7963 | -59.1595 | 2026-09-17 01:00:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d2c07424-07de-3a7b-8652-f896676a6957 | -8.6455 | -66.5606 | 2026-09-17 01:00:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| eb17bd6c-2f73-3c4e-aaa0-9c2d7cb84fcb | -9.0557 | -65.892502 | 2026-09-17 01:00:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d6a3828c-fde3-360d-9271-4ec8e6c24ce4 | -8.9134 | -62.378201 | 2026-09-17 01:00:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c04c6cd6-f436-331b-87a6-0b4fc79dea1f | -2.8838 | -54.1301 | 2026-09-17 01:00:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88277f13-1434-3c25-8215-adc652c42d91 | -9.1026 | -65.920502 | 2026-09-17 01:00:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 82fef247-be61-3bd6-8370-ab5c4a5bb7a6 | -2.6914 | -57.586899 | 2026-09-17 01:00:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cf2b0ca0-2185-306c-893f-3d276febc9c8 | -9.288 | -60.6152 | 2026-09-17 01:00:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 96bc6b7d-644b-3acf-8e42-6e8920ec4144 | -10.7149 | -53.978699 | 2026-09-17 01:00:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f435e7e8-3b48-3a0f-a504-faad37eaeab9 | -10.823 | -65.0056 | 2026-09-17 01:00:00 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b697c163-a67b-3c5f-8bed-4e4fed996a06 | -6.8937 | -59.001999 | 2026-09-17 01:00:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9308a897-9372-35c2-84af-61154b22ff1d | -9.0882 | -60.959999 | 2026-09-17 01:00:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c418810e-098a-3747-9c32-a2be31201ee5 | -4.4906 | -54.941002 | 2026-09-17 01:00:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c39d03cc-8a55-3c56-933d-639ffe605f6d | -10.6035 | -64.936996 | 2026-09-17 01:00:00 | METOP-B | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f6d1749b-a4dc-3253-bea4-95e73e3da79e | -8.8809 | -62.370998 | 2026-09-17 01:00:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4e1e7ab8-c2a8-3f29-a129-3b69e8fb0fd9 | -9.0932 | -60.936699 | 2026-09-17 01:00:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f3eaa1ac-7d82-3498-980b-8935a5036db2 | -9.4084 | -62.705101 | 2026-09-17 01:00:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 24382827-05a1-3dc1-8a57-4487c3c16adc | -3.4702 | -54.702801 | 2026-09-17 01:00:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6eac15a3-b62b-3234-81cd-2ba172908244 | 2.7167 | -60.273602 | 2026-09-17 01:00:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| c35081af-ca47-31a9-b7b2-f6b7b8fcdf2a | -7.0635 | -63.039001 | 2026-09-17 01:00:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1e9b266e-b697-3897-aa42-af6837620a8a | -10.8196 | -54.0667 | 2026-09-17 01:00:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 78ba61c7-5064-3812-ac67-cb5ad62b242d | -9.2799 | -60.624599 | 2026-09-17 01:00:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 480a2691-cdc5-33ae-887a-44e65f9038a3 | -8.915 | -62.385201 | 2026-09-17 01:00:00 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 943e5dcf-22bc-30fb-a1e9-532c93bcd62f | -8.7511 | -66.527901 | 2026-09-17 01:00:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 33eb3578-b8ad-3f6c-aa9b-db11073ddb49 | -9.101 | -61.016399 | 2026-09-17 01:00:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c1cec336-7f3a-3759-bd6b-2f689c381a3a | -9.5363 | -62.354599 | 2026-09-17 01:00:00 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7b848782-967d-3c4d-9cb5-9a06dc0e45d7 | -9.275 | -60.6031 | 2026-09-17 01:00:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 15d168ff-63d2-3077-80d0-9e0635c87199 | -9.4477 | -60.3661 | 2026-09-17 01:00:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4089c1fd-e5fd-3660-b00f-fc9c4930a814 | -10.1439 | -61.1605 | 2026-09-17 01:00:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4bc6fcd1-5661-327f-a388-936b9c8c58df | -9.0428 | -60.4445 | 2026-09-17 01:00:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d9f05471-c14f-356d-830a-e99fcc5b1a56 | -4.51483 | -54.97305 | 2026-09-17 01:02:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| b0399cbd-ed34-3a87-b33e-d3b7e300b177 | -9.35045 | -65.93571 | 2026-09-17 01:02:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 7203050b-f113-38cb-b532-63bfbeef6d52 | -8.66135 | -66.50423 | 2026-09-17 01:02:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 727b48fe-ca4e-331b-8f1d-56fb57d33437 | -6.93428 | -63.03354 | 2026-09-17 01:02:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 76e1cab1-cb03-3004-a7b4-29c5861a9b4d | -6.31282 | -62.67984 | 2026-09-17 01:02:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b732625b-4cb8-333f-b44d-3fa0b81e2e23 | -8.10784 | -64.11738 | 2026-09-17 01:02:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 152173a7-1447-306c-ab85-f4fc69091ca6 | -9.01695 | -61.03174 | 2026-09-17 01:02:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| fc0af5a6-68c7-327c-b8df-ca40bc0c5af8 | -7.52702 | -63.38294 | 2026-09-17 01:02:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| ee324e14-775f-397f-9e11-2d46e29e8ad3 | -9.54192 | -62.37136 | 2026-09-17 01:02:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 852a7cb4-f5b8-37bc-a606-3968b2b51522 | -7.01081 | -62.98722 | 2026-09-17 01:02:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1aefa037-ccc6-377e-80a4-bb93977f7f12 | -9.11224 | -65.95093 | 2026-09-17 01:02:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 4e0f540f-6b13-3770-9113-df314556e7bc | -9.11096 | -65.94121 | 2026-09-17 01:02:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 18.5 |
| c1fd617c-c94d-33a5-a4be-32acff6e23ce | -8.09819 | -61.82407 | 2026-09-17 01:02:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 374525fa-570b-3cfa-b8ee-71cd5a891180 | -1.60303 | -55.5709 | 2026-09-17 01:02:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| efb39f21-e702-32e4-9a40-9c415e811f59 | -7.61292 | -67.24814 | 2026-09-17 01:02:00 | TERRA_M-M | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5455fc5f-d004-3a2c-811a-03576eb4977d | -9.10969 | -65.93149 | 2026-09-17 01:02:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 91522c68-b03f-3853-a8bd-f4a82809ce97 | -6.90099 | -59.02778 | 2026-09-17 01:02:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 8be1b6ef-0d0f-3f09-abc2-142429682049 | -6.70885 | -58.8048 | 2026-09-17 01:02:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 16.6 |
| fde28157-511b-3aae-accf-336bbb02845e | -6.37205 | -58.29513 | 2026-09-17 01:02:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 26.5 |
| d1307095-0beb-3c42-8c58-b501a9a1beeb | -9.14401 | -65.83839 | 2026-09-17 01:02:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d8a9ede1-963d-33d5-86da-9923a4499ba1 | -6.82003 | -59.18312 | 2026-09-17 01:02:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 4a783d9e-d373-38bd-bded-82c709176eb0 | -8.75224 | -66.56886 | 2026-09-17 01:02:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 43b52337-2e7e-3b89-bfd0-a54535e78935 | -9.27755 | -60.64176 | 2026-09-17 01:02:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 4fab2274-bc07-3d6f-890c-110e7aa687bd | -6.75189 | -58.80992 | 2026-09-17 01:02:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 265e1d39-3e23-330f-8fc7-d05d6e0e8d31 | -9.28428 | -60.62275 | 2026-09-17 01:02:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 253f9b74-de97-3b3d-a5ea-72b22de6a752 | -9.18705 | -66.02 | 2026-09-17 01:02:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7f901666-ba33-3fd0-bc5c-c9692a03849a | -6.93296 | -63.02413 | 2026-09-17 01:02:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 41.3 |
| f4e402c1-3956-3b7d-88ca-2c991a91327f | -9.02351 | -61.00757 | 2026-09-17 01:02:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| bd1bfe7d-e1d1-31a1-9bd2-08d756786720 | -9.47789 | -65.65104 | 2026-09-17 01:02:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c9dae17c-fd39-3474-843e-8ebadaed92fe | -9.34913 | -65.92587 | 2026-09-17 01:02:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1b013fee-4154-38aa-aa9f-bbf5304b522d | -9.40751 | -62.72097 | 2026-09-17 01:02:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 31.7 |
| f78163a0-e56d-33c7-96d6-5470c306795a | -8.91883 | -62.39835 | 2026-09-17 01:02:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 16.7 |
| b8c32ea7-ed8b-39c7-a787-a3f030e79e05 | -7.30216 | -64.68273 | 2026-09-17 01:02:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f91dddf8-6e6b-3f81-a8fb-6e29f06871cb | -8.63446 | -66.51826 | 2026-09-17 01:02:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5400a4ee-ef36-3713-91c4-e24670d0d0a2 | -6.90671 | -59.02042 | 2026-09-17 01:02:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 17.0 |
| fee837ba-b7d5-3641-aa9d-8d76b5b09030 | -9.10785 | -60.95359 | 2026-09-17 01:02:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| f0c08760-3870-3b35-9922-f513f5ea16fa | -8.2272 | -61.51072 | 2026-09-17 01:02:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 78776c24-1bbe-3916-a72d-15e4059c4b15 | -9.08655 | -61.01487 | 2026-09-17 01:02:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 363e067e-39f9-30ef-af71-0c15e9a2c13b | -8.00022 | -61.37325 | 2026-09-17 01:02:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 6505aef3-63fd-3d29-b52f-47680390b8ce | -9.10177 | -65.94244 | 2026-09-17 01:02:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c73ba24e-8961-3d93-88ee-568aed0a8ed7 | -6.16713 | -62.63634 | 2026-09-17 01:02:00 | TERRA_M-M | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8ffabc15-8844-33b9-94af-387655c63263 | -8.64244 | -66.57964 | 2026-09-17 01:02:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 2bf9d63b-0e1b-360f-845f-78b41899db03 | -6.90349 | -59.04467 | 2026-09-17 01:02:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.0 |
| dbe6a840-2366-38b1-8c9d-a31158945d1c | -9.28607 | -60.63463 | 2026-09-17 01:02:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 78b248dc-6e36-31de-9d99-642f1f5f3c84 | -7.97437 | -62.04388 | 2026-09-17 01:02:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 10.5 |
| b57378c4-22fa-3f82-ae26-d737192a855b | -9.41519 | -62.71038 | 2026-09-17 01:02:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d206b7ae-32e2-314f-b1d4-04472bbd6b4a | -6.94204 | -63.02282 | 2026-09-17 01:02:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 05b2422b-607b-3ed8-84dc-337f887e3e70 | -8.77308 | -61.39196 | 2026-09-17 01:02:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e8f09088-f2df-385b-8039-9e9104c5b914 | -8.15483 | -64.0506 | 2026-09-17 01:02:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f390614f-cc38-3f9a-b7d5-f39754dacde9 | -6.71543 | -58.81534 | 2026-09-17 01:02:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 3d489c8c-322f-30ea-b8fc-aeeac7b10d93 | -8.09668 | -61.81368 | 2026-09-17 01:02:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 61d2d213-1b16-3541-becd-152a6ff2df93 | -9.27598 | -60.63617 | 2026-09-17 01:02:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 2eae7c5c-ce0a-3d47-ab8d-79cc73b55fc0 | -8.64377 | -66.58989 | 2026-09-17 01:02:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 61adf309-eb00-3b76-bbc8-7d1d92c341f1 | -6.92389 | -63.02544 | 2026-09-17 01:02:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 607c9ac9-2075-39c0-b3a0-3a9ca623a51a | -6.94335 | -63.03222 | 2026-09-17 01:02:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6765b842-9106-371a-b718-fa3af388c623 | -8.8829 | -62.40025 | 2026-09-17 01:02:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 13.1 |
| d0602287-b4f3-3294-a3bd-6f7ee7e2d0d6 | -6.84918 | -62.89127 | 2026-09-17 01:02:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 43fffafb-bc67-3278-bb71-f394de5b3b27 | -9.27411 | -60.61796 | 2026-09-17 01:02:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 770cc627-e5cb-3a4a-ac44-f6da801274f9 | -9.09963 | -60.96653 | 2026-09-17 01:02:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 5f9294ea-ba43-3049-af6c-f615317fca72 | -9.28248 | -60.61083 | 2026-09-17 01:02:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 22.6 |
| a607a953-a3b5-376f-86a2-347621cbc243 | -8.88155 | -62.39062 | 2026-09-17 01:02:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 596aa207-b490-35fa-a32e-e08e0fe5383c | -9.40618 | -62.71169 | 2026-09-17 01:02:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 121.4 |
| ae9150e2-7538-35be-9255-7a6f93fb5855 | -7.30095 | -64.6739 | 2026-09-17 01:02:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9257f651-b19b-31ff-a284-3168dce2b470 | -6.84005 | -62.89259 | 2026-09-17 01:02:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6d97873b-0839-3baa-bbdb-c8d894774db8 | -9.09796 | -60.95514 | 2026-09-17 01:02:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.1 |
| a5c11acf-3a05-3dff-b4ba-cee6d906bb21 | -8.10906 | -64.12622 | 2026-09-17 01:02:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |


[Clique aqui para ver as próximas entradas](README8.md)
