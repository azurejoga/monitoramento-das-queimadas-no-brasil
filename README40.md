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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f9788f8d-3bfb-3671-8b50-bcc3ec0f0ac9 | -18.6387 | -57.2785 | 2024-10-06 03:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 116.8 |
| d53c58ec-93d1-3b43-824e-dd4dc2088f90 | -20.6024 | -49.3591 | 2024-10-06 03:27:00 | GOES-16 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 71.0 |
| accd58eb-b717-377b-a20a-9be52acf37ff | -20.6018 | -49.3821 | 2024-10-06 03:27:00 | GOES-16 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 9ba497a6-a5a8-3b5b-9897-b0a3fde756ac | -20.582 | -49.3635 | 2024-10-06 03:27:00 | GOES-16 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 244.0 |
| 9d65d9e9-d9ac-3a0e-a72b-95b61f9534f2 | -20.5813 | -49.3865 | 2024-10-06 03:27:00 | GOES-16 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 583.6 |
| 59e5bf45-dc1a-3e8c-9da7-50449952b1d5 | -20.5807 | -49.4095 | 2024-10-06 03:27:00 | GOES-16 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 66.9 |
| dd4754d6-26fc-3d35-b5e0-53f562671837 | -20.5609 | -49.3909 | 2024-10-06 03:27:00 | GOES-16 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 66.6 |
| cca9774c-ad2b-3001-97e4-1a64574e7a22 | -21.5218 | -50.9088 | 2024-10-06 03:27:05 | GOES-16 | LUCÉLIA | SÃO PAULO | Brasil | 3527405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 156.8 |
| d170890a-7b3c-3706-8e18-e205dd111569 | -2.92525 | -40.4499 | 2024-10-06 03:28:00 | NOAA-21 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c531b429-8cc5-358a-ba29-666ad1fc8691 | -2.92468 | -40.45329 | 2024-10-06 03:28:00 | NOAA-21 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1c1663bc-a7f7-33ae-8f03-4227e8e0d7e4 | -7.23822 | -38.54306 | 2024-10-06 03:30:00 | NOAA-21 | BONITO DE SANTA FÉ | PARAÍBA | Brasil | 2502409 | 25 | 33 | nan | nan | nan | Caatinga | 4.9 |
| a16e7695-4cc4-30d0-b0a7-a4528b7d1ca3 | -7.19157 | -34.79864 | 2024-10-06 03:30:00 | NOAA-21 | JOÃO PESSOA | PARAÍBA | Brasil | 2507507 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d556abb1-ca29-3133-83f2-3c8250fdeef0 | -7.14008 | -42.62311 | 2024-10-06 03:30:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 73103cab-3108-3ff6-a081-d4c6807bdace | -7.13998 | -42.61997 | 2024-10-06 03:30:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| be7f56ab-13af-32e7-af22-d49f597dc554 | -7.1393 | -42.6273 | 2024-10-06 03:30:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d2c08415-4c75-311f-a511-509ba13795e6 | -5.57063 | -44.87632 | 2024-10-06 03:30:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 54a4b8e8-466e-3ffe-88c4-3945f6556c20 | -7.13923 | -42.62413 | 2024-10-06 03:30:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 78b86535-d661-3639-8ee5-36791893e721 | -7.13566 | -42.61084 | 2024-10-06 03:30:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6d651a6d-1ad8-3211-83a7-a6744e1d36a4 | -7.1306 | -42.60582 | 2024-10-06 03:30:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 58258ffa-9fe6-3295-8738-788a1dd4c886 | -7.12193 | -42.62102 | 2024-10-06 03:30:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 386fdadd-c8ee-3927-87e7-275e922721d4 | -7.12121 | -42.62505 | 2024-10-06 03:30:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| dfecd5fb-bc5e-3697-b71b-858162d917cb | -7.12048 | -42.62909 | 2024-10-06 03:30:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 14c53663-019d-3663-afa6-a606d2366014 | -7.11615 | -42.62004 | 2024-10-06 03:30:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1b2bf28f-a582-34ce-8aaf-2c7da3ea6c08 | -7.09074 | -34.99086 | 2024-10-06 03:30:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1bfbe5ba-0971-3551-bd94-4b7cb6c91bed | -6.97891 | -36.51779 | 2024-10-06 03:30:00 | NOAA-21 | JUAZEIRINHO | PARAÍBA | Brasil | 2507705 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2ed5b687-8635-3b75-b377-ed6c06f75d6c | -6.87314 | -39.20414 | 2024-10-06 03:30:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 143a7025-029d-364d-a11d-ff485b6d5caa | -5.81542 | -44.1374 | 2024-10-06 03:30:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 9d3091c0-43d0-320e-b3bb-610592f40999 | -6.87302 | -39.2016 | 2024-10-06 03:30:00 | NOAA-21 | GRANJEIRO | CEARÁ | Brasil | 2304806 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fed200c9-1fbe-3788-83da-10f004036832 | -6.85007 | -41.69222 | 2024-10-06 03:30:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| db2ce3f8-dd9e-3ae3-9cbc-d1eae63a5582 | -6.84529 | -41.68745 | 2024-10-06 03:30:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d2ca4d58-6c54-3f2e-8019-b68cb021b3d2 | -6.82944 | -42.81405 | 2024-10-06 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 6ef10633-5d33-3387-bd4c-cf6907413580 | -6.82356 | -42.81307 | 2024-10-06 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fd17a62e-12d6-3cc5-a34b-2e12ac7d6241 | -6.6363 | -42.1265 | 2024-10-06 03:30:00 | NOAA-21 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| cdcb35a5-bf1d-369b-ab76-664fd47a3242 | -6.62996 | -42.12941 | 2024-10-06 03:30:00 | NOAA-21 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| acca8f3b-fd7d-3970-97e4-348c1e9493f0 | -6.62924 | -42.13341 | 2024-10-06 03:30:00 | NOAA-21 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| ee131bc5-bb25-34a6-8a0e-eb99fc9b2569 | -6.62566 | -42.12101 | 2024-10-06 03:30:00 | NOAA-21 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9df8b1f6-cc6f-3055-b7d1-87b21fcd2c59 | -6.62499 | -42.12475 | 2024-10-06 03:30:00 | NOAA-21 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 18d2e5d4-3de9-3b69-bfd3-79b65df32255 | -6.62432 | -42.12846 | 2024-10-06 03:30:00 | NOAA-21 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9976dfc1-c006-3eca-9f66-edce1875ce44 | -6.62362 | -42.13234 | 2024-10-06 03:30:00 | NOAA-21 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 8cb30b5f-24c3-315f-97b1-bf96febb86ee | -6.61863 | -42.12778 | 2024-10-06 03:30:00 | NOAA-21 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 1805d793-c74e-303d-97c4-2fd9a1ea36a9 | -6.49531 | -41.37933 | 2024-10-06 03:30:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 75197197-3b97-338a-ae15-9dd7efd6d128 | -6.49264 | -41.37924 | 2024-10-06 03:30:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 899280b8-0282-3660-b30b-b7d280c9f9df | -5.57101 | -44.88389 | 2024-10-06 03:30:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 0edff35a-14f4-36b1-a205-281839982f66 | -6.48988 | -41.37865 | 2024-10-06 03:30:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e774a2be-813d-33c9-8c0a-1d194e2328ab | -6.0771 | -42.33835 | 2024-10-06 03:30:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| fdf892f4-e4b6-33ea-9cf2-1629c14b6d74 | -6.07638 | -42.34242 | 2024-10-06 03:30:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 58855fb5-6fe2-3458-9894-b511aed2bf23 | -5.72277 | -43.7958 | 2024-10-06 03:30:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9cbf30a2-2c95-30d0-8bae-7858f90adfea | -5.34679 | -36.13478 | 2024-10-06 03:30:00 | NOAA-21 | JANDAÍRA | RIO GRANDE DO NORTE | Brasil | 2405108 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d0dbd635-b83e-37bf-a5ac-4e430357ca46 | -4.85379 | -43.17852 | 2024-10-06 03:30:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2d3ffb95-ac62-321e-ba9c-4af740dca0c2 | -4.84927 | -43.16792 | 2024-10-06 03:30:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 861e052c-ecc8-3326-b734-fca3dbdc99c3 | -4.84844 | -43.17264 | 2024-10-06 03:30:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8fd331b4-1fec-37e2-aa11-03da3d03f897 | -4.75409 | -40.22338 | 2024-10-06 03:30:00 | NOAA-21 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 8.4 |
| c7f29c98-176c-3dd6-8d44-9a6ae30e249b | -4.75193 | -40.22112 | 2024-10-06 03:30:00 | NOAA-21 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 4d564d50-fd9f-3d1b-ac37-c781686730c1 | -4.75139 | -40.22419 | 2024-10-06 03:30:00 | NOAA-21 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| e6dc90d9-31b0-3e94-a1fc-e649c70cf766 | -4.13469 | -43.80705 | 2024-10-06 03:30:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6c1be9bc-3468-3fd4-9803-eff2c96c8ad5 | -4.13414 | -43.80869 | 2024-10-06 03:30:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a342ffc4-cd1e-3d1b-a2d4-e52582092779 | -4.13373 | -43.81264 | 2024-10-06 03:30:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0e1eb6c5-8fc7-3133-be75-2d41dbc97261 | -4.13313 | -43.81429 | 2024-10-06 03:30:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b26daaff-46a6-3f07-92de-56e2ae4d4ccb | -4.1282 | -43.80579 | 2024-10-06 03:30:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9950e913-8222-3931-a400-d5ec94e3208e | -4.12764 | -43.80751 | 2024-10-06 03:30:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c254a22c-2d66-3d9e-8e7d-44bbf23c6c89 | -4.12724 | -43.8114 | 2024-10-06 03:30:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 23e4b97b-f979-395d-b133-663d849a8cc2 | -4.04599 | -43.24761 | 2024-10-06 03:30:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 59d97e5b-f995-3045-8777-d05cf691e6cb | -4.0451 | -43.25267 | 2024-10-06 03:30:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7b93f430-9434-390b-a7fb-bde0a8bea263 | -4.04299 | -43.24555 | 2024-10-06 03:30:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 43a6f313-a732-38e0-8aab-1fdce1de9664 | -4.04214 | -43.25061 | 2024-10-06 03:30:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 57cf8dff-4628-3466-b334-6737027f70ab | -4.01359 | -43.24727 | 2024-10-06 03:30:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb689bc4-cc0e-38ff-8598-322683ab142f | -4.01267 | -43.2524 | 2024-10-06 03:30:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0206f6d8-4b99-3538-91e1-1e1ee1030029 | -4.01062 | -43.24516 | 2024-10-06 03:30:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e59e5409-1eff-36ac-b608-b6eafff51063 | -4.00974 | -43.25025 | 2024-10-06 03:30:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 64788685-e47c-37d3-a077-425b152fa4f4 | -3.80322 | -41.59135 | 2024-10-06 03:30:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 8c8209a1-0703-3b91-b813-ae40907575f2 | -6.34456 | -45.70699 | 2024-10-06 03:30:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| da6a3173-dc12-3d37-9b57-925e44c2fb7b | -3.80255 | -41.59528 | 2024-10-06 03:30:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 9b588d5a-8a6e-3866-bd86-3fe8d52b9374 | -3.80186 | -41.59925 | 2024-10-06 03:30:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 61279b8a-b344-3521-939a-5df1d76f5e38 | -3.79821 | -41.5864 | 2024-10-06 03:30:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 1716f2f0-ed4c-3b28-8f8f-8918b97ce82c | -3.79754 | -41.59031 | 2024-10-06 03:30:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 9de2ce3f-7c76-3e97-8394-30e23da378eb | -3.79686 | -41.59423 | 2024-10-06 03:30:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 797c9ec7-6b3c-33b8-a048-37fab80fb5b5 | -3.79618 | -41.59819 | 2024-10-06 03:30:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 869cf3ed-5713-3e32-9a6a-ddd707b9c30a | -3.71549 | -41.68238 | 2024-10-06 03:30:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 23.5 |
| 49906c14-8b72-301f-9cc1-ece6d43173dd | -3.71481 | -41.6864 | 2024-10-06 03:30:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 17.6 |
| b77e77ea-4e0d-3e36-89e9-463e1c6aa60a | -3.70975 | -41.6814 | 2024-10-06 03:30:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 14.6 |
| 5feaa645-ff7b-3e69-9b38-714823c8b7f2 | -3.70906 | -41.68544 | 2024-10-06 03:30:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 14.6 |
| af0eb010-ed75-3335-bae8-7b26772a4f50 | -3.31796 | -40.00703 | 2024-10-06 03:30:00 | NOAA-21 | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a1e73fd3-e98d-3d1e-9fc0-439ac966b6fd | -5.57217 | -44.87758 | 2024-10-06 03:30:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 9709e25a-bd32-36aa-96b1-12b50ec1a938 | -5.81551 | -44.13879 | 2024-10-06 03:30:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 047074fb-6b64-3f00-9bcc-9b6ab30bab23 | -5.57631 | -44.88372 | 2024-10-06 03:30:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 17238a53-ef13-32ac-a516-11864d876cad | -5.57898 | -44.87867 | 2024-10-06 03:30:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 316e1bf3-1bc5-3013-92ae-0a6f38bde8bd | -5.57745 | -44.87733 | 2024-10-06 03:30:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 29.1 |
| ef4ec46c-76a9-3f76-af64-69cd185afb7d | -6.34305 | -45.71512 | 2024-10-06 03:30:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 669f0b64-33b2-3a45-8761-0190e7fa4dc6 | -5.5778 | -44.88508 | 2024-10-06 03:30:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 6a9218b9-9c4e-3dd2-9810-d7fe6087bd11 | -6.34897 | -45.71109 | 2024-10-06 03:30:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 3d4bdc67-3fd7-319f-97b3-ec1f7e22c7fb | -6.35041 | -45.71465 | 2024-10-06 03:30:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a6087404-1d29-32ad-8c2e-43dfe056b639 | -6.35187 | -45.70673 | 2024-10-06 03:30:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3d767ed1-264e-3b69-8810-92694dacb411 | -6.41233 | -45.82283 | 2024-10-06 03:30:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8a2a853e-b913-3f57-b40d-b1fa5e12ba42 | -6.75314 | -45.65084 | 2024-10-06 03:30:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 095bfa0e-4ae0-3300-853a-d0a6bc813202 | -6.75443 | -45.64397 | 2024-10-06 03:30:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| af4ef596-f0ac-3abb-9626-adc53847aad8 | -7.24183 | -44.94259 | 2024-10-06 03:30:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f45f8bbf-a3df-3152-ba4b-8beee39b831f | -7.24295 | -44.93654 | 2024-10-06 03:30:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c918173e-ec84-37e1-8bcc-056402c62f7e | -5.8164 | -44.13187 | 2024-10-06 03:30:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 317b20fc-5c82-3ac5-910f-c28272b00f89 | -7.24681 | -44.93826 | 2024-10-06 03:30:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 20c44221-09f4-395f-bef7-cca8e2b26edd | -7.4625 | -46.0696 | 2024-10-06 03:30:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README41.md)
