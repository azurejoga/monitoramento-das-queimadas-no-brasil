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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5d9c9a66-bb6b-3e5e-97a0-fb47c2b284b5 | -7.82674 | -45.09032 | 2025-08-06 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 91055fc0-13af-3a12-b692-7803f82f6b1f | -8.00642 | -43.22635 | 2025-08-06 04:19:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 37d5e0e4-a06d-3477-a604-57f1e9058f59 | -6.92279 | -43.68396 | 2025-08-06 04:19:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 58e91ab0-3900-3876-987d-2ce0027bc818 | -6.98698 | -43.39236 | 2025-08-06 04:19:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5181d916-0e2f-3ed9-844a-b93e1496db5b | -4.81882 | -47.3211 | 2025-08-06 04:19:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6793e9d3-ca0e-3b77-a744-c24c3b5aff27 | -7.22552 | -44.48365 | 2025-08-06 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ad2a73e6-24a5-3b75-b452-b466248e39b0 | -6.72223 | -43.57677 | 2025-08-06 04:19:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b172649b-af8f-3f48-b1df-933ffad13976 | -6.72503 | -43.58086 | 2025-08-06 04:19:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 2505dfc3-0637-31d2-9a0e-1cdc9dd67af3 | -7.64155 | -44.58117 | 2025-08-06 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 82759518-459c-33a0-874e-26debe029ff9 | -6.20168 | -46.4571 | 2025-08-06 04:19:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1394beb0-b899-30dc-9ea2-0da2788c0868 | -7.83114 | -45.08392 | 2025-08-06 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ed113810-6dd9-337a-957c-4873704d2214 | -7.63439 | -44.5836 | 2025-08-06 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e83c13f3-e60d-39fc-a3a4-f3c9aba41adf | -8.37719 | -45.79785 | 2025-08-06 04:19:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f8f5f589-549f-3ce1-9279-aaa6cb534843 | -7.90939 | -45.53358 | 2025-08-06 04:19:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 49d790a3-beaa-33ce-9bab-982b2df8e32b | -9.06822 | -45.05635 | 2025-08-06 04:19:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 50b5ed7e-9b47-3403-8af1-36dcef184c4c | -7.18769 | -45.47861 | 2025-08-06 04:19:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7056bfc1-32f6-3fd1-9c5d-453f806e953c | -9.07098 | -45.06037 | 2025-08-06 04:19:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2f1aadb5-ac3e-323b-b16a-25998670b9f4 | -9.69771 | -48.87135 | 2025-08-06 04:19:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| b85a8b10-bcbe-32bf-b720-486053ba24a6 | -8.00698 | -43.22264 | 2025-08-06 04:19:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| f78b8c06-0812-3526-9219-3789726bbbd8 | -11.04129 | -47.6161 | 2025-08-06 04:19:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5ccf3148-0722-3dc3-9404-ba16d2c15b56 | -6.41317 | -53.36754 | 2025-08-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 69415f91-e0de-30d0-980e-20e41de033e1 | -5.75475 | -45.10838 | 2025-08-06 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d6f3d079-693f-35a2-a355-b7fb5d530ba4 | -8.56302 | -47.45092 | 2025-08-06 04:19:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c6f2510-a441-3571-ab43-85f2d6984d27 | -6.95582 | -41.58417 | 2025-08-06 04:19:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4971f394-c02f-3433-8595-96737f43b85c | -11.76134 | -47.53018 | 2025-08-06 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 80ab31a6-37e1-3620-a9aa-092fdb9c079c | -9.46515 | -57.85423 | 2025-08-06 04:19:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7cfa412f-e270-3549-9906-599065264ca1 | -5.94119 | -42.55902 | 2025-08-06 04:19:00 | NOAA-20 | ÁGUA BRANCA | PIAUÍ | Brasil | 2200202 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 16d94d21-021e-371a-ba54-6473d4b70c73 | -7.99732 | -43.24014 | 2025-08-06 04:19:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5d0196cf-b97b-387d-b054-1b26c2c2a4a5 | -11.64666 | -50.15382 | 2025-08-06 04:19:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 268dbd9f-2d56-3dbb-be75-610845cd8c52 | -8.06289 | -49.71481 | 2025-08-06 04:19:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aec77fee-d81a-3cc2-8e20-5f32f92b6266 | -11.91683 | -44.92279 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1a4faa08-7cb2-3dae-acbd-5cc6cf2a64a7 | -11.44253 | -45.13713 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 24e45e6d-c046-3d4e-bb8d-f7151cb335dc | -7.305 | -44.67017 | 2025-08-06 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0bdf5e65-f7e7-3638-a446-a2e04f68e6d4 | -7.98936 | -43.15617 | 2025-08-06 04:19:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 247ff81f-5a16-3348-9472-f17facd0344c | -9.07208 | -45.05339 | 2025-08-06 04:19:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0c3c6744-d6ac-3822-b5af-e69b9c5c349c | -7.64432 | -44.58517 | 2025-08-06 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b65a0f8-e839-3571-a915-4a6e10c59d52 | -11.72343 | -47.52016 | 2025-08-06 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bf9ee493-d816-3aa6-b73b-fc34e15d792f | -6.59883 | -44.03902 | 2025-08-06 04:19:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9c9dc9f6-da2d-38b7-b870-3fdd5de03797 | -8.85085 | -47.46964 | 2025-08-06 04:19:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 632cdeb8-a9f9-3533-9d55-5e9b9d52642b | -6.41772 | -53.37155 | 2025-08-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d288de10-6bc2-39f0-8712-6db7aed7ccf3 | -10.4726 | -44.34034 | 2025-08-06 04:19:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e766af65-06cf-3e61-9067-54005d949e40 | -7.98593 | -43.15561 | 2025-08-06 04:19:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 18f96cba-fd6d-3eec-805b-a8a8e69e6dc5 | -6.6805 | -49.78181 | 2025-08-06 04:19:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c744b5a1-f6ea-3cbd-aa34-bfda36263f29 | -10.58911 | -45.25487 | 2025-08-06 04:19:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4ead6617-7fe4-3b31-95e6-efd72bf09e8c | -6.25131 | -43.0693 | 2025-08-06 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6e0fdd3a-d91a-3408-80b4-723e12d683f6 | -8.84803 | -47.46529 | 2025-08-06 04:19:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b9858adb-6e43-3ad1-883f-f682e5acc80d | -9.02793 | -51.13009 | 2025-08-06 04:19:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09655e13-da42-30a8-9b7c-d4d80a3d812f | -10.46877 | -44.38777 | 2025-08-06 04:19:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4d5b4670-f5da-3206-ab77-741eee76264d | -11.90624 | -44.96928 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0dc4813a-978f-3d83-8042-9eab9b51a6fd | -9.62331 | -43.85222 | 2025-08-06 04:19:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 38b87c1c-8dce-3b1e-804e-a3ea3bb8bda6 | -7.1436 | -44.07376 | 2025-08-06 04:19:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 633d76eb-c46f-3b18-b742-89e45b71bb3e | -11.72563 | -47.52801 | 2025-08-06 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 34f61edd-409e-3f1d-ac26-d36f84bad3af | -8.23866 | -45.0634 | 2025-08-06 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 17e2ef16-46fc-3a30-b0ea-cf3bac57ec20 | -7.70806 | -45.13151 | 2025-08-06 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1587f2dd-debe-3d54-bc80-c200ff84f135 | -10.44573 | -44.35835 | 2025-08-06 04:19:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 971ea531-73ce-363f-bcd0-6604126d701c | -9.61992 | -43.8517 | 2025-08-06 04:19:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c8b62ae6-e21c-3b02-bca6-ef904776b70d | -7.99829 | -43.14104 | 2025-08-06 04:19:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ad448069-1f42-319c-90ce-a21c2f6063f9 | -6.78292 | -43.23891 | 2025-08-06 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7589ec54-c6ad-360b-9fd7-3d66b02d403b | -11.62934 | -47.71275 | 2025-08-06 04:19:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d2e58538-32c9-30e3-b55c-4ca09494c454 | -11.83562 | -43.72553 | 2025-08-06 04:19:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 05648da9-bc15-330d-b631-b3f072e22780 | -7.51368 | -44.85616 | 2025-08-06 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 14f97c0e-650a-3721-b038-d88ac94161f4 | -6.41717 | -53.37462 | 2025-08-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68dab094-e76b-3ef8-b657-b335bdee6e05 | -7.83243 | -45.22618 | 2025-08-06 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8594a67d-c98c-3cb2-8995-3aaf2532d4e9 | -12.55094 | -44.74201 | 2025-08-06 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 43be99c3-1301-3b9f-a63e-a1bee911f059 | -11.90741 | -44.98395 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 36e7912e-251d-3400-a3a9-11ac9f027d2e | -9.07539 | -45.05392 | 2025-08-06 04:19:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b0521d03-0ce4-340c-87b1-492b615c1b59 | -9.1814 | -48.84073 | 2025-08-06 04:19:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 82855074-a528-3ba3-8fb9-bce25020b99d | -6.29222 | -45.74434 | 2025-08-06 04:19:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b5d08786-4092-3179-b952-35c194acf2ba | -11.76134 | -44.96128 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 66bf6e67-6f93-386e-9298-7b88c07d5761 | -11.76074 | -47.53384 | 2025-08-06 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 91838379-84d6-31ad-94fc-8578966d983c | -8.41716 | -47.43892 | 2025-08-06 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e83e639b-72c8-33e8-aed3-5937a40f7ffe | -10.70661 | -48.30688 | 2025-08-06 04:19:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 98c58322-d887-3831-9d66-6215a05cb10f | -11.02899 | -45.06805 | 2025-08-06 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0c98b9ad-c79d-35f1-80a7-5937a4a9ed5f | -4.79369 | -48.59022 | 2025-08-06 04:19:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e9e31ff0-82c6-3da2-b3b2-a48296f32e46 | -7.7053 | -45.12753 | 2025-08-06 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6c13fd1a-70b8-3ec0-bdcb-e3feeefca4d8 | -11.63552 | -47.71759 | 2025-08-06 04:19:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c2e19d7a-4588-3e67-9cfa-dbc2276b31ba | -8.52446 | -47.44856 | 2025-08-06 04:19:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9a738b2f-b126-31e0-89cb-cb8de82aaf95 | -8.24473 | -45.06791 | 2025-08-06 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 55594c34-adc2-320d-81ff-752faeacf3fc | -5.6776 | -50.26119 | 2025-08-06 04:19:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0f8d3ee1-5d79-3ad9-895b-c3e568290c6d | -8.51415 | -43.31768 | 2025-08-06 04:19:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 2961a74c-beb1-3b8e-8c1e-0737286d8fe5 | -10.48269 | -44.34196 | 2025-08-06 04:19:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 12f5d819-5d57-3a60-b652-fbbf2183fbf3 | -12.04032 | -44.0198 | 2025-08-06 04:19:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a5f2cc1b-4592-366a-8f1c-4497787ff63e | -12.09102 | -44.73102 | 2025-08-06 04:19:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 217f0fe6-4b89-334c-bca1-46c5bb115b51 | -5.79894 | -46.99596 | 2025-08-06 04:19:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 53f3b42d-2cc1-3ad7-b8c7-6177cd92ca6e | -10.3291 | -47.82858 | 2025-08-06 04:19:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7b07976a-ee43-3c7a-ba61-61ddbba6b26f | -5.80997 | -46.99383 | 2025-08-06 04:19:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f76e0c8-8204-3420-81f5-377c0d035fc6 | -8.00814 | -43.23801 | 2025-08-06 04:19:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 312464c0-3424-3376-8048-eb75151c7074 | -11.02622 | -45.06398 | 2025-08-06 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 5d98dfc1-c00d-3a5b-bda5-1a0e1a1a7772 | -10.70725 | -48.30302 | 2025-08-06 04:19:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 36008908-4583-336d-9d45-b49d910adf9b | -5.93717 | -42.56226 | 2025-08-06 04:19:00 | NOAA-20 | ÁGUA BRANCA | PIAUÍ | Brasil | 2200202 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 22393833-7b22-35c0-a14b-8dd6cf1f9d4d | -7.66755 | -45.1079 | 2025-08-06 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 11d9107f-5c18-3bbc-a468-546058735dd7 | -8.84397 | -47.59771 | 2025-08-06 04:19:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fbed66c2-7a2d-38cf-9c76-2fbdb2bc768e | -9.07484 | -45.05741 | 2025-08-06 04:19:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 41f25226-8536-37d2-a1ea-c1cab7857776 | -9.69697 | -48.87572 | 2025-08-06 04:19:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 6051140c-c7d4-3456-85bd-557ac6665a42 | -7.30941 | -44.66373 | 2025-08-06 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bca8a3b3-d33a-38d6-a1a7-dc54bc99cead | -6.85465 | -44.29337 | 2025-08-06 04:19:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b1811dbb-e5d9-3b1a-841e-7ab8a2ee7a86 | -7.14638 | -44.07775 | 2025-08-06 04:19:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a53d4ec2-277f-34db-bb9d-17e4a03890fb | -5.5762 | -46.52861 | 2025-08-06 04:19:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4821b063-bed0-34a4-a900-b2b677f457a5 | -6.63447 | -44.13762 | 2025-08-06 04:19:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| edf637ba-9fb0-3c05-96aa-23c817ef52b8 | -6.74413 | -45.29756 | 2025-08-06 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |


[Clique aqui para ver as próximas entradas](README18.md)
