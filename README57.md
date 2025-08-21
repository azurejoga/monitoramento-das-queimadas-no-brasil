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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a6cbfd72-0c9b-30c4-9490-efd9caca8836 | -13.0123 | -45.1756 | 2025-08-21 06:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 170.1 |
| 8f782d5a-87bd-3123-a852-297db933f225 | -7.0354 | -44.6167 | 2025-08-21 06:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 168.8 |
| 7241763c-77b7-31f9-842c-1066f5c61fc9 | -13.0312 | -45.1957 | 2025-08-21 06:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 88.7 |
| a743b851-098e-350d-81cf-a6e2c97cd192 | -7.0164 | -44.6413 | 2025-08-21 06:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 108.0 |
| cc564f8b-2556-30c1-b251-6a6d48482944 | -8.87434 | -62.40775 | 2025-08-21 06:20:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a6dd63be-4545-33de-b3de-03ee7d06aae0 | -9.51821 | -70.42199 | 2025-08-21 06:20:00 | NOAA-20 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 14477838-c111-37b3-a4be-d2e0fac96ec1 | -8.86803 | -62.41509 | 2025-08-21 06:20:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 46627579-3b32-3221-ba85-5aca2a52d5a5 | -8.29374 | -70.10289 | 2025-08-21 06:20:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 51d0ac63-10db-39e6-9b4f-fb13766582b8 | -8.87485 | -62.41595 | 2025-08-21 06:20:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 030b320d-ed2a-3793-8181-29717467a18d | -8.87589 | -62.39542 | 2025-08-21 06:20:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ecc330dc-3819-33a4-8e82-886c21034126 | -8.87024 | -62.39648 | 2025-08-21 06:20:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 014f647e-755d-3ad2-9bc1-01180673a81e | -8.22416 | -69.84386 | 2025-08-21 06:20:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b2dfaa7d-6275-3c21-be41-eb239c5b83db | -8.86672 | -62.41315 | 2025-08-21 06:20:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 70d98c6c-0f9d-3e97-811f-81466754322a | -8.33124 | -70.27378 | 2025-08-21 06:20:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7cb109b0-5370-3e00-9437-921280022d1f | -8.87468 | -62.3592 | 2025-08-21 06:20:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e52a2ea4-4715-3643-b274-ae31e1821aa4 | -8.88798 | -62.4095 | 2025-08-21 06:20:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3515bc48-b4b1-3860-af64-4dc5abf7c621 | -7.8416 | -72.88319 | 2025-08-21 06:20:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a88b2174-935c-359c-9ff5-ca704fe8669a | -8.85848 | -62.36817 | 2025-08-21 06:20:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6946c924-e7a0-333b-aff8-c5c088857ab8 | -8.88243 | -62.41056 | 2025-08-21 06:20:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dcb56a7b-1b2c-3ea4-b4cb-e963c04ea3bf | -8.56821 | -70.04134 | 2025-08-21 06:20:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef515a3b-9cd7-36c8-93e8-440f2e55762c | -7.7775 | -66.95377 | 2025-08-21 06:20:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5ef19a15-d785-3977-bca9-cdab200c6a30 | -7.55337 | -63.8504 | 2025-08-21 06:20:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 525055b8-7024-3164-9803-896f81bf83c8 | -7.55403 | -63.84847 | 2025-08-21 06:20:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 036a02b6-7162-393b-a42f-3fa191f4d71a | -8.70505 | -71.00801 | 2025-08-21 06:20:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0ebcb076-1f60-370b-bee6-9ad1aa1d0a6d | -8.22618 | -69.84348 | 2025-08-21 06:20:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4bfbbd12-950f-3225-bfcd-68c36ed2a23f | -9.19583 | -65.66541 | 2025-08-21 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86fd071c-e094-39d3-8b29-dbee0fd45307 | -8.87355 | -62.41401 | 2025-08-21 06:20:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fd953dd4-6a6b-3eed-99e7-2f2fd54e890c | -8.83931 | -69.1104 | 2025-08-21 06:20:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8f908cc-65aa-3e6a-940f-5819f5d7cd4d | -7.55954 | -63.85398 | 2025-08-21 06:20:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0a4f9f2b-c4b6-32f3-9c46-7e7ed0da59b9 | -8.87635 | -62.40345 | 2025-08-21 06:20:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 7b293f85-1eb0-3ab1-ba4e-f8cec683daee | -8.88925 | -62.41149 | 2025-08-21 06:20:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2cf03b9e-4b44-3c84-be41-9f6160e1f117 | -8.86593 | -62.41943 | 2025-08-21 06:20:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 7.3 |
| d552f8a0-f67f-3ca7-a63b-68fe8d96daf0 | -8.86298 | -62.38766 | 2025-08-21 06:20:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 10c389cf-4fe5-36d3-a85d-a1bcc09800d1 | -7.84508 | -72.88371 | 2025-08-21 06:20:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 46867608-77e8-3633-83ee-e6a11fe2f56e | -8.86877 | -62.40882 | 2025-08-21 06:20:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 7d36d61e-f0d6-3130-992b-d8377146dd16 | -8.86533 | -62.36896 | 2025-08-21 06:20:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0dc296b3-5a5d-34c2-8582-559bf0a45c67 | -8.55301 | -66.95401 | 2025-08-21 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1c4f689c-f7f9-3157-89e8-63343cdc44af | -8.3272 | -70.27318 | 2025-08-21 06:20:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 34b0c1e6-f4ec-39ed-872b-bac16014fadc | -7.50547 | -63.8372 | 2025-08-21 06:20:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 02451c9e-ae8b-3897-ad23-9bc4f417c94b | -9.39159 | -70.46597 | 2025-08-21 06:20:00 | NOAA-20 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| acf9c983-f217-3eea-aae4-7a299cc33f16 | -7.54724 | -63.85237 | 2025-08-21 06:20:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a72fd537-089c-3c70-bc57-bb0b0eb1aa5d | -7.77672 | -66.95957 | 2025-08-21 06:20:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd570845-f1b5-31fd-9014-da5e923ee9e8 | -8.86143 | -62.40008 | 2025-08-21 06:20:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 42317aa1-f4ad-31f3-884d-097876dc8d9d | -8.88316 | -62.40442 | 2025-08-21 06:20:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 686ab569-952d-3b6f-b626-1ff7470a22a0 | -8.86728 | -62.42137 | 2025-08-21 06:20:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 20117fcb-41e6-3ae2-adc7-f92ea6ff2165 | -8.8756 | -62.40969 | 2025-08-21 06:20:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 8a59b411-c429-3e96-8bea-e4f42c499937 | -8.54873 | -66.94732 | 2025-08-21 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aecd16d3-c2d4-3982-81d8-3ec05e81392c | -7.45449 | -70.01968 | 2025-08-21 06:20:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8d0da3c6-ea39-31fb-86ee-2ef01f35157d | -8.55462 | -66.94205 | 2025-08-21 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31bb45f2-16aa-3781-b85c-2297052b9b10 | -8.87394 | -62.3654 | 2025-08-21 06:20:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 131321d7-94a9-3510-99e4-57723f55d25c | -8.79649 | -67.00512 | 2025-08-21 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 93360267-048e-31b0-aed9-3755b98d92df | -8.87296 | -62.36355 | 2025-08-21 06:20:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 10153dfb-b205-347e-8f49-97e01bb22223 | -8.46566 | -70.09049 | 2025-08-21 06:20:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e3b437b3-3dca-37ef-a84e-f3e2ed5957af | -7.77711 | -66.95667 | 2025-08-21 06:20:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 77c29445-8a2d-3039-8aa6-31a01081554c | -8.55422 | -66.94503 | 2025-08-21 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94bbc17b-5b77-31aa-8281-4f4561ee49ae | -7.55339 | -63.85318 | 2025-08-21 06:20:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 12669498-0084-3668-a058-6ee9098f02a4 | -7.5061 | -63.83245 | 2025-08-21 06:20:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e0df5acd-4be2-37ff-9815-f66b36346572 | -8.86951 | -62.4026 | 2025-08-21 06:20:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 368db745-b7b9-3416-9a2e-5084b27f1009 | -8.28942 | -70.1024 | 2025-08-21 06:20:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 44b677b4-42cb-3f42-a08e-01d109da0909 | -8.87276 | -62.42026 | 2025-08-21 06:20:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 51f6ed9f-6840-330b-bda8-2552b418f1da | -8.57179 | -70.04564 | 2025-08-21 06:20:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d25fee0-6ad2-3f0b-ace9-1fa582c364c7 | -8.56556 | -70.05987 | 2025-08-21 06:20:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8bde8580-d2b9-34e1-842e-44c10a0cfb92 | -8.8622 | -62.39389 | 2025-08-21 06:20:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 76aa6794-ea55-363d-8575-9bb38d6ee539 | -7.55952 | -63.85121 | 2025-08-21 06:20:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d6db2ca3-e79e-3bb7-955a-28c9dfa59dbf | -8.54953 | -66.94134 | 2025-08-21 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 92fb2b59-ef4f-38da-9a0e-541e3ddf255f | -7.51226 | -63.83326 | 2025-08-21 06:20:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2aedfecd-7fbf-3697-a47f-2ad973c1da0a | -8.55381 | -66.94801 | 2025-08-21 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 62990f14-a499-3195-875d-017d25103799 | -7.78675 | -66.96106 | 2025-08-21 06:20:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3819c89-5098-3fba-a1bf-7e8e02ddae6c | -7.55891 | -63.85593 | 2025-08-21 06:20:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 68967319-c49b-3ad1-a025-bc877b41bb20 | -8.29351 | -70.10297 | 2025-08-21 06:20:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ecbaf3d1-dcba-3369-b2cb-04b269cdb30c | -9.19632 | -65.66171 | 2025-08-21 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a630d3d-5bdc-38a6-bce1-738524c5f88e | -8.86455 | -62.37519 | 2025-08-21 06:20:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8d1e7fb8-319a-3849-aa6c-771c2f107bc3 | -8.88038 | -62.41482 | 2025-08-21 06:20:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| eaa48bdd-968a-335a-8df3-59116027d194 | -7.78213 | -66.95741 | 2025-08-21 06:20:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74ee2b5b-f1fd-3334-88d4-86f915b20e34 | -8.46619 | -70.08682 | 2025-08-21 06:20:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4aefd811-cea8-31f6-b475-273fb52daa9e | -8.79141 | -67.0044 | 2025-08-21 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d77892b8-cd35-3a48-99e7-e60d1d7566d3 | -8.85989 | -62.41236 | 2025-08-21 06:20:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 8a50c98c-c54c-3fe9-92e4-bcfe21d25c9f | -8.8675 | -62.40694 | 2025-08-21 06:20:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 14.0 |
| f1d2541a-2e76-32f3-8acc-7b508de16e29 | -8.28965 | -70.10235 | 2025-08-21 06:20:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 594ea455-78b8-36a9-908c-93dc5359b375 | -8.86905 | -62.39466 | 2025-08-21 06:20:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 5257bd2e-4b82-3ea3-bef1-e09c309f56b6 | -8.86828 | -62.40077 | 2025-08-21 06:20:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 8bdde8e6-9cd3-33a2-b697-51b07481d37b | -8.33072 | -70.27734 | 2025-08-21 06:20:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 111412cf-f271-345a-9eaa-146ab56dfc66 | -7.54722 | -63.84958 | 2025-08-21 06:20:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1c8bc77c-3e0b-318a-bd5c-208e7ae77f2e | -7.55276 | -63.85512 | 2025-08-21 06:20:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b2b3918f-56a8-305d-8666-a72ebf36bc94 | -7.54788 | -63.84766 | 2025-08-21 06:20:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9a44ae70-7499-38c5-bf1b-a85ed0c223dc | -8.02581 | -71.40739 | 2025-08-21 06:20:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2eaa567c-638f-34eb-bb44-ed9c30cc05d9 | -8.70348 | -71.01065 | 2025-08-21 06:20:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 463349f9-ac19-3baf-9537-b890244becef | -8.85911 | -62.41862 | 2025-08-21 06:20:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 7.3 |
| dc96bbf8-2bd7-3531-8588-082e088ae2e3 | -8.54913 | -66.94433 | 2025-08-21 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b0b1c225-1b28-39cb-a005-cf04a0a34041 | -8.88116 | -62.40862 | 2025-08-21 06:20:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a6da9fd1-d39e-334c-9dff-0aaebc2434f1 | -8.55341 | -66.95101 | 2025-08-21 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f4fb6a48-b1c3-3852-8070-728a10ebcd26 | -8.57232 | -70.04194 | 2025-08-21 06:20:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f07d165-5a4d-333c-b6e8-84f4e29b7ab6 | -8.3544 | -70.28449 | 2025-08-21 06:20:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c2d07cd-1a0a-3db8-af62-2416215139e4 | -8.8661 | -62.36279 | 2025-08-21 06:20:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 00b154cd-7c0c-3bed-917d-ea5c82621e28 | -9.05066 | -67.45961 | 2025-08-21 06:20:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f9db9e34-6c6a-3cd7-9fd6-b0875d727fd7 | -7.54661 | -63.8543 | 2025-08-21 06:20:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 95e10c3f-ae46-3f1b-8271-084b95e936f3 | -8.87218 | -62.36975 | 2025-08-21 06:20:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2953c435-4549-37cc-9482-247dbfc8cfe0 | -8.22203 | -69.84286 | 2025-08-21 06:20:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| abaca5a4-31b3-3531-9fb3-a825072b3871 | -8.8736 | -62.4115 | 2025-08-21 06:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 72.0 |
| d521f6ad-f5db-35b2-b6b7-5f972059d707 | -7.0166 | -44.6184 | 2025-08-21 06:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 131.0 |


[Clique aqui para ver as próximas entradas](README58.md)
