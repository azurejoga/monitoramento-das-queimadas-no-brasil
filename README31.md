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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2fb3d7fa-eef5-3ab3-ac54-9734dba597cb | -13.95312 | -46.35792 | 2025-08-10 12:14:00 | TERRA_M-T | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 502d3174-c009-3c2a-8fda-0f4f5b731df7 | -11.64937 | -50.2114 | 2025-08-10 12:14:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 3361a859-f993-3fa6-b8de-9cb05286b926 | -8.75499 | -40.79224 | 2025-08-10 12:14:00 | TERRA_M-T | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 16.6 |
| 88b56725-ef05-3a72-b549-e98c6046d663 | -12.98417 | -47.49911 | 2025-08-10 12:14:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5cb91bd6-747b-337c-ad66-0963c16c8b55 | -8.11939 | -47.43204 | 2025-08-10 12:14:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 8b284531-0666-38ed-8377-9864efaa0f03 | -12.55615 | -47.08279 | 2025-08-10 12:14:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 24.0 |
| a8c3144a-ab56-3a6d-8b36-d40b39afec50 | -7.44949 | -43.98013 | 2025-08-10 12:14:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 376.1 |
| b725cc5b-7a6a-3bd8-adea-5ae4e3e5fbee | -8.46074 | -46.93758 | 2025-08-10 12:14:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7e174695-ef4d-379f-a5dc-78797a86ecc4 | -11.72996 | -45.00733 | 2025-08-10 12:14:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 2a7a88a2-46db-3432-b666-8efe105b71d5 | -14.30367 | -51.97047 | 2025-08-10 12:14:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 9b05b430-31d1-3740-89eb-d9a359ab8c6f | -7.37272 | -44.84838 | 2025-08-10 12:14:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 17d07511-d005-3fbb-9990-3d9d8e195159 | -7.1195 | -44.22733 | 2025-08-10 12:14:00 | TERRA_M-T | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| b9e44be4-31ed-323b-b6f7-93551898ffab | -7.87877 | -45.55268 | 2025-08-10 12:14:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| b302ef4b-029a-37d8-804c-75864f5ee0e6 | -16.30305 | -52.92058 | 2025-08-10 12:14:00 | TERRA_M-T | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 473cb778-4a0d-32ec-b8f1-4cf3b809685d | -14.13333 | -44.88708 | 2025-08-10 12:14:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 218f8a1e-8917-346d-a370-e3bbcf23ce62 | -8.10845 | -47.44085 | 2025-08-10 12:14:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 950d2151-ccfa-30dc-a1fe-5e8a9bd4b59c | -18.97759 | -47.07653 | 2025-08-10 12:17:00 | TERRA_M-T | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bfb26aba-a2ec-3fda-8d0d-323cc155bb2c | -21.93435 | -47.79955 | 2025-08-10 12:17:00 | TERRA_M-T | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d8cf9dd3-76e6-3bdb-87a8-e86cbb7540e7 | -19.82735 | -44.63232 | 2025-08-10 12:17:00 | TERRA_M-T | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 9e5e09dc-bbea-332a-a207-71cf3586dd5e | -18.17803 | -46.99327 | 2025-08-10 12:17:00 | TERRA_M-T | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 81921df1-ba34-35b1-9ab1-450b1c5fd3be | -22.2664 | -48.63256 | 2025-08-10 12:17:00 | TERRA_M-T | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| f90f3911-50d8-3ae4-a2a8-1fd2b7c2c20e | -18.17672 | -47.00249 | 2025-08-10 12:17:00 | TERRA_M-T | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| d92f2a07-f013-3bf0-b8d4-f2a118d04dc0 | -22.53003 | -46.82142 | 2025-08-10 12:17:00 | TERRA_M-T | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| 3ebae1c9-ce30-3bab-b31c-7ac6415418db | -22.53139 | -46.81133 | 2025-08-10 12:17:00 | TERRA_M-T | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.8 |
| 7a546eb4-f05e-357f-b2da-bd80d6aca925 | -19.92559 | -43.6486 | 2025-08-10 12:17:00 | TERRA_M-T | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 66c2defe-10a1-3d54-a324-64cd1068175e | -18.53259 | -45.01071 | 2025-08-10 12:17:00 | TERRA_M-T | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 4fb3f3fa-c8e3-3834-85ed-e392fc526634 | -19.40981 | -43.3641 | 2025-08-10 12:17:00 | TERRA_M-T | ITAMBÉ DO MATO DENTRO | MINAS GERAIS | Brasil | 3132800 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 924dc64f-9ee8-322d-8ea4-ab56889964fa | -21.08864 | -51.59306 | 2025-08-10 12:17:00 | TERRA_M-T | NOVA INDEPENDÊNCIA | SÃO PAULO | Brasil | 3533205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 6a2e0a83-2da6-3447-b131-f1d17502e30f | -19.4055 | -43.35663 | 2025-08-10 12:17:00 | TERRA_M-T | ITAMBÉ DO MATO DENTRO | MINAS GERAIS | Brasil | 3132800 | 31 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 4ab17db4-d62b-3091-9a03-729d12d70cf9 | -22.26779 | -48.62302 | 2025-08-10 12:17:00 | TERRA_M-T | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 46.0 |
| e6572a3a-c169-3218-8786-bd1de16d82bc | -11.7278 | -45.0274 | 2025-08-10 12:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 465a321c-2d17-34ee-b633-616eb0f40506 | -14.1108 | -45.3844 | 2025-08-10 12:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 175.6 |
| 83fc087f-19b5-3304-a56d-254e7c36f318 | -14.1103 | -45.4077 | 2025-08-10 12:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 79f0a90d-f5f2-3dd2-8376-964658958fd5 | -7.437 | -44.0036 | 2025-08-10 12:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 09ea95fe-6980-32b9-86d5-246447599e49 | -7.3012 | -39.6453 | 2025-08-10 12:20:00 | GOES-19 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 137.1 |
| 4805a4d6-d46a-3ea9-ade3-0edb25e7068e | -7.4373 | -43.9804 | 2025-08-10 12:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 198.5 |
| 5a92f489-9026-38d4-a7de-bb89d5ae13fd | -14.1108 | -45.3844 | 2025-08-10 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 196.3 |
| b56045a9-e975-3533-b71d-6b9c0cce9452 | -7.4373 | -43.9804 | 2025-08-10 12:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 349.5 |
| 3f5f57cf-de7b-3307-875a-8939e2fbd686 | -7.3012 | -39.6453 | 2025-08-10 12:30:00 | GOES-19 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 84.8 |
| 8ec012a1-2b81-34cb-a5c5-d67040d828c9 | -7.437 | -44.0036 | 2025-08-10 12:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 89.8 |
| b0d604cb-462c-398a-b4a5-00956ae905d4 | -14.1103 | -45.4077 | 2025-08-10 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 183.7 |
| a9eb9c91-63e4-3953-8dd2-1ada632c5313 | -8.7822 | -46.4174 | 2025-08-10 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 5dcbcc5c-9ab2-3e58-9fc6-fd781090ee48 | -7.4373 | -43.9804 | 2025-08-10 12:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 304.6 |
| c8751397-1019-3214-9911-6aa3b3a5d268 | -7.3012 | -39.6453 | 2025-08-10 12:40:00 | GOES-19 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 204.0 |
| 05a310df-a67c-3097-9c66-c64051792460 | -14.1108 | -45.3844 | 2025-08-10 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 221.3 |
| 511b2ba0-e0ed-32eb-83a5-32cdab086e6e | -6.5658 | -42.8474 | 2025-08-10 12:40:00 | GOES-19 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 73.5 |
| 4fdad5db-ac80-3f62-be0c-da79a6345a90 | -14.1103 | -45.4077 | 2025-08-10 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 203.0 |
| d8577224-869e-33f9-8150-b4f056fd5f97 | -7.3016 | -39.6203 | 2025-08-10 12:40:00 | GOES-19 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 78.1 |
| f389217a-83b5-3d2e-81e7-be10ac2c4df1 | -7.3012 | -39.6453 | 2025-08-10 12:50:00 | GOES-19 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 165.5 |
| daa492a6-4bf7-3e60-8cd3-b6c593da56a9 | -14.1108 | -45.3844 | 2025-08-10 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 219.5 |
| d10fd5bc-3298-3f1b-9286-53f4a05c7112 | -14.1103 | -45.4077 | 2025-08-10 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 177.5 |
| 6c2db298-14c6-30d7-a940-dfb7fb7583c2 | -7.437 | -44.0036 | 2025-08-10 12:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 8405d9d6-f323-39d0-9cf6-63fec7e1e49f | -7.4373 | -43.9804 | 2025-08-10 12:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 229.8 |
| d05c4f98-9730-30d9-83ce-736a52f5bd30 | -11.747 | -45.0246 | 2025-08-10 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 396acaa4-5863-3147-a555-95b5e78a5436 | -7.3016 | -39.6203 | 2025-08-10 12:50:00 | GOES-19 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 80.2 |
| e1bb1642-b967-3fe5-a020-0d3de44bffcd | -11.7466 | -45.0478 | 2025-08-10 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 0c09f2cf-fc8f-3d29-8e87-7447c88a14e3 | -14.1103 | -45.4077 | 2025-08-10 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 174.2 |
| 69d74845-279f-3a6b-bc5c-312f62289651 | -14.1108 | -45.3844 | 2025-08-10 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 215.8 |
| 18cfa723-d53d-30dc-95c9-93f920362feb | -7.4373 | -43.9804 | 2025-08-10 13:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 148dd2c7-09c4-3ad7-8601-689eb5c1d1e9 | -7.3012 | -39.6453 | 2025-08-10 13:00:00 | GOES-19 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 132.8 |
| aa88a9b7-a956-33d4-86b2-f5b054a76b1e | -8.7822 | -46.4174 | 2025-08-10 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| a70385a7-abb9-30b8-ba22-748a10587400 | -14.1108 | -45.3844 | 2025-08-10 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 204.7 |
| 50db398d-01dc-3046-8829-722016a83585 | -7.3012 | -39.6453 | 2025-08-10 13:10:00 | GOES-19 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 138.7 |
| ee557b89-e1ad-3ef2-9971-abc4a812f48a | -7.4373 | -43.9804 | 2025-08-10 13:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 0c779b79-ca4f-3f8f-b6e8-d23473704d8e | -14.1103 | -45.4077 | 2025-08-10 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 184.4 |
| cc1416fd-e93b-3385-bdd5-1f29d5ee5133 | -14.1108 | -45.3844 | 2025-08-10 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 218.7 |
| 19458aaf-087a-3917-82e1-75336cc427cc | -7.3012 | -39.6453 | 2025-08-10 13:20:00 | GOES-19 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 122.6 |
| d2d4aff0-e359-305c-9b10-ea9ff151f844 | -8.7822 | -46.4174 | 2025-08-10 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 1f1902ab-9c85-34ee-9b1d-856b13a2338a | -7.4373 | -43.9804 | 2025-08-10 13:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 13571ce3-522c-338c-b9bb-19310b32a694 | -7.6017 | -44.4031 | 2025-08-10 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 65526b01-d087-36ef-969e-fdfe34fb4178 | -14.1103 | -45.4077 | 2025-08-10 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 236.8 |
| 08137d6a-ddc5-3140-a982-c957e76c6495 | -6.9411 | -42.9306 | 2025-08-10 13:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 65.1 |
| a2c47d2c-b7e2-381b-a47c-4a6579673f88 | -19.5851 | -47.2323 | 2025-08-10 13:20:00 | GOES-19 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 46e11553-4b16-39d5-bb82-c61e2fe9f2e5 | -8.7822 | -46.4174 | 2025-08-10 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| c81905ee-26b9-3965-86aa-4febd5283795 | -14.1108 | -45.3844 | 2025-08-10 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 274.5 |
| b4ac9b80-c343-3380-b875-948fe326035d | -7.4373 | -43.9804 | 2025-08-10 13:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 3ac53c06-8f1a-3b0e-8d33-7392d0f589d6 | -7.3012 | -39.6453 | 2025-08-10 13:30:00 | GOES-19 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 115.5 |
| c645d6ea-aa80-3968-a369-f67ae5c9f171 | -7.6017 | -44.4031 | 2025-08-10 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 7a073ffd-b65e-35ee-8c83-37560ae292b9 | -14.1103 | -45.4077 | 2025-08-10 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 279.3 |
| 4c38f4a1-4c40-33e8-a76a-bf481371d318 | -6.9411 | -42.9306 | 2025-08-10 13:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 66.0 |
| c807febf-a738-30a1-9748-1d2ca4619d63 | -7.6015 | -44.4262 | 2025-08-10 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 71.3 |
| a97f3a68-8edf-3208-a9ca-8de775feb198 | -7.4373 | -43.9804 | 2025-08-10 13:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 80bdbc22-ef2d-390f-8b1b-ebc65fba6568 | -7.3012 | -39.6453 | 2025-08-10 13:40:00 | GOES-19 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 72.3 |
| 0eb43a87-6547-39e1-aec1-0af58825738d | -7.6015 | -44.4262 | 2025-08-10 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 55.4 |
| ccfcac97-eb0c-3497-a253-878c6af142a1 | -14.1108 | -45.3844 | 2025-08-10 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 255.2 |
| bb730c6e-8ef2-3c4f-9639-b0c710e3716a | -8.7822 | -46.4174 | 2025-08-10 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 90.5 |
| b060700f-c9bb-32e5-beb7-561f79613f33 | -14.1103 | -45.4077 | 2025-08-10 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 243.0 |
| 89afbb8e-c5a5-3edf-9f99-d8d471d0ba69 | -7.6017 | -44.4031 | 2025-08-10 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 14756fdd-d1ef-3e1c-a598-f34963a73601 | -6.9411 | -42.9306 | 2025-08-10 13:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 67.7 |
| 03bdb4ad-2a15-337b-b291-8ee2e29c3aaf | -6.9411 | -42.9306 | 2025-08-10 13:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 66.1 |
| dd5c3504-e90a-39c0-a9d5-4bb0bb3bacba | -10.3483 | -46.6452 | 2025-08-10 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 7d2680ac-f52c-39c0-a337-6cd857884a05 | -10.3677 | -46.6204 | 2025-08-10 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 9286a1ca-4217-39d6-9d01-36f84ad0f96d | -14.1297 | -45.4043 | 2025-08-10 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 126.2 |
| f5de8a7e-abf7-30ab-86ba-8429363b3274 | -8.7634 | -46.4194 | 2025-08-10 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 926568bf-f782-3d53-8b6a-c9e4b5b7c84f | -7.6017 | -44.4031 | 2025-08-10 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 546e2fde-403a-3ab2-b275-defc814848ff | -7.4373 | -43.9804 | 2025-08-10 13:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 6b442b35-aecb-3a11-86cc-8cbe4d5681b8 | -14.1108 | -45.3844 | 2025-08-10 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 239.5 |
| aa75f243-d61a-33c5-9c08-b77b913cb24a | -9.5015 | -46.2725 | 2025-08-10 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 9a44f6f4-6683-3fdc-bc51-d3646ddcf7de | -7.1739 | -43.9824 | 2025-08-10 13:50:00 | GOES-19 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 59.7 |
| d7a3650f-3aca-3afc-980c-890f54d0815a | -6.7865 | -45.0945 | 2025-08-10 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 62.0 |


[Clique aqui para ver as próximas entradas](README32.md)
