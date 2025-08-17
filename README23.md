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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 11c1a09e-27cd-357e-8cba-0c2e2cb8e5fd | -15.15217 | -48.76027 | 2025-08-17 04:17:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3a6c5faa-9ef2-352e-afdf-eb230f918c31 | -18.26989 | -45.15374 | 2025-08-17 04:17:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e55db5fe-34dd-3623-a6f8-6861c999894b | -14.60359 | -47.96003 | 2025-08-17 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9e1057d4-2b34-331c-a250-d700251e58c3 | -13.58612 | -47.77818 | 2025-08-17 04:17:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 32b3f958-c39e-331a-99b8-028373c3935d | -17.55344 | -46.61588 | 2025-08-17 04:17:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 03bb01c0-5753-3fdf-abac-937cdd6fb830 | -14.18469 | -45.31297 | 2025-08-17 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 19486f8b-621f-388c-af9b-294a07d0995e | -13.5897 | -47.77865 | 2025-08-17 04:17:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bb0da4d6-964f-384a-89bd-22c270e997bb | -22.21223 | -56.19809 | 2025-08-17 04:17:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b1087dc9-80f3-3fb8-8bc8-bc3d63cddb1f | -15.14428 | -48.74059 | 2025-08-17 04:17:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 30640e3b-6a40-3191-a640-17254bfc47ae | -16.07665 | -43.62411 | 2025-08-17 04:17:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f4ea446a-597b-3399-b5c2-97ce77ad0208 | -16.62769 | -51.38436 | 2025-08-17 04:17:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8abda559-f7a5-3476-ba63-b5442d1b2b15 | -13.42072 | -57.02944 | 2025-08-17 04:17:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 655e57c7-64a5-3392-8fe9-a6022f96c2da | -18.95829 | -43.74647 | 2025-08-17 04:17:00 | NOAA-20 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 15d8a0dc-0e43-322c-86b2-c58b5ee20796 | -18.76399 | -47.63805 | 2025-08-17 04:17:00 | NOAA-20 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ff823f5d-457f-3276-884f-49076ecdb562 | -16.73922 | -44.95837 | 2025-08-17 04:17:00 | NOAA-20 | IBIAÍ | MINAS GERAIS | Brasil | 3129608 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c23f1845-7791-315f-b213-7a0f2e8a4fb7 | -14.18631 | -45.32416 | 2025-08-17 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 45633543-f9e6-3493-8028-f3d5c38fe8a4 | -17.21656 | -49.5853 | 2025-08-17 04:17:00 | NOAA-20 | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2ad53240-6e75-33d7-9921-1dc8d4350226 | -20.21941 | -47.00621 | 2025-08-17 04:17:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4586f06a-0919-313d-941c-cac8b44cdb6d | -13.60032 | -47.75904 | 2025-08-17 04:17:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 208544c3-a039-3b7f-a8e7-7b5b4d0df0bf | -13.87519 | -45.55054 | 2025-08-17 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0eae34ee-b190-3649-ab47-4e36429839c3 | -14.183 | -45.32361 | 2025-08-17 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 04b90157-b9ad-3d24-a94c-a5ac4d6ba0c2 | -15.89905 | -48.34586 | 2025-08-17 04:17:00 | NOAA-20 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 089957aa-6d99-35f9-affa-e5722fc44bad | -14.95096 | -54.75658 | 2025-08-17 04:17:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7df9485c-a88e-3d9a-9231-c0370a41b619 | -21.41815 | -46.42855 | 2025-08-17 04:17:00 | NOAA-20 | CABO VERDE | MINAS GERAIS | Brasil | 3109501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| a17d1e66-0362-3760-9aae-7484e280726c | -13.59608 | -47.76249 | 2025-08-17 04:17:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 10ed5daa-14ff-3efe-a4be-86234f971822 | -25.18082 | -50.08104 | 2025-08-17 04:17:00 | NOAA-20 | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| abb81647-c0e1-350a-88fb-175b9facb550 | -14.97051 | -54.75583 | 2025-08-17 04:17:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 709cacc3-1c31-378c-b397-479983f578da | -13.58635 | -46.98061 | 2025-08-17 04:17:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df53eef2-f992-3bf6-93c1-2d089b18ecb5 | -26.61977 | -51.82198 | 2025-08-17 04:17:00 | NOAA-20 | ÁGUA DOCE | SANTA CATARINA | Brasil | 4200408 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 62df5ff5-e502-3697-8ac5-4244097a3b95 | -13.61519 | -47.7576 | 2025-08-17 04:17:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e98c9380-72b2-3801-b9a6-5bdd540f9eae | -15.14505 | -48.73617 | 2025-08-17 04:17:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f7d2c950-e625-3d5d-8fef-ed43a5fad834 | -16.49438 | -45.57081 | 2025-08-17 04:17:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5236cdb0-60de-37cc-bfd1-076885c6ae09 | -13.5854 | -47.78243 | 2025-08-17 04:17:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 22ac577d-1f86-3a02-b6eb-95fc140e0789 | -13.59391 | -46.97776 | 2025-08-17 04:17:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 31e0b359-3c86-3d0d-adb6-26bbb8ab944c | -14.34467 | -47.25632 | 2025-08-17 04:17:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c832d432-1fd7-3418-b487-3063a0963046 | -22.77022 | -49.15562 | 2025-08-17 04:19:00 | NOAA-20 | IARAS | SÃO PAULO | Brasil | 3519253 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6fab43c6-2a33-3f29-80a8-f779bf1a58f2 | -23.01898 | -46.23571 | 2025-08-17 04:19:00 | NOAA-20 | PIRACAIA | SÃO PAULO | Brasil | 3538600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 431c1c37-12b1-389c-bc1b-4a87dbcf28bc | -22.35922 | -48.35774 | 2025-08-17 04:19:00 | NOAA-20 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 767543fe-21fc-3bf1-b34c-80d261609b0b | -20.89243 | -56.9477 | 2025-08-17 04:19:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 329cd2de-3b50-3a1b-bfb5-29e9b1a84842 | -23.66586 | -47.40092 | 2025-08-17 04:19:00 | NOAA-20 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 73ca3c20-8608-3e50-b98b-7d5fea7b49fe | -20.51819 | -54.70498 | 2025-08-17 04:19:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6a88ba2f-ff35-3212-b924-25e7b7ba7352 | -21.65546 | -53.44954 | 2025-08-17 04:19:00 | NOAA-20 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fda260f5-64b2-3862-8f19-cb4435286850 | -22.76902 | -49.15876 | 2025-08-17 04:19:00 | NOAA-20 | IARAS | SÃO PAULO | Brasil | 3519253 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4cd34d76-51b1-30ea-b7a1-eef32e75ab09 | -22.80252 | -47.46872 | 2025-08-17 04:19:00 | NOAA-20 | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 1d315dba-ce35-324e-872d-ae706ef4dc1b | -22.09263 | -51.3924 | 2025-08-17 04:19:00 | NOAA-20 | PRESIDENTE PRUDENTE | SÃO PAULO | Brasil | 3541406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| c6715064-6968-33c6-9a97-c018109313a9 | -20.55485 | -54.67329 | 2025-08-17 04:19:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c864338d-13f0-3781-b678-5303d3c8ef14 | -29.77926 | -51.17797 | 2025-08-17 04:19:00 | NOAA-20 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 1.8 |
| d698f5ae-f996-3740-aec7-7791f632b30d | -23.66315 | -47.39654 | 2025-08-17 04:19:00 | NOAA-20 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| d64ff86d-a27d-33e6-b07f-3d5e00c2732f | -22.36056 | -48.35718 | 2025-08-17 04:19:00 | NOAA-20 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 68462afe-de10-3dc6-9cbb-fe2ffb364a3b | -21.93353 | -44.6489 | 2025-08-17 04:19:00 | NOAA-20 | AIURUOCA | MINAS GERAIS | Brasil | 3101201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 16475c2e-faf7-3fb5-a4e0-a391298e6ba7 | -22.80192 | -47.47246 | 2025-08-17 04:19:00 | NOAA-20 | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 28d45288-1b89-31bc-9b3b-31fc10751af2 | -21.07086 | -49.39191 | 2025-08-17 04:19:00 | NOAA-20 | POTIRENDABA | SÃO PAULO | Brasil | 3540804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 4c64a63a-2a2a-3887-8d05-8f7c28e2971e | -22.13477 | -45.04246 | 2025-08-17 04:19:00 | NOAA-20 | SÃO LOURENÇO | MINAS GERAIS | Brasil | 3163706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 764fe106-ce34-3348-9cef-94a5e259af5b | -20.88447 | -56.95782 | 2025-08-17 04:19:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0e04b558-73c4-3f92-a7cd-ed4d177f3990 | -23.09583 | -46.96699 | 2025-08-17 04:19:00 | NOAA-20 | LOUVEIRA | SÃO PAULO | Brasil | 3527306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f041d32f-6b27-300c-b129-537b3630e4ee | -20.89784 | -56.9492 | 2025-08-17 04:19:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9cc33767-8137-3fc8-a02d-f99a7a0aed13 | -23.51 | -47.37636 | 2025-08-17 04:19:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3646f86a-e58c-3403-800a-6af2a0389d72 | -21.65124 | -53.451 | 2025-08-17 04:19:00 | NOAA-20 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c468c9f1-fef8-3ed8-a273-d5de1e3d45df | -27.33252 | -51.30413 | 2025-08-17 04:19:00 | NOAA-20 | ERVAL VELHO | SANTA CATARINA | Brasil | 4205209 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| cd74cc32-f945-357d-ac70-ffc6f04ab6b8 | -21.07509 | -49.38839 | 2025-08-17 04:19:00 | NOAA-20 | POTIRENDABA | SÃO PAULO | Brasil | 3540804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 861a8f02-ac8c-3f01-896b-328d4aaf1cb6 | -20.87906 | -56.95631 | 2025-08-17 04:19:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1e00cf7e-a01c-3b8b-8cdf-3f6232b30ec2 | -21.0644 | -50.30577 | 2025-08-17 04:19:00 | NOAA-20 | BURITAMA | SÃO PAULO | Brasil | 3508108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 23f90708-e8cd-3992-8929-b8824c92f221 | -23.01841 | -46.23948 | 2025-08-17 04:19:00 | NOAA-20 | PIRACAIA | SÃO PAULO | Brasil | 3538600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 0c2eb4aa-5d38-346f-815a-41926c2ebd94 | -21.47254 | -47.01172 | 2025-08-17 04:19:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5f43ade7-0868-3186-9b95-7c24c27451b4 | -23.02231 | -46.23631 | 2025-08-17 04:19:00 | NOAA-20 | PIRACAIA | SÃO PAULO | Brasil | 3538600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d662364a-187a-3b1e-938d-f1c5f30dfb6d | -20.51927 | -54.70544 | 2025-08-17 04:19:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 43ddf67c-67f4-3834-b866-8420bee7ccf6 | -26.88769 | -52.46001 | 2025-08-17 04:19:00 | NOAA-20 | XANXERÊ | SANTA CATARINA | Brasil | 4219507 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2916cfef-464f-324b-9632-d3fdcf0adb0e | -23.66255 | -47.4003 | 2025-08-17 04:19:00 | NOAA-20 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| c98596fd-2cbe-3c23-96f7-0c132e36849b | -20.89146 | -50.91096 | 2025-08-17 04:19:00 | NOAA-20 | PEREIRA BARRETO | SÃO PAULO | Brasil | 3537404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ace42944-2f5c-34b8-acd5-54525f730074 | -20.89235 | -50.90607 | 2025-08-17 04:19:00 | NOAA-20 | PEREIRA BARRETO | SÃO PAULO | Brasil | 3537404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| c6f4ffc7-3b6f-316c-ab0e-bf57cc2cb4c3 | -21.06805 | -50.30657 | 2025-08-17 04:19:00 | NOAA-20 | BURITAMA | SÃO PAULO | Brasil | 3508108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f793c49d-019b-3f62-b8a2-2e2bb13fbd95 | -23.66646 | -47.39716 | 2025-08-17 04:19:00 | NOAA-20 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f1de57c8-0f2a-3a09-aac4-b34e31d6a99b | -23.06175 | -46.64212 | 2025-08-17 04:19:00 | NOAA-20 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f55d12fc-40f3-305d-953f-10eb296e36d7 | -9.518 | -60.5268 | 2025-08-17 04:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 47.8 |
| d909f9f8-4f71-3553-ba7b-335966e73b32 | -9.5179 | -60.5461 | 2025-08-17 04:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 40.2 |
| fedf8aa4-b445-3972-a324-531f5acb3141 | -8.9788 | -60.4964 | 2025-08-17 04:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 6562d0cc-bb65-375d-9592-e0840b43483c | -10.8436 | -45.3586 | 2025-08-17 04:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 65.7 |
| b5a1a4e2-e097-3bd7-8f8d-7bcf42a5a9ea | -9.518 | -60.5268 | 2025-08-17 04:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 42.4 |
| b5c79809-4d4a-3a34-bcdf-9760d73d9eda | -8.9788 | -60.4964 | 2025-08-17 04:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| f8c0e220-ccb4-30ce-bdba-af0e82f201e5 | -9.4994 | -60.5278 | 2025-08-17 04:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 44.3 |
| d2892ffd-0303-35b0-a8af-931461b137c7 | -8.9788 | -60.4964 | 2025-08-17 04:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 7b43cfa6-2acf-3b1d-b0de-a875e5be8f7c | -9.518 | -60.5268 | 2025-08-17 04:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 52.6 |
| c775077c-08b6-3d19-a6fc-863961f2370d | -8.9788 | -60.4964 | 2025-08-17 04:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 0b04d839-f93a-354b-84e2-ba8165c515b1 | -9.4994 | -60.5278 | 2025-08-17 04:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 48.6 |
| fc72a4a4-9d60-3084-873a-1915c0503f6c | -9.518 | -60.5268 | 2025-08-17 04:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 219ea4f1-167a-3368-b885-4183b646a14c | -9.1895 | -59.6364 | 2025-08-17 04:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 874bda93-9ab5-3090-814f-70e1654ad442 | -10.844 | -45.3356 | 2025-08-17 05:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 53.2 |
| c638d230-35d3-301b-abc7-66bf60dd4b33 | -23.6985 | -51.7687 | 2025-08-17 05:00:00 | GOES-19 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 51.2 |
| 372e480d-86d1-3477-9785-634321dbf1f9 | -9.518 | -60.5268 | 2025-08-17 05:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 713a6131-56b4-349a-9d6c-d275cdf4dc4d | -8.9788 | -60.4964 | 2025-08-17 05:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| c38516da-4286-3bc1-adf1-d6bc8e1a12de | -14.9819 | -54.7536 | 2025-08-17 05:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 62.0 |
| a2ca20bf-6ec2-3375-97a9-e6c1394e4953 | 0.96578 | -60.41042 | 2025-08-17 05:01:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 981e724d-8622-38e9-ad69-b5e4f19cfe90 | 0.96737 | -60.41001 | 2025-08-17 05:01:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9922bfdc-f20b-3fda-8f2b-2ae9241a363a | -0.55153 | -52.17725 | 2025-08-17 05:01:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 935ae748-a563-3198-a311-4dccb08af907 | -8.50417 | -44.73436 | 2025-08-17 05:04:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 92f8e732-488e-39c3-89a9-2d9576e970be | -3.97525 | -42.53189 | 2025-08-17 05:04:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 2e349c5e-e3bf-3f70-b850-ac0f2c79fadd | -6.13072 | -57.93299 | 2025-08-17 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f1a08954-1e49-34bf-bb19-0164960f5f6a | -8.50355 | -44.73931 | 2025-08-17 05:04:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 7189f456-415f-30a3-9979-703e18fb27c5 | -6.66758 | -58.81677 | 2025-08-17 05:04:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b0bc235-cd8d-364e-92de-884552196a5a | -7.60491 | -44.93731 | 2025-08-17 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |


[Clique aqui para ver as próximas entradas](README24.md)
