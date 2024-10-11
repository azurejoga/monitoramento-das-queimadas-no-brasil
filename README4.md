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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 716f9db2-9df5-3d6e-b54d-8293bcf92e4b | -10.363 | -55.8755 | 2024-10-11 00:36:05 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 5ba8ab47-47c8-3cbc-b4e1-b6ad4dc1284f | -10.3632 | -55.8554 | 2024-10-11 00:36:05 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 4c52b5a8-a7fc-33ff-889f-ffb01a74e29a | -10.382 | -55.854 | 2024-10-11 00:36:05 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 7e390648-5cd0-337d-80c9-b8ce5b35379b | -10.6171 | -47.704 | 2024-10-11 00:36:06 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 83.6 |
| b5955383-52f8-3e71-8ddc-67be92f12fa1 | -10.6962 | -53.0354 | 2024-10-11 00:36:07 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 156.9 |
| edc091f6-8686-319f-89f8-acd33e2ca5c6 | -10.6965 | -53.0147 | 2024-10-11 00:36:07 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 129.0 |
| 68e8ceec-ec97-3a60-9bff-cdc2cc93e389 | -10.7151 | -53.0337 | 2024-10-11 00:36:07 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 03d7fcff-1691-3cf1-ae2d-162dd231228b | -10.7059 | -64.1138 | 2024-10-11 00:36:08 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 63.7 |
| c587714b-59ed-3e11-bf68-b8a9fa5219d7 | -11.2407 | -53.2738 | 2024-10-11 00:36:10 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 104.5 |
| ceaab873-da32-3baf-a091-e0ae05cd1d57 | -11.241 | -53.2531 | 2024-10-11 00:36:10 | GOES-16 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 9dd45e8c-2b34-3375-88e3-21333e87471d | -11.2722 | -50.9228 | 2024-10-11 00:36:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 56.0 |
| a6165720-fea5-345c-8280-5efb9203062e | -11.2597 | -53.272 | 2024-10-11 00:36:10 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 3194650e-f0ac-38a2-bd81-9eb4fb321e13 | -11.2859 | -51.3031 | 2024-10-11 00:36:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 59.5 |
| a3a4adac-55fb-3729-a4cd-ed87b8725b69 | -11.2906 | -50.9633 | 2024-10-11 00:36:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 60.4 |
| a6a8688c-1bef-3c23-ba31-42772f309caf | -11.2909 | -50.9421 | 2024-10-11 00:36:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 82bdefd3-1cd4-33ce-bcd7-afd2eb8cc7d0 | -11.2912 | -50.9208 | 2024-10-11 00:36:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 150.7 |
| dda84361-ce22-3615-b0bc-617594d09748 | -11.6729 | -65.2251 | 2024-10-11 00:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 47.1 |
| b7fc41b7-81c4-32f6-90c0-a4d710d8e606 | -12.3171 | -45.3083 | 2024-10-11 00:36:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 78.8 |
| fbeb4f58-5d83-388b-854b-2f9d296d641d | -12.7673 | -44.8904 | 2024-10-11 00:36:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 89.7 |
| fc3a919e-bde4-30cb-bce8-ea890eefc803 | -12.7678 | -44.8671 | 2024-10-11 00:36:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 146.3 |
| d233b06a-e881-39f8-a23d-e3c303d07239 | -12.7866 | -44.8873 | 2024-10-11 00:36:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 1217d542-9d1d-3c6b-a49d-3365163679a3 | -12.7871 | -44.8639 | 2024-10-11 00:36:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 127.5 |
| 31f43f79-2b04-37d9-ba10-18c9ab36375a | -12.9661 | -53.4902 | 2024-10-11 00:36:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 65.5 |
| f4d6c405-1692-32e7-99a5-e2a7db79a9d5 | -12.9664 | -53.4694 | 2024-10-11 00:36:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 722c77c7-c952-3966-964f-a3cccdec39cf | -12.9852 | -53.4881 | 2024-10-11 00:36:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 93.3 |
| b75eeb2a-596b-3dc0-bce5-17defda021c4 | -12.9855 | -53.4673 | 2024-10-11 00:36:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 143.7 |
| 24566cd7-8d2b-3456-9c64-ac83b3166ed3 | -12.9858 | -53.4465 | 2024-10-11 00:36:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |
| a622c3ed-3dfd-3d1a-8d25-0a011007357e | -13.0046 | -53.4652 | 2024-10-11 00:36:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 56334c04-1956-3c1f-a5f0-541b0c9f0472 | -13.7346 | -60.6079 | 2024-10-11 00:36:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 98b1738c-3de3-37a3-be56-11f08d990afe | -15.429 | -60.0156 | 2024-10-11 00:36:34 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 86.0 |
| fc06986e-6866-3e1c-9e22-0fbe1d21eb96 | -18.1582 | -56.4286 | 2024-10-11 00:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.7 |
| ef1c7b77-f17a-3477-9777-a139684def34 | -18.1532 | -56.4128 | 2024-10-11 00:43:21 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 13c19609-1453-3f29-915e-d096d357ab50 | -13.9196 | -43.799702 | 2024-10-11 00:43:46 | METOP-B | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b8bf8f6b-9e8e-34e9-ac50-de586585eeed | -13.9224 | -43.8111 | 2024-10-11 00:43:46 | METOP-B | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ab67a182-6256-3a3d-94cf-80b3ec02a16d | -13.9099 | -43.8022 | 2024-10-11 00:43:46 | METOP-B | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ac844128-98e5-3448-af40-cc5993b4bf62 | -13.9127 | -43.813599 | 2024-10-11 00:43:46 | METOP-B | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 93bca3c5-39a4-3ffe-a4ec-b435e49c8d93 | -13.3599 | -44.7682 | 2024-10-11 00:43:58 | METOP-B | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b988950b-73fe-3447-b6b7-24dcee62d403 | -13.1068 | -44.069401 | 2024-10-11 00:44:00 | METOP-B | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 079f9e0a-65c5-3404-a555-f040a3e9e061 | -12.5809 | -42.413399 | 2024-10-11 00:44:02 | METOP-B | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| bcfba465-308e-39ef-89f4-a11ff76c4b39 | -12.7849 | -44.869801 | 2024-10-11 00:44:08 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c0bb997f-f1a2-3133-a0e7-bdf2a5da8b7b | -12.7873 | -44.880001 | 2024-10-11 00:44:08 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 024550fc-1b94-3a9d-8a1f-61545dcd694f | -12.7726 | -44.862 | 2024-10-11 00:44:08 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0c8e6bd0-7328-3a76-9654-bc8e7d348522 | -12.7751 | -44.872299 | 2024-10-11 00:44:08 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2d6cbaf8-ddcd-3acd-bbd7-04ffc4e231e8 | -12.7776 | -44.8825 | 2024-10-11 00:44:08 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 43d11a92-5a8c-3b58-87f9-9f6ca76cdd0f | -12.7604 | -44.854198 | 2024-10-11 00:44:08 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ab813259-7f42-3c1e-b4ba-7b3a76f76bca | -12.7629 | -44.864399 | 2024-10-11 00:44:08 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 46960441-6d5e-3e0d-a7ad-85368ce83f20 | -12.7654 | -44.874699 | 2024-10-11 00:44:08 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7677f83d-5527-37d8-b369-4c9224c0470d | -12.7679 | -44.884899 | 2024-10-11 00:44:08 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b75289f8-d49d-385c-85bb-1e7ec576d681 | -12.7506 | -44.856701 | 2024-10-11 00:44:09 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 64f9a9e6-eb3f-391d-af2b-20a9f6fcf65c | -12.7531 | -44.866901 | 2024-10-11 00:44:09 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 81e6205a-076a-3215-b72b-cabb606ba290 | -12.9647 | -46.184101 | 2024-10-11 00:44:10 | METOP-B | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 81fb4f52-d1d5-3d32-8e7f-a7b22875666b | -12.3438 | -43.741001 | 2024-10-11 00:44:11 | METOP-B | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| be1eca29-7bc7-35b7-8f69-b4fc82d9f872 | -12.3468 | -43.753201 | 2024-10-11 00:44:11 | METOP-B | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b6a9c646-4c18-3109-a381-69bc4a93bd2d | -15.4314 | -59.978401 | 2024-10-11 00:44:16 | METOP-B | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4ccdec5b-525b-313e-a776-00b4fdb27695 | -12.3113 | -45.306198 | 2024-10-11 00:44:17 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4aa3fdda-7f5e-3766-a14f-756dae649d76 | -12.3066 | -45.286598 | 2024-10-11 00:44:17 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| eb311ae1-e42f-3073-aef8-44051de5d8dd | -12.3089 | -45.296398 | 2024-10-11 00:44:17 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 38ef6fe2-9cf8-3d79-839f-6eb7b5f8b3dc | -11.8927 | -43.881802 | 2024-10-11 00:44:19 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e7187d16-6ce0-3f07-951c-fd9dfd9e6dd3 | -13.0003 | -53.4492 | 2024-10-11 00:44:36 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3ed9aac6-d13c-3323-8946-0fc224c276b0 | -13.0022 | -53.458302 | 2024-10-11 00:44:36 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4025f6e4-70ef-30b4-8fae-f5ca8c108408 | -12.9886 | -53.4422 | 2024-10-11 00:44:36 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 669ead2e-1b3b-3ea4-9482-4cee546cc373 | -12.9905 | -53.451302 | 2024-10-11 00:44:36 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cd848539-e9dd-30f8-a4ec-c259cb7bfbbc | -12.9924 | -53.4604 | 2024-10-11 00:44:36 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8952e064-b69b-31a8-b02e-d1c651ca4103 | -12.9942 | -53.469398 | 2024-10-11 00:44:36 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e183f117-0df7-39e2-a0f1-2a8346d73674 | -12.9961 | -53.4786 | 2024-10-11 00:44:36 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 81ccfd89-84e1-3668-94b8-2ca2eb4b14f9 | -12.9788 | -53.444302 | 2024-10-11 00:44:36 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0898c92e-b481-3b5e-9b50-9517241dc2b8 | -12.9807 | -53.4534 | 2024-10-11 00:44:36 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eeaf03ff-2e7c-3306-b274-fe606d5303a0 | -12.9826 | -53.462502 | 2024-10-11 00:44:36 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3affdc2c-72b2-3c6d-8b5a-47a469efd74a | -12.9844 | -53.4715 | 2024-10-11 00:44:36 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c8cf7339-eff6-3ce2-9f9d-a5a1e02ffbcf | -12.9863 | -53.480701 | 2024-10-11 00:44:36 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 640571fc-8d14-349a-bc01-efd2811d0abf | -12.9882 | -53.489799 | 2024-10-11 00:44:36 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 35e07592-cd30-31a0-b014-4b976ab9a913 | -12.9728 | -53.4645 | 2024-10-11 00:44:36 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7c8a567a-d3a0-334a-9956-0e687e7cfdd2 | -12.9746 | -53.473499 | 2024-10-11 00:44:36 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 09260075-7f24-3cb9-8149-fc6e3aeb1fc0 | -12.9765 | -53.4827 | 2024-10-11 00:44:36 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c37c6fae-fcc3-36b4-8d76-e45d88ca8876 | -12.9784 | -53.491798 | 2024-10-11 00:44:36 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b20282dd-4198-3984-8838-a9e3b78e9985 | -12.9667 | -53.484798 | 2024-10-11 00:44:36 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8553698b-6466-3923-b278-4c856e83f36c | -12.9686 | -53.4939 | 2024-10-11 00:44:36 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 68ba6a82-fed0-325b-a923-96b5334a0059 | -12.8752 | -53.437901 | 2024-10-11 00:44:38 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f301f69c-5a3a-3dc6-9ea6-d5f29ccd40d5 | -12.8771 | -53.446999 | 2024-10-11 00:44:38 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3ed00356-1df6-387b-b1f3-90d549209df5 | -12.8636 | -53.431 | 2024-10-11 00:44:38 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 59fe8a60-ef4a-39b5-bc54-1c48b055da2c | -12.8654 | -53.439999 | 2024-10-11 00:44:38 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5673a2d2-9efd-3774-b406-be6d9dae11a3 | -12.8673 | -53.4491 | 2024-10-11 00:44:38 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6b2ff6bb-772c-3921-88e7-8e027ceefc2d | -12.8692 | -53.458099 | 2024-10-11 00:44:38 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5a755ee6-4b47-3687-8a95-d7e059285fe8 | -12.8711 | -53.467201 | 2024-10-11 00:44:38 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 20a6938a-6e57-3d4c-be39-85e56e38d435 | -12.8556 | -53.442101 | 2024-10-11 00:44:38 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 86dedd1a-c0b7-3811-bfc6-9e33a158b353 | -12.8575 | -53.451199 | 2024-10-11 00:44:38 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 79fc28d7-7a8a-3508-92ef-5c279070fb01 | -12.8594 | -53.460201 | 2024-10-11 00:44:38 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1f0af36a-e776-376a-8643-d84a20648fe3 | -12.1239 | -50.549999 | 2024-10-11 00:44:40 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a41cc930-5015-39d7-9930-1afb40f1bfdf | -12.4478 | -53.106499 | 2024-10-11 00:44:44 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4be9ac09-fe44-36c1-b821-f7c47e98fb72 | -12.4496 | -53.115101 | 2024-10-11 00:44:44 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b33b3a43-75a5-3aa7-9355-27873e166620 | -12.4434 | -53.134399 | 2024-10-11 00:44:44 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c3fe638e-a0c6-3fb9-af25-b83244055836 | -10.9342 | -47.9245 | 2024-10-11 00:44:50 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| eb899684-7fef-37a9-864d-16cc342b4549 | -9.5229 | -42.979 | 2024-10-11 00:44:53 | METOP-B | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 39128f9d-4cd0-3fb8-89b9-b68f83a3a89f | -9.5267 | -42.994099 | 2024-10-11 00:44:53 | METOP-B | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 8ab83443-b095-3fe4-a43e-7164779f2ebf | -9.5132 | -42.9814 | 2024-10-11 00:44:53 | METOP-B | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 7f85e35d-93aa-38a6-9232-0afd0ef3457b | -9.517 | -42.996498 | 2024-10-11 00:44:53 | METOP-B | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| eb2a9916-2064-3bdd-bd39-b518a022ac44 | -10.4695 | -46.770699 | 2024-10-11 00:44:53 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| eab9db0e-e3a3-3a79-a0ed-e0685b654501 | -10.4715 | -46.779301 | 2024-10-11 00:44:53 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8e3ab731-becb-3db5-b003-a24ec6ac908f | -10.4597 | -46.773102 | 2024-10-11 00:44:53 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e4915a98-07bf-33ac-8cf6-b772f734ee90 | -10.4617 | -46.7817 | 2024-10-11 00:44:53 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README5.md)
