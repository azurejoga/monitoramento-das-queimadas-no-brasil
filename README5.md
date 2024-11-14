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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c7e035a1-0db0-373c-97f1-c8cc1b1df25a | -1.377 | -52.3508 | 2024-11-14 00:32:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54676eae-41b9-347d-8c62-2ba9a8f63f8b | -3.3769 | -43.9352 | 2024-11-14 00:32:00 | METOP-B | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0ec3fa4d-8952-384f-811a-78ba21142939 | -4.9323 | -44.9547 | 2024-11-14 00:32:00 | METOP-B | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5ed3566a-ed43-32f6-b2a8-b643da425a4b | -3.4033 | -50.367599 | 2024-11-14 00:32:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61a46833-7eec-3f0f-be7e-cc4f65042b8e | -2.6216 | -46.172401 | 2024-11-14 00:32:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4b7f657b-c075-3922-98c5-80f634fd5061 | -2.1057 | -50.691502 | 2024-11-14 00:32:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf4687c5-071f-318a-a913-20947591e1c1 | -4.5153 | -46.480598 | 2024-11-14 00:32:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 391b6e14-1154-3b14-9a3d-28c009973b41 | -1.3786 | -52.3578 | 2024-11-14 00:32:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a73ab1f8-3c02-34ec-ae2e-a8a4d1e6acd7 | -3.1541 | -50.587601 | 2024-11-14 00:32:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a505145-76ee-3f4a-8503-3299ab2fe26d | -1.3947 | -52.383701 | 2024-11-14 00:32:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c124696-ea29-3119-8e16-9d548a62bf61 | -4.5779 | -46.617599 | 2024-11-14 00:32:00 | METOP-B | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1a71eb67-570b-3294-84ef-9dca8a1c4cab | -4.1296 | -43.8596 | 2024-11-14 00:32:00 | METOP-B | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a63edcb6-33d6-34de-92df-2e52fd3f7d21 | -4.2596 | -48.1922 | 2024-11-14 00:32:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc5460eb-db62-37ae-a31c-3fab87513da5 | -3.4715 | -50.259102 | 2024-11-14 00:32:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45c1ece7-b675-3950-ae99-fb45cb590fcb | -3.2949 | -50.024899 | 2024-11-14 00:32:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c29319ec-b662-3907-adb0-b385c9a4e9bd | -5.8509 | -46.4179 | 2024-11-14 00:32:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 51c72c03-d821-32d9-9044-983f6b2f2857 | -3.1116 | -50.216999 | 2024-11-14 00:32:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6f2e63b-f28a-3755-94a7-a80a9a1cbcc0 | -4.7822 | -43.663601 | 2024-11-14 00:32:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 13cdc77b-a1d7-3fe2-b2ac-24c6ec969eca | -4.0256 | -47.216599 | 2024-11-14 00:32:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 916c8cae-1560-3d65-8736-c45485c684a9 | -2.6627 | -46.9785 | 2024-11-14 00:32:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8ca7f0d-1f37-3d96-906e-bf921a6cfc36 | -1.8274 | -46.0737 | 2024-11-14 00:32:00 | METOP-B | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d1a54e30-7545-3701-afce-4c1d8dea2c85 | -4.2878 | -48.089901 | 2024-11-14 00:32:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f175cc7-aeb3-3a72-a54d-2464f4f46fed | -5.5997 | -46.401299 | 2024-11-14 00:32:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c5628de2-e445-3a1c-8bff-d3a32035d0dc | -1.2068 | -51.777699 | 2024-11-14 00:32:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 847d13a8-1d29-3d52-b3c1-b283045e7bef | -5.4704 | -47.0009 | 2024-11-14 00:32:00 | METOP-B | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d57ae0ad-aa13-3824-a113-cebd03a0bc27 | -4.1448 | -45.771198 | 2024-11-14 00:32:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f7c5f467-5d37-320d-b640-dcbda41da28d | -2.0506 | -52.047901 | 2024-11-14 00:32:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ac92ff4-403a-34a5-ad3e-cf0c6c90956e | -1.2644 | -52.170502 | 2024-11-14 00:32:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd522198-19d4-3a7a-a86d-98b0e9573378 | -2.2298 | -47.4715 | 2024-11-14 00:32:00 | METOP-B | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79271945-47a8-30d1-af0c-2a7667c7866b | -3.1625 | -50.4426 | 2024-11-14 00:32:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76dea41d-3103-30bc-8990-e8a2e6fc3c06 | -1.0335 | -52.426498 | 2024-11-14 00:32:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73735f9b-d409-33bf-9e2f-24e722322762 | -3.0259 | -45.073799 | 2024-11-14 00:32:00 | METOP-B | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cefccc3d-24b1-32c6-89da-5b9b800e13bb | -1.397 | -51.112999 | 2024-11-14 00:32:00 | METOP-B | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32786093-cd40-3254-8d89-beb1e498c8bc | -2.6568 | -46.817902 | 2024-11-14 00:32:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 643f2a78-f0f8-3663-a611-b4491801214c | -1.3316 | -46.557999 | 2024-11-14 00:32:00 | METOP-B | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13550476-270c-3490-b2d8-48c77089adc9 | -2.6412 | -46.1679 | 2024-11-14 00:32:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 152cb335-e9a0-3d7f-8ef4-b5cb533609f6 | -3.8149 | -51.924099 | 2024-11-14 00:32:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ad239cd-26e7-3ccf-bbaa-833ae9ca2e2e | -6.0423 | -44.030899 | 2024-11-14 00:32:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 55e2a908-8bdb-30b5-9c3e-67ac074bcf10 | -5.9269 | -39.6689 | 2024-11-14 00:32:00 | METOP-B | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 9539f6f9-85d2-3f62-8862-20fd15adf91e | -2.9493 | -51.004902 | 2024-11-14 00:32:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40b6954d-f955-359d-be10-f3ad33855863 | -4.3745 | -50.653198 | 2024-11-14 00:32:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0dea710d-58e2-3a65-8283-e08d43dcc659 | -3.4798 | -50.250198 | 2024-11-14 00:32:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6536a240-6c04-3f4c-b342-f3b823f2dda8 | -2.8775 | -51.785099 | 2024-11-14 00:32:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60b3b326-f582-359d-a033-3680add9e361 | -4.7502 | -49.0779 | 2024-11-14 00:32:00 | METOP-B | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 911023e8-b77c-3667-bbe5-4b77827cd84b | -4.2631 | -43.728298 | 2024-11-14 00:32:00 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 47bfa501-f13b-39dd-aa94-7b971580e705 | -3.2447 | -50.395699 | 2024-11-14 00:32:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9faf59e1-e2bf-307a-8b65-44ea87cdd49c | -2.657 | -46.9986 | 2024-11-14 00:32:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b91f59b-aa13-3baa-9d87-1fc22143125f | -1.0351 | -52.433498 | 2024-11-14 00:32:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fdb01b85-c8f2-3d16-bd40-7fe406e7527e | -6.8652 | -44.764 | 2024-11-14 00:32:00 | METOP-B | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 711c45b1-3416-328b-bb15-ce6bf8aa3c60 | -17.5714 | -57.484798 | 2024-11-14 00:32:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f2c12782-fa01-36fe-aeb0-56310290695d | -2.876 | -51.778198 | 2024-11-14 00:32:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66a471c8-43a3-32a9-81ef-88a31767ad28 | -2.19 | -46.353901 | 2024-11-14 00:32:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a853b953-cac7-38ce-82ea-5762faf663e2 | -4.1414 | -46.244701 | 2024-11-14 00:32:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c8f0d3f0-d6b8-3a62-9891-0d5dd098041e | -1.6551 | -52.534 | 2024-11-14 00:32:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71e2955d-7e66-3aaa-ac03-121e559bac2c | -3.3671 | -43.937401 | 2024-11-14 00:32:00 | METOP-B | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1624f8be-5860-37d4-8b7f-3dc1b9efd025 | -3.997 | -45.578499 | 2024-11-14 00:32:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2394b031-8ae9-35d9-a72d-fd3a7c5024c9 | -1.403 | -52.3745 | 2024-11-14 00:32:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df577327-749d-37b9-9e6f-7d5806f8a4b4 | -1.5695 | -52.015701 | 2024-11-14 00:32:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0dbb83b4-7b06-355d-9c87-71339432ef53 | 0.6688 | -51.777302 | 2024-11-14 00:32:00 | METOP-B | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 7a28553f-657b-3e2e-9e42-14dc1f6596dc | -3.7034 | -50.6017 | 2024-11-14 00:32:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f80f3eb0-72e1-3778-a4e4-448c498a14f0 | -3.6383 | -50.587399 | 2024-11-14 00:32:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02e52b0f-4d7c-322f-8eb6-0d958249a3a0 | -0.2157 | -51.4958 | 2024-11-14 00:32:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| a4a4eeae-80f4-3fdf-a5f2-a1d325da7dcb | -4.777 | -46.098598 | 2024-11-14 00:32:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| adaa1029-4eb8-33a8-b9f9-6507aaf8eeec | -3.0418 | -50.318802 | 2024-11-14 00:32:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d2253d0-b2f2-36c6-b58c-83e4b3af191c | -5.0614 | -45.505901 | 2024-11-14 00:32:00 | METOP-B | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 84c7bf4c-0a91-3abd-87ed-dc04daa50bd4 | -1.6048 | -52.492901 | 2024-11-14 00:32:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e259b697-1ba9-3fc1-970d-36cf5eed983d | -2.5278 | -47.018398 | 2024-11-14 00:32:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83c661f2-f993-3541-b9b9-461b5bbf4d44 | -3.727 | -50.431801 | 2024-11-14 00:32:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f65a5430-f134-3c9c-9d20-12a8747f0c8e | -4.0536 | -50.007301 | 2024-11-14 00:32:00 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 98a2284c-314d-31fa-b093-d40184c3ee2c | -1.5534 | -51.852501 | 2024-11-14 00:32:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ffe6f90-5317-34fa-85f5-59def82c6ba4 | -3.0232 | -45.062199 | 2024-11-14 00:32:00 | METOP-B | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 31a9c627-df50-3ab0-94fb-5a87e26a527d | -3.7383 | -50.436401 | 2024-11-14 00:32:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3713f408-9586-3899-8d98-739fa1ba5f50 | -2.6687 | -46.824799 | 2024-11-14 00:32:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c083881d-2555-3ab1-ac4d-8cc3331c1b43 | -0.3341 | -52.021099 | 2024-11-14 00:32:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 6bc06872-27ea-3a0a-84d8-d9065242d958 | -2.2086 | -48.372101 | 2024-11-14 00:32:00 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d32b62c0-0279-3e7c-9a75-0e2564832fd0 | -17.584999 | -57.506001 | 2024-11-14 00:32:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8610a71e-0c3b-3c92-87f8-5aa762324c1c | -3.262 | -50.563702 | 2024-11-14 00:32:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4bcc5d19-f3d2-3aaf-b012-0ff82834074a | -4.2579 | -48.184601 | 2024-11-14 00:32:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c432befa-486d-3e9c-9adc-ce3037d47037 | -2.0641 | -46.567101 | 2024-11-14 00:32:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 004a5c62-8ff1-3d75-bd82-048d41cb4feb | -3.7019 | -50.594898 | 2024-11-14 00:32:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 794bcd8e-905b-3472-9c6d-d7b523ea72c4 | -1.6567 | -52.5411 | 2024-11-14 00:32:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a42d2cb-bddf-3388-a90f-9a804dace75e | -2.6393 | -46.831402 | 2024-11-14 00:32:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0593dda-0f36-3159-beb8-4d96102cfeea | -1.982 | -46.254101 | 2024-11-14 00:32:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb9c8eb0-ee53-383c-86cd-a1b23e609ca4 | -3.6301 | -50.596401 | 2024-11-14 00:32:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e896eb96-ccc8-3104-b3cf-5800672d41a9 | -2.8692 | -51.7943 | 2024-11-14 00:32:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fef236b8-aefe-3579-9a41-8d03d06a496a | -2.206 | -53.704102 | 2024-11-14 00:32:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6dfb4848-b031-3cf2-9c0c-e2ed5bbedfed | -2.6668 | -46.996399 | 2024-11-14 00:32:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 379ef5bc-576e-39d9-a795-4ec2449135b3 | -0.7848 | -49.4986 | 2024-11-14 00:32:00 | METOP-B | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c02223a5-b2df-3d79-9fa6-42056c05d59b | -2.6239 | -46.182301 | 2024-11-14 00:32:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d4e0c479-ca27-3450-be5b-8b6196dee946 | -2.4038 | -45.228401 | 2024-11-14 00:32:00 | METOP-B | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9996d2ce-bdf3-33fa-884c-eecfaf245a41 | -4.2665 | -48.222401 | 2024-11-14 00:32:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 922a9e64-c7f2-3770-a875-8286dc065560 | -0.6471 | -52.357899 | 2024-11-14 00:32:00 | METOP-B | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 6daeb2ff-1b4f-31b2-9e05-35066683802c | -4.3064 | -46.735802 | 2024-11-14 00:32:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c7472e6b-9de9-3f38-9976-630c5dcd3e38 | -5.8489 | -46.409 | 2024-11-14 00:32:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 574a6618-912f-369b-b889-79edb00a4d04 | -5.181 | -44.349602 | 2024-11-14 00:32:00 | METOP-B | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 29764dea-29ec-3e09-a862-08aa625fe01e | -4.276 | -46.871799 | 2024-11-14 00:32:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cd8465f5-1105-3991-a384-1d610298db63 | -3.1875 | -50.279202 | 2024-11-14 00:32:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce42a8e2-63ce-3b51-8fb6-0f6d4a46bc02 | -3.6465 | -52.2757 | 2024-11-14 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 193f9a10-a207-30e0-8f28-06c4c8e98d5e | -4.4341 | -46.575298 | 2024-11-14 00:32:00 | METOP-B | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 450f76ce-4ae9-37c1-afc2-40406e9ab45f | -4.0619 | -49.998299 | 2024-11-14 00:32:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README6.md)
