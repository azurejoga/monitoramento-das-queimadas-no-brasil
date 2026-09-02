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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a7c00792-1cb0-332c-8134-dcf8f3c973f8 | -10.49722 | -59.62303 | 2026-09-02 01:05:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 18.4 |
| f4e6512e-6adc-3cd8-81d2-62a37fda0b5f | -10.19336 | -69.03847 | 2026-09-02 01:05:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 7.1 |
| c7fb2796-94da-385d-9204-c4364518803f | -8.47505 | -54.7363 | 2026-09-02 01:05:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 120.6 |
| ec78af64-c6a6-389b-bbdc-2af3967b9c58 | -8.4513 | -54.7 | 2026-09-02 01:05:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 613.2 |
| 68b478b5-f678-3726-b7a4-b2e8c27800d3 | -8.10951 | -54.943 | 2026-09-02 01:05:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 2f971f25-287d-3f1b-b19b-e32c77c87782 | -10.49172 | -64.32191 | 2026-09-02 01:05:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 31.6 |
| 1240f4c9-9cc5-30ea-b9f1-27647195c0e1 | -9.83027 | -63.01715 | 2026-09-02 01:05:00 | TERRA_M-M | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 3898a649-eed1-3a19-98f5-e7522ae8abbb | -9.09721 | -65.49902 | 2026-09-02 01:05:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 47ee42c5-698e-3e1f-a295-6745cc3acf94 | -8.75583 | -62.59408 | 2026-09-02 01:05:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 34.8 |
| 42ee6eb8-a810-3859-89cb-3e1315b9fc7d | -13.9833 | -58.69603 | 2026-09-02 01:05:00 | TERRA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 6bdd9e0b-135a-3f28-bd4c-7c90b8509d86 | -9.43982 | -64.56786 | 2026-09-02 01:05:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 1d0b55e5-f440-394f-ad84-891213a71338 | -6.8833 | -59.40359 | 2026-09-02 01:05:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.6 |
| f20dc9a7-a96a-3391-8cbd-dab5c0344086 | -9.44461 | -67.44599 | 2026-09-02 01:05:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 4db68375-0800-31c4-9207-0f236a772561 | -9.15389 | -60.95936 | 2026-09-02 01:05:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 6b406e17-52e2-3b8f-98d6-5ef6612a1b18 | -6.65019 | -59.43918 | 2026-09-02 01:05:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.7 |
| d06f3daf-ab2c-3ba5-9153-ca7ac4c3f476 | -9.44737 | -67.46764 | 2026-09-02 01:05:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7ce8e9a6-682d-3762-b09c-f665db7e82b2 | -7.21327 | -60.67627 | 2026-09-02 01:05:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 6a844b4c-3fbd-3cd8-874a-c06386dd8a79 | -8.11604 | -54.98084 | 2026-09-02 01:05:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 337b0ae3-1e53-3f39-8864-2c78b46b7f0a | -8.44105 | -54.74195 | 2026-09-02 01:05:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 191.8 |
| b2d1663f-3b38-3d03-854f-bb678a0c152b | -7.47185 | -63.75238 | 2026-09-02 01:05:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 11262811-2232-3862-9ae5-97208be0210e | -7.75385 | -61.20148 | 2026-09-02 01:05:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 18.6 |
| a4106d38-03ac-3a93-a315-249c2a0e0041 | -10.50331 | -64.32343 | 2026-09-02 01:05:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1dc0bf2f-2059-3aa7-bdc8-5e29cb61cb8c | -8.12898 | -54.98408 | 2026-09-02 01:05:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 659782c0-092b-3865-bbda-f05c6147d01b | -9.44334 | -67.46291 | 2026-09-02 01:05:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 5a7f9912-5e17-3c97-b0ed-5a2a7f483349 | -11.89182 | -63.18507 | 2026-09-02 01:05:00 | TERRA_M-M | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 08376499-d158-3d94-bada-f163743cca53 | -13.99576 | -58.70307 | 2026-09-02 01:05:00 | TERRA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 260.5 |
| 01f690b0-b597-3a35-b320-3de93f1ad0b0 | -8.40376 | -62.71196 | 2026-09-02 01:05:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 11d36fbd-7cc5-3dc8-99a5-fcd7793cd729 | -6.77277 | -59.44468 | 2026-09-02 01:05:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 22.4 |
| b63d0d94-345c-3575-ac00-54d82abce869 | -7.69269 | -67.11727 | 2026-09-02 01:05:00 | TERRA_M-M | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| a1566eaa-b7f1-3780-bf42-1e1743efc0f5 | -8.12272 | -54.94594 | 2026-09-02 01:05:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 116.9 |
| 225a84d9-92cb-3e05-a908-34be9a25bb16 | -9.88271 | -64.97788 | 2026-09-02 01:05:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 36ab3050-24af-3741-afa5-86e6125d3e0d | -10.75028 | -54.05068 | 2026-09-02 01:05:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 34.0 |
| 0f056ac3-867f-3a67-9896-77040a414608 | -13.99699 | -58.70951 | 2026-09-02 01:05:00 | TERRA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 32.4 |
| c63f6401-ac88-3d4b-b620-56ee44a1b7fa | -9.22753 | -65.8595 | 2026-09-02 01:05:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e2ba19f3-6fea-3ecb-96e6-012d4357b550 | -7.20946 | -60.66835 | 2026-09-02 01:05:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 30640484-9728-363a-b681-85329dc3ebdb | -7.76424 | -61.19986 | 2026-09-02 01:05:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 8995aa16-a10e-3e81-8b24-c9ad43fee1fe | -9.86388 | -64.97149 | 2026-09-02 01:05:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 55dc1dd0-2fab-3916-b851-4687dd592aaf | -9.54668 | -66.17551 | 2026-09-02 01:05:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 914cc1a7-8b7f-3765-8f6a-da7f0c9b8965 | -9.0891 | -65.37232 | 2026-09-02 01:05:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 88bf882a-6f51-3176-b5ae-91535735b17e | -8.45501 | -54.74479 | 2026-09-02 01:05:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 175.8 |
| 2679d161-92b7-34d1-b148-f0e6a659dd99 | -6.60295 | -58.59206 | 2026-09-02 01:05:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 8d7dd4b6-b518-3cd4-bd39-7e074bef06b8 | -7.45306 | -61.37398 | 2026-09-02 01:05:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| ad4867c8-8873-3ad9-9230-d38966273a4b | -7.20232 | -60.6777 | 2026-09-02 01:05:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 59a16ab3-8f7d-3b1d-a04e-c85309ff1ef9 | -6.75399 | -59.43562 | 2026-09-02 01:05:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 336495ee-ec2f-3e78-8510-aa52bb1ccb7b | -6.68777 | -59.9388 | 2026-09-02 01:05:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| b0a6c042-b9d7-3fce-a150-8b3f39c67162 | -9.00551 | -65.43594 | 2026-09-02 01:05:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4ae296fa-e18e-376f-9b0e-95b250eebba5 | -6.64175 | -59.43506 | 2026-09-02 01:05:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 4d905e89-2923-3417-80ae-c1d04396618e | -8.22344 | -62.74053 | 2026-09-02 01:05:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| cc25f83a-5d81-37ac-a5f8-58511d0e63d0 | -10.49295 | -64.33081 | 2026-09-02 01:05:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 95e2be68-8663-36f0-9e08-6752b2ec9678 | -7.5744 | -61.30501 | 2026-09-02 01:05:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| f5706241-a92f-3d6b-99b8-e89f3beb2787 | -9.01072 | -65.40784 | 2026-09-02 01:05:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 1089d297-febe-352c-9a24-60b491250671 | -10.18952 | -69.03036 | 2026-09-02 01:05:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 11.8 |
| d99926d7-0ede-3119-a3eb-f141a7412ea8 | -8.43427 | -54.70295 | 2026-09-02 01:05:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 433.3 |
| 73667b9a-21ab-38a8-b843-8684f2c38a8d | -7.56473 | -61.36382 | 2026-09-02 01:05:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| a92e59db-6efa-379c-854d-ad9ae0bbe210 | -8.43805 | -54.74784 | 2026-09-02 01:05:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 3e6fbd21-4143-3b4f-96d0-3597de04e5f2 | -9.03204 | -65.4322 | 2026-09-02 01:05:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3964cc15-e2df-30d9-9b04-f2f838daf9d2 | -9.87268 | -64.97023 | 2026-09-02 01:05:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 064924f1-5950-3ada-ae41-3d6923f5be9c | -7.68342 | -67.11854 | 2026-09-02 01:05:00 | TERRA_M-M | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f24bea77-6f29-330a-8987-471ef59c0f0d | -6.85772 | -59.4801 | 2026-09-02 01:05:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 17.1 |
| d3779ae2-75ab-318b-9ee2-72906b682bfb | -8.91778 | -62.36916 | 2026-09-02 01:05:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 36d04033-d533-31f0-9ba3-0a6bcd56f6dc | -6.77003 | -59.42674 | 2026-09-02 01:05:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 57c256f3-5d70-30f0-a90d-5093d0c192e0 | -9.87511 | -64.98804 | 2026-09-02 01:05:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 8e3e1972-1c8e-3a06-ba89-1c7449fa6020 | -8.45291 | -62.67822 | 2026-09-02 01:05:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| baa0a3b1-51fd-3fb0-9ca8-a0835366fa18 | -8.45804 | -54.73905 | 2026-09-02 01:05:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 291.5 |
| ca1b6aa8-a17c-3241-bc44-a69696097dae | -14.49764 | -59.83558 | 2026-09-02 01:05:00 | TERRA_M-M | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 8dc6dfdf-9d7d-3594-9d3a-84347ab35f7d | -10.16883 | -69.31172 | 2026-09-02 01:05:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 5c9aacd5-e8d4-394e-9e87-d591586b8c68 | -9.00309 | -65.41805 | 2026-09-02 01:05:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 6fdcf022-cbf9-34e0-9f81-0821cf4d48bf | -8.76374 | -62.58246 | 2026-09-02 01:05:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 13.2 |
| d9247a97-bd1c-3894-b122-6084d7b18a8f | -6.68103 | -58.76262 | 2026-09-02 01:05:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 45d715f3-925a-389a-9737-db9280f3ce7f | -7.36181 | -60.60356 | 2026-09-02 01:05:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 73fae6ca-8354-3e31-a431-ea7d7087dcde | -8.55358 | -63.18444 | 2026-09-02 01:05:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2082bb97-bd4c-3b2d-a071-9ca7546fe326 | -9.018 | -65.46157 | 2026-09-02 01:05:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| dd402140-9234-30fe-b452-0d7d50b5600d | -8.4684 | -54.69743 | 2026-09-02 01:05:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 1ffd6d92-fd66-3150-8a3f-aa6501f57f65 | -13.99322 | -58.68757 | 2026-09-02 01:05:00 | TERRA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 546.1 |
| 81d842ac-59dd-3e7a-b4a8-6e5395d55303 | -8.70744 | -70.72923 | 2026-09-02 01:05:00 | TERRA_M-M | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 45a47d49-5fa8-37c2-a514-558171f28aa8 | -9.8739 | -64.97913 | 2026-09-02 01:05:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 48.7 |
| c1d29671-2f3f-346c-8f1f-4703e0435313 | -8.99814 | -67.79877 | 2026-09-02 01:05:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 63219e77-c02e-384a-b29f-5605835603e5 | -7.55944 | -60.45314 | 2026-09-02 01:05:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 6d4b981e-36a2-3682-a749-dea6abecee49 | -9.02563 | -65.45136 | 2026-09-02 01:05:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| ac4a0b1b-7e0a-347d-ae44-b759fda034d5 | -7.43794 | -61.41426 | 2026-09-02 01:05:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| c5bc736f-ef03-3d03-a637-e3f74e567c5c | -8.56406 | -63.19267 | 2026-09-02 01:05:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 104.1 |
| 85635a4b-d562-3b64-bcd8-5ecdaa2bdc73 | -7.72951 | -60.96843 | 2026-09-02 01:05:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 22.6 |
| b50033c5-9d2d-32da-8065-eb5d23729db4 | -8.472 | -54.74191 | 2026-09-02 01:05:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 170.3 |
| 5f4d89ca-03f5-32f7-a299-0900404a8f1a | -8.43148 | -54.70855 | 2026-09-02 01:05:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 380.1 |
| 55f6595d-5f1e-371f-bed5-1d7b2935817d | -8.78508 | -62.49006 | 2026-09-02 01:05:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 82c84dc8-bbf3-3687-9ae9-6a4bafded494 | -8.56271 | -63.1831 | 2026-09-02 01:05:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 45.8 |
| a09bf95d-5dc9-3078-9440-d79aa6dfdb57 | -7.21149 | -60.68238 | 2026-09-02 01:05:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 12c90efd-e5ff-318f-9649-1c1f249e897d | -9.43759 | -67.41979 | 2026-09-02 01:05:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1262b0f2-d72d-348d-9d24-0ab2abe3439d | -7.45602 | -59.93024 | 2026-09-02 01:05:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 524459b4-ffd3-3872-ad0e-d5c74a5220b0 | -7.20017 | -60.6636 | 2026-09-02 01:05:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 39.9 |
| cc87ef79-8259-3140-9474-fef717327697 | -7.50017 | -63.75772 | 2026-09-02 01:05:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 68b26370-e2ea-3ad2-ad0a-e5a75fdf4872 | -8.9163 | -62.35878 | 2026-09-02 01:05:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 65ec2922-82e5-363d-90bd-257bed0d2b24 | -6.65391 | -59.43303 | 2026-09-02 01:05:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 6b1eacb7-9984-3d5f-9d2c-12c49ebe7b66 | -10.50454 | -64.33234 | 2026-09-02 01:05:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cc4c2747-569e-33ee-b4b2-77bc0f1687cb | -9.44186 | -67.42441 | 2026-09-02 01:05:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 810a8312-d04a-39a0-ba37-ebe5e331e714 | -9.01678 | -65.45261 | 2026-09-02 01:05:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 1261adb9-41f0-312a-89ac-c6df705e47e6 | -8.93297 | -62.37157 | 2026-09-02 01:05:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 5902cb8c-6fd2-35d7-a4c9-5e5e5b1a59a0 | -9.55225 | -67.49139 | 2026-09-02 01:05:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| fa113cb2-eb62-3851-b2b3-b3fafe8b63b0 | -8.90832 | -62.3706 | 2026-09-02 01:05:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 36.2 |
| e03b3a6a-8dda-30d0-b311-8a12fa071246 | -10.94577 | -61.43147 | 2026-09-02 01:05:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |


[Clique aqui para ver as próximas entradas](README5.md)
