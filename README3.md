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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 46a60ecf-6299-3b97-979b-fc71ccb1f46b | 1.42378 | -59.94962 | 2025-01-31 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 11.6 |
| e233da70-0b86-3e61-9673-106d0ac43ce1 | 1.42004 | -59.9502 | 2025-01-31 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 8c3bbd8b-181f-3d03-8b30-4f7d4b1a602a | 1.42075 | -59.95463 | 2025-01-31 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 6f3ef2f0-81ff-3046-aaf4-1b68a7ecdbaf | 1.42364 | -59.95208 | 2025-01-31 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 23edefc7-f4d2-3f6a-8998-c3de83662a1a | 1.42611 | -59.94769 | 2025-01-31 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c4f75977-e9a6-3aa3-aca0-01c00a844ffa | 1.42424 | -59.95583 | 2025-01-31 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 7fef4a12-aaff-37ed-8569-863173b4c9ed | 1.42304 | -59.94833 | 2025-01-31 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| fd3ce6b8-8585-3cc4-9afe-43a628462ea7 | 1.4217 | -59.95601 | 2025-01-31 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5a72cb92-ed36-33e3-bf40-cf2dd5fd8ccc | 1.42734 | -59.9551 | 2025-01-31 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 978e0cba-329a-31b4-9e11-44c5f61da51b | 1.42672 | -59.95139 | 2025-01-31 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a15e1097-bb32-3a61-ab4b-882d930cbca3 | 1.42107 | -59.95224 | 2025-01-31 06:03:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 568fd220-6d84-3503-8cff-0310f03281a4 | 1.42156 | -59.94038 | 2025-01-31 06:18:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 44b99ee4-1278-3a4b-83fa-42ddd13e693d | 1.43294 | -59.94991 | 2025-01-31 06:18:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.6 |
| b92f6c7e-cd95-3f87-8ff5-2246bd9d26ac | 1.42317 | -59.95137 | 2025-01-31 06:18:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 34.7 |
| 01febbec-a42d-3f9f-b170-e1160219e19f | -16.27512 | -56.7803 | 2025-01-31 06:22:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.0 |
| 035f9f1d-a297-3d28-b744-5a649451d2b8 | 1.4316 | -59.9503 | 2025-01-31 06:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 327afd82-d65d-3567-a02c-d83321a52d7a | 1.4316 | -59.9503 | 2025-01-31 06:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 48.9 |
| a6a38be1-6145-3ed7-af1f-155c88caaf6c | 1.4134 | -59.9504 | 2025-01-31 06:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 0d81e1bf-7969-3253-8851-dbb8a70ed40b | 1.4134 | -59.9504 | 2025-01-31 06:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 325cfca1-9813-3e4d-93f8-a117f5697fe3 | 1.4316 | -59.9503 | 2025-01-31 06:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 743bb063-55d3-3de0-8cd2-c1aabe8ca8e9 | 1.4316 | -59.9503 | 2025-01-31 07:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 80406c6e-e3ae-3b52-b27a-98f1ade27d98 | 1.4134 | -59.9504 | 2025-01-31 07:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 8a383bda-c4c0-36f9-9078-5fef77abfa4a | 1.4134 | -59.9504 | 2025-01-31 07:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 3f1c2100-5ae3-3b5b-a0bb-fd2683938f73 | 1.4316 | -59.9503 | 2025-01-31 07:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 9474beab-d68d-31d9-afd2-f2669e624edf | 1.4316 | -59.9503 | 2025-01-31 07:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 94658d83-4339-33fe-bf75-1407cc6ce139 | 1.4134 | -59.9504 | 2025-01-31 07:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 8db50c92-e175-362d-a6a4-da15dad34b9e | 1.4316 | -59.9503 | 2025-01-31 07:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 64082204-7c89-3c8e-9e8d-39cc4f9f450f | 1.4134 | -59.9504 | 2025-01-31 07:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 36.4 |
| d1020539-4159-3108-8023-c743742a2944 | 1.4316 | -59.9503 | 2025-01-31 07:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 4fcda3a3-60c0-3d05-a895-db562b80eb54 | 1.4134 | -59.9504 | 2025-01-31 07:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 34.2 |
| 98f339ec-cf3d-3bc4-80d8-02e4dc412260 | 1.4316 | -59.9503 | 2025-01-31 07:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 46.3 |
| ef752ac6-6e31-356c-83a3-021949f30799 | 1.4134 | -59.9504 | 2025-01-31 07:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 34.3 |
| fa38b903-7a70-330d-b592-0fa8801f328f | 1.4316 | -59.9503 | 2025-01-31 08:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 349f9e87-2c7e-3bd7-9245-493c8734ddac | -7.02359 | -44.45086 | 2025-01-31 12:27:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0edb3d49-fe05-3284-b10b-76a8a40478be | -7.05834 | -43.36401 | 2025-01-31 12:27:00 | TERRA_M-T | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 74b29ffa-27a5-3c77-9e10-2155958f7142 | -3.29824 | -42.52724 | 2025-01-31 12:27:00 | TERRA_M-T | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 2ec78506-aad9-3b94-9784-13dbedcbcafd | -4.18345 | -38.35714 | 2025-01-31 12:27:00 | TERRA_M-T | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 16.0 |
| 5b1aa16a-96d4-3581-a639-ae1319f0fb36 | -7.8466 | -44.74955 | 2025-01-31 12:27:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 94a32929-2f96-31f4-8b31-556b024163ff | -18.42678 | -40.03918 | 2025-01-31 12:29:00 | TERRA_M-T | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 16.8 |
| c56da7c3-8269-35ac-9078-3039aec1edad | -17.68248 | -42.30719 | 2025-01-31 12:29:00 | TERRA_M-T | ANGELÂNDIA | MINAS GERAIS | Brasil | 3102852 | 31 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 3c5eac39-fd20-3faa-b6b8-14a0cf4f4c5e | -15.30433 | -41.8427 | 2025-01-31 12:29:00 | TERRA_M-T | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.8 |
| c41e110a-cce0-36c5-896f-8348a47a52c2 | -11.24393 | -37.26619 | 2025-01-31 12:29:00 | TERRA_M-T | ITAPORANGA D'AJUDA | SERGIPE | Brasil | 2803203 | 28 | 33 | nan | nan | nan | Mata Atlântica | 39.8 |
| 375a2cb5-c696-3c1d-818e-4d2484ccec72 | -11.24619 | -37.25956 | 2025-01-31 12:29:00 | TERRA_M-T | ITAPORANGA D'AJUDA | SERGIPE | Brasil | 2803203 | 28 | 33 | nan | nan | nan | Mata Atlântica | 38.1 |
| eebabaf3-cc5c-3785-a990-733d4f592bc7 | -30.98567 | -53.32858 | 2025-01-31 12:33:00 | TERRA_M-T | SANTANA DA BOA VISTA | RIO GRANDE DO SUL | Brasil | 4317004 | 43 | 33 | nan | nan | nan | Pampa | 13.0 |


