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
| 791d193b-4801-3914-9a3a-99b42381ba1f | -7.63848 | -47.18545 | 2026-09-13 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1e7a7b9b-809d-3ed9-870a-e006bc1fb275 | -3.22624 | -43.04082 | 2026-09-13 04:14:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e2bec431-8e1a-3088-800c-fdb7d0cb1272 | -7.46872 | -46.14889 | 2026-09-13 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8d6948ba-2047-3943-8b3e-b19ad195a31e | -2.96322 | -50.40703 | 2026-09-13 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d5ef6b1b-40ad-34e5-99e1-5993880bb7a4 | -3.87531 | -51.18181 | 2026-09-13 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e1faf0c2-bd99-3996-aec5-ed0798546ec1 | -7.01902 | -44.62184 | 2026-09-13 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 69990b40-b396-3db3-a0fa-32b308214223 | -6.23383 | -43.51497 | 2026-09-13 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7f57b1cc-8c56-3396-ac01-3859cfe8db62 | -5.18013 | -49.35116 | 2026-09-13 04:14:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14dc5dcf-c408-34e4-a062-322f07909fd4 | -2.01957 | -47.55219 | 2026-09-13 04:14:00 | NOAA-21 | MÃE DO RIO | PARÁ | Brasil | 1504059 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 568b6d08-278b-37ca-aabd-55f0f0351135 | -5.81016 | -53.80508 | 2026-09-13 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb3b4347-96ec-3e09-a18d-f8d43e8459f0 | -5.987 | -44.8422 | 2026-09-13 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f7dfdacc-77cc-3b04-9855-d0c815dfad08 | -2.96583 | -50.4051 | 2026-09-13 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 76aae0e3-62cd-34d6-ac6a-3e43495ccbb0 | -7.3495 | -45.37023 | 2026-09-13 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9ed48df7-ce38-3613-a412-2d02c09084b6 | -5.48178 | -45.60051 | 2026-09-13 04:14:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0b4572fc-d546-3641-a007-2a10eaa7ea17 | -7.31748 | -45.30807 | 2026-09-13 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 851f8d00-cd40-365b-86e0-450ea09d9606 | -3.04386 | -51.25554 | 2026-09-13 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d3c208be-9f36-390e-a9ed-964f7ee57edc | -5.76424 | -45.09405 | 2026-09-13 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ef8c59f5-53df-3b57-8aea-82212172d198 | -5.20117 | -49.33275 | 2026-09-13 04:14:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| df153638-6aba-3b10-89f0-195d4f10945b | -2.82665 | -49.2373 | 2026-09-13 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| afa43998-8580-3615-9742-26ccf7067626 | -8.74696 | -46.43393 | 2026-09-13 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3840cb72-f7a1-346c-a62a-3f763d3618b7 | -2.94135 | -50.38668 | 2026-09-13 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2a96a095-b635-39cc-a6e5-753690298750 | -2.82585 | -49.23341 | 2026-09-13 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1d6a1b4e-f518-3346-b503-e7b06add906c | -7.10904 | -42.10616 | 2026-09-13 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4cc981a0-f34a-3ee4-ba0a-55ed0f9c21f6 | -2.95428 | -50.40004 | 2026-09-13 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2d91b2bd-8121-3540-adc8-2252013aead7 | -7.3701 | -45.35063 | 2026-09-13 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dab74090-20ac-34b6-b01c-89bd1c5cd1ff | -6.17914 | -44.01513 | 2026-09-13 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 711cd59b-03fd-3997-9ad4-17bb5a76ff66 | -7.51602 | -47.33603 | 2026-09-13 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 604b1ff4-f7a8-305e-b52b-da64f50bbd54 | -7.02124 | -44.62948 | 2026-09-13 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e48d69c3-7d80-3448-a247-d1e56ef31dba | -7.17137 | -43.89462 | 2026-09-13 04:14:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b5c20385-98aa-3981-bb5a-8db27bfc42d2 | -2.79854 | -49.4054 | 2026-09-13 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e2df09b9-b0c9-379f-88c3-8263e3419214 | -7.37409 | -45.3509 | 2026-09-13 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 91cc9b85-52b3-3950-83fd-b37f3d52c10c | -4.65717 | -42.43702 | 2026-09-13 04:14:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 272f57b8-d11b-35a2-a686-402d35889fe2 | -6.5088 | -47.59739 | 2026-09-13 04:14:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7ae2520e-ebe2-35ba-8731-51a2e3d15cec | -6.22709 | -51.69117 | 2026-09-13 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| da2a59ff-0850-3241-baa4-894f4f8bedb4 | -7.01567 | -44.62131 | 2026-09-13 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e976c161-7c46-3a99-942a-6cba7396aedc | -2.11559 | -47.11285 | 2026-09-13 04:14:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b245deb-9a45-3fd2-97da-fa7f5b3ecd0c | -8.92346 | -45.43612 | 2026-09-13 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 684e704c-2bd2-3a10-946e-234b2cc6ba44 | -6.08658 | -51.7557 | 2026-09-13 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 628246ea-32fa-3ada-a0e0-d2b133291867 | -7.20344 | -45.92646 | 2026-09-13 04:14:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dc81c74c-d323-32c8-99f1-a16992bd662e | -2.53704 | -54.65689 | 2026-09-13 04:14:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| ae07fabb-48c8-3dc1-b69c-06a7924690ea | -5.13875 | -44.59 | 2026-09-13 04:14:00 | NOAA-21 | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d666d6f2-52d5-3fe9-8c45-2e011918d75a | -2.47268 | -48.04224 | 2026-09-13 04:14:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5486a120-8cfa-3e20-8640-3bfa4340f9fc | -5.20556 | -49.33347 | 2026-09-13 04:14:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ab288090-8861-3fcf-840d-9baf45ca56db | -6.2402 | -51.70577 | 2026-09-13 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98373691-9010-3829-aa95-5a3895abb082 | -4.02057 | -52.0827 | 2026-09-13 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 33d8e4f6-02be-3d63-aa40-c58e2d2e1950 | -2.95516 | -50.39457 | 2026-09-13 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ccbdef57-66bf-3a25-bbac-4625d2465b8c | -7.47292 | -42.12111 | 2026-09-13 04:14:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5be3a183-abf9-3922-9e9f-1862c2f0195e | -1.22348 | -54.12845 | 2026-09-13 04:14:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7a5f5c25-4fe5-3fa6-8738-388c76a503ef | -2.95111 | -50.40283 | 2026-09-13 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 40e62218-1952-3f5b-89d6-2ead1deade5f | -3.87433 | -51.18771 | 2026-09-13 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 696eb97c-b8fe-3c0f-a72d-e41568c0f614 | -3.78996 | -48.93302 | 2026-09-13 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 500e8f0a-3d72-3bff-9af9-8876d6c7a06c | -7.28701 | -50.78291 | 2026-09-13 04:14:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c9d5b6c9-f508-36fb-b7dd-42fcfce89c91 | -6.76599 | -45.46207 | 2026-09-13 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c3b39a01-b468-378f-8c3a-a1a91747ab5f | -5.1876 | -49.27806 | 2026-09-13 04:14:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 60cd2167-cb04-3a70-b7d9-458c3a38e366 | -3.70883 | -45.3876 | 2026-09-13 04:14:00 | NOAA-21 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d423a2a2-f80a-30fa-bc25-b2b952c4297d | -6.2332 | -51.68608 | 2026-09-13 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc58e999-b395-37d7-aa1c-64125ac76b43 | -6.80461 | -44.81876 | 2026-09-13 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e1204866-b751-3057-bad4-18e8f5d77cca | -6.24578 | -51.70374 | 2026-09-13 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1fc7157f-c0b4-3ae1-8c55-4fdee7e0418f | -6.51924 | -42.09233 | 2026-09-13 04:14:00 | NOAA-21 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8f152e4c-e464-39c6-a0fe-31574d38cc12 | -7.47346 | -42.1175 | 2026-09-13 04:14:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8f337ead-1eae-3ba0-8d48-1694f5c7c2a6 | -6.00108 | -44.2608 | 2026-09-13 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 63c1edcf-4dae-3a90-9217-0f1ca94d1b60 | -8.21248 | -47.8681 | 2026-09-13 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ba2d0f59-5ea4-3126-beff-b3aa3982d62b | -7.34437 | -46.01671 | 2026-09-13 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0085ef7d-1f5e-33ca-a8ca-02d6f2b708e2 | -7.0218 | -44.62593 | 2026-09-13 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 24a4698e-b9f1-329f-91a8-efb61b48933a | -4.92805 | -45.83643 | 2026-09-13 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 11.2 |
| e5881944-d114-3d44-bda9-8cf4c3a29371 | -7.46674 | -42.11645 | 2026-09-13 04:14:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 7e3314cc-3d36-3bb4-8032-b8b41115b892 | -5.05514 | -42.94051 | 2026-09-13 04:14:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 712a67cb-26f6-3320-a37e-5899d6742a29 | -3.32899 | -42.29628 | 2026-09-13 04:14:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3a11a65d-1109-363e-a098-fbd4ba475684 | -4.60599 | -46.3181 | 2026-09-13 04:14:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 711e29a0-41d9-3bb0-8d30-a72ea64e3468 | -5.20616 | -49.33198 | 2026-09-13 04:14:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f1f68513-7ced-3dc8-bee9-9b127ccf706e | -4.93199 | -47.71311 | 2026-09-13 04:14:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 10b7c29e-1be5-39a4-ad71-997acc930ad1 | -7.09217 | -43.94266 | 2026-09-13 04:14:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 219fa91c-6355-3257-b0c6-3ed81d7b4cf9 | -7.96592 | -43.98907 | 2026-09-13 04:14:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d56bf412-446f-326f-8366-3481b710da31 | -4.93454 | -47.71578 | 2026-09-13 04:14:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 59de158b-1755-33c6-9bb6-dfa7bac00581 | -6.22307 | -51.68437 | 2026-09-13 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85bb8b98-9fe7-3c39-81ed-b7d5b4eb248f | -2.94448 | -50.39843 | 2026-09-13 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e18e57f6-302b-3cce-92ac-277999c676ed | -4.43916 | -48.94198 | 2026-09-13 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0a586ba8-c5f6-3643-bc3c-bbb57e1d5f56 | -8.28976 | -41.35532 | 2026-09-13 04:14:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| e12dfdd4-e1d0-30b2-b152-2cb8e63e64aa | -2.94672 | -50.4157 | 2026-09-13 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 705af4ed-29cd-37e2-aafe-c2725add053b | -3.2257 | -43.04427 | 2026-09-13 04:14:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2d96f41d-ca76-3650-83ac-857fa5e6c81f | -4.9328 | -47.70801 | 2026-09-13 04:14:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a0c8e276-7ede-3f98-a9e3-af2688ab322e | -3.16104 | -48.61155 | 2026-09-13 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c742a4fa-fc61-3f99-8615-65b61f068942 | -2.95026 | -50.39375 | 2026-09-13 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0daa9ad6-7252-351b-a0fc-997b24302c81 | -7.01733 | -44.63252 | 2026-09-13 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 545e469a-296f-3fa2-9af9-95a1c6e38707 | -2.93645 | -50.38592 | 2026-09-13 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e04518d4-c674-370f-b9d7-def446715a41 | -8.39498 | -47.58739 | 2026-09-13 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 846fd4c2-2e0d-3d9b-9f1d-2c08aba54cfb | -5.74393 | -46.15247 | 2026-09-13 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8fdff609-ecd3-3198-90f3-9f8aa969cc26 | -8.11867 | -42.96399 | 2026-09-13 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| caa51718-9983-3193-85ce-7a5c47c5d076 | -2.9649 | -50.4106 | 2026-09-13 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8f48ae18-c83f-33c0-b2a7-a9a9a6687d82 | -6.72452 | -45.41313 | 2026-09-13 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ca0d1334-55a6-3f6e-8b39-652dfd4742aa | -7.95767 | -43.99845 | 2026-09-13 04:14:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6ad6d0e5-1104-3ac5-9f6c-b29249fd8aec | -2.96812 | -50.40783 | 2026-09-13 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3a932d60-794a-3e48-a707-19efaa5b54b9 | -5.77109 | -45.0951 | 2026-09-13 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a0600e89-4bc5-30d1-b78c-cb302d5a6f41 | -3.22772 | -50.58635 | 2026-09-13 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9a8c3f8e-67af-3166-a2de-04389b786418 | -7.11966 | -42.10413 | 2026-09-13 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4c02232f-1d87-3632-aa31-cdb87c9821a4 | -6.73019 | -45.42166 | 2026-09-13 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 91ce4515-6b1a-35e1-80e3-7d3b749d9880 | -5.11971 | -41.08479 | 2026-09-13 04:14:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d8bbdaa8-401a-372f-8d8f-0f1b3fac6a55 | -2.95295 | -50.39192 | 2026-09-13 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 472294d6-6770-3677-8957-0e64261912e1 | -7.54015 | -44.89899 | 2026-09-13 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 57fdcfaf-5dd4-3922-bcc6-6310855c074d | -7.09711 | -47.54173 | 2026-09-13 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README22.md)
