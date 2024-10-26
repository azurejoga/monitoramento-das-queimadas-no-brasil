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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 06c3ab3f-093a-3b56-ab1b-848a7f799aec | -4.58398 | -49.49319 | 2024-10-26 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 87076f8c-a09f-39fa-8300-d9ce5111bec4 | -4.18568 | -49.41345 | 2024-10-26 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b49afa9b-209a-3ad1-88e8-78563cad9def | -4.18234 | -49.41294 | 2024-10-26 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 50d0c3c1-3464-3b71-b135-ff611f1ca09a | -3.91898 | -49.38334 | 2024-10-26 04:44:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ff4dddfb-37dd-33e1-abed-9fa685ca723a | -3.91564 | -49.38282 | 2024-10-26 04:44:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4683e95f-005a-377d-b4f0-9f094a1da047 | -4.99167 | -49.86529 | 2024-10-26 04:44:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3dadccdf-acdc-3ccd-b1c7-bb4b003b8a48 | -4.99112 | -49.86877 | 2024-10-26 04:44:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c679e2d0-eced-3637-bb4c-fc51dfccc7ac | -4.97197 | -49.77264 | 2024-10-26 04:44:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aa0c34aa-72e9-3c4c-b2d0-701ccae24404 | -4.97142 | -49.77615 | 2024-10-26 04:44:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8928748a-f146-3efb-bcb5-0107ea1e87c3 | -4.96962 | -49.89762 | 2024-10-26 04:44:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 72203602-1ef7-3aa7-975b-6c2baf8aae61 | -4.9663 | -49.8971 | 2024-10-26 04:44:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5166efe6-1e5f-398f-b82b-123d513243ad | -4.95424 | -49.93092 | 2024-10-26 04:44:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0750d6e6-8749-3562-be49-371b4d5415f0 | -4.8599 | -50.77237 | 2024-10-26 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3c9c81fd-c6a6-3400-abff-bae318cb5803 | -4.82267 | -49.83887 | 2024-10-26 04:44:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 02a906ee-cfbf-3d84-9530-4a85a070c777 | -4.81453 | -50.88864 | 2024-10-26 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cd50d77f-5fc8-39f3-ad04-ede1cd16a01b | -4.81399 | -50.89209 | 2024-10-26 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1be86174-8710-3184-8382-4a40f6cf55e5 | -4.812 | -50.72924 | 2024-10-26 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b8527678-83d2-3e6d-84ae-bc2b3f84b087 | -4.73984 | -50.69331 | 2024-10-26 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd0cee32-e44c-3afb-9f70-289e18d9b3ea | -4.72691 | -50.79702 | 2024-10-26 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7eb90d89-8a58-3d4f-86ba-969652291217 | -4.65606 | -50.77179 | 2024-10-26 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bb06a7c2-d286-3a51-9248-ba7c141c222e | -4.62438 | -50.65055 | 2024-10-26 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9352698f-a138-3b60-a380-06f81f0f4c46 | -4.40747 | -50.73303 | 2024-10-26 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3018863e-0049-31dd-802c-09751221465a | -4.40693 | -50.73647 | 2024-10-26 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c8270bd-e83a-3208-94b0-48e759d4adf7 | -4.40363 | -50.73596 | 2024-10-26 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 87343dd8-7903-3404-a6df-5b01780f8f9d | -4.3965 | -50.51954 | 2024-10-26 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d5cb7b88-3dec-3534-a281-67bca874c63d | -4.29808 | -50.73665 | 2024-10-26 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d0883b2b-474b-3351-b0fa-b595d15e4c23 | -4.29532 | -50.7327 | 2024-10-26 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3d74b5ea-4ac1-342b-9ff8-9085afc85d88 | -4.29202 | -50.73218 | 2024-10-26 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f9eaceee-23ba-314c-956a-876153b5cd9b | -4.29147 | -50.73561 | 2024-10-26 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0b67b484-122a-3319-94af-beacacd4ce22 | -4.29093 | -50.73906 | 2024-10-26 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b07a75d-ae81-3b11-aa8d-255e8eff6c87 | -4.23308 | -50.63132 | 2024-10-26 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0de2ab53-096b-3310-b030-815752929c11 | -4.22978 | -50.6308 | 2024-10-26 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 938211e4-5db1-368a-aefd-75ab2188a93c | -4.22924 | -50.63424 | 2024-10-26 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9308d4c-aea3-3411-b884-1b6206847989 | -4.09553 | -49.99237 | 2024-10-26 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b874a1a-d51b-3567-ada7-f64e69ee29cf | -4.03584 | -50.43811 | 2024-10-26 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75c1de9f-2eab-3601-84d3-5ce78024ec8f | -3.95752 | -49.89673 | 2024-10-26 04:44:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0542daec-47ed-33eb-b140-1cfed96d9ad0 | -3.95698 | -49.90019 | 2024-10-26 04:44:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3703ddb0-bb93-3045-8833-ad1e6dbc3360 | -3.92156 | -49.86635 | 2024-10-26 04:44:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5973b4ce-1b2d-31e7-824c-e21c36679ac0 | -3.88244 | -50.05131 | 2024-10-26 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed470c85-1c8c-34ed-acd4-023db9325886 | -3.87913 | -50.0508 | 2024-10-26 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46e26446-8bba-38dc-82c6-83cb9b0717b4 | -3.77725 | -49.83299 | 2024-10-26 04:44:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81cc8493-d556-3014-a5b6-52029b674826 | -3.77394 | -49.83248 | 2024-10-26 04:44:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a97ac3e2-ff87-356c-9927-faef29537aae | -3.70758 | -50.16833 | 2024-10-26 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 06933735-6cb5-3eda-a171-a21cb1859bdd | -3.70704 | -50.17177 | 2024-10-26 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5ddb470f-4271-30d7-abd3-a5913da7f066 | -5.33558 | -50.87893 | 2024-10-26 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| efec96f5-84ab-338b-9136-a11bb8948d1e | -5.33228 | -50.87841 | 2024-10-26 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02645e52-37f8-32b5-88cf-adaed266767e | -5.32898 | -50.87789 | 2024-10-26 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7aeb5caa-2dcc-3190-a5c7-3fbf6ef343c6 | -5.28852 | -50.9845 | 2024-10-26 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c52cabab-937e-32ad-98bb-7feb5df8745e | -5.26246 | -49.5207 | 2024-10-26 04:44:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ce03e24e-c6db-3813-848a-31d03e72aaa9 | -5.2591 | -49.52018 | 2024-10-26 04:44:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6f9706e5-b459-3294-9dae-1123090b8aed | -5.24605 | -50.69169 | 2024-10-26 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cdcb902e-e6d9-3083-beed-ffe18997c668 | -5.06989 | -50.58297 | 2024-10-26 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed93e382-3974-3e74-ab3a-11ba41e6e048 | -6.43627 | -49.90092 | 2024-10-26 04:44:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f75e449d-be27-3ce2-957c-926a20a2b6c5 | -6.41013 | -50.78694 | 2024-10-26 04:44:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ca6a6ab-8949-3701-b085-997bc0fbb99b | -6.40905 | -50.79383 | 2024-10-26 04:44:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c5f55d7-761b-3f0b-943f-c0231783f012 | -6.22009 | -50.87347 | 2024-10-26 04:44:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a0f7f863-20a1-30cf-9159-937500334f95 | -6.21019 | -50.87191 | 2024-10-26 04:44:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 297ffe0a-a537-3425-8c69-16565a7a18e2 | -6.20541 | -50.85695 | 2024-10-26 04:44:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 154cfada-1128-373c-863d-65549cc32e55 | -6.20211 | -50.85644 | 2024-10-26 04:44:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d3c8e175-0282-33a0-98b4-b893dbdac10c | -6.19881 | -50.85592 | 2024-10-26 04:44:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2f164db7-50ac-3a8a-8d95-fdf5c2066a54 | -6.19827 | -50.85937 | 2024-10-26 04:44:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0aadc76c-1fdf-3710-a985-22fadea825cc | -6.1922 | -50.85489 | 2024-10-26 04:44:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ba7ed846-d738-3a0e-a97e-acbdf508d0d6 | -6.1856 | -50.85385 | 2024-10-26 04:44:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| db1d4588-5df8-3d35-9498-98b2fb53bbc1 | -6.18176 | -50.85678 | 2024-10-26 04:44:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5006341-efa5-3aff-a08a-efd41bd7e629 | -6.17791 | -50.85971 | 2024-10-26 04:44:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 50557dfa-61fa-363b-a42c-2d6f336a64e8 | -6.10371 | -51.11654 | 2024-10-26 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0de4cbc8-1eec-3ea8-8e94-2184fa98adbe | -5.95426 | -50.87776 | 2024-10-26 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf605043-9463-31c3-9774-08a055f99fdf | -5.95371 | -50.88121 | 2024-10-26 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a5f4543-7a30-3fe1-8d48-f06b754726ca | -5.95041 | -50.88069 | 2024-10-26 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bd7c0f62-2aaa-3628-af66-ea9872a4b9ea | -5.94927 | -50.86639 | 2024-10-26 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc7a93e0-259f-380a-bca1-85ca537ffbe8 | -5.94711 | -50.88018 | 2024-10-26 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c3e5c6b6-d340-3616-8727-e4722172be4a | -5.94543 | -50.86932 | 2024-10-26 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 152591a9-a074-3655-a8dd-18ccc1640d64 | -5.94489 | -50.87276 | 2024-10-26 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1171be09-a70d-3526-9fa1-3312aa9f1b87 | -5.93828 | -50.87173 | 2024-10-26 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1bf7cb6a-28b1-3e52-ac00-de525fe658bd | -5.8526 | -50.35546 | 2024-10-26 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fdf84c70-b83e-3127-9f14-22d5fb739d2b | -5.75457 | -49.82818 | 2024-10-26 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fa20f533-cf7e-3dd6-9972-adcfda79d58e | -5.5722 | -51.08185 | 2024-10-26 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d77544ec-2b45-321f-b055-a0e41e468dfd | -5.49785 | -50.58364 | 2024-10-26 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c25982b4-9b5b-3ac3-b3e0-1fa744865a88 | -5.28797 | -50.98795 | 2024-10-26 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fbf5a88d-a0d8-3173-afd7-f3065cde3508 | -5.24935 | -50.6922 | 2024-10-26 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 737ccd7b-42d8-3995-9c6b-3b3c01cc66de | -5.24881 | -50.69564 | 2024-10-26 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cf2ba33e-876d-3842-be53-fce34e9193e8 | -5.18081 | -50.11191 | 2024-10-26 04:44:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00f1b098-e551-3979-b977-c72ae44c8da7 | -5.07043 | -50.57957 | 2024-10-26 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0ff9d74-7bc9-3f2c-92c4-5501ae11a724 | -5.06712 | -50.57906 | 2024-10-26 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 65b793fe-2917-3c4c-ae1c-ade02bffb92d | -6.4162 | -50.79141 | 2024-10-26 04:44:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 144918e3-cc09-367e-b4ed-339bacccef83 | -6.41236 | -50.79435 | 2024-10-26 04:44:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a9d2f69-b9cc-3542-bf0d-8ce433c0561f | -6.40959 | -50.79038 | 2024-10-26 04:44:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2794dba7-461a-39ec-9203-7498ba978f7f | -6.40629 | -50.78986 | 2024-10-26 04:44:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f469d0e8-4a35-3c56-b0a9-7a02c4a7f66c | -6.22892 | -50.88191 | 2024-10-26 04:44:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3afe0b7e-4bc4-30d4-9b10-89a82b5060c2 | -6.2267 | -50.8745 | 2024-10-26 04:44:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9eb4590-8d1c-3e91-9fda-472685b06ad8 | -6.22394 | -50.87053 | 2024-10-26 04:44:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5ca47588-414f-3201-a907-beae18dcd1b5 | -6.2234 | -50.87398 | 2024-10-26 04:44:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91055820-198a-3c62-819b-260af1e9ccbe | -6.21349 | -50.87243 | 2024-10-26 04:44:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 934d842c-c938-3beb-98a4-73e8668d21d6 | -6.19773 | -50.86282 | 2024-10-26 04:44:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b4510a49-bda6-36fd-8d68-62d9aa88459d | -6.19551 | -50.85541 | 2024-10-26 04:44:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c8927394-22c8-3d7d-997c-765d3acd56c3 | -6.19496 | -50.85885 | 2024-10-26 04:44:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2fbbe45d-a368-3512-9a53-7645089e912e | -6.19275 | -50.85144 | 2024-10-26 04:44:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8530c4c4-7f3d-3960-8aa5-174abacf0cd1 | -6.1889 | -50.85437 | 2024-10-26 04:44:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d780558-f166-3cb9-b139-d2152312c998 | -6.17845 | -50.85627 | 2024-10-26 04:44:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 906d3d2b-e898-3e12-b581-e98af42c5852 | -6.16591 | -50.89314 | 2024-10-26 04:44:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README82.md)
