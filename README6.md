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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6246afe0-4778-3342-b2ff-83325026365b | -7.78633 | -46.99641 | 2025-09-28 00:52:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 2bb59574-d63f-34fe-97af-05070a5179c5 | -11.95667 | -47.91141 | 2025-09-28 00:52:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 612adc49-80d6-38c9-8f30-6af9841770ad | -13.61236 | -48.08937 | 2025-09-28 00:52:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 2268d376-ff3a-345a-8b95-9d2581d80317 | -14.38408 | -54.93549 | 2025-09-28 00:52:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| b4408e47-2a1f-366f-b2d0-cfd4cddaa77c | -12.94198 | -45.10574 | 2025-09-28 00:52:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 06284d5e-c5a5-3f1b-aeee-07b1d72b5aaf | -9.04215 | -46.72189 | 2025-09-28 00:52:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 22cc43f1-10e6-3a6f-bc69-8153464f498c | -11.99221 | -47.05695 | 2025-09-28 00:52:00 | TERRA_M-M | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 84b170fe-fa5c-3408-9b97-4d4c279bba8f | -7.73846 | -49.32663 | 2025-09-28 00:52:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 6b2df6e8-60d1-3f8f-a22b-0824bdd2c259 | -10.76961 | -49.03415 | 2025-09-28 00:52:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| c636e841-cb42-3b3d-bd4a-5bca217496c6 | -7.73634 | -49.31264 | 2025-09-28 00:52:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| acadc3aa-3ed4-3a86-88d3-e0c486d8a199 | -8.49106 | -47.82693 | 2025-09-28 00:52:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 18fe8da9-ae29-31a3-b748-bf0dc458db29 | -13.71701 | -48.33755 | 2025-09-28 00:52:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 6ea063f3-43ae-37a9-9a5f-4a0b00d43e85 | -10.79178 | -49.58844 | 2025-09-28 00:52:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 8c6d6e58-53a1-39a9-808b-b8d1e820a579 | -12.94611 | -45.12958 | 2025-09-28 00:52:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 4e573e6f-b44f-3a56-a0a0-fb4d49acfe7f | -13.59042 | -47.3124 | 2025-09-28 00:52:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 38.1 |
| 3eebf33c-0fd8-3af3-818f-1fac621acb08 | -12.22892 | -60.83714 | 2025-09-28 00:52:00 | TERRA_M-M | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 20.4 |
| d5acd402-e159-37b4-9f03-0215967b0464 | -10.97185 | -49.56582 | 2025-09-28 00:52:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 1ddfc75e-06ae-3f8d-85d0-220c3ae9912a | -11.94783 | -47.92841 | 2025-09-28 00:52:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 9f988fae-6bd9-3df3-9c4f-1256dd8d4eaf | -7.84795 | -43.78978 | 2025-09-28 00:52:00 | TERRA_M-M | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 45.4 |
| 3aa68ba1-302f-392d-a548-f40901bfefa9 | -10.54268 | -43.6235 | 2025-09-28 00:52:00 | TERRA_M-M | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 51.9 |
| af33cd1e-ca94-3187-b16d-2267301a5b91 | -11.38865 | -46.9786 | 2025-09-28 00:52:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 23.8 |
| a5eb3d9b-22e9-316f-a2cb-5dd161d6280d | -8.48062 | -47.80412 | 2025-09-28 00:52:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 54.8 |
| b6aa0cea-e41d-3243-bb12-c70c7c1021b0 | -11.86889 | -56.87722 | 2025-09-28 00:52:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 186066de-56ff-30f0-90a4-e9c59c18ad6b | -9.31503 | -48.94737 | 2025-09-28 00:52:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 97f53174-75ca-323b-a8d7-fd273a4c5f4f | -7.00696 | -45.63024 | 2025-09-28 00:52:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 23.5 |
| b3648ba5-dc7b-3e32-ab31-0aef6aa5de37 | -13.60949 | -48.09557 | 2025-09-28 00:52:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 32.3 |
| bf43a597-e26d-386a-af9b-6e7688f490d0 | -10.16612 | -49.38345 | 2025-09-28 00:52:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 3d8bdf43-9132-3f9f-a9a2-91631d6a5445 | -8.47632 | -47.81138 | 2025-09-28 00:52:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 81c10c11-2fe1-35c6-a39c-4f1381e037f2 | 0.27889 | -51.41048 | 2025-09-28 00:54:00 | TERRA_M-M | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 1e1c265d-157b-3a7b-841f-7af8fbc5127e | -3.7262 | -49.43451 | 2025-09-28 00:54:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 5a1b8998-d56f-370a-8d82-3c897e0ca986 | -5.04498 | -45.30857 | 2025-09-28 00:54:00 | TERRA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 36f0ae46-c7fb-3b13-9950-270a6f51971b | -4.95383 | -45.5621 | 2025-09-28 00:54:00 | TERRA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| ff894fa7-fdd9-32e6-85f1-f539894899ae | -3.79099 | -48.87186 | 2025-09-28 00:54:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 1a0ca10f-649f-3144-9e2b-0a98f7c20d89 | -3.74003 | -49.44859 | 2025-09-28 00:54:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 37.1 |
| b174e7aa-e267-3fe2-b23b-eccf0f318c3d | -4.71314 | -55.98466 | 2025-09-28 00:54:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c93e921b-2b9b-36cd-8410-2fd9338a042c | -4.79454 | -50.80231 | 2025-09-28 00:54:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| c68a667e-78ea-3ae8-a79a-5b8461b693a5 | -3.33681 | -50.25196 | 2025-09-28 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| cfbbba44-1c35-356f-95e3-a3eea156b755 | -4.85757 | -45.74072 | 2025-09-28 00:54:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 19.1 |
| f53d94d5-130c-38ed-9802-f39793b1ca9d | -3.80757 | -47.57989 | 2025-09-28 00:54:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 4a3e8682-347b-3697-9350-7e48b057adbe | -3.73775 | -49.43279 | 2025-09-28 00:54:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 12800cda-4918-3bce-9d1f-a38ba7920475 | -2.47227 | -47.66375 | 2025-09-28 00:54:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 30.3 |
| ad10c48f-b1bd-3dcc-a5d5-e5d4c4ed0746 | -6.50513 | -54.86833 | 2025-09-28 00:54:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 185cd4f1-3baf-3916-a388-09cde9d15b10 | -4.28925 | -48.25925 | 2025-09-28 00:54:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| c9affb29-8b64-3146-9497-29a6ee5f3c57 | -4.85944 | -45.76483 | 2025-09-28 00:54:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 2070e2db-33aa-3ac5-a109-11cba70eeb84 | -5.05091 | -45.31305 | 2025-09-28 00:54:00 | TERRA_M-M | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 46.2 |
| 479ed8c8-20fa-3bf6-809d-2944fac302eb | -4.79624 | -50.81437 | 2025-09-28 00:54:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0c338f00-5650-3e32-8aad-0fa587b9778a | -3.33006 | -50.26057 | 2025-09-28 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ed7c588f-e57a-371e-8ad6-3db00425bdbd | -3.08118 | -52.92475 | 2025-09-28 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 9d6d2fe7-451f-306a-b26f-052c4d344347 | 0.28552 | -51.40396 | 2025-09-28 00:54:00 | TERRA_M-M | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 8.8 |
| dbdd3eaa-1e47-3039-bc3c-6cc97063e483 | -4.79378 | -50.80896 | 2025-09-28 00:54:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| d08f114e-4adf-39a8-b1f1-a7ecd4b3fc08 | -4.87536 | -45.85844 | 2025-09-28 00:54:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 05590175-ba27-3d76-ae45-5cd4c35656f6 | -3.03223 | -50.44011 | 2025-09-28 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| f3ccd0f6-0cd9-3d35-b0d5-7a18d06947c3 | -4.86219 | -45.77127 | 2025-09-28 00:54:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 36.5 |
| df99e9af-f495-3d4e-b9f7-a06f13e3d45a | -3.64231 | -48.31944 | 2025-09-28 00:54:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 12342b89-51c3-346a-ab5a-92344e30d43e | -1.36008 | -49.30328 | 2025-09-28 00:54:00 | TERRA_M-M | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 30256e21-9b2b-3f28-a007-10c5d22035d9 | -2.57984 | -48.40969 | 2025-09-28 00:54:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| b9b20271-d420-393e-8f40-e9de0be2de29 | -3.7285 | -49.45033 | 2025-09-28 00:54:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 8d1784b4-336b-32ed-adf7-5766abc15327 | -1.36586 | -49.29093 | 2025-09-28 00:54:00 | TERRA_M-M | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| de374e29-4a6e-394b-a26b-ad1a95d3fa54 | -2.97299 | -49.22883 | 2025-09-28 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 3fcc511a-8415-319e-a1e0-552df516eb9b | -3.97072 | -49.45948 | 2025-09-28 00:54:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| f4f627ea-a3de-3e9e-9905-d5838211a91f | -4.87328 | -45.85201 | 2025-09-28 00:54:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 11425701-2978-3078-962f-ea32ace8d7ba | -3.328 | -50.2467 | 2025-09-28 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 363ea6c9-17ac-30ab-813f-78983f749d56 | -2.47913 | -47.65698 | 2025-09-28 00:54:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 26314910-4897-36b6-94fd-8b7bb036bb3f | -4.47849 | -47.6789 | 2025-09-28 00:54:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| f322238e-3c6f-3915-8600-378b862c6b72 | -1.3683 | -49.30862 | 2025-09-28 00:54:00 | TERRA_M-M | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| a34611be-d902-31b4-85aa-03fa1b95c8d8 | -1.95811 | -54.05385 | 2025-09-28 00:54:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 962f88fa-3378-3868-9dd4-c3aef8b3ecaf | 1.86646 | -50.83973 | 2025-09-28 00:54:00 | TERRA_M-M | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 8.2 |
| fabf9dee-df1c-35ca-a90e-be46f201d68d | 0.28376 | -51.41688 | 2025-09-28 00:54:00 | TERRA_M-M | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 7.7 |
| e10f3795-03c2-3291-8630-740929d995c6 | -6.51402 | -54.86708 | 2025-09-28 00:54:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4d4cf4c3-5c41-3e10-9bdc-c081f81138a7 | -3.88833 | -52.29369 | 2025-09-28 00:54:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 143113c7-d0a1-3c7c-9cde-1dd46d5bd6ef | -4.85918 | -49.47468 | 2025-09-28 00:54:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 0f97846d-182a-3700-9e82-d23f8f849fb5 | -14.7655 | -45.6854 | 2025-09-28 01:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 152.7 |
| bb3788db-7e95-345a-b648-54bbf4065cc5 | -13.0106 | -49.4641 | 2025-09-28 01:00:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 9b6b1337-cd65-3345-acc6-7b232ff51914 | -16.9667 | -53.6975 | 2025-09-28 01:00:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 5079232d-4d0c-3552-89e2-d5811e8d7f83 | -14.7851 | -45.6818 | 2025-09-28 01:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 6e66515f-726f-37bb-b918-de5731e5befc | -7.7975 | -47.0019 | 2025-09-28 01:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 8c4574c3-70a0-3781-9f95-be05e1932d3e | -18.0254 | -51.1591 | 2025-09-28 01:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 4a196dba-8e0e-3c24-8986-12d78f0c9792 | -7.3847 | -47.0378 | 2025-09-28 01:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 56.4 |
| a8e0fc72-21af-39a3-805b-5eb98e5fe19e | -9.6511 | -62.8526 | 2025-09-28 01:00:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 199fb22c-efbe-36f1-97a8-c4a41c544979 | -7.7412 | -47.007 | 2025-09-28 01:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| bc838795-c383-38e7-aed0-974d56cd5e83 | -9.0766 | -45.5519 | 2025-09-28 01:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 74.7 |
| c4387937-5fda-35ef-b5f4-74962395dd40 | -7.7599 | -47.0053 | 2025-09-28 01:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 819bb356-875a-3271-ad14-4658355379d6 | -5.8149 | -42.8167 | 2025-09-28 01:00:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 74.4 |
| 8daeea9d-822d-3716-929b-7366f7805546 | -6.9233 | -39.5871 | 2025-09-28 01:00:00 | GOES-19 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 63.2 |
| d64f102c-7124-3bd6-a0f4-4e8f2d506a68 | -13.011 | -49.4423 | 2025-09-28 01:00:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 03e330ff-d3ff-363f-b2bd-593f0c4003ad | -11.9846 | -47.8865 | 2025-09-28 01:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 24d5b180-4e05-31aa-966a-a30b6587400c | -9.058 | -45.5313 | 2025-09-28 01:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 256.6 |
| 43be0ea4-87a5-3e17-a630-00b5b571cf96 | -18.0653 | -51.1522 | 2025-09-28 01:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 84.1 |
| da702c35-0f40-359f-8861-2efa7344c786 | -7.7602 | -46.9831 | 2025-09-28 01:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 60.3 |
| f4e495a2-caff-3885-9aaa-fc1fbba0d848 | -9.0577 | -45.554 | 2025-09-28 01:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 836b42f4-5aa3-32b3-85f4-8a91cd65d4de | -12.9918 | -49.4448 | 2025-09-28 01:00:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 31.4 |
| d36543a6-1c7c-39f9-ac7c-703a4c03640a | -6.7782 | -44.0876 | 2025-09-28 01:00:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 14015c94-e542-38b8-be71-e553cfcd2fc8 | -9.6512 | -62.8336 | 2025-09-28 01:00:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 2a4bde83-c008-345b-809e-2d138fe955a5 | -18.0249 | -51.1811 | 2025-09-28 01:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 65.8 |
| d99d34d9-a807-3f9b-a309-a4ea2618ccf8 | -9.077 | -45.5292 | 2025-09-28 01:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 277.3 |
| ab436454-d914-314f-8b58-87f0d3181eeb | -14.766 | -45.6621 | 2025-09-28 01:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 121.8 |
| 4f3287fd-00b1-3474-81a9-0d213f83135c | -14.7861 | -45.6353 | 2025-09-28 01:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 3b632895-5689-30e0-9527-0e32377d9153 | -7.7785 | -47.0258 | 2025-09-28 01:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 100.8 |
| bf192443-34b0-3878-9fed-15170f9fe300 | -9.0583 | -45.5085 | 2025-09-28 01:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 2ee133f2-3740-367c-92f3-725f88b9d27f | -9.0773 | -45.5064 | 2025-09-28 01:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 71.9 |


[Clique aqui para ver as próximas entradas](README7.md)
