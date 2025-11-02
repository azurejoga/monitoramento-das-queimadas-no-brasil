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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 104edfc4-5770-368c-afd5-bac88da268f8 | -4.46557 | -50.50364 | 2025-11-02 04:48:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f2d6522c-b5e1-3c08-8e4a-d70c2214c529 | -1.55754 | -55.42686 | 2025-11-02 04:48:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b95d27da-33e3-3c52-a876-4c5614dcd59c | -3.24317 | -50.78897 | 2025-11-02 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8a356bae-b93c-3a8f-b372-b705034e8414 | -3.42495 | -50.23691 | 2025-11-02 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a03fa4d-68ed-3202-aac3-e34053446a79 | -3.5167 | -49.71878 | 2025-11-02 04:48:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f1dc5622-63d2-3b93-9bda-055d59874d21 | -5.52294 | -41.09735 | 2025-11-02 04:48:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 283a8437-3794-37b6-8363-5dcd8649ce19 | -3.29301 | -52.95799 | 2025-11-02 04:48:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5fe80ff-ea43-326d-b864-036cd55eaf9e | -3.41913 | -49.99907 | 2025-11-02 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf73f65c-543f-314f-a2c8-b6caea9c6f45 | -3.14692 | -49.42494 | 2025-11-02 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6dbde216-bc1e-341e-9ea9-2995825ed2a1 | -3.9599 | -49.29413 | 2025-11-02 04:48:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a2a13cd-5ba7-3566-bbf7-d9048569dfca | -3.72686 | -51.70218 | 2025-11-02 04:48:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 841d7c9e-5cfa-39cf-bf65-8197ad334c3f | -3.55778 | -54.57721 | 2025-11-02 04:48:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| f51f6468-9ef8-3d9f-af43-8e3bca77b3b8 | -4.6422 | -38.57535 | 2025-11-02 04:48:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 53e0106e-df6a-38a9-b7ed-d60dae470db1 | -4.29873 | -45.89973 | 2025-11-02 04:48:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3f018abd-39e9-3a76-811e-96fcb7dd20e4 | -3.07867 | -51.24871 | 2025-11-02 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bfa062f4-1fce-3d99-bc6b-ba4019329a6f | -2.63135 | -47.30055 | 2025-11-02 04:48:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a2fa01d-6b69-34f5-b032-39bc37af133b | -2.37802 | -47.72105 | 2025-11-02 04:48:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 87dace1b-8687-337c-8642-e38820284c13 | -3.99912 | -47.73161 | 2025-11-02 04:48:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 145b77ce-ddcc-3d06-b91b-de7a7211b50d | -0.68822 | -52.36994 | 2025-11-02 04:48:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 71036bdb-3c41-37cc-86b0-1add6fda3bfa | -3.72034 | -45.55361 | 2025-11-02 04:48:00 | NPP-375D | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 0f1a3b79-5555-32eb-8dd4-c0237612d8d0 | -4.30739 | -45.89606 | 2025-11-02 04:48:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7eb10c98-b7d8-3a91-9028-7c686ad0d551 | -4.37568 | -49.74155 | 2025-11-02 04:48:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4ca23fca-0745-3b1b-9a25-45ae6fe8f214 | -5.07231 | -43.67171 | 2025-11-02 04:48:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f4ed76e0-3969-3b84-bb8c-b85ecd94fe7d | -7.19628 | -44.26889 | 2025-11-02 04:48:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 17ad481c-e089-3eae-860a-b9ae73944f28 | -5.52593 | -41.10411 | 2025-11-02 04:48:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f012841b-0185-3858-9dbb-0858b5690444 | -2.83559 | -49.40576 | 2025-11-02 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a04a6884-b24f-3109-ace1-dd8b0fcd8b9d | -4.00268 | -47.73215 | 2025-11-02 04:48:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 26a1b5b3-6f77-385b-a8a8-6e12d3b23319 | -3.47471 | -53.13165 | 2025-11-02 04:48:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a2f1dc3f-efee-323c-b02b-0c66792609ad | -4.13472 | -51.1391 | 2025-11-02 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 36eacd4c-9cfe-3af1-88f6-65195b3cb226 | -2.92937 | -51.46421 | 2025-11-02 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4c40f3f1-cc7a-383a-aab2-2dfc4d9141de | -4.63574 | -38.57371 | 2025-11-02 04:48:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| ba355b05-aca5-3971-b9cb-709d01278cc1 | -3.46474 | -50.22191 | 2025-11-02 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 470a4e03-9035-3c04-900b-2f522e2a4113 | -4.07554 | -50.36075 | 2025-11-02 04:48:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1b5b38ce-2c54-3ed9-a28d-0300e66e51a5 | -4.29475 | -45.8992 | 2025-11-02 04:48:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff46a45b-6d4a-3ff2-850b-829b659028b1 | -3.42325 | -45.91206 | 2025-11-02 04:48:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ef294aeb-5e06-3d4c-9676-61c5f41f8bb0 | -4.14026 | -51.14714 | 2025-11-02 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8eaac204-f115-34d2-beff-bdce34133714 | -3.15894 | -50.829 | 2025-11-02 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4448f1c3-90c0-3dee-88cb-794c069f7b99 | -3.8587 | -49.91509 | 2025-11-02 04:48:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 505985ab-218c-3960-8f2a-d62be259bf93 | -4.30082 | -45.89853 | 2025-11-02 04:48:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a75b8fcd-fd46-3013-801e-4da42d3023ed | -3.2454 | -50.79642 | 2025-11-02 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 11e237eb-b0da-3341-ab48-b5ac187b2d1f | -7.30288 | -41.57508 | 2025-11-02 04:48:00 | NPP-375D | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| dfd632a7-e0ab-3dfc-8e65-8f41e3884840 | -4.64302 | -38.56926 | 2025-11-02 04:48:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 34de186d-8c73-346c-8896-0e52d899f0b7 | -1.42084 | -55.23799 | 2025-11-02 04:48:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 527a8852-ec94-36a1-be13-5dd3d3feb292 | -5.52696 | -41.09669 | 2025-11-02 04:48:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| de88007a-d483-3853-bae6-d00c35196ed7 | -3.50869 | -54.37396 | 2025-11-02 04:48:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a40d38da-09e9-357f-9abb-3f1f67eb3816 | -6.72074 | -44.23455 | 2025-11-02 04:48:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d8fb9083-f2f8-3541-8792-452be05a8bed | -3.04465 | -51.2254 | 2025-11-02 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50604299-fa63-3420-8fc2-3b7463a03597 | -2.82835 | -49.40822 | 2025-11-02 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f1938143-3bf4-3467-8155-b441eb011068 | -3.07756 | -51.16947 | 2025-11-02 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8d3faa5c-1e8a-3532-882a-1e28cfebae6a | -3.01757 | -53.96989 | 2025-11-02 04:48:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 707c19f4-778d-323e-8a08-e524f384f8a9 | -3.32686 | -52.56408 | 2025-11-02 04:48:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d7d34d51-a168-3f04-8d93-5c69fbdbcfc2 | -3.14181 | -50.44743 | 2025-11-02 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3eddbfbc-dcf0-3f66-bae3-4e2436472933 | -3.82402 | -52.36018 | 2025-11-02 04:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f80ee22a-a3bc-3138-a4d3-e67b803fb78a | -4.14359 | -51.14765 | 2025-11-02 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 42d1ab78-14f6-3eec-a452-1a97d2826b71 | -3.22825 | -50.58465 | 2025-11-02 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd026c66-fe63-3277-9440-e69873a7ea89 | -3.24152 | -50.79937 | 2025-11-02 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8391625b-5b43-3b83-af81-36099de83a5b | -2.27077 | -47.85796 | 2025-11-02 04:48:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a36b48a-4fff-3baf-9eb2-d958f7720c4e | -2.6284 | -47.29594 | 2025-11-02 04:48:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c24380f3-2fac-318f-8454-026fb49910d3 | -1.26327 | -53.86058 | 2025-11-02 04:48:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ca6ee614-e6f9-3b38-af9d-e17a489826c2 | -4.63722 | -38.56353 | 2025-11-02 04:48:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4be65a0a-a957-36dc-a17c-e6ea62369083 | -5.68075 | -46.42986 | 2025-11-02 04:48:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b3f1ec7e-1cbc-36f1-b265-2c5e065ca051 | -4.6793 | -44.61892 | 2025-11-02 04:48:00 | NPP-375D | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8685ca9f-7d99-3f5b-8838-75dfd96f68d6 | -7.1956 | -44.27354 | 2025-11-02 04:48:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5ef7e563-9b13-31ab-b12e-5af50e928e2d | -3.45117 | -45.57634 | 2025-11-02 04:48:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0f35cd9c-81bd-3b08-ab07-f263ad4277cd | -4.35421 | -49.11946 | 2025-11-02 04:48:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2e3f6695-51d7-395c-a0bd-3719d256000c | -2.44701 | -49.03559 | 2025-11-02 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 927c1d7c-d701-3261-9eaf-2a686c71813d | -2.98698 | -48.7079 | 2025-11-02 04:48:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 997e8f10-6e1b-3f46-9834-808ee6955298 | -2.83504 | -49.40926 | 2025-11-02 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b0910bce-0335-31c3-81f9-e39606b3c262 | -3.47396 | -49.92574 | 2025-11-02 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc013b53-8ea3-3f9c-83e2-6caa0afcc818 | -3.14412 | -49.42091 | 2025-11-02 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 981ef3a9-4ed3-33fe-a421-dfd4c407391a | -2.72225 | -48.34893 | 2025-11-02 04:48:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4559655d-9bce-30b6-92be-2d598327eda0 | -5.09786 | -46.16784 | 2025-11-02 04:48:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85b3be1d-c35e-3f23-9b62-ed05d43be4c4 | -2.37863 | -47.71718 | 2025-11-02 04:48:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a1dc865a-a4f8-3444-9aac-e1ab3b8cdf99 | -3.89401 | -52.09648 | 2025-11-02 04:48:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1570e35a-4145-392b-97f2-8659560cdfaa | -3.22438 | -50.58758 | 2025-11-02 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e966ef40-8d7e-3393-9959-e5b908ae7d68 | -2.65171 | -48.50754 | 2025-11-02 04:48:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 86138631-36fb-33c8-957f-8e63565a8ab6 | -3.32448 | -51.57351 | 2025-11-02 04:48:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d7404017-4c13-3aaa-ab53-88b7ccbf328c | -3.54043 | -50.17075 | 2025-11-02 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 53bbbf9d-8692-3ef1-910f-cdd2dff6e8d8 | -0.84285 | -48.61717 | 2025-11-02 04:48:00 | NPP-375D | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e24b99ce-2b80-35fa-819d-a3d19052cda9 | -3.93898 | -52.20835 | 2025-11-02 04:48:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2fded343-6a60-3d92-a12c-ff053c5e602c | -4.2976 | -45.89312 | 2025-11-02 04:48:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dec5c7be-1116-37f0-a291-242a2d241495 | -3.5733 | -50.26435 | 2025-11-02 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 27719115-c04b-30f3-87e2-0ae7b0b393aa | -4.2087 | -53.86245 | 2025-11-02 04:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 158ef204-882f-3b23-9959-4f38675c2040 | -2.8289 | -49.40472 | 2025-11-02 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2c7722ea-0eca-3903-9a55-def840eda9ea | -1.5617 | -55.42754 | 2025-11-02 04:48:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84c3ebfb-2293-3e38-bf51-69abdf501e75 | -3.79887 | -53.88007 | 2025-11-02 04:48:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2a7e29d5-1366-3f47-aebb-b7a0502f0e07 | -3.77997 | -55.44644 | 2025-11-02 04:48:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8c6a6f47-647f-3e10-81c0-c7b55838eff5 | -3.28877 | -50.20169 | 2025-11-02 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 562d72e8-5cc5-3c42-a458-cbaf33caf686 | -4.67433 | -44.62243 | 2025-11-02 04:48:00 | NPP-375D | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e2220881-454a-3591-978b-60cd81f46186 | -5.12642 | -45.81925 | 2025-11-02 04:48:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 289484e6-1d89-3467-b910-0561188b5544 | -6.79687 | -42.20183 | 2025-11-02 04:48:00 | NPP-375D | SANTA ROSA DO PIAUÍ | PIAUÍ | Brasil | 2209377 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 8407149c-c5a4-3b0d-8bf1-337e6489942f | -3.01585 | -49.44066 | 2025-11-02 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| bae6b53f-2050-3977-9a94-ba34c250f6e4 | -4.13962 | -48.81502 | 2025-11-02 04:48:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b5fac12-321b-350e-8476-e30ff241913d | -5.12956 | -43.37549 | 2025-11-02 04:48:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d1577ac7-1f15-3ad6-ab67-32365049556f | -3.42793 | -45.90771 | 2025-11-02 04:48:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0361d80d-9266-334c-a5a3-2791611e57fd | -3.56889 | -50.27074 | 2025-11-02 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 30937404-2f08-3cc1-aabe-5f50511e2711 | -3.23985 | -50.78846 | 2025-11-02 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2e459d96-8d2a-32eb-89ce-7acf8e0924b9 | -2.34095 | -47.54358 | 2025-11-02 04:48:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 553725f5-d51f-33d5-83f5-56d1c850a9fd | -3.4244 | -50.24036 | 2025-11-02 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6963715d-737a-3361-96f9-d03a15d62c87 | -3.50413 | -54.37803 | 2025-11-02 04:48:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README17.md)
