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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e5f04c3a-d8c1-32c2-874a-108f199b59dc | -6.8834 | -45.64354 | 2025-09-13 03:45:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 725e42dd-a567-3d57-9429-122ade2e54c8 | -6.59569 | -44.30874 | 2025-09-13 03:45:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4cbf4e5a-b9af-3a7a-afd3-9343c0519a81 | -6.87775 | -45.64174 | 2025-09-13 03:45:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 56dd8c5a-0c80-3e43-b434-ff6d9572259a | -4.831 | -42.85046 | 2025-09-13 03:45:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 54c6be5f-78cc-3242-bbb4-1323cc570f2c | -5.65684 | -42.61145 | 2025-09-13 03:45:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d9fac691-c60d-3338-810b-b6519b15f251 | -4.94347 | -37.93554 | 2025-09-13 03:45:00 | NPP-375D | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d317f5db-5926-3aca-b41a-d59d119b602e | -6.39424 | -45.6522 | 2025-09-13 03:45:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| eb30160f-6c87-3e0e-bdce-0a623673ca41 | -5.65293 | -42.6054 | 2025-09-13 03:45:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4aac09bf-1edf-3e76-8d05-b2778fedfad9 | -3.23455 | -46.7837 | 2025-09-13 03:45:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 8107ac36-dfc3-3527-a561-144d9cd8273c | -6.18331 | -41.1187 | 2025-09-13 03:45:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 97c2e593-dd42-3d5b-9bf9-1536dd3f027d | -1.97546 | -47.98761 | 2025-09-13 03:45:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 90499670-6a05-356a-9bc6-36d513ce0d54 | -6.51126 | -43.93346 | 2025-09-13 03:45:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8f4bb020-22d9-3169-9163-15ab7a1e3143 | -7.2195 | -43.97498 | 2025-09-13 03:45:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6376eae1-585a-3a04-8286-eea4dc7826b6 | -3.2197 | -47.63938 | 2025-09-13 03:45:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 838f7868-50eb-3864-96ee-58b5d32c458c | -6.5061 | -43.80386 | 2025-09-13 03:45:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e8d8a839-ff0d-3939-9f13-1562f4a90336 | -4.92425 | -47.8727 | 2025-09-13 03:45:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b1fb105-79b1-306a-9f03-f5fe45f2d2b1 | -6.72107 | -44.02414 | 2025-09-13 03:45:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| be51ff86-951b-3a07-89bd-f195b98519c3 | -3.22085 | -47.63277 | 2025-09-13 03:45:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| b6ba7715-58ae-34f3-97da-a7aca0949f86 | -3.23213 | -47.12818 | 2025-09-13 03:45:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 306978ce-dc0e-326a-bc88-18a1c36142cd | -6.53471 | -41.35488 | 2025-09-13 03:45:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| be29ff69-8c02-331b-a8a1-46fbed001e68 | -6.5107 | -43.93662 | 2025-09-13 03:45:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 19e0c14b-57d7-3624-aaca-4557972cba9c | -6.91456 | -38.25309 | 2025-09-13 03:45:00 | NPP-375D | NAZAREZINHO | PARAÍBA | Brasil | 2510006 | 25 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 27c81988-14ac-36d7-91bb-678670de137e | -5.4947 | -42.67935 | 2025-09-13 03:45:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 25ba2f27-f725-316f-9477-fec46aae9301 | -6.69437 | -44.14392 | 2025-09-13 03:45:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dba560ca-1cd5-3e43-a556-9585c12de261 | -7.31217 | -43.93147 | 2025-09-13 03:45:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a140364c-cca3-3761-be21-995002fc2e1c | -7.33075 | -34.80079 | 2025-09-13 03:45:00 | NPP-375D | CONDE | PARAÍBA | Brasil | 2504603 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0cf5f880-5315-3ca1-b99d-29a71734e715 | -7.07857 | -44.12927 | 2025-09-13 03:45:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f575969a-fc8a-30bd-ab42-3609ec68cb3d | -3.22542 | -47.12708 | 2025-09-13 03:45:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 35393487-8861-367f-a58a-87e9ee7dfb68 | -6.99079 | -43.80606 | 2025-09-13 03:45:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0c9d3948-ceb7-3513-9a2b-24e509b2e979 | -3.79501 | -47.58279 | 2025-09-13 03:45:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0ba10f64-744f-39d2-8539-e637d8f121a9 | -6.69497 | -44.14053 | 2025-09-13 03:45:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 692a3ef4-5a17-365f-b6fb-33b6b48ed94d | -6.17487 | -41.14251 | 2025-09-13 03:45:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 699d04fe-44da-34db-9205-ce2300992e4f | -7.21566 | -43.84026 | 2025-09-13 03:45:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 59908049-ab91-32ee-a9fc-45ad03f68419 | -6.10562 | -45.95137 | 2025-09-13 03:45:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1346a1d1-f9b8-34ce-9780-b7d52c37e25c | -6.77273 | -41.59748 | 2025-09-13 03:45:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3c6c188e-181a-350e-a4e6-27d2d66deabc | -3.23358 | -46.78927 | 2025-09-13 03:45:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 5117bbff-4d09-351e-89d7-f8bcc765749a | -3.22196 | -47.62633 | 2025-09-13 03:45:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 91716884-4910-3953-86a7-c9a9fea42e28 | -3.23919 | -46.79598 | 2025-09-13 03:45:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| d70c7b9e-b3be-3482-94c4-b3d323e98fbb | -3.22212 | -47.13359 | 2025-09-13 03:45:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 73f99a48-b998-3ff2-9e39-c44f0b24e4ff | -6.10724 | -45.94257 | 2025-09-13 03:45:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f58ec20a-e938-31b8-ac5b-f2f42c0d9853 | -6.11066 | -45.94296 | 2025-09-13 03:45:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 345f6d8e-38bc-3b36-8517-7aa11e243098 | -5.645 | -45.94923 | 2025-09-13 03:45:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3c5886f8-68b8-3a57-b110-4e42d65970a4 | -4.92539 | -47.86627 | 2025-09-13 03:45:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8cf8ba1c-c4b2-3873-930b-8275c6e47f7d | -6.14069 | -43.36622 | 2025-09-13 03:45:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f9295027-2d88-39d3-9ebf-5256915c44de | -6.5072 | -43.80656 | 2025-09-13 03:45:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 670b6c25-6b46-3418-8f9c-f3fa52053c39 | -3.23107 | -47.13416 | 2025-09-13 03:45:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 84faea53-123c-3b1e-ba19-30631b2a8a73 | -6.39492 | -45.64835 | 2025-09-13 03:45:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8a081a10-936d-37f6-8b0c-7927fe7abb29 | -8.02798 | -39.59092 | 2025-09-13 03:45:00 | NPP-375D | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 98f19ac5-4cb9-34ec-9493-286ca4d2156b | -7.31883 | -43.92363 | 2025-09-13 03:45:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eeed086a-6038-3636-8eca-45687be9796a | -6.2911 | -44.24046 | 2025-09-13 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8794014b-3ab7-33a3-bc2c-3460b482eeea | -6.78949 | -43.40568 | 2025-09-13 03:45:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 6473c222-6ac2-3864-85c1-0b5ee11c602f | -7.54592 | -42.64692 | 2025-09-13 03:45:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c82102d2-a841-3e91-ac10-6219b7abaa22 | -3.72084 | -38.63103 | 2025-09-13 03:45:00 | NPP-375D | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1b8558d4-547e-35df-a1f4-9acd12c09524 | -3.22887 | -47.62754 | 2025-09-13 03:45:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 864f1121-222e-3d2e-9fef-5724819b0a46 | -5.64579 | -45.94483 | 2025-09-13 03:45:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7bc6764a-95fc-3288-93cd-6948d968f313 | -5.7981 | -42.47334 | 2025-09-13 03:45:00 | NPP-375D | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| cad65773-b362-30bf-acbe-bb5bfd3110a6 | -6.87701 | -45.64585 | 2025-09-13 03:45:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bbaa6001-d177-36ca-b577-94b39750c35c | -5.47798 | -37.53545 | 2025-09-13 03:45:00 | NPP-375D | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4fbe112f-e561-3128-ba21-34098a403665 | -6.10317 | -45.95052 | 2025-09-13 03:45:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 53fe4750-ebf4-3965-afaf-50e9e953dacb | -4.64991 | -47.55604 | 2025-09-13 03:45:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f7cf5be3-b3db-3b66-a3b0-a545a1074866 | -4.34289 | -38.76958 | 2025-09-13 03:45:00 | NPP-375D | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8f627e33-8991-312c-85e6-4390b776fb6d | -1.97669 | -47.98037 | 2025-09-13 03:45:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5ad8470d-c81c-3e79-8aa9-7c9628eccf4a | -6.50553 | -43.8072 | 2025-09-13 03:45:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 49f913fd-ab0e-396a-bcf9-e50508273f5b | -5.20556 | -44.3153 | 2025-09-13 03:45:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 83cf225d-c762-38b8-8f9f-3b84665516e6 | -4.54864 | -43.7321 | 2025-09-13 03:45:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a65a1000-056e-394b-bcf5-2f0d14f2f8e1 | -6.85071 | -45.65905 | 2025-09-13 03:45:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4ef67a63-a6f1-3a05-9bc8-bc4c7070fada | -6.87848 | -45.63773 | 2025-09-13 03:45:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c98abeed-d27a-315e-9654-41198a8a7d31 | -5.25247 | -45.5802 | 2025-09-13 03:45:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c535f572-65e9-35d7-a686-0976b562002a | -6.46653 | -46.03677 | 2025-09-13 03:45:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fdb0a59e-3cbe-3f83-b9ae-8ce95807c9b9 | -6.31531 | -44.58574 | 2025-09-13 03:45:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fbc3caf2-d8b9-3943-92cb-1aa12f6c3882 | -3.24112 | -46.78485 | 2025-09-13 03:45:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| ccf49b38-357b-34bd-ac68-26838570a0e1 | -4.83071 | -42.85128 | 2025-09-13 03:45:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 241bbf34-7fb5-3a15-9222-9667c1367ea5 | -4.91735 | -47.87189 | 2025-09-13 03:45:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8a58ad0e-da63-3d39-83db-f20a50123b6a | -6.20442 | -42.70028 | 2025-09-13 03:45:00 | NPP-375D | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 7e271fa2-c885-3b72-a737-49ee99c60c48 | -6.47254 | -46.03762 | 2025-09-13 03:45:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2773e7b5-7c40-3d89-8622-ed7f00fb9be2 | -3.24015 | -46.79043 | 2025-09-13 03:45:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 55e3bd24-7cbf-3dfb-8472-0c4575e75a35 | -3.22775 | -47.63402 | 2025-09-13 03:45:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| cf5533a5-e4d9-3f20-95fd-069c56fd5b9a | -6.619 | -44.08328 | 2025-09-13 03:45:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9c1dc5ab-cc08-3048-bad6-7c511031427d | -6.69304 | -44.12099 | 2025-09-13 03:45:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a184df09-c484-3e75-be03-83edf5354841 | -6.77092 | -41.59948 | 2025-09-13 03:45:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4b1cc320-e707-3ec6-9a56-ef4e1a6ba8b2 | -6.1742 | -42.75993 | 2025-09-13 03:45:00 | NPP-375D | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 3e0c801f-6154-3c4b-a748-fb37ee19058f | -6.17764 | -41.12605 | 2025-09-13 03:45:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c875343a-63cf-3834-ac07-9412495cdf54 | -6.76757 | -41.60113 | 2025-09-13 03:45:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 00289f8f-0538-39ef-b54f-54a8742de622 | -6.16988 | -41.14574 | 2025-09-13 03:45:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e41fa387-1950-37b9-bd90-cd2af0d29f6d | -2.87251 | -41.74545 | 2025-09-13 03:45:00 | NPP-375D | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e7a50cc4-0b30-3f12-a707-ec6914640750 | -5.75618 | -39.12889 | 2025-09-13 03:45:00 | NPP-375D | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d5e61fc1-e6e2-32c2-980a-e293d825dfec | -18.16286 | -49.19271 | 2025-09-13 03:47:00 | NPP-375D | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| fc6ef283-5e92-3b8f-bf57-26c2d404f840 | -11.21194 | -41.59805 | 2025-09-13 03:47:00 | NPP-375D | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| dcabfcf5-54ee-33c1-9715-f48c5a51b40f | -14.22218 | -46.27427 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 1e78aa61-be8d-3178-81f9-96bd77ca38b2 | -12.9373 | -47.97855 | 2025-09-13 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| caa98c55-b156-3d53-a72b-f4462d3a3422 | -14.22718 | -43.51053 | 2025-09-13 03:47:00 | NPP-375D | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 951e4938-ae71-38f6-8233-94f07e746ee3 | -17.2945 | -48.74668 | 2025-09-13 03:47:00 | NPP-375D | SANTA CRUZ DE GOIÁS | GOIÁS | Brasil | 5219209 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9c8f7aad-4c67-35ea-9eec-d68a9fd7e13a | -17.28503 | -46.10859 | 2025-09-13 03:47:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 27d297b9-ad17-3336-a2e0-248482082aa8 | -14.20171 | -46.24778 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 0847bde4-e0ec-386a-a1f8-f6a0e4c38db3 | -7.55745 | -42.66412 | 2025-09-13 03:47:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 79140e22-48ed-3037-bcb8-b91de23c3eb4 | -16.64589 | -49.77261 | 2025-09-13 03:47:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6e891d3d-5d89-34d6-9f1b-4d6c3842275c | -11.40668 | -50.74356 | 2025-09-13 03:47:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b44ed9ee-5910-3d07-bff1-3e59cee27a1f | -17.33004 | -46.66759 | 2025-09-13 03:47:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cc5cec28-d7f1-3175-8cbc-3395cadabb01 | -11.83278 | -50.57243 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| a68ee3a7-25e9-312d-9fd7-fe638a11b1d8 | -11.86336 | -50.59096 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |


[Clique aqui para ver as próximas entradas](README23.md)
