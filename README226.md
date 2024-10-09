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

## Dados Diários - Página 226

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 40761b0c-e330-35dd-8461-ec458e621095 | -15.7076 | -59.3726 | 2024-10-09 07:06:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 6abc8bd3-c442-3002-a1c8-92902beb8303 | -16.8898 | -55.8039 | 2024-10-09 07:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 80.1 |
| 55177610-1d24-3b0b-918e-ec38ddad8978 | -16.8901 | -55.7831 | 2024-10-09 07:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 70.1 |
| fe1ad984-8c9a-35ca-b94a-d58cbdf7d11b | -16.9091 | -55.8222 | 2024-10-09 07:06:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 94.7 |
| 4bd25a5b-78af-318c-8247-71de6e52a0ab | -16.9094 | -55.8014 | 2024-10-09 07:06:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 162.6 |
| 90a351df-6323-3560-9e15-7fcb401c58a4 | -16.9098 | -55.7806 | 2024-10-09 07:06:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 121.7 |
| 7b1a996b-19c9-3e9c-bdc7-0bd3479e9b6a | -16.929 | -55.7989 | 2024-10-09 07:06:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 72.4 |
| db09720b-296c-3400-abde-9c1c5ed5218a | -17.0623 | -56.0308 | 2024-10-09 07:06:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 147.5 |
| 79567065-0b85-375a-864b-ec99f5f661e7 | -17.0626 | -56.01 | 2024-10-09 07:06:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 91.9 |
| 23392c57-a6b8-3d36-9469-fbd06688ed1e | -17.0795 | -57.3674 | 2024-10-09 07:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 117.8 |
| 7918bbd5-78de-329c-8acf-9a15fde661ab | -17.0799 | -57.3469 | 2024-10-09 07:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.3 |
| c1e1cb01-428c-35f7-8cd9-a711b94c1a07 | -17.1467 | -56.8463 | 2024-10-09 07:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.3 |
| a4cea54c-11a6-343a-9787-b74ea090d308 | -17.1588 | -56.1222 | 2024-10-09 07:06:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 53.7 |
| bc0e0374-9223-351d-be13-27c9651f106a | -18.1193 | -56.3921 | 2024-10-09 07:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.8 |
| 0dd9cdd3-d431-32c1-afe9-8d49e2280f09 | -18.1391 | -56.3895 | 2024-10-09 07:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.6 |
| f2424f4d-6f91-3f2b-83bc-65682cc445d0 | -18.5993 | -57.2629 | 2024-10-09 07:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.8 |
| a48c8615-93e1-34ff-9aca-463e0719da96 | -21.0408 | -47.5696 | 2024-10-09 07:07:02 | GOES-16 | BRODOWSKI | SÃO PAULO | Brasil | 3507803 | 35 | 33 | nan | nan | nan | Cerrado | 92.0 |
| b1917dbf-a5c7-3fb1-8d5b-433591b8f219 | -21.6729 | -47.7441 | 2024-10-09 07:07:06 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 51a05dae-edf8-3254-b2f4-6c80a7a38548 | -21.6737 | -47.7204 | 2024-10-09 07:07:06 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 151.1 |
| 9bfac636-0436-313c-bbba-f4d3377edf3f | -10.8754 | -63.9169 | 2024-10-09 07:16:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 25d497d7-e118-3a8e-8723-56f1df016d67 | -11.5233 | -65.137 | 2024-10-09 07:16:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 5d8ed359-488e-34e1-bab3-5697a7ee1a08 | -11.6806 | -64.0312 | 2024-10-09 07:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 26cde4cd-57ba-321b-9954-4e5938c816b9 | -12.878 | -62.8007 | 2024-10-09 07:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 87121cca-f306-3488-81f5-325eafcff433 | -13.417 | -61.9169 | 2024-10-09 07:16:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 4c04b447-fd91-3eb4-87d0-44dc99c83346 | -13.398 | -61.9182 | 2024-10-09 07:16:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 31.8 |
| 3f5d81e7-c988-3fae-b5db-ffd8bb8c4d26 | -13.3978 | -61.9376 | 2024-10-09 07:16:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 25.0 |
| c36de037-b838-3a88-b8e0-9885ef15f269 | -15.6882 | -59.3745 | 2024-10-09 07:16:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| c8f2f9cd-67ca-3a99-a580-924cf44864de | -15.688 | -59.3945 | 2024-10-09 07:16:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 9451f7f3-ea97-39c4-be90-c69cba925642 | -15.6686 | -59.3963 | 2024-10-09 07:16:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 8e232152-e5b2-33b0-84b2-bda53b24593c | -15.6683 | -59.4163 | 2024-10-09 07:16:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 74.5 |
| f695bba5-4cf7-3a2e-aa2f-65a7cc44c40c | -15.7076 | -59.3726 | 2024-10-09 07:16:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 79.5 |
| f3f55c79-25bf-3fcc-bb04-3956aaacff34 | -17.0623 | -56.0308 | 2024-10-09 07:16:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 134.7 |
| bbea9bf5-2abb-3371-8770-1b7b11138789 | -17.0626 | -56.01 | 2024-10-09 07:16:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 85.3 |
| f8d5d33c-cc44-315d-9cd4-699e8fbacf46 | -17.0795 | -57.3674 | 2024-10-09 07:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.6 |
| 01f9af44-492e-3444-b7e1-92d1117fe37f | -17.0799 | -57.3469 | 2024-10-09 07:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.9 |
| ffe5e8d3-09e0-3dd6-8125-1c606d0b0afb | -17.1467 | -56.8463 | 2024-10-09 07:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.3 |
| a292a019-b2e3-3945-847c-24496dd6bb1b | -17.1471 | -56.8256 | 2024-10-09 07:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.9 |
| fe2d7fde-4af6-39cc-87d6-08a2e4f65baf | -17.1588 | -56.1222 | 2024-10-09 07:16:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 56.2 |
| 877c8b24-3002-3b92-b09f-3eb2cd7f8b5f | -18.1391 | -56.3895 | 2024-10-09 07:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.4 |
| 48bc669f-a512-3cc0-bee8-e12fe60c082e | -18.1193 | -56.3921 | 2024-10-09 07:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 108.0 |
| 23d58ac5-2845-3ebe-a572-6a40331c9a89 | -18.5996 | -57.2422 | 2024-10-09 07:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.0 |
| 98492632-b2c3-3982-b182-aa5a193b3de2 | -18.5993 | -57.2629 | 2024-10-09 07:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.2 |
| 7d427756-3447-38ad-b32a-6af31e7f9ccf | -20.3756 | -47.9826 | 2024-10-09 07:16:59 | GOES-16 | IPUÃ | SÃO PAULO | Brasil | 3521309 | 35 | 33 | nan | nan | nan | Cerrado | 95.4 |
| d0ca816d-77c3-3463-bb6d-ed52e9626f1c | -20.7839 | -47.2559 | 2024-10-09 07:17:01 | GOES-16 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 97.7 |
| e56eab26-c7ea-326f-bf34-e1adb8cedf33 | -21.6737 | -47.7204 | 2024-10-09 07:17:06 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 0abf39a3-2348-315c-b4a4-9e7225b8c432 | -10.4287 | -60.9979 | 2024-10-09 07:26:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 193966a4-2783-3d1a-9ad1-60baf665165d | -10.8754 | -63.9169 | 2024-10-09 07:26:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 8a4abc21-3a6e-3464-ac71-f0081300e99a | -10.8755 | -63.8979 | 2024-10-09 07:26:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 21e1fa65-498a-3dee-839a-fa32420d257e | -11.5233 | -65.137 | 2024-10-09 07:26:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 041fd0e0-ec79-39ef-9bf9-88eebbf6421a | -11.6806 | -64.0312 | 2024-10-09 07:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 9e99d5ea-1b50-3eec-bdc3-d785b6e59d23 | -13.398 | -61.9182 | 2024-10-09 07:26:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 2bc13143-d4d4-33ba-8566-cf1f88657097 | -13.417 | -61.9169 | 2024-10-09 07:26:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 50fe9698-264a-3573-9704-6facf07add85 | -13.3978 | -61.9376 | 2024-10-09 07:26:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 484515e7-0444-3b17-bfb8-37b1f5550281 | -17.0626 | -56.01 | 2024-10-09 07:26:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 81.7 |
| c69d29a2-61d1-3b65-9923-cb803cfca20d | -17.0623 | -56.0308 | 2024-10-09 07:26:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 171.0 |
| 7ad31d7b-e12d-3178-9462-64f8c5570573 | -17.0426 | -56.0333 | 2024-10-09 07:26:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 76.3 |
| 240d43ea-ca31-3c1e-9bbb-238954ade30a | -17.0799 | -57.3469 | 2024-10-09 07:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.5 |
| 4fff81cd-2e31-30a6-87f4-331b343713c0 | -17.0795 | -57.3674 | 2024-10-09 07:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.3 |
| dc193962-c81d-3972-a382-3f870b128f30 | -17.1188 | -57.3628 | 2024-10-09 07:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.1 |
| 94ae2807-4faa-389a-a960-172298d0ce25 | -17.1467 | -56.8463 | 2024-10-09 07:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.4 |
| 007a240a-2914-39cc-88ca-45d2cecabe56 | -18.1193 | -56.3921 | 2024-10-09 07:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.6 |
| f4168074-3839-39a5-9b40-31cb0a6a64f0 | -18.8682 | -54.5831 | 2024-10-09 07:26:52 | GOES-16 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 76262cd5-b187-38ef-9fbc-ef190719a46b | -20.3756 | -47.9826 | 2024-10-09 07:26:59 | GOES-16 | IPUÃ | SÃO PAULO | Brasil | 3521309 | 35 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 270b3700-3b1f-3844-9757-fe276d0eed0c | -10.8754 | -63.9169 | 2024-10-09 07:36:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 51.5 |
| e1519f31-65e6-3c20-b2a8-60f3951266c9 | -10.8755 | -63.8979 | 2024-10-09 07:36:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 51fb24a5-6cd0-3b05-a473-d183a482e441 | -11.6806 | -64.0312 | 2024-10-09 07:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 47.1 |
| e3541080-a3e4-3d27-8084-74b54d818935 | -13.3786 | -61.9582 | 2024-10-09 07:36:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 37.1 |
| bab09086-9e27-3321-8d98-4cca41ceb7a2 | -13.398 | -61.9182 | 2024-10-09 07:36:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 17b01bf1-2cc2-330c-886a-7f95d5a197ee | -15.7076 | -59.3726 | 2024-10-09 07:36:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 6bb96107-7625-3592-a48d-22c12cbc2df3 | -15.6686 | -59.3963 | 2024-10-09 07:36:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 64.7 |
| aaa572f3-c219-3a40-b16f-3efd91635f30 | -15.688 | -59.3945 | 2024-10-09 07:36:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 83.3 |
| ab17f5ad-b3fe-3d33-b650-1d7b225f29a3 | -15.6882 | -59.3745 | 2024-10-09 07:36:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 5ac80dae-f2e3-3f48-988a-6eaf0d004a33 | -17.0626 | -56.01 | 2024-10-09 07:36:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 76.3 |
| 2483122c-05af-326f-8f39-510c953ad55e | -17.0426 | -56.0333 | 2024-10-09 07:36:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 70.7 |
| a9da391d-5645-3d94-9716-91c56a7521a7 | -17.0623 | -56.0308 | 2024-10-09 07:36:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 138.5 |
| f2ffb6ab-798d-3d1c-8946-e21cd5bc4fc2 | -17.1467 | -56.8463 | 2024-10-09 07:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.1 |
| 1084d3a5-c926-3892-9b2f-aa5a6c9d5c76 | -17.0795 | -57.3674 | 2024-10-09 07:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.0 |
| 5dc46f5b-e7a6-3a4b-9e78-e33a05177a19 | -18.1193 | -56.3921 | 2024-10-09 07:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.9 |
| ccf9d769-480c-315f-8209-afd9a73d161d | -19.0219 | -44.9992 | 2024-10-09 07:36:51 | GOES-16 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 65.0 |
| bd63b466-99ea-329a-a662-9e342f509835 | -22.1578 | -48.1172 | 2024-10-09 07:37:08 | GOES-16 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 69.9 |
| aab5daa8-c139-3135-881b-20be51ba938b | -22.1369 | -48.1224 | 2024-10-09 07:37:08 | GOES-16 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 1eb2e52c-a91f-32e0-b5c8-abdf890dde32 | -22.8137 | -48.4225 | 2024-10-09 07:37:11 | GOES-16 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 232b1cc1-d24a-3a4a-acf4-7206d484a6b8 | -10.8754 | -63.9169 | 2024-10-09 07:46:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 55830521-f79e-374a-a3fd-1a3229ece2bc | -10.8755 | -63.8979 | 2024-10-09 07:46:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 37.3 |
| d09b0eb6-011c-3fd7-8891-7f15c94d60bb | -11.6806 | -64.0312 | 2024-10-09 07:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 50.9 |
| c6541117-0e62-31da-b862-ce42ca63ae1a | -13.3786 | -61.9582 | 2024-10-09 07:46:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 41.6 |
| d8677afc-aad0-32d6-bae0-d07e235f8837 | -13.3978 | -61.9376 | 2024-10-09 07:46:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 34.3 |
| 4ac854ef-5772-3133-a8e2-cc4e5ad7971d | -13.398 | -61.9182 | 2024-10-09 07:46:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 26bad099-18dd-37d6-9a97-a696e697f086 | -15.6795 | -52.4993 | 2024-10-09 07:46:35 | GOES-16 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 44f095f8-53bb-388f-9fd1-291360803395 | -15.6683 | -59.4163 | 2024-10-09 07:46:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 69bdd3d6-608f-3b87-b41c-79011a67b855 | -15.6686 | -59.3963 | 2024-10-09 07:46:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| f2640103-1c03-36d3-aed1-3fa546e7b412 | -15.688 | -59.3945 | 2024-10-09 07:46:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 03ee1d60-1508-396b-af06-d68feef1e141 | -15.6882 | -59.3745 | 2024-10-09 07:46:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 67.5 |
| f7c88c35-ee6f-33af-900c-fcc968ca985a | -15.7073 | -59.3926 | 2024-10-09 07:46:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 1aea7fc5-7aca-32fa-9241-1e59083a4cbf | -15.7076 | -59.3726 | 2024-10-09 07:46:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 7fe75e86-9cab-3440-9b13-213768532f48 | -16.8898 | -55.8039 | 2024-10-09 07:46:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 67.5 |
| 482c3640-7396-34c6-84cc-c01d81cb4e81 | -17.0426 | -56.0333 | 2024-10-09 07:46:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 69.2 |
| bdf71eee-3230-3f50-8dd5-cefa018f62f4 | -16.9098 | -55.7806 | 2024-10-09 07:46:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 69.3 |
| 6ec5abb7-ae4d-3057-a4f4-73b33c8cc2f1 | -16.9287 | -55.8197 | 2024-10-09 07:46:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 95.1 |
| 194589d0-ebe2-3038-9df2-f4e0e590fb33 | -16.929 | -55.7989 | 2024-10-09 07:46:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 72.6 |


[Clique aqui para ver as próximas entradas](README227.md)
