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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 79a819d9-f136-384a-a3de-0cd74e7e0a0e | -17.6658 | -53.0741 | 2024-10-07 01:20:28 | METOP-C | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e689823e-e904-3ddb-b4b0-5ea8335f28ef | -17.6675 | -53.0816 | 2024-10-07 01:20:28 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| bd29e1b5-8a59-36ff-9ab9-72d2bcdd1405 | -17.6693 | -53.089001 | 2024-10-07 01:20:28 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ff72f8e0-d534-3f3d-8dc2-8ee4da0789ce | -17.649099 | -53.0466 | 2024-10-07 01:20:28 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7447aa1c-fe61-32d1-b210-13b27c4904a6 | -17.650801 | -53.0541 | 2024-10-07 01:20:28 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8086bd8a-40b1-300c-a42b-23f9825ba932 | -17.656 | -53.0765 | 2024-10-07 01:20:28 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b5e544ca-680c-349c-9aae-15dfe9d047bd | -17.6577 | -53.084 | 2024-10-07 01:20:28 | METOP-C | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1ea5db96-2249-39e1-8ef0-b82c9e153316 | -17.6595 | -53.0914 | 2024-10-07 01:20:28 | METOP-C | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| aa6c002e-3a43-35e1-a021-67ae293fc6ad | -17.6394 | -53.049099 | 2024-10-07 01:20:28 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ee8ea920-3ef6-312b-a9c9-b3c67dabd441 | -17.6411 | -53.056599 | 2024-10-07 01:20:28 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 30ea6b6e-3d59-3a71-a790-0ad70c545f3b | -17.6446 | -53.071499 | 2024-10-07 01:20:28 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e02d21bf-dc11-3460-8d9c-828a2aad0d12 | -17.646299 | -53.078999 | 2024-10-07 01:20:28 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2a000b7f-6db8-391d-93d8-4fafe0634bc3 | -17.648001 | -53.086498 | 2024-10-07 01:20:28 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 356ba551-0d4b-3c46-9a18-db7048a5b15c | -17.626699 | -53.083801 | 2024-10-07 01:20:28 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 31fcc7b4-3dc6-3af9-ac55-8957d81f0d41 | -17.628401 | -53.091301 | 2024-10-07 01:20:28 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0afa8bb0-a995-3d85-9147-419a510f6147 | -17.630199 | -53.098701 | 2024-10-07 01:20:28 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 34cececa-b904-3de0-b04e-c8e9ebb27727 | -17.6187 | -53.0938 | 2024-10-07 01:20:28 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6f5a6e75-a692-3e79-b292-7688e29afe61 | -17.620501 | -53.1012 | 2024-10-07 01:20:28 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0022bec5-a943-3c55-b375-7cc83f2e25db | -17.6222 | -53.1087 | 2024-10-07 01:20:28 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e2a793ff-6b31-3462-82a8-ebffb25c24a1 | -17.8225 | -53.757999 | 2024-10-07 01:20:28 | METOP-C | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 881771d4-2d69-306c-9312-4c122f54b889 | -17.8242 | -53.765301 | 2024-10-07 01:20:28 | METOP-C | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ff0beddc-d87c-313e-80ba-4663127ad58f | -17.8258 | -53.772499 | 2024-10-07 01:20:28 | METOP-C | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f8f7cfb5-9a3b-3e8f-9bf6-04fd1c993e61 | -17.827499 | -53.7798 | 2024-10-07 01:20:28 | METOP-C | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7ebaf127-2fba-3dea-af7b-213ca37065a3 | -17.8291 | -53.786999 | 2024-10-07 01:20:28 | METOP-C | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 45e88e10-5030-3b54-bc92-c8ab99dad26b | -17.830799 | -53.7943 | 2024-10-07 01:20:28 | METOP-C | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 443e14b0-f8a1-3a1e-b2d9-3c0d4b6d132a | -17.8111 | -53.753101 | 2024-10-07 01:20:28 | METOP-C | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5683f387-4854-3ec8-a470-b0bc94c49f92 | -17.8127 | -53.760399 | 2024-10-07 01:20:28 | METOP-C | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 328d1890-4c91-3e59-8286-044d515009c3 | -17.8144 | -53.767601 | 2024-10-07 01:20:28 | METOP-C | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9e3725fd-5b29-38fd-9956-4d589567244e | -17.817699 | -53.782101 | 2024-10-07 01:20:28 | METOP-C | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b3a7c856-d95b-352e-b9d9-2133b651fff8 | -17.8193 | -53.789398 | 2024-10-07 01:20:28 | METOP-C | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a90272dd-5082-3383-a7f5-41e77c36b32f | -17.820999 | -53.7966 | 2024-10-07 01:20:28 | METOP-C | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2e8f3817-6ded-35b3-91a5-ea4c6d37281b | -17.8013 | -53.755501 | 2024-10-07 01:20:28 | METOP-C | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5041363e-254d-39a1-a4fb-e7ad6f791450 | -17.802999 | -53.762798 | 2024-10-07 01:20:28 | METOP-C | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c60283ef-810f-3655-bcfe-70a82e52034d | -17.806299 | -53.777302 | 2024-10-07 01:20:28 | METOP-C | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5de4fed4-84bc-308c-8d3e-55d2b5e4acc2 | -17.7899 | -53.750702 | 2024-10-07 01:20:28 | METOP-C | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5ee47c6c-8d6a-3997-99f8-abc25120e3cb | -17.791599 | -53.7579 | 2024-10-07 01:20:28 | METOP-C | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| be37fa12-ea18-351e-8650-89565aa0c08d | -17.7932 | -53.765202 | 2024-10-07 01:20:28 | METOP-C | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0aacd07f-a400-3042-92e6-d57efe1be9cc | -17.794901 | -53.7724 | 2024-10-07 01:20:28 | METOP-C | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f7de2100-5e93-35f0-aa93-8b015cac8d22 | -17.796499 | -53.779701 | 2024-10-07 01:20:28 | METOP-C | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 720d91ca-e354-3182-ac22-eaef18dce230 | -17.798201 | -53.7869 | 2024-10-07 01:20:28 | METOP-C | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bdce9aa2-83ff-3ec2-ad03-3df3a77ff9be | -17.799801 | -53.794201 | 2024-10-07 01:20:28 | METOP-C | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 259aecba-a162-3d51-bb2e-53e6f560d874 | -17.8015 | -53.801399 | 2024-10-07 01:20:28 | METOP-C | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bc563894-1577-3ab1-9211-357d241bb671 | -17.7801 | -53.753101 | 2024-10-07 01:20:28 | METOP-C | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2686850a-66db-3097-b770-a893498d2517 | -17.781799 | -53.7603 | 2024-10-07 01:20:28 | METOP-C | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a083a90e-2d13-3429-a12d-06e95d56b88f | -17.7834 | -53.767601 | 2024-10-07 01:20:28 | METOP-C | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a452164c-efdf-30ce-ab38-259a107ba724 | -17.785101 | -53.774799 | 2024-10-07 01:20:28 | METOP-C | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a4ef581e-2d65-3d6f-81e6-ee7ccbe2b49b | -17.786699 | -53.782101 | 2024-10-07 01:20:28 | METOP-C | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d1b1800a-61e8-3b7e-b2b2-f3fe2aa9feb0 | -17.788401 | -53.789299 | 2024-10-07 01:20:28 | METOP-C | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 23e2f87a-ad40-3263-ab58-6363129b3af5 | -17.790001 | -53.7966 | 2024-10-07 01:20:28 | METOP-C | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9765175b-255c-3589-ac37-342bde081a30 | -17.7917 | -53.803799 | 2024-10-07 01:20:28 | METOP-C | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 23a5a757-0627-3627-aec1-8ed0349f8d81 | -17.793301 | -53.8111 | 2024-10-07 01:20:28 | METOP-C | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b975a37b-70f7-33b2-a894-bd8e84368b05 | -17.771999 | -53.762699 | 2024-10-07 01:20:28 | METOP-C | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bbf21002-a295-326d-a222-ab1bc693252c | -17.7736 | -53.769901 | 2024-10-07 01:20:28 | METOP-C | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bcaa51c5-828a-3cda-a5cd-d136ccd7bbd6 | -17.775299 | -53.777199 | 2024-10-07 01:20:28 | METOP-C | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a27a97ac-ea2e-33a7-b475-2b5b399ec953 | -17.776899 | -53.784401 | 2024-10-07 01:20:28 | METOP-C | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 022c9ac0-1539-3a03-8cd6-1a46dec7355f | -17.778601 | -53.791698 | 2024-10-07 01:20:28 | METOP-C | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bc49d09e-6d22-3dd5-b63b-571e61aadd15 | -17.780199 | -53.798901 | 2024-10-07 01:20:28 | METOP-C | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f79e8e07-5123-343e-a067-f42d7c51bb36 | -17.7819 | -53.806198 | 2024-10-07 01:20:28 | METOP-C | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| be0fa9a6-aac9-3b9c-9c67-59405866649d | -17.7672 | -53.7868 | 2024-10-07 01:20:29 | METOP-C | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 81fffb50-7114-3dd4-befd-9bb5f24d5bf5 | -17.768801 | -53.794102 | 2024-10-07 01:20:29 | METOP-C | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 683c6641-baf5-3939-98b2-ce3d44d0692b | -17.124201 | -51.694099 | 2024-10-07 01:20:31 | METOP-C | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4f016f59-ea6f-3803-86a6-3acbc51c758a | -17.1262 | -51.702499 | 2024-10-07 01:20:31 | METOP-C | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 768f52ea-425c-3f33-9f99-5da69a76defc | -17.128201 | -51.710899 | 2024-10-07 01:20:31 | METOP-C | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 84e4a006-23b0-3967-a049-adec4026e806 | -17.0853 | -52.1395 | 2024-10-07 01:20:33 | METOP-C | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| bd1af3bd-2886-3601-a460-0986a960355d | -17.1758 | -53.908001 | 2024-10-07 01:20:39 | METOP-C | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1fd425c1-3186-3792-80e2-1fc1d1a7a633 | -17.177401 | -53.915199 | 2024-10-07 01:20:39 | METOP-C | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 65abe9fb-f0f4-3375-8b27-da903536a70f | -17.1791 | -53.922401 | 2024-10-07 01:20:39 | METOP-C | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 964a2c3f-8546-3f56-aa8e-ce79b13979bd | -17.166 | -53.9104 | 2024-10-07 01:20:39 | METOP-C | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e6f9f402-5518-35c2-8c24-45a39a7ac60e | -17.1677 | -53.917599 | 2024-10-07 01:20:39 | METOP-C | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0b5bb12c-d3b7-3ddc-863e-de98cc9bf5bb | -17.1693 | -53.924801 | 2024-10-07 01:20:39 | METOP-C | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4c3a7dff-b8ab-3b4b-9040-53d4c4b9b749 | -17.159599 | -53.9272 | 2024-10-07 01:20:39 | METOP-C | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c282f6d5-838a-3363-9f7c-04de73ce54a4 | -17.3244 | -55.028599 | 2024-10-07 01:20:40 | METOP-C | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4283fb39-88b9-3dcd-bc77-4561b2c744c7 | -17.325899 | -55.035801 | 2024-10-07 01:20:40 | METOP-C | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ef434d3d-37b4-31c2-95e3-891fa717a0c4 | -17.3162 | -55.038101 | 2024-10-07 01:20:40 | METOP-C | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c7c972c9-d280-3f43-9f77-cf3178c9050a | -17.317699 | -55.0452 | 2024-10-07 01:20:40 | METOP-C | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| afd7640f-408a-31ce-96fb-286668ce712e | -17.716299 | -57.082401 | 2024-10-07 01:20:41 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d2ac89d9-5a82-3591-b0d3-c87a53a6d97c | -17.8498 | -57.6744 | 2024-10-07 01:20:41 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c7cabc7b-e213-393c-88fd-caa536676789 | -17.84 | -57.676601 | 2024-10-07 01:20:41 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d2f1c4ff-bb6a-39e5-bbdc-d362e3f36725 | -17.841801 | -57.685101 | 2024-10-07 01:20:41 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| fc35afef-5932-3813-a5c4-531318f0754f | -17.307899 | -55.047501 | 2024-10-07 01:20:41 | METOP-C | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5d7cded6-e25f-3139-9ecc-88105670d4bd | -17.3095 | -55.054699 | 2024-10-07 01:20:41 | METOP-C | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7a1d9182-64a6-3eab-9d2d-2bf5883d5c7a | -17.2981 | -55.049801 | 2024-10-07 01:20:41 | METOP-C | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9f853ca6-830b-33c2-b391-a71f2dedb0ec | -17.2997 | -55.056999 | 2024-10-07 01:20:41 | METOP-C | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7c2a58f1-904b-3d11-b704-5a8ea1f66bc8 | -17.7341 | -57.069901 | 2024-10-07 01:20:41 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9ee88090-2842-3925-8f0e-221913391729 | -17.7358 | -57.077999 | 2024-10-07 01:20:41 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a4b1c1cb-679a-3909-9624-b4ce1dfd6be9 | -17.7374 | -57.085999 | 2024-10-07 01:20:41 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 39a38ee0-eca3-3279-9ba3-8e29ef4632c4 | -17.7243 | -57.072102 | 2024-10-07 01:20:41 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9a49f406-b763-3186-a9ea-e8fd2a9ff16b | -17.726 | -57.0802 | 2024-10-07 01:20:41 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e2dd0e6c-c638-3326-974f-c98c9c183d9a | -17.7276 | -57.0882 | 2024-10-07 01:20:41 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f39584bb-68ce-3c74-8805-012c49721401 | -17.7146 | -57.074299 | 2024-10-07 01:20:41 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 573225fe-4993-3f3a-8af5-15dfa36cddd7 | -17.717899 | -57.090401 | 2024-10-07 01:20:41 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| dc82827e-0122-3027-b555-c0e5ec7d1dfd | -16.317801 | -51.268398 | 2024-10-07 01:20:42 | METOP-C | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 030416ca-855d-3260-a963-a7a7bf04fc18 | -16.315599 | -51.259499 | 2024-10-07 01:20:42 | METOP-C | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| efc266b8-40a6-3bad-a4c0-847f542b7c81 | -16.0525 | -50.437698 | 2024-10-07 01:20:43 | METOP-C | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f98cd4bf-5bad-3e37-86f7-a9b93afa06eb | -16.1751 | -50.937401 | 2024-10-07 01:20:43 | METOP-C | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0085e768-7aca-3d4c-a529-f7e6c638fbaf | -16.305799 | -51.262001 | 2024-10-07 01:20:43 | METOP-C | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 92d0537a-a75a-3190-910a-30c089ec3057 | -16.1826 | -50.925499 | 2024-10-07 01:20:43 | METOP-C | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3e0a3660-43b0-38fd-bb5f-8fcfc7a5cc69 | -16.184799 | -50.934799 | 2024-10-07 01:20:43 | METOP-C | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 511de241-bba6-3d44-8598-cbfed883950e | -16.202 | -50.920502 | 2024-10-07 01:20:43 | METOP-C | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b5813bde-5dbb-345d-afa1-6e36e5ab8e39 | -16.308001 | -51.270901 | 2024-10-07 01:20:43 | METOP-C | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README19.md)
