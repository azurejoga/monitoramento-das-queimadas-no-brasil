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
| 8e5d2072-a3c4-317a-9fa9-d3c69f652447 | -7.64456 | -49.72433 | 2025-09-15 04:49:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fddce334-d0e7-3485-96c0-19ede4d5111f | -7.87248 | -43.57592 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 2d0e7927-2021-3c31-b1a7-73a9aece200e | -8.94093 | -45.79168 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ac793c59-bae2-3537-8aec-16ebfcf42ea4 | -7.88859 | -43.56727 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 23b0c941-0c18-36c8-a47a-1902acff637e | -6.63029 | -44.73419 | 2025-09-15 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6a6c189d-e1ae-3050-a6ff-3a24df42daae | -10.17439 | -46.14782 | 2025-09-15 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d6749e24-c009-3db0-b169-e1a569e8e8b6 | -8.62519 | -46.36976 | 2025-09-15 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d02f8346-9c23-3dbe-b1e5-a71556e5bffe | -9.1682 | -45.58287 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9bb144e5-dc3e-336b-8782-d550fed1c2f5 | -5.85889 | -43.72493 | 2025-09-15 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 25424eae-a0d9-36e7-9a3c-9be1650b943f | -7.88297 | -43.57198 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 67.5 |
| d0d511dc-1194-360b-ba63-e314378d5f3f | -7.06106 | -43.89089 | 2025-09-15 04:49:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b38092d1-a19a-3267-b00e-f0ec8cf1264e | -9.55096 | -45.94204 | 2025-09-15 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf2bf672-fb1c-38d9-8da0-28145629308c | -5.93948 | -43.23157 | 2025-09-15 04:49:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d51d47a3-fdb6-3fa6-8537-a2f1e2559808 | -7.39663 | -49.99768 | 2025-09-15 04:49:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd69ff16-f7e0-3e2d-aa85-e7dc62b5703c | -3.64761 | -54.05674 | 2025-09-15 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ae007590-dfe2-3281-bcda-fe6eb5505f08 | -7.509 | -44.37129 | 2025-09-15 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9b874518-4f83-3560-9f9a-2c168ce58115 | -8.2044 | -45.53762 | 2025-09-15 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8f6a1da0-870b-31ee-b8e1-821f48b4b346 | -7.88372 | -43.58762 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 120.1 |
| e46ca63c-0f35-3458-a567-2c7113782d38 | -8.98728 | -45.76418 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2ea91df6-8acd-335f-9aec-6e0d61134e51 | -7.05259 | -44.13598 | 2025-09-15 04:49:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0f11dd6c-9088-3082-a760-7563578d93db | -6.34206 | -43.164 | 2025-09-15 04:49:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bad3e7ed-4ecd-3f65-8aa2-23c81c9cddf7 | -7.97924 | -45.66918 | 2025-09-15 04:49:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8170a599-9081-3c51-b58e-e6c3a96a3e92 | -7.88527 | -43.57689 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 8a775c7a-a6e0-3639-9f43-4541ab330984 | -7.88859 | -63.69743 | 2025-09-15 04:49:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 26ef7e62-46b6-351a-971b-484e3aae0303 | -8.9209 | -45.46831 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 0a7c289a-c8f3-38b4-a909-438658cec8b6 | -3.83053 | -52.28093 | 2025-09-15 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 501fe772-5077-35d2-9929-4250ea5a3b40 | -7.70344 | -44.67134 | 2025-09-15 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9f3bcb71-0689-3c99-8b95-25ccd55d3c98 | -8.11147 | -50.15924 | 2025-09-15 04:49:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a7900faf-34ae-3f31-8179-4e99563f32f5 | -7.862 | -43.57984 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 48825fd2-3cd9-3c80-8778-1ab6d68b0d49 | -4.79634 | -56.11003 | 2025-09-15 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bec0554b-dd42-30b2-8490-798d8171bc0d | -7.87103 | -43.58665 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 14.9 |
| e5d9852c-b73f-318a-85f7-4cf6d673b497 | -10.90224 | -45.44846 | 2025-09-15 04:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c89888b2-3fb1-37fe-ace6-1ff7dd48f5c5 | -8.09293 | -50.16747 | 2025-09-15 04:49:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e5bb6e65-47b9-377c-ac54-1b3dad7bb7ea | -6.66214 | -45.56317 | 2025-09-15 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| edc2a67e-a496-3ce7-b903-12644b8566d8 | -9.09506 | -44.81304 | 2025-09-15 04:49:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9001a599-8a12-3f98-9c4b-6339e3cbea45 | -6.63784 | -44.74417 | 2025-09-15 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bb7db27d-7c09-3749-a008-73782cae84de | -9.91771 | -50.29372 | 2025-09-15 04:49:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ff2645bc-8359-3840-b5cb-e104f2a3664e | -6.16971 | -41.19861 | 2025-09-15 04:49:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 04fdc4d6-3f36-39ec-a7ba-bee81a8a0737 | -5.64199 | -45.94453 | 2025-09-15 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6e7b68d5-e93c-350d-85ef-5d536f99453b | -8.91913 | -45.48108 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 78e91538-f793-3083-93ff-88de0e73afe6 | -7.97613 | -45.66087 | 2025-09-15 04:49:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3bb349fa-d0b0-30b3-b397-c1533dbb4f89 | -7.35722 | -44.2958 | 2025-09-15 04:49:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 83ab3426-703d-3138-bd4c-0f3969be26ca | -8.91677 | -45.49802 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6e9917f9-d38c-3152-941f-ae1671b201f5 | -6.1995 | -46.43409 | 2025-09-15 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 71b7934b-24b2-324a-a773-c3b8d1e0a9b8 | -7.2219 | -49.59288 | 2025-09-15 04:49:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c6e026cc-dd41-3227-aa80-efb9b8930ed0 | -5.76531 | -52.36563 | 2025-09-15 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 27a3c59c-b7ed-3d79-9b62-b4202d411f6d | -6.34772 | -43.15932 | 2025-09-15 04:49:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d02f0fd4-b80b-32cf-9abb-68801904a45a | -8.42501 | -47.22432 | 2025-09-15 04:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 160b4136-1f5d-378d-8133-93110be8c5e8 | -7.50443 | -44.37048 | 2025-09-15 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e5254d88-b752-3e5e-9e09-f392aedce945 | -7.6744 | -44.48476 | 2025-09-15 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8b3ad74d-72b0-3bff-8780-7425abcdf02d | -10.15747 | -46.14528 | 2025-09-15 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d90a5e1b-330f-3d5f-9b07-02081fe31d00 | -7.87628 | -43.57011 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 4884bb07-0c88-3f00-8b23-145b6b1aca45 | -9.36067 | -45.39116 | 2025-09-15 04:49:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1d5d0df6-86e8-3e40-a6cb-1cc365f7b137 | -6.15596 | -41.18636 | 2025-09-15 04:49:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8f903871-d6c9-35cc-8ba9-f69b1a709cd2 | -7.49148 | -44.68571 | 2025-09-15 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| faccf532-f768-3cf6-9a71-dd1b152118f4 | -6.05208 | -43.56258 | 2025-09-15 04:49:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3da94f02-d016-371e-8f31-338b5f19ab9c | -8.09403 | -50.16037 | 2025-09-15 04:49:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53b85aab-6b45-3bc1-bb98-d63c33a66f03 | -5.7439 | -43.20607 | 2025-09-15 04:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 10d98b01-0eb1-325e-8b82-0bf7947eb56c | -7.39437 | -49.98997 | 2025-09-15 04:49:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 102f822a-ce87-3b61-ae57-adba4ddba930 | -6.76511 | -44.72287 | 2025-09-15 04:49:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bd7fe60c-058e-3b88-8a2b-d3b11c4a214c | -7.49211 | -44.68143 | 2025-09-15 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9c399323-9ab2-356f-91f5-5befdaebd637 | -7.8886 | -43.58833 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 120.1 |
| a8b71fc6-9b1d-3c65-8d05-012dc338aa9b | -6.17118 | -41.19978 | 2025-09-15 04:49:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 327bf7a6-70c2-3af9-8cd0-94c508ccf818 | -7.29933 | -46.57692 | 2025-09-15 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 097a0ab4-83bc-317e-b136-049a6862e50e | -7.87063 | -43.57476 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f1edcceb-079b-349c-bc8c-7c14e9d4ecf0 | -7.89093 | -43.57219 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 1e92ffd9-5b1a-3fb6-ae62-107fbb3d23ae | -5.85819 | -43.72977 | 2025-09-15 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8defdedf-a773-3eeb-bc91-549657b1bb6f | -9.55638 | -48.04664 | 2025-09-15 04:49:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 95b6c35c-a03c-38e0-bbbc-7b7f2036e4e7 | -7.892 | -43.57878 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| f42ad905-706c-35f9-bf39-f26802ac1ebe | -6.97445 | -38.45035 | 2025-09-15 04:49:00 | NPP-375D | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c8e90297-a4b0-3013-86e5-be11e801b381 | -10.88873 | -45.44697 | 2025-09-15 04:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 54b175f8-03df-3222-ab92-43d54e0a6896 | -7.86688 | -43.58056 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 36680742-80a3-35f2-a49e-de2e734102ed | -6.99751 | -44.5633 | 2025-09-15 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9051c71e-a774-3291-bbb4-c177bed028a5 | -8.91502 | -45.51056 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 077de412-7712-38e8-b617-ed125a8fd60f | -10.72762 | -44.77571 | 2025-09-15 04:49:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 71575bb6-ddc8-3dd8-bf60-8946c3a364b2 | -8.19564 | -47.12524 | 2025-09-15 04:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aad2d573-5242-3570-8146-7222399914f9 | -7.19907 | -44.38612 | 2025-09-15 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bc19aa86-e59d-3ce3-8cfe-bb8f758a62c8 | -7.48252 | -44.68422 | 2025-09-15 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4927da68-dcfa-3e5b-a633-1434ad68ebb0 | -5.63745 | -45.94748 | 2025-09-15 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ca18b1d9-a295-3d91-ac99-e13852ce65e4 | -11.08175 | -49.73275 | 2025-09-15 04:51:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 96a84864-466f-3d08-9b00-621af024c0fd | -13.8848 | -48.12788 | 2025-09-15 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1584b950-4465-34ad-9798-72b53d0ce709 | -13.93944 | -44.80184 | 2025-09-15 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4e838e3a-e731-36b7-8ef6-f4b434cd0854 | -11.07765 | -49.71211 | 2025-09-15 04:51:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1fbf8543-1d76-3071-b3a6-c282cd4dea49 | -11.07418 | -49.73557 | 2025-09-15 04:51:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e55f9453-08ab-3800-97d2-0b5f8b0a229b | -12.17129 | -44.0999 | 2025-09-15 04:51:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 8b249757-5889-3cd9-a5f7-abd3781e2f9f | -11.0765 | -49.74106 | 2025-09-15 04:51:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b5e68dcf-c107-395d-89ec-2ca20ccc53be | -13.89481 | -48.31731 | 2025-09-15 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0361ada9-e3d3-3c19-b167-ed904ef31a51 | -13.77224 | -49.35098 | 2025-09-15 04:51:00 | NPP-375D | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0fae306f-2a6b-3c9f-9550-aa505119d2a2 | -12.62564 | -47.94271 | 2025-09-15 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bef941df-28d6-3449-a189-ddff46d77b44 | -14.20622 | -48.76289 | 2025-09-15 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7427337d-9d3a-353f-9504-3514cf90d94b | -11.74709 | -50.45712 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f71c858d-9840-30e9-957b-beb14d9f2396 | -10.92659 | -61.96188 | 2025-09-15 04:51:00 | NPP-375D | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 89e552eb-f262-3853-a814-0848736ad646 | -10.92153 | -45.59525 | 2025-09-15 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ce4d7955-2a27-3494-a465-9a95fd0b35b0 | -16.67655 | -49.77986 | 2025-09-15 04:51:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 149e5d3d-004e-3c8a-9435-73ce46b23f6c | -16.28219 | -45.68156 | 2025-09-15 04:51:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7aba1a94-1f00-3545-a013-7254f69ed2d4 | -11.07597 | -49.72102 | 2025-09-15 04:51:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 81204851-230e-36fa-b1a3-ae809fd1e780 | -15.78099 | -52.21707 | 2025-09-15 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c5be6131-1090-3bc6-98a9-fe22dcbe73e8 | -11.73625 | -50.45927 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 004a02c8-e17c-3d85-af68-b89f65db06b4 | -11.3996 | -51.36241 | 2025-09-15 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 4891b0f2-cf20-3884-9560-c1b4b79b3a5c | -15.79049 | -52.19994 | 2025-09-15 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README47.md)
