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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4ae916ac-2622-38f0-972b-433ab2973f94 | -4.8931 | -43.2582 | 2025-10-26 03:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| f6409092-36d5-3d0f-af2d-6d61a448fe32 | -5.0992 | -43.2211 | 2025-10-26 03:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 2afba3f1-9183-38a2-9efc-3471788ecc35 | -2.7755 | -45.0835 | 2025-10-26 03:00:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 31.9 |
| a653178d-004c-377e-88c3-a05f377ee52b | -17.3165 | -43.643 | 2025-10-26 03:00:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 182.0 |
| f4eddecc-5604-3d21-b39b-6e9bcbbe6bcc | -3.7661 | -47.5727 | 2025-10-26 03:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| ee40c3eb-68c1-3cdb-984a-00860a2cd3c9 | -2.3178 | -48.5717 | 2025-10-26 03:00:00 | GOES-19 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 36.8 |
| bc7b443c-2b0b-3e67-89ed-77585b6330f6 | -4.8931 | -43.2582 | 2025-10-26 03:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 59.7 |
| ec9b773a-d47b-3ed1-834a-60790464f6ad | -13.5405 | -43.0077 | 2025-10-26 03:10:00 | GOES-19 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 100.0 |
| 9d281f0f-e25c-37e8-ba11-d64e9b3bd2c9 | -5.118 | -43.2198 | 2025-10-26 03:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 60bb75e9-b09a-3bb3-abbb-59e62169ae15 | -5.0994 | -43.1977 | 2025-10-26 03:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 175.2 |
| 3aa57a3a-fba5-30e1-ad6a-5b1dd9111ba7 | -5.1181 | -43.1964 | 2025-10-26 03:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 176.2 |
| 7bd10851-5b53-3a64-aff1-3e15af98769f | -3.7661 | -47.5727 | 2025-10-26 03:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 37.5 |
| a160a273-7b0e-326f-a42d-5d4a056611aa | -5.0992 | -43.2211 | 2025-10-26 03:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 37741141-b0f8-3ab1-90da-e296d0e79ee1 | -4.8933 | -43.2349 | 2025-10-26 03:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 8d5b5a2f-12ec-35c3-9be0-24d72122be44 | -6.52565 | -37.98801 | 2025-10-26 03:10:00 | NOAA-21 | BOM SUCESSO | PARAÍBA | Brasil | 2502300 | 25 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 4af255c5-9fca-3cf4-a9e9-42762a586a01 | -5.65534 | -35.70052 | 2025-10-26 03:10:00 | NOAA-21 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 1d1c0f09-c200-3e80-8ba9-98e11bdd1033 | -7.04762 | -39.75025 | 2025-10-26 03:10:00 | NOAA-21 | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c623b3f8-4caf-3b58-baea-5fc5e494a952 | -5.32736 | -35.93872 | 2025-10-26 03:10:00 | NOAA-21 | JOÃO CÂMARA | RIO GRANDE DO NORTE | Brasil | 2405801 | 24 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 6df8fdac-8d2b-38df-9bb5-bdd50e223b1e | -6.35869 | -38.3667 | 2025-10-26 03:10:00 | NOAA-21 | LUÍS GOMES | RIO GRANDE DO NORTE | Brasil | 2407005 | 24 | 33 | nan | nan | nan | Caatinga | 3.2 |
| f5cd57fb-22e8-31fb-995a-6c21e21cd0ce | -8.03197 | -41.19951 | 2025-10-26 03:10:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 38c35d22-319e-3f6b-b3cb-f58566e5e9ff | -5.82305 | -40.80354 | 2025-10-26 03:10:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 7.1 |
| d5a0a2b6-c140-3db2-a9a9-ca7429674096 | -7.08837 | -39.56771 | 2025-10-26 03:10:00 | NOAA-21 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ce90b506-d598-3352-a809-f769d66cbeb7 | -5.32795 | -35.93532 | 2025-10-26 03:10:00 | NOAA-21 | JOÃO CÂMARA | RIO GRANDE DO NORTE | Brasil | 2405801 | 24 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 146b8753-c1ab-36bd-b978-478dadd21abd | -6.36391 | -38.37238 | 2025-10-26 03:10:00 | NOAA-21 | LUÍS GOMES | RIO GRANDE DO NORTE | Brasil | 2407005 | 24 | 33 | nan | nan | nan | Caatinga | 3.2 |
| d909147d-44be-386d-95b6-743b7546a207 | -8.54006 | -38.1675 | 2025-10-26 03:10:00 | NOAA-21 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0cd3c640-0567-32af-9cf1-367d68c0a07c | -4.81044 | -38.66763 | 2025-10-26 03:10:00 | NOAA-21 | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 72ffc666-f42d-3f0d-9100-b55b49a9ff03 | -5.65016 | -35.69976 | 2025-10-26 03:10:00 | NOAA-21 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 2bdacffd-f130-3bf7-b9b9-0c79a8d6402c | -5.46886 | -37.84859 | 2025-10-26 03:10:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 6d85bd68-2cf0-3d25-942c-d0e91b9308e2 | -6.52963 | -37.98874 | 2025-10-26 03:10:00 | NOAA-21 | SANTA CRUZ | PARAÍBA | Brasil | 2513208 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5aee8555-f010-3ac5-a3a1-1da9f0430559 | -5.3233 | -35.93082 | 2025-10-26 03:10:00 | NOAA-21 | PARAZINHO | RIO GRANDE DO NORTE | Brasil | 2408805 | 24 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 7f092d7b-296b-3652-b5e6-c203f97bc146 | -7.08883 | -39.56907 | 2025-10-26 03:10:00 | NOAA-21 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| be9db5c3-bb70-3703-9113-10fa880387f9 | -6.36316 | -38.37646 | 2025-10-26 03:10:00 | NOAA-21 | LUÍS GOMES | RIO GRANDE DO NORTE | Brasil | 2407005 | 24 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 3f21d4ee-d715-35f2-af97-d67184c9f142 | -6.36265 | -38.37399 | 2025-10-26 03:10:00 | NOAA-21 | LUÍS GOMES | RIO GRANDE DO NORTE | Brasil | 2407005 | 24 | 33 | nan | nan | nan | Caatinga | 9.7 |
| f47150e3-0529-39b9-a983-1e2cf78d8ce4 | -6.53044 | -37.9843 | 2025-10-26 03:10:00 | NOAA-21 | SANTA CRUZ | PARAÍBA | Brasil | 2513208 | 25 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1c681bfc-993b-3bb6-87d4-0a6fbdf01915 | -8.5396 | -38.16845 | 2025-10-26 03:10:00 | NOAA-21 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 40dfaa7f-f9de-3cb8-9e63-43d4aea97bd1 | -7.04877 | -39.74422 | 2025-10-26 03:10:00 | NOAA-21 | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| b605e2cf-3c33-3082-b2eb-1a7d50375cb1 | -7.3616 | -34.92782 | 2025-10-26 03:10:00 | NOAA-21 | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 3e213cc1-6deb-336e-b3a9-f48daf0205ae | -7.51012 | -35.23559 | 2025-10-26 03:10:00 | NOAA-21 | TIMBAÚBA | PERNAMBUCO | Brasil | 2615300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 79bd0e6a-fc90-3a31-b8f2-c1f0b33676cc | -5.65071 | -35.69664 | 2025-10-26 03:10:00 | NOAA-21 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 2c6ff0dc-960d-3245-a978-b612df4f8be6 | -4.81309 | -38.66731 | 2025-10-26 03:10:00 | NOAA-21 | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 4.6 |
| ab3e34c2-1fa3-387f-8eb3-240e58a13d44 | -6.52647 | -37.98333 | 2025-10-26 03:10:00 | NOAA-21 | BOM SUCESSO | PARAÍBA | Brasil | 2502300 | 25 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 535297cd-4942-36da-b718-3c1e8792fdf2 | -6.36338 | -38.36981 | 2025-10-26 03:10:00 | NOAA-21 | LUÍS GOMES | RIO GRANDE DO NORTE | Brasil | 2407005 | 24 | 33 | nan | nan | nan | Caatinga | 10.7 |
| a0ee080c-a52e-3f70-b172-5cb4828ead1e | -7.04951 | -39.74308 | 2025-10-26 03:10:00 | NOAA-21 | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f995be34-8b41-3cca-ad9f-7fd5440d16b4 | -5.32271 | -35.93423 | 2025-10-26 03:10:00 | NOAA-21 | PARAZINHO | RIO GRANDE DO NORTE | Brasil | 2408805 | 24 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 03b83c2e-e4b5-36b2-8f06-b0a85ee533d7 | -7.08778 | -39.57457 | 2025-10-26 03:10:00 | NOAA-21 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a7c830a2-d3ca-3bb9-a682-76ad50c31bab | -7.0484 | -39.74914 | 2025-10-26 03:10:00 | NOAA-21 | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1d12bc6c-0aee-36ce-babf-219c442d0b66 | -6.36469 | -38.36808 | 2025-10-26 03:10:00 | NOAA-21 | LUÍS GOMES | RIO GRANDE DO NORTE | Brasil | 2407005 | 24 | 33 | nan | nan | nan | Caatinga | 3.7 |
| b7dac3a3-cc79-3812-ba5b-8a6662c949f2 | -6.52444 | -37.9838 | 2025-10-26 03:10:00 | NOAA-21 | BOM SUCESSO | PARAÍBA | Brasil | 2502300 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6160bd2a-0a0c-3cc7-b3c8-c7816a60fdd4 | -7.08737 | -39.5732 | 2025-10-26 03:10:00 | NOAA-21 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 97f7b140-771e-34cb-ab32-0a0f667676bd | -5.32853 | -35.93192 | 2025-10-26 03:10:00 | NOAA-21 | JOÃO CÂMARA | RIO GRANDE DO NORTE | Brasil | 2405801 | 24 | 33 | nan | nan | nan | Caatinga | 15.3 |
| c1a3eea4-8c08-3463-8dbd-b3e8725f56bd | -6.35786 | -38.37121 | 2025-10-26 03:10:00 | NOAA-21 | LUÍS GOMES | RIO GRANDE DO NORTE | Brasil | 2407005 | 24 | 33 | nan | nan | nan | Caatinga | 5.1 |
| d5c5c20e-0853-31c3-8f6e-5d56c67588ed | -15.29829 | -42.93639 | 2025-10-26 03:13:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 45e18fc8-6b66-3b72-bd67-f7b49d3f304a | -13.39872 | -43.02353 | 2025-10-26 03:13:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f4d03d13-eaf1-3efa-8644-af17545ed473 | -13.40299 | -43.02133 | 2025-10-26 03:13:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 2d9d90b8-1b26-30a1-bf7a-d7c70e762cf3 | -13.40025 | -43.01637 | 2025-10-26 03:13:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 23999219-8174-3c5c-a8be-41ef94660e77 | -14.51271 | -43.00756 | 2025-10-26 03:13:00 | NOAA-21 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 49fa5bf3-1e22-38cd-9af3-03b911222c28 | -13.53465 | -43.01324 | 2025-10-26 03:13:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 36.7 |
| 9447000f-2852-3eba-b5a5-97a0dc3deae1 | -15.27267 | -43.18091 | 2025-10-26 03:13:00 | NOAA-21 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 66aa82da-7cb1-3418-bff7-c940952c72a0 | -14.50577 | -43.00608 | 2025-10-26 03:13:00 | NOAA-21 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 17.3 |
| 16ec1131-d968-321a-86ae-f7811ecc4cbe | -13.4058 | -43.02499 | 2025-10-26 03:13:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 74b37066-d057-31ff-97b8-9dbeadadd722 | -13.53624 | -43.00599 | 2025-10-26 03:13:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 36.7 |
| b0b902b5-e449-3219-b3ef-454957d7b913 | -15.26577 | -43.17937 | 2025-10-26 03:13:00 | NOAA-21 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b7ba7cfa-9acc-34ce-a4b3-51d7434e638e | -15.27119 | -43.1876 | 2025-10-26 03:13:00 | NOAA-21 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 498f4323-d80f-387c-b734-dee3fad996a5 | -14.51433 | -43.00023 | 2025-10-26 03:13:00 | NOAA-21 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 4c9aee72-1c5b-310f-a0d1-dbe3ed740138 | -15.27247 | -43.17816 | 2025-10-26 03:13:00 | NOAA-21 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 9dbdf3be-8400-37b8-b6eb-6dd0a00e682f | -15.27094 | -43.18482 | 2025-10-26 03:13:00 | NOAA-21 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 52e847b8-177e-3d55-a6cd-bd18ebc5d037 | -14.50743 | -42.99863 | 2025-10-26 03:13:00 | NOAA-21 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 17.3 |
| 4793360d-b386-394b-bb29-f5bf77cc71c0 | -13.53789 | -42.99849 | 2025-10-26 03:13:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 33.2 |
| b9b6d6e1-5eda-3206-af28-ce93d09d2e1e | -17.32521 | -43.6595 | 2025-10-26 03:15:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 4d0c4c7e-f9c2-3a96-ac51-bcf93ec5b4b2 | -17.32127 | -43.64573 | 2025-10-26 03:15:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 1648e7ad-a7af-3fbe-a287-b769abab17f0 | -15.58445 | -43.20173 | 2025-10-26 03:15:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8bb6e459-4281-33e7-aa28-94e0037f8c9e | -17.31966 | -43.65102 | 2025-10-26 03:15:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 52c1313d-aa47-3610-b892-2e19a05d2615 | -19.8574 | -42.18559 | 2025-10-26 03:15:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 1372c553-3653-3925-9154-b77be682a518 | -17.32809 | -43.64732 | 2025-10-26 03:15:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 6abe7007-fb56-324e-99e2-edb0ec18e42e | -15.58823 | -43.21715 | 2025-10-26 03:15:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 9273a593-2bbe-3f70-8443-10ac0c991a9c | -19.86332 | -42.18737 | 2025-10-26 03:15:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 71c8a3d9-ebff-39b0-97bc-9c918969bfaf | -17.31817 | -43.65752 | 2025-10-26 03:15:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 85.9 |
| f48d857c-3579-3e5c-b6f7-02c19fda39b6 | -22.52497 | -44.36267 | 2025-10-26 03:15:00 | NOAA-21 | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| bb71a032-7c90-3cf0-a918-3fca59b3d34a | -15.58976 | -43.21026 | 2025-10-26 03:15:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 42883a84-43ad-328c-bdd1-b08c63191246 | -20.51103 | -41.99233 | 2025-10-26 03:15:00 | NOAA-21 | CAPARAÓ | MINAS GERAIS | Brasil | 3112109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| fc940ab1-9cba-34bf-966d-1493abe2fb2b | -17.3267 | -43.65322 | 2025-10-26 03:15:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 84fd50fb-1035-37b0-9dfd-219d3efab278 | -17.32656 | -43.65229 | 2025-10-26 03:15:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 51e9eba9-544b-3870-a6a7-4cfdf4ab569a | -15.47835 | -43.12914 | 2025-10-26 03:15:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9b54bcb3-3008-3607-9cd2-6b3f5178fdab | -19.65451 | -44.62517 | 2025-10-26 03:15:00 | NOAA-21 | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 65d3dbfc-d18f-3f76-bb76-815411a8cea0 | -17.32512 | -43.65855 | 2025-10-26 03:15:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 49.8 |
| f643f95c-a073-316f-91dc-5e195eadcc86 | -19.85864 | -42.18639 | 2025-10-26 03:15:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| c1a0b197-4b99-3e48-836c-eb62d64ef959 | -15.5887 | -43.21384 | 2025-10-26 03:15:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 53fc90e3-b9dc-3e23-bdd9-b93ff132ddfe | -22.52632 | -44.35724 | 2025-10-26 03:15:00 | NOAA-21 | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f914946b-dc2f-3efd-95f5-ca2280aa46b2 | -17.31978 | -43.65202 | 2025-10-26 03:15:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 51.4 |
| b6827399-1004-3f39-8738-d89f2d8e24aa | -17.31824 | -43.65851 | 2025-10-26 03:15:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 51.4 |
| a5ac7573-c9da-3d17-8596-d22031f98513 | -6.7061 | -42.0517 | 2025-10-26 03:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 66.2 |
| 1cf246c1-9eb8-3604-9204-2a980f5e759a | -5.118 | -43.2198 | 2025-10-26 03:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 58.7 |
| df80d66a-394d-30b7-8fc0-4c3d7d775c9f | -5.0992 | -43.2211 | 2025-10-26 03:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 18be7b39-bb23-3ebe-adc1-0c917b623bd4 | -5.1181 | -43.1964 | 2025-10-26 03:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 175.1 |
| abf13f6e-b3f2-3757-b5f4-c4970bf05847 | -5.0994 | -43.1977 | 2025-10-26 03:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 172.8 |
| a757f096-aa97-3294-b0c9-e1480f3ef7d3 | -13.5405 | -43.0077 | 2025-10-26 03:20:00 | GOES-19 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 88.2 |
| fa90ba70-f06b-3fef-a66f-f3a2f255c010 | -3.0908 | -49.4671 | 2025-10-26 03:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 31.2 |
| dcd6566f-01d6-30fc-abe6-357e392da767 | -4.8933 | -43.2349 | 2025-10-26 03:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 6bb7f289-7665-33c8-8324-42a0096c82a3 | -3.0909 | -49.4459 | 2025-10-26 03:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 33.2 |
| bf612c28-13d2-341b-8b7b-b6b11d40833f | -2.3178 | -48.5932 | 2025-10-26 03:20:00 | GOES-19 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 32.3 |


[Clique aqui para ver as próximas entradas](README7.md)
