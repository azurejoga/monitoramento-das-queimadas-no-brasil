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

## Dados Diários - Página 129

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1a7a628a-07c8-3fe0-ac5f-f585387fe2e7 | -17.782 | -53.81675 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 448eab52-ffb4-338a-b928-26c578d9c1e7 | -17.78136 | -53.82199 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9ba41372-dfdb-3732-b42a-58454b0058eb | -17.78038 | -53.79246 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8cb45508-a07a-3660-97db-4cc53761bd98 | -17.77982 | -53.79734 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| db72f650-925f-3776-8b0f-5710ff78e95c | -17.77925 | -53.80231 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4a206bcf-e9b2-3b02-a582-46ee4de7b3e3 | -17.77868 | -53.80727 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 43ce8a2e-de5d-3f34-93f9-991d9e1f3e76 | -17.77811 | -53.81223 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0eb7b2a3-13f9-3ff5-83ad-ce5ba157fbed | -17.77752 | -53.8174 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 462d7c43-4e83-3896-af97-f91e55b51727 | -17.77621 | -53.7866 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 224ade38-136a-3aa2-9e13-8f454a4ac79b | -17.77564 | -53.79164 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3b9281b8-8748-30ea-96fa-e6349c677f07 | -17.77506 | -53.79666 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 95a5569a-3761-3d60-ab7c-11dae09869ca | -17.7745 | -53.80158 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 83c977a5-b93c-39cf-a07d-803eef2e6874 | -17.77208 | -53.78042 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6689402f-3e25-34e0-acc1-190e3353d5b6 | -17.77149 | -53.78559 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| cbc2b84f-f79a-3787-b5d4-8043599da539 | -17.77089 | -53.79086 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9fabccc5-b890-36c0-b3e8-a94ee00c2b02 | -18.87559 | -54.57331 | 2024-10-07 05:21:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9190cb38-b22e-335c-b59e-672dc6b2df20 | -18.89275 | -54.54628 | 2024-10-07 05:21:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 945d9141-3ba0-347d-b3f2-47e3bc05d1fd | -18.89223 | -54.55067 | 2024-10-07 05:21:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 26b957d9-67c3-3efc-8b5a-8e6683153621 | -18.8917 | -54.5552 | 2024-10-07 05:21:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1565f84d-eaf2-374f-bce7-acf71c6ae9fa | -18.89112 | -54.56013 | 2024-10-07 05:21:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7950a882-7d6d-309c-b9ac-45f9c698cb88 | -18.8905 | -54.56547 | 2024-10-07 05:21:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 567c3f51-e2a7-3702-90f6-4a7224f1bb89 | -18.88986 | -54.57091 | 2024-10-07 05:21:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5f9b823b-912e-3019-a897-47172a72fdb9 | -18.88592 | -54.56474 | 2024-10-07 05:21:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ce801dbc-0782-38a2-9600-0c9a70f9ad6e | -18.88529 | -54.57008 | 2024-10-07 05:21:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8b88dca8-3625-3d7d-90a4-5317a0215678 | -18.88071 | -54.56939 | 2024-10-07 05:21:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e3b12bd5-edcf-3b84-9992-9873453c877f | -18.88015 | -54.5742 | 2024-10-07 05:21:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 614d76df-c559-37db-8e8b-15640646d589 | -18.8767 | -54.56373 | 2024-10-07 05:21:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8113aa88-fced-3236-9cda-42b223842d5a | -18.87613 | -54.56858 | 2024-10-07 05:21:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 94565020-3117-3e60-b27e-587ecb0ab125 | -18.87272 | -54.55774 | 2024-10-07 05:21:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b6c7a809-782e-30e1-8964-11a0613e92c7 | -18.8721 | -54.56318 | 2024-10-07 05:21:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ebe26ebf-5927-3f1d-9167-86c52a6ff7d4 | -18.87156 | -54.56781 | 2024-10-07 05:21:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 67ace51a-f554-3850-a3b8-bfce545c3a0c | -18.87103 | -54.57236 | 2024-10-07 05:21:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ad0ce826-8990-35c7-bef0-682320c7e1fd | -18.86815 | -54.55686 | 2024-10-07 05:21:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a7c1f187-09c0-3884-9c42-22e637123c13 | -18.86755 | -54.56214 | 2024-10-07 05:21:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8aceb576-d7fd-3c42-9d3d-fe7e158104f3 | -18.867 | -54.56683 | 2024-10-07 05:21:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0886d45e-74d8-36b1-a466-4fea8566a8c7 | -18.86438 | -54.5584 | 2024-10-07 05:21:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 6.6 |
| fb0b3eba-aaf6-35d5-aa42-9c42724c15aa | -18.86378 | -54.56331 | 2024-10-07 05:21:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 000552be-a1e5-3835-a270-6e2a31b4dd6b | -18.86359 | -54.55595 | 2024-10-07 05:21:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 45d7786c-8969-32c7-a33a-4c0fb17ce327 | -18.86302 | -54.5609 | 2024-10-07 05:21:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fbb1492b-de46-3a4a-8ad6-8db6b5f77e83 | -18.86246 | -54.56576 | 2024-10-07 05:21:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 89267e90-3bdc-3190-9bf4-4d090243d9e0 | -18.85921 | -54.56249 | 2024-10-07 05:21:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cb163b29-3ddb-3ec5-8d61-10bf977e44d2 | -18.85861 | -54.5674 | 2024-10-07 05:21:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b44479c2-1aa7-3a77-8f0e-ca1364c7934b | -18.85787 | -54.56507 | 2024-10-07 05:21:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e005b3fc-28c2-370f-a585-d3c82f0129d4 | -18.85462 | -54.56186 | 2024-10-07 05:21:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9efc82eb-aabf-3002-9213-006635296138 | -18.85328 | -54.56445 | 2024-10-07 05:21:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 67bc09f8-0558-335a-808c-a9c2762d7726 | -18.84942 | -54.5662 | 2024-10-07 05:21:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4fa9a124-f07e-36ab-8843-a2f2a3d7fad7 | -18.84868 | -54.56382 | 2024-10-07 05:21:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9417d7dd-deec-3d07-ae80-dce03073c233 | -18.89838 | -54.5381 | 2024-10-07 05:21:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d1310a33-6b74-31c8-87d6-b5a18e1068a9 | -18.89505 | -54.48637 | 2024-10-07 05:21:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3b699ceb-6162-3865-9671-32960e93dde4 | -18.89382 | -54.53713 | 2024-10-07 05:21:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ff43ed09-228a-37d5-9312-e9f499b82a8b | -18.89327 | -54.54177 | 2024-10-07 05:21:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6ef3f4a1-819f-3018-9b3b-4431eb04956e | -18.89168 | -54.47493 | 2024-10-07 05:21:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 19a90655-a51f-36db-9042-1c07c06cf6c6 | -18.89108 | -54.48016 | 2024-10-07 05:21:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4ad186e1-3870-37b6-b5cc-1db131aa9440 | -18.89045 | -54.48554 | 2024-10-07 05:21:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8ca4596a-075d-3784-8437-33dabffff4d2 | -20.7825 | -54.82469 | 2024-10-07 05:21:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9cde2b97-7756-382d-9daf-691a141b1dc7 | -20.77842 | -54.81914 | 2024-10-07 05:21:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b639787f-01be-352c-afde-7eb262eeeb2c | -20.25466 | -54.78787 | 2024-10-07 05:21:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a556ce3b-aa25-3e5c-a736-d419f53677c1 | -20.2541 | -54.79282 | 2024-10-07 05:21:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 13.9 |
| d540e9af-cb42-38a5-a866-efd576eecb15 | -19.97964 | -55.46949 | 2024-10-07 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ad02360f-b64c-3452-a692-75331fa0055b | -19.55499 | -55.06958 | 2024-10-07 05:21:00 | NPP-375D | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 94efa317-af2f-381c-9612-48e4581b2332 | -19.55051 | -55.06883 | 2024-10-07 05:21:00 | NPP-375D | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2687dbb6-9a40-3877-96b0-44d48bdc4424 | -20.07532 | -54.53482 | 2024-10-07 05:21:00 | NPP-375D | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a71c675b-d97a-377f-a757-725022be8249 | -20.07067 | -54.53398 | 2024-10-07 05:21:00 | NPP-375D | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 76a5b017-200e-3cd3-8630-6eec7cf5782f | -20.07006 | -54.5393 | 2024-10-07 05:21:00 | NPP-375D | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 65faf319-61fb-35ef-8bc6-a1dc772d0f20 | -20.06602 | -54.53311 | 2024-10-07 05:21:00 | NPP-375D | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bbd15703-41e0-3f98-a8f6-463e8a3f29f7 | -21.36214 | -55.69517 | 2024-10-07 05:21:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 446a03c5-3828-37bb-b0e4-8147936c463d | -21.36163 | -55.69942 | 2024-10-07 05:21:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 83ba8674-6300-358b-8a46-1b42b8f2eaea | -21.33401 | -54.65124 | 2024-10-07 05:21:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 119a876d-0bbc-3313-ad1f-b7a38f84e34c | -21.3302 | -55.70005 | 2024-10-07 05:21:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 87678188-ca55-3272-b993-0dfd1392941d | -19.10906 | -57.47721 | 2024-10-07 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 3dba47d6-33a0-3f22-ad09-75079e5ce8ea | -21.41356 | -57.25192 | 2024-10-07 05:21:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b971b081-2356-3848-af93-6d48413d029b | -21.41287 | -57.22443 | 2024-10-07 05:21:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cfed253a-329c-3080-a9df-fbd008b1805c | -21.41223 | -57.25077 | 2024-10-07 05:21:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e4ccb5e0-8cfb-3fcd-910f-12649880e15a | -21.41216 | -57.23027 | 2024-10-07 05:21:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 94705d88-0316-3554-ba37-702a6c9d7410 | -21.41157 | -57.2559 | 2024-10-07 05:21:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1b615135-b3c4-361b-a109-f0ae8e4df313 | -21.41098 | -57.22893 | 2024-10-07 05:21:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 83eccfb0-7f0e-36c3-96c5-000cc0bffb3e | -21.40953 | -57.25163 | 2024-10-07 05:21:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 14bd4f6a-4834-38b7-9ab4-a7fad32854f6 | -21.40889 | -57.25679 | 2024-10-07 05:21:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5dc7e8de-87fa-3064-aa69-97b4a2237092 | -21.40752 | -57.25565 | 2024-10-07 05:21:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c0fd17ce-1bb7-3226-97bb-3eacb6a93017 | -21.40549 | -57.25141 | 2024-10-07 05:21:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6bb916de-a8ce-312f-a7b0-70948df33324 | -21.40485 | -57.25653 | 2024-10-07 05:21:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a7d5b3a6-b608-394b-9628-4b28a0799e53 | -21.40413 | -57.2503 | 2024-10-07 05:21:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ff8a4214-cc93-3688-8e19-71471d0876a9 | -21.40347 | -57.25544 | 2024-10-07 05:21:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 72c9ce85-32c5-37a3-8278-bf79cebd524c | -17.73699 | -57.09238 | 2024-10-07 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 0506c34e-e6af-3bb8-bc53-54ee3a98ddf5 | -17.73514 | -57.07696 | 2024-10-07 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| beb5a261-60c4-3e26-a5d7-e067139b6759 | -17.73447 | -57.08191 | 2024-10-07 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 11a63b76-9637-3c43-a1e4-25206e55b694 | -17.73314 | -57.09181 | 2024-10-07 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 2739e235-b36a-3340-b255-78709d2b51d1 | -17.73247 | -57.09676 | 2024-10-07 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 9ad25349-da22-3d76-b293-067632d53234 | -17.73128 | -57.07638 | 2024-10-07 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| d77fb250-590a-3eac-80eb-69417d5bb740 | -17.73062 | -57.08134 | 2024-10-07 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| e5f57b8c-c85c-342c-89fd-3954d9e1be1b | -17.72995 | -57.08629 | 2024-10-07 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| cc2260ee-b08e-37ff-8934-a9157a3e2a55 | -17.72743 | -57.07581 | 2024-10-07 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| fc10c976-d07d-3f09-b1f5-51097101a647 | -17.72676 | -57.08076 | 2024-10-07 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 87d43115-0c00-3601-ac0b-6ec866560d54 | -17.7261 | -57.08572 | 2024-10-07 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| daf4a553-8379-36ea-bba0-40f1113155ae | -17.72543 | -57.09068 | 2024-10-07 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 029e4b08-9bec-334c-892a-7bb14defeeb1 | -17.72424 | -57.07027 | 2024-10-07 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 9a485fa2-538e-3b7c-a693-c8239f951f64 | -17.72357 | -57.07523 | 2024-10-07 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| df3b4361-1e94-3830-8fa8-b2e9c328ba49 | -17.72291 | -57.0802 | 2024-10-07 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| a255df52-5814-3c82-9046-e68d86bc021f | -17.72224 | -57.08515 | 2024-10-07 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| c2ed85ac-a766-35f4-9b52-b4daf67389f5 | -17.71972 | -57.07466 | 2024-10-07 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |


[Clique aqui para ver as próximas entradas](README130.md)
