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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f4b39bdf-3a9a-3d06-9c85-138e093efaab | -5.53035 | -41.71102 | 2025-10-28 04:12:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e0a54564-f599-3154-afb3-cdac2fed0b64 | -4.19832 | -43.17973 | 2025-10-28 04:12:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 95e7ea14-e349-3d2f-8a89-c6c2c312f5ce | -5.80984 | -40.8111 | 2025-10-28 04:12:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9a7d1b9e-e74a-324d-bc9a-c96d4c39c866 | -5.81041 | -40.8073 | 2025-10-28 04:12:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e16a67bf-c7ca-3b21-8762-0cdbc1b72536 | -6.17162 | -41.67622 | 2025-10-28 04:12:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 94dc6825-5b01-3756-b0c6-aa27915e0535 | -6.10126 | -41.77777 | 2025-10-28 04:12:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c46da4cc-29fe-3248-98e7-82adc1e596f0 | -3.58434 | -43.6208 | 2025-10-28 04:12:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d0087a9d-343e-3084-8230-4b9e77ef2832 | -4.45503 | -43.64599 | 2025-10-28 04:12:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| df1353e9-de17-3409-927d-823e5f072da5 | -6.14641 | -41.81731 | 2025-10-28 04:12:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 507502f3-94dc-3191-91b6-d2210efb0cd7 | 1.04027 | -51.31348 | 2025-10-28 04:12:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 01947f03-14c0-3556-947b-9dee451f57f4 | -3.54986 | -54.69411 | 2025-10-28 04:12:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe928584-a75b-3111-8376-f11f7bff0d30 | -4.87727 | -47.54809 | 2025-10-28 04:12:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c58b7e5e-566e-3ad6-a186-7b777fd90469 | -2.30103 | -47.01261 | 2025-10-28 04:12:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0fc8b530-c584-32d0-b27e-ea1fcd3e90c9 | -4.42682 | -45.90038 | 2025-10-28 04:12:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8868c599-69ea-3169-9416-e1b0e518b0f3 | -5.83065 | -43.49197 | 2025-10-28 04:12:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 94a856d7-f444-33ca-b0bf-e73337cde2eb | -3.28236 | -41.09335 | 2025-10-28 04:12:00 | NOAA-21 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 191f7a81-144f-3fed-a063-7ad7a11bb580 | -5.14197 | -44.96378 | 2025-10-28 04:12:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5caac4c9-cd01-351d-a19c-641b28efd982 | -3.75288 | -50.95618 | 2025-10-28 04:12:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e4f8e03a-657a-30aa-82c3-b7707a7155e4 | -3.02402 | -45.37633 | 2025-10-28 04:12:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 1297a5a2-8cc4-3157-9b2a-50721a4dc78c | -4.45869 | -43.23523 | 2025-10-28 04:12:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 11f7ba49-027d-3c68-9ccf-28f207af208d | -2.75819 | -45.40111 | 2025-10-28 04:12:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 77b0dd7d-74b7-38ee-91e4-65c73fed068a | -4.43045 | -45.90101 | 2025-10-28 04:12:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d7a902a-2869-35f4-a498-22787f5f8ff2 | -1.84084 | -45.29389 | 2025-10-28 04:12:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3b0607b7-8c73-36a2-bab4-554dd15a9a1a | -4.37567 | -49.67056 | 2025-10-28 04:12:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7d1e2d90-d2d0-3d8d-852c-9d0c5ceeba44 | -5.64747 | -41.08881 | 2025-10-28 04:12:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6090b91b-8c19-3598-a9a5-6b19184b9c36 | -3.58379 | -43.60255 | 2025-10-28 04:12:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4cec524b-6206-37fe-810b-b544ee535cfa | -5.8057 | -43.02439 | 2025-10-28 04:12:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7b2a42e9-4eba-3928-8dea-78dad21a3a1c | -6.15045 | -41.68029 | 2025-10-28 04:12:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 15a06179-aab0-3914-adca-ea67633fe398 | -2.75095 | -45.40001 | 2025-10-28 04:12:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 549ed7c2-2d31-30dc-9345-1ea9284c3c54 | -5.663 | -41.13222 | 2025-10-28 04:12:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 37d818e3-5851-3929-bb29-f309da69724d | -4.34408 | -49.88283 | 2025-10-28 04:12:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 098b44e8-1e45-3980-849b-e40b68501906 | -3.57652 | -43.62685 | 2025-10-28 04:12:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 294b4592-e4b1-31ac-9fad-cb0bb048d6ff | -3.23966 | -48.77448 | 2025-10-28 04:12:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 45d8ed1f-b7ba-3c81-86e0-152c79f21520 | -6.08878 | -42.1456 | 2025-10-28 04:12:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9e55e7af-2951-3ef2-9807-90bedaa65c34 | -2.97907 | -48.97152 | 2025-10-28 04:12:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 241ad64c-d4c7-302e-b7c5-91eed1952273 | -2.80519 | -49.14651 | 2025-10-28 04:12:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 91eeded5-d303-37e9-96dc-334359ee4215 | -4.75854 | -46.42539 | 2025-10-28 04:12:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a342dc10-d744-3367-847b-090be99858c3 | -2.82932 | -49.39954 | 2025-10-28 04:12:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 69e28e71-63a3-3497-98cd-f30c7c062b10 | -3.01811 | -45.36695 | 2025-10-28 04:12:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0c9ab5a7-3137-368f-82c0-73b991d06729 | -2.64007 | -47.29878 | 2025-10-28 04:12:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8d41670-82c0-3770-a592-5ba67e29085d | -3.46786 | -49.96687 | 2025-10-28 04:12:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f8506bd1-7625-3575-ab27-f1dbde1347ee | -3.80278 | -51.09974 | 2025-10-28 04:12:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3e49b6e5-e8e9-39cf-bec6-fbdb44c04976 | -4.08238 | -44.42576 | 2025-10-28 04:12:00 | NOAA-21 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b53cc611-5df9-3c53-b844-43a773de2678 | -6.14308 | -41.81678 | 2025-10-28 04:12:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 102cd93f-0bb7-376e-a716-65396742dfb4 | -4.45225 | -43.64196 | 2025-10-28 04:12:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ae523bf7-54dc-3a38-be31-123a7c3471cc | -5.27256 | -44.32328 | 2025-10-28 04:12:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1b1de7fc-e26e-35f0-b294-1289dc750816 | -5.606 | -42.77405 | 2025-10-28 04:12:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8c628cf8-1968-343e-a332-73dc7a852b90 | -2.91922 | -48.72449 | 2025-10-28 04:12:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a589b978-ecf7-3455-b1eb-59bb29bb77a7 | -4.99653 | -48.3451 | 2025-10-28 04:12:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aa7b8950-e786-3107-b8b0-de0f0d02e257 | -6.1355 | -41.71071 | 2025-10-28 04:12:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 0c428e6d-076d-344e-a04b-6065ad4f13f7 | -2.91281 | -49.81538 | 2025-10-28 04:12:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4585a5dd-09c3-343e-b1e2-75f68ab9a21c | -5.25794 | -42.47938 | 2025-10-28 04:12:00 | NOAA-21 | PAU D'ARCO DO PIAUÍ | PIAUÍ | Brasil | 2207793 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8d7e38f7-cc17-3d3a-8625-a7e5c3028c1c | -3.58545 | -43.6355 | 2025-10-28 04:12:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 278a8f06-91bd-307a-936b-cb8eeb102708 | -3.02951 | -45.3766 | 2025-10-28 04:12:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 1a86fc43-b741-3496-b6a3-9e90f5a492a2 | -5.66528 | -41.13999 | 2025-10-28 04:12:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e4b5f65b-b339-3585-b97b-c9ee37a989cd | -2.75029 | -45.40419 | 2025-10-28 04:12:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb907aaa-4eb8-3158-94dd-3d5ca73c7cb8 | -2.74962 | -45.40837 | 2025-10-28 04:12:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| d1e3f0a4-b92f-307a-a801-a9a7573e0a49 | -3.57541 | -43.61216 | 2025-10-28 04:12:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33fc1712-7371-3592-9d52-3bf2bc793e37 | -3.57598 | -43.6086 | 2025-10-28 04:12:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e80aac14-bcb5-3fc3-9290-c38bc2f4ad9d | -3.57429 | -43.61925 | 2025-10-28 04:12:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3b14ec07-5e55-3c09-876e-5b9e83a6d201 | -3.12679 | -50.15289 | 2025-10-28 04:12:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b00bf007-31bc-3990-928d-651168a12306 | -4.47765 | -43.41627 | 2025-10-28 04:12:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e8b1ad69-4d9f-3d63-a29d-9797a42446fb | -6.1288 | -41.70977 | 2025-10-28 04:12:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 938a602c-fc78-3e81-aaca-53508d7c7c90 | -5.43821 | -40.87749 | 2025-10-28 04:12:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 46b63f42-19d7-3e51-8e1c-cbebafb4e585 | -3.13465 | -53.00054 | 2025-10-28 04:12:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c2cd5815-92ac-3021-8c25-d585d1a49f36 | -2.66436 | -47.87077 | 2025-10-28 04:12:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5183cd6f-3f79-3928-9773-5eadf63a5ab3 | -6.11552 | -41.72949 | 2025-10-28 04:12:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 60104383-ff29-3d34-b699-83507f912ed8 | -5.65812 | -39.63337 | 2025-10-28 04:12:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 853ecfe8-35bf-3f00-91f6-9d7041083d6f | -4.7382 | -48.30696 | 2025-10-28 04:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6446a0c-8901-3fb9-9862-bee1be0b1da2 | -5.81442 | -40.82724 | 2025-10-28 04:12:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 46a6f220-4d42-3656-8324-584b90081d36 | -5.46263 | -40.87743 | 2025-10-28 04:12:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6ffed4be-d0cb-3279-bf87-f6f43115351b | -5.49053 | -42.16632 | 2025-10-28 04:12:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| f2e4b7a9-7426-3dc1-82ef-3feb6868cbc2 | -6.13495 | -41.71426 | 2025-10-28 04:12:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 872f11a7-2928-3b2a-8e9e-0fe5edb4776b | -4.92578 | -42.72988 | 2025-10-28 04:12:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ebec4d2c-4008-349f-93ad-b49e5dfbd6bd | -4.51634 | -44.03415 | 2025-10-28 04:12:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b541589a-739d-39c3-9931-c97b7bb66b23 | -3.75341 | -50.95311 | 2025-10-28 04:12:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 32668c76-51cf-32ef-be2f-609f50b9307a | -5.65727 | -41.10159 | 2025-10-28 04:12:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 528c868d-4019-37c9-b283-d54848476834 | -2.41818 | -48.44088 | 2025-10-28 04:12:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dd1f5856-7abc-30e6-871c-a7631090de6f | -5.66015 | -39.63177 | 2025-10-28 04:12:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0d07981f-2e57-352a-a830-5559f72dd4f2 | -4.46255 | -43.23227 | 2025-10-28 04:12:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 86e8431c-c29a-3aa0-a8b5-0b512799a741 | -2.99882 | -51.03949 | 2025-10-28 04:12:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e3a92a5f-e073-3135-84c8-aa6514c02ff6 | -2.43561 | -49.76022 | 2025-10-28 04:12:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 83bff979-07cb-3b75-8d72-6b4ff045e0e8 | -4.50345 | -42.83929 | 2025-10-28 04:12:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 10569a76-1c7e-332e-b886-7def65188c35 | -3.46698 | -49.9721 | 2025-10-28 04:12:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ed56eabe-57d7-3d7d-9bde-ebf2ec9e47b9 | -3.11556 | -51.21206 | 2025-10-28 04:12:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca15a3b8-72a6-3e8b-9e18-0f22770761f4 | -4.50015 | -42.83878 | 2025-10-28 04:12:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b10373ce-a045-3f5e-ba6a-6189a631f5c8 | -3.02106 | -45.37164 | 2025-10-28 04:12:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 59ad8d27-35c2-39ec-b931-eb1c4d8d5569 | -3.86502 | -43.35164 | 2025-10-28 04:12:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9adfb314-77f8-387e-a586-749ce84578b7 | -5.81213 | -40.81914 | 2025-10-28 04:12:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2022449e-8ab0-3401-a411-6abf03c87bec | -6.17388 | -41.68382 | 2025-10-28 04:12:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fdebf8b0-6079-30d7-a472-3a25794a8331 | -2.74829 | -45.41676 | 2025-10-28 04:12:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4c2614dc-9df5-37f6-a4d3-0bf5d83880d7 | -3.77385 | -44.24553 | 2025-10-28 04:12:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 24ebb912-9475-323f-bce7-57ea3fe5fef2 | -5.78337 | -42.96743 | 2025-10-28 04:12:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6bdec233-9d77-3f0a-a5a3-3be9fb3333c4 | -5.69944 | -43.93339 | 2025-10-28 04:12:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a355cfc0-8dfd-37d7-8ae8-a8942c015d35 | -2.29914 | -48.5663 | 2025-10-28 04:12:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a968f67-75be-32e5-9b7b-eeee8e981b43 | -3.36101 | -41.9239 | 2025-10-28 04:12:00 | NOAA-21 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f3b83c5a-1e9e-3546-be08-a00d71f0d22f | -3.42948 | -39.04515 | 2025-10-28 04:12:00 | NOAA-21 | PARACURU | CEARÁ | Brasil | 2310209 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 427cbc80-af33-3c36-a130-1b642829aedc | -4.22649 | -43.19477 | 2025-10-28 04:12:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e8b19b4e-8b92-309e-a253-6b169380b01d | -5.84148 | -43.27006 | 2025-10-28 04:12:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f30544f-cf93-3631-9040-2cbac4c8da19 | -6.11001 | -41.74306 | 2025-10-28 04:12:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |


[Clique aqui para ver as próximas entradas](README17.md)
