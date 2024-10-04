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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eb5d4011-6a4a-308a-ba37-1739c841620d | -19.3167 | -42.5724 | 2024-10-04 01:16:52 | GOES-16 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 61.3 |
| 7fb4da43-59d3-3742-9dec-5f3e43520024 | -19.4899 | -42.8746 | 2024-10-04 01:16:53 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 109.7 |
| 70edf987-5051-36b7-88d7-f7fb54d54ee5 | -19.5104 | -42.8691 | 2024-10-04 01:16:53 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 93.5 |
| f7020074-3e13-367a-b050-a652ef0cd809 | -20.083 | -43.4332 | 2024-10-04 01:16:56 | GOES-16 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 78.0 |
| 1d83d2b7-eed5-3e69-9af7-2a7323d25d87 | -20.1036 | -43.4276 | 2024-10-04 01:16:56 | GOES-16 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 80.9 |
| 72a24192-0c3a-3a78-baef-67cbae365860 | -20.121 | -43.5219 | 2024-10-04 01:16:56 | GOES-16 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 78.1 |
| 31b833b4-5de3-3425-b8f9-daf30628768d | -20.1416 | -43.5162 | 2024-10-04 01:16:57 | GOES-16 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 81.0 |
| 7117b5c9-7c41-3497-bb94-398c1c2c793d | -20.0111 | -48.6869 | 2024-10-04 01:16:57 | GOES-16 | PLANURA | MINAS GERAIS | Brasil | 3151602 | 31 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 028e92b3-e844-391d-995b-a497cce95be6 | -20.4591 | -43.1795 | 2024-10-04 01:16:58 | GOES-16 | DIOGO DE VASCONCELOS | MINAS GERAIS | Brasil | 3121704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 92.3 |
| 463a8227-d9e7-344f-8311-61e97d8d062d | -21.3334 | -48.8044 | 2024-10-04 01:17:04 | GOES-16 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 91.4 |
| 904ce394-04de-380d-93f9-5effb48f62d6 | -21.3534 | -48.8229 | 2024-10-04 01:17:04 | GOES-16 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 87.1 |
| 0e3aec80-7f37-3d85-ad91-c537cdcb2b60 | -21.3541 | -48.7996 | 2024-10-04 01:17:04 | GOES-16 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 121.0 |
| 0916bf78-d2b5-397b-b9bc-1938779600b3 | -21.7988 | -48.3691 | 2024-10-04 01:17:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 113.3 |
| f50e3ba8-124e-3fbf-90dc-561c544c2bbf | -21.8079 | -48.7626 | 2024-10-04 01:17:06 | GOES-16 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 4b35c6c2-a0e2-3a03-bf32-9a0fe53e4f82 | -21.8175 | -48.4346 | 2024-10-04 01:17:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 0601ceca-39fb-3c48-be6a-6d026537f759 | -21.8189 | -48.3876 | 2024-10-04 01:17:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 86.6 |
| ef5d92cc-25f3-3efc-b392-7735b81c5eec | -21.8196 | -48.3641 | 2024-10-04 01:17:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 7ce2d92e-c480-3496-98e8-66850c9ed16e | -21.8376 | -48.4531 | 2024-10-04 01:17:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 89.1 |
| a1b77b87-b2db-3ba0-938d-de841b1f1a6d | -21.8383 | -48.4296 | 2024-10-04 01:17:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 95.8 |
| cb2b372a-fa3e-3bc6-813f-fae5711409e3 | -2.9493 | -52.7952 | 2024-10-04 01:25:23 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 91c39a4b-9d8c-347a-80f2-0ae499e1e330 | -2.9494 | -52.7748 | 2024-10-04 01:25:23 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 462317e3-4289-387e-8380-f097cde4d328 | -3.2349 | -50.3695 | 2024-10-04 01:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 711fc07c-007a-373f-aae5-b3d7fb2eac2d | -3.2534 | -50.3689 | 2024-10-04 01:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| c851d99c-386c-3a3d-ab8f-1ac7b8a245a7 | -3.404 | -42.2858 | 2024-10-04 01:25:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| d8594384-c362-367d-be70-e8f58d22b64a | -3.4227 | -42.2849 | 2024-10-04 01:25:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 638f48f9-2ef6-3554-b87b-c0f2a6ce6c9e | -3.2899 | -50.4725 | 2024-10-04 01:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 104.5 |
| 69d26f61-98ee-3bf6-b79e-74e630b1b9a7 | -3.2899 | -50.4516 | 2024-10-04 01:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 186.7 |
| 0a17810f-9a88-3907-a92e-4cf10db43d0f | -3.3083 | -50.4719 | 2024-10-04 01:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 141.4 |
| 66007fc1-5fc0-3e1a-8558-90b6cfa93ae7 | -3.3084 | -50.451 | 2024-10-04 01:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 240.8 |
| e6b7422f-8a0c-3acb-988d-64381f8de9cf | -3.3085 | -50.43 | 2024-10-04 01:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 9000ef97-f5ae-32db-b116-1ebf5ca2bbde | -3.4915 | -50.8004 | 2024-10-04 01:25:26 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| c6c783eb-ecf9-3fc8-9012-eade18f559b5 | -4.0949 | -48.4894 | 2024-10-04 01:25:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| ccd67d6b-0d61-3228-b12c-700da76ba3ec | -4.5375 | -43.304 | 2024-10-04 01:25:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 94c8c417-8f79-3630-a1b5-d14036ba871a | -5.5033 | -48.8046 | 2024-10-04 01:25:37 | GOES-16 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| c9f48f92-e84c-35be-baff-58c0776f8b15 | -5.8214 | -44.1426 | 2024-10-04 01:25:39 | GOES-16 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 70fc7e59-bdb4-3ce9-9657-3409d7b130b4 | -5.8216 | -44.1196 | 2024-10-04 01:25:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 121.4 |
| 60012d1c-a779-37fc-aa29-a08f3b9a59cd | -5.9786 | -45.3847 | 2024-10-04 01:25:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| d0c6e9d8-86d2-3ac3-8bb9-0242263c8c88 | -8.6448 | -50.0518 | 2024-10-04 01:25:55 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 149.9 |
| f66ef3d4-d841-36d7-b660-170395c56e15 | -8.6636 | -50.0501 | 2024-10-04 01:25:55 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 92.3 |
| f6f569b5-f50b-33e2-b991-c168173e1f94 | -22.4459 | -50.1021 | 2024-10-04 01:25:55 | METOP-B | ECHAPORÃ | SÃO PAULO | Brasil | 3514700 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 80bc5a55-e453-3982-ad48-8657c7ed2081 | -8.649 | -66.6582 | 2024-10-04 01:25:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| fac49824-b35b-3a21-bbdf-91a057d7840a | -8.6491 | -66.6396 | 2024-10-04 01:25:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| b219d3ed-9adc-32ca-af1f-aaa61717577b | -8.6676 | -66.6391 | 2024-10-04 01:25:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| d6e1b728-e463-3fa7-86a7-3c813a7a9cdb | -21.812599 | -48.361198 | 2024-10-04 01:25:57 | METOP-B | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 142fc7ac-4043-35f2-a0a8-2a4599649f6d | -21.8258 | -48.4072 | 2024-10-04 01:25:57 | METOP-B | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b88daafd-7628-31c2-b561-4beb9b2ebcc4 | -21.7964 | -48.341202 | 2024-10-04 01:25:57 | METOP-B | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 85f0f3b3-dd08-358d-824d-3cafee9a236b | -21.802999 | -48.364399 | 2024-10-04 01:25:57 | METOP-B | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e330b833-f883-3b0d-ac2a-478899d2cee4 | -21.7869 | -48.344398 | 2024-10-04 01:25:57 | METOP-B | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a60aabf0-f44b-3b02-928e-3703e4b5dce4 | -21.793501 | -48.367599 | 2024-10-04 01:25:57 | METOP-B | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 76e399be-814d-3c43-8854-2d12b817093d | -21.8067 | -48.413601 | 2024-10-04 01:25:57 | METOP-B | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 6bad1a00-6f12-3461-a262-e104508756e7 | -21.8132 | -48.436501 | 2024-10-04 01:25:57 | METOP-B | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 90f1df9f-cc19-3039-a259-67c4bf531be2 | -21.7773 | -48.347599 | 2024-10-04 01:25:57 | METOP-B | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c7b0c9ec-613e-32cb-b203-3972fb9f99d6 | -21.783899 | -48.370701 | 2024-10-04 01:25:57 | METOP-B | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 887e55c3-ceb9-368c-b583-0911aa9cc351 | -21.790501 | -48.393799 | 2024-10-04 01:25:57 | METOP-B | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 1ee54537-92a7-39e7-85d5-4f2de2aeb1d6 | -21.7971 | -48.416698 | 2024-10-04 01:25:57 | METOP-B | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 7e97c84a-4e75-3adc-ae6e-467e60dc9a4d | -21.8036 | -48.439602 | 2024-10-04 01:25:57 | METOP-B | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 2fb743cf-9b02-307a-849c-b7d5104eb645 | -9.1158 | -51.5315 | 2024-10-04 01:25:58 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| ace8cf66-beeb-38e2-a473-feb7c3771807 | -9.0347 | -67.39 | 2024-10-04 01:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 27162ae0-f94f-34c9-9b73-c67d709b0075 | -9.0898 | -67.4997 | 2024-10-04 01:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 6c097ce3-d40a-3526-bebc-70661b8e6d0e | -9.1084 | -67.4993 | 2024-10-04 01:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 88212182-6b60-31c1-b92e-87f3076254d8 | -21.767799 | -48.3507 | 2024-10-04 01:25:58 | METOP-B | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b0e07454-69c8-33e2-aeaf-c4b2d9e4af95 | -21.774401 | -48.373798 | 2024-10-04 01:25:58 | METOP-B | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 61af7f13-9f3f-39c9-9174-c89f0cd721c3 | -21.7876 | -48.4198 | 2024-10-04 01:25:58 | METOP-B | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 251b80ef-97a9-3b93-87a8-e6c5637fbe71 | -9.3115 | -50.8203 | 2024-10-04 01:25:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 95.1 |
| a3773a7b-4bfa-34c1-9df1-c30e664b948b | -9.3118 | -50.7991 | 2024-10-04 01:25:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 137.4 |
| 336fb6ef-f462-38c2-a8eb-d446dc0d62ca | -9.3303 | -50.8186 | 2024-10-04 01:25:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 5d26c7fd-6832-3983-bd0f-e761705073cb | -9.3306 | -50.7974 | 2024-10-04 01:25:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 20a954c9-3188-3eb8-9908-496bbd3dffc6 | -21.794201 | -48.736198 | 2024-10-04 01:25:59 | METOP-B | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 411858af-636f-3cb9-8afa-b31e45ca170f | -21.784599 | -48.739399 | 2024-10-04 01:25:59 | METOP-B | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 967c4b11-9c8f-3ce1-8975-a9404ac07fc7 | -21.7908 | -48.761299 | 2024-10-04 01:25:59 | METOP-B | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 38261ee5-e082-3404-9b5a-0b2d25ebbd89 | -21.561701 | -48.469398 | 2024-10-04 01:26:01 | METOP-B | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 1ed01a92-96d6-37df-9b54-615fb511f4ba | -21.5522 | -48.4725 | 2024-10-04 01:26:02 | METOP-B | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a9d73533-ae74-34ca-bba5-d60645ad85f5 | -22.2479 | -51.4603 | 2024-10-04 01:26:04 | METOP-B | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bce92077-12a9-3f56-ab45-1ea41c2dd321 | -22.251801 | -51.4748 | 2024-10-04 01:26:04 | METOP-B | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cd2ee157-2ad2-3338-8a9e-fd82ea13c97e | -10.4424 | -50.7336 | 2024-10-04 01:26:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 46.2 |
| eb4f11d9-5ba1-3324-927e-b7454afbdd31 | -21.329599 | -48.864101 | 2024-10-04 01:26:07 | METOP-B | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 801ba5ec-4b20-31ae-adda-8139f7540c88 | -21.3358 | -48.886002 | 2024-10-04 01:26:07 | METOP-B | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 3776367c-4f95-3157-9c67-f881e1439a98 | -21.313801 | -48.845299 | 2024-10-04 01:26:07 | METOP-B | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 6474ca9c-b6c6-3d11-8a44-a195e7dec27c | -21.32 | -48.867199 | 2024-10-04 01:26:07 | METOP-B | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 8b786691-489d-3b9d-b07a-fb4d96201362 | -21.3262 | -48.889099 | 2024-10-04 01:26:07 | METOP-B | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ea618468-5cd7-3efa-a968-281d1c508ac9 | -21.3043 | -48.8484 | 2024-10-04 01:26:07 | METOP-B | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 6fd82308-c239-3b19-b66e-085c311db0e0 | -21.310499 | -48.870399 | 2024-10-04 01:26:07 | METOP-B | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 7e6f4e19-c308-3a4c-aac9-4502770fbb12 | -21.3167 | -48.8922 | 2024-10-04 01:26:07 | METOP-B | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ecec8ca8-fbe6-37f5-a0cf-6f3d3244464f | -21.294701 | -48.851501 | 2024-10-04 01:26:07 | METOP-B | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ece46af2-2117-329a-a941-c5ad0dee9532 | -21.3009 | -48.873501 | 2024-10-04 01:26:07 | METOP-B | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 04b3c66c-3ff7-3802-9b13-d00eaefdd6cf | -21.3071 | -48.895302 | 2024-10-04 01:26:07 | METOP-B | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 527ae646-b98a-38cf-88f7-a4b85e33a7f7 | -21.33 | -48.791801 | 2024-10-04 01:26:07 | METOP-B | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7da3880f-c5e2-3cbd-839d-0b88931d0da9 | -21.336201 | -48.8139 | 2024-10-04 01:26:07 | METOP-B | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f67fe7e0-ef80-35b8-a1ed-efb67fb86a00 | -21.320499 | -48.794899 | 2024-10-04 01:26:07 | METOP-B | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 37cda073-ab38-345d-966c-18ca51fdfdb8 | -21.3267 | -48.817001 | 2024-10-04 01:26:07 | METOP-B | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 461734f1-4459-3b03-8e62-0c64b570bed3 | -21.298 | -48.826401 | 2024-10-04 01:26:07 | METOP-B | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2144418e-e86f-3d83-a41b-512e63072058 | -11.0532 | -46.5344 | 2024-10-04 01:26:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 555315e0-15ba-329d-ad6b-a439c251e742 | -11.0536 | -46.5118 | 2024-10-04 01:26:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 91a99f88-1391-3b42-b4c1-3f5244d61d16 | -11.0723 | -46.5319 | 2024-10-04 01:26:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 718d023b-7bb6-3a90-87b6-2a26fd3aa044 | -11.0727 | -46.5093 | 2024-10-04 01:26:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 9757c486-18e3-359f-9778-2806133c6531 | -11.0921 | -46.4843 | 2024-10-04 01:26:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 2fa6514d-fe6b-3ac7-b77a-7a7c929125b5 | -21.2852 | -48.854599 | 2024-10-04 01:26:08 | METOP-B | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 1b457316-38cf-3845-ac8c-02cf646f59d4 | -21.291401 | -48.876598 | 2024-10-04 01:26:08 | METOP-B | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e00b98e9-7bd0-343b-9be7-ed52349c335c | -21.2976 | -48.898399 | 2024-10-04 01:26:08 | METOP-B | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 73aea9c1-6071-31fd-bb91-b9de58c2e5fb | -21.2756 | -48.8577 | 2024-10-04 01:26:08 | METOP-B | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README32.md)
