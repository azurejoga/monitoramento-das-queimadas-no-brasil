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
| 9da21d1b-2766-39a9-92e6-77f4a797539b | -18.88892 | -40.17575 | 2026-06-11 03:40:00 | NOAA-21 | JAGUARÉ | ESPÍRITO SANTO | Brasil | 3203056 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5492a076-6433-3212-b28a-ed5a6d33430d | -17.36283 | -42.1824 | 2026-06-11 03:40:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 16bfdfb9-dc4b-307c-8ede-3e053169e114 | -20.25932 | -41.85424 | 2026-06-11 03:40:00 | NOAA-21 | MARTINS SOARES | MINAS GERAIS | Brasil | 3140530 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| eda9bbf9-3eed-3530-bc18-3a388e5b87ed | -20.61454 | -42.89205 | 2026-06-11 03:40:00 | NOAA-21 | TEIXEIRAS | MINAS GERAIS | Brasil | 3168507 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 56c73a5e-f62e-3226-8601-7499472106be | -19.0742 | -42.00224 | 2026-06-11 03:40:00 | NOAA-21 | ENGENHEIRO CALDAS | MINAS GERAIS | Brasil | 3123700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 30af0822-4c02-31ca-b67b-b00ea09b2a1e | -20.61378 | -42.89315 | 2026-06-11 03:40:00 | NOAA-21 | TEIXEIRAS | MINAS GERAIS | Brasil | 3168507 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| aaa477fd-d828-3e61-882d-a18c2f25043c | -19.46058 | -39.83855 | 2026-06-11 03:40:00 | NOAA-21 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ce26c9cb-9f77-3535-8bc5-1145f59bdb92 | -9.3234 | -45.4787 | 2026-06-11 03:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 232f1584-8e9f-3a07-899d-f96a7a4beb63 | -6.4357 | -44.5535 | 2026-06-11 03:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 65341f35-e5bb-37d3-b3c2-7f3e264486c3 | -6.4355 | -44.5764 | 2026-06-11 03:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| aa04031c-4667-314b-908e-a93cecdc7755 | -6.4355 | -44.5764 | 2026-06-11 04:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| e7cf756c-0bae-3651-aeee-87f41aa83cca | -6.4357 | -44.5535 | 2026-06-11 04:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 08fc098f-9781-32ec-87fe-8c7f45888f1c | -9.3234 | -45.4787 | 2026-06-11 04:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 4badec10-67b1-379e-99b7-43d749e940ac | -9.3234 | -45.4787 | 2026-06-11 04:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 84.2 |
| dc44c9d6-ef0c-31e1-a50d-6b2ad6c447ec | -6.4357 | -44.5535 | 2026-06-11 04:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |
| f32e72b1-2c7c-3cc1-9f3e-859e34be481a | -6.43689 | -44.56261 | 2026-06-11 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| c149ca0f-9f08-354b-a2c5-485cb2954efc | -5.52154 | -37.48402 | 2026-06-11 04:10:00 | NPP-375D | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f8c53d15-314a-3b15-9a74-1967ce7a4f22 | -6.44227 | -44.57838 | 2026-06-11 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 842224ef-0da5-3772-af6b-388de116cef9 | -6.44777 | -44.56927 | 2026-06-11 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 4449493e-4525-3559-a697-b614f27c6340 | -6.44387 | -44.56868 | 2026-06-11 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 6b672d0a-dcd0-3b84-8505-37b04dc0214a | -6.43997 | -44.56809 | 2026-06-11 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 2fd90e62-5f32-30f1-9700-edcfb417210d | -5.0436 | -43.26257 | 2026-06-11 04:10:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 335d41f0-43f5-3306-a1ce-48298279247d | -6.43607 | -44.5675 | 2026-06-11 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 53f46d0a-4879-350b-ad47-e865270e1afb | -6.99648 | -43.86448 | 2026-06-11 04:10:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 462a2b0b-7c9c-3f98-877d-c7dfea5ff03d | -6.43837 | -44.57777 | 2026-06-11 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 80670fe8-b695-31c2-8bc4-135206c37d5a | -6.43447 | -44.57719 | 2026-06-11 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4371939a-8e83-3a87-a841-1850635f41d7 | -6.57504 | -47.919 | 2026-06-11 04:10:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| efbebaeb-d469-3ef5-a878-103c95ea89f7 | -3.50866 | -48.03703 | 2026-06-11 04:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8ea334e-3894-36e1-b39d-80d09a8bd0d8 | -5.0429 | -43.26689 | 2026-06-11 04:10:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cd4d6199-5510-3745-bb7e-d9014e3f7e4c | -6.43917 | -44.57295 | 2026-06-11 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ee5842c1-9c46-3e74-a74e-a0c46882b28c | -6.18749 | -44.86173 | 2026-06-11 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bf221a2b-133b-3474-87fe-f4929e273bc4 | -6.57604 | -47.91334 | 2026-06-11 04:10:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a1653ea9-abbe-337a-92ab-f80399bf2a03 | -6.19148 | -44.86235 | 2026-06-11 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2a8c2093-2cfd-3151-8aab-f9ea7ce1a0f5 | -3.51028 | -48.03837 | 2026-06-11 04:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8c85a360-dc5a-3315-8988-11dc956bb02d | -5.6111 | -37.53259 | 2026-06-11 04:10:00 | NPP-375D | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f3ed7226-c8bc-39bb-812b-1afe470c62ab | -7.47609 | -36.60541 | 2026-06-11 04:10:00 | NPP-375D | SERRA BRANCA | PARAÍBA | Brasil | 2515500 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4a11ae36-452b-3f66-a2bf-a0049be7986b | -6.56635 | -47.91161 | 2026-06-11 04:10:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| af46a625-5b8c-3dcd-b18c-3002fcda9a2f | -6.72867 | -39.27436 | 2026-06-11 04:10:00 | NPP-375D | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 10.3 |
| c63fd5d5-ed3a-3f20-8c0e-2e2cdedee947 | -5.73166 | -49.09967 | 2026-06-11 04:10:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5d85dafd-bbb8-33ec-bf66-08b0023ff92c | -4.36476 | -37.90047 | 2026-06-11 04:10:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e3c329db-4c80-3732-a21c-4095a2a7660f | -3.50298 | -48.03941 | 2026-06-11 04:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3ba6ce47-b0b7-3ba3-82c4-6a864594b7cd | -5.52094 | -37.48793 | 2026-06-11 04:10:00 | NPP-375D | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 021ea0a8-5d56-3cc5-9c3a-f4dca488b407 | -3.50813 | -48.04027 | 2026-06-11 04:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aec9b3bc-fb32-3953-9352-6000e5103fc6 | -5.52145 | -37.62277 | 2026-06-11 04:10:00 | NPP-375D | FELIPE GUERRA | RIO GRANDE DO NORTE | Brasil | 2403707 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 08692693-00e5-38ce-929c-da61ddf71b02 | -5.49307 | -37.24564 | 2026-06-11 04:10:00 | NPP-375D | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b1c379ca-76b7-3c9e-9172-8d9d63f9d4fb | -5.73108 | -49.10297 | 2026-06-11 04:10:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf6843a6-81f4-356b-8dc0-70c2ecb2ec68 | -4.42168 | -41.63631 | 2026-06-11 04:10:00 | NPP-375D | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 465a4fbe-f26d-32d8-9685-c813160f07d8 | -6.95573 | -44.55217 | 2026-06-11 04:10:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 90a1f255-6dc3-3729-a1f8-0ec5ac235f90 | -6.99721 | -43.86009 | 2026-06-11 04:10:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| af80bea2-744e-3f01-b422-e4a5a6620c4f | -5.03992 | -43.26197 | 2026-06-11 04:10:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| ea3e61da-ec0d-31d3-83cb-c717b1840a7b | -6.43527 | -44.57236 | 2026-06-11 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f7f3826a-dca8-313f-8d97-0d8ba7ae084d | -6.44858 | -44.56438 | 2026-06-11 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 783dd17b-79d3-31c0-8ed7-0933a41603bf | -5.93495 | -43.48668 | 2026-06-11 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| fe2705e5-0004-3dfa-83a6-500b0fde0e62 | -6.44079 | -44.56318 | 2026-06-11 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 48e28db2-b7db-31b0-b486-5ae8ba90becf | -6.44697 | -44.57414 | 2026-06-11 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2e8f6295-257a-31b1-b161-d03b2f7fe3c0 | -6.95652 | -44.54747 | 2026-06-11 04:10:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 151157f4-0505-3e3f-8994-6110c9b31493 | -6.44617 | -44.57901 | 2026-06-11 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 27a929e0-6948-340a-8503-4040fc7cb788 | -6.44468 | -44.56377 | 2026-06-11 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| a64e9f18-3efc-3f70-a482-79ac3e9ac2a4 | -12.06113 | -45.29349 | 2026-06-11 04:12:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c251d5a5-d013-34ad-ae4a-ed64b535cd2c | -12.85982 | -44.37189 | 2026-06-11 04:12:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 58b50edc-633e-3744-b8c2-b5630d619ea7 | -9.11028 | -47.96433 | 2026-06-11 04:12:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 25887697-0e0f-30bc-8ea5-dc8a8eac904d | -12.86268 | -44.37659 | 2026-06-11 04:12:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d3e71bab-5057-35e6-a40b-6db33aaaa8d9 | -9.33046 | -45.48462 | 2026-06-11 04:12:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 920de1e3-37c0-3c90-8dda-4fdda0c898fb | -11.57736 | -47.45116 | 2026-06-11 04:12:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 77b6373b-c87a-363d-b9c4-38f204004ff6 | -8.99035 | -48.08928 | 2026-06-11 04:12:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a2f43fdf-1fd7-39ac-8ab0-5a50f61d3f5f | -9.31557 | -45.47675 | 2026-06-11 04:12:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 8981f9d5-d962-3c97-b20a-07ffe44a3938 | -12.86336 | -44.37252 | 2026-06-11 04:12:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ce270f3d-ae8f-33b6-b223-cf7a30cf8f1a | -8.98526 | -48.09501 | 2026-06-11 04:12:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e53a3e2b-b97b-357b-bd46-7e989e23c035 | -8.66831 | -46.60231 | 2026-06-11 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3f98ddf9-20b1-30eb-a94d-b59b1c87c57b | -10.93437 | -44.66655 | 2026-06-11 04:12:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3c157899-d46a-3e1e-bb59-4a0b17548202 | -12.14548 | -48.45165 | 2026-06-11 04:12:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7b099441-7b2a-3995-882c-f6a69b0b4637 | -13.36488 | -43.20099 | 2026-06-11 04:12:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 459af3f1-88c4-3f45-a467-326d992eb2e5 | -12.64402 | -43.43756 | 2026-06-11 04:12:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 44b482ad-f9b4-3bd8-bbfb-6de4f5ce0737 | -9.31163 | -45.47604 | 2026-06-11 04:12:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 19.5 |
| db890df1-1008-3ab9-aa2f-70b3b4e4ac74 | -9.32344 | -45.47817 | 2026-06-11 04:12:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 533b4c34-2bc4-3107-b957-d97f405b3529 | -11.58241 | -47.44783 | 2026-06-11 04:12:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4f622fd7-77c0-3dd4-82fd-ba12d7d69c87 | -9.21629 | -48.58398 | 2026-06-11 04:12:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 26897b26-1bc2-395b-9b8d-6adeb1680e1c | -13.26594 | -45.57843 | 2026-06-11 04:12:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 20744ff7-7494-35d9-ace9-c2f506a71523 | -10.38251 | -46.62045 | 2026-06-11 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f3d9fb5f-ff78-3e2d-bf39-98672d74b763 | -12.30639 | -47.90934 | 2026-06-11 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 372c78f5-1579-34d2-8826-edf814ee1eb9 | -11.87226 | -47.10423 | 2026-06-11 04:12:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e2c3a5a0-25e0-3ae5-b37d-d843ed8a10d4 | -12.65181 | -40.97826 | 2026-06-11 04:12:00 | NPP-375D | IBIQUERA | BAHIA | Brasil | 2912608 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 21ff1820-a9bb-35b8-b900-377fcc3838ad | -7.72018 | -44.16256 | 2026-06-11 04:12:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b152edee-f0aa-3ccb-a912-b3885a2ce9be | -9.3077 | -45.47532 | 2026-06-11 04:12:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 29f2f7f7-056f-3c7a-bb25-2ff76aa376f4 | -13.36827 | -43.20157 | 2026-06-11 04:12:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9a0f5e5c-2320-3dfa-87b5-e3db6fdbf1f2 | -12.14375 | -48.46114 | 2026-06-11 04:12:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 82bf759f-7597-3ade-b1b6-70e321ef8f2c | -12.77806 | -46.82791 | 2026-06-11 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 28c870d6-51c0-3c6a-98ef-914e9ece3988 | -10.38117 | -46.62805 | 2026-06-11 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c3903229-7515-34e2-b1a7-b68f43d0c3e1 | -12.30558 | -47.91373 | 2026-06-11 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8cd30f6b-b942-36b1-b9aa-217e819bb7f4 | -8.98477 | -48.09341 | 2026-06-11 04:12:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 237b44fa-abc3-3b58-9be2-b58461d3c5de | -12.02832 | -47.80334 | 2026-06-11 04:12:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 596862c4-b0f2-3b71-8010-e0862059b721 | -8.31741 | -43.81869 | 2026-06-11 04:12:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 6379690d-eeb6-3606-b5d6-bfaa98c521e3 | -11.98237 | -47.3828 | 2026-06-11 04:12:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4b7071fb-36e2-3fda-95d2-7c6d33df2e8f | -12.8605 | -44.36783 | 2026-06-11 04:12:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4ebabf9b-3bed-3c7e-b201-6c53f4e1d3bb | -12.3072 | -47.90491 | 2026-06-11 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eea6db93-a10d-390c-af77-a652bef58b2b | -7.24773 | -49.5408 | 2026-06-11 04:12:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8b4274e-89d2-3426-bb92-cba54b2d3d06 | -7.34419 | -49.84946 | 2026-06-11 04:12:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e96b0c30-2a32-3dc1-9800-3909fad956e9 | -7.59854 | -46.46395 | 2026-06-11 04:12:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7c0d9f8b-3d83-3131-b122-72d5968eb231 | -11.79851 | -48.79469 | 2026-06-11 04:12:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 75a109f7-ad45-3fa3-9641-3ae5d18ed21d | -9.33132 | -45.47956 | 2026-06-11 04:12:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README5.md)
