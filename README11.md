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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 399d32e3-7007-3407-887d-a4595d85538b | -6.6949 | -58.7485 | 2026-09-02 01:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 5436759f-917b-312e-b9be-bb2bb86f5df1 | -8.5728 | -63.1807 | 2026-09-02 01:50:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 7fd9065d-9e58-3cef-aa44-66ddfb378d47 | -11.3521 | -50.6373 | 2026-09-02 01:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 94.3 |
| ae0094b3-6c29-33dd-b3ea-f00d5829793f | -12.1512 | -47.0833 | 2026-09-02 01:50:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 133.2 |
| 17ee3ecc-5ae9-3b48-9601-ecdce77fd50a | -11.3331 | -50.6394 | 2026-09-02 01:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 3192528f-f61b-33c0-b5ab-50a4bdcf5178 | -10.9013 | -45.3279 | 2026-09-02 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.6 |
| e7fcfd07-70b6-3479-bbf2-828cc5bcb3d6 | -6.6948 | -58.7678 | 2026-09-02 01:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 0ab2b9f1-f291-3b9d-96bb-4ef3dd21a7a1 | -11.3524 | -50.6159 | 2026-09-02 01:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 156.5 |
| bb301272-afa3-3812-8ca6-dfb0c697ce42 | -12.8839 | -45.8412 | 2026-09-02 01:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 0a993073-9d62-37a3-82b9-737bc6868a4f | -8.4669 | -54.7237 | 2026-09-02 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 122.2 |
| a4aa6519-d020-3538-beb2-1a25b29c5601 | -11.3334 | -50.618 | 2026-09-02 01:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 190.4 |
| 4bf51a03-c0d1-369a-94d3-d2c656c61e11 | -9.862 | -64.9771 | 2026-09-02 01:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 68.5 |
| d1cb317d-5123-3ba8-96aa-491bdf595ff9 | -11.7906 | -50.5236 | 2026-09-02 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 224.2 |
| 03a14680-e26a-38df-bc40-670aa14e7dff | -10.7965 | -44.7437 | 2026-09-02 01:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 38.6 |
| 6e7e2641-c294-3e1b-898c-1d646217cd07 | -10.7962 | -44.7669 | 2026-09-02 01:50:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 77.6 |
| d9162087-e714-3181-9cf4-1bc1bc35ad15 | -10.7774 | -44.7463 | 2026-09-02 01:50:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 277f3a97-96e8-3e58-b0e1-808e8cb6f3fa | -8.4483 | -54.725 | 2026-09-02 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 109.8 |
| b6eb217b-07a2-35df-b9c1-5c473c345589 | -7.2006 | -60.6706 | 2026-09-02 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 42.5 |
| ba9d6845-0edd-38c4-a967-bcb706826e6b | -8.4296 | -54.7262 | 2026-09-02 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| d1c9566c-b8d2-3f63-bbdf-c89de8ac8f76 | -12.1516 | -47.0608 | 2026-09-02 01:50:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 156.1 |
| 1acb11f8-2b11-396a-ab53-d9e35d160332 | -11.7716 | -50.5258 | 2026-09-02 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 130.8 |
| 5f88a979-1e00-3729-acfa-071318732aab | -12.1504 | -47.1283 | 2026-09-02 01:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| f4530bed-5d18-308f-8510-73a701aa6b3c | -11.7906 | -50.5236 | 2026-09-02 02:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 218.1 |
| 9ef30517-86a9-344a-a36d-530d2e0ae74d | -7.2006 | -60.6706 | 2026-09-02 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 9d2455c7-4f11-33fb-9862-50112d45b3cd | -10.7965 | -44.7437 | 2026-09-02 02:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 44.4 |
| 2277096c-461c-3fbb-88a5-33e4fe530b08 | -10.7774 | -44.7463 | 2026-09-02 02:00:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 717abd99-b29c-3350-9f76-53239162bc16 | -8.5727 | -63.1996 | 2026-09-02 02:00:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 840856a3-e8f6-33f5-ac85-32b07ae6445a | -11.3524 | -50.6159 | 2026-09-02 02:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 142.0 |
| 379b1ad5-bce7-3ded-b3d1-b9b0e74c4502 | -17.0878 | -56.8534 | 2026-09-02 02:00:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.6 |
| 3f536640-c3fd-361c-af73-2a0f111f6e26 | -8.4485 | -54.7048 | 2026-09-02 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 160.0 |
| 8ea0406c-59f6-331e-9ddb-81d20f62698b | -12.1512 | -47.0833 | 2026-09-02 02:00:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 5843faa8-665d-3e96-8ef3-1f2f326aafea | -8.5728 | -63.1807 | 2026-09-02 02:00:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 89375e09-d213-329b-a90a-9f2dd1b09980 | -12.1516 | -47.0608 | 2026-09-02 02:00:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 126.9 |
| b098e9cf-5327-312d-a269-d77b0b62d3f8 | -8.4483 | -54.725 | 2026-09-02 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 131.4 |
| 1b226b78-25e4-3244-a413-ac934073b110 | -10.92 | -45.3483 | 2026-09-02 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 329c33bc-e259-32b6-bc94-6a5e11e7242e | -11.3334 | -50.618 | 2026-09-02 02:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 165.7 |
| ff32a33d-c005-3b25-80e0-ca700d49a4f7 | -8.4298 | -54.706 | 2026-09-02 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 123.3 |
| 39291ff5-57b5-35a1-912c-c8ab5d175b7e | -12.8843 | -45.8183 | 2026-09-02 02:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 124.5 |
| a00ec70b-95bb-37f5-9b39-599db5618a99 | -11.7903 | -50.545 | 2026-09-02 02:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.2 |
| fc69b3d3-bbbc-3293-85d9-535744a764f3 | -8.4296 | -54.7262 | 2026-09-02 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 02630852-6510-321f-be21-7d2dfb26c6f2 | -13.9853 | -58.6919 | 2026-09-02 02:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 58.6 |
| b3e2c722-019a-3f02-aeee-2f4f77ac11a9 | -11.7716 | -50.5258 | 2026-09-02 02:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 142.7 |
| 1c2fafd6-3a4e-3351-a42c-34e7cbd1bc0a | -11.3521 | -50.6373 | 2026-09-02 02:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 29dcb51e-02dc-3ec7-b63b-7b24aa40c6f8 | -12.132 | -47.086 | 2026-09-02 02:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 560ed908-4b89-389d-a6e5-9116c0d89993 | -14.0044 | -58.6902 | 2026-09-02 02:00:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 43.0 |
| 4289a42e-0997-3c67-a247-6ef5f602b6d4 | -12.865 | -45.8213 | 2026-09-02 02:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 0abb4781-c647-3870-b902-4f62063caf6b | -6.6948 | -58.7678 | 2026-09-02 02:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 48.1 |
| dc8f2235-b466-3250-a98b-eb7e58db814d | -13.9855 | -58.672 | 2026-09-02 02:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 6dc2980e-7f0d-3a07-9989-ce0310cefd68 | -8.4671 | -54.7035 | 2026-09-02 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 205.2 |
| b40016c4-ff7f-3b8d-89b1-0d1f6d010c6b | -12.1504 | -47.1283 | 2026-09-02 02:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 1eec3ad3-fcf6-34ea-ae80-dca381401cef | -10.7962 | -44.7669 | 2026-09-02 02:00:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 020a1e04-1cb9-38b9-a2ee-ebb1bf0c8e52 | -10.9009 | -45.3509 | 2026-09-02 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 256.5 |
| 4082cd85-6ea9-3465-86f5-874c8de026df | -11.791 | -50.5021 | 2026-09-02 02:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 309bad08-fffc-3228-a3de-cde2083cee13 | -10.777 | -44.7695 | 2026-09-02 02:00:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 93.9 |
| fc387628-9917-3050-833d-4b17512dec94 | -12.1324 | -47.0635 | 2026-09-02 02:00:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 73c47462-3d4c-3d3c-9130-849305eaeb40 | -8.4669 | -54.7237 | 2026-09-02 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 212.5 |
| 587fa69c-074f-34d4-9491-8a9e4a742289 | -10.9013 | -45.3279 | 2026-09-02 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 205.8 |
| faea326e-d311-3192-b7ff-2606f8cdc87e | -12.1312 | -47.1309 | 2026-09-02 02:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 61ded094-f4d4-3e64-8919-8fd72b955078 | -12.0936 | -47.0913 | 2026-09-02 02:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 27d56268-5d74-3399-9e60-8f0cdf6548e3 | -13.9855 | -58.672 | 2026-09-02 02:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 49.9 |
| ace2591f-3a8d-3d32-8fc1-f967b3dd72ff | -6.6949 | -58.7485 | 2026-09-02 02:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 5a520beb-8d01-35dd-b63c-bf74ab622f06 | -10.8822 | -45.3305 | 2026-09-02 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 06c6427c-265d-3b13-b62e-5179de38ffc2 | -12.1324 | -47.0635 | 2026-09-02 02:10:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 131.9 |
| b7f26451-756d-3180-ae67-384a4ca14a8a | -10.7965 | -44.7437 | 2026-09-02 02:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 57a2920d-55ba-3e83-9bff-d9b4a5a3b830 | -12.8843 | -45.8183 | 2026-09-02 02:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 40052a19-474b-3798-9f81-f9760d89202a | -10.8818 | -45.3534 | 2026-09-02 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 68c57508-910c-3cb5-91aa-e6d96b68bc3b | -8.4669 | -54.7237 | 2026-09-02 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 138.2 |
| 4da138cc-a201-34a9-b848-6df61bf33ceb | -12.132 | -47.086 | 2026-09-02 02:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 89.5 |
| e0a51dd3-2616-392e-9c28-8632c933b59d | -11.7906 | -50.5236 | 2026-09-02 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 192.5 |
| 2086c5a0-cb61-3cf1-8f63-0cf4077a6834 | -8.4298 | -54.706 | 2026-09-02 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 116.2 |
| 0548b8db-f87e-3514-b5d0-efceb2309065 | -10.9204 | -45.3253 | 2026-09-02 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.6 |
| ce8fbb05-a8a2-3f4e-aa22-dd832a0116f4 | -11.3524 | -50.6159 | 2026-09-02 02:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 185.9 |
| aa2e7402-b367-36ba-a2bb-ffe6de6f0468 | -10.9009 | -45.3509 | 2026-09-02 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 214.7 |
| 67c97b1c-fa0e-37ee-bff1-109c0a4b11c9 | -12.1512 | -47.0833 | 2026-09-02 02:10:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 39a9334a-7dc0-3234-bfcd-1821026cc345 | -11.3334 | -50.618 | 2026-09-02 02:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 194.2 |
| 88b3cdff-bfcc-3cc7-b4a2-1fe1da2bc902 | -10.9013 | -45.3279 | 2026-09-02 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 217.1 |
| 815f2299-327b-39db-a458-20ff367ca52a | -10.7774 | -44.7463 | 2026-09-02 02:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 7e9c05ba-a538-3397-b8a0-9f5addeed715 | -10.92 | -45.3483 | 2026-09-02 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 86.4 |
| b506571f-81ee-3077-b188-1430a234be26 | -11.3331 | -50.6394 | 2026-09-02 02:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 4fe55700-c6e0-38f3-ba98-871fde4f70f6 | -11.7716 | -50.5258 | 2026-09-02 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 149.3 |
| c5aeed89-ca5d-3056-8836-14bb41899769 | -8.5542 | -63.1814 | 2026-09-02 02:10:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 52.2 |
| a8fa07aa-643c-32db-83a6-f2beef4192e3 | -10.3956 | -49.9918 | 2026-09-02 02:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| f4a2229b-43b6-3ed3-bb4a-f04262ccddcd | -11.3337 | -50.5966 | 2026-09-02 02:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 3584f9d0-4dea-3f86-8d04-988e627d1e85 | -12.1504 | -47.1283 | 2026-09-02 02:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 423d95a4-a05e-34fc-b0ac-6200b8a3accb | -6.6764 | -58.7686 | 2026-09-02 02:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 4e0903a8-6db1-347c-8820-bff352c84c84 | -7.2006 | -60.6706 | 2026-09-02 02:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 0df6d8a1-c892-31dc-835c-7b9393c6eb11 | -6.6948 | -58.7678 | 2026-09-02 02:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 153dbdaa-443c-3b13-b98c-58454567704a | -8.4483 | -54.725 | 2026-09-02 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 103.3 |
| 6e1412af-33d1-3ae4-a03b-a45d2521454f | -8.4671 | -54.7035 | 2026-09-02 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 55da02c1-4a92-3665-a9cf-57b3f346595d | -10.7962 | -44.7669 | 2026-09-02 02:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 103.8 |
| b6ebea46-5be5-3861-b6ef-b470a06301f8 | -8.4296 | -54.7262 | 2026-09-02 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 956f217b-0c1a-371a-9516-f271921074aa | -12.1516 | -47.0608 | 2026-09-02 02:10:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 129.3 |
| c2ca3063-2d1c-3c3d-9f3f-c0533a750973 | -8.4485 | -54.7048 | 2026-09-02 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 127.7 |
| 920494bd-b1d4-330a-b353-87fc58da18fd | -10.777 | -44.7695 | 2026-09-02 02:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 777f292e-bdb7-322a-850d-9b89e70fae92 | -13.9853 | -58.6919 | 2026-09-02 02:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 89b1b640-4dee-3901-bfbd-77ab844f54a7 | -11.3521 | -50.6373 | 2026-09-02 02:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 97.6 |
| a1055662-d67d-3bea-8c88-88cc50a4088b | -8.5728 | -63.1807 | 2026-09-02 02:10:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 75383692-3272-3030-aea6-26b67381a02d | -12.1312 | -47.1309 | 2026-09-02 02:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| b81a1c47-642c-3d66-a4de-bfeb540d029a | -10.9 | -45.35 | 2026-09-02 02:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| efa87a52-4ade-3a42-a4c4-0cce4d74c1d9 | -8.4485 | -54.7048 | 2026-09-02 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 108.4 |


[Clique aqui para ver as próximas entradas](README12.md)
