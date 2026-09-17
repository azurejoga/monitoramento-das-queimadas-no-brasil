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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b666b229-a5e4-30ac-95b3-adba7b3a33f0 | -9.90927 | -46.51598 | 2026-09-17 04:40:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 01a4efbc-cc83-3f33-93b7-92cfa1adb984 | -9.18709 | -46.75653 | 2026-09-17 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 97755d4a-5874-3803-8ab4-743c53fc1a93 | -5.48335 | -45.13184 | 2026-09-17 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9322ea0d-5f5b-3d0f-b455-8ef6e761b30a | -6.1204 | -51.70607 | 2026-09-17 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2b530c9c-d0b6-3900-9955-dcc3b1fceff5 | -9.48033 | -47.2332 | 2026-09-17 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 80018d96-f5d7-3c81-9c73-d3e00d47d15d | -9.94375 | -45.44818 | 2026-09-17 04:40:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 610a6617-cd2f-390a-a2e8-8eb30678d1f1 | -5.86239 | -52.12349 | 2026-09-17 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8c7d21e8-bc43-3716-96d3-93043e5474b2 | -7.08032 | -41.77368 | 2026-09-17 04:40:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| e5dd3ab5-9a2b-30b2-9a8f-bb96fbfbfbe3 | -6.75603 | -55.8472 | 2026-09-17 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2573d6d2-5ff9-3ed8-858c-61ae51b40d1b | -6.1583 | -55.71415 | 2026-09-17 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d5db3448-6f3a-3236-a570-197d7a7e49f8 | -9.61174 | -45.35781 | 2026-09-17 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 13ba3da8-ceb2-3ab0-9ea1-e80c9fb7aa9c | -7.08795 | -43.47396 | 2026-09-17 04:40:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 28fed7bf-b3f8-3bce-bbcc-45eff9f6ea95 | -10.78895 | -46.1963 | 2026-09-17 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 665b0dde-df96-3dfd-8ad4-eef6b15634ed | -8.73494 | -45.33695 | 2026-09-17 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0c817f22-ba6f-3d0e-a014-d84dd33b5f47 | -10.986 | -48.30601 | 2026-09-17 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a3057f02-bdbf-3a4a-96d3-788862109c7f | -8.69418 | -44.87426 | 2026-09-17 04:40:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 140442b9-5306-3da9-8fad-397400b3902e | -9.36819 | -50.26739 | 2026-09-17 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b1bfa61-425b-3792-9941-75ff3cb0b2d5 | -7.72517 | -42.50416 | 2026-09-17 04:40:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 3c687a61-0062-315f-9b49-e315a7614eeb | -11.49133 | -45.73975 | 2026-09-17 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 39da992a-4f7c-3bba-8a58-ecc03bf64a93 | -10.54374 | -44.85432 | 2026-09-17 04:40:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 989d163a-c4d4-39b1-9f92-d337873b0eca | -9.3601 | -50.34092 | 2026-09-17 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5fcbbb8a-d728-3dc0-9220-ba06d835c82d | -7.37611 | -44.52372 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0844de02-bc15-3db2-8f12-cf39496d1b5c | -7.35729 | -44.4789 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fd984047-5f36-3138-847a-4161be073abd | -11.34504 | -43.98869 | 2026-09-17 04:40:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 778248e3-f04f-301b-b9d4-523788658d34 | -9.61527 | -45.36191 | 2026-09-17 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b1f08586-3a9d-33a8-8a21-065413261723 | -9.86871 | -48.3496 | 2026-09-17 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 61993e28-4802-3dad-9699-f00e61dbb76f | -7.04343 | -42.06718 | 2026-09-17 04:40:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| e0ff803d-04cc-3e72-a655-c512695b7efc | -7.09179 | -41.7638 | 2026-09-17 04:40:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 05612828-41d5-3ade-8d7b-b4f8299a67b6 | -5.15718 | -55.93853 | 2026-09-17 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 12dd4509-0120-37a4-81e1-b8e919bc2725 | -6.88177 | -45.46787 | 2026-09-17 04:40:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7b3dc7dd-f7c9-32a0-83af-72787f444425 | -3.64422 | -58.5603 | 2026-09-17 04:40:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8eedb7e0-2657-3422-9dc1-8a8e38dfe4d8 | -8.0974 | -61.82293 | 2026-09-17 04:40:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1960ad5f-6c79-3c5e-945f-e181321a8413 | -11.48072 | -45.77421 | 2026-09-17 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 168e687e-5af8-389d-8ae8-95fc2e06485a | -8.27064 | -42.16491 | 2026-09-17 04:40:00 | NOAA-21 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 7b26c7d2-16a2-3c34-ae8e-169ee4696ecd | -8.86519 | -44.89906 | 2026-09-17 04:40:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e6c771ea-5052-34ab-823d-47e68ce4d0f1 | -11.33035 | -46.77184 | 2026-09-17 04:40:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ddab2f81-d023-3bab-be4a-c721a23cff37 | -9.83324 | -48.35196 | 2026-09-17 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8a1115cd-c21c-3d44-91fc-003d39546803 | -11.78967 | -47.70669 | 2026-09-17 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4bac7cff-4ca8-35ff-8805-8413acfa994d | -9.49017 | -45.42568 | 2026-09-17 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bdf0a2d3-d305-34c8-ac94-329e7d03b2b9 | -7.2769 | -44.21103 | 2026-09-17 04:40:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a411c4bb-3c87-3a75-ac98-f06dc8130019 | -9.11222 | -45.7188 | 2026-09-17 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 677d95b1-87da-351e-a01f-a22f61159186 | -7.3818 | -44.51321 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 837b56c2-8600-335b-b455-3d34cff31454 | -4.1039 | -56.34598 | 2026-09-17 04:40:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 605dd428-4f3b-336d-9e23-69105dfa2a57 | -6.83474 | -58.98383 | 2026-09-17 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c3704f9-e145-344e-8f9c-9f15d7751696 | -5.54548 | -46.59238 | 2026-09-17 04:40:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e93ea128-fd42-30fc-89c6-f90abbe60eab | -4.88184 | -56.06488 | 2026-09-17 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1736492c-ec03-3ef9-bcd3-ffae2c894907 | -8.47267 | -44.55949 | 2026-09-17 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| e2315156-f424-3218-bad3-61f5ab769e5f | -8.58315 | -44.57145 | 2026-09-17 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0982a29a-2b5d-3b23-b469-fdc31e404f74 | -6.8209 | -41.10897 | 2026-09-17 04:40:00 | NOAA-21 | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bd510c12-46b3-3e9d-8744-f085ab167392 | -11.48562 | -45.78223 | 2026-09-17 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a96731c-20a3-3b2b-b480-6fa92ff73b78 | -7.14291 | -42.15907 | 2026-09-17 04:40:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| b60cdf1e-d537-3a38-ba20-6d844095ffc6 | -8.94401 | -44.40206 | 2026-09-17 04:40:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0545e404-9d8f-3a84-a324-06da7d2f790e | -6.75415 | -55.84799 | 2026-09-17 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3c88422-aeef-3327-8065-c0b0957cb1e7 | -9.555 | -45.42743 | 2026-09-17 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 780aec66-8a68-32fa-ab42-97cdb6c06fe1 | -7.04572 | -42.0512 | 2026-09-17 04:40:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 75b9615e-d406-3907-b1de-0ab96005685b | -11.33412 | -46.77229 | 2026-09-17 04:40:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 41eef635-f135-3fc0-990d-06f45291fb23 | -7.51311 | -47.49324 | 2026-09-17 04:40:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d8e3fae2-abc5-3908-9e22-8f8391398f86 | -6.76842 | -42.77479 | 2026-09-17 04:40:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| c2a579bb-2cf2-3faf-b957-26c0502b383d | -7.03238 | -42.03396 | 2026-09-17 04:40:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 541a33ca-24d0-3c47-bad8-c664633d9677 | -8.84214 | -46.91996 | 2026-09-17 04:40:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 044da19d-47fe-311f-b8a8-fc9b226850ba | -6.9993 | -43.33595 | 2026-09-17 04:40:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6da8d1ca-c805-3ea7-87ce-50e239f2fc74 | -5.83855 | -52.08752 | 2026-09-17 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cdda1c35-ab02-36de-beff-174f64c4bc5f | -7.02829 | -42.06976 | 2026-09-17 04:40:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| c59cd9f1-c8cc-316b-ab24-5c532f812d95 | -11.57027 | -46.88399 | 2026-09-17 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a17b9a86-0015-33ae-bc94-30f114bfbe41 | -8.78476 | -46.90023 | 2026-09-17 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 35a78827-1067-3795-a746-de15c52c6af6 | -3.48861 | -54.72145 | 2026-09-17 04:40:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 857d96bd-4060-3893-acd9-68f75ad31571 | -6.70536 | -59.46046 | 2026-09-17 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1743e5f3-c231-3ff7-9acd-4535a1478527 | -8.53244 | -44.49836 | 2026-09-17 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5f413d65-3ff0-36ce-b512-6ba0fb01461e | -8.87127 | -44.91489 | 2026-09-17 04:40:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9d7dae77-162d-3959-b312-e129149dd2c2 | -8.46432 | -44.55856 | 2026-09-17 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3556599e-7a86-35d5-b96c-1e635b901449 | -11.89363 | -47.60873 | 2026-09-17 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2c1523c9-0f54-3f3f-b81d-27fd89b31a62 | -8.11735 | -54.80511 | 2026-09-17 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 90cb3321-cb0b-3d69-b3f1-f3ffcd6cd259 | -9.84097 | -50.50742 | 2026-09-17 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3cfe162a-4625-34a3-9081-22080f55fa70 | -11.57467 | -46.87992 | 2026-09-17 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6e97b8b1-b525-3cbf-9ea8-7ca667808806 | -7.57998 | -44.92598 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c81fa9f6-3d5c-367e-8afe-2db78cbfc6e4 | -6.82605 | -41.10963 | 2026-09-17 04:40:00 | NOAA-21 | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bed62576-047b-3247-9f1e-59f36f1fafe5 | -9.90246 | -46.50998 | 2026-09-17 04:40:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e1d9c322-70ad-34f6-9023-73e97114179a | -8.78414 | -46.90439 | 2026-09-17 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 31afcb9f-8724-3fe1-8158-7f96de18b028 | -8.78837 | -46.90083 | 2026-09-17 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3293816b-da8c-3df5-a660-1d51f317f4a9 | -4.51286 | -54.96072 | 2026-09-17 04:40:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9b69b0a5-2f5f-372e-aeb5-698b2b184552 | -7.36192 | -44.47585 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 00d5efcc-749d-3f5f-a137-7cb1da5572f0 | -8.85756 | -44.89402 | 2026-09-17 04:40:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c3bcfb40-9894-34d2-9e5b-2314e101aeb1 | -4.54424 | -54.92886 | 2026-09-17 04:40:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| d7e75752-1b14-35b8-b02d-394fa997324a | -11.59236 | -47.31083 | 2026-09-17 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bd386791-cd08-39e2-9e52-a37626035ccf | -7.50038 | -44.91061 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f107434b-a961-3b52-b07f-e96e5e8dca52 | -10.11399 | -45.57391 | 2026-09-17 04:40:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4c5e9241-545b-3040-818f-4a9469f7dc5d | -4.38709 | -56.34829 | 2026-09-17 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a50971c5-a123-342d-ad76-facb0ada67c8 | -7.8355 | -44.85556 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5b493c3d-41f0-3887-adee-90513b07b5e0 | -6.3582 | -58.28337 | 2026-09-17 04:40:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 32a0e883-334e-3b9b-9819-86d97b0169b2 | -8.41145 | -54.73148 | 2026-09-17 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bff4b352-f5d5-3761-a532-86c971e50bd2 | -9.26361 | -49.11954 | 2026-09-17 04:40:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1047cad8-12fb-3ce5-80be-b61497f8263b | -4.48953 | -55.49788 | 2026-09-17 04:40:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7b1dfd68-96d2-32f8-ac65-b5794cde378b | -5.14328 | -47.60312 | 2026-09-17 04:40:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6c2912e7-5caf-3b8e-9df6-8df4c3d04418 | -11.01763 | -44.48504 | 2026-09-17 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| da6d377c-d82a-3bac-922f-208b66937287 | -12.32164 | -47.95489 | 2026-09-17 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2e47593b-2ace-33a4-bad4-f30a18ff1007 | -8.60855 | -44.51239 | 2026-09-17 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c1f767af-e07e-3fdc-940c-aa2b079dac44 | -11.35818 | -44.02781 | 2026-09-17 04:40:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 75ddb560-69b8-3fe0-b5de-3b2f40691b8c | -8.5272 | -44.51535 | 2026-09-17 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d7df90b0-a329-3063-a344-107614342bd8 | -5.79808 | -42.54534 | 2026-09-17 04:40:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fbcd6a38-5b2a-371c-ab0c-f11e3806538f | -7.17852 | -42.11127 | 2026-09-17 04:40:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |


[Clique aqui para ver as próximas entradas](README49.md)
