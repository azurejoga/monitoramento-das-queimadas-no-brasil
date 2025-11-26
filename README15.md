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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 46316a5b-720a-3ef4-8ce5-80c1a525e354 | -2.50006 | -47.82408 | 2025-11-26 04:21:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 94343943-a371-38dc-b811-84358b32170d | -8.05356 | -43.10813 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 68e0ebaf-3a69-3966-a586-d6fece2481e5 | -4.2578 | -45.11956 | 2025-11-26 04:21:00 | NOAA-20 | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| caaa85db-9d6a-372b-b03a-91181ac20691 | -3.22425 | -50.57314 | 2025-11-26 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de2c5b94-bf6f-3fb7-8196-28b60bf65760 | -4.96387 | -50.8761 | 2025-11-26 04:21:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f82eac60-fe6d-36ba-b60e-e8165cff7ab4 | -3.47445 | -43.43283 | 2025-11-26 04:21:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 517bc3b7-31ae-36e7-8abf-592dc575cad1 | -3.6062 | -40.4384 | 2025-11-26 04:21:00 | NOAA-20 | MERUOCA | CEARÁ | Brasil | 2308203 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 21cadb80-0326-3bfc-9ea2-98abdea718e1 | -6.47786 | -40.79787 | 2025-11-26 04:21:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 552aecc2-0da1-35e0-ae55-42be37b5a2ca | -6.68533 | -43.94476 | 2025-11-26 04:21:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e43cd408-535c-3224-932c-9028dfa51e36 | -3.49125 | -51.21653 | 2025-11-26 04:21:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 652f8d64-b851-38f7-bfe1-b503fdafe729 | -3.70543 | -45.89853 | 2025-11-26 04:21:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2271b546-7f55-3b07-9a71-cc5fb2fa4843 | -3.2335 | -51.17868 | 2025-11-26 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e19c3eb8-bb9a-38d7-a1b0-432c17cee40b | -3.46891 | -43.42487 | 2025-11-26 04:21:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7e469093-b82b-3751-8de7-41ca4086a4d5 | -2.32492 | -46.50978 | 2025-11-26 04:21:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 53799e76-38b2-30cd-9862-5745071477d4 | -3.58272 | -42.36807 | 2025-11-26 04:21:00 | NOAA-20 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 37a09068-4951-3304-a869-adf1ae56befa | -4.17388 | -43.73735 | 2025-11-26 04:21:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 87b7f425-896e-3adc-b885-9d0c126fc38f | -4.14162 | -43.64022 | 2025-11-26 04:21:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1ea7f250-a31a-3dec-9a65-1afccaf5006b | -3.90541 | -47.74997 | 2025-11-26 04:21:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f30ec54d-9711-36b3-9a62-67c7bd12b2ba | -4.03172 | -49.10205 | 2025-11-26 04:21:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 17568221-2ac2-3c8e-92f7-a181204fb04d | -4.0348 | -46.78025 | 2025-11-26 04:21:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42019e45-e05d-3b4a-81ca-039ec49d9cba | -6.76648 | -46.51788 | 2025-11-26 04:21:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0c781f41-830e-3551-9d0e-5d80c8dfe71e | -2.71104 | -45.69132 | 2025-11-26 04:21:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| cdd96604-77aa-32dc-9053-481c421786fb | -4.17102 | -49.88077 | 2025-11-26 04:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 75d7e0bb-78d3-3012-a942-2e9bf2f82bec | -5.283 | -43.64029 | 2025-11-26 04:21:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| af9296a8-eff7-3943-a802-bde4ddf84666 | -4.82034 | -43.81758 | 2025-11-26 04:21:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 64436c4c-e7a6-3cd5-b46c-b39cbe4ad669 | -6.04655 | -45.83932 | 2025-11-26 04:21:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 09a68f8a-f7eb-3129-a67b-478c406485f9 | -8.54107 | -40.21379 | 2025-11-26 04:21:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 91392855-b203-37fd-893d-0bb9893b67ad | -6.0669 | -43.25001 | 2025-11-26 04:21:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c6b3f935-8bd0-3465-a8cc-50d3c303b33c | -4.30423 | -50.74429 | 2025-11-26 04:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d5e8527-6e27-3f0d-829c-8d103007b44d | -4.41261 | -43.49356 | 2025-11-26 04:21:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8609c04f-4f9b-3ae1-ab78-dbc54329ee56 | -5.75452 | -45.11092 | 2025-11-26 04:21:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 110e9ad4-aedb-30f0-aca5-fd6111956887 | -4.29814 | -48.60107 | 2025-11-26 04:21:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 807d45a3-659f-321a-9bad-ee77474531cd | -6.10551 | -42.95507 | 2025-11-26 04:21:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 501b690b-cd34-322c-a755-1125c3b487d2 | -5.17491 | -47.10304 | 2025-11-26 04:21:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 3b716d8c-d678-37a4-8b72-63a0f44df6ea | -3.58977 | -40.98278 | 2025-11-26 04:21:00 | NOAA-20 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2b3a14a6-8aee-3d24-b7d6-5df90751abea | -3.22141 | -50.59087 | 2025-11-26 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7d85b521-0745-3d9f-bd18-1068ea033720 | -4.53659 | -45.56759 | 2025-11-26 04:21:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| df1416c8-e064-3a86-bc5c-69cd0408e5e4 | -6.31008 | -43.78238 | 2025-11-26 04:21:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b39dcb4-b65e-3ba6-acb8-35e849399ee0 | -3.53253 | -53.25834 | 2025-11-26 04:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 15341b82-46b2-3414-b693-c5e3862fbc20 | -3.9624 | -49.03713 | 2025-11-26 04:21:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4937187a-b565-3719-a2b7-149b96cfb790 | -6.35402 | -46.05616 | 2025-11-26 04:21:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 53c30e58-8870-3235-9c86-72db1caecb72 | -8.06441 | -43.12897 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 438eb324-7665-326a-8aaa-fbf17abf8f18 | -4.7708 | -46.42762 | 2025-11-26 04:21:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 88ae53dc-88e2-39cb-a590-cd2128a3f4e7 | -4.56036 | -50.45677 | 2025-11-26 04:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c609036c-6191-3be3-9147-8c00f2187e93 | -6.58165 | -47.9058 | 2025-11-26 04:21:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c48cc03b-8231-34d5-9005-abf1acd8d3dd | -4.56461 | -43.80212 | 2025-11-26 04:21:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0add505d-2d25-3ba8-82ef-4fa35a1a5748 | -8.05184 | -43.11938 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 19.6 |
| 9c2bddb2-2c4f-3b49-b08b-30f2f68da219 | -4.61666 | -41.06278 | 2025-11-26 04:21:00 | NOAA-20 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 52d96971-8111-3e90-a3d5-8220104261eb | -3.35889 | -50.48728 | 2025-11-26 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6dfe9162-f979-31c8-9706-1bb61bcfcaa7 | -4.16834 | -43.72941 | 2025-11-26 04:21:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 6089e900-a8e4-3fdc-976f-464971b38d0c | -2.87744 | -51.78276 | 2025-11-26 04:21:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 65e698a4-9ef0-3fa4-ab3b-dabbbc5de035 | -3.02814 | -51.09329 | 2025-11-26 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a819c65-00b6-306d-923b-768b005c2cc8 | -4.83851 | -38.61229 | 2025-11-26 04:21:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3ffbffee-6f63-3c18-a435-469b57882338 | -2.73065 | -49.46167 | 2025-11-26 04:21:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e2783f30-ccd7-3a5e-b57a-363ee13954cf | -8.03984 | -43.10601 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3f008624-c9d4-37a4-9b50-b69ab0ea6a41 | -5.71534 | -39.50299 | 2025-11-26 04:21:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1d734ab1-1d55-3f6d-8397-be0de7954427 | -6.06187 | -43.26028 | 2025-11-26 04:21:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c741ef13-e159-37f6-a0f3-af8f368989c3 | -5.38852 | -50.49122 | 2025-11-26 04:21:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 70679387-3b1c-3ca4-923e-b02ac51e2237 | -7.16635 | -44.99203 | 2025-11-26 04:21:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9e4a16cd-ab92-3551-89b9-f1dd07664c47 | -7.55973 | -45.87495 | 2025-11-26 04:21:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fe2279f1-4e33-3608-8a15-cd8e76b1ee5b | -8.54228 | -40.21288 | 2025-11-26 04:21:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 0ffe66bd-00b3-3772-90cd-89416f3f34c1 | -6.57512 | -47.90049 | 2025-11-26 04:21:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9de0b855-574c-3270-b460-6595706ba22d | -3.51779 | -50.2375 | 2025-11-26 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 13c02b9e-8e73-3e36-9cc1-202a7ee9732f | -8.05641 | -43.1354 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 8439b1a2-8dea-35f9-8e94-4359a4dea54e | -2.47985 | -47.82737 | 2025-11-26 04:21:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66c12f6c-6c30-3abe-8707-5b5dcfe43abd | -4.70533 | -43.98727 | 2025-11-26 04:21:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| cdc4b35e-0331-3eb8-9929-4b33e9dc2b60 | -5.05887 | -44.15951 | 2025-11-26 04:21:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0a10dce5-0411-3710-b4df-50c671f1b240 | -4.65126 | -43.96468 | 2025-11-26 04:21:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a487d2a4-cdad-3a7a-8f0d-e66182205d3c | -6.75284 | -44.20969 | 2025-11-26 04:21:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6cb26649-29bf-384a-bf81-d23a062a59f7 | -8.06443 | -43.10596 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 142defc3-5167-3e14-898f-019f0cb1497b | -8.03984 | -43.12903 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| bd6621ad-5790-3980-bdf5-aadf5ddfeb97 | -3.4394 | -50.19162 | 2025-11-26 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 55e57737-aa13-3325-98d5-17d8954d6212 | -4.45549 | -47.61681 | 2025-11-26 04:21:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be4a528a-5309-3533-9ce1-5b2b71bfbd10 | -4.1628 | -43.72146 | 2025-11-26 04:21:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 87db9001-3c2b-3d00-b1cb-bb61bd8c6ebf | -4.17828 | -43.73096 | 2025-11-26 04:21:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 6268b7b5-2a2c-3344-ae0a-11871ab9118f | -3.02279 | -51.03788 | 2025-11-26 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 16d943cd-ee82-375b-ade7-f07094805d4d | -4.71593 | -46.46562 | 2025-11-26 04:21:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0646c423-048a-3cb9-bed3-ba18be6c9930 | -6.22343 | -43.36227 | 2025-11-26 04:21:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 20ee1ddb-1527-3958-9621-7b6c3eba3505 | -3.39019 | -47.18504 | 2025-11-26 04:21:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7cedaa0f-c486-3fc8-bf76-accf4951d282 | -3.94927 | -49.96508 | 2025-11-26 04:21:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dcbd141b-d37e-304a-922f-a56698216ad6 | -4.55607 | -43.29387 | 2025-11-26 04:21:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3339b536-fb43-3094-9dad-1210568dc171 | -4.25613 | -45.13004 | 2025-11-26 04:21:00 | NOAA-20 | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 244ad265-da7c-35e0-803c-ebc32b260699 | -6.80576 | -41.72252 | 2025-11-26 04:21:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 57a47ed5-08d9-3f0d-987b-d1388514ff99 | -7.18391 | -45.50292 | 2025-11-26 04:21:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ea7cf7bb-9aa4-329a-ab1c-ab128bacaec4 | -3.39312 | -47.18975 | 2025-11-26 04:21:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 1c08a790-5836-3694-b44e-bfaa20f1f0ad | -5.57762 | -46.27759 | 2025-11-26 04:21:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ab719de4-60d6-358c-96b6-258a83d047d7 | -2.6035 | -49.44513 | 2025-11-26 04:21:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 14d5bc54-53e5-3897-8694-ac94d1ce7e4e | -3.65839 | -44.8285 | 2025-11-26 04:21:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7b9f220b-231e-3335-bb02-8394841d73cf | -4.09178 | -50.20417 | 2025-11-26 04:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dc5d4974-7ba7-3436-b6d4-c57813f8df7a | -2.28572 | -47.04306 | 2025-11-26 04:21:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2e59873-d8e8-38d0-ad94-c56342b7c436 | -2.90514 | -45.4841 | 2025-11-26 04:21:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b99b3801-9d14-3988-936e-27e455983268 | -4.08846 | -48.73442 | 2025-11-26 04:21:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d117458-a2f0-3e97-8178-341babce9bbb | -4.74592 | -46.55873 | 2025-11-26 04:21:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fb2c7b53-7122-39b0-8914-eac161d3cda8 | -2.93095 | -48.23251 | 2025-11-26 04:21:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 355e5b17-876e-3400-93e5-c4fa5d8523c7 | -5.23181 | -45.42758 | 2025-11-26 04:21:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4dd275e1-0967-32c8-82b3-4f3a794376f8 | -4.67334 | -49.38402 | 2025-11-26 04:21:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4a61c879-ef90-3e6b-be17-64800b65bc93 | -6.76308 | -46.51733 | 2025-11-26 04:21:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 70f8b208-8df5-3f3b-b1d6-f545a0f5c7ca | -3.71426 | -42.78728 | 2025-11-26 04:21:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b1a94af7-3811-3ff3-a80f-dce2215d8f53 | -4.64221 | -45.22321 | 2025-11-26 04:21:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bbdb09f9-b6ff-326b-ad03-59ef7d41566b | -4.65956 | -43.97659 | 2025-11-26 04:21:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README16.md)
