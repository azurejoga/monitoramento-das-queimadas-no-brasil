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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ef9640e8-413c-32a6-87cb-28e5a649bedc | -3.14381 | -53.14125 | 2025-10-26 04:49:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 20418398-0218-3a2b-a32b-8ed90968c0a0 | -3.1284 | -49.10218 | 2025-10-26 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 02d04355-3e63-348e-86f3-1c3bf860acfb | -2.26874 | -51.92926 | 2025-10-26 04:49:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ff644cb0-2be7-37ff-83a9-1bf88619f7f8 | -2.22587 | -48.37378 | 2025-10-26 04:49:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a3e090de-5752-3fcf-babd-18c1320e7194 | -3.94697 | -52.12419 | 2025-10-26 04:49:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 21ebd14d-1655-3f14-86d5-e36329d461fb | -4.30908 | -48.06551 | 2025-10-26 04:49:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d6ace328-4f85-303d-bb17-200685b5a0f1 | -2.92128 | -52.71632 | 2025-10-26 04:49:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cc227634-aea2-34b8-89a8-f36104af250e | -3.10176 | -49.44978 | 2025-10-26 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b3d1635b-fa9d-3a46-a603-e0ee497806b7 | -3.10267 | -49.45083 | 2025-10-26 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d01915a-81a8-3002-bd92-0a5f70fc0809 | -4.59691 | -49.59069 | 2025-10-26 04:49:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c38379b5-501d-3c3c-a8b5-76622ea15511 | -6.66849 | -45.93604 | 2025-10-26 04:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7a9ae5ae-b3c5-3155-b19f-373faa300f1f | -5.11586 | -43.19328 | 2025-10-26 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b5dea96c-70a7-3edf-9a2a-93648222e872 | -6.08245 | -42.15219 | 2025-10-26 04:49:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 0beef738-03fd-3d10-914b-6d00b2acf645 | -3.09921 | -49.45028 | 2025-10-26 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3088cf86-b7bd-3ce5-bae4-a3742cb08bdc | -6.90747 | -46.14579 | 2025-10-26 04:49:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0fd7451d-dd5f-393b-9f53-cf409e4a2858 | -1.63999 | -54.39706 | 2025-10-26 04:49:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f227b73f-70e7-3aec-88d0-85a4f2964a2c | -3.62795 | -51.98936 | 2025-10-26 04:49:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2d1cc465-5a69-3cb6-80f2-da9d428bb258 | -2.67062 | -49.4945 | 2025-10-26 04:49:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 66573c01-b34f-387f-b88e-310ca1faad2e | -3.11627 | -51.21252 | 2025-10-26 04:49:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a7bb564a-bbbe-38ad-88b3-d47e603cc30f | -5.5086 | -49.58122 | 2025-10-26 04:49:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89e7b2b3-cbee-3dc7-a3c4-966ff6bed505 | -6.60011 | -48.76081 | 2025-10-26 04:49:00 | NOAA-21 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b4207727-3e4f-3c4f-9ebe-9d5c676dd9b7 | -3.06398 | -54.61185 | 2025-10-26 04:49:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d442f500-8ad2-3da9-872f-aa51961034a4 | -3.78415 | -43.40742 | 2025-10-26 04:49:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0b2e790e-7023-3930-8612-a52e276deb33 | -4.18275 | -48.58593 | 2025-10-26 04:49:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9c445b0e-133c-3ad3-989d-3aa823be1ddf | -4.27335 | -40.69242 | 2025-10-26 04:49:00 | NOAA-21 | PIRES FERREIRA | CEARÁ | Brasil | 2310951 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f79c484d-ab8f-38bb-b65d-fe39a8776492 | -3.10864 | -50.20758 | 2025-10-26 04:49:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07bfdc76-05a5-3cab-973d-88a29ab02df2 | -4.3394 | -49.89333 | 2025-10-26 04:49:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f8d430c-1c46-3ca6-87a5-123184b56193 | -6.43162 | -45.66742 | 2025-10-26 04:49:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 695a6925-33d2-38c5-906f-edf802b6a599 | 1.62812 | -55.724 | 2025-10-26 04:49:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c2a399c4-32ab-308d-944b-7122d60661a7 | -3.94367 | -52.12368 | 2025-10-26 04:49:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 088e06ec-fe9b-3a5b-a3ab-4e4bef585997 | -3.77032 | -47.57691 | 2025-10-26 04:49:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 9ca262c0-5bf2-3921-ac6c-d0dd4b3943de | -3.82352 | -48.65701 | 2025-10-26 04:49:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63cc5a29-d65b-3195-b535-0bb06a67d310 | -3.14397 | -50.15769 | 2025-10-26 04:49:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 02747c9a-022e-32c3-8744-244083ea4b4e | -5.16659 | -50.73934 | 2025-10-26 04:49:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 896134b4-6eff-3029-a212-01cdbf9f9d24 | -3.53125 | -52.99168 | 2025-10-26 04:49:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 87bc2f4b-56a7-3eea-879b-e4febbba021a | -2.9775 | -49.11957 | 2025-10-26 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 057c4b27-f55f-314b-8714-7c76fd12c539 | -6.14155 | -41.812 | 2025-10-26 04:49:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 1e421bb3-f8c4-3847-b10b-f1ac04876924 | -2.92074 | -52.71978 | 2025-10-26 04:49:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e08d4e14-7d8f-3a2f-82f5-f6608d6479bc | -6.83079 | -41.55709 | 2025-10-26 04:49:00 | NOAA-21 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fdd954b7-9662-36e5-99f9-8c7091c3c7c8 | -3.14743 | -50.22466 | 2025-10-26 04:49:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e389e487-4e1d-34f0-85b7-5ba1fefd4b65 | -2.7865 | -54.41926 | 2025-10-26 04:49:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| db92544f-7ee6-33b8-919d-353fbbe33d77 | -2.77286 | -54.57243 | 2025-10-26 04:49:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 85e4fc5a-36c7-3386-bb95-94fbb151f636 | -6.53225 | -43.57431 | 2025-10-26 04:49:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d4d7a137-d440-373b-a6b8-40bf0febdb46 | -3.66789 | -51.9499 | 2025-10-26 04:49:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c33f51a6-5b31-3972-9af5-f5c74a39b974 | 1.95097 | -55.76212 | 2025-10-26 04:49:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 41b6c716-78cb-3c04-9a16-2fd360f5a53a | -4.26625 | -40.69813 | 2025-10-26 04:49:00 | NOAA-21 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| bf298c1d-616a-3ffa-a3a4-c724b7d8fba6 | -3.6093 | -49.34729 | 2025-10-26 04:49:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f31324d7-d44b-3f60-8fa3-3f9dec8bdc33 | -6.79177 | -45.40909 | 2025-10-26 04:49:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 03f58f5c-0439-3f20-9393-0ed31c4fa17d | -3.76328 | -52.25665 | 2025-10-26 04:49:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 328b69ee-61c2-3379-bc6e-e9ea0092d0bd | -3.86928 | -52.07621 | 2025-10-26 04:49:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b4bc9de9-3746-3dc1-984f-e7f82f5719ce | -5.41128 | -46.00646 | 2025-10-26 04:49:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 58a07131-bf82-399d-aaf9-10888ae708d2 | -2.12753 | -56.84462 | 2025-10-26 04:49:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1ed3f3be-5d29-3d0f-a0fa-465f65264eff | -3.10274 | -51.27749 | 2025-10-26 04:49:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e3bb8730-7ec3-3892-8764-cfb92c4d05f4 | -4.8013 | -47.88224 | 2025-10-26 04:49:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 428c35c4-1ff8-3ba7-92a4-9979f1df861a | -5.77832 | -51.39959 | 2025-10-26 04:49:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9fcad3f0-6fd7-32cb-a7ec-b59ffeb10697 | -3.9724 | -49.79226 | 2025-10-26 04:49:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 80ec8bdb-bf02-33c1-9d6b-a708b8e850cf | -2.66316 | -49.4972 | 2025-10-26 04:49:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 40e82f57-283b-3371-b9b6-8d51cf1c8de1 | -4.89609 | -43.2313 | 2025-10-26 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b82495bf-a225-3634-a2bb-f27cdfee68ee | -3.86729 | -50.10712 | 2025-10-26 04:49:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b833709f-200e-3d00-9bb2-66d5b6025ed6 | -4.72432 | -49.09159 | 2025-10-26 04:49:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 277f0e77-9edf-38e6-b251-346b4ed2ba4d | -4.82683 | -50.69108 | 2025-10-26 04:49:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1a5a3314-78f2-3e69-88bf-afb76509e634 | -3.82204 | -51.40061 | 2025-10-26 04:49:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bc46bae9-7da0-3bf3-b519-0240e18fa91f | -3.69455 | -49.54568 | 2025-10-26 04:49:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab2b1556-282f-3070-b8c2-6c12f8b7519e | -6.47481 | -47.55679 | 2025-10-26 04:49:00 | NOAA-21 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 6db2ae34-ef38-3c63-b367-6c35125af5f7 | -4.60159 | -49.5835 | 2025-10-26 04:49:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a5e5729-3cd2-3e03-baec-388999184acd | -4.83721 | -50.92947 | 2025-10-26 04:49:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cdc09370-c1b2-3261-bf8a-7b9bc2d05532 | -5.79704 | -49.94739 | 2025-10-26 04:49:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36743a45-9f88-3386-a1d0-a96a15c7cfc0 | -3.10029 | -49.46603 | 2025-10-26 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e7457bf0-9fb4-363b-8b02-fc5d42b45ca7 | -3.76261 | -47.57574 | 2025-10-26 04:49:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f9e3f773-f472-3fb7-a37d-01c97e415db0 | -3.14342 | -50.1613 | 2025-10-26 04:49:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc59d79f-6b74-3285-b83e-272df533d7e5 | -3.73536 | -42.29624 | 2025-10-26 04:49:00 | NOAA-21 | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 01b2347a-92a7-35d4-aadd-153d800211f7 | -4.26267 | -50.50894 | 2025-10-26 04:49:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 946c2887-ca29-3961-ae2d-ba7066d4e5ed | -3.14462 | -50.22054 | 2025-10-26 04:49:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0b072a58-d6a8-35c8-a145-ac569bd1f02e | -3.34153 | -52.83585 | 2025-10-26 04:49:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f347cb1a-4d48-3358-9a53-65b55533967d | -3.72534 | -47.39439 | 2025-10-26 04:49:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1210b482-39bf-3a61-a47b-368fd46bcdd4 | -4.81109 | -43.3005 | 2025-10-26 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bf90a4df-24bb-3bfb-8e84-4f14cb281a6d | -5.02444 | -48.36184 | 2025-10-26 04:49:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2a5e972-52ec-32ec-83e4-4d2d901d7c54 | -1.19542 | -53.38224 | 2025-10-26 04:49:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e53228fd-00fd-36ad-932f-bd0371aa6250 | -4.89813 | -43.25538 | 2025-10-26 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a9d12642-ba76-33fb-8bd2-1e8010a87ac1 | -2.81698 | -49.14495 | 2025-10-26 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 36d53514-f8a6-3c1a-8a97-81fcf58ee3cb | 1.61821 | -55.73988 | 2025-10-26 04:49:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b57aab39-ab0d-38e1-af2c-e41445fe0025 | -3.45383 | -49.69579 | 2025-10-26 04:49:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 19c987c2-f207-3133-adef-968322d7b9ee | -5.10967 | -43.19893 | 2025-10-26 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7a3eaedd-532e-3aa4-83c2-0c389f246bb1 | -3.81346 | -49.2931 | 2025-10-26 04:49:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb38b89c-c073-3d1e-96ff-e2375d811843 | -4.29495 | -47.56364 | 2025-10-26 04:49:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 811b70b7-adc7-3ba2-bef7-3d407e192f29 | -6.71628 | -44.62806 | 2025-10-26 04:49:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9f9ce1c2-0b1d-3c5b-9233-a2f839afe99e | -4.26885 | -50.51358 | 2025-10-26 04:49:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d4f6e2c-4548-3238-a624-0f75456701c8 | -3.1361 | -50.16389 | 2025-10-26 04:49:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e3c9d139-b1f2-3e48-b787-c6735a4a6f37 | -6.82968 | -41.54995 | 2025-10-26 04:49:00 | NOAA-21 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 159e1886-4a70-322b-af71-b5545559b5a5 | -4.15136 | -50.7698 | 2025-10-26 04:49:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2d187ab-a87d-3a24-85fd-0f3782be913e | -3.96307 | -45.4135 | 2025-10-26 04:49:00 | NOAA-21 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 14.0 |
| fc2ba3c4-907f-3e28-b361-c4ad68d2c21d | -4.60099 | -49.58739 | 2025-10-26 04:49:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28c39ec3-079c-3578-a29c-652bc5080625 | -3.13948 | -50.16441 | 2025-10-26 04:49:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 09bb15a0-c52a-3c16-be03-602aadb200b0 | -7.35372 | -42.44212 | 2025-10-26 04:49:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 84f4546c-330c-338e-873d-e57615f0bdaf | -4.87599 | -50.85551 | 2025-10-26 04:49:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 909c4763-3fda-3cc6-b0ab-0ab95052be75 | -2.97169 | -49.11065 | 2025-10-26 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4f7179ee-1d1d-35c2-a754-c7bf663c2379 | -2.32751 | -48.58594 | 2025-10-26 04:49:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 017cd525-db0e-38fd-bacc-11b51650d5fb | 0.71369 | -50.91699 | 2025-10-26 04:49:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0808f6fe-85d9-317b-866a-18d228d53140 | -5.11012 | -43.19568 | 2025-10-26 04:49:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 42b7bd45-1384-306e-8bdb-834900700390 | -2.81638 | -49.14883 | 2025-10-26 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README35.md)
