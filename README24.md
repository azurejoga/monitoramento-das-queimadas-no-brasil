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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 65144a72-a56e-3354-ab93-264bad698d56 | -17.24678 | -57.47309 | 2024-11-12 05:59:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| eccf19ca-314f-3907-9fec-b5571eb83c46 | -16.94258 | -57.64537 | 2024-11-12 05:59:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| ba4bad5e-81f2-3120-86d5-c0b6436fd409 | -16.95154 | -57.64684 | 2024-11-12 05:59:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.6 |
| e2f5aa34-a98d-3a80-b6bd-c57381f6c541 | -16.09734 | -60.10243 | 2024-11-12 05:59:00 | AQUA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b5f08148-6090-3593-9fe8-144f9fb06446 | -19.62482 | -54.15106 | 2024-11-12 05:59:00 | AQUA_M-M | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2c05b323-7c36-3e7d-84d3-791adda8c229 | -2.1271 | -50.6912 | 2024-11-12 06:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 117.4 |
| 2faee940-83e9-3aa2-b71a-64670924b8d5 | -2.1272 | -50.6703 | 2024-11-12 06:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| e834b00b-d670-3394-8cf0-f8e56938a799 | -2.1271 | -50.7121 | 2024-11-12 06:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| c91e4691-d6a7-33fe-906a-2a05a6b425ab | -2.1455 | -50.6908 | 2024-11-12 06:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| bdb587ca-9aeb-347a-a24c-4cb9a8284d10 | -2.1087 | -50.6916 | 2024-11-12 06:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 55a2853d-453b-3466-a4e0-2933b4c91750 | -3.1096 | -54.3066 | 2024-11-12 06:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 362aa23d-f81c-315f-a6f8-63167b166ac8 | 1.06046 | -60.61151 | 2024-11-12 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 079f3896-7078-36cb-8b15-3e9eca796b5e | 1.06424 | -60.60031 | 2024-11-12 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 80262218-a2e7-33c7-afb6-12612f009ebb | 1.08758 | -60.59654 | 2024-11-12 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e0a79e1c-146e-3ab6-aee1-3b4efbaebd85 | 1.05934 | -60.59394 | 2024-11-12 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4aa77c4c-8e7f-34c0-a812-7ffddcd69650 | 1.0622 | -60.61116 | 2024-11-12 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 12aacf42-4c21-3b79-9d4c-61c798bca7cd | 1.0534 | -60.602 | 2024-11-12 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f2d16edc-235c-3857-a06f-6d7d48afe7be | 1.05991 | -60.60807 | 2024-11-12 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2abee59-bcc4-3c21-b074-0dd1c198789b | 1.05992 | -60.59741 | 2024-11-12 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2e15f659-3965-351e-9ffb-6bf3e3498cae | 1.06163 | -60.60774 | 2024-11-12 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e85444b7-24d0-366b-af96-3151b0c64c55 | 1.05773 | -60.59423 | 2024-11-12 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| eb3cb697-011e-3156-b37f-854b333a5b38 | 1.05828 | -60.59771 | 2024-11-12 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1a07354b-8dc3-3184-a062-8a217b57d99e | 1.05882 | -60.60117 | 2024-11-12 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a243f25f-6357-306c-aea1-94b676556d84 | 1.06049 | -60.60086 | 2024-11-12 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 430afe95-1f73-311e-b526-3ac70519442e | 1.06533 | -60.6072 | 2024-11-12 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a33e41b9-7c23-3489-8bb9-aea552404513 | -16.08991 | -60.11764 | 2024-11-12 06:07:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 517398f1-9942-348e-b51c-1500af9e14d8 | -16.09058 | -60.11084 | 2024-11-12 06:07:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b72486d2-50d8-376b-95b6-768db18844da | -2.7588 | -49.3285 | 2024-11-12 06:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 6c1151f3-357a-3262-8c5f-aa10d2c6c373 | -2.7587 | -49.3497 | 2024-11-12 06:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| ab832d3d-f6a3-3ab7-b5e9-740609a71b7e | -3.0913 | -54.307 | 2024-11-12 06:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 32178428-db8f-3cb0-ae22-11f3c2a003b1 | -3.0504 | -50.3332 | 2024-11-12 06:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 116.9 |
| b79b53a2-9215-3c64-8896-106e22730477 | -2.1271 | -50.6912 | 2024-11-12 06:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 133.2 |
| b584e77a-da1d-3697-81eb-8c484699968e | -2.1271 | -50.7121 | 2024-11-12 06:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 9cca5993-7206-3f9f-98ca-e847b30fc5c0 | -2.1087 | -50.6916 | 2024-11-12 06:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| c3ac5444-c278-3275-8bea-350c5d771c75 | -3.0689 | -50.3326 | 2024-11-12 06:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 130.9 |
| c6ceff70-44b6-34ce-a0c2-453c007cf677 | -2.1455 | -50.6908 | 2024-11-12 06:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 0aae1195-8cf1-3405-95e3-4169aa48860a | -3.1096 | -54.3066 | 2024-11-12 06:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 29c3f0e4-b4e5-3fa2-9912-da4da9a2413d | -3.1097 | -54.2865 | 2024-11-12 06:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 81cbbba1-d541-33a5-8fb9-da4c4d783b3b | 1.048 | -60.5986 | 2024-11-12 06:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 46.3 |
| fb0ff6f8-db09-38de-8be8-96e45ba00201 | -3.0505 | -50.3122 | 2024-11-12 06:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 6c520cd4-fa65-302d-8c3b-c1d097d92c01 | -3.1096 | -54.3066 | 2024-11-12 06:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| f2a69782-18d4-36b5-8410-aa1b1ec8580c | -3.0504 | -50.3542 | 2024-11-12 06:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| f9566bf7-6cf1-3fea-a908-c95b7b72c84a | -3.0504 | -50.3332 | 2024-11-12 06:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 175.1 |
| 807b3b4a-d75c-3e4e-9ee8-3feac00efe0e | -3.0688 | -50.3536 | 2024-11-12 06:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| ed299fe3-931e-30e8-9bdd-b51368fab5d9 | -3.069 | -50.3117 | 2024-11-12 06:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 1e14a7fb-dd84-3d22-8729-e0c4c954593b | -2.1271 | -50.6912 | 2024-11-12 06:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 135.6 |
| 74d94f3e-7e9a-3edc-85a9-691ce4c6f4b2 | -3.0689 | -50.3326 | 2024-11-12 06:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 248.7 |
| 91b52cc7-5a8f-3dff-9058-81ec0ccf3c54 | -2.1087 | -50.6916 | 2024-11-12 06:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 267a4844-6079-386d-baac-b0164d6fcb70 | -2.1271 | -50.7121 | 2024-11-12 06:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 0a717aa3-1494-3118-888f-eb2a666aacbe | -2.1271 | -50.6912 | 2024-11-12 06:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 96.9 |
| e8d9e09e-b4ef-3b9e-adf4-a26bc4a95d09 | -2.1271 | -50.6912 | 2024-11-12 06:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 98.9 |
| ac3cbd2d-96ed-313e-bf64-7c1464cd0da9 | -3.0349 | -45.2546 | 2024-11-12 06:40:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 38552a0a-b6da-326c-9581-665701fe8371 | -2.1087 | -50.6916 | 2024-11-12 06:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 1a1fc22c-fc08-3036-abcf-95bfb623919d | -3.0535 | -45.2539 | 2024-11-12 06:40:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 70f54c17-71d2-3525-97b0-ac0b0e0e96e2 | -2.1271 | -50.6912 | 2024-11-12 06:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 4fa4cc44-69e5-33b3-b781-e076f638b1bb | -3.7806 | -44.9521 | 2024-11-12 06:50:00 | GOES-16 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 58ceb964-59f5-349c-b5b1-a91ed9da1496 | -2.1087 | -50.6916 | 2024-11-12 06:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 2fc1fabb-0e7c-3ea1-a3b0-accb808ef81b | -3.0534 | -45.2764 | 2024-11-12 06:50:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 106.4 |
| 8f303d40-2962-3785-9407-7755c963f0c8 | -3.762 | -44.9529 | 2024-11-12 06:50:00 | GOES-16 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 80.4 |
| c7541676-76ba-32f5-9e68-f1b3bbd4d660 | -3.1279 | -45.2511 | 2024-11-12 06:50:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 99.4 |
| a2bb723d-d3b2-31ab-aff0-71ccdfb2c505 | -3.0535 | -45.2539 | 2024-11-12 06:50:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 141.3 |
| f885a5ba-9ffb-3dfc-bfd0-08a89f6bea7e | -3.0349 | -45.2546 | 2024-11-12 06:50:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 1e956340-205e-38ba-bb73-dff2f600df1a | -3.0535 | -45.2539 | 2024-11-12 07:00:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 8c30f6e0-541d-3e52-8c31-9f49937d4ace | -2.1271 | -50.7121 | 2024-11-12 07:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| ab6a2fb5-27fc-3096-80f6-e96ae1508cd7 | -2.1271 | -50.6912 | 2024-11-12 07:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 130.4 |
| 38c769e8-2795-39aa-a9e6-608e87ebfb73 | 1.0663 | -60.5985 | 2024-11-12 07:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 4e54ee1e-4fea-3d18-b62c-138cc1c25401 | -2.1087 | -50.6916 | 2024-11-12 07:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| d550df97-7b60-39b5-85c4-0042a200ab01 | -3.1279 | -45.2511 | 2024-11-12 07:00:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 116.0 |
| f759f6e6-37b2-3858-965b-cbb6fca45c0f | -3.7806 | -44.9521 | 2024-11-12 07:00:00 | GOES-16 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 125.1 |
| 00408748-8b5e-30b4-8fe0-9ffd3a6d488e | -3.128 | -45.2285 | 2024-11-12 07:00:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 098ddd39-2148-30e4-844a-ebd08f79dd95 | -2.1087 | -50.6916 | 2024-11-12 07:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 08bc34d6-39d6-3c99-bccf-acafa1d8033c | -3.0535 | -45.2539 | 2024-11-12 07:10:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 0bdb9d21-7be9-3cbf-bf8d-20d41d9cd5d1 | -3.3543 | -44.6079 | 2024-11-12 07:10:00 | GOES-16 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 107.2 |
| 851fcd60-82f2-3b19-81a8-d0c2664c7431 | -3.1279 | -45.2511 | 2024-11-12 07:10:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 133.2 |
| b8735aeb-deeb-3cab-8392-8a49e0d652ff | -2.1271 | -50.6912 | 2024-11-12 07:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 110.6 |
| a93204b8-a34f-3700-8dca-f45857709700 | -3.3543 | -44.6079 | 2024-11-12 07:20:00 | GOES-16 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 4e46fd81-4aa4-3c8a-af97-856acb67eff4 | -3.1279 | -45.2511 | 2024-11-12 07:20:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 91.1 |
| d8e9eea5-04ee-35d1-92bd-cb66bc0c697d | 1.0663 | -60.5985 | 2024-11-12 07:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 48.9 |
| a722297e-a133-3b71-85b1-549503f6672d | -17.2933 | -57.4857 | 2024-11-12 07:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.2 |
| 27e13a23-8474-37ef-a3ae-51346265d80b | -17.254 | -57.4903 | 2024-11-12 07:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.6 |
| 79d85a46-8605-3eb5-a9f0-8d69559a97a9 | -17.2936 | -57.4652 | 2024-11-12 07:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.9 |
| aac1ffde-6205-3786-bc48-3182b7699844 | -17.2543 | -57.4698 | 2024-11-12 07:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.2 |
| 63ecf9e2-b5d9-30ca-ad42-3ff2aabdaab9 | -2.1271 | -50.6912 | 2024-11-12 07:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| e6842668-c708-30b1-8608-bd2b79706b43 | -17.5872 | -57.5328 | 2024-11-12 07:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.3 |
| ed0ba8e5-e9b6-3014-a53c-9c32d4dbbe2c | -17.274 | -57.4675 | 2024-11-12 07:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.9 |
| 73b5960e-30ec-3e94-a74f-666714ca2458 | -17.2737 | -57.488 | 2024-11-12 07:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 86.5 |
| 1634912f-5bd0-32c7-ae56-88e5ccca260a | -17.6069 | -57.5304 | 2024-11-12 07:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.7 |
| b3e47d49-3554-37af-a202-dd5c03ec9ccc | -17.5875 | -57.5122 | 2024-11-12 07:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.2 |
| 01422ef6-5521-38b1-8d00-4079c4c40dee | -17.274 | -57.4675 | 2024-11-12 08:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.2 |
| ed81ec5c-243d-3435-8150-582f48bd0533 | -17.2933 | -57.4857 | 2024-11-12 08:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.2 |
| 781c86d8-2d8e-38c8-a7d6-a5baf5be09b6 | -17.6069 | -57.5304 | 2024-11-12 08:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.0 |
| db3f42e8-3b6b-3d81-9d17-6eb5d973b2ad | -15.9605 | -59.2885 | 2024-11-12 08:00:00 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 5eb2ad6e-89ba-3628-a78c-3af46396c811 | -17.2936 | -57.4652 | 2024-11-12 08:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.0 |
| 6351801a-8df6-348d-8199-6669aabdf877 | -17.5872 | -57.5328 | 2024-11-12 08:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.1 |
| b2d18157-601f-3b9a-be2d-98daeefac857 | -17.2543 | -57.4698 | 2024-11-12 08:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 64.0 |
| b43d5264-2f0d-33da-a778-32c774eb764c | -17.2737 | -57.488 | 2024-11-12 08:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 96.3 |
| e9c4fef2-c4ba-3e7d-9ff1-1d25299b78cd | -17.254 | -57.4903 | 2024-11-12 08:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.7 |
| d4376998-dccc-3939-9c79-1c147097a4e4 | -17.5875 | -57.5122 | 2024-11-12 08:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.6 |
| 05aba568-6f16-3a34-978b-7fd2431d1d26 | -17.6069 | -57.5304 | 2024-11-12 08:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.9 |
| 3beaeff4-4109-3c52-9666-1098f6b7a1fa | -15.9411 | -59.2904 | 2024-11-12 08:10:00 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |


[Clique aqui para ver as próximas entradas](README25.md)
