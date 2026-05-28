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
| 9744edd4-67e2-3cf3-b38a-2812a71e2dc7 | -2.9666 | -39.92387 | 2026-05-28 03:49:00 | NOAA-20 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f4da7739-cb44-3549-9369-8b840751871e | -4.66202 | -42.42912 | 2026-05-28 03:49:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| beeff104-0311-3505-a6aa-321f93d6c30c | -4.65769 | -42.4284 | 2026-05-28 03:49:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| eb2806dd-bf3a-3516-baf4-4c8dd348794b | -13.2186 | -54.5182 | 2026-05-28 03:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 4be10824-7fa4-338b-94b5-2c3b17866552 | -13.2189 | -54.4975 | 2026-05-28 03:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 80c7a2d4-9eef-3b4c-be9e-08aa5f1c5877 | -11.591 | -47.4496 | 2026-05-28 03:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 455de061-6952-3436-bc6e-41e738fed413 | -10.97563 | -44.60445 | 2026-05-28 03:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3f9abee7-a444-32ea-9ec6-5cfea96abf69 | -6.54401 | -44.68374 | 2026-05-28 03:51:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cf76a1ae-25d3-3cf9-8d60-aac9acf54327 | -8.67779 | -48.30626 | 2026-05-28 03:51:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 94be5cc1-3552-35d9-aca3-9cbf03e0d227 | -9.34051 | -45.47179 | 2026-05-28 03:51:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8d80d61e-f014-3e4b-9e9a-a11116254589 | -5.95781 | -43.49333 | 2026-05-28 03:51:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 427defde-0bc7-3542-b5ba-876f8ac0974e | -11.59786 | -47.44347 | 2026-05-28 03:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 10f2b21f-fc70-322f-b26a-6ee26bfe4c39 | -10.61969 | -46.91048 | 2026-05-28 03:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e1817052-d75a-3b2a-a6ef-40ff2bb38e5f | -10.6307 | -46.90353 | 2026-05-28 03:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3f7e654d-3881-3101-b900-4dafea6b06f9 | -11.58918 | -47.44799 | 2026-05-28 03:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8ddc105c-43b7-3cfa-b3b9-403eb124128f | -11.58853 | -47.45143 | 2026-05-28 03:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 402bf958-0b45-3aa4-9c90-90d3d6c90ec1 | -11.58445 | -47.44351 | 2026-05-28 03:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 072230f3-ad36-3f55-a264-34e0ce17b3c1 | -9.34641 | -45.46718 | 2026-05-28 03:51:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 49e3a9fb-522b-3da2-8d54-c4b66f69071b | -11.59584 | -47.44227 | 2026-05-28 03:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4134be3a-6d61-3d09-b423-286fe6de7579 | -5.95408 | -43.48775 | 2026-05-28 03:51:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| edad9656-eb28-36de-91f7-0c402679c697 | -9.05 | -46.30542 | 2026-05-28 03:51:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b23a5d3-ebf6-3f99-9871-abcacdc5f0cb | -9.14599 | -51.27958 | 2026-05-28 03:51:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0539c7be-62be-38b0-9fcf-a7e6b710674b | -10.62541 | -46.90252 | 2026-05-28 03:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d69fcb7d-d590-36fe-8144-0634662fddd8 | -9.73165 | -49.21634 | 2026-05-28 03:51:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c8bd62bd-5f42-30c9-ad36-7effc5416d95 | -12.10062 | -40.28391 | 2026-05-28 03:51:00 | NOAA-20 | MACAJUBA | BAHIA | Brasil | 2919603 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1a56b27e-27a2-3a16-ba8d-1a0842ae936d | -9.39093 | -37.81131 | 2026-05-28 03:51:00 | NOAA-20 | OLHO D'ÁGUA DO CASADO | ALAGOAS | Brasil | 2705804 | 27 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 00e593dd-884d-341b-8bb7-2bcc4f2761b4 | -8.70706 | -47.80017 | 2026-05-28 03:51:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 84729abd-a62c-3b6a-a430-ad6054921144 | -9.04417 | -46.3078 | 2026-05-28 03:51:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 593cf9bb-d2a0-35ca-b1ff-33ca7df4b10a | -9.39355 | -48.4393 | 2026-05-28 03:51:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d4187d5e-8058-3344-8594-52b35699a887 | -9.94081 | -48.02021 | 2026-05-28 03:51:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a787f473-0328-32cd-93ef-98211d99cf65 | -9.34774 | -45.46961 | 2026-05-28 03:51:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9ddda99e-fe68-3bb1-acc4-a41adc4ba10e | -10.77562 | -46.9113 | 2026-05-28 03:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e584e4cc-6202-3b67-9411-66c535f710cd | -10.63728 | -46.89775 | 2026-05-28 03:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a6099df0-8301-365a-baac-22f6a84786b1 | -9.3572 | -45.46357 | 2026-05-28 03:51:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 28516705-0fa8-3bd2-aac1-0c44e857c241 | -9.35857 | -45.46598 | 2026-05-28 03:51:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 625cd7ed-4a2c-3230-b0c3-b80beb57e26d | -11.59116 | -47.44919 | 2026-05-28 03:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bb5e8415-3861-333d-b7c6-b25395194ebd | -11.58509 | -47.44009 | 2026-05-28 03:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0767b7b9-e757-3ad5-8dd5-774630502b44 | -9.73637 | -49.21547 | 2026-05-28 03:51:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dd7ca760-bab0-344f-863b-b22a2b7bbf15 | -7.34941 | -46.2156 | 2026-05-28 03:51:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9fbc4018-cafe-3b21-877f-10603279519a | -6.53913 | -44.68282 | 2026-05-28 03:51:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3acfe2e3-6744-3c7e-af83-9b80f38e8538 | -11.82938 | -48.21098 | 2026-05-28 03:51:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5fbfd777-340f-334b-adbd-bf2a9b001db4 | -8.72214 | -48.33403 | 2026-05-28 03:51:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4eefd599-fe65-32ba-a007-ac1dca87ea3a | -8.7246 | -48.32076 | 2026-05-28 03:51:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| dcc73797-ba74-3b21-b649-2537d111fec4 | -9.35817 | -45.45813 | 2026-05-28 03:51:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6ffcb86c-0c09-3550-9ff5-38bc0a8a0c24 | -11.59455 | -47.44915 | 2026-05-28 03:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 729012ea-5fe0-3efc-a0cd-a0b1bb873e29 | -9.14124 | -51.28743 | 2026-05-28 03:51:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 24bd8ff6-58f5-35c8-90a6-41bebb7b534a | -9.41714 | -40.37486 | 2026-05-28 03:51:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d0ce17a4-45d7-30bb-8bf1-3123843356ac | -9.95475 | -37.40491 | 2026-05-28 03:51:00 | NOAA-20 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ae4c9650-150f-323e-a464-2facf8d07d30 | -11.94039 | -43.39861 | 2026-05-28 03:51:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f380409d-b0f1-35d8-a869-c67efede9504 | -10.63792 | -46.89438 | 2026-05-28 03:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 38014ef4-ad95-32bf-a26e-59b71c42f1e0 | -11.8286 | -48.21498 | 2026-05-28 03:51:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0cb43789-9479-3dfb-b081-105e3a6f5c05 | -5.92223 | -43.47988 | 2026-05-28 03:51:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2d208121-1726-3a44-bfdf-b79bc6adfbc0 | -6.54299 | -44.68967 | 2026-05-28 03:51:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cf6bb265-34f3-363a-bd54-aeb5a9445f0b | -8.71286 | -47.80119 | 2026-05-28 03:51:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1ac2a047-4e50-3582-b6b2-2f97fe3c3b80 | -5.79137 | -45.13741 | 2026-05-28 03:51:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7bd11d3a-f76e-31d9-8085-d0d85b651a43 | -6.2879 | -43.62762 | 2026-05-28 03:51:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d55a5da0-56ad-3be6-be13-b41d108ba99a | -8.72897 | -48.33059 | 2026-05-28 03:51:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0f724278-df23-3c26-8633-1e701d8a72ce | -10.48171 | -48.90681 | 2026-05-28 03:51:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 3baac2b3-3ed5-392d-81af-042e238da218 | -8.72298 | -48.32954 | 2026-05-28 03:51:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f5c9f36c-d53a-36e6-b99a-448db8652cf5 | -5.79754 | -45.1322 | 2026-05-28 03:51:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e7789fc-feca-3f05-84d8-b1ab2de6e0d3 | -10.47478 | -48.91027 | 2026-05-28 03:51:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5a74d1ef-bf69-374c-9dfd-7ce337704933 | -8.7128 | -47.80157 | 2026-05-28 03:51:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a1c04e5a-fdea-3b28-9f14-4f99998efd7e | -8.72381 | -48.33641 | 2026-05-28 03:51:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ffa82942-a6cd-3631-a4ee-b9ce6e2268f9 | -9.52346 | -40.34531 | 2026-05-28 03:51:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 19c6bccf-3db2-31cd-bc1e-a9a17d7ab07f | -9.35958 | -45.46054 | 2026-05-28 03:51:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1d500d26-81b6-31e2-9ba4-4f0f4887072f | -12.00923 | -45.3494 | 2026-05-28 03:51:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 86ab8cde-66c9-393e-9ad6-c16e36ec51ee | -8.72379 | -48.32514 | 2026-05-28 03:51:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0291d513-5655-32f4-bec3-2196234a9984 | -10.84901 | -39.31175 | 2026-05-28 03:51:00 | NOAA-20 | CANSANÇÃO | BAHIA | Brasil | 2906808 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ccf395dc-b23f-3580-b16f-68d49eb32d85 | -10.77693 | -46.90437 | 2026-05-28 03:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c262c0a1-d346-3ad6-b7ad-d7560d57535e | -11.58983 | -47.44456 | 2026-05-28 03:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 479ca9d3-e96b-34c5-a60c-57873a4334ab | -9.34877 | -45.46408 | 2026-05-28 03:51:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b0c61b27-0ee7-360d-86da-c892a8164212 | -7.55659 | -42.64513 | 2026-05-28 03:51:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f2bbb6b0-da6f-3911-a518-354c371e1ed1 | -9.3621 | -45.46455 | 2026-05-28 03:51:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5ee76ec9-7d26-3742-9e43-b1ef7f2aa9d2 | -9.38758 | -48.43819 | 2026-05-28 03:51:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2a632e1c-0803-3922-b2c5-2bd6701af7a0 | -9.43928 | -48.89292 | 2026-05-28 03:51:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e24770dd-a9a7-3018-9089-a79955be89e1 | -5.92224 | -43.48214 | 2026-05-28 03:51:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5deba336-674a-30c6-97c6-93ff00b782d0 | -11.58646 | -47.44467 | 2026-05-28 03:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4a9d2bdf-cfc0-3c46-be2e-2d1943e89911 | -9.14267 | -51.28032 | 2026-05-28 03:51:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d9e174d9-aa89-3ee6-bd85-afb9536dac5a | -5.93456 | -43.4652 | 2026-05-28 03:51:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 60524714-83c3-3f55-9e6f-55aa9bfcc8b5 | -10.62416 | -46.90905 | 2026-05-28 03:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| fcea29fc-e8c4-3710-a3c9-2c21898b75f6 | -7.55593 | -42.64899 | 2026-05-28 03:51:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 30a5c2a1-56a4-33b5-8d51-91ec20fe4c7a | -11.5925 | -47.44234 | 2026-05-28 03:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 154b0d4f-cd04-3ba5-b68f-8df3e4147520 | -11.5939 | -47.45259 | 2026-05-28 03:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 98c4e50a-43fe-3922-bf80-0f8ea9906c75 | -9.9553 | -37.40141 | 2026-05-28 03:51:00 | NOAA-20 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 62ccf3ae-559e-321b-b836-883fc5399e4c | -9.3523 | -45.4626 | 2026-05-28 03:51:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0946292c-54a1-397a-ba75-951431764ed4 | -8.67865 | -48.30173 | 2026-05-28 03:51:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 87c94cf2-2d50-3423-819a-035cbdd7ab70 | -6.2925 | -43.62822 | 2026-05-28 03:51:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 10088797-7a3b-3e90-829f-6276f2ed558f | -11.60055 | -47.44693 | 2026-05-28 03:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f97d3ca3-4b32-3c18-83c7-c3aa3e4f75f7 | -11.59049 | -47.4526 | 2026-05-28 03:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 04fce223-32e1-33cc-9904-12aa213fa9ab | -10.63117 | -48.3274 | 2026-05-28 03:51:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 05184dc4-d065-3f05-a54c-a5b05712e58d | -9.05524 | -46.3063 | 2026-05-28 03:51:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1342b255-0a50-3829-9038-12db5668a7fa | -11.59317 | -47.43894 | 2026-05-28 03:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| acf5eb99-f33d-3b27-a564-d5805c473f64 | -9.35264 | -45.47055 | 2026-05-28 03:51:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b64a369b-283f-3447-b005-d02a1bcd444f | -11.93972 | -43.40233 | 2026-05-28 03:51:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 41308864-32cd-3720-b395-f9a99432ed1a | -10.48082 | -48.91132 | 2026-05-28 03:51:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b1cb54f1-2f8c-3cac-9fc9-da1ccc502506 | -5.95861 | -43.48866 | 2026-05-28 03:51:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 11339516-02f6-3136-a3c5-0031f93598f1 | -11.59183 | -47.44574 | 2026-05-28 03:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 90369fa1-5f5c-38fc-b1a6-0061d877987c | -8.72468 | -48.33193 | 2026-05-28 03:51:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f3406410-d751-3b62-85e4-85fddd638600 | -11.5952 | -47.44569 | 2026-05-28 03:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 751804ad-3576-3a35-8647-8efda99a7faa | -7.35476 | -46.21656 | 2026-05-28 03:51:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README5.md)
