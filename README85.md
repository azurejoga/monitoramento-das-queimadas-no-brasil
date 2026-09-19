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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a6344b07-f073-3951-af42-2c92e4f6d579 | -6.35614 | -58.284 | 2026-09-19 04:57:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e6667a1e-1fc2-338b-91a1-db4296108c4b | -5.89265 | -52.15646 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b8ea302-57b8-3f47-90ce-3a336203909c | -6.28754 | -56.03405 | 2026-09-19 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 168efab9-bb27-3056-8fd9-810f011daede | -6.70605 | -59.45972 | 2026-09-19 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ef95b01c-9ddc-39ad-84e4-7b67476fc8c6 | -4.35671 | -47.77995 | 2026-09-19 04:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0542e963-f77f-3ab7-8f73-dad46ec8326a | -6.36443 | -58.28542 | 2026-09-19 04:57:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cd08ad67-3310-3208-b08e-b0b1433ed087 | -8.60841 | -54.61727 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 12f9cef8-7a6a-391a-84f6-4bba2c5334f1 | -6.67009 | -50.89836 | 2026-09-19 04:57:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8050c1ef-e0fd-317a-8850-fcaca81fc98c | -6.24936 | -55.4219 | 2026-09-19 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cb924a5c-0a76-3403-9070-85aa0e939c16 | -5.8339 | -52.03296 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 90d37c0a-c979-3808-b04b-44bb76b54a9c | -5.85995 | -52.06192 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 27dcfc14-bd82-3316-afc8-e1fdcaa2f280 | -9.84105 | -48.37617 | 2026-09-19 04:57:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 422311dc-76ef-3be9-b02a-eb7f264eeb9d | -6.97514 | -42.18542 | 2026-09-19 04:57:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9b6402e4-272c-3b6c-a472-b79da1b7bbd4 | -9.96011 | -46.56232 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 49e88b9b-7c16-3bfb-bea5-bdbd53b81d8e | -10.5235 | -46.71305 | 2026-09-19 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| be6e590a-72cc-34eb-9819-dcd898dd4a9a | -4.14398 | -48.22365 | 2026-09-19 04:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 84099932-bec5-3cb5-9049-9ebccf2c2a3a | -11.07677 | -48.299 | 2026-09-19 04:57:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0e19c180-36a8-3169-983b-9d95de0d7a5b | -9.94909 | -45.27354 | 2026-09-19 04:57:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2e99b1f9-9282-31fc-b0bc-68e4291bf7ed | -8.76963 | -48.67768 | 2026-09-19 04:57:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 04d3cf9a-d0f6-3698-94d9-cf7794b9de80 | -5.75169 | -57.58103 | 2026-09-19 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4b743848-59e6-327c-8e68-553ff544f26f | -7.19522 | -50.83035 | 2026-09-19 04:57:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b3cb6f5-c3d1-37df-bc02-3b7f3e1eb13a | -3.38292 | -61.30179 | 2026-09-19 04:57:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b266a7b-a98d-3884-85db-636c1f766858 | -3.2083 | -53.9508 | 2026-09-19 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 893aa57a-cc0c-3ff0-bc11-bd9ec4faf9df | -9.83983 | -50.6486 | 2026-09-19 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 52fc9cd8-5cf8-3244-8e46-a8a0c7d25046 | -3.0033 | -52.70428 | 2026-09-19 04:57:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bdd02e01-e37c-36d4-844f-e03f1752b53f | -3.48476 | -54.65976 | 2026-09-19 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 43d78eab-74d0-390f-8503-c52a076cc767 | -4.56278 | -42.97883 | 2026-09-19 04:57:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f8d9c4da-2ac9-39dd-93cd-f8f73e793994 | -3.91679 | -55.73233 | 2026-09-19 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 83a6b6ee-2a80-3fe7-a84d-2babf1102c41 | -4.35678 | -55.42575 | 2026-09-19 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b7b8488c-67d6-3ffa-8468-ef792b805c03 | -3.36367 | -50.44491 | 2026-09-19 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 245ad3df-f2e6-3bb4-b51a-3aebf8f76916 | -7.69583 | -46.10972 | 2026-09-19 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3be9393-ac95-3e16-a19a-11ef5db1b7dd | -6.79308 | -52.32644 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bb0091f6-81e2-37a3-88f5-e964229bc7ac | -4.53658 | -54.92728 | 2026-09-19 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 65b1b630-4a0d-33a5-aeec-7ff81261de19 | -9.2507 | -45.92783 | 2026-09-19 04:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f91ac23d-0c49-3680-9898-89e5622e08d7 | -4.53944 | -54.93173 | 2026-09-19 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 0e5c2dc7-a19e-3fa2-8a0b-d9fd50b139a3 | -6.01398 | -51.79189 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 49b820ab-ee87-338b-a3ad-4e8140f8b191 | -5.85499 | -52.0718 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 61971d57-f550-32f7-b6d6-7a287afcae52 | -7.55087 | -61.327 | 2026-09-19 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3618b593-ce3b-3396-9d8e-01ac5f8e1272 | -11.31099 | -46.7537 | 2026-09-19 04:57:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b70cd9d7-37ec-32ee-8549-2d09f95c5c87 | -6.36994 | -58.29008 | 2026-09-19 04:57:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ea1bf925-83d9-3502-a6b8-469596743bc4 | -11.30631 | -46.75334 | 2026-09-19 04:57:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 68c2a5a0-5b02-3d13-a4e9-abc4dc82d5c9 | -4.54691 | -42.97311 | 2026-09-19 04:57:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c1760b70-e686-3ab1-9658-83da9058e940 | -10.59188 | -46.54884 | 2026-09-19 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b2eda313-acce-306d-be92-9f5eee44f4d0 | -11.18156 | -45.38954 | 2026-09-19 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3ade73f1-2000-3b9f-be86-52aadcd7231a | -3.1895 | -57.87815 | 2026-09-19 04:57:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6230a490-4796-3149-8566-285e97387de9 | -6.93478 | -55.02367 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d54419e-4e7c-34b8-9f54-36aa62faf807 | -6.6643 | -50.93559 | 2026-09-19 04:57:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d50dfa7-ac95-3f9b-b672-70ebcf0c3c6e | -8.4994 | -57.62999 | 2026-09-19 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b7897379-fdc4-3e52-81e7-1fc561926380 | -3.69126 | -60.6057 | 2026-09-19 04:57:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 074492e1-1f57-352a-8c79-8dbff6563061 | -9.8025 | -46.10452 | 2026-09-19 04:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1663df83-40c3-315c-8f17-699f33e451db | -8.09555 | -54.98341 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a681d592-9e5e-3094-b0ad-24353a17c16c | -8.14932 | -54.80645 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eca8d312-f3bc-3911-b1da-e4f21e3388d5 | -3.36427 | -50.73656 | 2026-09-19 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf106923-3b9c-3c7f-9b21-c2f7aa43acca | -7.57449 | -44.91193 | 2026-09-19 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 515b1b38-1d0d-32da-976f-09000a6e09b6 | -6.45166 | -59.9863 | 2026-09-19 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1808e0b2-470a-39d6-84eb-428347be1dd0 | -8.387 | -47.20352 | 2026-09-19 04:57:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f277c52a-5dcc-35a3-9cc6-095c7513426a | -7.58021 | -43.44515 | 2026-09-19 04:57:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a1de1271-2be1-364f-8917-ef8348c78520 | -3.3597 | -50.44804 | 2026-09-19 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3b27c2f2-fa57-37c0-9ddd-44b3aed82f9a | -7.74265 | -47.30599 | 2026-09-19 04:57:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dd88ee9f-2685-3d09-8a1c-aef19613d88c | -4.53529 | -54.9351 | 2026-09-19 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0d86f5fd-480a-3fa3-a862-dfa0ec674f91 | -7.835 | -55.41561 | 2026-09-19 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f80eaed-e6fa-374a-a4ec-645f2cc645a4 | -7.2161 | -49.63663 | 2026-09-19 04:57:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 502e5471-4d9a-3113-b8be-dbb2ff51bf7b | -4.49461 | -54.98138 | 2026-09-19 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f9112769-2731-3f74-bea8-9798347377fc | -3.36989 | -50.44962 | 2026-09-19 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60bbf28c-1093-37cc-800e-fecc8675a3df | -6.37433 | -58.31409 | 2026-09-19 04:57:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d77ab02e-8100-3f0f-a09f-b71fb2d5dc21 | -8.41678 | -54.73428 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 80c2768e-48de-33fc-9411-39334200e6e4 | -8.35545 | -47.54299 | 2026-09-19 04:57:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 53a787cd-e5db-3d6e-b1a3-254965a62840 | -6.36604 | -58.31266 | 2026-09-19 04:57:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 875e7a11-6b4f-3438-82ff-30b44a408e09 | -2.81681 | -54.49062 | 2026-09-19 04:57:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9fb62a8e-f522-3e03-a717-6d8c77b63af9 | -6.36857 | -58.28614 | 2026-09-19 04:57:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| afb86625-b080-3071-b5dd-4c1f5f07ae20 | -9.04047 | -48.71353 | 2026-09-19 04:57:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 92117232-9de6-3a2c-b081-d50057f29db3 | -6.0217 | -51.76425 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 430f294d-d216-3f71-8f6d-107052541666 | -7.5847 | -43.45354 | 2026-09-19 04:57:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 273618b5-0e93-3d1f-b0c8-c07f3283f0f7 | -10.55945 | -51.31946 | 2026-09-19 04:57:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ce54ed6-057b-3d1e-8600-c2f162fec34e | -11.00127 | -48.3224 | 2026-09-19 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 0ce4d4ed-9ae6-339f-804c-2b27a8634bdc | -6.70823 | -59.46257 | 2026-09-19 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4088560b-d866-3d59-9959-aeafa084c0c7 | -3.35742 | -50.46259 | 2026-09-19 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cd96e81f-ae0f-3b1d-bec6-b3132d98916c | -4.35988 | -47.78557 | 2026-09-19 04:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d30f0e12-08c7-3b66-80f7-98fa6b1a3e59 | -9.71161 | -54.81837 | 2026-09-19 04:57:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dca8b314-4120-3764-8449-48488dd663ad | -9.35265 | -50.11003 | 2026-09-19 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dc54fdb1-f6e4-32cc-a965-6695088dc4b9 | -9.70708 | -54.82504 | 2026-09-19 04:57:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d32db733-1e4f-34c2-b4bd-56a3c56f59ac | -11.33084 | -47.68136 | 2026-09-19 04:57:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0fb38f14-acbe-3bbf-875b-ef08c40ea5ee | -7.56507 | -49.60072 | 2026-09-19 04:57:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc816b92-033d-3d61-ae9f-49b23ee25c56 | -8.78071 | -48.68166 | 2026-09-19 04:57:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 8.5 |
| f3d660ec-a5b3-36bb-b5ca-c96724664427 | -10.70467 | -50.25474 | 2026-09-19 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3f85fb4d-48c0-34c7-96b9-ba0f68c9d7b5 | -2.89401 | -54.18514 | 2026-09-19 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d6efbd7-ecaf-3825-bf44-b921bd77184b | -7.67404 | -46.13079 | 2026-09-19 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ebf40f18-510a-31ca-a7c7-78d6cc2bcfae | -8.41795 | -54.72704 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1fe410f2-c7ce-309f-ad31-2e15cd53513f | -3.69273 | -60.5968 | 2026-09-19 04:57:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5bb273e9-fcee-31d0-ac15-f4d4db78a51a | -8.29657 | -50.81613 | 2026-09-19 04:57:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| edbcc7b9-8934-348c-9d5b-48988bc50fce | -8.60897 | -54.60286 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6bb4ab93-5ccd-3d62-b73c-5a7682850cb4 | -4.42683 | -55.51783 | 2026-09-19 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eab6f250-8063-3b9e-86f0-c613e52623c8 | -11.80164 | -46.7913 | 2026-09-19 04:59:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ba63433c-3b04-3a14-a4d4-c337616a9051 | -15.02835 | -48.56863 | 2026-09-19 04:59:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6802de21-f85e-3fe3-b853-8f3b7a3fbb1b | -11.05829 | -49.7555 | 2026-09-19 04:59:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2723128a-9054-38c8-b4a7-7f653fed6c28 | -12.57757 | -47.09261 | 2026-09-19 04:59:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 927519e0-c5bc-303a-9273-4a07c85e940a | -14.92273 | -49.91917 | 2026-09-19 04:59:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 23.9 |
| e9313803-b9a1-36fb-af2d-20d22466a571 | -11.55364 | -46.89802 | 2026-09-19 04:59:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 03902620-f38b-3f08-a04b-568f5066648a | -15.05242 | -48.60063 | 2026-09-19 04:59:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b427d619-0be1-3f70-9eae-b445ec7f8442 | -12.19856 | -46.4862 | 2026-09-19 04:59:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README86.md)
