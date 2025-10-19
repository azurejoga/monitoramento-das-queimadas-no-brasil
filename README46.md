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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6d310df6-35f7-3464-86b8-f8c6531aa92f | -11.80013 | -49.32493 | 2025-10-19 04:32:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2293265a-934d-3476-919e-ee2b55ecdc3e | -4.8842 | -48.305 | 2025-10-19 04:32:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e042eb57-f9a0-3250-b57d-d6f7ddbd5633 | -7.45085 | -47.13253 | 2025-10-19 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 36c5ffef-0019-3345-b092-290bc54edd43 | -9.22157 | -46.06541 | 2025-10-19 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3892aad4-9123-3deb-8501-49dc0a05c80a | -7.31659 | -42.47067 | 2025-10-19 04:32:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 0424cd66-7190-343a-9653-8d96134ebe39 | -10.88547 | -46.08785 | 2025-10-19 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3ca7d5ba-d09c-3390-a627-061566114098 | -11.62483 | -44.0863 | 2025-10-19 04:32:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f43924da-87e9-3d27-a0f9-b9be9ea0852c | -6.17882 | -46.3165 | 2025-10-19 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc844b31-a99f-36cd-8f6e-9599ccb7c359 | -9.09963 | -48.91445 | 2025-10-19 04:32:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ec46f2ef-7a7d-34b7-8159-1e7bcca87523 | -9.68715 | -48.93774 | 2025-10-19 04:32:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a67d4cf2-5b52-3638-9697-1acdd4663f6e | -9.67857 | -44.55702 | 2025-10-19 04:32:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 99a47b22-76e1-38b7-ac76-bc0e533182e6 | -5.62909 | -49.06244 | 2025-10-19 04:32:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f7f71216-0505-3c97-9425-29d6c1c610ba | -9.70021 | -44.59261 | 2025-10-19 04:32:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9bb67126-e77d-3611-aff6-e1dba07f4da7 | -8.24986 | -43.99385 | 2025-10-19 04:32:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 465540ed-682e-3661-937a-90d51b1f2c21 | -11.60934 | -44.05254 | 2025-10-19 04:32:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| df880e63-3d88-3808-aff5-4f664c95b4ef | -6.01904 | -41.92017 | 2025-10-19 04:32:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bedef719-e953-3975-9e70-414006a11e8d | -7.92591 | -49.99986 | 2025-10-19 04:32:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0ac19996-6d36-39c8-b479-f6e5743e54c8 | -5.95191 | -42.23177 | 2025-10-19 04:32:00 | NOAA-20 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6230dc50-1525-3b15-8761-105c0078d2e0 | -5.19642 | -46.13364 | 2025-10-19 04:32:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e7a1bd5-b147-3c03-9872-a27b45adc909 | -8.34676 | -46.22162 | 2025-10-19 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a5f4dd42-a9c2-373a-bcb7-17bc3a1f2779 | -6.36101 | -45.74519 | 2025-10-19 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 876614dd-736e-3b62-9a72-2d9a27e9e250 | -8.7003 | -47.06718 | 2025-10-19 04:32:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cbd1378e-2f70-341c-b71e-e3ef11353447 | -8.1258 | -46.50016 | 2025-10-19 04:32:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ea6f55ba-e02b-383b-ac73-5357d839783f | -11.78153 | -47.55123 | 2025-10-19 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5b4ebec8-576e-3069-bb97-6d8432b6fc81 | -11.62878 | -44.08689 | 2025-10-19 04:32:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| befe63e1-ec17-3686-8329-5bc872c05c29 | -9.6222 | -49.13218 | 2025-10-19 04:32:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f4010876-e779-3897-a200-bc15a130c609 | -4.83483 | -48.08287 | 2025-10-19 04:32:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6876343d-925d-37f8-962a-59d87833a90b | -8.07805 | -47.09739 | 2025-10-19 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8406f82c-ea84-3e8b-8dca-645d304d8470 | -9.30336 | -44.47717 | 2025-10-19 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0a1ac3d8-7685-3dcb-a20c-320ebbcd0a59 | -6.47432 | -47.01557 | 2025-10-19 04:32:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e2efcb58-974c-3700-94d2-4c149c1cb47e | -9.92155 | -47.66393 | 2025-10-19 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3e9544a4-ed93-3947-aa41-a13e804d90e1 | -7.18587 | -42.17772 | 2025-10-19 04:32:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 641e42dc-03e0-3f9b-890d-edc2602dbd5d | -6.35718 | -44.25153 | 2025-10-19 04:32:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 34306b68-e43c-3779-8b02-2af8f73de740 | -5.36496 | -45.27492 | 2025-10-19 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 91ed9094-f77b-3d3e-aa3a-0ad256c7386a | -10.53336 | -47.76756 | 2025-10-19 04:32:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fbcc8511-b4b5-3920-8f20-45d4a875d909 | -9.76659 | -47.87343 | 2025-10-19 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 080c98cc-8f05-32e4-a412-dc67a03e181c | -5.15345 | -46.16695 | 2025-10-19 04:32:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a63a4264-9757-3d60-ada9-44c80a1feaa5 | -5.18386 | -49.92622 | 2025-10-19 04:32:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 239a057b-bfa5-3401-9252-47d0d34e0f39 | -9.90659 | -45.95924 | 2025-10-19 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bbc1973f-a15a-36e0-9231-26ba1a9aa7fb | -4.73986 | -48.63476 | 2025-10-19 04:32:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc4d8d2e-bf75-3c6c-bcfe-e1dd29b5c4b7 | -5.72221 | -49.09536 | 2025-10-19 04:32:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 562fb936-d5f2-3a38-bda4-2f4ed4680672 | -12.14749 | -45.083 | 2025-10-19 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dc6c85fa-884d-32a4-9c9e-b7b06c9dcc76 | -9.23136 | -46.07085 | 2025-10-19 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 89f5c8ab-bae9-309e-a70b-e4bf4d45273e | -7.08368 | -46.87411 | 2025-10-19 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5e3a9a59-7e1a-3fe9-be20-69a4b6e1019c | -9.18396 | -61.38963 | 2025-10-19 04:32:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 6e67da12-40fc-3462-9731-1c95b528b54e | -8.20082 | -43.9579 | 2025-10-19 04:32:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 24b5bc2b-226f-3361-a42b-78246ce10f58 | -6.35536 | -46.36566 | 2025-10-19 04:32:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 01cfa9b8-0e0e-3f8b-873d-c2391785a983 | -10.55854 | -45.15904 | 2025-10-19 04:32:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3d487dff-d2ca-3bcd-a124-93c51b195507 | -6.60632 | -48.05439 | 2025-10-19 04:32:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 45babd07-8d1e-34dd-8037-0bf1c5d5ef48 | -8.69026 | -47.06561 | 2025-10-19 04:32:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 778b632c-bef2-3084-87a2-bf92fcf7ed77 | -5.33835 | -44.71365 | 2025-10-19 04:32:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 933190e5-3339-35a8-b929-530dc309ca60 | -7.59276 | -46.07011 | 2025-10-19 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e87c2f43-ead1-3796-82da-ff01b3d0141a | -9.45807 | -49.7487 | 2025-10-19 04:32:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d85a178e-1a29-3ba0-b13b-489ce02924a1 | -10.1262 | -44.53165 | 2025-10-19 04:32:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7332371e-33bf-3c2b-9866-51c602c8a55f | -6.08573 | -46.45919 | 2025-10-19 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4223bdc2-e8aa-3170-9fc3-74825308062e | -6.27812 | -44.57464 | 2025-10-19 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6b082199-0920-369f-a0eb-8bdc9f0d58a1 | -5.49828 | -45.86647 | 2025-10-19 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a20fd6b7-63b7-3bbb-ba5a-478f5c2b9907 | -12.68959 | -46.9599 | 2025-10-19 04:32:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4893e294-59fb-37fe-a02c-34943edc07aa | -6.78968 | -46.4692 | 2025-10-19 04:32:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1fdb9314-5e09-3d0b-9ae8-a0f24a40cfd0 | -7.05767 | -44.2375 | 2025-10-19 04:32:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 34eae7bf-d71c-3f1c-ba81-ed7e4902e3c0 | -4.48828 | -50.55774 | 2025-10-19 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7cd3e49f-6c2d-38fe-85e0-53415d55a60b | -7.19678 | -42.19112 | 2025-10-19 04:32:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 96d7b963-2188-358b-9b95-7b8e52e4930e | -12.18729 | -45.09887 | 2025-10-19 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7805f592-8166-3553-9df3-252a66ceba36 | -5.34204 | -46.06387 | 2025-10-19 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b63d31e-b41b-3ee4-b4ab-de1870d940cd | -5.36441 | -44.94284 | 2025-10-19 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 94222434-4f90-3130-aacd-4286f53f11ef | -5.13235 | -48.39146 | 2025-10-19 04:32:00 | NOAA-20 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4aa1da58-ab5b-3674-8693-faa3ef9238b2 | -5.31101 | -44.84666 | 2025-10-19 04:32:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7a25d93a-7972-3a0b-9ca9-7ab8c0d65033 | -8.60173 | -45.43515 | 2025-10-19 04:32:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 137f38ce-6fe5-37b4-8fd4-ccce587f9084 | -8.06362 | -47.10234 | 2025-10-19 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0ae1da45-f891-3f80-9bea-243639f1d06e | -10.12555 | -44.53618 | 2025-10-19 04:32:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 547eca6e-34c3-385f-99dc-1da0bbaed89f | -10.13063 | -44.52755 | 2025-10-19 04:32:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d51d39d8-3620-3464-9685-53923775a369 | -9.78968 | -44.95324 | 2025-10-19 04:32:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 26d8e817-93c0-3164-94dd-a4e5f85c52c0 | -5.35961 | -47.21295 | 2025-10-19 04:32:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 23f71f73-0939-3c60-a96b-c478a2382b85 | -11.41676 | -41.42329 | 2025-10-19 04:32:00 | NOAA-20 | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 54100b11-641b-38f8-92bf-53be363119e4 | -9.8822 | -49.12077 | 2025-10-19 04:32:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ed1a1228-9ab0-317b-b094-048443d643ec | -5.46682 | -44.88904 | 2025-10-19 04:32:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 750976f0-a243-3b1d-82ef-c035fb414750 | -10.15021 | -44.52542 | 2025-10-19 04:32:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9bdef65b-7c2e-3819-abf4-fba6439193f6 | -9.67704 | -44.55939 | 2025-10-19 04:32:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 134e08a8-a7c1-34be-b02a-d7a173272c71 | -5.93066 | -45.44783 | 2025-10-19 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5172b3a6-2502-3221-bdb1-3e2fdfd75b34 | -5.89656 | -47.23413 | 2025-10-19 04:32:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 82fbf602-41a8-39bf-8b83-60ebae9e1f6d | -6.2227 | -44.6501 | 2025-10-19 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b24ef051-4629-345c-83ba-f678b99b3976 | -5.12283 | -49.67577 | 2025-10-19 04:32:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 08cbc799-d24f-34e5-ba8f-fdc03fba7e88 | -7.01502 | -41.81112 | 2025-10-19 04:32:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2c4d98eb-293e-3d4d-8fb8-80ec2457c55c | -5.7163 | -43.81719 | 2025-10-19 04:32:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 661d37f3-24eb-34d1-a448-2784049484a1 | -5.1501 | -46.16643 | 2025-10-19 04:32:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 32e61785-8996-3b28-8060-889d10de2027 | -11.14218 | -47.71747 | 2025-10-19 04:32:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fff8108d-b4e5-36b9-aa46-1014e2dfd24e | -7.41025 | -44.80316 | 2025-10-19 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 8906c461-031e-3f4a-bc18-81d77e13cb3c | -5.36291 | -47.21346 | 2025-10-19 04:32:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| c6bf1387-6452-30db-a1e6-d6c8e422ffb9 | -10.6099 | -49.52131 | 2025-10-19 04:32:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f36a0c2-e2b6-3877-ba16-c1a934f7c2f0 | -6.25823 | -42.68675 | 2025-10-19 04:32:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9686d484-a775-3cf9-aa0c-a599b208ac73 | -5.13569 | -48.39199 | 2025-10-19 04:32:00 | NOAA-20 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 005d90f2-d2f7-39df-9baf-cde9c61e190e | -10.74223 | -47.29418 | 2025-10-19 04:32:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4a48a4d4-e551-35d3-a4fa-e00cff46557e | -6.35754 | -45.74504 | 2025-10-19 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1020e323-5b68-388b-94f4-5dddc0f604cf | -10.88839 | -46.09243 | 2025-10-19 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 1e39b689-eb4d-3a36-8891-ae927a05c0cf | -7.31765 | -42.46327 | 2025-10-19 04:32:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d80a62ba-7a64-3168-bcfd-99d3c91098e3 | -7.768 | -42.48113 | 2025-10-19 04:32:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 217083a2-084b-38ce-a27f-789396d6fb45 | -8.2453 | -43.99593 | 2025-10-19 04:32:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| adaf12d0-2d47-3bb8-86c7-1b4de51a8f09 | -4.76173 | -50.69703 | 2025-10-19 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e4c0306e-4d17-3986-a890-e0f691eeb04d | -6.49241 | -46.59434 | 2025-10-19 04:32:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7fea1520-079f-3d9b-9d69-cd34b3748af2 | -6.00091 | -44.18457 | 2025-10-19 04:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README47.md)
