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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1fefd2ee-1d35-3986-815f-ad280b0d9e95 | -11.2821 | -44.257 | 2026-10-05 13:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 91.5 |
| bf35b56c-c522-319b-9d9b-9bb70b39a44a | -11.3204 | -44.2514 | 2026-10-05 13:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 913c0b02-37f6-3190-aaad-aedfb4b7b68f | -11.3013 | -44.2542 | 2026-10-05 13:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 55721876-c1c2-3072-9846-17ceba22b695 | -8.7526 | -64.1909 | 2026-10-05 13:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 095d7f2c-0a6b-3e85-aa2b-631efec16494 | -7.8356 | -45.3175 | 2026-10-05 13:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 41a4461b-d681-3ec1-93cf-4254fad56550 | -7.9056 | -44.1883 | 2026-10-05 13:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 078e3567-fafe-3df4-b115-4d9c71e75011 | -9.8447 | -44.7988 | 2026-10-05 13:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 38570710-4bb5-37b2-85f8-772a1f80a52a | -11.2438 | -44.2626 | 2026-10-05 13:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 89.5 |
| f3ae5c51-893e-314b-9911-09663a061ad5 | -9.8257 | -44.8011 | 2026-10-05 13:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 08b9c072-4ac1-3378-bfe0-3cec4a027611 | -6.9143 | -43.6583 | 2026-10-05 13:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 30b5a30e-02b1-3ebf-93a7-8193bc033050 | -10.7493 | -45.3024 | 2026-10-05 13:40:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 86.1 |
| d8e0455a-49ae-3393-aee0-ec4efe4e23e3 | -10.4904 | -46.0419 | 2026-10-05 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 973a2e48-736a-31f5-8d43-e57c562b0726 | -6.8952 | -43.6833 | 2026-10-05 13:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 183.0 |
| 5e1c1940-9611-3292-a131-7321c83adf78 | -10.9575 | -45.389 | 2026-10-05 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 2bdad4d6-0992-3846-9eeb-606d17edbf87 | -9.8067 | -44.8035 | 2026-10-05 13:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 68.2 |
| e2b5f209-a03f-3257-84c4-0b422e79af1d | -7.8867 | -44.1902 | 2026-10-05 13:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 7887eacc-5fdd-3598-aab3-35cdb3e0306c | -8.8713 | -45.37 | 2026-10-05 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 2bc2140d-d9dd-38dd-8ffd-bfd76bb1950a | -7.7208 | -45.4872 | 2026-10-05 13:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 085cae15-9433-3b2c-a4d5-7817d7ab3724 | -7.8358 | -45.2948 | 2026-10-05 13:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 7968075f-deda-3f9f-978f-47c1e317e128 | -10.9762 | -45.4094 | 2026-10-05 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 176.9 |
| 2bad66cd-fb22-3feb-bd82-f3681034a006 | -9.8634 | -44.8195 | 2026-10-05 13:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 49c13dd4-868e-3c31-bc98-d212fcb2cbf6 | -7.721 | -45.4645 | 2026-10-05 13:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 85.7 |
| b1052462-76cf-33ef-87e0-3b982d61117e | -10.9567 | -45.4349 | 2026-10-05 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 220.9 |
| 769a1f3d-50b4-3a98-ba36-7833c2820075 | -10.9571 | -45.412 | 2026-10-05 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 139.4 |
| 6d23c10b-9f31-3c5a-b666-5b4ed515145f | -11.3009 | -44.2776 | 2026-10-05 13:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 680330a0-22e7-397d-bbbf-64c49f6efc49 | -8.05486 | -72.43706 | 2026-10-05 13:40:00 | TERRA_M-T | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 4b61cef7-d48a-356d-b636-853f9402290e | -9.17233 | -68.24567 | 2026-10-05 13:40:00 | TERRA_M-T | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 30.1 |
| 2665c2e4-b3be-30cb-8871-b9b60851ecd9 | -9.16881 | -68.25215 | 2026-10-05 13:40:00 | TERRA_M-T | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 0b11cedd-8ef6-3e78-b526-583c47a91cab | -9.14029 | -67.75568 | 2026-10-05 13:40:00 | TERRA_M-T | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 448bc561-58b2-3f0a-92de-6301b63bdc4a | -9.13395 | -67.75996 | 2026-10-05 13:40:00 | TERRA_M-T | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| be48c9f2-d0da-35d8-af15-7bd9e4bda32a | -4.57636 | -68.91108 | 2026-10-05 13:40:00 | TERRA_M-T | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| ee31e2b9-3e88-3218-80fc-8bcbf462e2e3 | -9.16867 | -68.27576 | 2026-10-05 13:40:00 | TERRA_M-T | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 89a43b88-58d7-3428-9f80-f035b8875d53 | -7.8867 | -44.1902 | 2026-10-05 13:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 279cd7c7-1229-3b74-b7a5-3e21eb85f82a | -10.9758 | -45.4324 | 2026-10-05 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 425.1 |
| ba45eeff-6eed-328d-8b54-1324673564cf | -10.9567 | -45.4349 | 2026-10-05 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 223.6 |
| 07ca2457-f809-3607-a0d0-3435657fc743 | -6.3435 | -42.5365 | 2026-10-05 13:50:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 98.3 |
| eccc1c7f-e515-370f-9c2c-cee28351f6ab | -10.7493 | -45.3024 | 2026-10-05 13:50:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 54.3 |
| ab37d9c7-d641-36eb-9fbb-e4dc336c4a22 | -11.6758 | -43.658 | 2026-10-05 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 88.5 |
| ee49e3c6-ba37-316b-b4d3-f64482d8ad32 | -11.2442 | -44.2392 | 2026-10-05 13:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 799e1bb1-ce92-381e-bb61-8ea9847006fa | -6.8955 | -43.6601 | 2026-10-05 13:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 94a239ad-2a81-39cf-925c-fb9455b51d36 | -10.9575 | -45.389 | 2026-10-05 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 60.0 |
| bf384a14-ea51-33b7-9802-1b9ccd732e8d | -10.9762 | -45.4094 | 2026-10-05 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 147.1 |
| 69e0f29d-6cfa-3be2-bece-591cb34471ee | -10.4904 | -46.0419 | 2026-10-05 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 77932133-9db8-3c38-ad10-4ad4c3e70c14 | -7.9056 | -44.1883 | 2026-10-05 13:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 9841c5a1-c444-300b-bb44-9b76ab7751c3 | -10.9571 | -45.412 | 2026-10-05 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 124.2 |
| a6f13966-57f9-31ea-bb7e-5393446b1612 | -8.7526 | -64.1909 | 2026-10-05 13:50:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 7042cea1-a568-3d7a-869f-3c4b26e5d6ef | -9.1613 | -68.2568 | 2026-10-05 13:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 49bacc5d-d09e-32de-8749-49813e510c7b | -7.1778 | -42.0055 | 2026-10-05 14:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 97.0 |
| 9b33a699-1d12-31c1-848b-64b222879e3e | -8.3211 | -44.1447 | 2026-10-05 14:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 6d4024e3-f235-3afe-8123-116d77d372f4 | -11.7169 | -43.5098 | 2026-10-05 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 103.8 |
| fde9852f-edab-32a0-abac-fca8365db0a7 | -10.4904 | -46.0419 | 2026-10-05 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| f2652111-c608-3a9f-850e-6400dafd5064 | -11.6758 | -43.658 | 2026-10-05 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 5d139686-d8de-3225-a6cd-339ed5f72908 | -9.1613 | -68.2568 | 2026-10-05 14:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 1d6d1189-1bd3-3813-9b16-49befde58dd9 | -7.9056 | -44.1883 | 2026-10-05 14:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 81.1 |
| fec4c6e9-2d98-3998-a8ee-71e41899ab75 | -10.7493 | -45.3024 | 2026-10-05 14:00:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 9b12bf26-92b9-3276-a397-50f70aedd9d7 | 1.978 | -60.6099 | 2026-10-05 14:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 158.6 |
| b39e8c92-3226-321b-9264-ab0212d4ed4e | -9.4116 | -65.8912 | 2026-10-05 14:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 10bc858d-b2bd-30c5-9a9f-49aec64c9e73 | -8.7341 | -64.1915 | 2026-10-05 14:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 399864c4-ac33-34eb-b3cb-f556f50f21ee | -7.8867 | -44.1902 | 2026-10-05 14:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 352d9415-e70f-3416-abb8-24eeb9913163 | -9.7687 | -44.8082 | 2026-10-05 14:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 59.2 |
| fa78d690-35e5-3051-859d-7a2e7687a0ab | -8.3397 | -44.1658 | 2026-10-05 14:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 63.7 |
| e7083b72-eced-3b64-91b4-08d327136fe3 | -8.7526 | -64.1909 | 2026-10-05 14:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| eb052869-da3e-3223-924e-6ac29e895879 | -10.9758 | -45.4324 | 2026-10-05 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 627.9 |
| 5f099e70-15c8-3562-a76e-d669fbc29727 | 1.978 | -60.6099 | 2026-10-05 14:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 316.2 |
| 8930611a-d4e1-3471-ad96-b20771ffffed | -10.4904 | -46.0419 | 2026-10-05 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 5e565721-281e-3483-958c-03a87561b8e5 | -7.8358 | -45.2948 | 2026-10-05 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 0a9e719c-cbad-3b24-9268-8c931fa02ac7 | -7.8356 | -45.3175 | 2026-10-05 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 57041c4b-a65b-35a8-bf9b-41bbc41abf4b | -10.9571 | -45.412 | 2026-10-05 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 151.0 |
| 99f29ef0-618c-35f2-836a-3175bf1e4125 | -11.6758 | -43.658 | 2026-10-05 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 138.9 |
| dbe7265e-c7a4-39be-b0b8-6b3a69543f7d | -9.1613 | -68.2568 | 2026-10-05 14:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 81f1fcdc-bbbd-3205-8899-fbc0aac67ab4 | -8.7898 | -45.8321 | 2026-10-05 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 2b1ff410-402b-3b63-99c2-0b037f90be09 | -11.6951 | -43.655 | 2026-10-05 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 243628da-c8f2-3856-bfa3-dd9e99c26bf5 | -10.9575 | -45.389 | 2026-10-05 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 108.8 |
| aaf95935-42eb-3224-8bd5-209a255d172d | -7.7399 | -45.4627 | 2026-10-05 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 88.0 |
| c67622f2-6742-3cf6-ad04-e258290de070 | -10.9762 | -45.4094 | 2026-10-05 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 124.5 |
| 2042d6f0-5129-3dbf-ae23-06a6e90c7a0c | -8.3211 | -44.1447 | 2026-10-05 14:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 8d6e3b8d-f94e-330b-b404-6400e1c8b41f | -9.393 | -65.8918 | 2026-10-05 14:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 713e1e60-9932-37ae-beab-671e537bb833 | -8.3208 | -44.1679 | 2026-10-05 14:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 41bd07d0-f542-3677-b89d-80c6a45dd014 | -10.97 | -45.46 | 2026-10-05 14:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d979c0c0-db92-3a22-9be9-c415151f0b71 | -11.63 | -43.62 | 2026-10-05 14:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5761e32c-0d40-332e-b8f4-c5fc31ba5820 | -11.0 | -45.47 | 2026-10-05 14:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ff4620f1-0b9b-3072-8447-f84d4dfc4d27 | -11.66 | -43.63 | 2026-10-05 14:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fcbdc978-3d4f-3170-88f8-15eee32b8f7d | -10.97 | -45.41 | 2026-10-05 14:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 28e3fdf1-ff97-3abc-b2ef-a02e8c6cdeec | -11.63 | -43.67 | 2026-10-05 14:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9c5969c8-0f87-3073-b37d-10dc093d74fe | -11.8315 | -43.5391 | 2026-10-05 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 6145b2da-b897-3655-a57a-900732ee512c | -8.7526 | -64.1909 | 2026-10-05 14:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 77ca12a2-1a84-3551-a467-8644d8b9e980 | -10.9571 | -45.412 | 2026-10-05 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 122.7 |
| a4287099-adb5-300c-8a7a-e47ecd79514c | -10.9758 | -45.4324 | 2026-10-05 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 437.6 |
| ac7b0a6c-fbde-3359-9b12-ab522461c3e4 | -9.1613 | -68.2568 | 2026-10-05 14:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 40ad2c7d-b0dd-3cd5-a7a5-259f7b7f7591 | -8.3211 | -44.1447 | 2026-10-05 14:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 66.8 |
| f4f67f9d-ce44-3233-a1f9-405cb633f820 | -11.8123 | -43.5422 | 2026-10-05 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 86.3 |
| d20e54a8-7e05-337e-98da-76679f0c705c | -7.8358 | -45.2948 | 2026-10-05 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 90.7 |
| b942f417-6f78-3fdb-92bc-5e89c7ebd1bf | -9.393 | -65.8918 | 2026-10-05 14:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 98ec4395-5835-3914-98b3-135576540b9c | -11.6951 | -43.655 | 2026-10-05 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 8b9b5b5f-58cb-3be9-9018-3ec4ee4dd0d1 | -8.3397 | -44.1658 | 2026-10-05 14:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 73.0 |
| e16cb9bc-f222-37ef-ba01-2f96c38fb346 | 0.4465 | -60.5252 | 2026-10-05 14:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 120.2 |
| e0b64339-2da9-3c7f-b828-1a26a4d9b754 | -7.721 | -45.4645 | 2026-10-05 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 5600820a-8149-3236-affd-b49936897a3c | -10.9567 | -45.4349 | 2026-10-05 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 271.5 |
| a68b248f-be29-326b-9375-0dfdefc7b5d1 | -8.3208 | -44.1679 | 2026-10-05 14:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 34b2ad03-fe36-3d03-ac38-92204f63b15a | -10.9575 | -45.389 | 2026-10-05 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 60.7 |


[Clique aqui para ver as próximas entradas](README65.md)
