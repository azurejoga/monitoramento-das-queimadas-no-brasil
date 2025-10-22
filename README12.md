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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f6aa3cdc-805d-3487-8674-1e0b8921510a | -2.51666 | -51.93283 | 2025-10-22 04:53:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 030f843d-0c31-301e-944a-9016654abb8f | -3.87549 | -47.99678 | 2025-10-22 04:53:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6197e8f4-9f42-3f03-9213-3d13e57ad7e8 | -2.96198 | -48.5911 | 2025-10-22 04:53:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 73764928-c4c3-31c7-bc88-c69eaa71c75e | -3.3317 | -50.75058 | 2025-10-22 04:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7af5e2c-df62-3389-92d4-0a6f878dae4b | -3.0388 | -49.52491 | 2025-10-22 04:53:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84edbf82-fcb5-3ac7-ab1f-f9a96596f257 | -5.97564 | -46.60733 | 2025-10-22 04:53:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0c960f2e-3409-30e7-9392-f3aef2603432 | -3.25006 | -50.13466 | 2025-10-22 04:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 00301f9a-5fe7-3171-afcc-c06573faaeb0 | -2.44314 | -49.37373 | 2025-10-22 04:53:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d96e6b76-debf-3b2a-9446-43815ad5e1ef | -3.44743 | -41.85017 | 2025-10-22 04:53:00 | NPP-375D | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 961266ce-d3cc-3f5d-8c30-781c074867ca | -3.99453 | -43.28233 | 2025-10-22 04:53:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8469143f-1805-3f9b-85a8-685eef163f38 | -3.24721 | -50.13045 | 2025-10-22 04:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ef83ac03-4730-339d-8915-2acf4f7c5c38 | -2.02957 | -56.88329 | 2025-10-22 04:53:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f056a21c-7203-3d2c-8987-ae52f234c0c8 | -5.7345 | -46.45675 | 2025-10-22 04:53:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8f2ae7a7-6f0a-3c10-8340-1c89b1ce843f | -2.94907 | -49.3409 | 2025-10-22 04:53:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fa1a60cc-f510-3fda-a068-1fbcbc1f38e1 | -2.03893 | -56.62198 | 2025-10-22 04:53:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4dcef47c-5e1e-37cb-aa09-16b4b666ec31 | -3.66917 | -50.28838 | 2025-10-22 04:53:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fd1b0ba5-2b85-3a30-9dee-e2e4a98e58ff | -3.25407 | -50.1315 | 2025-10-22 04:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f13983e-18a7-3f3c-bc07-2d006222688e | -3.25122 | -50.12729 | 2025-10-22 04:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4e182049-3172-356c-b0a9-a06a7621b605 | -3.02168 | -49.45098 | 2025-10-22 04:53:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 48e37730-6dee-3811-9a0a-a019d7f1fc13 | -3.33226 | -50.74702 | 2025-10-22 04:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5734bd0-bc04-3d5c-bb0a-bfcdc3e623ab | -4.65516 | -48.69482 | 2025-10-22 04:53:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 227b5a3b-0b32-31e3-849a-d06ac7c66b1b | -3.23737 | -42.07456 | 2025-10-22 04:53:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5b593c59-0941-32d2-b70d-ab2e8b83a052 | -3.99104 | -48.32638 | 2025-10-22 04:53:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26c29428-dc4b-3b8f-bc52-69dfcca0b988 | -3.94283 | -48.08582 | 2025-10-22 04:53:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d2b8a031-5b04-35ae-bd90-6185d29a4fae | -2.92783 | -48.29939 | 2025-10-22 04:53:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 4dc3d365-5786-3cf4-b402-09c1e06de3fc | -2.92617 | -48.3013 | 2025-10-22 04:53:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| a68eb569-53f3-3bc2-a74f-a78c7a2d17e8 | -3.04352 | -49.51774 | 2025-10-22 04:53:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 19dc299a-2b45-3ba9-87ad-a4bbd8114819 | -2.25389 | -51.92368 | 2025-10-22 04:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| dccab584-12b4-3e22-ab86-d0f827dfec01 | -6.52918 | -41.43777 | 2025-10-22 04:53:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b9c27be9-0dc9-3e91-9fc5-c5b10d823ce6 | -2.25721 | -51.92419 | 2025-10-22 04:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 215dc83d-1c15-3a95-b4c0-dfdc238f1e54 | -2.27055 | -57.01467 | 2025-10-22 04:53:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 56cf714b-f612-335b-b9d6-473c4bde13c0 | -4.2835 | -48.25357 | 2025-10-22 04:53:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1ac552e9-3c46-3752-8c0d-a8764b84b770 | -3.02628 | -49.46751 | 2025-10-22 04:53:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bf26da23-cb23-36f6-b6f0-de4715f82e45 | -2.25112 | -51.91971 | 2025-10-22 04:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ee299b4e-da04-3732-89d2-aace00f73e45 | -1.52747 | -52.6225 | 2025-10-22 04:53:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a2a08a7-4b77-31b1-8f4e-8e3aaca6b314 | -3.14818 | -49.47334 | 2025-10-22 04:53:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 34dcddcf-17a0-3e8d-8bf7-f63b90f9cb44 | -3.23171 | -42.07382 | 2025-10-22 04:53:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 972ac9ac-a6f6-39f6-a7a7-1177786ea339 | -2.3629 | -47.9837 | 2025-10-22 04:53:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d4ec8e66-36fb-3f75-b1d7-ad038291f7e2 | -3.339 | -50.74807 | 2025-10-22 04:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c7a6f61f-76d9-3e54-b3b1-a4c8d88184e8 | -2.25057 | -51.92316 | 2025-10-22 04:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ba7ba609-abc4-3797-9abb-ef78d22662bf | -6.53653 | -44.36157 | 2025-10-22 04:53:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8a99f279-33c1-357a-b231-14c0c38c5cf5 | -3.03941 | -49.52105 | 2025-10-22 04:53:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 03d501f5-9d5e-383e-bbe2-7cafba9a2aa6 | -3.02398 | -49.45926 | 2025-10-22 04:53:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ff6f583f-e3e3-3825-8dae-44ed1d936ee0 | -3.02338 | -49.46312 | 2025-10-22 04:53:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b9237c50-30af-3201-9e28-e01426a03bc9 | -3.81765 | -47.41221 | 2025-10-22 04:53:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e83b19b7-4799-3159-a68e-81fcd79877fe | -4.39789 | -43.30082 | 2025-10-22 04:53:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 64d1c736-1632-33bb-a658-326365a1c764 | -3.99486 | -43.2828 | 2025-10-22 04:53:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d24ed995-115d-380d-97a3-42ee9a7655d6 | -3.40741 | -46.90434 | 2025-10-22 04:53:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d0b7ba81-0709-3bbe-9010-809137a19d22 | -3.0561 | -49.55813 | 2025-10-22 04:53:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e77054d-058d-3428-9002-6b42ca846b1b | -2.36544 | -47.64963 | 2025-10-22 04:53:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 17bf5e2c-8916-3b88-9936-9221435e9ed2 | -4.29712 | -49.96839 | 2025-10-22 04:53:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef0a8d52-a8b9-3f9b-9ac5-84efba041e15 | -3.38606 | -50.26749 | 2025-10-22 04:53:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| acb14853-d5bc-300b-829a-dd4d8efb8125 | -2.94845 | -49.34484 | 2025-10-22 04:53:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b5b3b85-f842-3f4b-8084-f10134269318 | -3.99075 | -48.32853 | 2025-10-22 04:53:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b3b05a7-5173-3df8-9b5c-45c5c7faedd4 | -6.34958 | -47.50007 | 2025-10-22 04:53:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 90915aca-4002-3fb1-86df-1ca8ab43a967 | -2.35984 | -47.9786 | 2025-10-22 04:53:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 940a4314-e1d6-31a9-bda7-b839d9b2c456 | -4.45343 | -43.24563 | 2025-10-22 04:53:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| f48b6cea-f2ee-30fd-a749-c00ead833c02 | -4.45485 | -43.23574 | 2025-10-22 04:53:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 1de3dac0-3faa-3f0e-9800-cf92508dc4f4 | -5.97217 | -46.61047 | 2025-10-22 04:53:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 56ac5265-1cd8-35ef-84f0-12cfe486207f | -4.03262 | -50.46329 | 2025-10-22 04:53:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e73d4e84-9078-32e8-82c1-588e32eb267d | -2.77285 | -48.58538 | 2025-10-22 04:53:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4fb48b94-631a-32ab-b1fa-4b0a0919e26d | -3.99499 | -43.27911 | 2025-10-22 04:53:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0cf3f1c1-3a96-3f52-ba5d-0561833a0f3e | -3.51969 | -49.44725 | 2025-10-22 04:53:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45ed4482-0195-397b-9d83-ffaf6afd5ef0 | -3.33507 | -50.75109 | 2025-10-22 04:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eceea919-bafe-33a2-b401-625d02872f25 | -2.27523 | -57.01176 | 2025-10-22 04:53:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ad8ebd5-d7df-3cd6-b24b-bde015fb801e | -4.15575 | -40.91305 | 2025-10-22 04:53:00 | NPP-375D | CARNAUBAL | CEARÁ | Brasil | 2303402 | 23 | 33 | nan | nan | nan | Caatinga | 6.4 |
| ae7c63de-1a7a-3741-bb4b-cd824e5009fb | -4.07142 | -47.31033 | 2025-10-22 04:53:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ccf5a7f5-f177-335a-80a5-b073758ffc02 | -2.77221 | -48.58959 | 2025-10-22 04:53:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 89bcfc2f-35d9-3416-b311-592b350e4b5e | -4.22649 | -47.21268 | 2025-10-22 04:53:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 65983810-1a25-3181-9061-7fdd7fef72aa | -3.56832 | -49.48283 | 2025-10-22 04:53:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 78645f64-ffb6-325b-a64b-e37d0218df24 | -3.99534 | -43.27958 | 2025-10-22 04:53:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d4dc52a8-b5e5-3d2f-9884-b38679642057 | -1.89872 | -54.07174 | 2025-10-22 04:53:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7654a30-6865-3d33-bff3-616a6bd7599c | -3.57153 | -49.43913 | 2025-10-22 04:53:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a393556-d963-3cc9-801d-d00332269688 | -3.25349 | -50.13519 | 2025-10-22 04:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 03ac17aa-e8fb-3f68-80a5-82bdd0f82b1a | -1.87075 | -54.49623 | 2025-10-22 04:53:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0d743371-b34a-3bc5-897f-bbcc93ab200d | -3.49933 | -51.10617 | 2025-10-22 04:53:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c92c5846-c509-3d5c-8cb6-9ea53eacedae | -4.15562 | -40.90981 | 2025-10-22 04:53:00 | NPP-375D | CARNAUBAL | CEARÁ | Brasil | 2303402 | 23 | 33 | nan | nan | nan | Caatinga | 19.4 |
| ef54946c-f8f0-34a9-83b2-5039e84c2fda | -2.25667 | -51.92765 | 2025-10-22 04:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 48bed3db-20c8-33ca-b53d-a357d15b6bef | -4.15026 | -40.90765 | 2025-10-22 04:53:00 | NPP-375D | CARNAUBAL | CEARÁ | Brasil | 2303402 | 23 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 7deed583-ef16-3bf1-9873-0340e3593a34 | -0.33463 | -51.7991 | 2025-10-22 04:53:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ae3fd66-fa7c-3dfe-af4e-3275c8707cf9 | -5.52179 | -50.41707 | 2025-10-22 04:53:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 97bbc92e-3a26-331a-857c-4e22b697b800 | -4.39213 | -43.30324 | 2025-10-22 04:53:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8ca0bb58-1cf6-3f96-b7f0-993ad42d3434 | -4.45532 | -43.23244 | 2025-10-22 04:53:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 4adf8498-bcad-3fde-8b6e-4e2a888b522c | -5.51656 | -47.42168 | 2025-10-22 04:53:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4c71f405-291e-3432-8ce1-d6e8b37f756e | -2.18671 | -54.4808 | 2025-10-22 04:53:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bb7cc8de-b106-3b3b-9a80-d6a4ef6cc1b7 | -1.49036 | -47.81295 | 2025-10-22 04:53:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d5f3f20b-8949-3be0-a474-c0b520b8de34 | -4.4539 | -43.24233 | 2025-10-22 04:53:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| c4f208eb-f84b-332b-a99b-9732016f8165 | -3.03815 | -49.43763 | 2025-10-22 04:53:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 6215a777-2fec-3926-8612-b16157d0d2db | -3.57506 | -49.43967 | 2025-10-22 04:53:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ecad3f0-669a-38ce-9539-cdf8bb8b7a58 | -3.94213 | -48.0905 | 2025-10-22 04:53:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f25eef18-2ee8-3d37-887c-59324a0bcaef | -2.92717 | -48.30377 | 2025-10-22 04:53:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 0ca287df-d2d2-342c-9941-c6fca1c30dd3 | -3.02689 | -49.46365 | 2025-10-22 04:53:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a4e7984f-ccc1-31d5-afba-e0454d438977 | -3.24949 | -50.13834 | 2025-10-22 04:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5f7a7cb7-46fe-3b77-8745-c8217721dbfa | -1.49096 | -47.81157 | 2025-10-22 04:53:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8c0b16a5-16a2-318d-ae81-b3cd533473ca | -2.36359 | -47.97917 | 2025-10-22 04:53:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c80a03ee-a4a8-307d-9436-35aa3ada4202 | -5.70728 | -49.3144 | 2025-10-22 04:53:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9735cc7f-61eb-3959-92c6-df3079cccd60 | -4.45579 | -43.22915 | 2025-10-22 04:53:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cd1e64e4-5a2d-38ae-a81f-4c2161914b89 | -4.39261 | -43.3 | 2025-10-22 04:53:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2b49db72-76d6-30a2-a070-38dd9d1feb23 | -3.15169 | -49.47387 | 2025-10-22 04:53:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3d794360-8ecc-3c36-8db6-61ef23567a5c | -3.24664 | -50.13412 | 2025-10-22 04:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README13.md)
