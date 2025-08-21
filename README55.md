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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fd91342d-5267-3ab8-b224-9490a021ce61 | -11.32165 | -55.21883 | 2025-08-21 05:31:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e87faddb-29b7-307e-83b7-734fddb3311a | -9.90219 | -60.28778 | 2025-08-21 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ff045cd8-9537-3b26-b5ee-4ba33ecd8d9b | -14.63068 | -54.87026 | 2025-08-21 05:31:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cae87fa3-48e2-3022-9bf2-0e313688a201 | -12.22332 | -53.60628 | 2025-08-21 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b0507445-51ea-3e77-acbd-a0afa99d2612 | -15.56675 | -50.32236 | 2025-08-21 05:31:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8887a903-b4cc-31d3-8dcc-c44790adf621 | -13.14121 | -54.91517 | 2025-08-21 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 21403412-c60b-3563-8a13-37830e1cc0fc | -12.98476 | -56.87819 | 2025-08-21 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 421d9825-e65f-3b78-88e2-27d70f067c2f | -14.53513 | -56.23725 | 2025-08-21 05:31:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7126ee07-c4ff-3069-805e-ae04bbc656ec | -7.0164 | -44.6413 | 2025-08-21 05:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 243.2 |
| 3f1b4c38-f1c8-30de-ba1c-5e89bacf2a68 | -8.8552 | -62.3933 | 2025-08-21 05:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 98.4 |
| f80e4e45-3e0f-354d-8945-fd51b869f2d4 | -8.8736 | -62.4115 | 2025-08-21 05:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 173.4 |
| f0975172-2835-3c90-aa15-c5b80c4da2b5 | -8.8551 | -62.4123 | 2025-08-21 05:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 75.6 |
| b54a3180-121e-3ce3-9da1-12cfffdc1461 | -7.0166 | -44.6184 | 2025-08-21 05:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 236.4 |
| d280b478-59a4-3c22-a018-38e2d0a19b9d | -7.0352 | -44.6396 | 2025-08-21 05:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 214.2 |
| b7b06aca-6000-3bb3-8c24-080cafcf6251 | -8.8737 | -62.3925 | 2025-08-21 05:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 196.4 |
| d3ca2e90-d015-37f3-a1ab-abe9244e2c70 | -7.0354 | -44.6167 | 2025-08-21 05:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 209.1 |
| a99bf7b0-ddf8-3830-a1b3-9f26a8bfbaf8 | -8.8736 | -62.4115 | 2025-08-21 05:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 175.0 |
| 9dd5c7bb-b70d-33af-b1c2-31814f3cfdf5 | -7.0352 | -44.6396 | 2025-08-21 05:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 170.9 |
| c78d921f-2791-381c-b47d-9a0fc6cba1a9 | -7.0164 | -44.6413 | 2025-08-21 05:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 195.7 |
| f41096ca-cabd-354a-973a-e61b7dbd6637 | -7.0166 | -44.6184 | 2025-08-21 05:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 185.2 |
| 8bc79f14-b9e9-3df3-879e-86adafdc641f | -8.8735 | -62.4305 | 2025-08-21 05:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 48.6 |
| c2cb2ceb-a462-33b1-8276-8d6e2381abf0 | -8.8551 | -62.4123 | 2025-08-21 05:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 71.9 |
| e434c925-6a9f-3160-b8da-99ac8eeaf3ab | -7.0354 | -44.6167 | 2025-08-21 05:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 164.9 |
| 918ac1a0-1e88-3a80-9812-8b9e73b1c74a | -8.8737 | -62.3925 | 2025-08-21 05:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 197.8 |
| 101399d5-d38e-3e82-b6a9-7304be786822 | -8.8552 | -62.3933 | 2025-08-21 05:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 88.9 |
| b343e874-e87b-321e-80d6-82ed3db74ea5 | -6.34641 | -55.55843 | 2025-08-21 05:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4256e809-24ee-3442-9ec2-100dcc8441f2 | -7.55601 | -63.84781 | 2025-08-21 05:55:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2637bb54-ac72-3c39-b1e8-be04d56989b8 | -7.05305 | -59.83323 | 2025-08-21 05:55:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b96ae245-69b4-373e-9a03-72aef2919b29 | -7.50824 | -63.82872 | 2025-08-21 05:55:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf536861-7b5d-3078-8137-6f77ea75aa5c | -4.96057 | -62.34542 | 2025-08-21 05:55:00 | NPP-375D | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 972fe3aa-7ae3-3be5-977b-be60621922d6 | -6.9337 | -62.88438 | 2025-08-21 05:55:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7bd57a9-608c-3831-9556-a36416377311 | -6.9379 | -62.88501 | 2025-08-21 05:55:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f9fdb67-d1fd-39d3-8302-555dca440158 | -7.51221 | -63.82931 | 2025-08-21 05:55:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a264f4f-99cd-3630-948e-81ff77ee484b | -6.93735 | -62.88884 | 2025-08-21 05:55:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9e0a726-f40b-3e97-9646-e910edc3c5e5 | -7.55925 | -63.85349 | 2025-08-21 05:55:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 915c28d9-c49c-3009-843b-172677a49bb9 | -7.5035 | -63.83326 | 2025-08-21 05:55:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5602022f-59eb-30aa-a016-bf91a66bd7f9 | -6.3481 | -55.55801 | 2025-08-21 05:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 75d675e2-3825-309a-951c-07f5f9c62ed4 | -6.34731 | -55.56403 | 2025-08-21 05:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f918060c-3283-3c55-9938-d8b19efff6f5 | -7.50748 | -63.83384 | 2025-08-21 05:55:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 33750e70-d170-3662-9d04-6a561243f9da | -7.05432 | -59.82401 | 2025-08-21 05:55:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4f230a7e-5ea6-3e51-bd9a-f9aece95d6f9 | -7.56396 | -63.84898 | 2025-08-21 05:55:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d594fca-2c1e-3317-9e38-aed874eb45f4 | -6.62472 | -69.87625 | 2025-08-21 05:55:00 | NPP-375D | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6d6cdf8f-172a-399b-aaef-1cdf28927c09 | -7.55204 | -63.84721 | 2025-08-21 05:55:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| da902767-5505-3272-868d-c171f2ff8b3b | -7.54733 | -63.85173 | 2025-08-21 05:55:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a1d0836f-2a3e-3f68-925a-d583d0c04df1 | -7.05348 | -59.83011 | 2025-08-21 05:55:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66fed3cc-f80e-3d6a-b6ef-f5a9e4e6a656 | -7.51145 | -63.83443 | 2025-08-21 05:55:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f226698c-bb00-32af-aba7-409f7982edd0 | -7.5513 | -63.85232 | 2025-08-21 05:55:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b7b2b05-8450-3ac3-b32d-868c306ffdcc | -7.47752 | -64.59904 | 2025-08-21 05:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ba2bb84-6b9e-38c6-96ca-5fe09eaa7b0a | 3.54384 | -60.72464 | 2025-08-21 05:55:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a9a5179e-28e1-3b89-983d-f85fb88d70d1 | -7.05868 | -59.83074 | 2025-08-21 05:55:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f97b882c-bdb6-37c3-9969-6b7b9e46b835 | -7.0539 | -59.82704 | 2025-08-21 05:55:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b05279ad-f4d5-3bea-9203-4091826f2c9d | -7.55527 | -63.85291 | 2025-08-21 05:55:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 925c02bb-3818-378b-9b28-c8d4f7a396a0 | -7.54807 | -63.84663 | 2025-08-21 05:55:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b89a1f3c-33dd-3518-bc8e-f8fbe33f3bef | -7.84355 | -72.88258 | 2025-08-21 05:57:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4bcc8540-b575-3647-a5c5-6914cf1b6939 | -8.88438 | -62.40134 | 2025-08-21 05:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4bcac626-e23d-3ffd-91e2-498b85d28262 | -7.96608 | -70.02718 | 2025-08-21 05:57:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 510fe005-9d8d-316d-96ef-13b61eb6d768 | -8.869 | -62.38119 | 2025-08-21 05:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9a76f51d-afc1-330f-9092-0ad4d9979cf1 | -10.98483 | -55.24041 | 2025-08-21 05:57:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6f467e16-3b3a-34aa-bb6d-3b463e555624 | -8.33165 | -70.27541 | 2025-08-21 05:57:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e7a81ae3-7563-3574-8c66-04945b5aaf6d | -8.86469 | -62.41195 | 2025-08-21 05:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 46ba3b64-2124-3531-b3aa-af796c1cb742 | -9.86765 | -58.67693 | 2025-08-21 05:57:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2176af9-61f9-3f80-aab7-229b6ccd2da2 | -11.80988 | -55.5275 | 2025-08-21 05:57:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 5b831d34-5ffc-3e5c-9eda-2409b1624485 | -9.90825 | -62.14666 | 2025-08-21 05:57:00 | NPP-375D | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6bd0898c-99d6-3d70-922b-5489eb743594 | -8.66425 | -63.85064 | 2025-08-21 05:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86e4d65b-866c-3f09-bbf2-3a9efc0c9eef | -8.86977 | -62.40818 | 2025-08-21 05:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 13a6b41f-ad9d-3c28-8947-20ddfe62fa8f | -9.34514 | -62.58651 | 2025-08-21 05:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2dc8974f-aca6-31a5-a040-51942ab7c555 | -7.77897 | -66.95919 | 2025-08-21 05:57:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d89d1b28-331a-358e-b4e0-f330920ef3e3 | -8.86962 | -62.37676 | 2025-08-21 05:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 66354ae7-4fcf-3946-9354-f798960660d9 | -7.77612 | -66.95499 | 2025-08-21 05:57:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d496e1af-9a12-36d3-bb16-0076261cfd02 | -12.5882 | -60.36049 | 2025-08-21 05:57:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0938a4fb-7d56-36d2-b3d0-6e274b63858a | -8.87039 | -62.40377 | 2025-08-21 05:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 11.8 |
| b3532df9-2795-3723-a972-a5500ab6c208 | -8.61575 | -62.12669 | 2025-08-21 05:57:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 29498814-1c0b-37ec-b9ea-c3dadfff7c74 | -8.87619 | -62.4271 | 2025-08-21 05:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b6399d6a-1484-3e98-9340-12fa772860f5 | -8.32826 | -70.27486 | 2025-08-21 05:57:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8935c454-cc1a-36da-8c30-353f8d893d66 | -8.55778 | -66.95474 | 2025-08-21 05:57:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b776c38c-51ad-32a7-a7f0-ba43e8c845e7 | -8.88127 | -62.42331 | 2025-08-21 05:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6de22f57-d368-3189-b766-4ce286a6effd | -8.88314 | -62.4101 | 2025-08-21 05:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 44f182f6-cac6-3491-9625-e1579cbe8a20 | -8.55836 | -66.95102 | 2025-08-21 05:57:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5b20dc55-5a96-3bc3-ab9c-8c1d817bf4cb | -9.90166 | -60.28754 | 2025-08-21 05:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6dd8c448-3923-39e9-b36b-3cd21d9840dc | -8.86268 | -62.39381 | 2025-08-21 05:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 39.8 |
| aba48aaa-d00a-3575-a236-499a30af1746 | -8.86915 | -62.41259 | 2025-08-21 05:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e3b15a35-2a78-361a-b45b-fcf8974c4f7a | -8.68069 | -62.09563 | 2025-08-21 05:57:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2a9c9ee2-51ab-3018-a4b2-11fb87b373b2 | -8.87868 | -62.40946 | 2025-08-21 05:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f7ac38a8-168e-3861-976a-90d8a2976108 | -9.04848 | -67.46227 | 2025-08-21 05:57:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52294de5-f225-3daa-af79-5fc0e9b8467a | -8.87682 | -62.42267 | 2025-08-21 05:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6d22f00d-b7e4-3258-8ab4-4f5187590cfe | -7.78294 | -66.95605 | 2025-08-21 05:57:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e2192dc4-0d69-3660-bc0c-9844464eae7d | -8.43846 | -63.86739 | 2025-08-21 05:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7f66563e-52f9-3b62-af1d-a32115ca528c | -9.90208 | -60.28429 | 2025-08-21 05:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3578607-4675-3afa-b988-0d0ba3aa4b13 | -8.22571 | -69.8445 | 2025-08-21 05:57:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b3d139c9-a6b4-314e-8c2f-4d76b25d5222 | -8.86853 | -62.41702 | 2025-08-21 05:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 7.1 |
| d97a00f4-1a64-3d39-9578-abc855158c86 | -9.05243 | -67.45915 | 2025-08-21 05:57:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 88fd85df-98e0-3149-ab05-636bd60fe89b | -8.85822 | -62.39314 | 2025-08-21 05:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ee40c649-f6c0-34d9-be6c-577d8f5c4cb5 | -9.52235 | -60.53832 | 2025-08-21 05:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f00c3dc-6ce2-3289-a68e-d3d0f97381cc | -8.75829 | -64.19651 | 2025-08-21 05:57:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30b8b0d1-8221-358f-bef9-fa874b090da5 | -8.88376 | -62.40572 | 2025-08-21 05:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ff63c75d-0f76-3ede-b01d-0d12e35e07a8 | -11.80832 | -55.5291 | 2025-08-21 05:57:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 33e7469b-e34c-377b-8709-5d3228561bdb | -8.55207 | -66.94624 | 2025-08-21 05:57:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60010189-883a-3e39-8df5-ee6f6f4112bc | -9.19453 | -65.66049 | 2025-08-21 05:57:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 97e0c1e6-5c47-38da-a99c-1ea6dceeae4d | -8.85761 | -62.39755 | 2025-08-21 05:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 05ae5fcd-ee41-3d4a-b1ce-0f217fa7298c | -8.54921 | -66.94198 | 2025-08-21 05:57:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README56.md)
