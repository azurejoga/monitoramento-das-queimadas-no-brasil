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
| a0fa76ed-a158-391d-a68f-cde2d1f48f03 | -20.38631 | -48.82476 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 44ded02f-fbea-3917-9653-bba99ba25340 | -20.38586 | -48.80009 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 393d1380-bb3e-3ce0-b4f3-2d84b46e1639 | -20.3856 | -48.82472 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 21.9 |
| cf65521a-edee-3418-bf91-c6405720f74a | -20.38547 | -48.82862 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 8732d89c-d5a0-31c6-84b3-9df61b015a46 | -20.3853 | -48.80018 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 15932b67-10dc-3975-a30c-ea9f3625520b | -20.38502 | -48.80399 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5428b207-7601-37b0-846a-73ab43c0db75 | -20.38474 | -48.82858 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 630417ad-d2ec-3427-b64e-1c2a582d42bb | -20.38464 | -48.83249 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 7ba8f4e8-4d75-3152-9148-a7e1f56f1b57 | -20.38444 | -48.80406 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b1104f69-fe05-3dfe-99f9-129c44e9f295 | -20.38418 | -48.80786 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f0c5ba59-9ce6-3e51-b488-695a916248cb | -20.38388 | -48.83243 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 24.7 |
| f4d1e64a-7ce8-345c-95c3-f1a661ea4e96 | -20.3838 | -48.83635 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 62f28fa5-bac0-34e5-9c4c-52b5d0a420e4 | -20.38358 | -48.8079 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3601206b-608e-3ca6-98d2-6c6cf9357099 | -20.38335 | -48.81171 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 662a996c-a8a6-33d6-837a-b7eaa4947c96 | -20.38302 | -48.83629 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 32cc02bc-2291-3a77-8b4e-f8291a6bd765 | -20.38297 | -48.8402 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 2965a32a-e3da-3531-a04a-b123c2713bb5 | -20.38272 | -48.81173 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e9e55b94-69c1-3aed-961a-729bfa7d0711 | -20.38253 | -48.81554 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 02b48b8a-8b79-3a67-ae92-6322791acda1 | -20.38216 | -48.84012 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 33.5 |
| b6554cee-57db-38e3-9cf4-5e5ac6a0bacd | -20.38187 | -48.81553 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ecfe2a1c-82cd-3973-8d02-e02fda5d3be7 | -20.3817 | -48.81935 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 85c5429e-92af-3d0f-91df-880b271205f8 | -20.38102 | -48.81932 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a8b3dff4-9d45-3c8c-98f6-5877c179a7d9 | -20.38086 | -48.82322 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 62507de6-2500-335f-a44d-3af7186c8945 | -20.3804 | -48.79868 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| db125a9c-7219-38e7-9fb2-5ca0ab23a7a2 | -20.38016 | -48.82318 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e69c478b-c931-319b-940f-cabf194ea983 | -20.38001 | -48.82714 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 3334ad78-734c-36c2-9a10-8d5a704ae461 | -20.37984 | -48.79878 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9103a2a3-2c61-3809-ac83-cebc87423dee | -20.37956 | -48.80254 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ffd3267a-c0e0-3cc2-8489-fa38628a071d | -20.37928 | -48.82711 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 6.1 |
| da552575-c48a-30a3-b075-92be9d3d88e7 | -20.37917 | -48.83105 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 8.6 |
| a804162b-4f81-3492-809f-1b35647428f6 | -20.37898 | -48.80263 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 698c9247-b78c-3058-af96-aa68f2bbcf84 | -20.37873 | -48.80638 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cfc38544-9f52-33f7-a4bc-c50c3076fea3 | -20.37841 | -48.831 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a80b0a78-703a-39d6-b50b-2f60c8019d53 | -20.37834 | -48.8349 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 96e851bf-b6a3-3ae7-96ba-184f5886a6bc | -20.37791 | -48.81018 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3ca929ce-4534-313b-8cfa-3b5ba142e3ab | -20.37756 | -48.83483 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 39.6 |
| ab2953ae-5b5f-3125-bd9b-4953962adee0 | -20.37751 | -48.8387 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 37.1 |
| b91105d2-714b-33ae-8038-5bb4b7bfd4b0 | -20.37728 | -48.81021 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d6bf6b1e-171e-39ec-9aec-2d9d247c3b4c | -20.37709 | -48.81397 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b5f78dd6-c952-3278-8464-899896c42a3b | -20.37671 | -48.83863 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 39.6 |
| e20f2655-c22b-317f-897e-ec769db93985 | -20.37644 | -48.81398 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 774e8cc9-870c-347e-b0a9-922fc82c8128 | -20.37626 | -48.81778 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4677fbb5-7379-33f2-aab4-b589c91eaa44 | -20.37559 | -48.81778 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5b829b71-212f-3e35-a442-d2de0bfb7a6f | -20.37543 | -48.82164 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a9556538-7f5d-382c-8cd0-7a2aca50c8ad | -20.37497 | -48.79712 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| efb80972-2724-315e-9aae-8ecadb4b55cf | -20.37472 | -48.82163 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fe210215-8549-3563-9825-e5e69e7941ef | -20.37457 | -48.82559 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 792d5729-7856-338d-bc72-e934578f5c68 | -20.37413 | -48.80101 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 50892903-185a-3250-b3aa-6681d05eee05 | -20.37384 | -48.82556 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 60e05dfb-5862-3a1e-b4ae-0e87d815c13c | -20.37372 | -48.82951 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 27f0fa40-92de-36b4-904a-10cb5db1ac19 | -20.37289 | -48.83334 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 45.3 |
| a979fa68-c5a0-311e-ab01-46dfeb0250f8 | -20.37127 | -48.83707 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 52f57dc3-92ff-390b-9e6e-45f6fde5b222 | -20.37082 | -48.81623 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9c93bc7a-8b46-3cb6-8b69-78d42ea6eede | -20.37041 | -48.84085 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 148.5 |
| 06edb2b1-740a-395b-9f26-ca5b86ff7fb9 | -20.36827 | -48.82797 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 6babd55c-976b-3ab4-a351-40b5b90807d3 | -20.36451 | -48.81871 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9d8a9762-d809-3ce2-9ed4-3cd764b1b8bb | -20.36326 | -48.7979 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 119a8687-5d66-3f34-9a08-6a959d515a71 | -20.36282 | -48.82645 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 11754e64-dce1-3cca-8209-d76c0e94cfcb | -20.36074 | -48.80946 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3e53a709-37e9-3e1e-902a-5abb190106dc | -20.36032 | -48.83798 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 174.5 |
| dcc6b55f-766e-3405-af5a-cec26fce6b6a | -20.35738 | -48.82491 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 775c351e-1c9b-3e21-9c19-d0e41d1b5ff6 | -20.35402 | -48.84032 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 174.5 |
| 67feacd6-77cd-31b1-9abb-bb7071b0668f | -20.35108 | -48.82727 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dad086ad-90b3-361c-b903-b7c2234909ab | -20.42079 | -48.7963 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7e4e9533-d6ea-3c1b-b1b6-f6d1fded8b3d | -20.41733 | -48.81199 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 964a694a-3f3f-3a5a-ab61-7447a5b4dd92 | -20.41647 | -48.81586 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5dbb5188-3f86-32d8-b610-d436fedb127c | -20.41617 | -48.79113 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 24e0bcf5-46e3-3b12-91da-897e3f87edec | -20.4156 | -48.81976 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 13.7 |
| d454e664-e4f1-3234-9ba0-79a5f96cf447 | -20.4153 | -48.79505 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f546c8df-671a-3406-bffd-ea3b177b70c4 | -20.41474 | -48.82364 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 79422a7b-f9f1-3a26-8736-9f3f3d9b10fb | -20.41186 | -48.81061 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 41c94fa8-59d7-38a4-beb8-58cd24b3c404 | -20.41099 | -48.81452 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 90bc6219-f787-3459-9bf1-d8f24441dddf | -20.41013 | -48.81841 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 13.7 |
| d956e8ee-0a1a-39d5-88a9-48cf8b8428d8 | -20.40927 | -48.82229 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 13.7 |
| ef24381d-ff95-3cb0-881e-2b24d7df9c87 | -20.4084 | -48.82619 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 10.3 |
| a204bfb8-534d-3922-a130-ea69c68f1f5f | -20.40754 | -48.83007 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 1e676907-4fc7-3cdb-ac4c-0f3a60f56b54 | -20.40637 | -48.80932 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 67e88773-12d5-351d-82c5-0139ea9065ab | -20.4055 | -48.8132 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e592204c-82e9-3177-832e-cd6ec23f9c56 | -20.40466 | -48.81702 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 11.8 |
| c9e31ac3-0488-38e3-b713-824590099557 | -20.40381 | -48.82085 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 50f23689-a127-3736-9a19-94f81ca589d8 | -20.40294 | -48.82474 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 5c21adb6-5b54-3ca4-80b1-e987af325027 | -20.40231 | -48.80404 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5d117276-fe75-3455-9067-921daf8cc152 | -20.40207 | -48.82864 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 69.6 |
| ae733437-7e8e-3ed7-bc4a-c28e8cead849 | -20.40147 | -48.80797 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c684998f-d884-325d-84cb-9284ccf449ee | -20.40089 | -48.808 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dbce70b7-e760-3c7d-9be1-bca5f5fa8453 | -20.40062 | -48.8119 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c566d40f-470b-3a06-a6e8-38f4fc61933d | -20.40002 | -48.81191 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c5f1b868-5e77-3b39-8f4a-aea6980a5adc | -20.39979 | -48.81575 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 2a59900e-04a7-32c5-ba4c-4318b0f97e86 | -20.39936 | -48.79097 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9574e41d-12dd-3c75-b7ba-054d1b925e0e | -20.39916 | -48.81575 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 5407b349-9a8f-38c3-af44-9785774ba4b4 | -20.39897 | -48.81956 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 36252e37-9bb0-3e5b-a65c-50a3779170f1 | -20.39888 | -48.79106 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ceb7c98c-6bc3-3ca5-afcc-fe8b0b2cee22 | -20.39852 | -48.79489 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6ca731f6-f985-3268-94c0-39005e83c80a | -20.39832 | -48.81955 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 11.8 |
| b38c63ef-8cc3-3b37-b4ec-34c08afffae0 | -20.39815 | -48.82339 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 4e4c2ff9-5917-3012-b41d-4044992aae94 | -20.39801 | -48.79497 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0465aa06-2581-3871-a42c-c7867916d249 | -20.39768 | -48.79878 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f8ed8506-fe74-3009-8d1f-69c4eb6dfcc2 | -20.39747 | -48.82335 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 342e8075-d07d-3378-8eed-b19951755baf | -20.39733 | -48.82722 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 24.9 |
| a3281a6d-9ca1-3506-b400-dadfd16a1383 | -20.39715 | -48.79885 | 2024-10-08 03:45:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README45.md)
