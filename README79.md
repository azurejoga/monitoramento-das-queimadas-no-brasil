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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 59e13630-eded-3734-877b-99f66af62c35 | -3.20322 | -46.49825 | 2024-11-10 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 711889c5-18b4-3841-ad7b-0506363bb693 | -4.72872 | -43.2527 | 2024-11-10 04:38:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 561f54f2-ce37-3cfa-acb8-557da0f7b7de | -2.32738 | -50.51036 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3761ff94-f248-37a8-983e-da696c874f7f | -3.23612 | -50.30843 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| b0c75a24-8d3c-3cc6-9be5-07d8d2fa78aa | -4.05795 | -48.31617 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b4102bac-cef7-3825-83c4-f6ee484840c2 | -7.12729 | -45.39877 | 2024-11-10 04:38:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 70dd8bac-c1df-36b8-84b5-0984461dcf93 | -2.838 | -46.64656 | 2024-11-10 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a872ce23-61ee-3835-aec3-47032276eeaf | -1.66915 | -55.17493 | 2024-11-10 04:38:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a426cf87-5e2b-30d7-b209-569084347e37 | -2.68279 | -51.94123 | 2024-11-10 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 00ee187f-360d-329b-8c43-c3e8a4606a87 | -3.03456 | -49.52972 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9fc87da0-3a00-30ce-b503-da16db0d6628 | -2.73556 | -49.01821 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d0d96189-2ae4-3faf-bd40-c74506a1ad4f | -3.22307 | -50.30262 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6c077354-73bd-3aeb-adff-6a3f9561d08a | -2.60509 | -49.81801 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f9a671dd-3bc8-32dd-99dc-5df690d16231 | -3.04062 | -50.41747 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1b1e16c2-5b1a-3c40-a10c-2ede842bb349 | -4.24277 | -45.37906 | 2024-11-10 04:38:00 | NPP-375D | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 73644c3f-6eff-3a48-9bc0-f54f8b066cd9 | -2.50572 | -50.48343 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4b93e0d2-ade2-3dc7-b25e-ec7e07550e03 | -3.1161 | -50.20797 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 08b7454d-f004-3249-8b78-a6b064460ef7 | -3.23472 | -46.53777 | 2024-11-10 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f46e4dd3-b26e-341a-ba6e-e9a91eadc86f | -2.32475 | -50.57175 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4b701691-6128-3b97-865a-772720879cd4 | -4.7129 | -48.798 | 2024-11-10 04:38:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4dac757d-abf4-3161-ae70-f4ff7496cec8 | -2.84628 | -53.97862 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 6e49178c-fd39-3964-8f3a-378512cac718 | -2.91571 | -49.35683 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3531f974-93de-3f2f-b33e-41fee6717216 | -3.59315 | -50.23736 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 487065b6-2832-30b7-a799-5a6a82b30012 | -4.38468 | -47.26928 | 2024-11-10 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1e100f24-9254-37cc-8e0e-69debe07a91c | -2.8237 | -46.64814 | 2024-11-10 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fbb065c3-1b75-3040-b348-21775c6bb8d3 | -2.85909 | -48.45058 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d8725ac-a157-30c3-ae09-1e4194982fb4 | -6.417 | -47.71043 | 2024-11-10 04:38:00 | NPP-375D | SANTA TEREZINHA DO TOCANTINS | TOCANTINS | Brasil | 1720002 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f815af4-f9cc-31e4-839f-74bebd8ad095 | -4.01723 | -43.66628 | 2024-11-10 04:38:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4f30d45c-c0d5-38f1-9615-1596f9b7096b | -3.53793 | -49.25788 | 2024-11-10 04:38:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd59a8ea-b5f2-3e9c-bfc6-9c0bb4b8c8c5 | -3.1963 | -46.49717 | 2024-11-10 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4e2c5a8-914e-34b0-8e85-bd0dc8871d7c | -2.36075 | -49.79173 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a4223f0-e8f0-3cca-84cf-f78787acbf72 | -2.68635 | -51.8231 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8db69273-0eb4-38b7-82bd-1dbb22becc57 | -2.83478 | -49.46634 | 2024-11-10 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b92dd021-0615-3ba1-b36f-a2fe4f3eae8f | -2.78345 | -53.96552 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2a88e0a8-0625-37fe-b6d7-beb242f44c19 | -4.30027 | -48.64498 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 32e8ce0f-d9b6-304a-8b1a-b72b32fd5f45 | -2.73127 | -49.77242 | 2024-11-10 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5695ef5e-947f-3fd2-ab1f-94bc7cdd881c | -2.43212 | -50.51101 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b8b4301e-7198-32d2-896f-2d33ef2008bb | -4.60912 | -45.98185 | 2024-11-10 04:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 630d12f9-b177-3541-8122-16f0ea49c466 | -3.82007 | -48.88423 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9fe94a8f-5608-34cc-af0c-0351b37e9326 | -2.45851 | -50.25611 | 2024-11-10 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6ef8e1d2-6acb-3738-b062-5a63ed662b50 | -2.31331 | -50.84834 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b3dbfdeb-279c-3753-946b-7e46ddb13e3a | -4.51278 | -45.68249 | 2024-11-10 04:38:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ff19ffbf-4ad7-37e7-b2a0-02823291ecc2 | -4.24307 | -48.02024 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5b574aa7-d2d4-3ce7-a8c9-7b19b626ef96 | -3.08437 | -49.57307 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e46d02f7-7924-31d9-a449-fe47bf359274 | -2.88958 | -49.39215 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69b09e00-7f32-3671-94d3-6d7e3c8b0a44 | -3.48263 | -50.38405 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a502befe-6176-3637-938d-885df2f9d072 | -3.05544 | -48.0217 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7837108f-cbec-33e2-b3c7-c39361281d4d | -3.70471 | -53.39703 | 2024-11-10 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a24f5478-b7c1-34a6-a9c6-2874eb600951 | -3.66577 | -50.2632 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a72450bb-c57c-3f24-9a41-e03855e2ecb0 | -2.28847 | -50.46576 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 59b7cb55-dd10-3232-87d0-2f15593afd0d | -3.6222 | -55.51561 | 2024-11-10 04:38:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bd1d05dc-9015-337c-b112-1f2b9f214721 | -5.17103 | -50.68377 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d36a1f4-0302-3880-9f7b-e21b6fadf4d3 | -2.39928 | -50.32282 | 2024-11-10 04:38:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 943d2042-06fd-3954-991b-0d648cab0699 | -2.4232 | -51.95217 | 2024-11-10 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| e84701ef-c3aa-315e-8b69-6ba2f4f866bd | -3.51618 | -44.02326 | 2024-11-10 04:38:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2a67d6e1-8ccb-3078-82ff-f0fc3fafd2ba | -3.94923 | -48.14272 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e6c4119a-f479-3b7d-bf61-e5d56ec244da | -3.01351 | -53.27058 | 2024-11-10 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1b802454-a408-3715-b4ec-dc10c852426d | -3.34301 | -50.36229 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4b2192fe-f68c-3f9a-a66d-4fad08fe99f5 | -3.17465 | -51.31058 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 15423fb6-13b5-3c4b-83c3-afcd577b2dc2 | -4.88611 | -48.60181 | 2024-11-10 04:38:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 255589fd-e1bc-3ca0-8385-9542e2430b3a | -2.70552 | -49.42399 | 2024-11-10 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1410c469-e8c8-3e65-9427-4e606b42ef06 | -4.51811 | -45.69613 | 2024-11-10 04:38:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 12d1d355-3427-31ba-9652-78c0d5aec5af | -3.04014 | -49.5378 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f7bbf3ac-9819-3fef-be31-43ba5e068dbd | -3.03158 | -51.52815 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 80fb370c-374f-373d-ba96-d18a6d4bde31 | -5.01627 | -45.04101 | 2024-11-10 04:38:00 | NPP-375D | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e1b44ab7-da93-38b7-aae4-867f2f5cb081 | -4.10287 | -48.97782 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 44b9d1a5-55d1-3a06-9740-c03c2f5ab0a7 | -3.62982 | -50.18352 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d86108d7-6b81-3b6c-836f-a3afcd738c75 | -2.93865 | -51.04945 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 20530db4-cc8a-33f7-9d7a-68dc6dd1dc14 | -5.84503 | -42.48882 | 2024-11-10 04:38:00 | NPP-375D | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| eaf8da43-3532-35f8-a79b-b36ba6d35a59 | -5.26648 | -46.30677 | 2024-11-10 04:38:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0eccb7a1-63c3-39e7-b352-dc612ef77d63 | -3.24626 | -45.99229 | 2024-11-10 04:38:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7aa2613a-2d33-31f6-8412-72f2d173f8a7 | -3.58576 | -50.41472 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c6cb37c5-8a5b-3416-80e3-95c4d441b248 | -4.31179 | -48.61491 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b78fffc8-e568-3feb-a6f0-9046ad384885 | -2.88847 | -49.39914 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e1ee1f23-471c-3832-86bc-04b257b18a39 | -5.37905 | -42.76441 | 2024-11-10 04:38:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0ebc9e02-343b-399a-902c-5479a026e97e | -3.89258 | -49.98219 | 2024-11-10 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 93367b45-3ec4-3f22-a9d1-e907f54364c5 | -2.94049 | -54.45633 | 2024-11-10 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 77df3b93-d4a7-3a40-9e56-4fa4301f0faa | -5.06244 | -50.01048 | 2024-11-10 04:38:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| ffd1a7ef-a961-3be9-b90e-8983375a5250 | -2.9493 | -49.51285 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a7bb7423-c1be-31fe-b82c-a720e578f3b4 | -10.94406 | -40.82148 | 2024-11-10 04:38:00 | NPP-375D | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 43ef6594-cede-3a9e-9d85-759a07b62931 | -2.20384 | -51.94717 | 2024-11-10 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8a51f733-2534-3e18-b259-74802aca63b2 | -3.66352 | -50.25543 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 59b18c02-0bf3-35b2-bdc1-a3507f7eecd1 | -3.25225 | -48.74875 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c49337c-3fb3-3100-a454-a1deead48500 | -2.46633 | -50.45116 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 73a46ec8-54b2-30b5-825a-d17d9728527e | -2.81862 | -52.96008 | 2024-11-10 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d6b402ad-138e-3542-a75f-df55811480b3 | -4.01676 | -48.29906 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b35be0b-4c5b-323f-b99b-28d0ff1d40c0 | -2.24851 | -53.66912 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fe3e84cd-62ed-3646-8e44-aea5440a2cd0 | -3.96208 | -48.16962 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1fe7ea4-9d13-327f-ba38-1806e0ced2a2 | -2.99123 | -51.45934 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 15dd5178-3214-3410-8759-254bcf947864 | -3.15011 | -48.58122 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 119e430c-b886-3cf6-9695-3def31d6fe4c | -3.01403 | -53.25792 | 2024-11-10 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 13a1d6ec-e9e6-3c8a-85bd-c59cf5928401 | -3.0971 | -54.26908 | 2024-11-10 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e47a72e2-4885-3b15-9f98-1a70df3b6c29 | -2.93815 | -51.0496 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3f1edb02-0e93-3fdd-afc0-71c1620bdc73 | -2.93812 | -49.4967 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 77bded0e-0e81-3fc8-b949-c34d8ef9bbcb | -4.20396 | -48.54814 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c514f1f-40ad-30c0-89ae-1b4f81155609 | -8.4109 | -44.13394 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| be8ccb11-6e2a-3dc7-81de-c1f53b595d38 | -3.24132 | -50.2756 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8287040e-8afe-3cf4-a893-27f476916696 | -3.96148 | -48.99473 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5b8ba126-be64-3762-8267-d549d9fa5101 | -4.11696 | -48.49896 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a043e731-5734-3d9c-9d83-b1ffde663f40 | -4.29586 | -48.65137 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README80.md)
