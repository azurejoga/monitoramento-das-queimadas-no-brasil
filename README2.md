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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eceafb54-f8e9-3d90-bcb1-e2a4111b9d0d | -5.9758 | -45.3615 | 2024-10-01 00:07:19 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a23e7c1a-7aa7-372f-90d5-ee77bf4155dc | -5.9628 | -45.348801 | 2024-10-01 00:07:20 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c4005ccd-4a66-39cc-993f-e3fbf8a7accc | -5.966 | -45.363602 | 2024-10-01 00:07:20 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f7c23a9f-8664-3798-89bf-4b62365a20ae | -5.3972 | -43.418999 | 2024-10-01 00:07:22 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8c673481-2899-34e7-a668-b141bca6a58f | -5.3996 | -43.429699 | 2024-10-01 00:07:22 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d656eb62-8ed8-3f0a-9311-d6b876f6f9d0 | -5.7679 | -45.530899 | 2024-10-01 00:07:23 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4c6b4497-ab27-3fbf-9bc7-49658123f8d4 | -5.7712 | -45.546001 | 2024-10-01 00:07:23 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f567745b-97e6-39fb-9112-3d352cdad5df | -5.7549 | -45.517799 | 2024-10-01 00:07:24 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a6ed1852-7d16-38c7-9c6c-2b5061650752 | -5.7581 | -45.532902 | 2024-10-01 00:07:24 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d0a58cde-128f-3d4c-854b-6f8e78659c55 | -5.7614 | -45.5481 | 2024-10-01 00:07:24 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 02e9c86e-4f6c-3114-98ad-d9f158b79c03 | -5.7103 | -46.157799 | 2024-10-01 00:07:27 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d4f6e129-5f77-3ddc-a47b-fa06c4be3263 | -5.714 | -46.174599 | 2024-10-01 00:07:27 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0deaef83-4a7a-351a-a247-42c402abbd36 | -5.5669 | -46.293701 | 2024-10-01 00:07:29 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e34f9cfd-fd63-301a-9e55-a6ac27cfadc4 | -3.7837 | -39.083 | 2024-10-01 00:07:32 | METOP-C | PENTECOSTE | CEARÁ | Brasil | 2310704 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 03b7f69a-2d18-3cc2-aa15-22a2867da530 | -3.7853 | -39.089901 | 2024-10-01 00:07:32 | METOP-C | PENTECOSTE | CEARÁ | Brasil | 2310704 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| a73abd11-6124-311c-913b-a24ed40a4eee | -3.958 | -41.480801 | 2024-10-01 00:07:38 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 78ee1945-cd1b-3524-a2f3-da3fc9bba393 | -3.9598 | -41.488899 | 2024-10-01 00:07:38 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8d37d8c4-8d84-369a-8513-92f95d3675ae | -3.942 | -41.501301 | 2024-10-01 00:07:39 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5ac971e6-2130-348e-83d2-8dab938853c9 | -3.9438 | -41.5093 | 2024-10-01 00:07:39 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 96171834-af03-332f-8ad6-fdfd463277e0 | -3.9456 | -41.517399 | 2024-10-01 00:07:39 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6c2e0d8f-aa77-314d-8015-e5681070b324 | -4.5718 | -47.977699 | 2024-10-01 00:07:52 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f68201c-8b0a-31a8-85c6-5730143f8793 | -4.5622 | -47.979801 | 2024-10-01 00:07:52 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2e36b84-dd7f-3bee-8eb9-aafadb265814 | -4.5669 | -48.001301 | 2024-10-01 00:07:52 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf1a8f43-67c3-3732-82f2-56ccfb74f7af | -4.6873 | -49.765598 | 2024-10-01 00:07:56 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ee58015-2367-3f7a-957a-e1cc6e2f136e | -2.8914 | -50.6782 | 2024-10-01 00:08:29 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 00d36864-38ad-3558-a119-438b33ca8724 | -2.8983 | -50.7094 | 2024-10-01 00:08:29 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc749ea1-f91b-3678-b575-0fb3d2cdea61 | -2.8748 | -50.649101 | 2024-10-01 00:08:29 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c51c62b-90dc-3224-a63b-81e71df7c38d | -2.8817 | -50.680199 | 2024-10-01 00:08:29 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e72cb7ac-b84f-3741-b3bb-eb6f18213fe7 | -2.8887 | -50.711399 | 2024-10-01 00:08:29 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ba9a665-5170-365e-b1d9-fbdb9856539f | -2.8957 | -50.742802 | 2024-10-01 00:08:29 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8cbeaacf-98a6-339a-b27e-4513f5835f8c | -2.8652 | -50.651199 | 2024-10-01 00:08:30 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07bab9d8-10ad-32bf-ad63-52387d69e0e7 | -2.8721 | -50.682301 | 2024-10-01 00:08:30 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4bda172e-d1a8-336e-9190-4e9420d4be1c | -2.8791 | -50.713501 | 2024-10-01 00:08:30 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5641b305-8d70-34b4-8efa-04b6daca7592 | -2.8861 | -50.7449 | 2024-10-01 00:08:30 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1f09128-d68e-3f09-b177-539ff3b9cdaa | -2.8555 | -50.653198 | 2024-10-01 00:08:30 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae258715-7c95-3604-92c5-80248fa96a0a | -2.8624 | -50.684299 | 2024-10-01 00:08:30 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3de1d459-0a7a-3833-9c1c-a2519d266279 | -2.8694 | -50.7155 | 2024-10-01 00:08:30 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84fff814-8c9e-3ef6-a4ae-89fd61b599af | -2.8764 | -50.746899 | 2024-10-01 00:08:30 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e08c7d5f-9791-3f32-9995-721671749000 | -2.8459 | -50.6553 | 2024-10-01 00:08:30 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ecc7453a-dd1f-31a6-9887-2047963a9985 | -2.8528 | -50.686401 | 2024-10-01 00:08:30 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e323da19-eac0-36aa-b3ab-4b2fb4a9fb4c | -2.8598 | -50.717602 | 2024-10-01 00:08:30 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dbf5e11b-6122-3f4f-a1e0-567997e1716f | -2.8668 | -50.749001 | 2024-10-01 00:08:30 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4aa5410e-e05a-3a3c-947e-5d57c63ffe84 | -2.8363 | -50.657398 | 2024-10-01 00:08:30 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ea97ba1-04ac-3185-9885-aaa15cc401fa | -2.8432 | -50.688499 | 2024-10-01 00:08:30 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0d1fcef-14df-3c4f-9eb4-323709acfeeb | -2.8502 | -50.7197 | 2024-10-01 00:08:30 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fad901bf-0c5a-3966-b4c5-5c21ebdffcb4 | -2.8267 | -50.659401 | 2024-10-01 00:08:30 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d28a41de-30ab-39d2-b5ab-31ed2371bb67 | -2.8336 | -50.690498 | 2024-10-01 00:08:30 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dce49ee2-a41f-3523-bafb-53d5137bd448 | -2.8406 | -50.721699 | 2024-10-01 00:08:30 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3dba1ab8-3eb9-3d49-b849-63a32d8659cd | -2.824 | -50.6926 | 2024-10-01 00:08:30 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58edcd1c-c88f-3c51-a042-0cac4ef42fc1 | -2.3893 | -50.284698 | 2024-10-01 00:08:36 | METOP-C | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70927725-381a-329f-9656-80d59f10fa69 | -2.3732 | -50.258099 | 2024-10-01 00:08:36 | METOP-C | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a089f080-c656-378a-831b-166f8f2cd2a7 | -2.3797 | -50.2868 | 2024-10-01 00:08:36 | METOP-C | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0bde64e-2fa0-3cd8-a7d3-c24363fe479c | -2.3862 | -50.315601 | 2024-10-01 00:08:36 | METOP-C | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3fc6012-8e41-3143-8897-14b8ee3cd947 | -2.3701 | -50.288898 | 2024-10-01 00:08:36 | METOP-C | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0099575-4f0c-37d1-8d06-67c886955e64 | -2.4048 | -50.3085 | 2024-10-01 00:15:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 00c9e608-48c0-346f-8e04-09271700ed0c | -2.4047 | -50.3295 | 2024-10-01 00:15:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 151.3 |
| 2a0c7e50-359e-3472-83e7-0ec91c9e3293 | -2.3863 | -50.309 | 2024-10-01 00:15:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 08dadc5f-fea5-34e1-a790-853232382854 | -2.3863 | -50.3299 | 2024-10-01 00:15:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 152.3 |
| b0ef7000-76ec-3a03-9f13-2ca3ed7a90cb | -3.8166 | -52.3608 | 2024-10-01 00:15:28 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| e1459744-e775-3c0d-b947-e56e71532dcd | -3.8165 | -52.3813 | 2024-10-01 00:15:28 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| dedd3a9a-61ce-3a53-abf8-427f0f3185a6 | -4.6987 | -49.8062 | 2024-10-01 00:15:32 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 54e33d01-f724-3283-a725-8b35e1e23d84 | -4.7172 | -49.8053 | 2024-10-01 00:15:33 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 95cae7a2-2f99-3b35-a0b2-ab997d51ad27 | -5.7717 | -45.5349 | 2024-10-01 00:15:38 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 55.3 |
| ac07345a-a11b-3cb2-84c8-ef6a8115c6dd | -5.7715 | -45.5574 | 2024-10-01 00:15:38 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| ee75b32a-6650-34a2-a863-d9c55de14520 | -5.9788 | -45.3621 | 2024-10-01 00:15:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 64.4 |
| c7101014-ce9f-3b67-a469-332380e77b60 | -5.9786 | -45.3847 | 2024-10-01 00:15:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| d40c86e7-54ab-36d6-9730-0c96d293424d | -6.2524 | -44.132 | 2024-10-01 00:15:41 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 90.7 |
| f779930b-4725-361b-afd1-276343a33e8e | -6.2336 | -44.1335 | 2024-10-01 00:15:41 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 7fdb7417-3ca7-3f31-96e3-8d2449dbe561 | -7.1111 | -35.3112 | 2024-10-01 00:15:45 | GOES-16 | MARI | PARAÍBA | Brasil | 2509107 | 25 | 33 | nan | nan | nan | Caatinga | 153.3 |
| 55351f05-6bc2-39f9-99cb-2aa48b32047a | -8.4643 | -62.7124 | 2024-10-01 00:15:54 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 5726915f-93a7-3b91-b457-249ab0fa8d7a | -8.4642 | -62.7313 | 2024-10-01 00:15:54 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 1826bb16-974d-319c-b0e4-1655e3916c3e | -8.7544 | -47.1328 | 2024-10-01 00:15:55 | GOES-16 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 97.6 |
| c25a6f9e-6008-37a9-90f1-f467cb4278e5 | -8.4829 | -62.6927 | 2024-10-01 00:15:55 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 45562c4e-d501-3cff-96af-2c6c1604a3c9 | -8.4828 | -62.7116 | 2024-10-01 00:15:55 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 580477aa-8942-3e9d-82e6-808f1886b5a3 | -10.9432 | -50.0619 | 2024-10-01 00:16:08 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| ffbe1d11-4c11-359e-917a-a327028f79bd | -10.9429 | -50.0833 | 2024-10-01 00:16:08 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 236.5 |
| 21b8e6f5-b8dd-3280-9e88-424baca02da2 | -10.9426 | -50.1048 | 2024-10-01 00:16:08 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 116245b8-ad2f-31a0-98f5-c396fba08d4c | -10.924 | -50.0854 | 2024-10-01 00:16:08 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 163.1 |
| aa559426-e3cf-39bd-ac9a-d453175f2def | -10.9237 | -50.1069 | 2024-10-01 00:16:08 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 90b9f956-e970-38dd-9323-c862025a4ae9 | -11.6367 | -64.9999 | 2024-10-01 00:16:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 184c6cd8-ae57-38de-80fe-c49cfce34809 | -11.6744 | -64.9793 | 2024-10-01 00:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 55.3 |
| a26d9662-df96-3dda-9b37-a78d7efc7931 | -11.6743 | -64.9983 | 2024-10-01 00:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 948030b1-eea2-39dd-9ac4-3112fba4c674 | -11.6556 | -64.9802 | 2024-10-01 00:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 94.6 |
| e29b46b8-5cd4-34c4-b778-05d293b179d0 | -11.6555 | -64.9991 | 2024-10-01 00:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 131.8 |
| 97e379ef-323c-3ac7-a881-814a583d9f2f | -11.6554 | -65.018 | 2024-10-01 00:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 08742fde-891d-3033-9999-dd1a35388af6 | -12.6039 | -53.4879 | 2024-10-01 00:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 312.8 |
| 2af95191-5f79-3fe9-84f2-001f3d9d266e | -12.6036 | -53.5087 | 2024-10-01 00:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 157.6 |
| 276448cf-fd8d-3376-9e93-d8372fbb322a | -12.5848 | -53.4899 | 2024-10-01 00:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 64253316-96f4-3d6d-8997-54a8ade0af71 | -12.9807 | -51.2786 | 2024-10-01 00:16:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 92.1 |
| eb611638-72b3-3fd0-8a8d-96b030698eef | -12.9803 | -51.3 | 2024-10-01 00:16:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 21e27a69-1547-3097-a1cb-a5d670707aff | -12.9615 | -51.281 | 2024-10-01 00:16:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 104.7 |
| c5991bb8-c961-3aad-a328-30960cc229cb | -12.9612 | -51.3023 | 2024-10-01 00:16:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 179.6 |
| 22c430e1-d5aa-3bd2-b372-6b3dbe84a160 | -12.9608 | -51.3237 | 2024-10-01 00:16:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 155.2 |
| 4768aa18-1111-36f6-83a4-1e20c7bfe386 | -12.9605 | -51.345 | 2024-10-01 00:16:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 93eab4a9-b6b1-36c3-8cda-513d0e857099 | -12.8845 | -51.3117 | 2024-10-01 00:16:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 6dd03a5c-d1fe-3456-8717-d901ba271429 | -13.2496 | -51.2238 | 2024-10-01 00:16:21 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 63d692dc-73cb-3f49-93b5-799e7bf8859a | -13.2493 | -51.2452 | 2024-10-01 00:16:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 1c395243-cf30-3e8c-a2ef-69fdd4f0295e | -13.5765 | -51.1821 | 2024-10-01 00:16:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 78db40c0-11d9-35d5-8459-4cdc674e2f14 | -14.7406 | -48.7498 | 2024-10-01 00:16:28 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 81.7 |
| ec4cf9f2-4a2a-3cca-ac0e-8191e0b6571d | -15.6372 | -57.447 | 2024-10-01 00:16:34 | GOES-16 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 72.3 |


[Clique aqui para ver as próximas entradas](README3.md)
