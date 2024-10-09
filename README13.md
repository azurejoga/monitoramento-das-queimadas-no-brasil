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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 979e1bc9-4591-37cb-a4a8-0bd948e0c054 | -12.6539 | -47.037399 | 2024-10-09 00:39:44 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 56182618-732e-3748-a00a-75cb7ef9e30a | -13.5654 | -51.3717 | 2024-10-09 00:39:44 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cf9765fb-f4a1-309a-b662-e6928b6d12ce | -10.0469 | -36.377602 | 2024-10-09 00:39:45 | METOP-C | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| 4c2da658-4f73-3534-8863-4818de4b71d1 | -10.0523 | -36.398399 | 2024-10-09 00:39:45 | METOP-C | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| 0655ad61-866d-37c5-bd7d-14f32d30e7fc | -10.0373 | -36.3801 | 2024-10-09 00:39:45 | METOP-C | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| 8136b386-6e1f-385e-b655-a76adcc64c35 | -10.0427 | -36.400902 | 2024-10-09 00:39:45 | METOP-C | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| 854cda91-d3d5-32b4-b8a6-f416b661f2c6 | -11.8886 | -43.879601 | 2024-10-09 00:39:45 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 54ee6786-80a8-3c7b-969a-0d234af2f4e2 | -11.8903 | -43.886902 | 2024-10-09 00:39:45 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0b0fb333-84e6-327e-b2d9-26a2f9b76747 | -12.7748 | -48.208199 | 2024-10-09 00:39:46 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 74b58d72-49fe-3180-9a87-339bdc5e2a5f | -11.9222 | -44.605801 | 2024-10-09 00:39:47 | METOP-C | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bc44ec3b-2636-381e-9350-547d38986e5b | -11.9238 | -44.612801 | 2024-10-09 00:39:47 | METOP-C | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6b09bc26-d295-3fde-8011-fd2dea779856 | -12.7275 | -48.4184 | 2024-10-09 00:39:48 | METOP-C | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9dbb7eff-69e2-3dfe-a070-366bba1788ff | -12.7293 | -48.4268 | 2024-10-09 00:39:48 | METOP-C | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ffad9b55-5f56-3577-82c7-015b27020d37 | -12.7178 | -48.420502 | 2024-10-09 00:39:48 | METOP-C | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0b5bfc65-9367-3eda-a195-bc5fe86f7549 | -12.4548 | -47.301201 | 2024-10-09 00:39:48 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0e52dc11-58b4-3d68-8be3-f5455468a4a6 | -12.4565 | -47.3088 | 2024-10-09 00:39:48 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 996f8b2a-c990-323d-883b-dfb47830c31a | -12.4581 | -47.316299 | 2024-10-09 00:39:48 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1efdc210-7de7-3942-847a-896e1a67f9cb | -12.7257 | -48.41 | 2024-10-09 00:39:48 | METOP-C | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6d688f6a-2ffd-32de-b5d4-f79b56d62a23 | -12.2028 | -46.716499 | 2024-10-09 00:39:50 | METOP-C | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3af463e8-b14f-3fba-9a5c-fc92f323bbb5 | -12.2044 | -46.723801 | 2024-10-09 00:39:50 | METOP-C | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5eddcc59-884c-39e2-a65c-7d4980c2c931 | -12.3111 | -47.2076 | 2024-10-09 00:39:50 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e33f6a0e-c0fc-3fd2-b12b-f2459016ff1f | -12.3127 | -47.215099 | 2024-10-09 00:39:50 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 099eade9-e48e-35bc-a1c8-6f0be0f6a30c | -12.3812 | -47.669399 | 2024-10-09 00:39:51 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 38b69188-a3ed-3a5a-b053-b00fd0608fab | -12.3714 | -47.6716 | 2024-10-09 00:39:51 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 80b4b3a2-3de7-36cd-81cf-8f8da2031a01 | -12.3731 | -47.679298 | 2024-10-09 00:39:51 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8ecdd165-ea4b-3780-801b-17330221044f | -11.6458 | -45.245899 | 2024-10-09 00:39:54 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cad27c1f-c04b-3dd6-a4b6-c3d0bcb57e98 | -11.6474 | -45.252899 | 2024-10-09 00:39:54 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 57165fc8-81c2-3d9f-b3c5-6e59530c2b27 | -11.649 | -45.259899 | 2024-10-09 00:39:54 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f737de5f-cc67-3445-8a97-a47340eeab06 | -11.6506 | -45.2668 | 2024-10-09 00:39:54 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d2c012d3-7358-3a52-899d-563365e0295a | -11.6985 | -46.484699 | 2024-10-09 00:39:58 | METOP-C | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 687c2c00-80de-3b66-8d52-1946f552d7a7 | -11.7935 | -47.3778 | 2024-10-09 00:39:59 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f12a41e0-5f50-3873-85ea-028f58ec51b7 | -11.7951 | -47.385201 | 2024-10-09 00:39:59 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fdfc5948-f51f-38d7-9250-da02e2af7ac8 | -12.0039 | -48.628601 | 2024-10-09 00:40:00 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c9abf582-5767-3b3a-b948-c85a0c6ada7e | -11.9097 | -48.286598 | 2024-10-09 00:40:01 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6cea4441-ca8c-3f54-9fc9-4f6fcbcb2610 | -11.9114 | -48.294701 | 2024-10-09 00:40:01 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b1c1f73c-c696-3221-a0f0-257a67332544 | -10.9529 | -44.1618 | 2024-10-09 00:40:01 | METOP-C | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b117e88b-954f-359f-9c5a-798e4fb95ae9 | -10.9546 | -44.168999 | 2024-10-09 00:40:01 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ceb7614f-aa09-3715-b887-1c2c498493e0 | -11.1223 | -44.940399 | 2024-10-09 00:40:01 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 01ee5302-e0bb-3905-bd80-12863cc3c38e | -11.1239 | -44.947399 | 2024-10-09 00:40:01 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 27e3d272-bc5b-3bab-a541-5c47bb8cad05 | -11.1255 | -44.954399 | 2024-10-09 00:40:01 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4f977002-6a04-3b42-b8cd-4be98708adf1 | -11.1397 | -45.377399 | 2024-10-09 00:40:03 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5620847f-90a5-3f90-913a-6612ef633781 | -11.1381 | -45.370399 | 2024-10-09 00:40:03 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| aefa333d-2809-3acb-95f9-c88244bd9b72 | -11.7411 | -48.4086 | 2024-10-09 00:40:04 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 742255a1-0241-31b1-9041-74cc1d9af44d | -12.2009 | -50.576 | 2024-10-09 00:40:04 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7b3cef5f-ebb2-3f71-9ac1-7e08af00e0e9 | -11.7313 | -48.410702 | 2024-10-09 00:40:04 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 888f6630-8329-34c3-9c82-58a9718ed0f4 | -12.1912 | -50.577999 | 2024-10-09 00:40:04 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c7b50912-e546-3887-a2c3-2aaf5dca6527 | -10.8583 | -44.600201 | 2024-10-09 00:40:04 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 658d7ef8-0192-30fe-bd20-310dd2005028 | -10.9399 | -44.7752 | 2024-10-09 00:40:04 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b40bdeb6-f4ce-3734-b264-0f684c35f733 | -10.8068 | -45.138699 | 2024-10-09 00:40:07 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e33a34de-1862-36f6-ab21-d86068f314f3 | -10.8084 | -45.145699 | 2024-10-09 00:40:07 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1acfa2f1-f600-3ae2-b02e-d5c256a32442 | -10.797 | -45.140999 | 2024-10-09 00:40:07 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5373cc01-4c35-33b4-a0ab-de684b47f065 | -10.7986 | -45.147999 | 2024-10-09 00:40:07 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 01d7fb95-a249-3aa6-a51d-7452e0f6e753 | -10.7159 | -45.012402 | 2024-10-09 00:40:08 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7217f132-59db-330d-a911-ac7eb2feeee5 | -10.7175 | -45.019402 | 2024-10-09 00:40:08 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 34a35322-23f0-37f4-afd8-808720e06da0 | -9.5738 | -40.339298 | 2024-10-09 00:40:09 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 9d59459c-eef1-3688-924b-0a8e246ff49d | -12.0009 | -51.037399 | 2024-10-09 00:40:09 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f4988cbc-68bb-3708-892d-854acad3a8c3 | -12.0033 | -51.049 | 2024-10-09 00:40:09 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 22178908-f843-3b88-83cd-9d1b228ec9db | -12.0056 | -51.060501 | 2024-10-09 00:40:09 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 111b371d-cef4-30f1-bf74-59562e987f36 | -12.008 | -51.072102 | 2024-10-09 00:40:09 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5877cba9-947a-34c5-b2dc-42862abb3b94 | -11.9911 | -51.039398 | 2024-10-09 00:40:09 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c525f26b-9a96-36b2-8501-b502ade50329 | -11.9935 | -51.050999 | 2024-10-09 00:40:09 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9847e885-7ceb-30f6-8151-d04b75ad2e79 | -11.9959 | -51.0625 | 2024-10-09 00:40:09 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 108c54ba-4685-322d-b4ac-b351af7e9672 | -11.9837 | -51.053001 | 2024-10-09 00:40:09 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 898bb907-efc4-36a0-8e70-9b627ccaf7ce | -9.5836 | -40.336899 | 2024-10-09 00:40:09 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| ac0217c2-ea90-3a9c-a89f-9fa3a2a928e6 | -12.6625 | -54.706299 | 2024-10-09 00:40:10 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 79fcc334-2f5b-3bb1-adf2-fed0cb7beb98 | -12.6527 | -54.708199 | 2024-10-09 00:40:10 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2eaa64b2-d862-38a1-89a7-4f6a39973b69 | -9.8059 | -41.674099 | 2024-10-09 00:40:10 | METOP-C | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 977847bb-bffa-3c9f-9297-4f8c6e20bd34 | -9.8082 | -41.683498 | 2024-10-09 00:40:10 | METOP-C | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| c112475c-2aba-31db-b325-8d030ee36c3d | -9.8105 | -41.693001 | 2024-10-09 00:40:10 | METOP-C | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| fec66672-3b75-3641-ae29-1f3d410634ab | -11.4686 | -49.477001 | 2024-10-09 00:40:12 | METOP-C | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9ffcaa70-5da7-3b91-9b65-88ec0b278c5b | -11.4705 | -49.486099 | 2024-10-09 00:40:12 | METOP-C | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 29b1b35b-8bd7-32b6-8f96-b3ea41ecc0d8 | -11.4725 | -49.4953 | 2024-10-09 00:40:12 | METOP-C | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 642b1fd5-af23-3b97-ac55-6a68116d0e42 | -11.5564 | -49.890099 | 2024-10-09 00:40:12 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f3f36b15-9570-3226-9a0c-239d3a22513b | -11.5584 | -49.899799 | 2024-10-09 00:40:12 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8640e036-941f-3234-a2fb-81dfeb924e98 | -11.5467 | -49.8922 | 2024-10-09 00:40:12 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0088e8b5-b872-34d3-86ec-2742cab2e2cc | -11.5487 | -49.901901 | 2024-10-09 00:40:12 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8f952e40-4640-31d1-9c24-99abee53bbb7 | -10.2827 | -44.165298 | 2024-10-09 00:40:12 | METOP-C | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 097700d8-4a69-3279-b5e9-356337289767 | -10.2844 | -44.1726 | 2024-10-09 00:40:12 | METOP-C | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3b7c2c07-8e3a-39b9-ab1c-7fafa63efd90 | -10.9665 | -48.526901 | 2024-10-09 00:40:17 | METOP-C | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 35ba34b9-1c87-3e75-914a-8b961ff5380a | -10.9683 | -48.535 | 2024-10-09 00:40:17 | METOP-C | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c7595c0a-e247-3036-9960-2b2310416423 | -11.3209 | -50.955299 | 2024-10-09 00:40:20 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a1a7f807-93e1-3abb-99b2-ca531f24c80b | -11.3232 | -50.966499 | 2024-10-09 00:40:20 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 215fa188-9450-3d9b-b8a8-bfec0932acd2 | -9.5307 | -42.9856 | 2024-10-09 00:40:20 | METOP-C | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 90a52e94-46c8-3da1-8035-30e6c12b9187 | -10.4902 | -47.527802 | 2024-10-09 00:40:21 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7264f8a1-ee86-3f18-a6f4-4e94f4c1e297 | -10.4919 | -47.535099 | 2024-10-09 00:40:21 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9e6ebf97-9a6e-3eb6-a502-02794fa7d7a3 | -9.6772 | -44.490601 | 2024-10-09 00:40:23 | METOP-C | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5b48c14a-5e75-3fa7-8cfd-fa4e4e470720 | -9.6789 | -44.497799 | 2024-10-09 00:40:23 | METOP-C | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2a1e5363-c5da-3683-afee-b74bd38115c5 | -9.5314 | -44.440601 | 2024-10-09 00:40:25 | METOP-C | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 642ebc69-519c-3a73-8643-c8a9a0e6431d | -7.1758 | -35.052898 | 2024-10-09 00:40:26 | METOP-C | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 22ba859a-a74d-3b20-a80a-afae4bc55722 | -10.5268 | -49.099899 | 2024-10-09 00:40:26 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 20c496d9-0f92-387a-844e-593cf6514eed | -10.517 | -49.1021 | 2024-10-09 00:40:26 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 88cb0b8f-6a76-37f8-a448-8d9cd7c7fe1e | -8.534 | -40.4352 | 2024-10-09 00:40:26 | METOP-C | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 07b115ed-c183-3195-9696-fa6bb1d05d55 | -9.4252 | -44.1175 | 2024-10-09 00:40:26 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a4b164fe-255f-3ab9-96de-c53c272593f8 | -9.4269 | -44.125 | 2024-10-09 00:40:26 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 29793a75-bc3b-37d6-8c34-4c17a94dc49b | -9.4171 | -44.1273 | 2024-10-09 00:40:26 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| cd432e5f-c757-34e4-bbb4-cf6ef4e27344 | -10.5412 | -49.450901 | 2024-10-09 00:40:27 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1bc3bbd1-8f77-382f-bbaa-964d1c815a85 | -10.5431 | -49.459702 | 2024-10-09 00:40:27 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bfd53a39-eca6-3475-a41e-f8b59ef50d0c | -10.5314 | -49.452999 | 2024-10-09 00:40:27 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8dbca259-a62f-3c5a-ae0b-20ab26fbd5b0 | -10.5333 | -49.4618 | 2024-10-09 00:40:27 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4a2c10d0-9ab0-3d99-8bc9-99054bbb44e6 | -10.6584 | -50.911598 | 2024-10-09 00:40:30 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README14.md)
