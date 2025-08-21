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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3dbf4923-80f8-3436-95fa-a872c23d7386 | -2.69676 | -48.21214 | 2025-08-21 04:14:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7f320522-c7c0-3dd3-97c1-71e814af0999 | -2.92602 | -48.23783 | 2025-08-21 04:14:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e81b7598-5dfc-3835-a73f-7629ba86d303 | -5.04717 | -43.05769 | 2025-08-21 04:14:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1a93b600-f3ba-3713-bf14-2bf239d96e62 | -5.38992 | -41.23659 | 2025-08-21 04:14:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2910b921-063b-38b1-8510-03e3bd928c35 | -5.04385 | -43.05717 | 2025-08-21 04:14:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 007805ff-750e-3c08-b8ca-a34d94d6874b | -4.65036 | -41.40919 | 2025-08-21 04:14:00 | NPP-375D | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 82d3d585-5c97-31a1-86e4-b0689e57230b | -3.81993 | -41.56908 | 2025-08-21 04:14:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9b6bf46a-991f-3aa8-9517-3d20b8e6d574 | -3.98628 | -42.5105 | 2025-08-21 04:14:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ed1e7ec9-9c5a-3975-9a0b-eebea1855f26 | -3.98461 | -43.24729 | 2025-08-21 04:14:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1855ee87-20e6-3d18-9ec5-b4dda07027f5 | -4.31151 | -48.09903 | 2025-08-21 04:14:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 27c60120-2c8c-3f07-b46c-54ee0db0d5af | -2.38446 | -47.66013 | 2025-08-21 04:14:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8f69cc91-6e6a-389b-bf50-d6cc3f8b8307 | -3.04114 | -49.44053 | 2025-08-21 04:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b5206199-e8a6-31da-9fe9-a7dc95e3760e | -2.2923 | -47.99096 | 2025-08-21 04:14:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b84566b0-6772-31a3-986e-e29421645737 | -5.11074 | -42.93282 | 2025-08-21 04:14:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fa946ed2-f2ae-3aac-a51b-134617cd0a84 | -5.41045 | -42.36253 | 2025-08-21 04:14:00 | NPP-375D | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8b86ce3b-1a10-3bbc-af56-f012c1da3a57 | -3.35757 | -42.87285 | 2025-08-21 04:14:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| db270af8-2d9f-38cd-9035-4f331edd9ecf | -4.64811 | -41.40154 | 2025-08-21 04:14:00 | NPP-375D | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0b5b1664-3f3f-3406-bd8d-d1179aa00f07 | -3.24209 | -39.52901 | 2025-08-21 04:14:00 | NPP-375D | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d7ac89d3-f4d5-395e-b748-0d4c50d2bbae | -3.98683 | -42.50704 | 2025-08-21 04:14:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1acbe227-adc9-3d40-a03e-a654cdc2e84e | -3.98127 | -43.24677 | 2025-08-21 04:14:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b7425d40-f30f-3eaf-b225-a32975efb47c | -2.30416 | -48.14391 | 2025-08-21 04:14:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1fe0e97b-99b8-3266-a1e3-3d889c5e1eb4 | -2.37664 | -47.65494 | 2025-08-21 04:14:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3536c1cd-e348-3430-9a98-e150a5929142 | -5.1672 | -37.98042 | 2025-08-21 04:14:00 | NPP-375D | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e2814310-bc9d-3150-b3e7-8358fc9b9427 | -2.62167 | -46.84395 | 2025-08-21 04:14:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 70d81d7f-70c3-35c4-a336-cc4e74b441de | -3.81659 | -41.56856 | 2025-08-21 04:14:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 53d08340-c78e-3916-b8ee-a6083348d182 | -3.67343 | -40.35373 | 2025-08-21 04:14:00 | NPP-375D | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f2d717e7-a0a7-3664-92b2-d79668f3c754 | -4.16847 | -48.58061 | 2025-08-21 04:14:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1c3babad-1897-3991-bd11-a255306d5830 | -5.411 | -42.35906 | 2025-08-21 04:14:00 | NPP-375D | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3e73c159-eb75-37ac-934a-f51df0677c0e | -5.10491 | -43.16295 | 2025-08-21 04:14:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7d271405-63ba-3a6b-b3bd-8b160b598a4d | -4.17098 | -42.02659 | 2025-08-21 04:14:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| dc8fc489-d812-32ec-8c6c-74ac4e4b25e0 | -4.64362 | -41.40822 | 2025-08-21 04:14:00 | NPP-375D | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c2e8e408-67ba-33f3-b520-745431151b2c | -5.12104 | -43.21185 | 2025-08-21 04:14:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8f8978af-7217-33e8-adb7-bb4bce98bbc4 | -4.17431 | -42.02711 | 2025-08-21 04:14:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| b94fc6b3-47f4-35d0-a188-9f4afdd5d94f | -4.65013 | -43.12674 | 2025-08-21 04:14:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 577f4096-3c61-3344-ab1b-ef7bbb1f3577 | -3.87859 | -50.97977 | 2025-08-21 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0d440d66-9881-3e2b-8707-a20abd1ead0b | -2.58891 | -51.92565 | 2025-08-21 04:14:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 632bb12a-3130-3a8d-955b-481b13696022 | -3.87046 | -40.4559 | 2025-08-21 04:14:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fa4d8611-e719-3bb3-8e28-dc3706879962 | -2.58328 | -51.9248 | 2025-08-21 04:14:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d8b50358-d454-3472-97c8-95e10b182892 | -2.91535 | -48.30437 | 2025-08-21 04:14:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 89e470b8-832f-309c-b962-47ef5d466c7a | -4.65148 | -41.40202 | 2025-08-21 04:14:00 | NPP-375D | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5a86c05d-b836-3a36-a9d5-5d0eefa2751d | -5.12159 | -43.20837 | 2025-08-21 04:14:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b6d55b6a-6cd1-3a52-98ad-95c2bb67fd9e | -4.17376 | -42.03057 | 2025-08-21 04:14:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 28df68c0-915e-3a34-bea1-4d1a58f11df2 | -5.482 | -42.16721 | 2025-08-21 04:14:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5d1bc650-51e0-3d19-bdfc-be8211f51fbe | -4.8682 | -42.53976 | 2025-08-21 04:14:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f3b94d96-e76f-39f8-8654-2f5428774d43 | -3.99292 | -42.51154 | 2025-08-21 04:14:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b86203ba-c821-3d69-ab88-18828bc3be43 | -4.87043 | -42.54719 | 2025-08-21 04:14:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 011c2c06-4eb8-3811-856c-9a75558c7789 | -5.12437 | -43.21237 | 2025-08-21 04:14:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8143fb63-b9fc-3d0e-b7ce-903436f8a4e7 | -4.64402 | -43.12221 | 2025-08-21 04:14:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b28f2540-6a1b-388a-a404-71a754cdf5ff | -3.86702 | -40.45537 | 2025-08-21 04:14:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4cdc2390-4df6-33fd-bd50-a132ca49b883 | -5.48533 | -42.16772 | 2025-08-21 04:14:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a51dc7ab-f0c1-3644-93bb-4cf9a74ea7f3 | -5.54807 | -37.31311 | 2025-08-21 04:14:00 | NPP-375D | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3b70db3a-6f0f-3feb-8bf9-1050d5145bc6 | -2.94622 | -48.05691 | 2025-08-21 04:14:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6711bbd9-b549-3893-be01-8372208b71a6 | -4.64458 | -43.11874 | 2025-08-21 04:14:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b0bebbae-46a2-3f91-bc42-27271bc12191 | -4.65092 | -41.40561 | 2025-08-21 04:14:00 | NPP-375D | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 41e2dcd8-dce7-3b94-9af0-8a4921710077 | -2.70112 | -48.21283 | 2025-08-21 04:14:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| af1fbd79-f3b5-381b-b194-0c2d30c62f79 | -3.36407 | -43.36578 | 2025-08-21 04:14:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 041b5aaf-198b-3d36-a679-4bb9d58ca58c | -2.30326 | -48.1452 | 2025-08-21 04:14:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f20ce408-eb20-3259-b778-46df28264df2 | -5.09251 | -43.74662 | 2025-08-21 04:14:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3eed200f-0ec7-3370-9232-c02daf14486e | -0.74976 | -47.7532 | 2025-08-21 04:14:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1a9c8060-5602-3e5e-8694-1996f849824d | -4.86463 | -41.57633 | 2025-08-21 04:14:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ff6dce82-da37-36bd-ac2d-599d2575614e | -5.16324 | -37.97984 | 2025-08-21 04:14:00 | NPP-375D | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 4ba8d423-b04d-3189-ab97-0726a6393267 | -4.91048 | -45.31973 | 2025-08-21 04:14:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c64b99d-a8e1-3156-ac2b-817d709a4f08 | -4.85823 | -42.5382 | 2025-08-21 04:14:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d06d9adf-8c70-3735-9889-6e9cbe9f01c4 | -2.44776 | -47.32958 | 2025-08-21 04:14:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 70433837-0143-3010-ad26-a611068e2cc2 | -3.81769 | -41.56157 | 2025-08-21 04:14:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b7a5d68c-879a-3d14-a01d-b698c8197e87 | -4.94153 | -42.89158 | 2025-08-21 04:14:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d8e34ad1-a5c3-3014-be53-910a371b22bb | -5.24294 | -42.71578 | 2025-08-21 04:14:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e73b7c68-d091-3590-a0a1-8f824763842c | -4.87152 | -42.54028 | 2025-08-21 04:14:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 608394a0-ab4b-359f-8769-8d0028040875 | -5.23962 | -42.71526 | 2025-08-21 04:14:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 20278272-3f98-357d-849a-f7240ed97fee | -4.248 | -48.61819 | 2025-08-21 04:14:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e021410f-f38c-3a51-aa71-0cea3f2e1ee3 | -2.38025 | -47.65944 | 2025-08-21 04:14:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 19eca1b2-59f5-32f0-8fb8-4c0ce021f028 | -3.04437 | -49.42067 | 2025-08-21 04:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b3517eb-c970-316c-8529-062c91b502ce | -3.98799 | -47.88703 | 2025-08-21 04:14:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3b2d799-35f4-36b7-8cc2-f2af73dd82e9 | -4.86101 | -42.54218 | 2025-08-21 04:14:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 40eaac50-671a-364f-8b43-430c76524e73 | -4.13453 | -48.01966 | 2025-08-21 04:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9243b569-bc45-34d1-ba0a-5f74e56e4a1e | -4.36804 | -46.53336 | 2025-08-21 04:14:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29a55b77-39d9-3f15-897c-0bca723d9595 | -4.86155 | -42.53872 | 2025-08-21 04:14:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ec7a823d-573c-3c39-9a6b-2ae1b0520575 | -3.94547 | -41.82745 | 2025-08-21 04:14:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8e2d9077-624c-339e-96cc-5ed46002c71f | -5.1177 | -43.21133 | 2025-08-21 04:14:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 97f250ec-0cb3-3811-9471-7596e313853f | -5.23708 | -42.71504 | 2025-08-21 04:14:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 580a4882-5246-38aa-a910-a8903be091f9 | -5.25787 | -40.73564 | 2025-08-21 04:14:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cc92c797-c3e9-32c2-8222-025fe99b7aab | -4.63534 | -42.5353 | 2025-08-21 04:14:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ae385bac-7815-315e-8c0a-d93171fdb21e | -4.64307 | -41.41177 | 2025-08-21 04:14:00 | NPP-375D | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c7404270-a1f5-3bb4-8c68-e5401984cbe6 | -4.65068 | -43.12326 | 2025-08-21 04:14:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| de7f3388-d5f0-3785-a87e-41ee077de2ea | -3.66999 | -40.3532 | 2025-08-21 04:14:00 | NPP-375D | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9d921fab-3870-323f-9588-bbe1c24eb7fc | -4.17044 | -42.03005 | 2025-08-21 04:14:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 265e8618-1d8c-3908-9e7b-d86f834d6cbd | -3.04908 | -49.42144 | 2025-08-21 04:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe5d3c2d-1a8f-3e8f-a5ba-a065304d1ce5 | -2.3504 | -47.4707 | 2025-08-21 04:14:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 05226286-dfe3-318b-8a1a-0bc5a28829ee | -5.25672 | -40.7202 | 2025-08-21 04:14:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 5.7 |
| d44e8504-ad5f-3b8b-b0a9-b5ea0289d12e | -4.64643 | -41.41229 | 2025-08-21 04:14:00 | NPP-375D | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 455a62ad-5140-369e-bb3b-d8f1df1aa632 | -2.44517 | -47.32958 | 2025-08-21 04:14:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f23803de-8fa0-36fc-96e3-a16ae8b0724f | -4.48326 | -43.90359 | 2025-08-21 04:14:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2c20f63d-6b13-30d0-b3d8-8395411a4411 | -4.64735 | -43.12273 | 2025-08-21 04:14:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 31294fe5-94e0-39c0-9c4d-e156c308186e | -0.75057 | -47.75146 | 2025-08-21 04:14:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9ff4aa96-bd34-35f7-902d-30e21aaafd0a | -2.38822 | -47.66394 | 2025-08-21 04:14:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0192e4ac-6a35-3137-bf0b-3b6c2e55c7e5 | -2.91601 | -48.30023 | 2025-08-21 04:14:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 23cfd038-4a4d-3c94-896c-1888f0c4c48f | -3.99237 | -42.51499 | 2025-08-21 04:14:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b4f3d7b6-d195-357a-8141-c6a6a841e9a7 | -2.79085 | -49.59677 | 2025-08-21 04:14:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e7cdb26b-c9f8-3e45-b724-3d011c1aef6e | -3.74219 | -48.93197 | 2025-08-21 04:14:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1199f438-20d2-32fb-a519-965527ea2fdc | -2.99551 | -40.00307 | 2025-08-21 04:14:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |


[Clique aqui para ver as próximas entradas](README22.md)
