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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4625984a-b5df-32b5-ac88-5cb3bd8f5b54 | -3.8625 | -47.955101 | 2024-10-10 00:21:25 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7617d84d-6d04-35ff-9779-a24a0e620b5f | -3.8652 | -47.967098 | 2024-10-10 00:21:25 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1d9059e-d3d7-39d0-92e2-a64626f6e0c1 | -4.0359 | -49.056801 | 2024-10-10 00:21:26 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 639a0096-954e-3239-b7ea-01a82be88fbb | -4.0391 | -49.071201 | 2024-10-10 00:21:26 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54962f51-182c-33d8-afdb-4973fe75a94f | -4.0262 | -49.058899 | 2024-10-10 00:21:26 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d07f2d7-a44f-3c05-838f-0c047e4d5b1f | -4.0294 | -49.073299 | 2024-10-10 00:21:26 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae34a14e-d51f-3e4a-bcd5-599013113eed | -3.835 | -48.336601 | 2024-10-10 00:21:26 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d33d9fb-2ade-39bf-be16-f2f593b1f743 | -3.8378 | -48.3493 | 2024-10-10 00:21:26 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dbe055a6-9396-3b40-9b12-ddf6801438ab | -3.6536 | -48.349201 | 2024-10-10 00:21:29 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d6292cf-eda8-3f71-a636-780922c1fe10 | -3.6439 | -48.351299 | 2024-10-10 00:21:30 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f150e2d6-3bb2-3226-892e-164b736609f0 | -3.2366 | -46.991798 | 2024-10-10 00:21:31 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0b4a4eb-0003-3c3e-aab2-af820cf95cb4 | -3.2314 | -47.014301 | 2024-10-10 00:21:31 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d1248ac-0d4e-330c-9cd3-1913893bb6aa | -4.0215 | -51.020599 | 2024-10-10 00:21:33 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a5b413f-8c29-379a-9219-777fcf430a43 | -4.0075 | -51.002899 | 2024-10-10 00:21:33 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66fe4a8e-996f-37f7-a3de-a415329a3e8e | -4.0118 | -51.022598 | 2024-10-10 00:21:33 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e21ac89c-973e-36fb-af3d-99df6e6b1c68 | -4.0162 | -51.042301 | 2024-10-10 00:21:33 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb62872e-ab8d-354a-bc8c-033e63de0e2e | -3.9978 | -51.005001 | 2024-10-10 00:21:33 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 651a0e92-9a32-3d91-b766-3940136c2120 | -4.0021 | -51.0247 | 2024-10-10 00:21:33 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a7665c9-40ca-34b8-984f-06bdeb0402f9 | -3.5851 | -49.509399 | 2024-10-10 00:21:35 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c992e1c-aa24-3137-9bdb-516f092b3ebf | -3.6053 | -50.105202 | 2024-10-10 00:21:37 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b41eb8d-9a2b-36aa-9261-f8332a91bda5 | -3.609 | -50.121899 | 2024-10-10 00:21:37 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3098c25-0a49-3ac5-8c1d-139073523428 | -2.7701 | -46.698898 | 2024-10-10 00:21:38 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 00795950-df39-307b-92db-5f90be18c247 | -2.7723 | -46.7085 | 2024-10-10 00:21:38 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4e64313-6fd1-3ebb-a2dc-ff6c81d633d7 | -2.7603 | -46.701099 | 2024-10-10 00:21:38 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9e19464-8959-3fcf-b7b6-d5d3f7039bb0 | -2.7625 | -46.710701 | 2024-10-10 00:21:38 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f4e3e54-0a98-3d78-938f-5ec402560711 | -3.6148 | -51.066399 | 2024-10-10 00:21:40 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6211d79b-1308-36de-be6c-f17f05bbe244 | -3.6051 | -51.068501 | 2024-10-10 00:21:40 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e7aa58a-112b-3b3f-9873-8c3ac5bdb64a | -3.6041 | -51.109798 | 2024-10-10 00:21:40 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b49cea0-eab2-38f1-93cc-f1a36a999017 | -3.7169 | -52.309299 | 2024-10-10 00:21:43 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f98f33f-e418-3ea9-9e20-28caedd21e66 | -3.7222 | -52.333302 | 2024-10-10 00:21:43 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 98df9090-4e59-3704-b9f0-2fc620746138 | -2.5717 | -47.365398 | 2024-10-10 00:21:43 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc7f1323-ffee-3d62-8442-0ab5e8391102 | -2.574 | -47.3759 | 2024-10-10 00:21:43 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5d60503-5481-3b7e-a07f-adba7ea318fe | -3.6633 | -52.295799 | 2024-10-10 00:21:44 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7e48653-268f-3f0b-ad58-e486e6011505 | -3.6536 | -52.297798 | 2024-10-10 00:21:44 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db199af6-2f27-3019-aa2e-faa610c8cda0 | -3.6589 | -52.321701 | 2024-10-10 00:21:44 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0404a8ce-ba1e-396a-a703-dba67da4989f | -2.2627 | -46.455002 | 2024-10-10 00:21:45 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a332b11-f349-369e-98ea-e1e0af68e333 | -2.2648 | -46.464199 | 2024-10-10 00:21:45 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 294822b6-4ee1-3691-97a9-0d8094b39ead | -2.8732 | -49.204102 | 2024-10-10 00:21:45 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43de9acc-e717-3f03-a65a-ae349d72b31a | -2.8763 | -49.218102 | 2024-10-10 00:21:45 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9df6f087-c261-302d-9fa9-b1e2e63e545a | -2.8922 | -49.289101 | 2024-10-10 00:21:45 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dbe645d4-8546-3b10-a60b-745672ebed13 | -2.8955 | -49.303398 | 2024-10-10 00:21:45 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1cb93310-8ead-3a57-89ee-8f38f6b1902f | -2.7193 | -48.565601 | 2024-10-10 00:21:45 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a5d9b76-4e77-3786-b43b-9a39f9b2287b | -2.7222 | -48.578201 | 2024-10-10 00:21:45 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd6d2b77-0fd8-3d8f-8808-15d78b8a8a86 | -2.9119 | -49.513699 | 2024-10-10 00:21:46 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e361cab-d08e-31b4-9d5c-a9777e14ddc1 | -2.9152 | -49.5285 | 2024-10-10 00:21:46 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc1ae1a0-e6d6-3a78-91ad-218a49fbb642 | -2.9055 | -49.530602 | 2024-10-10 00:21:46 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c684833e-0ec7-3af4-9861-4c1eb014324d | -2.0851 | -45.944801 | 2024-10-10 00:21:46 | METOP-C | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c23a732c-afc2-30a1-843b-5b5121cc546a | -2.6712 | -48.6698 | 2024-10-10 00:21:47 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 588749f9-7f20-399f-8bef-ffb2576473f7 | -2.6741 | -48.682701 | 2024-10-10 00:21:47 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 754bd5e3-345b-3ea7-902f-73a367645561 | -2.677 | -48.695499 | 2024-10-10 00:21:47 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6958f3c-d362-32f0-b6cd-7ec5f7670aa3 | -2.2258 | -46.971802 | 2024-10-10 00:21:48 | METOP-C | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| efb0f40c-f917-376e-8c7c-fe4fc5dc2cde | -2.216 | -46.9739 | 2024-10-10 00:21:48 | METOP-C | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 97c25e30-fe9b-3d9d-836c-c6aa5eb11ffb | -2.2182 | -46.983799 | 2024-10-10 00:21:48 | METOP-C | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 98cf392a-95d0-34d8-8384-de49d0c090e1 | -2.3861 | -47.815498 | 2024-10-10 00:21:48 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2b381b7-d885-35e5-a76d-a5dcade623d1 | -2.3886 | -47.826698 | 2024-10-10 00:21:48 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c01a511-18fa-3096-a708-f5e4a3d9ec12 | -2.6945 | -49.228199 | 2024-10-10 00:21:48 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e657719-0d99-3003-b2d6-376050fc40b3 | -2.6977 | -49.242298 | 2024-10-10 00:21:48 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a917e214-e31b-3d34-a093-ece59349d181 | -2.4108 | -48.060902 | 2024-10-10 00:21:49 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9594dd50-62c0-3efe-8441-bb799256fd32 | -2.0581 | -47.500301 | 2024-10-10 00:21:52 | METOP-C | MÃE DO RIO | PARÁ | Brasil | 1504059 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4cb2dac0-514d-3a50-9795-8995a5743d68 | -2.2601 | -48.482498 | 2024-10-10 00:21:53 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8178231e-4acb-3845-a256-d2e94d9793d1 | -2.1555 | -48.020199 | 2024-10-10 00:21:53 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ecaebc03-099e-38fb-885b-04b1c1909ac8 | -2.1581 | -48.031601 | 2024-10-10 00:21:53 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f62478b9-4464-3482-aa22-94e013d94b88 | -2.5238 | -49.7873 | 2024-10-10 00:21:53 | METOP-C | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9c94d18-4c6b-3d81-8dc8-4f51e2c7da89 | -2.5272 | -49.802502 | 2024-10-10 00:21:53 | METOP-C | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1587fa9f-fd2a-32ba-aa6b-f9666079ead2 | -3.2517 | -53.180698 | 2024-10-10 00:21:54 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2dd45c3e-c2ec-3aed-8a4e-b9ee3cf3bb1d | -3.2577 | -53.207802 | 2024-10-10 00:21:54 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb38ee3c-d735-3c00-a39b-e052127ec370 | -3.2637 | -53.2351 | 2024-10-10 00:21:54 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55ebf643-2832-3269-8767-d6ff51cb1fdc | -3.242 | -53.182701 | 2024-10-10 00:21:54 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72fdbc20-cd39-36d9-a3e6-ba97fc0af4d7 | -3.248 | -53.209801 | 2024-10-10 00:21:54 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa42f6e2-1801-3208-8af1-545bb20a3632 | -3.254 | -53.237099 | 2024-10-10 00:21:54 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d657c80-1ee5-3b7d-ac16-78b9badb699f | -3.1726 | -54.1441 | 2024-10-10 00:21:58 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f94ed95-6a60-3212-bab1-83bfa193a0de | -3.1796 | -54.175701 | 2024-10-10 00:21:58 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c43a079c-86de-3920-bcb3-2ded1cd23248 | -3.1699 | -54.177799 | 2024-10-10 00:21:59 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 078dc685-6d7b-390f-a04a-f6dece4555ca | -1.7159 | -47.8466 | 2024-10-10 00:21:59 | METOP-C | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c824c244-52ad-38fc-a64a-c45aa5ac95e6 | -1.7061 | -47.848701 | 2024-10-10 00:21:59 | METOP-C | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d76ebdd-9846-3274-9c1e-90358c58edcb | -1.3361 | -46.450298 | 2024-10-10 00:22:00 | METOP-C | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3d2f312-c7a6-3ec9-92ac-32030ec778d4 | -2.7683 | -52.873299 | 2024-10-10 00:22:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad6db8fd-8723-3a8c-8621-a1669a7e448b | -2.774 | -52.898701 | 2024-10-10 00:22:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58be5c3d-1071-38c0-82b5-a943064d789b | -2.7643 | -52.900799 | 2024-10-10 00:22:01 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6edb066-2f20-3afa-8e32-8981582de627 | -2.77 | -52.926201 | 2024-10-10 00:22:01 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20ef9caf-002c-365e-b0a0-d4e300ed4b17 | -2.7603 | -52.928299 | 2024-10-10 00:22:01 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b26b803-0081-3348-9573-5ce11c04a2a5 | -1.5154 | -47.641998 | 2024-10-10 00:22:02 | METOP-C | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e6879c2-83f0-3c86-8840-9cd84b7b82b1 | -1.1902 | -46.352402 | 2024-10-10 00:22:02 | METOP-C | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6104a7df-9789-3fa0-a582-668da5164eee | -1.1923 | -46.361198 | 2024-10-10 00:22:02 | METOP-C | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd14d81b-55c0-33e9-8dfd-8d84fe3c04aa | -1.3903 | -47.2286 | 2024-10-10 00:22:02 | METOP-C | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad4fcbfd-0292-3d88-a582-adfbeffe6f04 | -1.3926 | -47.238499 | 2024-10-10 00:22:02 | METOP-C | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 498ad91f-3c6c-38d9-9402-6dc588f8d9ef | -1.3948 | -47.248501 | 2024-10-10 00:22:02 | METOP-C | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54316996-c5bb-318f-90cc-12fd28198b45 | -2.5663 | -53.328098 | 2024-10-10 00:22:05 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b7bb16b-16d9-3762-9b05-fe1ecfa946f9 | -2.5917 | -53.350899 | 2024-10-10 00:22:05 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7120b217-6f97-36d1-aac8-b05750f382dd | -2.6049 | -53.319698 | 2024-10-10 00:22:05 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 63c57947-181b-3c85-a58a-58dc466dd86d | -2.611 | -53.346699 | 2024-10-10 00:22:05 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca75c9f9-95e9-3e57-a137-317d86e5d422 | -2.5893 | -53.2948 | 2024-10-10 00:22:05 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f49e6e76-2fdc-3bc8-92fa-bfcaf099d124 | -2.5953 | -53.3218 | 2024-10-10 00:22:05 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51684a32-4ec5-3d35-b978-8527906600b7 | -2.6014 | -53.348801 | 2024-10-10 00:22:05 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd8f6012-d29a-33e8-a753-e19a8e296632 | -2.5796 | -53.296902 | 2024-10-10 00:22:05 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d4b6398-4be4-35d3-9b86-09c866bae9c9 | -2.5856 | -53.323898 | 2024-10-10 00:22:05 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9bf14ca6-4f56-34a3-b51a-11f0a927b2b8 | -2.576 | -53.326 | 2024-10-10 00:22:05 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5079650-0e30-3c09-9367-b82639c23f86 | -2.5821 | -53.353001 | 2024-10-10 00:22:05 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8566a05f-ded8-3870-93ab-4bcc2b3134d0 | -1.2541 | -55.7101 | 2024-10-10 00:25:13 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| edc396db-88ee-3658-b87b-70873c86f149 | -3.2571 | -54.1824 | 2024-10-10 00:25:25 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |


[Clique aqui para ver as próximas entradas](README15.md)
