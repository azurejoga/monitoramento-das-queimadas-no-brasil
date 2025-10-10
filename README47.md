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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b1773f66-36c2-3586-9b46-e201dd55285f | -18.06072 | -57.55841 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 31de2517-1193-3733-8c38-7cd2b1731686 | -17.8448 | -57.65374 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| dc51c46e-f073-3f51-bd66-7b317364966d | -17.906 | -57.51683 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 5cdcc81a-1399-3ac9-bc0f-39749275a7b4 | -17.88577 | -57.66434 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| a5c1b794-a364-32a3-b21a-11db5a27e70e | -17.82166 | -57.659 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| ff261d32-0883-3d7f-9e72-01004e446355 | -17.8902 | -57.6602 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| d07f867a-1a4b-3d40-bcab-5592a2f90452 | -17.81914 | -57.64945 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 66a66fc0-7c82-3557-85ff-da37f3f8f3f1 | -17.89671 | -57.49934 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| a263dbba-f980-3e80-8c8e-2e79697dcfd7 | -17.829 | -57.65662 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| d23d98a2-4f23-3f18-8035-79f5166b2342 | -17.81981 | -57.64465 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 2aa53394-6b05-3fd3-9548-1f261983df8b | -17.90674 | -57.5114 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 007691bc-c70a-305b-a332-d217532f36a7 | -18.06967 | -57.54966 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 780574ff-2f7b-3f6b-aebe-c6ef490e15fc | -17.82504 | -57.63491 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 5298e316-ba19-36e5-a67c-6a349e69acb0 | -17.82272 | -57.62394 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 287ad4b9-8d77-3a2c-bc11-cd6856ecf6ec | -17.8378 | -57.64849 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| c0e6ab57-27a3-3da3-949f-30acc59a960c | -17.93401 | -57.62286 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 9629e02a-fb90-327b-bae2-4cec28961360 | -17.90121 | -57.49493 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 014f483e-0f25-3e21-9d53-93177f427bfa | -18.03845 | -57.56282 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| c3dc43b5-f4b3-3ebc-be2a-dee5afd15237 | -17.8328 | -57.65698 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 2f860762-03f4-32b7-b85d-27ad353c17e7 | -17.85124 | -57.60606 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 9e829257-36ae-3b47-aecf-6b5bae9d321d | -18.04227 | -57.56329 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 24a7ed7d-4465-3885-bfa7-c5e96f347ef0 | -18.06456 | -57.55876 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| fd31d611-fa01-3f2e-bf9d-d4df139ca8d9 | -17.82077 | -57.66055 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 6e35667f-fcae-36af-a5bf-76d8c75ae7b5 | -17.90977 | -57.51764 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 850dfe9a-4ffb-344f-b93a-63011a1fb7f9 | -17.82129 | -57.63416 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 7e3f3b64-ce04-36ca-9594-17cf29c7c358 | -18.03526 | -57.55779 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 4f4e1a5f-9c99-3be4-9af7-8dc01eaa6432 | -17.92262 | -57.62134 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| bf0c189a-821b-367e-945b-8eacdc5de80d | -18.04163 | -57.56796 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| d1c6a18a-8ee7-31ae-b13f-d89cc104a68a | -17.82994 | -57.65503 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| f4bcacc1-ae3a-32ef-84d2-bb1656d9324e | -18.03144 | -57.55732 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 2380f9b2-4673-3e16-962a-176a6968c9ae | -18.07351 | -57.54996 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| daef7ac9-9e9b-3183-91db-3896522a9f03 | -17.71585 | -56.78226 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 1f6595ef-3624-3404-9a80-4717b4fc05f4 | -17.90052 | -57.49996 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| dba86aa3-d034-3c5c-8d73-3f2207b09601 | -17.82839 | -57.66113 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 79dfc10d-41a3-37af-81b7-376866e37759 | -17.82458 | -57.66083 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 63a89d54-dfb9-31ff-86b3-fc711f73ad66 | -18.02879 | -57.54834 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 84c86f92-7e3d-35ba-a8b0-71ecf71a8a99 | -17.82222 | -57.6207 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 5c9d1bd0-79ae-33b8-b86b-308efad29fb7 | -17.90903 | -57.52308 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| c01be29c-ee40-303c-923b-967f8d78fac6 | -17.82579 | -57.62962 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 61f6e14f-33a4-359c-b2b7-91e51b11cf8a | -17.84121 | -57.59431 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| b9e0c659-1d27-391f-b933-21eb72b4a672 | -17.8889 | -57.66966 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 7a9f910b-7c23-3542-8b16-a988b53cafa0 | -17.88955 | -57.66494 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 77c12ae9-eec3-3d3b-a5fc-aaa6d09c4ebc | -17.82106 | -57.66334 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| adaf0fb9-2cee-3ee7-b4cc-359831726ddb | -17.89911 | -57.51034 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 0b3ecac8-61d2-3a82-a49e-e9e3cb4320e2 | -17.82931 | -57.6595 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 26c2a506-7e22-3d0b-9cf0-f266fbd8cabd | -18.05432 | -57.56052 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| f713bae7-4f21-3aa4-a123-a3b406afbe8e | -18.02761 | -57.5569 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 90b83d9c-828f-3b61-858b-5525db6bfdd8 | -18.06643 | -57.54476 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| ce2a5346-73fe-3ce2-a835-57fc5e810031 | -17.90364 | -57.50562 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| fbe90c2b-0e27-392f-b187-bea37f0f980c | -17.81787 | -57.65858 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 55d58655-a4cb-3cfe-8c63-32424ca08ca8 | -17.71742 | -56.78364 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 443efa87-fac9-3f06-a836-71501296fdcb | -17.8334 | -57.65251 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| ed7dda6c-4d3b-3a46-875d-e6ec33a195df | -17.8507 | -57.58125 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| d943e816-b6ca-3797-9693-a692756f2c3c | -17.89776 | -57.66135 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| fdd6d8db-e6d2-3abb-a7c4-9f3310d87542 | -17.84101 | -57.65329 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 6d677001-705e-30c8-aa02-430ade90325b | -17.90433 | -57.50053 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 041f904a-fb5d-31de-ab73-bb1fd5ed1f84 | -17.88775 | -57.50806 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| c2f06dd4-1e38-39bb-9989-b6359e48659d | -17.9022 | -57.51617 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| c7b46c59-f5a5-3be0-9245-3fad44260a53 | -18.03464 | -57.56234 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 04f11716-6aa9-385e-b3ca-ef48099f105e | -17.89332 | -57.66552 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 3d83f990-d50e-39de-89bb-1b0eabd0154b | -17.89528 | -57.50986 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 540f9ba7-be19-31d5-be0a-78bf282571d5 | -17.84628 | -57.58532 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| a29bf09c-a7ad-30a3-932c-8f423212be62 | -18.02821 | -57.55255 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| e1942015-5e4b-3e64-9d9c-70ec82190742 | -17.89152 | -57.50896 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 524bc3d7-1270-3005-b355-23cadc8edcd1 | -17.89267 | -57.67027 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 63d3c6b2-ed5c-3528-9ecd-0995ef1ad5f7 | -17.8486 | -57.65418 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| d03fa950-e890-3d69-9e0a-8d34914612ae | -17.84186 | -57.58949 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 5937cc30-78b6-3b6c-9b93-9e770ca615aa | -17.84694 | -57.58047 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| f7f4efe0-7b0e-3a7d-992c-3e9f118d85dc | -18.05816 | -57.56088 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 728a0d62-7dbf-35af-bb78-4909a1b3e978 | -18.03907 | -57.55838 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 1d3b0b0e-1c3a-317e-86e1-ec725fa246a2 | -18.06579 | -57.54956 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| bfabaf16-7add-36f7-8b3f-d45d352e5a54 | -17.90532 | -57.66242 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 62da337f-09f2-3eae-80ea-44e111440ec7 | -17.84161 | -57.64884 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| d8bd4dc2-f20d-381c-b09b-c32cc689d288 | -17.89602 | -57.50442 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 9fc0bbcb-be1c-3614-8f5e-4e5bff19fe61 | -17.8971 | -57.66608 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 37bd5f25-b72f-317d-83d2-e9000157a779 | -18.0326 | -57.54882 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 23b684b6-d88b-3a9d-90ec-f42d8779fd23 | -17.82549 | -57.65926 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| ae637fd2-9f24-3ef5-819b-3a8c6cb60c30 | -19.58638 | -54.02818 | 2025-10-10 05:25:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1b4736a9-ae59-325d-9d7d-281b06b64e9d | -18.06841 | -57.55904 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| e0c8e4e0-3aa4-3617-bb75-389efa1c333c | -17.82611 | -57.65482 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 2349b6b4-31cb-31da-a918-a3e59741ad72 | -17.81884 | -57.64622 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 50257029-f71c-361c-8bf3-76ea8b2a24c5 | -17.82467 | -57.63136 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 3a374dca-802c-38fb-acc8-5e996ce67b33 | -18.06256 | -57.54468 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| ab19bee8-286b-3d24-bf9f-dafdb5e3695a | -17.93371 | -57.62051 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| b3357288-5744-3d36-889a-99bdab68535b | -17.90219 | -57.65718 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| bdaca01a-d79f-3710-af89-a74747ad3d30 | -17.92991 | -57.62 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| cee4c15e-a339-32ca-8040-429b2a8150a9 | -17.82534 | -57.62626 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 335b360b-1378-3b4d-97c0-b93e53a080b7 | -18.06902 | -57.55449 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 8fcd5c0c-030e-37a9-a48e-579542f1495c | -17.85238 | -57.65467 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 37a85c48-ce0d-3ec5-9721-c8cbf8dfe466 | -17.89645 | -57.67084 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 71dda3d9-f024-3775-8940-a6d2a0da4064 | -19.587 | -54.02259 | 2025-10-10 05:25:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fff4269c-182f-3ed7-9668-fe981cdff069 | -17.84563 | -57.59018 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| b3aa57a7-0d8f-33b9-a6b5-d116894bc0f1 | -17.90154 | -57.6619 | 2025-10-10 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 0fa215b0-4b8d-3c8c-be21-429062549a5b | -2.1853 | -54.48003 | 2025-10-10 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3972fe48-cb3d-3ebb-b270-01b9abf6ee64 | -2.19086 | -54.48083 | 2025-10-10 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9339f3ca-6bbe-3a94-80bc-db9ba3898ae2 | -2.1903 | -54.48446 | 2025-10-10 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a09efc7c-e992-3e94-9833-e1efc5ededf0 | -9.64426 | -66.94125 | 2025-10-10 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd2c5dbe-1532-344a-b690-64320ee7e58a | -9.63976 | -67.39539 | 2025-10-10 05:42:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 917eb6e5-3ba3-35fa-971a-78074b8e3b3e | -10.49579 | -69.13624 | 2025-10-10 05:42:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d086aa87-3c2f-3aa8-824c-13dac167e3d4 | -9.95048 | -66.77279 | 2025-10-10 05:42:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README48.md)
