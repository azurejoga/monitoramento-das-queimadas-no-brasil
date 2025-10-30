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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0014e619-b4c0-3be6-bade-e4a9fc84758e | -8.25949 | -43.92788 | 2025-10-30 03:36:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 49deadd5-8819-39a1-976d-06b9c3f2b844 | -6.96992 | -39.11143 | 2025-10-30 03:36:00 | NOAA-21 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a3bce861-bb4b-3187-90c9-1f2d32476475 | -7.61284 | -43.57341 | 2025-10-30 03:36:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6adaed06-3262-3164-b7ce-af4eb09ec374 | -6.01693 | -41.97298 | 2025-10-30 03:36:00 | NOAA-21 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| aa78b7e7-0cee-3351-8e09-646c8627de03 | -11.17517 | -45.21506 | 2025-10-30 03:36:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| da12fcf6-d34d-3083-86c7-d324aaf4440f | -8.22686 | -39.54186 | 2025-10-30 03:36:00 | NOAA-21 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ece9a0ba-1e8f-3f7c-884e-95f20d4b88f4 | -11.03529 | -47.83907 | 2025-10-30 03:36:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2e99cbc8-ae04-3f98-82ad-20ce12e8eb00 | -8.70353 | -47.91001 | 2025-10-30 03:36:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| bcf237d5-4c4f-3b2e-a4d8-7795702d7610 | -6.69461 | -38.19652 | 2025-10-30 03:36:00 | NOAA-21 | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 012e66e7-1423-371d-be08-c82fdb25071a | -7.62185 | -43.5867 | 2025-10-30 03:36:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1f532267-f37c-3735-b0a6-1f35c00b0d78 | -8.70578 | -47.91388 | 2025-10-30 03:36:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a9172639-17fc-3242-b644-d519b95ee53d | -7.62742 | -43.58754 | 2025-10-30 03:36:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5cbd26cb-7a09-3801-96f1-e9ff2c200546 | -5.43192 | -45.33774 | 2025-10-30 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 4dfc1aa1-a5ee-3316-9fb8-c0dabf70be7f | -5.432 | -45.3449 | 2025-10-30 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 2964145b-977e-3fc6-b416-87ff41f7f051 | -5.41134 | -46.01768 | 2025-10-30 03:36:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f161f6fc-71f2-3091-acc8-338afd08e2cd | -6.21208 | -41.82241 | 2025-10-30 03:36:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e1206fb2-3af2-35cd-8aef-3037e90cd56f | -10.4949 | -43.32741 | 2025-10-30 03:36:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a171a91f-b0b4-38cb-8662-80cd9abed314 | -6.1571 | -41.66492 | 2025-10-30 03:36:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2e23079d-9d34-3503-8cad-0efce1e8ecbf | -11.04833 | -47.84431 | 2025-10-30 03:36:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 58b25e0f-a404-3c50-8a41-a5c83edd79f2 | -6.17285 | -41.60318 | 2025-10-30 03:36:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b49d2442-9801-3f3a-b43a-8a6afe89f72e | -7.37802 | -42.45431 | 2025-10-30 03:36:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ff5d1915-49ac-3325-a169-0554c020f828 | -6.13008 | -41.70199 | 2025-10-30 03:36:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| fce75956-f72d-3b46-87ca-e5718b5304c4 | -7.32468 | -42.47643 | 2025-10-30 03:36:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 767ac54f-d497-3749-87ca-c3ffcc40bb04 | -7.95934 | -46.72729 | 2025-10-30 03:36:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6d873669-51ea-32f8-96f2-e5485415dc59 | -6.91591 | -42.24923 | 2025-10-30 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 4b38a74c-0723-3010-a151-88d7d7a86d6c | -6.53405 | -43.56776 | 2025-10-30 03:36:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 32d6bc6f-4b02-364a-86e1-59c80a519c17 | -5.84411 | -45.54049 | 2025-10-30 03:36:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e7c4cd29-0dd0-33dc-8c35-f7996d3d3004 | -7.87393 | -44.23687 | 2025-10-30 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eb569dc1-8886-3d04-b326-3651fe4db714 | -7.09979 | -39.57485 | 2025-10-30 03:36:00 | NOAA-21 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7691e8eb-a152-3d6b-bf6c-589a9437bf6f | -7.86818 | -44.23584 | 2025-10-30 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 941ae103-6b0c-3941-b282-df983f1c2094 | -6.13666 | -41.69378 | 2025-10-30 03:36:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c6fc4806-da57-3bd5-b6e5-d2551d1b0253 | -9.89442 | -44.88137 | 2025-10-30 03:36:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 88cdb6d4-c46e-3bc6-8f5f-bd2907379374 | -6.92056 | -42.25287 | 2025-10-30 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| d6bd5d9d-69ed-335e-ab29-63049975b01b | -7.03326 | -39.47643 | 2025-10-30 03:36:00 | NOAA-21 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 76c5f12a-f447-365e-a05b-418ec8b3814c | -7.61418 | -43.56612 | 2025-10-30 03:36:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6324976f-215e-32fa-913b-b9ebaa49b8db | -7.32987 | -42.47725 | 2025-10-30 03:36:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 4ad25ce2-0a95-36c7-9865-2e41862c84f9 | -6.15305 | -41.59912 | 2025-10-30 03:36:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| a586af8c-0436-31d7-a8e5-9f233b6aa5f7 | -7.07471 | -44.94147 | 2025-10-30 03:36:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 2c968632-e906-3276-a9ee-810439d2af7e | -11.11716 | -42.26008 | 2025-10-30 03:36:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8765cc76-f841-36fc-8380-913bf379b5c2 | -7.08085 | -44.94232 | 2025-10-30 03:36:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 91dec95e-01c1-3ee0-9100-ab1c82292c41 | -6.119 | -41.70626 | 2025-10-30 03:36:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 360817a2-67fa-3e5a-ae96-35aac54c2be7 | -10.76744 | -47.8854 | 2025-10-30 03:36:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 165a89fd-424d-329b-a831-4968825b024b | -10.76896 | -47.88273 | 2025-10-30 03:36:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ecf0120d-d0fc-3529-af85-3ad6c7715e72 | -7.52241 | -42.85378 | 2025-10-30 03:36:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bf412534-7ed4-3312-8af3-cf6082dba5bd | -7.47278 | -38.5576 | 2025-10-30 03:36:00 | NOAA-21 | CONCEIÇÃO | PARAÍBA | Brasil | 2504405 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9da52966-151f-3242-aefd-61839abf71e6 | -10.88263 | -45.07993 | 2025-10-30 03:36:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| cd03752b-0a40-3fee-9c1c-afbb0e2e1c08 | -7.95796 | -46.7169 | 2025-10-30 03:36:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4411b0ba-5f97-3c54-a990-ae246488eb08 | -6.01078 | -41.97814 | 2025-10-30 03:36:00 | NOAA-21 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1e9b6897-3611-3d5b-bfb1-aadc9ff038e1 | -11.54879 | -44.68343 | 2025-10-30 03:36:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 81446e05-bc50-3b3b-af80-c661c7ca4ee7 | -6.05688 | -44.15872 | 2025-10-30 03:36:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d51e1db1-8aad-3eeb-bd3e-7fd4fd9b5e3e | -7.38383 | -47.62722 | 2025-10-30 03:36:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| d41a0c29-8ffb-3ba0-8b06-0014b8e734db | -6.14018 | -41.67349 | 2025-10-30 03:36:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 6234251b-2339-3371-bf86-396bf010aa53 | -7.32246 | -42.48903 | 2025-10-30 03:36:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| efdc8c30-fbee-3a21-8062-a8a1d41eca83 | -7.86891 | -44.23183 | 2025-10-30 03:36:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 76d22d3c-550a-36df-8f02-fe58efdf70ae | -7.95675 | -45.43945 | 2025-10-30 03:36:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 27848d26-6abc-375a-844a-09a67a88e4a5 | -9.98232 | -37.04303 | 2025-10-30 03:36:00 | NOAA-21 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| f1592975-45d3-3262-a9fb-16e61184f742 | -11.04183 | -47.8416 | 2025-10-30 03:36:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f93284cf-3621-3cce-902b-f70fcb4d9916 | -7.79376 | -46.41452 | 2025-10-30 03:36:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1a47c48f-6eca-3741-a48b-806e67f51b94 | -7.29848 | -45.66689 | 2025-10-30 03:36:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d287bcb1-df10-387e-acf4-d8228236b534 | -6.46476 | -41.64427 | 2025-10-30 03:36:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c6ae583b-eca7-3d3a-a73b-6ab1b6258580 | -10.85874 | -47.61666 | 2025-10-30 03:36:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b31d41f5-cf79-33b7-a928-399a4443255a | -7.08169 | -44.93774 | 2025-10-30 03:36:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 826a01f8-d9e9-382b-bd7f-6d7f46511c7b | -9.88861 | -44.88036 | 2025-10-30 03:36:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 45ec6ef9-38e9-366f-8e43-4291d934623c | -9.26413 | -46.2655 | 2025-10-30 03:36:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d3e10d5c-659c-36e6-8fe0-a696bf5a4526 | -7.00098 | -42.28978 | 2025-10-30 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 25adc140-294b-3ae6-954c-b765287bc1eb | -5.72843 | -44.40417 | 2025-10-30 03:36:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5b353de0-d461-36a9-9207-6939023e49f0 | -9.81267 | -47.58311 | 2025-10-30 03:36:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 60244856-4d36-30e2-b69e-7c4765c914ba | -9.84561 | -44.88545 | 2025-10-30 03:36:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ddb3fc32-5c95-3dc9-bb20-26230e998f29 | -6.11013 | -42.4356 | 2025-10-30 03:36:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 0a6c1f8f-5046-3570-aaf2-72c2b1401919 | -6.10899 | -42.4421 | 2025-10-30 03:36:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 7342cc4d-527c-394d-8088-779ef0dfdd4e | -6.12453 | -41.70419 | 2025-10-30 03:36:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 3fb83f10-f9af-3351-948a-12daf66364a4 | -6.12537 | -42.44162 | 2025-10-30 03:36:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 7cb74809-379e-39dd-81b8-a9f05d2689e9 | -6.9693 | -39.1151 | 2025-10-30 03:36:00 | NOAA-21 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0de91da1-ad64-3721-9e35-9763798b1ded | -7.95455 | -46.73491 | 2025-10-30 03:36:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 92fa6089-3632-3511-98fd-298a3688a957 | -7.58328 | -43.64805 | 2025-10-30 03:36:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 19e6d5b2-9fd7-392c-8b57-c743c0e45821 | -6.85787 | -42.14236 | 2025-10-30 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| bd188f07-657e-30de-a9ae-7ccc997c425b | -6.95106 | -40.91158 | 2025-10-30 03:36:00 | NOAA-21 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c7309d3d-09b0-3a26-99b8-a49aaa55fbbd | -7.79084 | -46.42109 | 2025-10-30 03:36:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ee6194e5-47af-3593-a73c-6f6e6bba8783 | -7.78969 | -46.42694 | 2025-10-30 03:36:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1f78e70b-bf0e-3392-98c0-b7d8c377ac42 | -6.13913 | -41.59078 | 2025-10-30 03:36:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| caa3cd5d-525a-3d68-8e0c-26f146402807 | -9.81397 | -47.57654 | 2025-10-30 03:36:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a374e382-e6df-33c4-89e9-3adcb15da58f | -9.91172 | -47.90852 | 2025-10-30 03:36:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| cd2809de-e4c8-372c-9537-5f3f986512f6 | -7.95815 | -46.73337 | 2025-10-30 03:36:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a20f0efa-246d-3fdd-9e07-4cff1407fbbc | -7.7861 | -46.41898 | 2025-10-30 03:36:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cafcf78a-b0dd-351c-af4f-a665d5642574 | -6.11808 | -41.71157 | 2025-10-30 03:36:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 370532fa-81ef-33f1-9086-201248fefc70 | -7.32302 | -42.48589 | 2025-10-30 03:36:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 1ebd1eff-72ac-3ba5-a41f-fb56d1cebdb3 | -10.26956 | -44.5818 | 2025-10-30 03:36:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 00b554ae-1cdb-3708-9ec3-31735e297b0b | -7.95574 | -46.74564 | 2025-10-30 03:36:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| b2c39dab-d91c-3217-afad-485b4feca12f | -6.1099 | -41.7288 | 2025-10-30 03:36:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 50473a3a-deb3-3ba2-9ccb-5dcdecb681d2 | -7.33177 | -38.85396 | 2025-10-30 03:36:00 | NOAA-21 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 315958de-ab18-34da-8ce3-9c390cf6bb40 | -6.31298 | -42.10677 | 2025-10-30 03:36:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5e440124-a13a-3560-8baf-abfaaef52278 | -6.12327 | -41.86124 | 2025-10-30 03:36:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 112313d4-312c-39cf-840c-5f02bbef82b6 | -6.10372 | -42.44119 | 2025-10-30 03:36:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| ae92befb-2873-3f63-893d-706c1bbace8d | -6.02735 | -44.32561 | 2025-10-30 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 438e865d-7d13-38ef-a7a5-45edebb504fb | -6.99582 | -39.13465 | 2025-10-30 03:36:00 | NOAA-21 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 99a20f5c-a16e-3bc5-8fcf-27b10ce4cf08 | -7.9693 | -45.44083 | 2025-10-30 03:36:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 66e1f3ce-ce35-3424-9231-4f792c621490 | -6.1289 | -41.85887 | 2025-10-30 03:36:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 5a34fc01-d1eb-3629-91a9-171cd9f3618b | -6.14341 | -41.71446 | 2025-10-30 03:36:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| cd7b2fe1-a42c-3bf0-94e5-705b3bc85cf6 | -11.16687 | -45.22705 | 2025-10-30 03:36:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7788c003-6f08-3c18-ac5d-1398def95158 | -11.17426 | -45.21978 | 2025-10-30 03:36:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README15.md)
