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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7211b18a-615f-3517-90dd-8336ab004ddd | -8.61373 | -62.59514 | 2025-08-24 06:14:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 06825aff-d1a8-315f-8996-02f6951a8cfd | -9.03011 | -65.71429 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d79133c1-56ab-3764-8d22-a463dfa94171 | -7.57604 | -63.44207 | 2025-08-24 06:14:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3851451b-6ccc-365c-af4c-213223bc00fa | -9.00844 | -65.7232 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1cdf2274-57f7-3f1c-8e96-4fdccb6e55ba | -9.02409 | -65.71967 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 325cad3b-4f7e-3b99-8cb7-c555df6aa7c2 | -9.00156 | -65.6985 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e27ab9b5-04e5-3bb3-b1e8-3b7e4a843e9b | -6.9237 | -62.90927 | 2025-08-24 06:14:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b36da209-70d7-3dff-a72e-7aae38d22ced | -8.91248 | -62.44924 | 2025-08-24 06:14:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 439f6f69-6987-305b-a46e-c3a372be543a | -9.01887 | -65.7217 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b93e17a-d5d5-39c0-b42e-e7e98a1bfc0e | -5.45055 | -60.18885 | 2025-08-24 06:14:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 6d31a28a-eadb-3022-93ee-dc2c0b3ceeb9 | -9.00846 | -63.63424 | 2025-08-24 06:14:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f6e0792f-b416-3a6e-a313-289333e387d6 | -9.00218 | -63.63747 | 2025-08-24 06:14:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 75f2ce1e-e34a-39c9-9b87-452ec1fdca9f | -7.55919 | -63.8551 | 2025-08-24 06:14:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 692091f7-25b5-38a8-a025-49355736c766 | -9.47768 | -63.13838 | 2025-08-24 06:14:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 586f6065-c7f8-382a-a9bd-d0bf6f3e9680 | -8.9068 | -62.45344 | 2025-08-24 06:14:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b54a38dd-a663-3605-9746-4825fd134e33 | -8.92109 | -62.44067 | 2025-08-24 06:14:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f6fa8438-5104-320a-a61f-4d85f86271e0 | -8.68813 | -68.68931 | 2025-08-24 06:14:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 96a72747-f147-3f78-a913-fc0ab6ce1b1d | -5.42415 | -60.17859 | 2025-08-24 06:14:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 5264d25e-614e-319c-a7a0-0b38d23e904e | -7.96838 | -63.07545 | 2025-08-24 06:14:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 74c3a8f1-52fa-3c65-8d3f-8d70869172ac | -9.04491 | -65.71672 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d439ee32-be54-3bc1-a923-1efacf9bf583 | -9.02911 | -65.7203 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a8235be2-8710-3b83-8dd4-ab52ee25fe74 | -7.55023 | -63.84626 | 2025-08-24 06:14:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c850aa6f-cb8b-308b-916b-1fd7dfd1ea79 | -9.01981 | -65.71318 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b8930a66-ced8-3630-b830-94a2ee58a307 | -7.55362 | -63.85431 | 2025-08-24 06:14:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7562c311-56d6-3b55-839b-9efe7e280381 | -8.9273 | -62.44152 | 2025-08-24 06:14:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4adca319-f1f5-39d5-806a-0569a8f38bae | -8.89797 | -62.41246 | 2025-08-24 06:14:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bbb284f9-ab09-33f9-b6db-f112b2b26d76 | -9.45634 | -63.50614 | 2025-08-24 06:14:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eccf1467-d339-33be-b0db-cd46fe4401be | -6.8781 | -59.82151 | 2025-08-24 06:14:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 97ce392c-3ce9-390d-a4be-b6dfaee9b927 | -9.02366 | -65.68661 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c45596ac-02e5-31a9-aa6b-b339d5d112ea | -8.58757 | -68.15111 | 2025-08-24 06:14:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bcb8265f-bb64-34a0-8aec-8cae7665ff13 | -9.02123 | -65.70438 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3008a6a8-a345-39bf-906f-6ce9f4398a5f | -9.01621 | -65.7037 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5c562058-0082-396e-a65b-9194e590a91e | -7.91754 | -63.05093 | 2025-08-24 06:14:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 559a33c7-327b-3718-bbd9-fab89a1c8081 | -9.02931 | -65.72006 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ddb4cf5a-f447-3f9c-9fb8-9b315d32c92d | -8.9155 | -62.43495 | 2025-08-24 06:14:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e6de033c-b68a-3908-ba65-57e4b246ebd0 | -9.01003 | -65.71153 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a7ca74d3-2cc9-38cf-8930-eaf2177c6f2f | -8.90125 | -62.43769 | 2025-08-24 06:14:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b6721d2c-3442-35ef-bebf-e136de4889e4 | -9.02006 | -65.71297 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f70b378f-ce00-3615-85de-6b7f0369da34 | -5.42582 | -60.16613 | 2025-08-24 06:14:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 0da3da86-b674-3c41-b9fe-c72ac8257557 | -9.45687 | -63.50193 | 2025-08-24 06:14:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d6d75b8-f98c-3808-aba7-396e34610061 | -8.13558 | -62.8685 | 2025-08-24 06:14:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8ae2890c-d952-3b88-bb83-b8f023140a9d | -8.89814 | -62.4224 | 2025-08-24 06:14:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 12404c27-34ef-33a6-896a-edc5a0ed0498 | -9.0226 | -65.38724 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 82c8313e-bca8-3a66-be3a-8e9ee9cc1744 | -8.63464 | -62.6268 | 2025-08-24 06:14:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 0404cdb2-09ca-34de-828d-35cd34ca83f0 | -9.06497 | -65.71976 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d26b0464-d172-3279-be1a-d1109335d5d6 | -7.54949 | -63.84233 | 2025-08-24 06:14:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5ad941fd-752b-3a8f-bd2a-a81166b7199b | -9.24612 | -60.47895 | 2025-08-24 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6a6de7b6-40ef-38cf-a9c6-a25644e94d22 | -9.0309 | -65.70853 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 576e8850-454e-3721-9d74-eca454f6912b | -9.00196 | -65.69556 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 51c8bce0-fa3b-3750-8c1d-fd4d2f822f2c | -9.19483 | -64.5531 | 2025-08-24 06:14:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0607ca63-989d-3d9b-bb05-02e5354c9eee | -8.89504 | -62.43679 | 2025-08-24 06:14:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1d4eb6c7-c014-3d31-832c-e1224f21681d | -7.80844 | -63.56103 | 2025-08-24 06:14:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 09b138d9-2262-3d0d-8dce-6a0a8fe70d19 | -9.02163 | -65.70145 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 05df4c25-5662-3d96-b625-f57c58bed0f4 | -7.56428 | -63.85962 | 2025-08-24 06:14:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dcd03e8f-1040-37b5-b909-3977805e36e3 | -9.00657 | -65.69929 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3f3883f0-7822-3fc5-8d5f-dcb4d656aa74 | -9.197 | -60.76681 | 2025-08-24 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 55588b5d-dfc7-3efd-9425-ab2e2d5da664 | -9.02321 | -65.68679 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 42681eec-89bb-30b8-b7a0-78b78ac70cb7 | -9.20231 | -60.78225 | 2025-08-24 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2d42423c-4d8d-3d5e-9bdc-5660c8201c8e | -8.67539 | -68.69113 | 2025-08-24 06:14:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bae8add7-b3a6-37c2-99e7-f138ece8eff1 | -7.55871 | -63.85881 | 2025-08-24 06:14:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0a116c23-6221-3b44-b2cc-411b6f31d4f5 | -9.6308 | -63.10363 | 2025-08-24 06:14:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ea6734a4-aa10-372e-b499-60fb3dd740f9 | -7.54921 | -63.85368 | 2025-08-24 06:14:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6de8565a-5c83-3fa2-b19f-291c6e0e3b3c | -8.68405 | -68.6887 | 2025-08-24 06:14:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e1e759d6-08ac-3d0b-ab61-d03a9ae6c08e | -6.57435 | -59.87616 | 2025-08-24 06:14:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 64ff50c9-2779-37bb-a1ff-7916de72d0e7 | -8.61391 | -62.64306 | 2025-08-24 06:14:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f00a8900-6b23-3c94-b236-931374f801a0 | -9.02389 | -65.72235 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08438c31-c817-3f1c-be26-d44799aeb1da | -9.01385 | -65.72102 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0a6d696-4c77-3aa1-9924-d39ef83b8818 | -7.55428 | -63.85816 | 2025-08-24 06:14:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 77dad598-f4bc-3c0d-98d2-9e58d5c40d0d | -8.61254 | -62.60459 | 2025-08-24 06:14:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |
| bb0031a6-c5c3-36c6-9903-abdec31afeaf | -7.54901 | -63.84606 | 2025-08-24 06:14:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b6718813-d43a-352f-a5f9-3252d6503baf | -8.14157 | -62.86935 | 2025-08-24 06:14:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0d695b19-b2b5-35cd-bd8b-113409e68925 | -9.24416 | -60.47993 | 2025-08-24 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 85df0a9a-c2dc-35ce-b4db-4ef58e18872c | -9.04955 | -65.7204 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ad0062bb-216c-36e4-b8e9-f0f82112820a | -6.92481 | -62.9088 | 2025-08-24 06:14:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c7be02d0-1808-38f8-9fcd-20cca6b86ea3 | -9.01199 | -65.69708 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 71c492bf-c4e7-39e8-a092-8bd5e1ddde2d | -8.14756 | -62.87018 | 2025-08-24 06:14:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e6c2ce4f-a584-36f8-8308-1e08369c00fe | -7.76391 | -73.06116 | 2025-08-24 06:14:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1ab788c-aa6b-333e-b27e-8f057d8d6cac | -8.91987 | -62.44047 | 2025-08-24 06:14:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ee83407-f12f-372c-b9ee-ac6c79c2d2e9 | -8.9174 | -62.4202 | 2025-08-24 06:14:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d0c74149-7f88-3a88-8c42-c946316da478 | -5.43264 | -60.16715 | 2025-08-24 06:14:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| f1b1f3c3-12d4-3684-8f1f-6f162fc8d30e | -9.00697 | -65.69633 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 81e45cfe-5062-34b2-b338-33be876a112c | -9.02484 | -65.71386 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 81809461-871c-3108-82c3-74b7aa14f225 | -9.02045 | -65.71012 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9e1399c0-d00c-37f0-8c7c-39bcb8c3836d | -9.19617 | -60.77476 | 2025-08-24 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6583cb95-97f8-32ed-b4a6-cd35c8bf08e0 | -9.00617 | -65.70223 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| cda85003-d5c5-32ca-b1c7-ae8bd5e5e7f8 | -8.90568 | -62.45323 | 2025-08-24 06:14:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cb1f71e1-0c4e-3bc8-8588-d05eeb720dd5 | -8.90066 | -62.44258 | 2025-08-24 06:14:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 58d64a47-041e-35af-9174-c83df19b6198 | -9.07883 | -66.067 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d3408f2d-6cfc-35b5-82f7-3f0be6ce46aa | -5.61407 | -60.23558 | 2025-08-24 06:14:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c9a79a1e-ec55-382b-a246-587442f9b196 | -9.24529 | -60.48581 | 2025-08-24 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 33cff0f1-8379-3d66-8fcf-a1d548170022 | -7.80951 | -63.55311 | 2025-08-24 06:14:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3513a1b9-b667-3bec-950f-8f0aca161683 | -9.01159 | -65.70004 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8f57c8e3-e29e-37b5-ad8e-b50514783da8 | -9.23307 | -60.92669 | 2025-08-24 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 69054425-c48a-3146-81c1-e399236a7ca5 | -7.9737 | -63.08058 | 2025-08-24 06:14:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d2a29e87-bbb0-39b5-a500-a691eaf17df8 | -8.90983 | -62.41904 | 2025-08-24 06:14:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e9a948a7-86fa-3c7a-b14c-f4546fd474d1 | -9.13947 | -60.77515 | 2025-08-24 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 582b1c29-838e-3e52-8d9b-7f19dcdad421 | -9.0213 | -65.70165 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0f1dc19e-f0fd-3821-a4ff-f952d9ac2248 | -9.02824 | -65.68747 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0f067327-192f-35bd-a669-0bea81171116 | -8.91605 | -62.41994 | 2025-08-24 06:14:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| babc245a-1c51-35d4-80fb-84d5742a41c4 | -9.0305 | -65.71141 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |


[Clique aqui para ver as próximas entradas](README87.md)
