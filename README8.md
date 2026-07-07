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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3203bdc5-7b1d-3df0-b7e8-61d548296aa1 | -7.01248 | -42.78699 | 2026-07-07 03:49:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f2c80cb7-1276-3597-b2d5-d0e8a80aa7d1 | -11.63753 | -46.37393 | 2026-07-07 03:49:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1fd9d49e-d3d0-3108-b4fd-3fedf01e23f9 | -11.68602 | -44.56148 | 2026-07-07 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3468e0b8-4e5d-34dc-b74d-e70482d31c96 | -6.89417 | -43.71293 | 2026-07-07 03:49:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7200257a-5b2a-3eeb-86bd-6dd555487ba4 | -9.45576 | -36.81594 | 2026-07-07 03:49:00 | NOAA-21 | ESTRELA DE ALAGOAS | ALAGOAS | Brasil | 2702553 | 27 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ec286004-f724-3d9f-bdec-3eac19e7d229 | -11.62979 | -46.36004 | 2026-07-07 03:49:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 719c3180-413c-356c-a781-81e5f99d9929 | -13.07571 | -48.17257 | 2026-07-07 03:49:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5df33948-0e34-3780-8881-a1c961a5c15b | -9.16025 | -36.81241 | 2026-07-07 03:49:00 | NOAA-21 | BOM CONSELHO | PERNAMBUCO | Brasil | 2602100 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 29e4eb18-d87c-3e50-8464-6198df7aa6b8 | -11.64282 | -50.36964 | 2026-07-07 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a496afe3-6ce7-3ce8-8c28-e670e25b9a6b | -11.67794 | -44.55538 | 2026-07-07 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 307e7e27-a6bc-3791-a9ca-45d24e91b39f | -10.69514 | -49.60743 | 2026-07-07 03:49:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ccc9efb6-eeec-336b-9376-0f1eb2a89f55 | -8.07386 | -46.69104 | 2026-07-07 03:49:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f7c03907-b809-3ecb-9044-e84253372c87 | -11.66498 | -44.57621 | 2026-07-07 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a1f5621a-1739-3519-9a4e-0531547b9fa6 | -9.38032 | -44.71688 | 2026-07-07 03:49:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0f403d21-d9dc-326f-89a7-8b8a2866cc36 | -8.1282 | -47.11696 | 2026-07-07 03:49:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 33b49da3-2d7e-3ed1-a5a1-bb7fb70aea47 | -11.62923 | -46.36297 | 2026-07-07 03:49:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f3e6474e-6fce-3d53-9b09-4e73f090a589 | -11.67995 | -44.56966 | 2026-07-07 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a8cfe833-8122-30ab-8904-d6416f381ec8 | -11.66134 | -44.57091 | 2026-07-07 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 83f1b574-4fad-3497-a425-8b5c5901625c | -12.79327 | -44.50685 | 2026-07-07 03:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b00ceeaf-47d7-3acd-8350-fd550e6781f5 | -8.12652 | -47.11565 | 2026-07-07 03:49:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c0c1c697-7694-35c4-8995-470736bc7984 | -11.66742 | -44.56275 | 2026-07-07 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 97899506-f34e-39fd-8a0a-efe0a4ad5135 | -9.19484 | -45.3188 | 2026-07-07 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2b664c39-a712-3945-b1ca-d3974390bf44 | -11.65934 | -44.55665 | 2026-07-07 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f6658282-eb12-30a5-bc7c-a4eb39ae71d8 | -11.62847 | -46.37043 | 2026-07-07 03:49:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 84a200b6-4548-38f6-a8ff-1c203fb44b36 | -11.63063 | -46.35865 | 2026-07-07 03:49:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c623c165-7eec-3914-8e2e-1cd39d9e23f8 | -12.76218 | -44.55437 | 2026-07-07 03:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b65e7d7f-b512-3842-bc8b-0a236d5d9384 | -8.12271 | -47.11531 | 2026-07-07 03:49:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b0969956-f247-38e5-ab00-9d84507cbdfb | -6.90494 | -43.70497 | 2026-07-07 03:49:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 22740e3b-7ba1-326f-8c46-0a99808e0ef9 | -9.28869 | -49.58216 | 2026-07-07 03:49:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5ac319c7-fbe3-34b0-ac48-26fd5741b052 | -9.50717 | -36.54744 | 2026-07-07 03:49:00 | NOAA-21 | PALMEIRA DOS ÍNDIOS | ALAGOAS | Brasil | 2706307 | 27 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 46c31b4b-8634-3cf4-8a06-478281fc3328 | -10.69416 | -49.61251 | 2026-07-07 03:49:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| aa73c5ca-f979-36bd-8540-9e269edc72a3 | -13.07648 | -48.16864 | 2026-07-07 03:49:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7c76ed52-7919-31f7-abbb-8e8bd9148621 | -12.45167 | -49.57926 | 2026-07-07 03:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d7357d19-5e23-3a6b-84c2-082d25e54c3f | -12.78615 | -44.49662 | 2026-07-07 03:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7b907469-b1dd-3e27-a654-0127485fbb70 | -11.99268 | -45.13823 | 2026-07-07 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5f62eddf-599f-3337-b09e-193caf924476 | -12.79249 | -44.51114 | 2026-07-07 03:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1381e339-8e67-3e27-8a7d-38c6f6d668fd | -11.67349 | -44.55457 | 2026-07-07 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 18.4 |
| c5a62e74-41e1-3b73-8ed4-39e0505d1e28 | -11.69127 | -44.5578 | 2026-07-07 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7c008083-a227-3156-984e-bd52257bb3e9 | -6.92849 | -43.70421 | 2026-07-07 03:49:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 1a30a7ad-f721-387f-b1b5-37c2e8dfe413 | -12.68476 | -48.21354 | 2026-07-07 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 96e26853-e75e-379c-8992-6ce72d4d5140 | -11.66216 | -44.56643 | 2026-07-07 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8b325f99-34cb-3213-a5e3-ac67f6250784 | -11.62789 | -46.37364 | 2026-07-07 03:49:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4bc59644-14fe-3b1e-aa84-bc049fc9e1a8 | -11.67105 | -44.56804 | 2026-07-07 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7a83378e-ead0-38bb-af40-335d0c813619 | -7.10505 | -46.51545 | 2026-07-07 03:49:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b296abd7-8b9e-3178-8a7e-9c07e6cdabf4 | -12.50418 | -48.26376 | 2026-07-07 03:49:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e1e7f2b3-0bf7-39f6-aa54-db6e65bfa829 | -11.63309 | -46.36995 | 2026-07-07 03:49:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 94693161-5ddb-3fe2-8b5a-44e7f1380e0e | -12.78971 | -44.50172 | 2026-07-07 03:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 459f251a-b2d5-35aa-b4e1-48afc31ab96c | -11.68157 | -44.56067 | 2026-07-07 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 49a406d7-a8df-32a7-b7d9-981941f133da | -11.69046 | -44.56228 | 2026-07-07 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 56f08ef8-756e-3778-9f13-672acba1383d | -6.89882 | -43.70963 | 2026-07-07 03:49:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d510d79d-269d-36e2-bd34-8c498f56871a | -12.75346 | -44.55275 | 2026-07-07 03:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dda5f731-81bd-3ab8-9da4-7a34ea29e2e6 | -11.62751 | -46.37198 | 2026-07-07 03:49:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 42eadcad-aaf4-3353-90e9-d314796f84b2 | -11.67187 | -44.56356 | 2026-07-07 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| be2509e2-0d2c-32e5-8d13-f3d1ca527835 | -12.78381 | -44.50952 | 2026-07-07 03:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 48250b6d-04c2-3aa4-b830-ea9639f4ed83 | -12.75782 | -44.55355 | 2026-07-07 03:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5ce1d757-bc81-34ed-842f-b43727553c4c | -9.19972 | -45.31971 | 2026-07-07 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d4267b8a-a411-356a-92cc-951b4a956b3d | -10.92974 | -43.0633 | 2026-07-07 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ecfb10d1-00e3-3d1c-9ce4-9c8936422c44 | -11.84463 | -48.2527 | 2026-07-07 03:49:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d851951b-c1d2-3458-a0d9-de7571b5c276 | -10.93382 | -43.06402 | 2026-07-07 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 3f38cf8c-dd66-387b-ace1-d7e10084e8b3 | -12.78893 | -44.50602 | 2026-07-07 03:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f8bfe55f-b73f-3fba-9916-a4f119a2037a | -7.90428 | -48.25331 | 2026-07-07 03:49:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 27776ce0-409a-3519-98f8-b5af881439f3 | -9.21231 | -45.31991 | 2026-07-07 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2b663bf9-9c3a-3487-a1a4-ff717d9936c1 | -7.90515 | -48.24857 | 2026-07-07 03:49:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6fd7ace5-4c11-3aab-a418-a580fea41b3c | -12.75425 | -44.54844 | 2026-07-07 03:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 40c4ff46-e8e4-3d97-96c5-bcc9677ad7f0 | -11.67268 | -44.55906 | 2026-07-07 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 280a44e5-98ac-3513-8de1-d1938245e0ba | -9.43837 | -40.32179 | 2026-07-07 03:49:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 96829357-676f-370d-971e-ac487b27e1ee | -9.44125 | -40.32645 | 2026-07-07 03:49:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| ba12a916-5a93-313f-b7b2-ddd08119641c | -12.78815 | -44.51032 | 2026-07-07 03:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b6bf9f9a-5bd4-3863-b4f5-f1186e7a65c7 | -11.67914 | -44.57415 | 2026-07-07 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0aa476cb-15d0-3cb9-bcd8-269113529c1a | -7.00668 | -42.76929 | 2026-07-07 03:49:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 27231cff-4c14-3455-ba1d-d063932685e5 | -11.67024 | -44.57252 | 2026-07-07 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d86b046a-0bfc-322c-aeed-3d531a5f5998 | -11.63347 | -46.37152 | 2026-07-07 03:49:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3f52d4df-f4b4-3bfa-b692-d5c78411cacd | -7.64044 | -50.02878 | 2026-07-07 03:49:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 563ac2d3-7231-34a1-95f0-60a33f0cc3a8 | -9.37945 | -44.72179 | 2026-07-07 03:49:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5e2c34a3-8d47-391d-9757-89a6f0228e2a | -9.28418 | -49.57788 | 2026-07-07 03:49:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 34bc4532-9a93-3851-833d-4e784fbcd3cf | -6.93383 | -43.7004 | 2026-07-07 03:49:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 66b7c194-0708-350c-8d59-c69bb1bc12c5 | -13.51859 | -43.98776 | 2026-07-07 03:49:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ec97e9fb-31ec-3a10-a0d6-a0b6a4cbe511 | -9.20948 | -45.3215 | 2026-07-07 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8120ca62-ca52-3d4b-8e4a-2d2009dd91ec | -11.92694 | -43.37434 | 2026-07-07 03:49:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 749e8547-0218-3c65-a0c7-09604f93f713 | -11.62304 | -46.36817 | 2026-07-07 03:49:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 35265456-6058-37b4-bffe-c4b207628a31 | -9.2823 | -49.58088 | 2026-07-07 03:49:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7c8099f5-697f-31c2-889b-8c7aa1db0388 | -7.64832 | -50.02411 | 2026-07-07 03:49:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 774bdf60-744f-35c0-a0c2-8d9cb09b7436 | -11.66823 | -44.55826 | 2026-07-07 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b0175f92-09ac-3308-8d68-dfd5f7163fc7 | -11.65326 | -44.56482 | 2026-07-07 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7453d960-7ee8-3cc6-adb0-ecb3b2625a59 | -12.7586 | -44.54926 | 2026-07-07 03:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2762624f-23aa-323c-8a88-620ad84f13c5 | -11.66661 | -44.56723 | 2026-07-07 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c79792c5-b557-3869-8b12-afab7ac8e866 | -10.56244 | -36.5809 | 2026-07-07 03:49:00 | NOAA-21 | PACATUBA | SERGIPE | Brasil | 2804904 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9772d399-4fcd-3544-b294-36df577448e5 | -11.62242 | -46.37137 | 2026-07-07 03:49:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9dbba097-138d-360e-90dc-1d96a98dc254 | -11.68763 | -44.55251 | 2026-07-07 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 492474e9-11f2-3ae1-a67a-c3e4b8b1729a | -11.66905 | -44.55377 | 2026-07-07 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 59f3b322-9407-3e24-842d-ab98690f592f | -7.006 | -42.77336 | 2026-07-07 03:49:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 68ad3bf9-5cd7-32d9-8cfb-364d18823087 | -7.00889 | -42.7822 | 2026-07-07 03:49:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4d2221f0-875f-3fe4-9eff-a2d8d7b27a7b | -8.12101 | -47.11417 | 2026-07-07 03:49:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| cbd70e54-9986-36a6-b5a1-a0b3cddb74af | -11.68682 | -44.55699 | 2026-07-07 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 09e3a5b0-e2a1-39ae-8841-e5ae4dedbc11 | -11.66579 | -44.57172 | 2026-07-07 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| cbb6db8b-55e8-3ef6-89b1-60562b939846 | -11.65853 | -44.56114 | 2026-07-07 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1c8c9b16-9e73-3e52-ae86-43b468cb0e1a | -10.93252 | -43.07138 | 2026-07-07 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 5b47b6d3-f23b-35f0-98c1-2b0d3b6ecd29 | -6.90412 | -43.70964 | 2026-07-07 03:49:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 7a225911-95b8-35d8-a2c7-ce537a1b553e | -8.07048 | -45.58219 | 2026-07-07 03:49:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c692fede-8877-3c71-a32d-e2875725d7a9 | -10.69213 | -49.60887 | 2026-07-07 03:49:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README9.md)
