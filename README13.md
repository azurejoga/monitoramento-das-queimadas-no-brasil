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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5d4e7ceb-b9e2-3d78-a4a3-f3efefc597d9 | -17.189 | -45.4644 | 2024-10-18 01:16:41 | GOES-16 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 18b41c27-f758-3e14-981a-0c7b3fdacffa | -17.0191 | -57.4768 | 2024-10-18 01:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.1 |
| 64cf99e0-b595-3dee-8d5f-5cfe205d9409 | -17.2177 | -57.3102 | 2024-10-18 01:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 112.5 |
| 8eee88f6-95ba-3a51-aa9a-677abe9ec135 | -17.2373 | -57.3079 | 2024-10-18 01:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 166.7 |
| 8e7a34e4-be98-3789-9cc9-cdbc32968b61 | -17.8246 | -57.4631 | 2024-10-18 01:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 94.0 |
| b1774f98-6db9-3b40-b740-5204f5dad995 | -17.8049 | -57.4655 | 2024-10-18 01:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 137.4 |
| b436a088-14ab-3a27-a90d-43100290ad08 | -17.7851 | -57.4679 | 2024-10-18 01:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.2 |
| c611c531-b86a-305d-bc9d-ee89811ef36b | -17.7855 | -57.4473 | 2024-10-18 01:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.5 |
| 4a85327f-17d9-3940-a163-1ead6c754aba | -18.1989 | -56.3608 | 2024-10-18 01:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.0 |
| e744a704-e117-344c-afdd-5103c112d362 | -18.1993 | -56.3399 | 2024-10-18 01:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.8 |
| a1a97c09-1834-38d8-9d5c-d343150133da | -18.1997 | -56.319 | 2024-10-18 01:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.1 |
| 00647234-2902-3928-bdec-ad613412aa8e | -18.2537 | -56.6237 | 2024-10-18 01:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 132.2 |
| 1fa0eb43-0fd7-3c90-8bbc-9dae61c648cf | -18.254 | -56.6029 | 2024-10-18 01:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.4 |
| 3342414b-ee87-3a4d-bc94-da9141f90b45 | -18.2735 | -56.6211 | 2024-10-18 01:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.4 |
| 604d05f3-cd95-3484-8cd9-9ee696b8c4d0 | -18.6575 | -57.3382 | 2024-10-18 01:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.5 |
| fe67e411-019e-3a07-bbb4-e4948e11dbf2 | -19.6013 | -56.9834 | 2024-10-18 01:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 191.0 |
| a0a6154d-992e-376c-871e-43e4ddd1cede | -19.6005 | -57.0253 | 2024-10-18 01:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 166.8 |
| 019c44ef-3994-301a-a22d-7f4889d42426 | -19.6009 | -57.0044 | 2024-10-18 01:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 330.8 |
| 6107365f-29be-364a-b7ab-516671018768 | -19.6213 | -56.9806 | 2024-10-18 01:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 106.9 |
| f2f86e9d-c484-3e48-8d9f-61babf0cc3e4 | -19.621 | -57.0016 | 2024-10-18 01:16:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 183.1 |
| 69ce7bc0-0d1e-3ed0-921e-3fdd83309870 | -19.6206 | -57.0225 | 2024-10-18 01:16:56 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 125.1 |
| b7580f89-f567-3d71-9d82-5de13b083e47 | -20.7911 | -50.7012 | 2024-10-18 01:17:01 | GOES-16 | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 71.3 |
| f14cee61-8a5f-3fcd-92ef-83a9a397243a | -21.9662 | -49.7186 | 2024-10-18 01:17:07 | GOES-16 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 130.4 |
| 27a76234-4bb5-3961-b381-2bc15988c8d5 | -1.6005 | -47.0922 | 2024-10-18 01:25:15 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| f20e799e-db1b-38e4-9fa3-2cc594d1b846 | -1.619 | -47.0919 | 2024-10-18 01:25:15 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| a8ceab56-2ec7-39ba-8902-f5d26e16f160 | -2.188 | -48.7248 | 2024-10-18 01:25:18 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 518fe27f-4583-369c-b498-61a1b7cb4f5c | -2.8795 | -51.6695 | 2024-10-18 01:25:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 9e2fc3f9-9fd9-3328-8f34-eda01728c201 | -3.1382 | -51.497 | 2024-10-18 01:25:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 116.4 |
| f0fe5812-1adc-3ce2-a55a-874998fbede4 | -3.1383 | -51.4763 | 2024-10-18 01:25:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 78dc0fba-a635-32c7-911d-9678ce43acea | -3.1566 | -51.4965 | 2024-10-18 01:25:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 81e6813a-8121-334b-b9d2-0e6e0ec17fd8 | -3.7009 | -45.9 | 2024-10-18 01:25:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 107.0 |
| 3f0f3462-9626-353c-a921-86a1bd640d72 | -3.8733 | -52.0715 | 2024-10-18 01:25:28 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 2f13c026-b387-358a-ba2b-e45c79712885 | -4.4072 | -45.9773 | 2024-10-18 01:25:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 280fdd76-0e58-3f19-b147-9b147835474c | -4.4258 | -45.9763 | 2024-10-18 01:25:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 154.3 |
| 41edb600-a2c3-31ce-875a-1c1d1a0c1573 | -4.426 | -45.954 | 2024-10-18 01:25:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 92.3 |
| bd175690-5abb-3c5f-9551-4707c950b070 | -4.4979 | -61.116 | 2024-10-18 01:25:32 | GOES-16 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 5871c9af-eca3-3492-94ae-1bea8a6d2c5f | -4.58 | -48.0132 | 2024-10-18 01:25:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 7c120885-59d8-30ba-a882-846fb8dd90ae | -6.6703 | -70.1174 | 2024-10-18 01:25:44 | GOES-16 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| ab7ae234-e709-30fc-a156-3da8a461dd39 | -6.6886 | -70.1171 | 2024-10-18 01:25:45 | GOES-16 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 63.8 |
| d942f726-d03e-34d5-813b-0db11c9f5192 | -9.7162 | -36.4319 | 2024-10-18 01:26:00 | GOES-16 | LIMOEIRO DE ANADIA | ALAGOAS | Brasil | 2704203 | 27 | 33 | nan | nan | nan | Mata Atlântica | 95.8 |
| 98d275f4-5863-3d59-873f-ec6ca28d2443 | -12.5155 | -63.2055 | 2024-10-18 01:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 018e0a1c-6bc0-384b-a95a-67f49205c2e4 | -12.4964 | -63.2258 | 2024-10-18 01:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 16f2b0fb-8fa1-330b-9272-c3a5727e889a | -12.4966 | -63.2066 | 2024-10-18 01:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 92.0 |
| fdb8c39d-30ce-3f14-ac1f-0b39dd2a8eec | -17.189 | -45.4644 | 2024-10-18 01:26:41 | GOES-16 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 9086efca-117d-35e4-82eb-5a6dca175b33 | -16.9992 | -57.4995 | 2024-10-18 01:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.8 |
| a8092a1b-acb4-30ac-8649-68f22044a2a8 | -17.0191 | -57.4768 | 2024-10-18 01:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.5 |
| 04e8a080-fe9e-321c-a12d-c910db84026e | -16.9995 | -57.4791 | 2024-10-18 01:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 77.3 |
| 2db39047-9cf6-308b-88cd-cb6f8eeaebb4 | -17.2373 | -57.3079 | 2024-10-18 01:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 148.5 |
| 11e37e82-f262-32b8-97d0-f4199ff22819 | -17.2177 | -57.3102 | 2024-10-18 01:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 118.0 |
| e5ae69b7-23b0-33f9-b105-119f1e1ea787 | -17.8407 | -40.0275 | 2024-10-18 01:26:44 | GOES-16 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 116.9 |
| 16763b47-e6fb-3d1a-bad8-9c800b4558d4 | -17.8415 | -40.0014 | 2024-10-18 01:26:44 | GOES-16 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 116.6 |
| 7c3e9fae-20ba-34d4-a85c-0d4782bb36b8 | -17.8246 | -57.4631 | 2024-10-18 01:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 94.4 |
| 49768ee1-4d01-3a19-abea-428f192fd439 | -17.8049 | -57.4655 | 2024-10-18 01:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 112.7 |
| 71fc210b-fc6e-370a-a4c6-59377ba9be05 | -17.7858 | -57.4267 | 2024-10-18 01:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.6 |
| 78144539-c24d-390f-b7cd-5197f16c5b50 | -17.7855 | -57.4473 | 2024-10-18 01:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 102.5 |
| 3296e953-4994-3be1-afdf-030c85bacb70 | -17.7851 | -57.4679 | 2024-10-18 01:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.3 |
| 9da6cc3f-1f03-304f-9d85-0a16c943dc05 | -18.254 | -56.6029 | 2024-10-18 01:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.1 |
| 0fd552a9-57d6-38fa-9cdb-6a7057be8530 | -18.2537 | -56.6237 | 2024-10-18 01:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 182.2 |
| 3d4ad32c-f3a8-36a5-be94-52118cf62966 | -19.3675 | -41.6001 | 2024-10-18 01:26:52 | GOES-16 | ALVARENGA | MINAS GERAIS | Brasil | 3102209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 92.8 |
| 6807a2df-8ff4-3c6d-9c2a-a9a2544506bb | -21.9662 | -49.7186 | 2024-10-18 01:27:07 | GOES-16 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 118.9 |
| fcffbb0b-6e53-3c3e-8492-9421ad14f727 | -23.3701 | -47.3747 | 2024-10-18 01:27:14 | GOES-16 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 100.9 |
| 77f008c1-51bc-3a80-aa7e-b040926a402a | -1.619 | -47.0919 | 2024-10-18 01:35:15 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 2cd2c7cd-27e2-36c5-b4a6-a6d455efd537 | -1.6191 | -47.07 | 2024-10-18 01:35:15 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 05692b09-0d08-340e-a8f7-63ee450881a3 | -2.188 | -48.7248 | 2024-10-18 01:35:18 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| a2db7611-55a3-329a-92f1-0b6eadf5979e | -2.8795 | -51.6695 | 2024-10-18 01:35:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 367b27b3-c2e9-3334-bb7c-88da869034cf | -23.3529 | -47.3536 | 2024-10-18 01:35:23 | METOP-B | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 08c1033d-fc77-3cfa-ab41-f03f1bc7098b | -3.1382 | -51.497 | 2024-10-18 01:35:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 6cfb16ee-2d95-3969-9192-4f7f91c632d6 | -3.1566 | -51.4965 | 2024-10-18 01:35:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |
| adc5843d-0b11-3c07-9c6e-5ef0303dd234 | -3.7009 | -45.9 | 2024-10-18 01:35:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 0232281a-8a22-3ce3-9c40-9e2f7f0cfc9c | -4.4072 | -45.9773 | 2024-10-18 01:35:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 66.9 |
| e411e914-c048-3e9d-bea6-8ea6a067cd4e | -4.4258 | -45.9763 | 2024-10-18 01:35:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 166.2 |
| afeaad51-0a8c-3632-9f46-714aebab53be | -4.426 | -45.954 | 2024-10-18 01:35:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 31e471e8-6520-3802-844a-c49c518691bd | -4.5162 | -61.1156 | 2024-10-18 01:35:32 | GOES-16 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 50c6fdc0-d393-37ff-9009-021978afcfcf | -5.5716 | -44.8927 | 2024-10-18 01:35:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 79fc77a8-66ab-35ee-acb0-4aaa16d8cd19 | -6.6703 | -70.1174 | 2024-10-18 01:35:44 | GOES-16 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| aec5bff4-d0da-37bf-aa8c-456904f19977 | -6.6886 | -70.1171 | 2024-10-18 01:35:45 | GOES-16 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| d490e473-ea4a-356d-acdf-fca0267b0978 | -21.952499 | -49.6982 | 2024-10-18 01:35:56 | METOP-B | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9b177624-5092-3d4d-88e6-8d0b262d115b | -21.9606 | -49.7257 | 2024-10-18 01:35:56 | METOP-B | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3e5553e6-0ddb-3f9f-a688-d44b1a12c70d | -21.943001 | -49.7015 | 2024-10-18 01:35:57 | METOP-B | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 46f6e3b2-8e2b-30e8-baaa-0b0bc33caeb6 | -21.951099 | -49.728901 | 2024-10-18 01:35:57 | METOP-B | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 36b9c295-8d05-39c7-8f0d-c60ff27f9622 | -12.4966 | -63.2066 | 2024-10-18 01:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 94.2 |
| cb87cfaa-b849-3b71-8e11-db388120fe76 | -12.4967 | -63.1874 | 2024-10-18 01:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 4df92bad-9e39-3ecf-a568-8fc8ed23e90d | -12.5155 | -63.2055 | 2024-10-18 01:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 956f2c68-e518-3ca7-b188-41d27d63561e | -17.0191 | -57.4768 | 2024-10-18 01:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 93.0 |
| 58261d5b-38dc-3a40-b834-1594e543db7f | -17.2177 | -57.3102 | 2024-10-18 01:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 95.8 |
| d6790341-2d9a-3baf-8988-c1c3515b09ac | -17.2373 | -57.3079 | 2024-10-18 01:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 171.9 |
| 6d820137-6a4d-3015-b8b4-b6e028d7df36 | -17.7855 | -57.4473 | 2024-10-18 01:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 107.9 |
| 62349f7a-a310-3e3a-af4e-ebd22f59aea6 | -17.7858 | -57.4267 | 2024-10-18 01:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.3 |
| c5da57ee-dde0-36a4-b1c9-df21f3933dc9 | -17.8049 | -57.4655 | 2024-10-18 01:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 121.5 |
| d687296b-572e-32a9-8b43-9d6965193f56 | -17.8246 | -57.4631 | 2024-10-18 01:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.1 |
| 0cd74ab1-11c4-3025-afd0-c848639e0490 | -18.2533 | -56.6446 | 2024-10-18 01:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.9 |
| fa9e2190-effc-37ee-addf-f12e8554fc93 | -18.2537 | -56.6237 | 2024-10-18 01:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 198.1 |
| 3e282146-c2f5-3d2e-850f-910beb480847 | -18.254 | -56.6029 | 2024-10-18 01:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.6 |
| c9949d0e-dc25-325c-bcb5-e48170b71347 | -18.2735 | -56.6211 | 2024-10-18 01:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 124.3 |
| 978cc97b-fb8e-387c-a7ff-4b56e0e81af7 | -19.628901 | -56.927299 | 2024-10-18 01:37:05 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6fd9b181-749e-3b66-a729-c568c5bc42ac | -19.613899 | -56.908501 | 2024-10-18 01:37:05 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7860b133-dbdb-3775-8959-2288b061deb7 | -19.6166 | -56.9193 | 2024-10-18 01:37:05 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 54ad2c72-73e3-3c47-9bb9-44e91dcc248a | -19.610399 | -56.9781 | 2024-10-18 01:37:05 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| da7e8761-1f9a-315d-be99-31a175320a88 | -19.613001 | -56.9888 | 2024-10-18 01:37:05 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 94e7b62d-5d94-3d52-9e1f-855aa501dbdb | -19.615601 | -56.999401 | 2024-10-18 01:37:05 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README14.md)
