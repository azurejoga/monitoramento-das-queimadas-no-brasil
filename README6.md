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
| 71857394-6a15-3c0b-ba16-2e33279c451a | -2.126 | -53.614101 | 2024-09-30 00:29:25 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7eee985-7fba-3117-bdce-6348129efa8e | -2.1307 | -53.635101 | 2024-09-30 00:29:25 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd8fbd9d-3da1-3f0a-a627-d5721dc42fb2 | -21.67 | -54.87 | 2024-09-30 01:03:22 | MSG-03 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 6ad37db0-1f57-32be-934d-86d09a32cb00 | -11.12 | -45.74 | 2024-09-30 01:04:20 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ca9c5e80-4737-30ce-bc8a-42106ed2e1c1 | -11.15 | -45.74 | 2024-09-30 01:04:20 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6b990da2-cc7c-336d-9622-0c8349143ec6 | -11.15 | -45.69 | 2024-09-30 01:04:20 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 91811833-314b-3add-9822-2da5ee0651f3 | -11.18 | -45.7 | 2024-09-30 01:04:20 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 79dbcdd5-c2b4-3e06-ba49-65485b072687 | -10.66 | -46.2 | 2024-09-30 01:04:25 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5dbbc2fa-4963-3e4c-b6d5-a35048fadcde | -10.66 | -46.15 | 2024-09-30 01:04:25 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 49cbc79d-8192-3fe3-a4a0-a9582bc82701 | -23.1063 | -50.3951 | 2024-09-30 01:08:53 | METOP-B | BANDEIRANTES | PARANÁ | Brasil | 4102406 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e0d8b954-7b7c-3d67-917c-966bcb98a81f | -21.512199 | -45.8484 | 2024-09-30 01:08:59 | METOP-B | FAMA | MINAS GERAIS | Brasil | 3125200 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| dcfdf6c5-312e-3064-ab2a-6f048754def3 | -22.239599 | -49.648102 | 2024-09-30 01:09:04 | METOP-B | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6b5bc777-d1d9-384a-b563-06f9e3e0d12e | -22.2421 | -49.658401 | 2024-09-30 01:09:04 | METOP-B | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 400a65e1-d777-3aaa-9d39-11a5a27a4d4c | -21.8531 | -48.3578 | 2024-09-30 01:09:05 | METOP-B | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c2e59242-764f-3ea4-97f3-4b1b82da690c | -21.6096 | -47.776501 | 2024-09-30 01:09:06 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| da6d3ecd-e2e3-37d8-b24b-785d082042e8 | -21.6131 | -47.790001 | 2024-09-30 01:09:06 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b7796510-6395-3e43-a35a-ec376b8a8925 | -21.599899 | -47.779301 | 2024-09-30 01:09:06 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 87019606-ecb7-36f8-974d-2f645844d38b | -21.603399 | -47.792801 | 2024-09-30 01:09:06 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| eeff0e01-1a24-391f-b2a6-d1deaa6ecf52 | -21.554199 | -47.763802 | 2024-09-30 01:09:07 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a929b787-3ddf-3383-b1f5-0eb3e27c9764 | -21.5578 | -47.777401 | 2024-09-30 01:09:07 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 911dc287-bcdb-3162-ab7a-c4d936c252c6 | -20.3081 | -46.632198 | 2024-09-30 01:09:22 | METOP-B | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 593a7c53-f736-347a-9b59-76b9bd61d5d4 | -21.6724 | -54.8162 | 2024-09-30 01:09:32 | METOP-B | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| cca9cd1b-a207-3634-8481-140dc5bd55dc | -21.674 | -54.823601 | 2024-09-30 01:09:32 | METOP-B | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| bbb4324b-1ec6-3063-8f9a-348f377161ba | -21.6756 | -54.830898 | 2024-09-30 01:09:32 | METOP-B | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| d0047915-6e4c-3094-b66b-a8018d79a863 | -21.6772 | -54.838299 | 2024-09-30 01:09:32 | METOP-B | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 47acbe79-7c0d-328f-b0c2-6cfdd5326466 | -21.6611 | -54.811199 | 2024-09-30 01:09:32 | METOP-B | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 712e5ed8-8c46-3f21-8222-64a7ff4c2cb2 | -21.6626 | -54.8186 | 2024-09-30 01:09:32 | METOP-B | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| b8f0277e-57d1-37cd-b1db-7e80a93cfb28 | -21.6642 | -54.826 | 2024-09-30 01:09:32 | METOP-B | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 44c0bab8-7f19-39ae-ac77-ea6f9222827b | -21.6658 | -54.833302 | 2024-09-30 01:09:32 | METOP-B | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| f859342f-5372-3a5f-8d82-59e7af4ad6e1 | -21.6674 | -54.840698 | 2024-09-30 01:09:32 | METOP-B | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 276d6741-d2cc-3e0d-9f7e-60f427588e83 | -21.669001 | -54.848099 | 2024-09-30 01:09:32 | METOP-B | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 6155ec95-62b6-38ff-bb13-2aa9de7bc605 | -21.6544 | -54.8284 | 2024-09-30 01:09:32 | METOP-B | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| ffee8542-2e46-3fb0-8251-25ca8ad4e068 | -21.656 | -54.835701 | 2024-09-30 01:09:32 | METOP-B | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 30904d9a-9f6c-3325-96a3-ccc022637562 | -21.6576 | -54.843102 | 2024-09-30 01:09:32 | METOP-B | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 0f1dc845-e92b-34d8-a3c9-a52b6d076c5f | -21.659201 | -54.850498 | 2024-09-30 01:09:32 | METOP-B | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| ddea2fdf-3b56-39a8-84fc-cf0732e4c9a9 | -19.43 | -45.8494 | 2024-09-30 01:09:33 | METOP-B | SERRA DA SAUDADE | MINAS GERAIS | Brasil | 3166600 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| db2d9b50-971d-39de-a966-e4c270521039 | -19.420401 | -45.852402 | 2024-09-30 01:09:33 | METOP-B | SERRA DA SAUDADE | MINAS GERAIS | Brasil | 3166600 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9072e3aa-bd84-3608-b72d-4d4f2df91818 | -19.4256 | -45.871799 | 2024-09-30 01:09:33 | METOP-B | SERRA DA SAUDADE | MINAS GERAIS | Brasil | 3166600 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a65cd4e2-f6a9-3319-a392-9a72df1264fe | -19.410801 | -45.8554 | 2024-09-30 01:09:33 | METOP-B | SERRA DA SAUDADE | MINAS GERAIS | Brasil | 3166600 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d801a218-85ed-388f-b2cf-3b2c3d6b1d38 | -20.742201 | -51.6493 | 2024-09-30 01:09:35 | METOP-B | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e50f3d74-9a3c-3828-883c-ac47257386ea | -18.9597 | -45.425098 | 2024-09-30 01:09:38 | METOP-B | PAINEIRAS | MINAS GERAIS | Brasil | 3146404 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3480b678-66e2-34d1-88cb-3e814849fab8 | -20.809799 | -53.1026 | 2024-09-30 01:09:40 | METOP-B | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 7326e174-87e7-3d41-bf06-231e2241d102 | -21.0175 | -57.494301 | 2024-09-30 01:09:52 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 36576dd6-4977-305a-8e79-7a1d58fbcee2 | -21.0077 | -57.496498 | 2024-09-30 01:09:52 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 21968620-3b04-38e6-877b-25e6fbd5e6ad | -21.009399 | -57.504902 | 2024-09-30 01:09:52 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 0da6b5d1-7564-398a-b179-1004b7ce22ef | -20.336901 | -54.825401 | 2024-09-30 01:09:54 | METOP-B | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| fa0fb763-ec8e-31ed-b0ef-4888cb915312 | -20.338499 | -54.832699 | 2024-09-30 01:09:54 | METOP-B | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 2fd48c1a-ece1-30d3-9222-a63711b77706 | -19.982599 | -55.470798 | 2024-09-30 01:10:02 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| fe5f1a1a-8eae-329d-817e-6d608c1efc6c | -19.9841 | -55.4781 | 2024-09-30 01:10:02 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 521d3933-52bb-36e9-9cc3-1165679a128f | -19.972799 | -55.473099 | 2024-09-30 01:10:02 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| ac7b241a-1469-3fb9-a99b-56f5c61b0f3c | -19.9744 | -55.4804 | 2024-09-30 01:10:02 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 7de3509b-f727-30fc-9ace-074e9c5cdcde | -19.975901 | -55.487701 | 2024-09-30 01:10:02 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| ea251d44-b7e8-352f-b700-13a51f68213f | -19.977501 | -55.495098 | 2024-09-30 01:10:02 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 7936a851-8c45-3583-bd15-8f72d37ac082 | -18.6458 | -52.4576 | 2024-09-30 01:10:12 | METOP-B | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a8e691bf-2e8d-3821-b36d-5d6fa7296367 | -18.6478 | -52.465801 | 2024-09-30 01:10:12 | METOP-B | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4e528679-ff87-3d53-9ad3-1d31a188649e | -18.8421 | -54.492199 | 2024-09-30 01:10:17 | METOP-B | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| f9e658ad-6c3c-359e-9e1c-e9ce140f8e5f | -18.8438 | -54.499401 | 2024-09-30 01:10:17 | METOP-B | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 885fe3bb-c72f-3a95-9f99-ca0385f49472 | -19.1474 | -57.454601 | 2024-09-30 01:10:22 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 22b639b0-1b80-3679-ae74-d5fed5382d12 | -19.149099 | -57.462601 | 2024-09-30 01:10:22 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f4c583e6-00ca-3952-a8a0-3a5dc646b30c | -19.1376 | -57.456799 | 2024-09-30 01:10:22 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 004b2748-3ab7-3ce1-bfc1-a112e0c87b1c | -19.139299 | -57.464802 | 2024-09-30 01:10:22 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ad8c74c8-dc14-38a8-a1d1-758d5e101e0c | -19.118 | -57.461201 | 2024-09-30 01:10:22 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 952a7ecf-e512-3678-ac8f-6fe337b3d143 | -19.124599 | -57.493099 | 2024-09-30 01:10:22 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8b145ca9-00fe-302c-9c76-964d83b52b4e | -17.1182 | -53.264702 | 2024-09-30 01:10:40 | METOP-B | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a135a453-f72e-345d-99ea-ebdd2fff49ae | -16.581499 | -51.309101 | 2024-09-30 01:10:41 | METOP-B | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 88925462-9085-3685-8a4f-31bba061c3f2 | -16.6668 | -51.7047 | 2024-09-30 01:10:41 | METOP-B | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5fb8ef6f-0fd2-3df6-a83d-3a6e63cff990 | -16.6691 | -51.714001 | 2024-09-30 01:10:41 | METOP-B | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ff292c87-664b-376d-acde-908e26415020 | -16.1038 | -50.333801 | 2024-09-30 01:10:45 | METOP-B | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| fccc3f6f-d7df-3345-b4da-8d38e0607b11 | -16.106701 | -50.3451 | 2024-09-30 01:10:45 | METOP-B | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| fb5c1d9e-f0f8-3ed5-a474-bf305b990ed1 | -16.109501 | -50.356499 | 2024-09-30 01:10:45 | METOP-B | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c94946d1-85a7-3d06-acac-5b0fd040c4fd | -16.094101 | -50.336399 | 2024-09-30 01:10:45 | METOP-B | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5dff9f1e-d5aa-3b91-af0e-f019159330fa | -16.074699 | -50.341499 | 2024-09-30 01:10:45 | METOP-B | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| cab883b5-eb6c-3305-ba68-3723243fc433 | -16.077499 | -50.352901 | 2024-09-30 01:10:45 | METOP-B | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 49dfc67b-bc43-377e-a30d-da4204fe4c21 | -16.067801 | -50.355499 | 2024-09-30 01:10:46 | METOP-B | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8ad91945-1a78-3fad-994b-b2f2f42f5096 | -17.2596 | -56.431599 | 2024-09-30 01:10:49 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5b38703b-c17a-345d-97d4-89aff0255b69 | -17.261101 | -56.438801 | 2024-09-30 01:10:49 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1f958795-a8af-3c75-9bc0-eeb0f66702aa | -17.262699 | -56.445999 | 2024-09-30 01:10:49 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| eaed28e9-ce00-3283-ad66-9ccb1bb2b1f3 | -17.251301 | -56.441101 | 2024-09-30 01:10:49 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a13d0ec3-8e1a-3699-8648-32e4a3cab27e | -17.146299 | -56.1926 | 2024-09-30 01:10:50 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 34984d89-9d4c-36ff-98c9-60eebcd9c424 | -17.1479 | -56.199799 | 2024-09-30 01:10:50 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f3834d33-2982-3d4a-91e5-a0f2bb35f876 | -17.150999 | -56.214199 | 2024-09-30 01:10:50 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b7939690-6cce-3430-9935-d02593dd0719 | -17.1525 | -56.221401 | 2024-09-30 01:10:50 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 534b8075-22bf-38af-b2f8-a6a70d1de8f3 | -17.1287 | -56.159 | 2024-09-30 01:10:50 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9b9e6af8-28e7-35d2-a342-5ca8e3436d86 | -17.130301 | -56.1661 | 2024-09-30 01:10:50 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e4eb8e0d-f216-3d30-9aca-85c746a88bdc | -17.1318 | -56.173302 | 2024-09-30 01:10:50 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1b33a7c6-7349-34c4-b701-1c7fc5256f76 | -17.1334 | -56.1805 | 2024-09-30 01:10:50 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5237c112-a87a-3d10-a621-d1c02e3efa6a | -17.134899 | -56.187698 | 2024-09-30 01:10:50 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e96e7c3c-99e1-3b4f-ad91-67e7d68d47df | -17.136499 | -56.194901 | 2024-09-30 01:10:50 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ef7e05ca-a602-3252-bbda-e332b6c3910b | -17.1381 | -56.202099 | 2024-09-30 01:10:50 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 60e0cb67-90b1-37ea-b7fe-3b03fc2c230a | -17.139601 | -56.209301 | 2024-09-30 01:10:50 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a8f4898a-a3da-3244-a629-c227fd52ef9c | -17.141199 | -56.216499 | 2024-09-30 01:10:50 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d0f6dee5-006b-3574-be63-2e88a37df1ad | -17.1427 | -56.223701 | 2024-09-30 01:10:50 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| dbf319ef-77a9-3611-8c3c-9ba3a58226f2 | -17.111099 | -56.125401 | 2024-09-30 01:10:50 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2c14b1b5-8f47-35f7-9834-e806dfb0aaad | -17.1127 | -56.1325 | 2024-09-30 01:10:50 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8867eefc-e6b5-32d4-82f0-20bfc0ceff0d | -17.115801 | -56.1469 | 2024-09-30 01:10:50 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c9fadbd4-7ed3-32b8-8065-8324222819a9 | -17.1173 | -56.154099 | 2024-09-30 01:10:50 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5e9ed126-a907-3b11-92d1-54d95ca70a69 | -17.1189 | -56.161301 | 2024-09-30 01:10:50 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7eb5334f-8af5-3614-8759-e5307aa9f0d8 | -17.120501 | -56.1684 | 2024-09-30 01:10:50 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 47c019b9-74db-3d30-aa9d-e13db11f4109 | -17.122 | -56.175598 | 2024-09-30 01:10:50 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fe5f6d7e-23c2-34e7-8537-0952b72dafe0 | -17.1236 | -56.1828 | 2024-09-30 01:10:50 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README7.md)
