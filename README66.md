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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e9b10f5d-3d5a-3252-94ad-8ef81c983ff2 | -11.4743 | -44.2053 | 2025-10-19 14:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 175.2 |
| f88ad844-49bd-3973-9666-37c6da42304a | -10.7044 | -44.548 | 2025-10-19 14:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 133.1 |
| 5db126c0-9ca5-32ea-8479-47e5acf0325a | -6.2015 | -41.7148 | 2025-10-19 14:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 84.1 |
| 183ac171-2266-3dd9-91c7-2a7b6ddc8018 | -10.6853 | -44.5506 | 2025-10-19 14:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 156.8 |
| 5bf7ddd0-43f8-3788-9baf-f8a303390223 | 1.7846 | -56.0393 | 2025-10-19 14:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| aeba3999-192c-365c-bb2c-b0231c8a89c7 | 2.0416 | -55.74 | 2025-10-19 14:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 329c0096-5176-3b6f-9bd6-083b23fa89cf | -4.115 | -42.2011 | 2025-10-19 14:30:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 101.5 |
| df23ecec-b060-3acf-9014-546547b43fe8 | -6.5223 | -41.6376 | 2025-10-19 14:30:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 104.3 |
| 45d7b9d0-b06d-395b-8457-addf51e0c335 | -11.4939 | -44.179 | 2025-10-19 14:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 165.0 |
| 3148d6a4-d4a6-3988-9452-7daaf3e2e620 | -6.4448 | -41.8368 | 2025-10-19 14:30:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 95.7 |
| 9966bbcb-0df9-38de-8a97-0d38d1827bb0 | -12.34 | -41.182 | 2025-10-19 14:30:00 | GOES-19 | WAGNER | BAHIA | Brasil | 2933406 | 29 | 33 | nan | nan | nan | Caatinga | 90.6 |
| 37061851-2642-372a-8c14-cef329c95964 | -4.3874 | -43.3827 | 2025-10-19 14:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 1b286e30-fda9-3cc9-9ffe-6911376e27de | -4.7623 | -43.2434 | 2025-10-19 14:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| cf6825fa-1365-36e0-a15a-2fbaee2d48be | -6.4066 | -41.8882 | 2025-10-19 14:30:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 68.9 |
| 49fd6128-deee-3d28-a778-161c17f0bff2 | 1.7481 | -55.961 | 2025-10-19 14:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 105.6 |
| b1a74d06-c243-37e1-acf9-b492c5f9185d | 1.7298 | -55.9612 | 2025-10-19 14:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 202.7 |
| 1488be6f-0e5b-3c02-9bc3-e7170e8d0d16 | -10.2554 | -44.0506 | 2025-10-19 14:30:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 138.8 |
| 22bc466c-e5ca-386a-a47d-31daec9afc6d | -11.4355 | -44.2344 | 2025-10-19 14:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 194.2 |
| 88425c28-1482-35f8-8f05-98573c9b81dc | 2.0417 | -55.7203 | 2025-10-19 14:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 6c875f41-49b8-367e-a5b1-0fdf056f13a0 | -11.4376 | -44.1172 | 2025-10-19 14:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 143.6 |
| 88eae923-105b-3c45-b316-d2c4c5ebbda0 | -4.0962 | -42.2258 | 2025-10-19 14:30:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 94.3 |
| c6b89e3f-f9a5-34a1-976e-fecb3756abe3 | -10.6853 | -44.5506 | 2025-10-19 14:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 156.3 |
| 5134ddd2-bc5c-3832-b0b0-644d542792c1 | 1.7482 | -55.9216 | 2025-10-19 14:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 832d6db2-7741-3220-bc23-076ea3aa45ca | -6.2032 | -41.5464 | 2025-10-19 14:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 87.6 |
| 39a5ff49-7eae-3d57-b5c0-41ec911287fb | -4.171 | -42.2215 | 2025-10-19 14:40:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 105.8 |
| 5b57a966-0ced-379d-aca8-92ba0d294803 | -1.2455 | -49.0407 | 2025-10-19 14:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 67aea891-e50a-3ca2-b69c-fd8a261775db | -11.3992 | -44.1229 | 2025-10-19 14:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 195.0 |
| 8aa80925-4c5a-3e73-8170-3ee09ffb8119 | -6.4257 | -41.8625 | 2025-10-19 14:40:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 79.4 |
| ab00cbaf-5737-3f44-af46-dc9dca97cedc | -3.8371 | -41.7883 | 2025-10-19 14:40:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 138.8 |
| 3d255f62-e389-3dd4-8093-712ec808ee53 | -6.201 | -41.7629 | 2025-10-19 14:40:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 87.5 |
| 81180f22-c714-376a-95e2-6f476955bb0a | 1.7663 | -56.0395 | 2025-10-19 14:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 4a00fd6a-99c4-39c0-8c44-039523933d21 | -10.7044 | -44.548 | 2025-10-19 14:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 134.7 |
| cb56b3cf-0462-3574-8e0b-3de2140b1421 | -4.1525 | -42.1989 | 2025-10-19 14:40:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 101.0 |
| 3637207a-8fc8-3a49-a02e-e916b1e856d7 | -5.933 | -42.2395 | 2025-10-19 14:40:00 | GOES-19 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 70.3 |
| d3b5fae3-8991-34d0-a63f-c5a11b390b75 | -6.5223 | -41.6376 | 2025-10-19 14:40:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 68.0 |
| 6f2c27d3-4e7e-342f-b2eb-23cee77b5749 | -11.3996 | -44.0995 | 2025-10-19 14:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 186.6 |
| f417f52b-a09a-3842-90ad-181f76cf9e2d | 1.7481 | -55.9807 | 2025-10-19 14:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| a8e0c017-5ffe-36be-82fd-fbedd1b1961e | -11.4184 | -44.1201 | 2025-10-19 14:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 196.7 |
| 32669f19-8c43-3f64-9118-5f338cb2f590 | -4.4095 | -42.8911 | 2025-10-19 14:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| a1fdea08-b865-3ae0-a4fa-de929059eb3d | -4.4845 | -42.8631 | 2025-10-19 14:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 50b3951c-7e30-3371-8ef6-eecf64d16f9e | -5.9063 | -43.0677 | 2025-10-19 14:40:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 71.4 |
| 6db3db15-fef9-3b7a-9cbf-f93d5f8c3f65 | 1.7663 | -56.0198 | 2025-10-19 14:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| be35897d-d2c3-3973-b029-e936874d443f | -6.4637 | -41.8351 | 2025-10-19 14:40:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 82.5 |
| 571acabf-5898-3d4f-b818-b5fcf76d1869 | -7.4717 | -42.6658 | 2025-10-19 14:40:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 64.8 |
| cf9b5b21-2599-38d4-b74f-43732e6d9782 | 1.7481 | -55.961 | 2025-10-19 14:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 27d6c0a7-ab56-34a6-b594-a9ac13b44f20 | 1.7846 | -56.0393 | 2025-10-19 14:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 86.7 |
| d04c9db3-6fdd-3c70-ba93-abf5a67f9bc8 | 1.7846 | -56.0196 | 2025-10-19 14:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| ccc4b61d-d04e-374f-bab0-edfb4342f417 | 2.0417 | -55.7203 | 2025-10-19 14:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 89.1 |
| dada4ed4-b3d4-3f7f-be02-52366a74806f | 1.7298 | -55.9612 | 2025-10-19 14:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 5f7f1219-9d74-3270-86aa-d4ad74c6f1dd | -7.1756 | -42.1968 | 2025-10-19 14:40:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 98.9 |
| 31bedec9-e359-3229-a6bb-d9b626e15eb9 | -6.4632 | -41.883 | 2025-10-19 14:40:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 62.9 |
| 4643251c-d40a-3b4d-8a72-aacbf951c041 | 1.7481 | -55.9413 | 2025-10-19 14:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 102.6 |


