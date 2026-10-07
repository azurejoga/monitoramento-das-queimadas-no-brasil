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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7be0d19b-827c-3dff-a6d6-e31499fe1987 | -3.14068 | -54.36731 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 300cd6ec-867c-3049-8263-69fab45f8784 | -3.06767 | -54.2449 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 112d6c36-ffd4-3156-b5ca-b94319c81d8d | -2.76958 | -54.1055 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 4e1b8055-5b6f-347c-a37c-a196d8a098ac | -5.17855 | -46.27473 | 2026-10-07 05:04:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 059fad4d-387a-3a23-83fe-13b78444b7a1 | -2.88017 | -54.11584 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| df8543a7-9e70-3558-b413-5e3a7a06cdab | -3.48139 | -54.62653 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5323454f-17c3-36e5-81e4-9a9f566dd651 | -3.10561 | -54.15382 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 24646103-ae0b-3a3b-8b7e-c156f74299a6 | -3.54152 | -54.65696 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5e1bb1ab-7b85-3d05-8d14-e69c2c25292f | -3.03429 | -53.91168 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3f99ed50-4e27-35a3-9a6e-52758fb685a1 | -3.04072 | -54.24432 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab2abdf8-9b71-31cb-9cf7-b14dbdbcf4a2 | -3.06434 | -54.37641 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 06724c3f-c207-3789-a597-f3e523a73c15 | -1.80332 | -57.11079 | 2026-10-07 05:04:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| f516a606-0bc9-3c0c-9d70-57f7bddc3308 | -3.34825 | -59.50637 | 2026-10-07 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 62da29b8-0ac1-39e8-871a-a6041f164bd8 | -2.97883 | -54.13797 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c048a29b-2daa-3417-b8c7-17b7fa9af6a9 | -2.15544 | -59.22394 | 2026-10-07 05:04:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8921bfd7-a2ff-303d-9f28-d3080f184f0a | -3.27711 | -54.18761 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a06608e9-84e6-3981-a495-e1a6c9a5de24 | -3.2277 | -53.89059 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25690a5c-21eb-3b7a-8119-3c39dbd074e4 | -3.51033 | -59.9482 | 2026-10-07 05:04:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ce6dd929-daac-31e6-b78a-bddf739ea968 | -1.79583 | -57.11356 | 2026-10-07 05:04:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0faf0df0-b71a-3db1-8420-3f8dbb9df4ce | -2.76345 | -54.10097 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7ff8238c-fed6-3d21-994b-5428f1dd5f7b | -6.83638 | -52.19159 | 2026-10-07 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 22cecf01-cc2d-3afe-af2b-17de2ba294ce | -3.50295 | -54.6405 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3e429e0e-a160-37c0-8933-a33a79403dd9 | -3.07603 | -54.25695 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 08c08e12-9726-3e84-8805-8adc45242d85 | -3.15586 | -59.08906 | 2026-10-07 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc37347f-8213-3111-b755-27ac159236b2 | -3.36495 | -59.90254 | 2026-10-07 05:04:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eddf15eb-3e10-38cb-8900-fc508f5daf65 | -4.24122 | -49.97969 | 2026-10-07 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a97fed7c-610c-32c5-bc0e-43b60e74b210 | -3.74624 | -51.22306 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c22b4d8c-ace4-344d-9c36-d15f55cf0ca8 | -3.51903 | -54.66781 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| efe39290-a8b8-3595-8a11-60d96d84ad91 | -2.15433 | -59.22621 | 2026-10-07 05:04:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 75310fa4-e279-3bf5-aa3b-eb7d6efe134c | -3.58104 | -54.31385 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6655c014-e877-3aec-8ef5-82f7bbf84f17 | -3.08322 | -54.25449 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bb9bf2f4-a377-3d8a-9cf9-2ae16d16d57e | -2.13941 | -54.45917 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1fc92aeb-e0ac-3ca5-9671-6cb823fda39b | -3.10561 | -53.76202 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db58b72e-6df9-3c43-8d82-b4715a5a336f | -3.73951 | -55.98058 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1287a39c-1c68-3b1d-ad07-8030cbebe1dc | -1.43225 | -53.23465 | 2026-10-07 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b46c7924-b165-3c15-925e-26d7e9523a24 | -8.7071 | -45.21441 | 2026-10-07 05:04:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 4f0e1c83-f364-34f2-9db7-fdf205620ce8 | -3.02282 | -54.18427 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 868dda0f-d00a-364e-aa16-016f59aa1188 | -2.60188 | -48.2609 | 2026-10-07 05:04:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 04b721a7-fe73-3ee4-b757-f300ecba93e8 | -1.29704 | -54.5603 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7054cb56-acd0-336c-9229-8cf49ccbbd14 | -4.77349 | -50.81585 | 2026-10-07 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c924263-96f8-3a51-835e-4b231f2b033b | -3.73862 | -51.22187 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32e0dd00-c796-3780-b92b-02a15cf47ef8 | -6.46379 | -55.44633 | 2026-10-07 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 446e0977-bc81-3213-b990-98cc49f8f7ac | -3.00766 | -54.12806 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3675f3b9-a1dd-32c3-99ee-0144d55b3c8d | -3.30373 | -53.86577 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 36a6c14f-02b4-38ef-a622-6d8384fe7fee | -3.56782 | -54.48677 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a53b79e2-dc67-35b4-99ad-9ba24af443b3 | -3.0638 | -54.37988 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ccff4fe1-c093-3139-82fb-d5830fc5a09b | -3.08732 | -54.16182 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 876f0e63-94a6-3d02-8cb8-bc6e1fdcab26 | -3.57019 | -59.50312 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8feb14cb-fcf2-3fdf-89ed-5b24e5a7beb9 | -3.49294 | -54.61768 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8c3a8d03-215a-3d87-b79b-885a849b1a6e | -3.13983 | -51.03054 | 2026-10-07 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6e9654d3-ff2e-3fe5-a458-2ada0c795233 | -3.12382 | -53.7683 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c4182b12-b879-3b23-85cc-ff09f870ec3a | -3.04079 | -54.26573 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d7ded1e1-be43-32f4-bdc3-e9b871e5043b | -3.57625 | -54.65165 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| adf78dd5-8d30-39ba-bfe7-c6e0f688b5ac | -3.28216 | -54.00448 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 354f1bf7-1ce3-3bbe-b93c-b06b092e6273 | -8.71561 | -45.19641 | 2026-10-07 05:04:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 15.6 |
| ed194e24-ff93-3000-ba59-9f440d3a8d43 | -3.27222 | -50.79185 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c24042b4-9970-3be0-852a-38021493b08e | -2.76066 | -54.09695 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2b0cb882-710c-3826-9056-cd9272ffb7af | -3.49348 | -54.61421 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 065d4e31-0ced-399c-9583-fbc79347902c | -3.1856 | -50.56356 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 258579f1-8be9-36cf-ac70-10a40a7978e5 | -2.9965 | -54.11195 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec5e5cb5-4738-3e21-b8ec-721857635ce5 | -3.30276 | -42.27635 | 2026-10-07 05:04:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 928572cf-0f39-3e2a-a523-f622e0a52a93 | -3.18158 | -50.56652 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 37ee1301-1550-3192-a29e-c0c0b8877f7b | -2.75122 | -57.6639 | 2026-10-07 05:04:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ebdb2816-7e02-397e-ab66-a00165108a44 | -6.17331 | -44.59845 | 2026-10-07 05:04:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e18001e3-8b88-3fc1-a551-b48a3dcb1144 | -2.99091 | -54.10389 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4224411b-c937-34c4-949b-f5506ee232da | -1.80793 | -57.10383 | 2026-10-07 05:04:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 297961b1-894c-3329-bb27-945e5ae0e6b4 | -3.60706 | -55.30466 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 28e84c5d-49c6-39b1-a0cb-f59a09477cc8 | -3.96548 | -56.12609 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8d77a26a-a7bc-3aff-83b2-1c60fc610a21 | -6.3063 | -54.79126 | 2026-10-07 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1d3e2f1-9080-3755-8285-e9fefad53ef9 | -3.05392 | -54.26778 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d19279d9-f73b-3d6d-9a6c-435dcf8279bc | -3.27966 | -53.86572 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eacaa086-e2f8-31cb-ab6c-e81ddb73ffb6 | -3.05214 | -54.14928 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 482c8270-f671-391c-a628-33adafc17941 | -3.05555 | -54.38929 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ec24a858-f153-3d4a-aaa6-32dc5e9e5919 | -2.9035 | -54.11944 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6fcbc5e4-7dff-3561-9780-0b483ab969bc | -6.27029 | -52.84272 | 2026-10-07 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8afaa708-2f67-3426-8ff4-2a7e2169df8d | -1.50893 | -54.81449 | 2026-10-07 05:04:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f72dc7f-53d7-3169-a15b-9cbc94ea3795 | -1.28938 | -54.56614 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9f6293f0-5263-3228-b162-9787fadf293a | -3.03929 | -53.90154 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bde2623f-9b00-3636-a014-33e827695a1c | -3.00936 | -54.13911 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fa2184ac-d45f-38bb-87ce-ac4cddaf83ce | -3.00378 | -54.13106 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 05388234-106f-340c-88ff-cff03b554f5c | -3.52112 | -54.63268 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 151000a7-a3c6-3ecd-97cc-d856aa11e3a9 | -3.38712 | -58.20424 | 2026-10-07 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 664acf67-3529-3b4d-b9fa-dcf0c4da3e42 | -4.11294 | -54.01829 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 358881da-1b8a-3160-b3d9-34d8ecc93f3a | -1.80449 | -57.10334 | 2026-10-07 05:04:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9913f5ab-c07e-35fc-b468-8e58538f3493 | -3.05535 | -54.21438 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6aedd799-fc9a-3c0d-8db6-333a26d85320 | -3.65751 | -54.522 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3bc9f66a-30c3-307a-9b1a-1fb1ccfa0c0b | -3.47979 | -59.46229 | 2026-10-07 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c2b3c88a-311d-37ea-b90b-c00d28ad01ee | -2.87476 | -54.15084 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fbe98228-0df4-38ee-9137-553b024b792f | -2.87143 | -54.15033 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8dfb6d61-7430-3f39-a1ae-b3e7ce3b1790 | -3.50903 | -54.64499 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e6cc2f5b-33f4-3e58-ac1f-ace335e2eea7 | -2.89125 | -54.11037 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ab3f3657-8151-310e-9d0a-52be564873bd | -3.13165 | -53.76216 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a49b55e3-81ee-351a-b212-8c8e78dfb145 | -1.89281 | -52.63944 | 2026-10-07 05:04:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e1200f5-d369-3b90-8c96-460511fdeca8 | -3.17682 | -50.43979 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 906136fa-d521-31c5-8af4-9f58bc1f2158 | -3.97307 | -56.05639 | 2026-10-07 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 25f8d310-72c9-35e3-90be-8252a07798f8 | -3.49158 | -59.58456 | 2026-10-07 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 155ceb3b-5f0d-3676-8091-070294de678a | -3.52536 | -58.75471 | 2026-10-07 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5deccf2-c311-3029-a8ed-3ff1f589a8da | -4.7598 | -55.65856 | 2026-10-07 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca2bf637-9ca3-3617-b3cf-bcc1b07e3c5a | -2.17861 | -48.14026 | 2026-10-07 05:04:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1e7505af-29d2-329f-b367-5ede191c4477 | -3.47808 | -54.62603 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |


[Clique aqui para ver as próximas entradas](README86.md)
