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
| 4d5d3837-c703-3069-8b97-2815497637aa | -4.3131 | -47.7599 | 2025-01-08 04:31:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 47bbde12-346f-3cfb-aeb0-a48e3bb512a9 | -9.0536 | -35.33252 | 2025-01-08 04:33:00 | NPP-375D | JAPARATINGA | ALAGOAS | Brasil | 2703601 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 604d70cc-67d1-3466-8e25-0275aede3b25 | -12.46311 | -46.93418 | 2025-01-08 04:33:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f9271aef-38bf-357d-bedc-9ce79669a230 | -9.04742 | -35.32524 | 2025-01-08 04:33:00 | NPP-375D | JAPARATINGA | ALAGOAS | Brasil | 2703601 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| e17724e9-8085-3005-8b61-d823720a3cd3 | -11.8098 | -49.33255 | 2025-01-08 04:33:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8392d108-186d-39d0-91bf-46cc31a701bb | -9.06134 | -35.327 | 2025-01-08 04:33:00 | NPP-375D | JAPARATINGA | ALAGOAS | Brasil | 2703601 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 534572d4-78ae-36a3-a8e0-90c0b1b9283a | -9.04806 | -35.32618 | 2025-01-08 04:33:00 | NPP-375D | JAPARATINGA | ALAGOAS | Brasil | 2703601 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| d0264e0a-723d-3b25-8c51-27c04bc7f8b3 | -9.05438 | -35.32613 | 2025-01-08 04:33:00 | NPP-375D | JAPARATINGA | ALAGOAS | Brasil | 2703601 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| f96c5ded-6113-348c-87cf-3924e2793490 | -9.05518 | -35.31956 | 2025-01-08 04:33:00 | NPP-375D | JAPARATINGA | ALAGOAS | Brasil | 2703601 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 494acf7b-2e8c-3439-a3b9-466f129655e9 | -20.31182 | -45.58323 | 2025-01-08 04:36:00 | NPP-375D | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ce9855ec-1cc0-3ce6-bf7e-854120e1a806 | -19.5814 | -49.37163 | 2025-01-08 04:36:00 | NPP-375D | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dc7fbe8c-4cd8-32c6-9c30-142ad272ebc0 | -20.95877 | -49.7554 | 2025-01-08 04:38:00 | NPP-375D | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| a5d80197-0d61-3765-8b54-88bfb46fe339 | -20.11522 | -54.6858 | 2025-01-08 04:38:00 | NPP-375D | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 91211c56-a5ce-305f-b431-745c1ad48ba1 | -23.33775 | -46.77021 | 2025-01-08 04:38:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 141b5aaf-d862-371b-996d-ce8d56bf1ccf | -20.95991 | -49.7476 | 2025-01-08 04:38:00 | NPP-375D | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 7ad30bd7-068d-3de6-b47f-ace356a7b50b | -23.63001 | -46.42726 | 2025-01-08 04:38:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f7a0a829-763e-3f4c-a8ec-fd57a9401ebe | -20.95934 | -49.7515 | 2025-01-08 04:38:00 | NPP-375D | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| b3449a38-a87a-30fc-9d0a-6ccdb9d3b91b | -23.79451 | -50.28075 | 2025-01-08 04:38:00 | NPP-375D | IBAITI | PARANÁ | Brasil | 4109708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| f1b0fb2a-fc0d-3686-bcb8-28054fc261a7 | -23.75503 | -50.3353 | 2025-01-08 04:38:00 | NPP-375D | IBAITI | PARANÁ | Brasil | 4109708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 87316f45-0130-31c0-b4f7-be0d6df726d2 | -20.95593 | -49.75092 | 2025-01-08 04:38:00 | NPP-375D | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 69d8c750-fd5a-3daa-a209-7503500da229 | -23.79567 | -50.2728 | 2025-01-08 04:38:00 | NPP-375D | IBAITI | PARANÁ | Brasil | 4109708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| 06f8b167-744f-3138-a01c-3168512a0b24 | -23.77222 | -50.28913 | 2025-01-08 04:38:00 | NPP-375D | IBAITI | PARANÁ | Brasil | 4109708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 467fe1f8-2678-396e-b35a-f6aba1dc47b6 | -20.96218 | -49.75599 | 2025-01-08 04:38:00 | NPP-375D | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 7f9dcd71-ea29-334e-8a83-d181a1da5a92 | -20.65367 | -49.30185 | 2025-01-08 04:38:00 | NPP-375D | ONDA VERDE | SÃO PAULO | Brasil | 3534005 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ecacd34b-9ea5-309a-a003-a06a299cced5 | -24.08008 | -51.01455 | 2025-01-08 04:38:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 7bd982fb-a627-3bc6-bd34-213c5d006c9f | -20.65022 | -49.30126 | 2025-01-08 04:38:00 | NPP-375D | ONDA VERDE | SÃO PAULO | Brasil | 3534005 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c677ed83-5bbf-306a-9883-6b02b61fe0b0 | -27.37374 | -51.52589 | 2025-01-08 04:38:00 | NPP-375D | CAMPOS NOVOS | SANTA CATARINA | Brasil | 4203600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8a73f1e1-f9de-323d-8f2e-35d8b67fa658 | -20.96275 | -49.75209 | 2025-01-08 04:38:00 | NPP-375D | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| d55c6cf4-6083-3b6f-8e08-bb53dcfaace9 | -20.64964 | -49.30524 | 2025-01-08 04:38:00 | NPP-375D | ONDA VERDE | SÃO PAULO | Brasil | 3534005 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d50078e7-d62d-3d0a-9444-63e42a8498d9 | -20.12083 | -50.41823 | 2025-01-08 04:38:00 | NPP-375D | TURMALINA | SÃO PAULO | Brasil | 3555307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 62048433-0f56-394d-8e69-e8e6f7726c90 | -20.64619 | -49.30466 | 2025-01-08 04:38:00 | NPP-375D | ONDA VERDE | SÃO PAULO | Brasil | 3534005 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c73bcf6b-ad8d-39de-aac7-8b235a42cb22 | -20.65712 | -49.30243 | 2025-01-08 04:38:00 | NPP-375D | ONDA VERDE | SÃO PAULO | Brasil | 3534005 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e5cd2cf3-5c76-37cf-b8fd-e11ca39eb596 | -20.65653 | -49.3064 | 2025-01-08 04:38:00 | NPP-375D | ONDA VERDE | SÃO PAULO | Brasil | 3534005 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c4300479-d2e1-33c1-840a-2095d9a13a1a | -23.79509 | -50.27677 | 2025-01-08 04:38:00 | NPP-375D | IBAITI | PARANÁ | Brasil | 4109708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| f8f20f30-b28b-364a-8a39-8beb641ec588 | -23.75218 | -50.33069 | 2025-01-08 04:38:00 | NPP-375D | IBAITI | PARANÁ | Brasil | 4109708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 75e3bdc2-45d1-34cc-97b7-a90b4266b214 | -20.65525 | -49.30494 | 2025-01-08 04:38:00 | NPP-375D | ONDA VERDE | SÃO PAULO | Brasil | 3534005 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 94cc2528-835c-3bcd-abc4-df6d9c43ba7c | -24.0795 | -51.01843 | 2025-01-08 04:38:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| b6fa2c69-78fd-31f5-8558-72773a5c9c67 | -20.5343 | -49.0414 | 2025-01-08 04:38:00 | NPP-375D | ALTAIR | SÃO PAULO | Brasil | 3500907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 972e9a99-2f96-3ebe-b053-040381be8ad5 | -24.68687 | -50.31696 | 2025-01-08 04:38:00 | NPP-375D | TIBAGI | PARANÁ | Brasil | 4127502 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 5fa11895-c867-3833-b917-7bdf734260c6 | -23.75161 | -50.3347 | 2025-01-08 04:38:00 | NPP-375D | IBAITI | PARANÁ | Brasil | 4109708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 0ce0b2ac-dd81-305d-93ea-aa5e66841e7f | -24.24205 | -50.7404 | 2025-01-08 04:38:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7d0064e3-0222-3b10-be9a-36536caeead3 | -20.76193 | -46.7702 | 2025-01-08 04:38:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7600440f-8cbf-37af-8efb-20a87f135f0b | -24.69032 | -50.31751 | 2025-01-08 04:38:00 | NPP-375D | TIBAGI | PARANÁ | Brasil | 4127502 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 10bf62f8-7f75-33b9-8eec-baf39ce67ff4 | -20.65582 | -49.30096 | 2025-01-08 04:38:00 | NPP-375D | ONDA VERDE | SÃO PAULO | Brasil | 3534005 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f93b9aa3-4bc7-3b44-a1e9-ffdf63e9bda0 | -23.59462 | -47.43666 | 2025-01-08 04:38:00 | NPP-375D | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| cd2f92cf-21db-3f9b-9f50-0a0d1f2500eb | -20.64905 | -49.3092 | 2025-01-08 04:38:00 | NPP-375D | ONDA VERDE | SÃO PAULO | Brasil | 3534005 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1d7c8c5b-a02e-3efa-9caf-c9814de766c2 | -20.47791 | -53.67503 | 2025-01-08 04:38:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b47d522e-3731-3112-928c-89244b39a25a | -23.79795 | -50.28131 | 2025-01-08 04:38:00 | NPP-375D | IBAITI | PARANÁ | Brasil | 4109708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 46f37624-96b3-3a61-88b6-e2e23971cfca | -23.59443 | -47.43789 | 2025-01-08 04:38:00 | NPP-375D | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| eaa7fe82-920b-3b54-ace9-d13033806d4a | -20.65308 | -49.30582 | 2025-01-08 04:38:00 | NPP-375D | ONDA VERDE | SÃO PAULO | Brasil | 3534005 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 81c5fef4-3f95-3d0e-a3fd-42c91b2dc290 | -23.79166 | -50.27618 | 2025-01-08 04:38:00 | NPP-375D | IBAITI | PARANÁ | Brasil | 4109708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| 71777797-7ee8-376b-a3af-25fe39eaee37 | -20.32965 | -53.24847 | 2025-01-08 04:38:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0468bf86-e8d9-3a91-9e39-d45d4f56cbe7 | -29.64813 | -51.10982 | 2025-01-08 04:40:00 | NPP-375D | NOVO HAMBURGO | RIO GRANDE DO SUL | Brasil | 4313409 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 2ffa22d1-f713-3beb-9f95-1a957a53c8a1 | -30.3209 | -53.4138 | 2025-01-08 04:40:00 | NPP-375D | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 18b32ee0-55b8-3a82-9cb2-08d3f033e45c | -30.32424 | -53.41449 | 2025-01-08 04:40:00 | NPP-375D | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| ba4e22d9-6bce-3758-a6a9-a661c00b2fe8 | -30.32362 | -53.41851 | 2025-01-08 04:40:00 | NPP-375D | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 1.8 |
| 0b16674e-6e19-3ab0-afd8-42eb7e3f4abc | -29.70727 | -51.28018 | 2025-01-08 04:40:00 | NPP-375D | PORTÃO | RIO GRANDE DO SUL | Brasil | 4314803 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 7b9b577c-acd8-3603-b8f0-3c028a1aa57e | -1.3585 | -53.72556 | 2025-01-08 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5a15e61-0bf6-3327-929d-0bac163d749b | 1.05955 | -59.55648 | 2025-01-08 04:53:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d697fa08-c13c-3d0b-952c-186d3a9b86a5 | 1.34795 | -60.03483 | 2025-01-08 04:53:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5f79cee1-3d66-3d7a-8e8d-0925eb3b61b0 | -0.28859 | -50.42554 | 2025-01-08 04:53:00 | NOAA-20 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 112c1845-0b7c-3860-81a4-8fbd584119db | 2.98855 | -61.19263 | 2025-01-08 04:53:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2edcf03-fd18-3507-a9b6-6e494e6df14c | 1.05491 | -59.55717 | 2025-01-08 04:53:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b12580cb-1ea8-30f7-8850-b666a3d8f282 | 2.98754 | -61.186 | 2025-01-08 04:53:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b87bb01e-7dbe-38b1-b596-0bffa955aa32 | -0.96811 | -53.09916 | 2025-01-08 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 45a95029-c267-3c50-8e87-fcb2df013a99 | -0.9648 | -53.09865 | 2025-01-08 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2afae2d4-d476-39fb-b965-c271cca5182b | -0.29059 | -50.42659 | 2025-01-08 04:53:00 | NOAA-20 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c192f5f6-bcef-3367-8d1a-c5ed78c160f4 | -1.28203 | -53.17701 | 2025-01-08 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1dea58c2-5bc2-3273-8f72-1ff932a0b9ac | 2.98804 | -61.18931 | 2025-01-08 04:53:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b2cb988-5ed7-3779-8b98-c530bc2c25ce | 1.34875 | -60.04005 | 2025-01-08 04:53:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3e39bce2-ea59-3e72-bb41-5d3b3738fbb6 | -1.01313 | -47.78807 | 2025-01-08 04:53:00 | NOAA-20 | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 068ba64a-ef6e-3a32-8193-3daf5849e782 | 3.58238 | -60.86246 | 2025-01-08 04:55:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e049f79c-94e0-3988-a6e4-3496f08e0fd9 | 3.90453 | -60.2515 | 2025-01-08 04:55:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eea867e3-15b7-3720-af87-4945f91d5583 | 3.45949 | -60.21811 | 2025-01-08 04:55:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d5ef78c6-174c-3fbc-8e7e-719d50d84c6b | -2.43243 | -53.87262 | 2025-01-08 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ec92d98-a6f0-3dfb-8484-4bf75efe5c06 | -7.80618 | -50.7679 | 2025-01-08 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6857274d-184e-3ee5-ba07-cbcc93fded33 | -2.86909 | -54.16164 | 2025-01-08 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 906ba270-22b9-35b1-ba21-81da121c3b93 | -2.53104 | -53.95869 | 2025-01-08 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fefd332a-7f07-3828-8cca-74997ecd6250 | 3.45906 | -60.21521 | 2025-01-08 04:55:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0145b041-f40e-375b-9981-ea93bba82ba2 | -2.86964 | -54.15817 | 2025-01-08 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 36aaea6c-a41e-38ec-b642-99d568fa4f53 | -2.67958 | -54.02851 | 2025-01-08 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2cf32627-148d-360c-b4fd-5959573d7354 | -2.76821 | -54.65314 | 2025-01-08 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1d5bdc05-e2ef-3b6a-9968-8b4f1de2bc83 | 3.90497 | -60.25446 | 2025-01-08 04:55:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6dd5f040-4e6f-3d72-ba4c-9f85822bae49 | 2.99147 | -61.18787 | 2025-01-08 04:55:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0f21874-0ce0-31e5-a82c-2d05e72a49a3 | 2.99099 | -61.18456 | 2025-01-08 04:55:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c861e71a-1caf-36ff-bb37-cb17f40dae72 | -2.60141 | -54.17982 | 2025-01-08 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8271e2f0-b9db-329a-8909-82c79cf4f450 | 3.00941 | -61.1613 | 2025-01-08 04:55:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93c81dbd-40bf-3e2e-963b-56b897bf03c1 | -12.36103 | -52.48375 | 2025-01-08 04:57:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dea4ae53-7890-32ca-afb2-71250f131220 | -12.35684 | -52.4874 | 2025-01-08 04:57:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9bea7f35-4ed6-3373-ac0e-46c518f63260 | -12.36043 | -52.48794 | 2025-01-08 04:57:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 938a3d16-908c-3e1f-8b9b-a361e035ec79 | -12.35385 | -52.48267 | 2025-01-08 04:57:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af932c7c-f799-3df3-bd55-5babaaef50c2 | -12.35325 | -52.48685 | 2025-01-08 04:57:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad0f3c07-f536-3f7e-ba67-a4fbe1372749 | -12.35744 | -52.48321 | 2025-01-08 04:57:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 17c67925-cc4a-35c7-9b1c-4758a6a93df0 | -21.55975 | -54.19828 | 2025-01-08 04:59:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 806f9617-3c11-33fd-a299-24be9e74000c | -24.07907 | -51.0146 | 2025-01-08 04:59:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 41f01ca1-cf3f-3ff4-ab1d-4f4e69ede7ba | -23.79359 | -50.2753 | 2025-01-08 04:59:00 | NOAA-20 | IBAITI | PARANÁ | Brasil | 4109708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| d4f9fbd4-1c29-348f-b642-00d5f9446d9c | -20.95657 | -49.74906 | 2025-01-08 04:59:00 | NOAA-20 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b00022b7-8e16-35ad-8ec6-6d0d2bb81706 | -20.12102 | -50.4204 | 2025-01-08 04:59:00 | NOAA-20 | TURMALINA | SÃO PAULO | Brasil | 3555307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 90743330-29e4-3dcc-a4f3-c8f75067efa0 | -23.79369 | -50.27414 | 2025-01-08 04:59:00 | NOAA-20 | IBAITI | PARANÁ | Brasil | 4109708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 49181f72-cbc8-38d7-9292-dc40eba87516 | -23.79255 | -50.28468 | 2025-01-08 04:59:00 | NOAA-20 | IBAITI | PARANÁ | Brasil | 4109708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |


[Clique aqui para ver as próximas entradas](README4.md)
