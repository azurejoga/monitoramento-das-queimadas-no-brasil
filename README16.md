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
| f36a467e-abb5-31c8-a53f-d8d438c560a9 | -6.6226 | -58.4995 | 2026-08-25 03:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 1efa92fc-0a0f-3682-bbd5-41466f3aaa1b | -3.5406 | -48.1889 | 2026-08-25 03:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 167.3 |
| 6f5b992a-878e-3b0e-8d89-e730a65e187e | -7.2901 | -45.3683 | 2026-08-25 03:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| ed2aeece-93e9-3715-8bad-04fc94cc93d8 | -6.641 | -58.4987 | 2026-08-25 03:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 102.0 |
| c483dd16-57fe-3f8e-8c7c-19246fcad844 | -7.2713 | -45.37 | 2026-08-25 03:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 53.4 |
| ede3179b-0676-3c2a-a71c-023374dcf286 | -7.2661 | -45.8443 | 2026-08-25 03:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 51.4 |
| f6fbfd86-d78d-3999-857f-6c9030d46fff | -6.9873 | -59.2389 | 2026-08-25 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 9b666879-e440-3801-8910-327c1afbe898 | -3.5221 | -48.1896 | 2026-08-25 03:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| c3e48fbe-f482-335d-8065-328f6986fb54 | -3.5407 | -48.1673 | 2026-08-25 03:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 158.2 |
| ca003870-4c5a-3445-9ecd-348fa35b5837 | -7.0058 | -59.2382 | 2026-08-25 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 148.5 |
| f8722295-e13e-335a-9c00-2e00ac052d3a | -7.2903 | -45.3456 | 2026-08-25 03:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 67c6ae66-7b28-367a-8ca3-3a05738ddcf0 | -7.0057 | -59.2575 | 2026-08-25 03:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 169.9 |
| 1c656d2e-608f-3c32-9a2d-a51df4753e03 | -7.31769 | -42.97936 | 2026-08-25 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 699b60e1-dbeb-3212-9d6f-b41535f51549 | -5.68349 | -43.27388 | 2026-08-25 03:30:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| eb88a5d4-bed4-34db-9110-de9ecd3423bb | -7.13817 | -42.78085 | 2026-08-25 03:30:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a89a17bd-3e5b-37b3-9f0e-d91780a6ebd2 | -7.14181 | -42.76064 | 2026-08-25 03:30:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| e8584465-8173-3a26-9f97-a1117d6decaf | -7.44377 | -43.10366 | 2026-08-25 03:30:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 1d0275e7-4863-3bbf-ab19-23e7c7aedd95 | -7.27607 | -44.07868 | 2026-08-25 03:30:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| d1f6048b-2483-3917-9564-b02a15b83f5c | -7.28145 | -44.0714 | 2026-08-25 03:30:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 5895240d-51ef-3149-9442-740b8f03bbda | -7.19299 | -42.74374 | 2026-08-25 03:30:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 19d64368-c87a-3e44-aff4-cb422f4c19f8 | -7.42957 | -43.08952 | 2026-08-25 03:30:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6c5c1246-86f2-3c86-b28d-360a40a9ede0 | -7.25693 | -45.36963 | 2026-08-25 03:30:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 946761ac-d73b-3713-9ebf-16252329bfcc | -5.62341 | -37.4859 | 2026-08-25 03:30:00 | NOAA-21 | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f6c11df2-973a-349e-a69f-73ba7259ab21 | -7.43789 | -43.10264 | 2026-08-25 03:30:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| ebce3759-fea5-3492-97c2-49305ff86aa7 | -7.43628 | -43.11125 | 2026-08-25 03:30:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 285bf3bb-715d-32c6-bf81-bd601f56f69a | -7.27425 | -44.07529 | 2026-08-25 03:30:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 33eedb6e-0f24-397b-ac5c-9a0f524e2eed | -7.15119 | -42.74168 | 2026-08-25 03:30:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 46c81bc4-79a3-3faa-b47d-0779deceb30f | -7.90567 | -46.3785 | 2026-08-25 03:30:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f0032d2c-47a2-32dd-a47b-0cf14e93f23f | -7.26565 | -45.84343 | 2026-08-25 03:30:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| e924f58f-e4ba-3621-ab32-932a3bf4a2f1 | -5.92211 | -43.63742 | 2026-08-25 03:30:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c611142a-ab8e-3d23-9c2c-b99756a2e1d0 | -7.89938 | -46.35706 | 2026-08-25 03:30:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 514d5d9e-5f91-33ef-8d2a-8b09227b8419 | -7.25745 | -45.85474 | 2026-08-25 03:30:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| b0672121-18a4-3408-9426-3d50b4c4730d | -7.26251 | -45.377 | 2026-08-25 03:30:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d2787c40-eb28-355c-b42b-e40e78afbbd2 | -7.28864 | -44.08068 | 2026-08-25 03:30:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| b16cb1e4-d1c0-3165-94e2-6d79700c8206 | -8.07877 | -44.64485 | 2026-08-25 03:30:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b40f9b28-f01e-3aa6-b454-40894ad47032 | -7.2868 | -44.07732 | 2026-08-25 03:30:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 42c882ea-a0d4-3bf9-83da-1065f818e11f | -7.64584 | -42.72469 | 2026-08-25 03:30:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a392699d-a677-30b1-99a6-215c2c44ffdf | -7.24799 | -45.8604 | 2026-08-25 03:30:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 2bd124f1-f5de-37fd-b401-720b0377dd66 | -7.89175 | -46.33633 | 2026-08-25 03:30:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 05945965-fdfc-38eb-8b26-98d600148497 | -7.90346 | -46.37354 | 2026-08-25 03:30:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| bb09b0eb-dbec-3210-8d63-0999f0090c96 | -7.43513 | -43.08496 | 2026-08-25 03:30:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| b6ca51c9-8415-3148-8a74-b82ee949a991 | -7.30133 | -43.00294 | 2026-08-25 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 47d19cdc-a51c-3aba-895b-ce6c22d360f0 | -7.25255 | -45.38122 | 2026-08-25 03:30:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 072d5fcb-6f6c-3154-8026-48f31db734ed | -7.18662 | -42.74327 | 2026-08-25 03:30:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bf541747-2a2b-34d1-8994-60b8f81787ae | -8.07136 | -44.64907 | 2026-08-25 03:30:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 10ffe4a6-4f71-3422-bc75-ab13e2598de7 | -7.26309 | -45.85669 | 2026-08-25 03:30:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 6077d5d9-40c8-3dea-9f86-c3b22876de35 | -7.14972 | -42.74985 | 2026-08-25 03:30:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 572852ef-0593-3768-bcec-e6dcf33bcebe | -7.06367 | -42.92621 | 2026-08-25 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 08260cd2-f183-3e01-a6b3-3f252038f035 | -7.26436 | -45.85619 | 2026-08-25 03:30:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| ceb2e17c-012f-3ae3-a569-0ffb65b3cea4 | -7.0629 | -42.9304 | 2026-08-25 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8d90f89a-8405-3eb7-8b2f-67bf1b39951c | -7.2616 | -45.37001 | 2026-08-25 03:30:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5d9c5a0a-2b7a-308a-b76a-4a037908c276 | -7.14757 | -42.76179 | 2026-08-25 03:30:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 59d0b025-2adc-3109-ac82-0eabda9eeadd | -7.4453 | -43.09542 | 2026-08-25 03:30:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2acc2e8d-2171-32ff-9a91-045cdfc319b4 | -7.27835 | -45.36723 | 2026-08-25 03:30:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 1db9f244-2e62-34ff-aae0-3134aa6cd7df | -7.29417 | -45.35751 | 2026-08-25 03:30:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| b77476b2-9468-32a4-8667-dbad8ff5b3be | -7.30164 | -42.96814 | 2026-08-25 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 68f42833-9c96-3d14-b142-ee9974659a79 | -7.9027 | -46.35565 | 2026-08-25 03:30:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| f47c327d-fb0a-3c95-a809-914141eb1dfc | -7.42797 | -43.12317 | 2026-08-25 03:30:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9bf4b951-4d50-39f4-816b-ddca3a9aafe2 | -7.9061 | -46.36018 | 2026-08-25 03:30:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e2469407-0956-37fc-ab9b-017e4cbec034 | -6.94543 | -42.68834 | 2026-08-25 03:30:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 54378b0d-584a-39da-ac3a-c6b379e07dac | -7.28625 | -45.36241 | 2026-08-25 03:30:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 16c81ad2-ab12-3bc1-9499-4b0764afb179 | -4.719 | -42.76824 | 2026-08-25 03:30:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9d9b1ed6-2a41-3c43-a29d-b02d5f01974e | -7.13168 | -42.7837 | 2026-08-25 03:30:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b03ac201-0a49-31fc-9ffb-f58ac51725b8 | -7.28508 | -45.36859 | 2026-08-25 03:30:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| bfeb491c-b599-35b9-a2c8-121f5c38627f | -8.07779 | -44.65004 | 2026-08-25 03:30:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 47324f7f-a5e2-3c6b-adf0-53f6b9f133da | -7.90479 | -46.36681 | 2026-08-25 03:30:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 2ad6e7bc-8ae4-3648-b162-2bf365619074 | -7.14828 | -42.75784 | 2026-08-25 03:30:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c927ab8d-7fe9-3d1e-a404-e3cbc82ee51f | -7.2656 | -45.84952 | 2026-08-25 03:30:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 530d6ce8-a663-3b3b-878c-065e4c2473d7 | -8.07038 | -44.65423 | 2026-08-25 03:30:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 45415f6b-30ab-32bc-a16d-7956c74fb81d | -9.25921 | -35.61981 | 2026-08-25 03:30:00 | NOAA-21 | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 4aa4dd2f-9395-3c16-b521-da9e4504eb0b | -7.31184 | -42.97836 | 2026-08-25 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 36c4df2d-de2f-30e7-b071-f5bab1bcdc40 | -7.42927 | -43.1249 | 2026-08-25 03:30:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 3b730a6b-5743-33ba-bb42-f4313de8fb09 | -7.26488 | -45.36455 | 2026-08-25 03:30:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 197880b5-e2ea-3bb6-8513-5b0497eb93ea | -7.25054 | -45.85324 | 2026-08-25 03:30:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 54e72128-49aa-377f-a5cd-f0e15a5f5bcb | -7.43005 | -43.12053 | 2026-08-25 03:30:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| da8f0687-4235-3f36-9249-8f00558de792 | -4.71822 | -42.77261 | 2026-08-25 03:30:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8b91b28d-7abf-3a0c-a1a8-aa180bd874f1 | -4.71682 | -42.76767 | 2026-08-25 03:30:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dc5a5afe-8cef-3dfa-b9b3-fb38018c1ec1 | -7.26836 | -45.37127 | 2026-08-25 03:30:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 639f9282-06ed-3462-9145-95ab4c35f8bb | -7.1924 | -42.74424 | 2026-08-25 03:30:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ce2a1096-9a63-3dfa-9164-bd30042c70ef | -7.30751 | -42.96902 | 2026-08-25 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9b1ccf45-4c28-3a4f-835e-8e63e62a51b8 | -7.15045 | -42.74578 | 2026-08-25 03:30:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d8ffd082-9511-3353-a1cb-27749c6aa403 | -8.37188 | -35.36374 | 2026-08-25 03:30:00 | NOAA-21 | PRIMAVERA | PERNAMBUCO | Brasil | 2611408 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d50da9ad-371d-3514-98c9-2e5de916316d | -7.8847 | -46.33493 | 2026-08-25 03:30:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| cff362e3-a8e0-36cb-a52b-cb98157d64b1 | -7.43466 | -43.11988 | 2026-08-25 03:30:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9433b8e4-a848-34e9-acba-5795ee3f4c2b | -5.68344 | -43.27608 | 2026-08-25 03:30:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d29b40b6-1676-31f4-b401-a415b780a78c | -7.14252 | -42.7567 | 2026-08-25 03:30:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c503c322-d6b6-3d5a-b7ca-2bf034b9f33f | -7.26948 | -45.36517 | 2026-08-25 03:30:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| a4827b06-7ba8-3a3a-ab4f-b120796d665d | -7.29184 | -45.36982 | 2026-08-25 03:30:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 01e2ddf7-8b82-3d86-8c0b-af2fc6e8f8dd | -7.14323 | -42.75275 | 2026-08-25 03:30:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 163b8b60-e5de-3088-802d-75ae667c6327 | -7.4316 | -43.11196 | 2026-08-25 03:30:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1b0b2b29-3ca7-32fd-9958-e722625e4412 | -4.46316 | -38.51057 | 2026-08-25 03:30:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6fa8e51b-0d18-3e9b-a070-031cff77e8e1 | -7.43905 | -43.10426 | 2026-08-25 03:30:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 9bb400a9-a990-31db-aded-636bbbfec86f | -7.19225 | -42.74774 | 2026-08-25 03:30:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1bf6080b-86e1-3ad8-9ffc-822959828fd5 | -7.28325 | -44.07471 | 2026-08-25 03:30:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| b95b617b-1d84-3970-9485-dfef7c96251f | -7.27698 | -44.07363 | 2026-08-25 03:30:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 4e4a1148-1311-3d9f-8963-121350be48fe | -7.27951 | -45.36115 | 2026-08-25 03:30:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| ab4019ac-74a1-3899-94d3-2ed73c3839b1 | -7.3126 | -42.97418 | 2026-08-25 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| b6bdb122-e760-3952-8ba6-010afe336981 | -6.47977 | -37.08972 | 2026-08-25 03:30:00 | NOAA-21 | CAICÓ | RIO GRANDE DO NORTE | Brasil | 2402006 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ba660cda-ccd7-3e4a-b2f2-9a008399f89c | -7.30055 | -43.00724 | 2026-08-25 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 20155476-8760-3dba-a266-3a325f0dbcf3 | -7.43672 | -43.11724 | 2026-08-25 03:30:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |


[Clique aqui para ver as próximas entradas](README17.md)
