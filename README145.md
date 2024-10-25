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

## Dados Diários - Página 145

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5147af2d-54fa-3677-85cd-d45a54e1fd8a | -9.61722 | -45.64401 | 2024-10-25 16:50:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 8a23be7c-dd8c-3af2-a4a2-9919c28ba465 | -9.28231 | -45.23735 | 2024-10-25 16:50:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 6cb3419a-c1a7-32f2-9d96-0ff914b2b498 | -9.28149 | -45.23236 | 2024-10-25 16:50:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 6e570b3e-6bfd-3ef6-8f2b-10350b317039 | -9.27758 | -45.233 | 2024-10-25 16:50:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 75.7 |
| bfc95890-6ba8-3d5c-80c4-6838b1db12b2 | -9.27674 | -45.22791 | 2024-10-25 16:50:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 38.6 |
| 199399db-a925-3313-b755-2fe8879972f1 | -9.27281 | -45.22846 | 2024-10-25 16:50:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 38.6 |
| 2ba4d5a5-8045-3b79-a8d6-0720f146bca0 | -9.26973 | -45.23406 | 2024-10-25 16:50:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 1030e170-a76b-3a60-915b-0736e2b351b3 | -9.26741 | -45.31623 | 2024-10-25 16:50:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 1ad5dc4d-ecea-3969-811d-f654ca076a0b | -9.2588 | -45.31254 | 2024-10-25 16:50:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 9f2a3ad5-900e-365a-ac58-933603d8da4e | -9.2388 | -45.26502 | 2024-10-25 16:50:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| ea742b4d-1b5b-368d-b472-40d5760ddded | -9.2349 | -45.26568 | 2024-10-25 16:50:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| af318cf4-62c4-310e-ab03-f2ceb809f3d5 | -9.23151 | -45.24556 | 2024-10-25 16:50:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 5861ddfd-5ed4-3c27-a824-d3fe3d51b20e | -9.23016 | -45.26132 | 2024-10-25 16:50:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 89689961-7be0-3234-a8fa-e66343ec46e3 | -9.22761 | -45.24624 | 2024-10-25 16:50:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 475192e8-697b-3b46-8552-7639bec56752 | -9.22541 | -45.25698 | 2024-10-25 16:50:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 48f5a821-ae17-3c06-9176-2649a99c139b | -9.22456 | -45.25197 | 2024-10-25 16:50:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 64d5eaa2-3778-3b88-93bf-5f453d8cdec4 | -9.09025 | -45.05425 | 2024-10-25 16:50:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 5790dd0c-3227-3953-ae0e-bc765e29936c | -9.08808 | -45.06543 | 2024-10-25 16:50:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5b892cc9-617f-3738-93d0-6896d0476ebe | -9.08719 | -45.06021 | 2024-10-25 16:50:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 25.8 |
| ecb653d4-30b1-3c37-81b3-15ced1b197fe | -9.08631 | -45.05502 | 2024-10-25 16:50:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 5cb25f98-5508-3b02-b8e8-892cdd53bf08 | -9.08412 | -45.06606 | 2024-10-25 16:50:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 35e248d7-3cf2-3a2b-8250-b51093b8e6c3 | -9.08324 | -45.06091 | 2024-10-25 16:50:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 8beaf8d2-b46d-3710-a8a2-756542e691be | -9.08145 | -45.05035 | 2024-10-25 16:50:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 2b080dd4-54a4-3927-be3f-f7ac65a8e0cd | -9.0784 | -45.05641 | 2024-10-25 16:50:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 8e4fd7cd-0950-36b1-895a-1fa38a26c118 | -9.07445 | -45.05709 | 2024-10-25 16:50:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| a129e70a-8c38-3417-9468-721d2e5a7a4b | -9.78604 | -45.53458 | 2024-10-25 16:50:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 002dd193-616c-32a1-8c4e-710fc0c630d4 | -9.66746 | -45.6887 | 2024-10-25 16:50:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 20ed9b68-a640-3c41-b9cd-ecc61474e159 | -9.6316 | -45.63679 | 2024-10-25 16:50:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| bc36ac21-83a9-3f28-ac23-864bf81c87d8 | -9.62939 | -45.64687 | 2024-10-25 16:50:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 2b008f52-ae12-3e3f-9513-56edd685a292 | -9.62781 | -45.63743 | 2024-10-25 16:50:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 975358f9-e900-3d3a-95c5-5ba0a3ba4c0f | -9.5816 | -45.61447 | 2024-10-25 16:50:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 9dee4746-88f3-3e0c-afcb-a0c47f804e17 | -9.57781 | -45.61515 | 2024-10-25 16:50:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |
| f91c127d-3f35-3e2d-9f1b-bd6324415fdb | -9.57652 | -45.70231 | 2024-10-25 16:50:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 50232381-8e36-3598-8400-fafd3f572d92 | -9.57571 | -45.69738 | 2024-10-25 16:50:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| f5833fac-fbb7-3865-b864-a24619bf1040 | -9.57416 | -45.68795 | 2024-10-25 16:50:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c286ab6e-bc2b-3cb1-8c49-02da92789594 | -9.57272 | -45.70284 | 2024-10-25 16:50:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 3549f07e-68b7-326e-9259-8d5aea916553 | -9.57193 | -45.69801 | 2024-10-25 16:50:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 111f440f-6a6f-3569-81c4-db79619596d1 | -9.57115 | -45.69326 | 2024-10-25 16:50:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7ea032eb-5fc7-34d0-a4bc-0fc598107c66 | -9.56736 | -45.69388 | 2024-10-25 16:50:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 12c3db74-e29b-3f49-a759-4a932302adb4 | -9.53873 | -45.22671 | 2024-10-25 16:50:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 8d875287-60e7-3045-b826-0f14336da414 | -10.04853 | -45.54982 | 2024-10-25 16:50:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 74023e1d-3223-32da-818c-16d7cf29c998 | -9.91971 | -44.59512 | 2024-10-25 16:50:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ec5a65ea-2c20-3174-bc12-9faf902717cb | -9.89496 | -44.5957 | 2024-10-25 16:50:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ec9ea257-279d-33fe-ace1-39e151bf0b30 | -9.79312 | -44.75664 | 2024-10-25 16:50:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 6c03fc1b-4fe5-34e6-9bee-dd53ea19a5be | -9.74144 | -44.63104 | 2024-10-25 16:50:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 752753c2-7217-3b2c-9f4c-ba295613810f | -9.55039 | -44.58615 | 2024-10-25 16:50:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 11d53fcc-4c20-341f-a0a9-611da72cf553 | -10.83813 | -44.95164 | 2024-10-25 16:50:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| cbf2638f-f270-3d28-bc7f-aae5e0665b95 | -10.82733 | -44.9586 | 2024-10-25 16:50:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 28.5 |
| d8ee6c37-93c0-3b72-96dd-1872951e2658 | -10.75677 | -44.87605 | 2024-10-25 16:50:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 93539400-9cac-3385-b9d3-7d77e7618ea9 | -10.5682 | -44.54664 | 2024-10-25 16:50:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| bd240e73-cfdf-3f91-be7f-b5b392d7ac62 | -10.56803 | -44.52134 | 2024-10-25 16:50:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 37.8 |
| 689e98da-fccb-3bd0-8dc4-635c20c4fb0a | -10.55324 | -44.88695 | 2024-10-25 16:50:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 822c8c99-239f-3d40-bc87-725111a920eb | -10.55278 | -44.88454 | 2024-10-25 16:50:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 27.6 |
| d349065d-f135-330f-a090-7c9dff03d9c0 | -10.54932 | -44.88763 | 2024-10-25 16:50:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 802a063b-b798-3b15-9d63-6d08cfac092a | -10.54886 | -44.88522 | 2024-10-25 16:50:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 906c998a-3bc3-3700-8eb1-77c9337ec13c | -10.54846 | -44.88261 | 2024-10-25 16:50:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 99eb64ee-61c0-3aa4-ae62-85a5d0f3ba81 | -10.50568 | -45.05724 | 2024-10-25 16:50:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e292dcc1-337d-3558-bbaf-00f776b8d3cc | -10.50547 | -44.86677 | 2024-10-25 16:50:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 3e973006-756f-3ffb-9928-f559497ad773 | -10.50156 | -44.86747 | 2024-10-25 16:50:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 4ddb9511-3689-31a2-99e6-2f76a83f44a9 | -10.50098 | -45.05305 | 2024-10-25 16:50:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 079ce0d7-0581-3808-843a-12e973ed43f3 | -10.5007 | -44.8624 | 2024-10-25 16:50:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 182d1947-4f4b-3f17-9f22-86c1985ab7c8 | -10.48976 | -44.91664 | 2024-10-25 16:50:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3c409d2e-1690-3552-ba2f-8d8b8dbd48ca | -10.36228 | -45.35672 | 2024-10-25 16:50:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| f28b9d91-875d-3d87-9898-4f940ac2c21b | -10.19512 | -45.37695 | 2024-10-25 16:50:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 30.7 |
| dd3ad935-3afc-32ba-9c6f-e0660bceba30 | -10.18826 | -45.38296 | 2024-10-25 16:50:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| c6b0deac-8142-3789-b6c1-73abcc35a2ed | -10.28936 | -45.01834 | 2024-10-25 16:50:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 6d7260a0-5591-3d83-9dda-2de4067bf0a4 | -12.11651 | -45.72282 | 2024-10-25 16:50:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 7a4bbf1d-235c-35d1-b3a8-0af022400eff | -12.11315 | -45.72618 | 2024-10-25 16:50:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 35.1 |
| f7ee6995-6a54-3321-af97-1f084fc94592 | -12.11286 | -45.72346 | 2024-10-25 16:50:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 17caaa84-2728-32de-b95e-997348dc8688 | -12.10775 | -45.71541 | 2024-10-25 16:50:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| a7d6eeb1-5245-36cb-82c0-63f434ace78f | -12.10515 | -45.72313 | 2024-10-25 16:50:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 9ec881fa-ca3a-3e75-8ff7-2839853ac20d | -12.10444 | -45.71877 | 2024-10-25 16:50:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| b43c130a-4b49-3d19-8c4a-a2fd235c4a06 | -11.95833 | -44.76388 | 2024-10-25 16:50:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| efe11ffa-2cc2-376e-a316-801ccf7fd084 | -11.90409 | -44.8188 | 2024-10-25 16:50:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ed7ecd4d-0a73-3db7-b036-2a10388c4594 | -11.82649 | -44.88605 | 2024-10-25 16:50:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 74a6a529-b25f-3e88-a7f5-12e5d89fb644 | -11.76229 | -44.94063 | 2024-10-25 16:50:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1aa021bc-189e-3966-8599-b8f224042287 | -11.75951 | -44.9331 | 2024-10-25 16:50:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| d27a6896-abaf-3161-a95e-84fa200aac3d | -11.53872 | -45.09347 | 2024-10-25 16:50:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 14b8ae38-a52e-388a-9fa1-27bf78da355d | -11.52608 | -45.87547 | 2024-10-25 16:50:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 5566af76-b849-3ba0-9f20-dff1a657c92e | -11.24729 | -44.67865 | 2024-10-25 16:50:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 1c1851bd-e371-389e-86f1-348073fbbd40 | -11.20857 | -44.66476 | 2024-10-25 16:50:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 549d2bdd-4f4f-3014-be54-0e20d890a60b | -11.18601 | -45.37659 | 2024-10-25 16:50:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 5b77b4c7-49ea-3f69-886b-b610b825d58c | -11.18527 | -45.37498 | 2024-10-25 16:50:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| bdb8b1f8-ce61-372e-ad30-13b6cbca9960 | -11.18223 | -45.37714 | 2024-10-25 16:50:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 57c8b36b-3b13-3d36-bdf2-cb69f16b3eca | -11.10672 | -45.92756 | 2024-10-25 16:50:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b7fce540-c13e-3fce-943b-465e1c298b8f | -11.10013 | -45.93311 | 2024-10-25 16:50:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| b22a0854-8833-3635-8a6c-3af9c4bfe209 | -11.0994 | -45.92875 | 2024-10-25 16:50:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 497d9929-7350-3096-bbc0-707c9dbcedd0 | -11.07893 | -45.96365 | 2024-10-25 16:50:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 1e06a969-cd4c-3621-9089-4adc8c6bcb20 | -11.07528 | -45.96429 | 2024-10-25 16:50:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| e24150f9-a7f0-392a-84fe-c759a3dca25b | -11.07164 | -45.96493 | 2024-10-25 16:50:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 8a515bdf-6c9e-302f-b822-0450d522c73e | -11.0709 | -45.96053 | 2024-10-25 16:50:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 13b38d10-b2a3-371d-9c57-ea823670c23c | -11.06848 | -45.96911 | 2024-10-25 16:50:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a635f435-ea25-32e6-a901-66698c06287b | -11.06799 | -45.96555 | 2024-10-25 16:50:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 673b0415-aaf8-30e8-a0e6-183e4db532c5 | -11.06725 | -45.96115 | 2024-10-25 16:50:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| df1f8f3c-e071-3d2a-8aa9-a442480c9232 | -11.06705 | -45.9603 | 2024-10-25 16:50:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| bb69b9ff-c2ca-3c68-bc7d-ac1ca740ffe6 | -11.06508 | -45.97057 | 2024-10-25 16:50:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 30fe3ce4-9080-3cc6-be0c-21c1047f2bbb | -11.06483 | -45.96973 | 2024-10-25 16:50:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9fe314f5-a513-3f86-8b14-3e2480d4fe4b | -11.06411 | -45.96532 | 2024-10-25 16:50:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| b59f6619-212e-3e29-9eb3-a5c6b48fd6e0 | -11.0636 | -45.96177 | 2024-10-25 16:50:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0fe1251f-b4ed-3c38-b2c4-c5c23d76fe91 | -11.0634 | -45.96092 | 2024-10-25 16:50:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |


[Clique aqui para ver as próximas entradas](README146.md)
