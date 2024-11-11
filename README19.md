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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c2f4b0f9-7cda-31a7-bbd2-ab103e645233 | -17.593599 | -57.505798 | 2024-11-11 01:33:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 22520783-19a5-3610-980f-e6dcc3dd4460 | -17.625601 | -57.509499 | 2024-11-11 01:33:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6fc4db07-3ec6-32d1-bfd9-15797350b375 | -17.2693 | -57.494499 | 2024-11-11 01:33:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f18aac66-eb99-35cf-8173-a0089d868f5e | -17.5907 | -57.494202 | 2024-11-11 01:33:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8dc954df-c8bb-3b18-b3e0-45942d52698b | -15.9826 | -59.340698 | 2024-11-11 01:33:00 | METOP-B | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1ab04805-18dc-32a7-a4a6-447c4fd15545 | -17.243999 | -57.4762 | 2024-11-11 01:33:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 03be718a-c369-383f-9686-d62f41e1af79 | -17.298401 | -57.486599 | 2024-11-11 01:33:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 00444f37-a62a-367e-82eb-040faf53d8a4 | -17.2925 | -57.463001 | 2024-11-11 01:33:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2c820211-867d-3abc-b437-be44f090ce6c | -15.9849 | -59.3503 | 2024-11-11 01:33:00 | METOP-B | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4271c324-3c13-3b08-baba-0a2d8ce5453c | -17.600401 | -57.4916 | 2024-11-11 01:33:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c7ed85e8-8ba4-337d-9f6e-8edfd6acdf18 | -17.6033 | -57.503201 | 2024-11-11 01:33:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f664e02b-b710-3774-b40e-604985f9e101 | -17.592501 | -57.4188 | 2024-11-11 01:33:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 535e09e8-6b46-30e7-8934-82da25b6260b | -13.4861 | -60.665401 | 2024-11-11 01:33:00 | METOP-B | CABIXI | RONDÔNIA | Brasil | 1100031 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c7788542-0fe0-3a19-b935-1d681f6769ed | -17.2887 | -57.489201 | 2024-11-11 01:33:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d427f14c-1c35-3300-bbf9-e4fdae98637c | -17.266399 | -57.4827 | 2024-11-11 01:33:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1e1c1dba-0c97-3a1f-8c68-1e70c9abe0a9 | -17.631399 | -57.5327 | 2024-11-11 01:33:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 371aa683-2dc0-3933-931a-6bb4c5cd5b36 | -16.9345 | -57.647701 | 2024-11-11 01:33:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7216d051-d47b-342b-bfc1-a7f31508a1c0 | -17.5858 | -57.4333 | 2024-11-11 01:33:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 514da1f0-4ba1-3b79-8fdc-063a4c3594e6 | -17.6159 | -57.5121 | 2024-11-11 01:33:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8264bfa7-9e59-3e9f-b78a-c1f220d0d5cb | -3.1097 | -54.2865 | 2024-11-11 01:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| b303881c-b034-33d8-84d8-16ff8655fe3e | -3.2774 | -53.6585 | 2024-11-11 01:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 835edf2f-3ab1-3722-9bd2-a81cd6a7a6db | -4.0293 | -46.9703 | 2024-11-11 01:40:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 79dbb28d-61de-369a-a381-dc48ad4dcae5 | -2.189 | -48.3815 | 2024-11-11 01:40:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 0a98265a-b618-34be-8bcd-49526a96aab4 | -4.0294 | -46.9484 | 2024-11-11 01:40:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 57.7 |
| d01b83f2-b7fa-3180-b1f0-d809fbfbef94 | -3.2428 | -53.0519 | 2024-11-11 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| fc9b31f1-ea9c-39bd-ba7e-98f5af8db33b | -17.6086 | -57.4276 | 2024-11-11 01:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.8 |
| 77d4e320-912c-3353-86be-dbf4dc519e57 | -3.0295 | -50.9815 | 2024-11-11 01:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 101.2 |
| a774cd60-7138-3c1f-bf87-7d4ee5aa862b | -3.1641 | -54.4854 | 2024-11-11 01:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 42bb01a0-6f67-3a2a-ac23-bcfbbc6f8040 | -2.8323 | -49.4325 | 2024-11-11 01:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| aabb2916-47a8-3b6d-b2f7-0c61850eb574 | -17.313 | -57.4834 | 2024-11-11 01:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 87.6 |
| b436f7cb-5d20-373a-ae84-8ebdd18e1866 | -3.0111 | -50.982 | 2024-11-11 01:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 18ea6b66-45ca-3963-898d-34f9c6f32365 | -1.4057 | -52.3758 | 2024-11-11 01:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 116.0 |
| 8651509d-d922-34f4-bcbf-f80efd612b92 | -3.0214 | -53.2404 | 2024-11-11 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 64ebfc8e-2c91-3af5-aae7-b2e7c349b65d | -2.8508 | -49.4108 | 2024-11-11 01:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| b5f8daf8-168c-30be-839f-90f8eb79a16e | -17.2737 | -57.488 | 2024-11-11 01:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.6 |
| e7009cf5-ddbc-3d56-b189-0ef87dac3691 | -3.3836 | -50.1336 | 2024-11-11 01:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| ea28009d-25ab-3da3-845a-36734e19ef5b | -3.0213 | -53.2607 | 2024-11-11 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| a89c4116-209b-358a-95ee-9ba830e4bd1d | -3.2168 | -50.2861 | 2024-11-11 01:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| fe71a19b-d3a4-3168-b81c-3d658e1dbaa3 | -3.2352 | -50.2855 | 2024-11-11 01:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| f4b6fb01-403b-3484-b410-5917fea48acd | -3.4021 | -50.1329 | 2024-11-11 01:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| e440d9d1-7790-3515-b46b-03a231a87831 | -3.1458 | -54.4859 | 2024-11-11 01:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 5486836d-bc95-3ad7-8480-c96a84cbf654 | -3.2603 | -48.7582 | 2024-11-11 01:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 628f95c3-d32c-3d73-9734-c068e8dcbf60 | -2.2504 | -46.5061 | 2024-11-11 01:40:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 6f722dcb-db26-3915-a8b2-3c97eb1a6cd6 | -3.2427 | -53.0722 | 2024-11-11 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| e25fc2eb-d565-397d-b815-38f3113c4ece | -3.3403 | -51.6563 | 2024-11-11 01:40:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| eebeeedf-67fa-35de-8223-5cb52160ce06 | -2.9355 | -51.482 | 2024-11-11 01:40:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 2d81f37e-62cd-3ca6-999a-5b7ba960cc54 | -17.2933 | -57.4857 | 2024-11-11 01:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 147.5 |
| 4516b078-b35e-3501-960f-a382c1b9f3da | -3.0296 | -50.9607 | 2024-11-11 01:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| c562bc18-21c6-302f-a8a6-7485eefdc158 | -3.2773 | -53.6787 | 2024-11-11 01:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| ee53d7c8-bb9a-3057-aae0-040efff99ef0 | -1.3873 | -52.376 | 2024-11-11 01:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 2a7d0a5c-6e43-3eed-848c-808c0afa7daf | -2.2075 | -48.3811 | 2024-11-11 01:40:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 5e573110-abb9-33e3-aae7-1aa5711200cd | -3.2588 | -53.6994 | 2024-11-11 01:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 718f8afa-8706-3bc3-bf05-e62de2204f71 | -3.0324 | -45.8154 | 2024-11-11 01:40:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 1c2fba33-4846-3712-a0b0-d5bca3cf2fb5 | -2.3863 | -50.3299 | 2024-11-11 01:40:00 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 36fe2b16-543e-3e83-8a6c-e27579960ebe | -17.2936 | -57.4652 | 2024-11-11 01:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.2 |
| 3b2f14e5-cd88-35d8-aac1-e70326ef2f5f | -2.8508 | -49.432 | 2024-11-11 01:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 102.2 |
| 936a41bf-63f4-3398-a89e-6865f6b06294 | -3.2244 | -53.0524 | 2024-11-11 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 95876195-11f8-335a-a96a-5bc00c76cd22 | -1.4057 | -52.3553 | 2024-11-11 01:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| f83e7b50-f63c-3992-a496-4efc05dafca1 | -3.2243 | -53.0727 | 2024-11-11 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 17a2ba36-f1fb-346a-a762-f330eccdc827 | -3.6789 | -50.2074 | 2024-11-11 01:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| a96e842a-6062-33b5-a735-5bfd7f1a8eb4 | -2.2504 | -46.5282 | 2024-11-11 01:40:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 6d0f64b0-8f9c-3b54-bea5-efb3d3388513 | -3.1983 | -50.2867 | 2024-11-11 01:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 6415c1ae-eb9a-3633-8e7d-e18ae416e845 | -3.2388 | -45.3818 | 2024-11-11 01:40:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 0e13b6ae-2c58-3778-a396-848d5cfc2d7d | -17.2737 | -57.488 | 2024-11-11 01:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 86.1 |
| f4a45313-fde3-3517-af6b-a3ac183c1683 | -3.2772 | -53.6989 | 2024-11-11 01:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 46d7e3ea-7b76-3b7d-92e3-fa47a20f2ecf | -17.2933 | -57.4857 | 2024-11-11 01:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 144.5 |
| c681d3f1-5d86-309a-a5f5-1b000d47dcf3 | -3.2243 | -53.0727 | 2024-11-11 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| c631d0a7-a0ab-3a19-a638-cf0b575379b6 | -2.8508 | -49.4108 | 2024-11-11 01:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| a3551d29-673a-325d-aaa2-dca25fba539a | -3.4021 | -50.1329 | 2024-11-11 01:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 905c2925-e053-36e3-8d26-455f0bd5372c | -3.0213 | -53.2607 | 2024-11-11 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 17bcb76e-0797-34a5-9de7-37f222f1147e | -3.1458 | -54.4659 | 2024-11-11 01:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| a3c3d8b6-d2ef-3fbb-8e51-cd5917d2fbc8 | -3.9669 | -48.1716 | 2024-11-11 01:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| fd20bc43-289b-3574-9096-3ac043f65dc1 | -3.2388 | -45.3818 | 2024-11-11 01:50:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 83.6 |
| b8a9be0b-63e4-3a1d-b398-5f0a0f154b53 | -3.2574 | -45.3811 | 2024-11-11 01:50:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 8ceae452-f4e1-348b-baa8-ac57b1910c7a | -3.0295 | -50.9815 | 2024-11-11 01:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 96.6 |
| ea9c5988-d1a0-34d0-b982-9789b77f1192 | -2.189 | -48.3815 | 2024-11-11 01:50:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 62675e10-10b6-3ad0-9f53-0ab61d5a9dc4 | -4.0294 | -46.9484 | 2024-11-11 01:50:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 2915e986-9147-3897-8f37-203c643395e2 | -2.2075 | -48.3811 | 2024-11-11 01:50:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 62fa3334-3878-3a5f-9f82-d658bdf9a751 | -3.2603 | -48.7582 | 2024-11-11 01:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 105b6a7b-d6f1-3626-b548-97b3b7e09147 | -15.9793 | -59.3267 | 2024-11-11 01:50:00 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 68.9 |
| ab2b186c-a65d-39ca-a68a-2981c59f9358 | -3.3836 | -50.1336 | 2024-11-11 01:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| d8e7a23d-ee20-3903-83be-a21662211abf | -2.2504 | -46.5061 | 2024-11-11 01:50:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 2942f3f0-45c1-31c8-89d6-d517af80ea53 | -2.2298 | -53.6623 | 2024-11-11 01:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 5c36fc2a-098f-36df-b140-2a53e034b1ef | -3.1458 | -54.4859 | 2024-11-11 01:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 564b06e6-a013-3a55-ab93-f0d30905c94c | -17.2936 | -57.4652 | 2024-11-11 01:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 92.1 |
| 97563726-e2ff-3d0d-a1a0-8fda03a6dc74 | -2.8508 | -49.432 | 2024-11-11 01:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 109.6 |
| 3f406469-fa9c-3ab4-8211-3a4b0c4d9558 | -3.6217 | -50.587 | 2024-11-11 01:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 6909f1ea-e741-3893-9c6f-75f770bd521b | -3.2588 | -53.6994 | 2024-11-11 01:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| d0b51de6-2f7c-374a-a96e-8d5165e26994 | -3.2427 | -53.0722 | 2024-11-11 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| ee1b0e2f-2e76-37f8-ac2b-0cf697f3926d | -4.0293 | -46.9703 | 2024-11-11 01:50:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 57.6 |
| f5ceee66-2565-32a6-bb60-76b1568ad041 | -15.9985 | -59.3449 | 2024-11-11 01:50:00 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 84.2 |
| c7862aec-98b7-3075-826f-f60b18b4515c | -3.0324 | -45.8154 | 2024-11-11 01:50:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 59.4 |
| a6ebbe51-cbf6-360d-855f-4a7aff1b45e7 | -3.2244 | -53.0524 | 2024-11-11 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 1f29f542-fffd-328e-b532-a98dfa66ec55 | -3.9485 | -48.1508 | 2024-11-11 01:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| dffe4681-eb3e-38c0-856e-71ec8cde5e6f | -3.0214 | -53.2404 | 2024-11-11 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 3f734d3d-d435-3fbb-9433-952ee66f6ae6 | -3.6218 | -50.5661 | 2024-11-11 01:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| ab8e14fc-39d4-3360-9116-08a8716c9ade | -3.0296 | -50.9607 | 2024-11-11 01:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 978b3209-5135-3354-94d3-53db4a447642 | -2.8323 | -49.4325 | 2024-11-11 01:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| a7e9308b-48b1-377d-86be-20d03b4e3e93 | -1.4057 | -52.3758 | 2024-11-11 01:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 111.5 |
| 647108c9-37e7-3aa5-85a3-5f47f9b8ac00 | -3.2428 | -53.0519 | 2024-11-11 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |


[Clique aqui para ver as próximas entradas](README20.md)
