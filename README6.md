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
| 8c7885c2-13d3-3b1b-8aa5-e015925dce66 | -3.57421 | -39.78449 | 2025-11-20 04:10:00 | NPP-375D | MIRAÍMA | CEARÁ | Brasil | 2308377 | 23 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 703722a2-d88d-3cf6-acb9-912f32100f5e | -3.61302 | -43.76004 | 2025-11-20 04:10:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6a488d8f-b64b-3958-88ae-ef515b627713 | -4.6812 | -43.21902 | 2025-11-20 04:10:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f0c69b5f-ebb1-304f-9246-c03ba133c068 | -5.64815 | -37.42471 | 2025-11-20 04:10:00 | NPP-375D | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 76f9aa45-9293-3bc2-81dc-4b8f5ad7927e | -2.50913 | -47.80944 | 2025-11-20 04:10:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| cbb6a750-df3c-3f1b-8f8d-0aac574d6b84 | -4.101 | -50.0646 | 2025-11-20 04:10:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 15a81ae3-5573-3ca2-81b4-fbbce6f66c78 | -5.81205 | -35.55397 | 2025-11-20 04:10:00 | NPP-375D | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6e6bbd1e-84b8-38c7-96f3-0f851359e2de | -4.66138 | -44.10907 | 2025-11-20 04:10:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 648888ac-2c93-3604-aaa3-5f0afe90c2a3 | -4.67775 | -43.21847 | 2025-11-20 04:10:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d4cc98b3-0bac-3841-9866-89b825ccc3ac | -5.99585 | -35.39394 | 2025-11-20 04:10:00 | NPP-375D | VERA CRUZ | RIO GRANDE DO NORTE | Brasil | 2414803 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c1240bc0-4fca-395b-9028-941314e40959 | -5.4954 | -39.1667 | 2025-11-20 04:10:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 407d3122-22d7-3ee2-8863-6a6648dc9348 | -4.66738 | -43.2168 | 2025-11-20 04:10:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bc1adc5a-75ff-343f-913c-2df09fdb17c0 | -4.60419 | -45.46291 | 2025-11-20 04:10:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6d6111c6-ffed-3aa8-af47-5f5af73e53c4 | -2.51303 | -47.81507 | 2025-11-20 04:10:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 1af9bb14-214c-3387-99d3-5f48ea1946e0 | -2.1291 | -46.19407 | 2025-11-20 04:10:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9dbfbb40-9aec-3f41-b5fe-cfac8ccfa6c6 | -4.14597 | -43.67541 | 2025-11-20 04:10:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b855f0b5-3c4c-32a5-858a-3a194dbc48c6 | -3.59134 | -40.96438 | 2025-11-20 04:10:00 | NPP-375D | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c75f060f-2bfb-3e40-92cf-de476d3b6e6a | -3.67218 | -50.1631 | 2025-11-20 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6630002d-289d-3c5c-8606-c1ec8685c937 | -3.16691 | -40.28587 | 2025-11-20 04:10:00 | NPP-375D | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5886a377-9f1a-3f8d-b211-43583a0e7dba | -2.97947 | -44.58047 | 2025-11-20 04:10:00 | NPP-375D | CAJAPIÓ | MARANHÃO | Brasil | 2102408 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e34eca4d-b89d-3a25-ae66-3c270f56d4b4 | -3.04825 | -40.11468 | 2025-11-20 04:10:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| db3ae15f-5224-3cd2-af3f-2a85d3fb65fe | -4.10688 | -50.06223 | 2025-11-20 04:10:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 874af3e7-3093-356a-82d9-d210ec4dd096 | -2.51463 | -47.80525 | 2025-11-20 04:10:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 24b25f66-a0a4-30aa-997f-6b99ff82e270 | -10.36581 | -48.89822 | 2025-11-20 04:12:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 114ae4e8-cdcb-30bf-8452-de68ada406e3 | -10.48951 | -49.37026 | 2025-11-20 04:12:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 92f5a295-6b7b-36e1-99eb-ea1806571a6a | -6.23327 | -48.06637 | 2025-11-20 04:12:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3285ebc1-3b3a-36ca-92f1-86542a0c1b5c | -11.25725 | -48.49357 | 2025-11-20 04:12:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8aa0824f-5af0-3ecd-b1d9-29d00f852bf1 | -7.14658 | -44.91992 | 2025-11-20 04:12:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d4ba9c54-712f-369b-9862-4affeb902836 | -11.00763 | -47.68468 | 2025-11-20 04:12:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6afd9ae6-3720-32ca-abbd-5e1bf8d2dc92 | -10.88758 | -54.14332 | 2025-11-20 04:12:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ed5718b4-20c9-3816-91b0-a0c717d658e5 | -10.36742 | -48.90501 | 2025-11-20 04:12:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 67099cd6-3175-3e35-a718-071a98bd6332 | -11.26575 | -48.49504 | 2025-11-20 04:12:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e8b72587-4d29-393b-8a0f-4ab917db6152 | -11.41335 | -48.44289 | 2025-11-20 04:12:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 944324c4-b816-3c83-a9ad-e08e9c7a7a88 | -11.2608 | -48.4983 | 2025-11-20 04:12:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7febe587-9d6c-3264-aef6-f1cb401274e6 | -11.49349 | -48.23555 | 2025-11-20 04:12:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1bccdcdd-2c04-368d-8685-1e44ae597531 | -10.35854 | -48.90351 | 2025-11-20 04:12:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| a977acf8-2bf7-3658-9c91-496e96ccbe1f | -11.50181 | -48.55713 | 2025-11-20 04:12:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5acf1efa-0b97-3848-8132-e0ad3f5216b4 | -6.23404 | -48.06185 | 2025-11-20 04:12:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 12f2f27b-dbe0-3126-a10f-9f8e8bcb4f3d | -10.53716 | -47.70959 | 2025-11-20 04:12:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 89064833-0100-3129-8e2c-fe4c0fcf68a6 | -11.50248 | -48.23328 | 2025-11-20 04:12:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 185e018d-e63a-3073-8a1e-c423d8ad83fa | -10.88658 | -54.13873 | 2025-11-20 04:12:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 509ea17b-a7a0-3fae-ba1a-82b348a82307 | -8.10716 | -55.08738 | 2025-11-20 04:12:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d3e2af8c-196c-33d5-ab2d-569b30da0d1f | -11.48866 | -48.2386 | 2025-11-20 04:12:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 483968c1-d173-3e75-aba1-af763d600043 | -11.41756 | -48.44368 | 2025-11-20 04:12:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bc7c8b8e-a3f8-3e03-a168-ef2588dbce78 | -8.11402 | -55.08847 | 2025-11-20 04:12:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6656f065-6e7f-3058-a1fd-6afff54cbd24 | -10.36505 | -48.9026 | 2025-11-20 04:12:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 18f414a6-5b20-3193-8263-d435d6e88a42 | -7.55289 | -47.5815 | 2025-11-20 04:12:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f456a7e6-460c-3fa4-a7a5-f7b202f48586 | -10.38594 | -49.92963 | 2025-11-20 04:12:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bb30b799-1059-3396-9e3b-e45a739252c3 | -10.52951 | -47.58496 | 2025-11-20 04:12:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0b781d5b-8bf3-3b78-a433-8c9c3ce89584 | -10.48582 | -49.36473 | 2025-11-20 04:12:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e0e58650-0019-34ad-b62c-c923af1e5fc0 | -8.45598 | -47.93683 | 2025-11-20 04:12:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 13484e6d-efb2-3467-a4d0-962c46ee851a | -10.38142 | -49.92754 | 2025-11-20 04:12:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ee98fa87-62dd-3bda-a02c-c50f5658ffe9 | -11.41662 | -48.44662 | 2025-11-20 04:12:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cbb68a4b-9379-39fd-9161-aa1b3b6fec30 | -7.95191 | -46.88725 | 2025-11-20 04:12:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3dba7f4f-2088-310e-9459-60771dc2d66d | -7.27025 | -48.03114 | 2025-11-20 04:12:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d6126175-2397-30d3-8d99-eff4d064d012 | -10.36138 | -48.89746 | 2025-11-20 04:12:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 20.3 |
| d58bd2d0-b947-3956-b87c-0e10e97d0eb9 | -11.41735 | -48.44265 | 2025-11-20 04:12:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 27bc1b10-60e6-3380-80cc-13cd90f52b20 | -10.36353 | -48.91133 | 2025-11-20 04:12:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 4f3b3d19-8d89-3dc7-8716-135729ef7c7e | -10.35542 | -48.9054 | 2025-11-20 04:12:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1639c38f-ff50-3edc-8688-3c5ef4359d84 | -10.36061 | -48.90184 | 2025-11-20 04:12:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 20.3 |
| c6a6e48b-2459-36a0-bd8f-e5b3355b81b1 | -6.15134 | -53.02064 | 2025-11-20 04:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 76b70899-7af1-3fb2-a145-ea21413ae788 | -12.52184 | -46.81013 | 2025-11-20 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 960c5cf3-2c25-3933-88dd-b5cc8b80da2e | -10.36662 | -48.90938 | 2025-11-20 04:12:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| d21cd1f9-959c-35ce-b21d-c3be9b25f2be | -10.36218 | -48.90865 | 2025-11-20 04:12:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| acc91d36-648c-3dc0-bc7e-152663eda71f | -6.23483 | -48.05727 | 2025-11-20 04:12:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c24b8eee-dccb-3959-811d-3090f9d5f0f7 | -10.88041 | -49.54618 | 2025-11-20 04:12:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| db114acb-0e02-3c68-9f82-fe11a094db38 | -11.41241 | -48.44584 | 2025-11-20 04:12:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b393b290-6e2c-365d-8807-a2470f95bf98 | -6.48144 | -47.50511 | 2025-11-20 04:12:00 | NPP-375D | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6baa1347-846f-3379-80ce-090c969d575f | -7.55356 | -47.57753 | 2025-11-20 04:12:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0aee8cc6-29d7-3e33-9a37-905ad2e58670 | -8.45239 | -47.932 | 2025-11-20 04:12:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d057a07d-d840-3bed-b9f8-bc31ce1d25a3 | -10.79128 | -47.96784 | 2025-11-20 04:12:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 67393b5f-7ae2-3fe1-8473-10fe3f9095a7 | -11.2615 | -48.49434 | 2025-11-20 04:12:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 18e7d565-0927-39ef-8e14-d17afb87ed42 | -11.56141 | -48.46074 | 2025-11-20 04:12:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c70a2598-f599-324e-8f1a-656224262cc1 | -6.95829 | -47.08348 | 2025-11-20 04:12:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 82a402ab-e829-3c35-92d9-03ef7865a29d | -6.57281 | -47.36718 | 2025-11-20 04:12:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d91ab16c-190e-3942-93a2-7372ff87858c | -11.5607 | -48.46466 | 2025-11-20 04:12:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b502e2d1-482b-3a50-a4d4-bc91bf44627d | -7.95593 | -46.88805 | 2025-11-20 04:12:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a9342f74-b22f-3cc5-9ea8-288d6ac4b857 | -10.36377 | -48.89993 | 2025-11-20 04:12:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 20e24b1b-0680-35f3-af11-37018f5b1586 | -10.36429 | -48.90697 | 2025-11-20 04:12:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| e81c91b9-6bb8-3bf5-be48-18a6543c05ad | -6.14512 | -53.01941 | 2025-11-20 04:12:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 355a724f-5ca8-3d11-b457-51c8cea3b9de | -10.48563 | -49.36782 | 2025-11-20 04:12:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 14a2c88a-f86b-3fd0-8202-2086fec78876 | -10.48495 | -49.36946 | 2025-11-20 04:12:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4ac9e07f-24a4-33ce-9c2d-d0462926c895 | -6.93074 | -46.00262 | 2025-11-20 04:12:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 66dad83a-bdd3-33ee-811b-e7acbac3a9c2 | -10.35934 | -48.89916 | 2025-11-20 04:12:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 1705cb06-6a71-3f55-adab-825a1c9c24e7 | -10.10241 | -49.59262 | 2025-11-20 04:12:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7784e8f4-3d6b-3e60-942b-5efc3e8c88d1 | -6.48212 | -47.50108 | 2025-11-20 04:12:00 | NPP-375D | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7fd6833c-3c83-33b9-9a3f-f2f3982315c4 | -11.41265 | -48.44687 | 2025-11-20 04:12:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dd93620f-d2ab-3e5d-8fba-390e0ecdf253 | -7.26951 | -48.02993 | 2025-11-20 04:12:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| caa9f4ad-5470-3de0-a20c-bbbd24245ce9 | -6.48576 | -47.50575 | 2025-11-20 04:12:00 | NPP-375D | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 59d90639-e1be-3485-ba2e-2f8b3468f470 | -10.36298 | -48.90429 | 2025-11-20 04:12:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| eb9cdbed-9afe-3914-baee-8566d99f5e58 | -11.49281 | -48.23938 | 2025-11-20 04:12:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 54feda38-4167-3421-986b-0c46f093dd36 | -7.26585 | -48.03041 | 2025-11-20 04:12:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ea5d7532-1712-3a6c-8d15-d747a34b2e6e | -10.54077 | -47.99023 | 2025-11-20 04:12:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 82b1177f-56f8-32f9-90d3-91963c54e5fc | -10.35985 | -48.9062 | 2025-11-20 04:12:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 8c5654a2-ce99-3e54-ad7d-eef407b65812 | -11.41313 | -48.44188 | 2025-11-20 04:12:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f617eaf6-e852-3231-a74c-710a2c06d82d | -9.70793 | -49.93433 | 2025-11-20 04:12:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b72a3ec4-5d77-349e-89e9-cb92e49deecd | -10.66614 | -49.71576 | 2025-11-20 04:12:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ab39db44-4060-3ed1-9fd8-bea2ef5a7e4b | -10.38616 | -49.92844 | 2025-11-20 04:12:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aff2419a-85cd-3bd2-8f0e-2136ffe8ec19 | -8.4517 | -47.93604 | 2025-11-20 04:12:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d9bc418c-6884-3ee9-ab32-49e60bf2d07f | -10.88854 | -54.13837 | 2025-11-20 04:12:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README7.md)
