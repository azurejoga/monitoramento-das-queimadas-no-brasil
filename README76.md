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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eef1c8dd-b306-3ce5-b894-dc6be901c6c9 | -8.91221 | -66.95235 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 72000ada-8d73-3f11-a2de-b6e8be4cd085 | -9.04803 | -65.44763 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c23b4e01-6d5d-31e2-a619-e58d6f83e104 | -9.08435 | -65.48849 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 615e5ce6-bb81-37f8-8405-be3d103e8593 | -9.17527 | -59.63178 | 2026-08-31 05:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| af842312-4e1e-3140-92ed-19f7eb0a0544 | -8.54428 | -70.50359 | 2026-08-31 05:55:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4abe625e-45fe-3bb0-b386-ce0821e6fc2e | -8.68071 | -62.81343 | 2026-08-31 05:55:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6914c91-797a-390a-8fe6-0eff2b4de6b6 | -3.62233 | -60.56919 | 2026-08-31 05:55:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 822ab3a0-f654-380e-b2fc-06bc6f9c9ec7 | -8.79607 | -62.49807 | 2026-08-31 05:55:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e35396eb-c5ff-3fb5-a329-adb26aa0a305 | -8.87145 | -66.78002 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0a76bdc9-3f77-398f-99d0-fff54929aefc | -8.93959 | -62.3707 | 2026-08-31 05:55:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bf6a9f62-5c79-3d99-a581-6a25f0766f2c | -11.0295 | -57.24141 | 2026-08-31 05:55:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 73dedafb-ba56-3cef-82d1-26040b39d9d9 | -4.95768 | -55.85224 | 2026-08-31 05:55:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 08a01466-027d-32a4-a15a-e5def10bb77e | -4.15627 | -60.69738 | 2026-08-31 05:55:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 693584f3-7f29-33e3-aea6-476460496873 | -10.17687 | -69.06545 | 2026-08-31 05:55:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 984dbbe6-f26c-3e1f-83aa-a0879145ee07 | -8.58101 | -66.9652 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bf52fd16-1286-3d40-a9fc-fca4547223f6 | -7.87516 | -71.78745 | 2026-08-31 05:55:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d8daf145-4184-3038-8019-585734b550a6 | -9.03202 | -65.39909 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5065d776-6f2c-34ab-91cc-99a20f7b9e55 | -8.96797 | -62.39958 | 2026-08-31 05:55:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 41514763-e274-3046-ac11-fb682054e8ce | -8.87272 | -66.90297 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af1ad61c-b76f-38b3-a2ab-2332f9cf51d5 | -9.06647 | -65.48965 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a149443-b1ff-3c20-93b1-5611f275027b | -9.15621 | -59.54811 | 2026-08-31 05:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3eb186fa-e255-3fdd-8aec-dcf4a95ae7ad | -10.48338 | -59.61618 | 2026-08-31 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7beac6d4-81d3-3591-a12c-486ce73270ae | -11.03432 | -57.25116 | 2026-08-31 05:55:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f5183d7-bcd3-3b62-9798-da43f61e0fdc | -8.00734 | -70.06419 | 2026-08-31 05:55:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7bed556f-6891-32e1-a152-e3479a60ad8c | -3.60989 | -59.07547 | 2026-08-31 05:55:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 52828515-5aea-31e4-ac95-4fce6df9cb44 | -9.48545 | -66.63197 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc831aad-592e-3b53-96e4-3e0532783a0b | -11.49376 | -60.58033 | 2026-08-31 05:55:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 19cc1775-4077-3dab-a297-0dd634c293fd | -10.48378 | -59.61322 | 2026-08-31 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bde18461-96f2-3593-b81b-07f5601fb71c | -4.14337 | -56.33035 | 2026-08-31 05:55:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 21009851-a778-38c6-a494-971a9ab33e44 | -3.96935 | -60.02613 | 2026-08-31 05:55:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3e9533e3-b87d-34f4-bcb0-a7bcff6f8578 | -9.00355 | -65.44578 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 949153f8-a18c-3de4-b762-7f74e745ff10 | -8.40278 | -62.66367 | 2026-08-31 05:55:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3cfae879-b360-357d-b3a5-adcadfd8ec60 | -9.40127 | -60.59149 | 2026-08-31 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e76b060-c4f6-3e28-8abf-944e12a2e463 | -8.9383 | -62.3728 | 2026-08-31 05:55:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eb0ae822-eb0a-3e71-81bc-e8a29939fede | -11.95476 | -63.28979 | 2026-08-31 05:55:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d6a1c03c-d999-3f94-a2c5-bb7781624aad | -9.15181 | -59.50498 | 2026-08-31 05:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 66dd1c97-16d5-39b2-9dc5-4b087111fc58 | -8.68011 | -66.52544 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f7447139-809d-370e-9e95-7ed87d8a2f58 | -4.58533 | -55.94365 | 2026-08-31 05:55:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fbc56cb8-33d2-3444-bc94-26e6d9626afc | -9.0463 | -65.43559 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 76138ef0-d40c-327a-b652-f062d5d2c0f4 | -10.0908 | -68.28719 | 2026-08-31 05:55:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e2515a63-b8b7-38a1-aa57-e41ee2fba576 | -3.63698 | -60.55902 | 2026-08-31 05:55:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4988f50c-3d2a-3a42-a401-07ef1e03717f | -8.60667 | -70.21148 | 2026-08-31 05:55:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f6dd5b22-3963-3af5-a43f-dfd6e8b91ab5 | -8.5871 | -66.96974 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b48f7951-1d56-38fe-92b9-46021786c8d0 | -3.25888 | -60.65976 | 2026-08-31 05:55:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7614513e-db42-3adb-a003-b918319023a7 | -4.13764 | -56.32938 | 2026-08-31 05:55:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f36efff4-ba03-331e-8ae3-2476bed67537 | -8.52004 | -67.18074 | 2026-08-31 05:55:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85e2e686-acde-3f6b-9d17-6a0d2baa1238 | -9.85711 | -64.98685 | 2026-08-31 05:55:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a416341-22ea-3a16-97b2-5212b633d8be | -11.49856 | -60.58102 | 2026-08-31 05:55:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3e18ca1c-d8a8-39d0-be67-b1aab74fa9e3 | -9.89077 | -60.28401 | 2026-08-31 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3d931c81-f1e7-329a-8130-056b23b072fa | -9.16388 | -59.37589 | 2026-08-31 05:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 16b3d417-bc72-38e4-9788-0851eca6f900 | -8.58046 | -66.9687 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5861ceac-6309-3bc9-a262-15adb8469992 | -8.95112 | -62.3709 | 2026-08-31 05:55:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f01f3857-07c5-3217-8d0f-3ef7f9057930 | -9.94252 | -60.5201 | 2026-08-31 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7fa822a8-89a7-3dfb-914e-1ddd98093a89 | -3.88621 | -59.40429 | 2026-08-31 05:55:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 75b8bd8f-b266-3f26-ac67-6fdd9db1d1b8 | -4.152 | -60.69675 | 2026-08-31 05:55:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1d09780a-dec4-3d49-9443-022a9432846f | -9.15199 | -59.54166 | 2026-08-31 05:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 76ec9446-b73b-38d8-bfb7-8b7f57d537cb | -9.90789 | -60.15269 | 2026-08-31 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c272f680-c2bf-3b32-a015-bb32b9758f68 | -14.42179 | -56.27449 | 2026-08-31 05:55:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1aede30f-923f-3aaf-b574-cc2e97d09b05 | -9.04394 | -70.63634 | 2026-08-31 05:55:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b1044328-1f9d-34b5-aa3b-c8d6b0c505c7 | -10.48962 | -59.60813 | 2026-08-31 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35d6fbaf-31ce-38bf-b154-717d9fa6fd44 | -3.11074 | -61.23256 | 2026-08-31 05:55:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cfd83e7b-5d36-349c-b395-6ae514757562 | -8.97006 | -62.38493 | 2026-08-31 05:55:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 93bdaa61-136d-3e7e-99e2-a73f79c36730 | -15.6729 | -56.27848 | 2026-08-31 05:55:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 35bf121f-db5d-3359-a923-21433aebf2a1 | -9.14091 | -61.0994 | 2026-08-31 05:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 12a13f5c-37f5-33dd-badd-e67688517af6 | -3.62721 | -60.56581 | 2026-08-31 05:55:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a1242bd7-97fb-3bbc-8c33-58067133dad4 | -8.70518 | -63.96612 | 2026-08-31 05:55:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e24cd25b-72d0-3a74-b059-9749acae7ab3 | -8.37554 | -70.09441 | 2026-08-31 05:55:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f17b80e0-31dd-31c7-82c5-f1962a22b111 | -9.04919 | -65.41637 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ba149ed-70cd-343c-a2c1-170e0a03642c | -9.01349 | -65.40413 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5447ecb4-bf97-3a7a-b7ad-5b0b38e0e8f0 | -9.72192 | -65.00163 | 2026-08-31 05:55:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 409072af-a764-38fd-a8a9-c6c2236600fb | -9.00867 | -60.59816 | 2026-08-31 05:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 481880c5-03f5-3907-9658-195f4797756d | -8.8705 | -66.8954 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 426d2a03-0ad3-35e0-a0bc-afc8fcfd8b40 | -2.97992 | -60.92268 | 2026-08-31 05:55:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e2bd7d3-61fd-3453-9823-645e4ea0777a | -10.64957 | -68.70257 | 2026-08-31 05:55:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e682c873-d138-36ad-bbcf-04a4bcf6c0f3 | -8.2544 | -70.52012 | 2026-08-31 05:55:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4eccd5f9-3e62-3ddd-a86f-55e15ac446d0 | -9.8484 | -60.27258 | 2026-08-31 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 67d704e7-5a43-3119-bcad-a50d498dfa52 | -3.11184 | -61.22542 | 2026-08-31 05:55:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7e954e49-6d4d-3b5b-a759-b51bc4205ef9 | -4.14713 | -60.70012 | 2026-08-31 05:55:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0883570a-cab8-39fe-85ae-f6c717c45318 | -8.95164 | -62.36721 | 2026-08-31 05:55:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ecdecda9-36d5-3ed7-babb-7adb801bc14f | -8.78432 | -71.0284 | 2026-08-31 05:55:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e85edeea-a3e1-3c2c-a6f8-2784582d12c5 | -9.05324 | -65.41305 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 209b0e3b-35a3-32ed-963f-b2df048ceba1 | -8.79766 | -62.48725 | 2026-08-31 05:55:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d9eb4c3f-d69d-3408-903a-d021597a462a | -9.48936 | -66.62892 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6537f805-13a7-360d-b331-8d2eb8ee9ced | -9.85439 | -64.98765 | 2026-08-31 05:55:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93c4c896-ca00-312e-97cd-d5e0a57f88f3 | -8.7221 | -70.54404 | 2026-08-31 05:55:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6718c17b-5e0a-3212-9d8d-dcaeeba82a02 | -8.68395 | -62.81915 | 2026-08-31 05:55:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 165246b9-8d93-3b01-b8bf-49f86c294373 | -4.1502 | -60.70875 | 2026-08-31 05:55:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6bc6a9ea-3f23-3c23-9768-e27e5e5402a8 | -4.14773 | -60.69611 | 2026-08-31 05:55:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a06c7854-ae28-3f02-a081-474dc7a891eb | -9.05843 | -65.42566 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b6e91fb-8153-3aaf-ba65-576895b237cc | -9.84076 | -64.9814 | 2026-08-31 05:55:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 35e10271-da66-300c-ad8e-757d19c2e243 | -9.0567 | -65.41358 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4fff00c8-820e-3a27-b29e-090a6bbcd6de | -9.7973 | -60.18391 | 2026-08-31 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb7b6488-44ff-30bd-877f-683f71442df4 | -9.89151 | -60.2787 | 2026-08-31 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0f19b836-1416-3026-b54e-653a62f1d8bf | -9.03994 | -65.43069 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d65de73-a348-3db4-90a4-c06f45e65a2f | -8.09185 | -63.83836 | 2026-08-31 05:55:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1fb62d43-9cc9-3cf5-a776-7eb5c8fab4ce | -9.89225 | -60.27343 | 2026-08-31 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4df14eca-26d7-3781-b7da-c85d0106aa7d | -9.15681 | -59.50566 | 2026-08-31 05:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fd7d7464-4d1f-3925-8953-4e6d771e78f1 | -10.08637 | -68.29366 | 2026-08-31 05:55:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a35cf085-62e2-30a3-86cb-66173c007c45 | -8.63076 | -70.57158 | 2026-08-31 05:55:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d530b920-a464-3a6f-bf06-988985b90f8b | -8.91554 | -66.95288 | 2026-08-31 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README77.md)
