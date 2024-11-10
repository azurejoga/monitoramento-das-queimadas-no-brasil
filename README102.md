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

## Dados Diários - Página 102

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b11820dc-993d-3876-a5a4-42542482679e | -4.34873 | -45.63279 | 2024-11-10 04:38:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa9a780e-8667-349e-9e71-09878c9867f2 | -3.24294 | -50.3095 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 09587fb2-5e51-3a8e-8db3-3591a8ac4fea | -3.25612 | -48.74582 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 87dd423f-82fa-3a23-aee1-b78f0d0c6eef | -2.71268 | -49.33542 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 215d3541-1c01-3a79-8048-a72863fbd9de | -2.71973 | -49.18289 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87b77b49-c958-33ae-980b-8721c7cc902f | -3.72561 | -52.40623 | 2024-11-10 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 874af56f-53eb-32bf-a95b-2f6cce4b4273 | -2.71609 | -47.98267 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fd469342-69a2-3d6e-ba26-4f8074eb65ab | -2.89722 | -46.82436 | 2024-11-10 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a6cc1eb-2bb6-302d-8b21-ec7016eb3415 | -3.10502 | -53.3242 | 2024-11-10 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7c958e77-01a0-32a0-9f57-c8c3c2ad72dc | -5.41492 | -46.41701 | 2024-11-10 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 216e81e3-8975-328e-8dbf-8b0f119bed6a | -4.4135 | -43.64278 | 2024-11-10 04:38:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e993366e-36de-3881-b8de-801861f77d7a | -2.05098 | -52.08278 | 2024-11-10 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5de4995e-63f9-3af2-b315-724e5b7defb2 | -3.01548 | -51.04163 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6d1677af-c2c8-37f7-ad3f-b4ec1ace7592 | -4.20728 | -48.54865 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 140cba99-4884-344a-9d18-8c7ea1e50ee6 | -3.24334 | -51.23921 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 82323f14-230b-388d-b55f-0975ce407c56 | -3.81377 | -50.78381 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e535b031-1a2a-37bd-b694-f4c159b75ec5 | -3.70337 | -47.63812 | 2024-11-10 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 45a4917a-1134-3aca-9b5c-c9628285b4bd | -2.42572 | -50.41798 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 48e15544-2892-3434-a2f8-fd163053db08 | -3.02358 | -48.11609 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2538907b-4ae6-3f32-ab57-77ec3b4b8cb2 | -3.95762 | -48.99767 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df181702-9b8b-32b8-a14b-f17836cfa22e | -6.27532 | -44.7403 | 2024-11-10 04:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9c55d47b-8962-3a82-8375-251db262a0a7 | -3.5412 | -43.55621 | 2024-11-10 04:38:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9fe0183d-9a37-3cd7-a0b1-d6d05b5b4752 | -4.85032 | -48.48618 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 866bb781-600f-351f-9bb2-84b83235c463 | -4.07777 | -48.2766 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a6b508b2-7c22-35ce-a3e3-bf76b2cd8cc2 | -6.67444 | -43.53809 | 2024-11-10 04:38:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d407f1e4-5c3e-3bd8-be03-5796d5276ddc | -4.09884 | -49.13296 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 04ecc807-8924-38f2-8af0-fdfc115f11df | -3.09414 | -51.11301 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a4c26802-bc8d-336a-8a30-20fe80f9d670 | -8.38423 | -44.10992 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e4bbf4e1-682a-3e69-a952-0b8cfc48b22b | -4.20991 | -48.68353 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 596d858e-fb99-35d2-a79d-9a357824adc9 | -4.93655 | -45.56581 | 2024-11-10 04:38:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c549ab68-1417-38d2-84d6-9874a3948d48 | -2.61455 | -48.20089 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0dbd9d27-9892-377f-84c8-678c953ad135 | -3.61271 | -48.92908 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 015063ac-080c-3441-a532-672e4040f3bb | -2.84504 | -49.22803 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ffda1b1e-281d-3565-8dcd-278e51bee5e9 | -2.4144 | -50.48899 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 47338220-82c1-307a-ae16-1c9d5af00fb1 | -3.15296 | -50.6326 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| df18866d-71ba-37cd-91f1-360be4c29d85 | -2.94299 | -48.71497 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 171eedc6-0887-3134-9317-cf604c1cd626 | -7.39979 | -43.60522 | 2024-11-10 04:38:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b98ed082-6bdc-318b-ab67-2ef450a44614 | -3.66295 | -50.25905 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54fbf564-f68e-3487-8828-6c609bf1116d | -2.6773 | -48.63779 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 07e9d67b-f575-386b-b342-330f73c4f769 | -5.18014 | -46.18789 | 2024-11-10 04:38:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c1c94413-ba3c-3c55-a44d-6f73ef3165c6 | -2.93824 | -49.14986 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 237b2e35-02ae-3c32-a105-9bf3108e13e2 | -2.33395 | -50.58094 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8bfd10b7-3326-3938-bcf0-788bc0a04502 | -2.8097 | -49.87217 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e0ab9db-b1ae-3e0b-a9fd-831fc9b3a435 | -3.55726 | -50.33218 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 202225b7-a760-37c0-9510-32f5f46bde1d | -2.25497 | -50.41923 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0abf3c26-b7f9-3536-b860-3d06e4d415b6 | -3.54065 | -43.55983 | 2024-11-10 04:38:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 107e80ca-8936-3fbe-8b11-81ae66fc18d1 | -3.027 | -47.96395 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77a615f5-7102-3213-8889-3b92d38dc5ec | -5.41795 | -47.69984 | 2024-11-10 04:38:00 | NPP-375D | PRAIA NORTE | TOCANTINS | Brasil | 1718303 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4dbf3012-fbea-3e87-b811-7ea283e1014b | -1.66543 | -53.80807 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 043ec7b6-31d0-3d32-8420-dd888463725a | -3.96934 | -48.18859 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9ab2dc6d-4fc1-3e9d-80e4-295688bd4c78 | -2.88295 | -48.29889 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f11d873e-b17a-3b97-b7dc-22045d098d34 | -2.94721 | -45.46452 | 2024-11-10 04:38:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 776afa51-7aea-3bdd-ac6b-0b6591c3f143 | -2.60568 | -48.19245 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ac3f2f4c-bdbe-3456-9d8d-3bffad64fb39 | -2.52831 | -48.2087 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6fe8e0b9-bcd2-35c7-a678-52a96e62f0d6 | -4.0173 | -48.29559 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 196539da-4303-30ab-ab81-ed6d00160908 | -2.71307 | -49.18185 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a56355bf-b35b-39e1-a5c9-239805ef1b88 | -4.42865 | -47.2573 | 2024-11-10 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc1b2b15-06bf-3df1-895b-194875ffdf93 | -3.78984 | -47.45871 | 2024-11-10 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1ddb882d-52b5-30e8-b7ff-aadb65bbc85f | -2.66523 | -49.89719 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 99cf59a4-f1ae-3cf8-a6e9-a1380117fd6f | -3.97709 | -48.18266 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9a4632be-b32b-3768-9615-b0c96bf57cd1 | -4.60738 | -45.96903 | 2024-11-10 04:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d11bbf52-7d7d-3bd5-bece-bb69fab75a66 | -2.14013 | -50.80642 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5cacc402-95b8-36db-9ade-25fd70eaad03 | -4.31246 | -48.65396 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a0faf90-ecd1-3f33-9671-e3dca3be2a2f | -3.47822 | -48.24006 | 2024-11-10 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 03f49c43-322d-3815-97dd-88dde476a9f6 | -4.60257 | -49.49682 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4dc85bda-7702-3523-878a-8f8a17b25ae7 | -3.6366 | -50.18458 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae6bb3e0-8a23-391a-aced-21722bb95b24 | -2.81549 | -48.46852 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68705995-3c51-35e9-808f-47677909e776 | -3.9149 | -47.95536 | 2024-11-10 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7bad389c-12c6-321b-af4b-a84be9c76ab4 | -3.22203 | -53.06359 | 2024-11-10 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 934c5fd2-402a-33dc-bc1f-6d50def072de | -3.10218 | -49.41784 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e6debba6-5cbf-31a0-bdf4-f46101d6e71e | -2.15596 | -50.50754 | 2024-11-10 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e2d92e4-b152-3946-8eda-4d512161fb01 | -1.48939 | -55.43357 | 2024-11-10 04:38:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| abbc2892-7175-312c-9212-9bca1f30175d | -4.34445 | -48.62354 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76bd4825-27b0-32df-a2b9-8a19ffde24a5 | -3.27079 | -50.35466 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a4223c45-338d-32c8-8177-257d1dacf879 | -3.0994 | -49.41382 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 315c9aa3-2a79-3cde-93d1-c20a992130dd | -2.71821 | -49.30049 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 27376235-80d0-3049-8d15-e05ddd838fa2 | -4.68409 | -45.14591 | 2024-11-10 04:38:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1a55d769-5e73-3c1c-83b6-16b81a471f71 | -2.38758 | -54.09274 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be582288-7dba-397a-b6bf-14418fd633a9 | -2.68062 | -48.63831 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 583bca11-7ec6-30d4-9900-0e0d4d89c2fe | -3.26077 | -53.70322 | 2024-11-10 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d3eb5397-c4cf-3df4-960e-7323627b161e | -4.68012 | -48.77458 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 72caead4-7dbb-3711-9fb5-4d72d28ced33 | -3.54464 | -49.9757 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0f2a821f-12da-3a86-8c1b-9da8bad916b2 | -3.34897 | -50.25856 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a3dd30ab-cabd-31ad-a9ab-7768766e8e69 | -2.58196 | -48.2135 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 013b1b9e-070d-33cf-a9ea-92ebabb3c647 | -3.96262 | -48.16615 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3f37745f-ec1c-3fc6-a178-60eaace86eaf | -2.23779 | -53.78877 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 86cd31d1-85be-32b0-ab6e-e07a4015d069 | -4.94022 | -45.5664 | 2024-11-10 04:38:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 63ef46b2-ee46-34bb-a7bb-0520523d6634 | -2.75024 | -49.16272 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0daafb3d-af42-3ee4-8f85-871c4d23205b | -3.2498 | -46.43975 | 2024-11-10 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 86105e2e-f2a8-3e22-a2e2-429224d3264a | -2.379 | -50.40718 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 11c3d447-1cdb-3cbf-bc90-b37abf4ef2f8 | -3.38819 | -51.46571 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 027272a6-3f41-3d1b-9b50-2166138b7e01 | -2.92128 | -49.36486 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7f2a488c-1f62-3623-a56c-c7dc0527ecf1 | -3.79546 | -47.46691 | 2024-11-10 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f22c0044-57ef-351e-810a-58ff123cf2ad | -2.08158 | -54.67862 | 2024-11-10 04:38:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6dc13c78-6ad8-35c0-8fd3-080dc1b7e931 | -2.20083 | -51.94224 | 2024-11-10 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 58e0f68b-888e-3231-9877-6ffca4e019e2 | -4.43204 | -47.25788 | 2024-11-10 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 78ebbc0e-28f3-3d97-95ff-497b794a4cf5 | -3.20585 | -50.63326 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5de5fe55-1939-3b99-9665-b769be844080 | -2.55255 | -51.2307 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3a79dd3f-da46-38d6-ae8e-c4eecfc30ab8 | -4.16375 | -48.24356 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c06b69e2-8db6-31e2-9650-e1c74711aa65 | -3.25666 | -48.74237 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |


[Clique aqui para ver as próximas entradas](README103.md)
