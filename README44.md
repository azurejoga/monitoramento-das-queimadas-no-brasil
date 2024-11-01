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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 24bf6a25-2507-30a8-81a5-858bff20dd68 | -2.07866 | -47.12887 | 2024-11-01 05:23:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9bf2f7d2-98e0-3694-956e-839d6b8bb48a | -2.07782 | -47.1345 | 2024-11-01 05:23:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3bd1b47c-e2d1-3434-a563-3e70bb66bfa5 | -1.94234 | -46.93589 | 2024-11-01 05:23:00 | NOAA-21 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a99cb343-d7e6-330c-a24c-bb582140d745 | -3.12124 | -46.04648 | 2024-11-01 05:23:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ef16c15f-f311-37ed-8bfd-4e34646b5223 | -2.92847 | -46.77942 | 2024-11-01 05:23:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f9e32e83-584d-376c-a30d-a9cded4a223c | -2.92167 | -46.77837 | 2024-11-01 05:23:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3ebc7310-f473-323e-aeba-c4d960e5e02f | -2.30211 | -46.82159 | 2024-11-01 05:23:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4ebe7ca9-3961-313a-b6a9-bedb8440115f | -2.30132 | -46.82701 | 2024-11-01 05:23:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 893f2e4d-0cc6-30ad-81e1-caa3b29a4d74 | -2.2985 | -46.82486 | 2024-11-01 05:23:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 478ca3c5-232a-3ebe-aa12-80a9b9a44e64 | -2.29765 | -46.83044 | 2024-11-01 05:23:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 88fbfa1e-13ca-3ca5-a813-286bcf8ef9f9 | -2.2946 | -46.82595 | 2024-11-01 05:23:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3355a4f3-813f-309e-bdf9-84d07f475ef6 | -2.26143 | -46.65758 | 2024-11-01 05:23:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fda80fc8-af06-3cb0-84ae-9dac0469b8ab | -2.26053 | -46.6637 | 2024-11-01 05:23:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 47921519-a15a-3e39-81b1-278753766d5b | -4.65933 | -46.31713 | 2024-11-01 05:23:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f73c0265-0113-30b1-992d-f69a9ae624eb | -4.65538 | -46.31947 | 2024-11-01 05:23:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 62468535-206e-3201-a6b1-c1c388fcba48 | -4.65222 | -46.31588 | 2024-11-01 05:23:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f7c0d552-1142-371d-a554-c2288b09067d | -3.56301 | -47.37889 | 2024-11-01 05:23:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 82baec19-9c18-32c5-a98a-ea45533bb567 | -3.56218 | -47.38462 | 2024-11-01 05:23:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| f6d010f2-7721-30cb-81e4-9686f6d1ecef | -3.56107 | -47.37774 | 2024-11-01 05:23:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 175a6b9c-c31e-3f16-a9f4-cadcce622ef7 | -3.56027 | -47.38353 | 2024-11-01 05:23:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| f620301d-e6fa-36e2-9910-f4f29ad65958 | -3.55949 | -47.38913 | 2024-11-01 05:23:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| a327b57b-4142-30ca-bdf8-1d0e7a671fd0 | -3.55559 | -47.38347 | 2024-11-01 05:23:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4f7b447a-d3be-3fdd-ae17-41a9b406ace2 | -1.04552 | -47.7915 | 2024-11-01 05:23:00 | NOAA-21 | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bcae5367-07d1-319f-825e-8c33a2edea67 | -1.03929 | -47.79049 | 2024-11-01 05:23:00 | NOAA-21 | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c7f6428f-86d3-3600-aae7-b69af70b66bf | -2.91219 | -48.61703 | 2024-11-01 05:23:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| dae128fa-f6c6-3ec0-8907-8fe08b6c14dc | -2.91153 | -48.62155 | 2024-11-01 05:23:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e23ad7f5-12f0-3ddb-8067-cf40506efad6 | -2.88467 | -48.28946 | 2024-11-01 05:23:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8dc5cbf5-db82-3bbd-adfd-7f0a057edf72 | -2.87304 | -48.66212 | 2024-11-01 05:23:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0527a9b2-5a2b-364d-b66a-516f7eeaeebc | -2.86857 | -48.66167 | 2024-11-01 05:23:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 409d73ba-b5db-3fa8-83b2-e92c362f3638 | -2.86698 | -48.6612 | 2024-11-01 05:23:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3edce0d0-529a-3764-a699-eb0492f304db | -2.86093 | -48.66025 | 2024-11-01 05:23:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0ecec2f0-ec28-33bc-b6b6-7a624cc98034 | -2.83147 | -48.43759 | 2024-11-01 05:23:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 154620b2-e9e0-3379-af45-feb7fa338103 | -2.77559 | -48.65151 | 2024-11-01 05:23:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9e3f2c8a-f451-3566-b589-2c7046475e17 | -2.77421 | -48.65041 | 2024-11-01 05:23:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1ed22ba6-c59a-309f-92c6-8038e669c183 | -2.7702 | -48.64602 | 2024-11-01 05:23:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| bd7dea3d-2434-3e5a-ac5d-73776e78fdf2 | -2.76955 | -48.65056 | 2024-11-01 05:23:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bb1aa161-5119-300b-b36b-fbf030e157ea | -2.76817 | -48.64948 | 2024-11-01 05:23:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 58d17696-4fc0-39b9-ae4a-fb901ad5bd11 | -2.62069 | -48.33339 | 2024-11-01 05:23:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f35b80cc-2a72-39bc-9ec9-ae7c289fcc3b | -2.51994 | -48.46558 | 2024-11-01 05:23:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e539fc0c-7a02-316c-becf-d2c28b28faca | -2.51926 | -48.47021 | 2024-11-01 05:23:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 994a70fa-5344-39fe-8e1f-4bb32faf6422 | -2.46448 | -48.50434 | 2024-11-01 05:23:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3552cd84-d4ff-3106-ac25-8ba28503f0bd | -2.46335 | -48.50374 | 2024-11-01 05:23:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d993a256-ccd6-37e3-b39d-3ca4acee4f71 | -2.45907 | -48.49876 | 2024-11-01 05:23:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ef6a02d3-0dca-33c6-a357-887837d73ed4 | -2.4584 | -48.5034 | 2024-11-01 05:23:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d2f2c60b-9690-325a-8a7e-d601d13b8b07 | -2.45797 | -48.49819 | 2024-11-01 05:23:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f85dcc2a-26a1-3cd3-b4b8-683ca9128aa6 | -2.45728 | -48.50281 | 2024-11-01 05:23:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| de99b6fa-bd7a-35e8-a6ec-cd57e520fb48 | -2.40122 | -48.5874 | 2024-11-01 05:23:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10945966-1ab9-37eb-a0ae-1829b9841107 | -2.39874 | -48.22586 | 2024-11-01 05:23:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 34f3fb75-a424-36ee-99c4-5e4209698d0b | -2.39518 | -48.58646 | 2024-11-01 05:23:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5d1b705a-96f1-3d9e-8d04-c1799302d1dd | -2.36258 | -48.68233 | 2024-11-01 05:23:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7e3c110c-0aa4-3106-a219-acf7ddc0c8d1 | -2.35657 | -48.68146 | 2024-11-01 05:23:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 257a9555-1480-3376-be4e-4e8c4f5d2f52 | -2.35122 | -48.67603 | 2024-11-01 05:23:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ddfda906-d851-36e8-b631-fc7137ac48a1 | -2.35057 | -48.68047 | 2024-11-01 05:23:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fc0a51ee-5dc0-3741-8499-e81757f3e0ab | -2.34993 | -48.68488 | 2024-11-01 05:23:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4f1a5252-0047-308c-b279-6bf67fb60fd1 | -2.34868 | -48.67696 | 2024-11-01 05:23:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3da32a0d-0b7b-3a6c-9e45-a72f3629dd3e | -2.34801 | -48.68136 | 2024-11-01 05:23:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4a21e534-7eba-3c00-b413-d2a2c691b955 | -2.34523 | -48.67504 | 2024-11-01 05:23:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b39e16c-e764-336a-8df7-5e0bab18db68 | -2.34269 | -48.67595 | 2024-11-01 05:23:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb333d59-e5e5-3273-8f86-3618f9b6db2c | -2.32808 | -48.83452 | 2024-11-01 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| efcf4b3f-d178-38ae-a630-f93e5a261db4 | -2.32744 | -48.83888 | 2024-11-01 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 28157a97-7cbc-3694-b059-6b79cf003573 | -2.17896 | -48.72681 | 2024-11-01 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| abb54472-9163-386c-9910-d89e34bcefd5 | -2.1783 | -48.73122 | 2024-11-01 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| e93dfdc2-de7c-3f65-bcab-287ea565316b | -2.173 | -48.72586 | 2024-11-01 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| d9524f9d-75f2-3081-8397-603f7528e145 | -2.17233 | -48.73031 | 2024-11-01 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 2b6f31f2-d369-3b4c-9b8e-012c3f5a24eb | -2.17168 | -48.73462 | 2024-11-01 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| c20dd819-7c07-39fd-b857-769a62d220f4 | -2.98051 | -47.92117 | 2024-11-01 05:23:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd8f8204-f81a-3bf3-9ff7-bc00af17a4a9 | -2.97775 | -47.9214 | 2024-11-01 05:23:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 28dbcf14-06a3-3746-8157-2cbb5047061d | -2.97416 | -47.92024 | 2024-11-01 05:23:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fa739b83-421b-35c4-810f-e8a926166d06 | -2.3964 | -47.72414 | 2024-11-01 05:23:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 685da80d-c968-3197-b7d8-0fd7cd7d9844 | -4.33925 | -48.59097 | 2024-11-01 05:23:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 077f4cdc-603a-37fe-b9d7-965c29eaef6a | -4.33852 | -48.59609 | 2024-11-01 05:23:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 97e97f5a-5f6b-31ab-b0b1-71c2f7c9dd1b | -3.94095 | -48.35296 | 2024-11-01 05:23:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 83ce796d-9fc4-3994-bb8f-e39ad402421b | -3.94026 | -48.35777 | 2024-11-01 05:23:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 943c5760-8063-3cca-8787-a0ac15880557 | -3.93958 | -48.36249 | 2024-11-01 05:23:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 230e28e0-e77c-3886-953e-a6f7da7aee7d | -3.93399 | -48.35689 | 2024-11-01 05:23:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98cc6c78-67c2-30eb-895a-046281f56fb3 | -3.87559 | -48.36303 | 2024-11-01 05:23:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2db8bdcb-8144-39a0-a5f8-ff79c20bae55 | -3.87159 | -48.36186 | 2024-11-01 05:23:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d9e91670-34e4-3d68-af54-c0672b16dbb9 | -3.27064 | -50.33856 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 548bafa3-ecfa-3fe6-80d9-62c17d59261d | -3.27013 | -50.3421 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8d640031-d3e5-3129-bacc-0e3ab790d1f5 | -3.26964 | -50.3363 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 876b2d7e-db87-3fc8-b156-61c0bb2100ac | -3.2691 | -50.33986 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 11b38997-f7be-30cd-86e2-8a94eea3550a | -3.26857 | -50.3434 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| facdd0ad-701c-314d-be9c-3ea0a37a845f | -3.2657 | -50.33408 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c1f819c7-925c-3082-8f58-ca4b5c534f43 | -3.26519 | -50.33767 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a6338009-0ef5-38cb-86b0-802a70a2b474 | -3.26468 | -50.34122 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dcd81799-c50e-3720-9f35-1d06c8fae5b6 | -3.26419 | -50.33542 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 01ca7e23-e936-34d1-9632-2be0838e3b4b | -3.26418 | -50.34478 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6cafc6b2-95c6-36ca-a492-d20c38573597 | -3.26365 | -50.33899 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dcd7a453-37e7-39f5-bc12-927ee4c3a234 | -3.26312 | -50.34253 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3cd3bc80-b90e-3b86-b777-a34c442e1b62 | -3.25974 | -50.3368 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 534b83c2-2ab2-3f41-90bf-b6bf1ca04670 | -3.25923 | -50.34036 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 12f9dbc4-2f4c-3393-bbaa-9dc6888451d4 | -3.2582 | -50.33815 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 454acf32-6ad2-3e69-9c61-9f5ff24c42d7 | -3.25638 | -50.04584 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4925c4a5-ba6d-3d6c-99e9-a2bb29a3f458 | -3.25584 | -50.04951 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 28fc8c62-1e20-3de9-b534-03300ff651e6 | -3.25274 | -50.33733 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90a3dfad-80f1-3107-9548-53fc10bf786c | -3.25221 | -50.34084 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 54652c00-8616-3444-bf10-6d371b456d9c | -3.25081 | -50.04503 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0154a915-afb1-3ee8-880c-d7cb6fb1a9de | -3.25028 | -50.04867 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c8ddcc4b-43c1-3fc8-a5bc-9b6c8b83587c | -3.24729 | -50.33648 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 963dc9a5-abd8-391c-a0ee-a5ff6ea202fd | -3.0542 | -49.48037 | 2024-11-01 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |


[Clique aqui para ver as próximas entradas](README45.md)
