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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3ed278e4-22ed-3ff6-a359-3a8de2cc9bce | -8.85458 | -47.67551 | 2024-11-09 04:57:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5afc88fb-ecc0-3d38-a7a5-dc878a072fd5 | -11.09781 | -43.33718 | 2024-11-09 04:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.5 |
| c4e901ee-3b42-3dcd-b42d-9ae4deb67319 | -11.86958 | -58.81861 | 2024-11-09 04:57:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2646e573-4fb4-3cec-8e71-5bd2e81cb6ab | -11.63834 | -42.01699 | 2024-11-09 04:57:00 | NPP-375D | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 1b3eb912-630a-380e-9c96-a7a83aad21fa | -11.09721 | -43.34239 | 2024-11-09 04:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.2 |
| bc4c1a66-8df9-319d-ac1e-676cc987fa35 | -11.08394 | -43.34579 | 2024-11-09 04:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 2d707ecd-aab8-3a79-907b-aafb0e7d92f6 | -8.84997 | -47.67482 | 2024-11-09 04:57:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4f7dd3bb-0a97-3367-a6d0-4e7b70ae8b94 | -8.14352 | -49.65496 | 2024-11-09 04:57:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 53f0c441-ed1f-3a51-86c1-bf97ef830851 | -6.75339 | -59.06517 | 2024-11-09 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7674d17c-c5f5-3f12-aac2-8cb392a903c0 | -11.09027 | -43.34671 | 2024-11-09 04:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 67ac6f19-5e92-3e07-badd-bb28a0005b71 | -17.24001 | -57.49678 | 2024-11-09 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| ca31e353-8a53-33fd-b5ef-38ca724e8f20 | -17.28232 | -57.51175 | 2024-11-09 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 165b28d2-43aa-35d1-a952-b8d0633750a8 | -17.24395 | -57.4937 | 2024-11-09 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| fb9c3d2c-f24d-3100-aa98-1bf24502858e | -17.28863 | -57.494 | 2024-11-09 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 61dbe0f9-1358-34d4-934b-5a498f797fd6 | -17.29079 | -57.50192 | 2024-11-09 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 33816a1e-2327-3ce7-82e1-8627214547ee | -17.29532 | -57.49517 | 2024-11-09 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 92deffe1-a2ea-3af5-9d4b-42f5b9f91868 | -15.46245 | -59.27425 | 2024-11-09 04:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6b77725d-713f-30b4-9a22-23da444c4d7c | -17.6309 | -57.45154 | 2024-11-09 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| e855d151-5a02-3a70-8e67-acbed518d6c5 | -17.28803 | -57.49767 | 2024-11-09 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 53f99320-4878-385b-86b4-1b8e40d1c8db | -20.28184 | -52.96595 | 2024-11-09 04:59:00 | NPP-375D | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 44e38452-7fbc-3580-b008-55d10d555499 | -17.24513 | -57.48637 | 2024-11-09 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 2c033dd8-ec51-3593-9645-89844bd76f9b | -19.82848 | -55.30534 | 2024-11-09 04:59:00 | NPP-375D | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 74944afe-31a5-34ae-aea3-f34c6a1a4389 | -14.87791 | -60.06438 | 2024-11-09 04:59:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56be6769-dcc5-30c7-9e39-5f50e0c363fc | -17.29473 | -57.49884 | 2024-11-09 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 662ca1c2-745c-30a3-a664-ea618459eb1e | -17.29138 | -57.49825 | 2024-11-09 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| f0543d72-0c00-3cb6-b894-3e7ef0fdd061 | -17.24454 | -57.49003 | 2024-11-09 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| f1742911-ab6c-31bc-8182-718819a763be | -17.40466 | -54.71521 | 2024-11-09 04:59:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8f07a00a-7aea-35e1-8b2e-92b90a6c04bd | -19.02417 | -57.6204 | 2024-11-09 04:59:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 539735ac-becb-3d80-98a8-9494253f6618 | -17.40629 | -54.71261 | 2024-11-09 04:59:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a23d5497-4d38-39c1-abfe-a63d871b0b24 | -17.30048 | -57.49623 | 2024-11-09 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| d6dedce6-5418-343e-b84e-c791a7151efe | -17.40571 | -54.71648 | 2024-11-09 04:59:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 04c33cb0-fb6d-3dff-822e-5cee6574a9a6 | -17.29866 | -57.49576 | 2024-11-09 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 3e730878-0af1-3de3-a7cf-fdfeb0c8b672 | -16.27063 | -59.14964 | 2024-11-09 04:59:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 8ddff7f1-15fb-36fe-b5fd-14a086020b11 | -17.29807 | -57.49943 | 2024-11-09 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 89acf536-a616-35d2-bed9-01e4c225e270 | -17.2406 | -57.49311 | 2024-11-09 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| e9ce73b6-2e51-3613-9f07-541cded1dc5d | -17.29197 | -57.49459 | 2024-11-09 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 95e521e4-c289-3711-a52d-4554b7619998 | -17.60752 | -57.44744 | 2024-11-09 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| f26985c5-53b3-3863-940a-9c917ab3dc13 | -14.58462 | -57.10545 | 2024-11-09 04:59:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5279576e-c11b-33cd-b85e-19dbd609bd4b | -11.0881 | -43.3219 | 2024-11-09 05:00:00 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 103.7 |
| a9b8a667-13ae-37a7-a015-2e2d4db9e44b | -3.6003 | -47.3614 | 2024-11-09 05:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 1ba604fe-415b-3665-bde2-b1fb20d783e6 | -3.9668 | -48.1932 | 2024-11-09 05:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 106.2 |
| 9ea63de1-208b-31c7-a51a-18ce1512c078 | -3.9853 | -48.1924 | 2024-11-09 05:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 1d048e2d-a6b2-3ab8-aaf4-c6a441648b4e | -3.5819 | -47.3403 | 2024-11-09 05:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| f7f66005-669c-3fc7-b91e-8dbb8f39e987 | -3.1511 | -52.9731 | 2024-11-09 05:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| e435350d-6d64-36e2-92aa-00e663585848 | -1.5163 | -52.1901 | 2024-11-09 05:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 94cc44be-ee51-36de-bb87-7f4f69242025 | -3.9854 | -48.1708 | 2024-11-09 05:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| c7b49e3f-346a-3a0d-8ec5-4ba4869884b9 | -11.1068 | -43.3428 | 2024-11-09 05:00:00 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 84.6 |
| a187b1e1-27fe-343c-bbdf-20f7ced5d148 | -2.6764 | -51.8189 | 2024-11-09 05:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 0500e789-a9c1-31bf-bedb-459c799beaa8 | -3.9669 | -48.1716 | 2024-11-09 05:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 136.3 |
| a525ecb5-5710-380c-9cd6-b198c0306745 | -3.6004 | -47.3395 | 2024-11-09 05:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 110.1 |
| 346db8c1-ef07-32f4-aa37-db43f2d64c37 | -4.2486 | -47.5729 | 2024-11-09 05:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 137.3 |
| 530fc8f2-6c91-3723-af60-51413b9a0607 | -4.2484 | -47.5947 | 2024-11-09 05:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 3a5d1083-5a7e-3f0a-93b6-122a1212107d | -11.0877 | -43.3456 | 2024-11-09 05:00:00 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 147.7 |
| d9bf83d5-4f95-3654-9d9d-ec1e8a0ddf23 | -23.89556 | -54.06314 | 2024-11-09 05:01:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f34a288e-a8f9-37db-8a1f-a3c1e3ef65f6 | -23.88864 | -54.05702 | 2024-11-09 05:01:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 8b21c578-35a0-3d6f-a64f-a6b3296aeac3 | -22.1375 | -56.57661 | 2024-11-09 05:01:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a02273f0-6eaa-37ee-bb6b-d8959f1527f6 | -20.60478 | -55.89942 | 2024-11-09 05:01:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d8d3ea65-07aa-3cb5-b90e-39968dde5b8c | -23.77149 | -55.41157 | 2024-11-09 05:01:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 10883740-1a67-313e-9488-84a816e16936 | -23.9069 | -54.06488 | 2024-11-09 05:01:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| d207e89c-86c1-3617-ba3a-6d50f639225c | -20.60138 | -55.89885 | 2024-11-09 05:01:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 16599c48-cfef-3356-97f0-411f58c4b53c | -23.90754 | -54.05994 | 2024-11-09 05:01:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a59f2ee4-ccfa-36bf-b153-f1d8708aeadc | -21.60208 | -57.53951 | 2024-11-09 05:01:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 42fa5fc5-9893-3826-8e83-478f5e3932aa | -23.88486 | -54.05644 | 2024-11-09 05:01:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| e8bab426-9022-329e-b917-7c6cedfaf9c2 | -21.13656 | -55.80914 | 2024-11-09 05:01:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 420dbb51-747e-352c-bae2-e88893a697c6 | -23.91132 | -54.06052 | 2024-11-09 05:01:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 9520d15b-71fe-3038-97c3-9b3ae0dbfe05 | -22.13693 | -56.58044 | 2024-11-09 05:01:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8c8781f5-cd52-36a0-8c36-edd047f42dd6 | -23.91068 | -54.06547 | 2024-11-09 05:01:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| c8d2c556-0446-3f67-b8a8-2c5317c9dce5 | -3.9668 | -48.1932 | 2024-11-09 05:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 102.5 |
| 821054fd-a45a-3e2a-bee1-47d5b33e21e0 | -4.2486 | -47.5729 | 2024-11-09 05:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 123.8 |
| 219dce71-3f45-3aa7-81b7-4ece866ea258 | -3.6003 | -47.3614 | 2024-11-09 05:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| bfccf4b8-c902-398c-9eb2-b962b81f4875 | -3.9854 | -48.1708 | 2024-11-09 05:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 17c88b6f-a28e-38d0-874f-2695b214c4d5 | -3.6004 | -47.3395 | 2024-11-09 05:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 122.6 |
| cd1c8798-b381-3467-a87d-5105302f6fed | -3.1511 | -52.9731 | 2024-11-09 05:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 7e0a45b8-22a9-38a5-b252-8d5ca278ce6b | -3.9669 | -48.1716 | 2024-11-09 05:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 140.0 |
| 8b067260-c471-33c5-924e-a4ea03fdde60 | -3.9853 | -48.1924 | 2024-11-09 05:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| c4cadbe7-6bae-32af-b06e-3e5427f3a265 | -2.2295 | -53.7832 | 2024-11-09 05:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 61b1bf47-848c-37a9-9e82-1a057918b948 | -1.5163 | -52.1901 | 2024-11-09 05:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| e78f2233-3c55-3831-a28c-95badfa9a2b0 | -4.2058 | -48.5491 | 2024-11-09 05:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| aedbabea-8eeb-3f25-9dad-7648b33dfea7 | -1.5347 | -52.1899 | 2024-11-09 05:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 9cc50f72-a43e-3c11-b961-f58c2ced4879 | -3.5819 | -47.3403 | 2024-11-09 05:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| e702c250-e3cf-3949-a40b-37f1bf6be2e7 | 3.36665 | -51.27858 | 2024-11-09 05:18:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3f1363e9-e764-3ad6-a8eb-0dd8767bb484 | 4.4245 | -59.77684 | 2024-11-09 05:18:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 956c6790-0f2b-37f6-8ea9-88d2bcfe8a05 | 3.37208 | -51.28263 | 2024-11-09 05:18:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 7.6 |
| ad9e52f2-d18b-3c36-bf89-67ba35af6c30 | 4.53687 | -60.95531 | 2024-11-09 05:18:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1b4f4ee7-ba09-3b89-9ebc-6c3968dffc05 | 3.52435 | -51.43519 | 2024-11-09 05:18:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8deefda6-16de-399f-8a77-af86900041b4 | 2.10731 | -50.85739 | 2024-11-09 05:18:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 59de4ae9-ad40-3cca-9d89-1ad2f2d78362 | 3.36122 | -51.27453 | 2024-11-09 05:18:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f897fc83-e3aa-35b3-88d6-d38ac4b46cd5 | 2.46862 | -50.96247 | 2024-11-09 05:18:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84f8a91d-6b03-3e15-91a0-2d138b12d180 | 4.54039 | -60.95462 | 2024-11-09 05:18:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5b13caf8-d061-310f-b6b0-464469e29870 | 2.56098 | -51.10474 | 2024-11-09 05:18:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d11de1b6-3c76-33f4-83b7-1efc26db2da7 | 4.36128 | -59.82357 | 2024-11-09 05:18:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da71077e-c954-3b1b-a3b7-9b01f5154610 | 3.9079 | -59.79296 | 2024-11-09 05:18:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70a5b38d-931b-3058-ad3f-840f29980c35 | 3.37128 | -51.27783 | 2024-11-09 05:18:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 7.6 |
| a140ee7d-17d7-34b2-a1fc-0266f5712402 | 2.56044 | -51.10654 | 2024-11-09 05:18:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d758662-de85-33b0-bfac-c9258f2917d7 | -11.0881 | -43.3219 | 2024-11-09 05:20:00 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 94.2 |
| cca8d0fe-3179-3485-b02f-efcb68bf903f | -3.6003 | -47.3614 | 2024-11-09 05:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| f104c53c-95f4-3d63-82b0-ce12ae080359 | -3.0865 | -50.5625 | 2024-11-09 05:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 6e8fd85a-0d4e-3be9-9514-5161ceb83108 | -3.9668 | -48.1932 | 2024-11-09 05:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 122.0 |
| ef6a192a-b899-34b9-9439-5408a90a124d | -11.0877 | -43.3456 | 2024-11-09 05:20:00 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 161.2 |
| ab908b0d-1132-3d9d-a4d2-b3664adb6da1 | -3.9669 | -48.1716 | 2024-11-09 05:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 154.8 |


[Clique aqui para ver as próximas entradas](README101.md)
