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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aec099b8-8d94-36a6-8aa1-c5bbed220972 | -3.9021 | -46.4689 | 2024-10-09 01:15:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 14ba09a5-2725-305f-af3f-2f6368b9689c | -3.9023 | -46.4467 | 2024-10-09 01:15:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 6f6443b2-3b70-3dbf-9b1a-febb0f1e1c4a | -3.9207 | -46.468 | 2024-10-09 01:15:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 60.2 |
| f60783d0-4259-3f6f-b2aa-94d5679ba230 | -3.9208 | -46.4459 | 2024-10-09 01:15:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 3c6c7a2d-5430-3f12-82ff-fd247ff1f52d | -3.9393 | -46.4672 | 2024-10-09 01:15:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 757990a2-37b2-39a4-8c69-39517b0156ef | -3.9394 | -46.445 | 2024-10-09 01:15:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 159.3 |
| 17dbc783-dd9c-3508-add7-4f0c7d8f8e02 | -6.7613 | -60.0751 | 2024-10-09 01:15:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 26.9 |
| fffa6f06-5dc9-36a3-bd61-79aee93991ed | -6.7614 | -60.0559 | 2024-10-09 01:15:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 169.1 |
| 56ec81d6-91cf-38cd-bca9-fd82d4a7004b | -6.7615 | -60.0367 | 2024-10-09 01:15:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 27d32250-ffb1-38b8-bebf-017d3fe33d52 | -6.7797 | -60.0744 | 2024-10-09 01:15:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 34.2 |
| f6352ea8-4a08-3e40-bde9-a758c138284f | -6.7798 | -60.0552 | 2024-10-09 01:15:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 255.4 |
| 17ee9e13-7b80-3a0e-9043-1bb30e2ff51a | -6.7799 | -60.036 | 2024-10-09 01:15:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 97.9 |
| 2c952393-effd-34df-951a-b7bd3b46d1fc | -7.1871 | -59.7893 | 2024-10-09 01:15:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 38.5 |
| c5201918-db62-3018-927c-a45fc178be87 | -7.1873 | -59.7701 | 2024-10-09 01:15:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 38022c82-9002-362c-944b-3ed5534e1213 | -7.2056 | -59.7886 | 2024-10-09 01:15:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 6c9b0805-ca6c-3506-8db4-b1673cc139de | -7.2057 | -59.7693 | 2024-10-09 01:15:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 1c0c8ba5-343e-3c0c-bfff-2dfa7ad469bb | -7.2435 | -59.633 | 2024-10-09 01:15:48 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 1c5bfb61-2e77-3f03-8f2b-90671e3757b8 | -7.2436 | -59.6138 | 2024-10-09 01:15:48 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 29.1 |
| 34fc587a-3df6-3a6d-aed5-41567dc7ebb2 | -7.2619 | -59.6323 | 2024-10-09 01:15:48 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 40ef95ee-9358-390c-b678-e3dd457cf9c1 | -8.4919 | -48.6476 | 2024-10-09 01:15:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 222.3 |
| 12609923-f921-3964-a246-185ac4667450 | -8.4921 | -48.6259 | 2024-10-09 01:15:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 132.4 |
| 3b5cd4e3-8248-3412-8ccd-ae88a3aca135 | -8.5107 | -48.6459 | 2024-10-09 01:15:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 85.3 |
| c1987d14-a64f-39ad-be5f-a659f59365a6 | -8.5109 | -48.6242 | 2024-10-09 01:15:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 75c67676-61c3-3f93-9847-dcb4996b61c0 | -9.4435 | -67.1008 | 2024-10-09 01:16:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 5bc72cbe-68ec-341c-b388-064cd973bae4 | -9.4635 | -66.7469 | 2024-10-09 01:16:01 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 7beff636-b016-3a2d-a09d-391877c6fca0 | -9.9292 | -58.1301 | 2024-10-09 01:16:03 | GOES-16 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 34.3 |
| c21694a5-1a6f-379e-9664-e7311f7ee978 | -10.3656 | -64.8262 | 2024-10-09 01:16:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 03ef5591-8c39-3179-a29d-53eef180336e | -10.3894 | -61.2502 | 2024-10-09 01:16:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 7ed6dd38-b138-326e-a018-5c5ed63b8f08 | -10.3895 | -61.231 | 2024-10-09 01:16:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 92b58973-e606-3891-a305-6b60a75af240 | -10.3843 | -64.8255 | 2024-10-09 01:16:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 63cefcd5-4d6e-3794-947c-91c3b9773aec | -10.4287 | -60.9979 | 2024-10-09 01:16:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 5b881bbc-01b1-3c73-b258-f933222e701a | -10.6068 | -55.9169 | 2024-10-09 01:16:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 0effa294-f4cb-3d38-8b6e-0bead2d3701b | -10.6253 | -55.9355 | 2024-10-09 01:16:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 5ec30672-406f-3fc5-aa8a-866f648c2469 | -10.6256 | -55.9154 | 2024-10-09 01:16:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 168.4 |
| 2b0f99e3-a23a-3e34-93c8-002b7c20e703 | -10.6258 | -55.8953 | 2024-10-09 01:16:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 110.9 |
| 62c10c47-a8ee-3248-a1e0-752d0f0aaa74 | -10.6444 | -55.914 | 2024-10-09 01:16:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 38.3 |
| 1ad3a054-78b3-3f39-8a3c-7c4d7eda8315 | -10.6446 | -55.8938 | 2024-10-09 01:16:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 2e148bc9-df4a-363f-bbc1-09ae7cf474d3 | -10.8754 | -63.9169 | 2024-10-09 01:16:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 112.2 |
| 00ee937b-f4a1-376b-bf93-8b84a5e8308d | -10.8755 | -63.8979 | 2024-10-09 01:16:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 93.2 |
| a09e52f4-2c91-3e4d-a6c0-122fc34228b0 | -10.8925 | -64.1623 | 2024-10-09 01:16:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 49075c17-39ff-3a3a-8ccc-7a194d9ab7fe | -10.8926 | -64.1434 | 2024-10-09 01:16:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 73.0 |
| eb773b4a-b4d8-3da5-ab5c-41ca22022f02 | -10.8941 | -63.916 | 2024-10-09 01:16:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 78.9 |
| ece995d2-ff9a-34d4-aa82-8bcf83795307 | -10.9112 | -64.1615 | 2024-10-09 01:16:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 120.1 |
| 1556866d-bda8-3c15-8104-b10d08fb5ff4 | -10.9113 | -64.1426 | 2024-10-09 01:16:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 138.4 |
| aff8de22-dfd2-385b-9740-dab74c318ac8 | -11.3283 | -50.9805 | 2024-10-09 01:16:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 884fca2b-49c9-3275-ba0b-e899f2f79a8b | -11.3286 | -50.9592 | 2024-10-09 01:16:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 0a7cdab5-0e56-37ae-851f-2ba0ae698c37 | -11.5233 | -65.137 | 2024-10-09 01:16:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 34f6ac5b-cb28-35b3-b743-68b626b0f69c | -11.5726 | -58.9619 | 2024-10-09 01:16:12 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 34916e4b-4f3d-3180-851a-c68e543790ea | -11.6806 | -64.0312 | 2024-10-09 01:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 76.6 |
| ebfae9b6-403d-316d-a70e-3872ec91c1e6 | -11.6808 | -64.0121 | 2024-10-09 01:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 69.9 |
| dcb94ecf-9c6c-39b6-a8aa-19f81b48cfde | -11.992 | -51.0553 | 2024-10-09 01:16:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 228c687e-5d8d-3875-bb76-806b88c4d14d | -12.0107 | -51.0744 | 2024-10-09 01:16:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 92.7 |
| b0691740-79aa-383a-8e06-45ccfa02a8c2 | -12.011 | -51.0531 | 2024-10-09 01:16:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 141.3 |
| ac54c5e8-03ee-3b37-83b3-ab822a74fb81 | -12.6676 | -63.0819 | 2024-10-09 01:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 038b96df-1416-3846-8f8c-22847bad1c23 | -12.878 | -62.8007 | 2024-10-09 01:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 275.6 |
| 7ca3f845-f606-3a3e-b317-783e366d6635 | -12.8782 | -62.7815 | 2024-10-09 01:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 4dfe781a-57dd-3faf-b16c-b084282b34cf | -12.9166 | -62.7214 | 2024-10-09 01:16:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 7f34f04b-a2e2-3256-8428-2f780c3c9eea | -12.9377 | -62.4697 | 2024-10-09 01:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 37c97cf8-1157-385c-be7e-eaf46c8123f6 | -12.9378 | -62.4504 | 2024-10-09 01:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 94a1155a-dad3-36a7-aaa3-7a15a3f3da89 | -12.9566 | -62.4685 | 2024-10-09 01:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 771b246e-d7e2-3f44-833b-7c2751f5ef8c | -12.9568 | -62.4492 | 2024-10-09 01:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 961a3ec3-847c-3b3e-b16d-9f9631c006d2 | -12.9756 | -62.4673 | 2024-10-09 01:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 2342b7fc-db01-3619-988a-a0f316888a5b | -12.9757 | -62.448 | 2024-10-09 01:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 122d2364-67af-3484-877c-8a8b951c909a | -12.8591 | -62.8018 | 2024-10-09 01:16:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 128.1 |
| 3e57477c-32af-3363-92dc-58ff491dc1ab | -12.8779 | -62.82 | 2024-10-09 01:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 4b86a80a-487e-337e-8bc8-075bdd2410e4 | -13.3065 | -53.7227 | 2024-10-09 01:16:21 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 3c9eb94f-ac3e-335b-b4c7-dec381df7700 | -13.379 | -61.9194 | 2024-10-09 01:16:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 86.3 |
| de285838-d1e0-393d-ad46-fb60cc6534e7 | -13.3978 | -61.9376 | 2024-10-09 01:16:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 111.6 |
| bad20891-192d-369b-b69b-9bf7d3c092a0 | -13.398 | -61.9182 | 2024-10-09 01:16:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 144.4 |
| e6be8a44-6aec-39a2-99a0-e121a7ea88d5 | -13.8369 | -44.5691 | 2024-10-09 01:16:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 63c9252a-b7d6-3431-b226-b00578fe4611 | -13.417 | -61.9169 | 2024-10-09 01:16:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 890839ce-4cf7-3536-8399-e1ae21029130 | -13.8564 | -44.5657 | 2024-10-09 01:16:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 454cd146-651f-3958-9a66-343190dda56f | -13.8759 | -44.5622 | 2024-10-09 01:16:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 7ffa1b84-c559-31a4-9f06-9932537e6454 | -14.1192 | -44.9872 | 2024-10-09 01:16:25 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 254b2406-1ea7-3dd3-87f1-d8339e2cb1e7 | -14.1197 | -44.9637 | 2024-10-09 01:16:25 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 144.0 |
| 9826fa31-82a8-3f4b-a93a-d6615a123b5e | -14.1392 | -44.9603 | 2024-10-09 01:16:25 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 07dd57fa-cf14-3ac4-8d08-6cbab6361cb0 | -15.1739 | -49.4335 | 2024-10-09 01:16:31 | GOES-16 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 5c76e80b-b0aa-39c6-b62f-e648b0ab60af | -15.1744 | -49.4114 | 2024-10-09 01:16:31 | GOES-16 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 5f2b2d6e-61fe-3c53-8e35-ba9cda42abc5 | -15.1934 | -49.4304 | 2024-10-09 01:16:31 | GOES-16 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 72b3311c-bcba-30c5-8042-4241ddaf2dd3 | -15.1939 | -49.4083 | 2024-10-09 01:16:31 | GOES-16 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 953b3d13-9c05-3e1b-925a-1e2e21ba5599 | -15.5996 | -57.3699 | 2024-10-09 01:16:34 | GOES-16 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 462d2352-8b3d-3e8b-a1d8-17eb4da9cb9e | -16.4184 | -55.9455 | 2024-10-09 01:16:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 91.9 |
| 96823d63-3f9c-35af-a1e5-54c2713c7488 | -16.4187 | -55.9248 | 2024-10-09 01:16:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 85.2 |
| 38405204-12b9-3fb0-9055-f0ed9e2590cc | -16.4379 | -55.9431 | 2024-10-09 01:16:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 54.9 |
| 885232b9-024b-3957-ac04-a2a381c9112f | -16.4383 | -55.9224 | 2024-10-09 01:16:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 53.7 |
| f4b1aad3-08fa-3c4f-a67a-61082a79ce35 | -16.8743 | -56.7352 | 2024-10-09 01:16:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.2 |
| 4e3f5138-bf86-3355-b0e8-90b9d8f6a8d6 | -16.8898 | -55.8039 | 2024-10-09 01:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 90.9 |
| 22182314-025c-34a6-ae17-95e122e20308 | -16.8901 | -55.7831 | 2024-10-09 01:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 90.0 |
| eea377b7-eaeb-3976-ac42-7ad562a3a5e0 | -16.9091 | -55.8222 | 2024-10-09 01:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 78.6 |
| c71de170-2f63-3496-8164-4eab320e8f61 | -16.9094 | -55.8014 | 2024-10-09 01:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 158.5 |
| 1f2a2076-16d2-3040-b2c0-962844e0c552 | -16.9098 | -55.7806 | 2024-10-09 01:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 109.0 |
| 9a15fb21-4676-37f5-9d5c-9961c8ac9f4e | -17.0878 | -56.8534 | 2024-10-09 01:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.1 |
| 5a73f6e5-f8e0-3871-a42d-b270ba5de6d6 | -17.2173 | -57.3307 | 2024-10-09 01:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.0 |
| cce2f737-26a9-3c9b-b97c-d1a5f34cdd4d | -17.1271 | -56.8486 | 2024-10-09 01:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.2 |
| cd4160c7-8678-3aa3-a225-14947e9dedad | -17.1467 | -56.8463 | 2024-10-09 01:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.0 |
| a4b81f19-9458-318c-b34f-3033591b7179 | -17.1588 | -56.1222 | 2024-10-09 01:16:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 101.9 |
| 0c8d6f1b-632c-3a52-941a-a74e1b76c0ed | -17.335 | -55.0366 | 2024-10-09 01:16:43 | GOES-16 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 49.7 |
| 8ecebe16-3e1a-31e4-a58b-005b602fab2f | -17.3353 | -55.0156 | 2024-10-09 01:16:43 | GOES-16 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 67.9 |
| 57599c68-bfc4-350d-9cea-8858a56473d2 | -17.9896 | -44.5723 | 2024-10-09 01:16:46 | GOES-16 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 103.3 |
| ada9172b-6edd-363b-a3f2-556793421aaf | -18.0097 | -44.5676 | 2024-10-09 01:16:46 | GOES-16 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 94.2 |


[Clique aqui para ver as próximas entradas](README33.md)
