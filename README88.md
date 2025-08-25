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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8f604357-a2ad-392b-aaf6-ed3d57a0364a | -14.42616 | -56.46483 | 2025-08-25 05:57:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 123ced33-f496-3997-893c-2f325143768b | -15.13601 | -59.59645 | 2025-08-25 05:57:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| eb4bb48b-b2af-337a-a6f2-0375c18fb147 | -6.03295 | -43.99627 | 2025-08-25 05:57:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 1b387bca-194b-38aa-915b-7d82e646497d | -5.09973 | -43.21162 | 2025-08-25 05:57:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 8e48d0fb-ef94-3233-8b2d-d071c00281c4 | -14.24053 | -58.62155 | 2025-08-25 05:57:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a97c8bac-0121-3865-bf9c-61aaa861fa68 | -14.25759 | -58.61892 | 2025-08-25 05:57:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a2c2c738-d340-3a78-a712-f222d1463a39 | -14.23428 | -58.62074 | 2025-08-25 05:57:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 371a4d37-dbf1-3669-bfd6-19265fad628b | -14.28709 | -60.36944 | 2025-08-25 05:57:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e001b5d-f02a-3c9b-b2ca-937e1541c580 | -14.29045 | -58.60783 | 2025-08-25 05:57:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2612cfaf-49f1-3a34-86ef-6467513679d7 | -14.28759 | -60.36517 | 2025-08-25 05:57:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 508c6a21-ea3e-3ec7-a579-097ce67fb3d5 | -14.25358 | -58.6181 | 2025-08-25 05:57:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ce9785a5-f287-39a3-a7b9-e054354c9ebf | -6.67949 | -44.41573 | 2025-08-25 05:57:00 | AQUA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 4cb429b7-13fc-3e21-b8a8-39f6b112f950 | -5.1016 | -43.19823 | 2025-08-25 05:57:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 41.3 |
| 19a2d05e-947b-3d52-b2d4-bba44014a6b5 | -14.20825 | -58.62716 | 2025-08-25 05:57:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d7d85947-ee0f-336c-aeae-cae0d0c8d70f | -14.29102 | -60.36835 | 2025-08-25 05:57:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b0d0d3b-41d4-37d0-aeb3-73bd71b46eb1 | -14.28114 | -60.37168 | 2025-08-25 05:57:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f4fbf472-3285-379b-bd9e-3d6598958158 | -14.64756 | -56.56318 | 2025-08-25 05:57:00 | NOAA-21 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 21ba1329-b875-3f39-8746-09daee37a621 | -3.4349 | -49.04969 | 2025-08-25 05:57:00 | AQUA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 024c511e-7360-3d30-8cb7-7b0ea5756885 | -14.24678 | -58.62236 | 2025-08-25 05:57:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a3a5a29e-4134-3db2-b591-9764a1147e2a | -14.23374 | -58.62575 | 2025-08-25 05:57:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c359b31f-df98-35a8-8d1b-75734434f121 | -7.50218 | -45.83319 | 2025-08-25 05:57:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 7d156d3e-85ab-3bbf-83ba-7726eed1553f | -7.46385 | -45.01941 | 2025-08-25 05:57:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 4139656f-3f7e-30ed-a208-b5c61540d3a4 | -15.13947 | -59.59723 | 2025-08-25 05:57:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 67e07dce-e9f8-3c26-b4ca-29be3e488c32 | -3.42567 | -49.04831 | 2025-08-25 05:57:00 | AQUA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 8323e84e-71f4-3d28-bdd2-3f1bc30d7e7e | -15.15278 | -59.58529 | 2025-08-25 05:57:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 14d82ff7-a5c3-3171-98fe-125c1d70d276 | -14.65392 | -56.5715 | 2025-08-25 05:57:00 | NOAA-21 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 70d928fd-5fcc-30bf-bc3e-e0af89fbde5b | -5.11045 | -43.21296 | 2025-08-25 05:57:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 470c7480-898c-3e34-b44a-7309cee3f5af | -15.13993 | -59.59277 | 2025-08-25 05:57:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| b0cfdc2e-c9cf-3a47-a49b-cf4363f5950d | -14.27346 | -58.6104 | 2025-08-25 05:57:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ab1e4f1-d81a-3098-b7f1-ab34bdd73599 | -14.24733 | -58.61731 | 2025-08-25 05:57:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 76661e87-d475-3fbb-8e0a-dfeb4f91c4bd | -15.13651 | -59.592 | 2025-08-25 05:57:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 24d7018a-f17c-34d2-8461-6878095dd5c6 | -3.45619 | -43.33904 | 2025-08-25 05:57:00 | AQUA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 3377dd54-8b5c-3714-8a91-f7e3bb048bcb | -14.28506 | -60.37078 | 2025-08-25 05:57:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ef75119-da28-3dbb-902d-c524c0a6869b | -15.14246 | -59.59272 | 2025-08-25 05:57:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0515b04f-2c9a-3bc3-90e2-7a38c6e7e08f | -15.13701 | -59.58753 | 2025-08-25 05:57:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 24d579de-307f-3da4-8429-e399e37f6a34 | -15.14296 | -59.58825 | 2025-08-25 05:57:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 6f6e2d7e-9a86-3923-a23d-ff1ca70b1732 | -14.64702 | -56.56862 | 2025-08-25 05:57:00 | NOAA-21 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 97d63e58-7fa1-3213-8a9d-1782e754116d | -6.52401 | -44.42898 | 2025-08-25 05:57:00 | AQUA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| ff30d971-a72f-3d6a-aeef-b3f49676a338 | -14.26664 | -58.61467 | 2025-08-25 05:57:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 989089c3-5821-3e06-9e69-8cdb5562caf4 | -14.2729 | -58.61547 | 2025-08-25 05:57:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 251939e8-feec-3757-a322-52e79477eb90 | -15.1404 | -59.58829 | 2025-08-25 05:57:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| e1a460ad-48d8-303a-bd64-fab0b81ea760 | -13.42418 | -46.9067 | 2025-08-25 05:59:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| a6e389d5-e7f2-33e9-8f4d-14a81ceaf0c5 | -14.38551 | -51.94649 | 2025-08-25 05:59:00 | AQUA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 11.7 |
| bbb3404e-6163-3edc-8348-289da1506402 | -13.50807 | -46.89282 | 2025-08-25 05:59:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| a8ba2eab-f7a4-3a70-b6a8-bded79ec5cc2 | -14.42815 | -56.46827 | 2025-08-25 05:59:00 | AQUA_M-M | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 56bb3e56-d36a-38e6-95ca-430a077176e7 | -8.05375 | -49.68142 | 2025-08-25 05:59:00 | AQUA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 8b692877-5c3a-37b8-a358-69c15f706a66 | -7.61787 | -45.23022 | 2025-08-25 05:59:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 7c2e04db-73f2-36b1-bf93-43000711860a | -15.64746 | -52.72327 | 2025-08-25 05:59:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 2e80e4db-5910-3daf-8057-820cfdf6911a | -13.61625 | -48.15422 | 2025-08-25 05:59:00 | AQUA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a5ff1a55-0fff-37d6-bfd1-a08ab9b1c233 | -8.06137 | -49.69228 | 2025-08-25 05:59:00 | AQUA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 6936c289-5591-3c53-8cac-6579deda2f4d | -11.60611 | -46.34637 | 2025-08-25 05:59:00 | AQUA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| ed4ded60-af27-3cfd-b2f1-fee873ec7fac | -12.74616 | -48.10429 | 2025-08-25 05:59:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 57124a6d-2d97-3db2-bb27-bf92a9427105 | -11.19713 | -48.46479 | 2025-08-25 05:59:00 | AQUA_M-M | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 29bf2f12-35f7-30f8-ae01-6ccdd12afb14 | -15.17776 | -48.1949 | 2025-08-25 05:59:00 | AQUA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| cb7399b5-3524-357a-a4b1-393e14d13445 | -8.54034 | -48.86193 | 2025-08-25 05:59:00 | AQUA_M-M | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b04cc6f8-82dd-30a9-a0dd-f8f80a175505 | -8.06285 | -49.68271 | 2025-08-25 05:59:00 | AQUA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 866e92e8-eecd-3839-ab42-c59e68072ffe | -10.0259 | -51.07522 | 2025-08-25 05:59:00 | AQUA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 63d6e16a-994c-3537-9c09-c43c8e9d034e | -13.42562 | -46.89633 | 2025-08-25 05:59:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 6b7fe729-7d6a-334b-a7b7-d0f8a5ad5ea8 | -13.38924 | -51.80921 | 2025-08-25 05:59:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 0f20fbd4-2886-32f1-9200-b4340452ae38 | -13.45955 | -46.99582 | 2025-08-25 05:59:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 0acee7b1-d6e8-3a6f-aa54-49340a6425c8 | -15.1764 | -48.20443 | 2025-08-25 05:59:00 | AQUA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| c3901993-2ff9-3f73-8e95-4baa9d6137ee | -13.50664 | -46.90316 | 2025-08-25 05:59:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 14fdd7a7-1b33-373b-890b-ebe9f2c1ebe2 | -14.50619 | -51.92536 | 2025-08-25 05:59:00 | AQUA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 11.2 |
| ad214772-b648-3a67-973c-7b08fc0c0fc2 | -12.74479 | -48.1136 | 2025-08-25 05:59:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| fe0328f8-c532-3bc9-998f-712ef3e2331a | -8.05229 | -49.6909 | 2025-08-25 05:59:00 | AQUA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 32.9 |
| 125eda68-460a-31eb-b33f-00174d5fd7f9 | -12.74076 | -48.14103 | 2025-08-25 05:59:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 39.4 |
| b77fba72-9e12-3520-9cc2-c1387df7b52e | -12.74967 | -48.1423 | 2025-08-25 05:59:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| ef6676a4-87c1-3a2a-bfb7-004c58e7edfc | -11.26495 | -44.98194 | 2025-08-25 05:59:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 1dea18f8-3411-3b2f-b651-fc1377783418 | -13.39091 | -51.79871 | 2025-08-25 05:59:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 0bc01d3a-1f12-3285-8092-474a65bc6f83 | -13.42727 | -47.02161 | 2025-08-25 05:59:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 1ec74339-2eb4-3ab9-b797-9702ded1a361 | -12.75366 | -48.11506 | 2025-08-25 05:59:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 4343bc1d-8ec4-3c22-866e-e7d409cd4e51 | -12.29613 | -49.14181 | 2025-08-25 05:59:00 | AQUA_M-M | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 6a347098-eeb9-3546-a3d0-d63759f106d2 | -13.43503 | -46.89772 | 2025-08-25 05:59:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 5d5dd1c2-e790-337c-b911-d15357ca35c0 | -8.28428 | -47.23652 | 2025-08-25 05:59:00 | AQUA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a271c26a-704c-3ac7-95b8-321435b41b76 | -8.05521 | -49.67202 | 2025-08-25 05:59:00 | AQUA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 0433072d-cb64-321a-9ceb-b298c0b01734 | -13.4581 | -47.00599 | 2025-08-25 05:59:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 57431d1b-a515-324c-a1b7-214e72e889bd | -10.47007 | -48.32411 | 2025-08-25 05:59:00 | AQUA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| d756959d-ac74-3821-b40b-078f4b140711 | -12.75235 | -48.12405 | 2025-08-25 05:59:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7d8d201e-7224-376b-ae95-c8578f31fe08 | -12.74209 | -48.13195 | 2025-08-25 05:59:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7aae19ab-2184-3fca-9b17-6ce122cae490 | -7.54117 | -46.01949 | 2025-08-25 05:59:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f32facd8-8d75-3844-8b6a-e52ca361dac9 | -13.61357 | -48.17273 | 2025-08-25 05:59:00 | AQUA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 80bd3767-2f70-3212-825e-ad99ba498fdb | -11.60464 | -46.35678 | 2025-08-25 05:59:00 | AQUA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| bf4f926b-175c-3a51-8a7f-6e7ae8364e0d | -13.44744 | -46.87756 | 2025-08-25 05:59:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| f9645ad5-137a-3a06-91c9-ae0ae5d337b0 | -13.43658 | -46.88647 | 2025-08-25 05:59:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 36742b90-51c9-34fc-a45d-16b10dad427d | -11.13795 | -46.3337 | 2025-08-25 05:59:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 1c0aaf84-2e81-3661-82e8-f703c1434927 | -10.59858 | -44.32322 | 2025-08-25 05:59:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 4a452611-a62d-35c1-a117-7c77a6b1597d | -14.26003 | -48.03809 | 2025-08-25 05:59:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| a00a5f00-a189-3705-a8e5-8236ff2b5b53 | -10.71105 | -48.3091 | 2025-08-25 05:59:00 | AQUA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 555b10ec-8232-3f35-9a10-0a054361c91f | -9.68163 | -48.33179 | 2025-08-25 05:59:00 | AQUA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 5e4067db-0da0-3232-bcee-dbcf8c784325 | -8.10707 | -47.12455 | 2025-08-25 05:59:00 | AQUA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 7aa48886-6b41-317e-9d01-04be7d5b8f1e | -13.50523 | -46.91335 | 2025-08-25 05:59:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9824cdfd-40c3-307a-ad12-11f5b311e1bb | -9.1722 | -59.4629 | 2025-08-25 06:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 050c9353-5a7b-3294-9cd4-d78b3d0191e5 | -8.8734 | -62.4495 | 2025-08-25 06:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 119.8 |
| e9a78843-34a1-314a-aeff-a94b280eac09 | -8.9689 | -65.4198 | 2025-08-25 06:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 494a551e-17a7-3bc7-91a6-66be318493d6 | -6.8413 | -58.9552 | 2025-08-25 06:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 9196484c-c3b5-3b54-9248-29558e6ddb5d | -9.0971 | -65.7332 | 2025-08-25 06:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 34.4 |
| eb6dc399-84ce-3ee3-99e8-6348f372061d | -9.006 | -65.4 | 2025-08-25 06:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.4 |
| fccfa7b2-de30-3f81-83bd-bd5ac602e8bc | -8.9875 | -65.4006 | 2025-08-25 06:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| ce74d4fe-cfe8-3fca-bb37-833a793c4b92 | -7.9077 | -63.073 | 2025-08-25 06:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 343.8 |
| 027c8372-3902-3eac-8b7d-c5bd28c81bf1 | -8.8918 | -62.4677 | 2025-08-25 06:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 68.6 |


[Clique aqui para ver as próximas entradas](README89.md)
