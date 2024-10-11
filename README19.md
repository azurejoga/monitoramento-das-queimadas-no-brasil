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
| b5290b22-6ac2-3ef7-947d-d8241beb00fb | -4.27079 | -50.96351 | 2024-10-11 00:56:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| 7fb78c38-5477-3857-a398-8f30f5b05cbf | -4.0692 | -51.11522 | 2024-10-11 00:56:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| ae2f94f4-ee79-3489-a898-8efa09002fee | -4.0194 | -51.0066 | 2024-10-11 00:56:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| b187d763-d141-3e06-a3ec-aacb242812a6 | -3.91856 | -51.22034 | 2024-10-11 00:56:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f6083183-79f0-3062-808e-651007b97ab7 | -3.89746 | -52.26951 | 2024-10-11 00:56:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 866f6735-9a9c-3214-8fba-775dbbe0611f | -3.85066 | -51.25673 | 2024-10-11 00:56:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 0980b797-b46d-3bbc-aed1-cd0d512c0f59 | -3.80479 | -52.26495 | 2024-10-11 00:56:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 39c11953-448d-38ef-8989-d3831adc1064 | -3.70556 | -51.07857 | 2024-10-11 00:56:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d9d4a4c6-33d0-380d-b7ec-21bb7935f500 | -3.69225 | -51.12088 | 2024-10-11 00:56:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 15d35e92-f31f-36cc-baf6-625c7c94e7de | -3.69091 | -51.11097 | 2024-10-11 00:56:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 493323b3-748e-3fee-b67b-d847724a2b6b | -3.68555 | -51.07124 | 2024-10-11 00:56:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 99ae2408-01a9-3135-aa16-70e4bd7e7751 | -3.68552 | -51.11808 | 2024-10-11 00:56:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| ba8a333b-1a9b-33f7-9137-91b706b31413 | -3.67997 | -51.07838 | 2024-10-11 00:56:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| a88422de-1529-365c-9394-a245043a49b6 | -3.6786 | -51.06852 | 2024-10-11 00:56:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| a0475575-4d2c-3a05-92a0-85df84d3942e | -3.67617 | -51.11937 | 2024-10-11 00:56:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7ea21823-51c6-3d9a-9a7b-5eade8ea38a7 | -6.40958 | -51.73244 | 2024-10-11 00:56:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 32e9e5fe-894c-38ed-8f10-14b2695bfb10 | -6.408 | -51.72071 | 2024-10-11 00:56:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 6662ad42-c938-3e84-b747-8a3caf9196b5 | -5.617 | -51.17016 | 2024-10-11 00:56:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 4ab06116-087f-331e-b12b-039099091a42 | -8.86177 | -53.01369 | 2024-10-11 00:56:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 6387f626-bb54-3e86-98e1-0914d95fb3ee | -8.85973 | -52.99773 | 2024-10-11 00:56:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| afe0485d-3eae-37e5-afae-25f51ed23223 | -9.74681 | -53.15211 | 2024-10-11 00:56:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| fc4b0a2e-54de-3c05-b1c1-e18607ab86fd | -9.71877 | -52.8268 | 2024-10-11 00:56:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 1df95517-019d-34bf-a24a-6878bd9e7784 | -9.71002 | -52.83321 | 2024-10-11 00:56:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| cacccaf9-8b30-33ed-815e-300a1947484e | -10.70762 | -53.03812 | 2024-10-11 00:56:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 33.5 |
| aa07af4f-1857-3fba-9e46-e4cb6a59d4a4 | -10.6957 | -53.03948 | 2024-10-11 00:56:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 60.0 |
| ed5dbdbb-3dfd-395b-a356-46f9d36c8b21 | -10.69358 | -53.02245 | 2024-10-11 00:56:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 112.2 |
| 31cd9daa-9832-377a-8f15-d5eab08674f6 | -10.60916 | -52.88695 | 2024-10-11 00:56:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| bfb4524c-d0b9-3f39-b840-3ec5baa28467 | -10.2684 | -52.18061 | 2024-10-11 00:56:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| c9c01315-6fd5-3b20-80a2-f1e711d9b29e | -10.26537 | -52.17278 | 2024-10-11 00:56:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| ca7a84e2-5de1-3696-8304-fdb49bf859da | -2.98484 | -52.91528 | 2024-10-11 00:56:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 141.6 |
| ee9e5f51-47d9-30a3-81e8-d19062e8dec6 | -2.98312 | -52.90289 | 2024-10-11 00:56:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 244.7 |
| 97acf6ff-0b14-3171-9d66-81effb1f5055 | -2.97443 | -52.91669 | 2024-10-11 00:56:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 41.7 |
| aa869ec4-70d3-3088-ac9d-5363a0fbd7b6 | -2.97273 | -52.90432 | 2024-10-11 00:56:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 157.2 |
| 8147ecf0-4569-3ed2-a3e7-e448372797bc | -2.97105 | -52.89204 | 2024-10-11 00:56:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| c021dd38-89c6-3450-b0b7-2956c815c1aa | -2.96402 | -52.91798 | 2024-10-11 00:56:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 23.9 |
| e078050b-ba9f-3555-a1be-0492075f7b61 | -2.96232 | -52.90558 | 2024-10-11 00:56:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 124.0 |
| 8e3aeafd-1439-38ca-85f3-97cf7c6055fa | -2.96065 | -52.89334 | 2024-10-11 00:56:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| aa365ef0-50d3-32b9-9c54-3d516f16345f | -3.48146 | -52.82283 | 2024-10-11 00:56:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 0a133c5b-9a98-341a-890c-a96b6213a99b | -3.44932 | -52.71962 | 2024-10-11 00:56:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a9832b50-bc53-3d2e-a297-7420df213f1d | -3.33366 | -53.01073 | 2024-10-11 00:56:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d2ab4fcc-6150-3d63-abd3-8ecfa77881e8 | -3.32311 | -53.01202 | 2024-10-11 00:56:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 3d3683e4-2764-39f4-b6fb-75eed2bbd10e | -3.83666 | -53.58778 | 2024-10-11 00:56:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| c28436bb-bc63-380a-bdce-d6dd69b67cff | -3.8345 | -52.3318 | 2024-10-11 00:56:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| f685f7fe-d7c3-35bb-8069-50dac78adb4f | -8.88954 | -54.57759 | 2024-10-11 00:56:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 883cd835-4130-3052-b093-cce92826133f | -3.34204 | -54.61834 | 2024-10-11 00:56:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 52a0c6ac-16a7-3933-a31c-5fa48f2e79bd | -3.57587 | -54.54034 | 2024-10-11 00:56:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 28bba81f-9725-3495-945d-0e08fbe35a82 | -3.25221 | -54.18826 | 2024-10-11 00:56:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 8af580df-4915-387f-ab01-e1ca7f313323 | -3.12168 | -53.73305 | 2024-10-11 00:56:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| c1a42404-a713-30ac-afdc-3518327d4192 | -3.12123 | -53.73925 | 2024-10-11 00:56:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 712ef6cc-81e9-3654-baba-ddbe8a00a295 | -8.4395 | -55.47001 | 2024-10-11 00:56:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 95.5 |
| a826b04f-7961-385c-816f-9c6974074dc5 | -8.29405 | -55.37224 | 2024-10-11 00:56:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 29.4 |
| e26fd400-6e56-31e6-9516-391babb27983 | -8.28812 | -55.37947 | 2024-10-11 00:56:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 85cf37c9-f2dd-398f-89ba-9c1e6e3c8358 | -8.28021 | -55.374 | 2024-10-11 00:56:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 078c0e6d-6503-33d9-aaf1-0cccc22ac922 | -10.3691 | -55.8751 | 2024-10-11 00:56:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 9c007047-4fa5-33d7-817e-567e4ce91cc5 | -10.36609 | -55.8534 | 2024-10-11 00:56:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 29.1 |
| 0d9bbffd-9f94-36fc-a817-68015a4334a7 | -5.18128 | -56.00494 | 2024-10-11 00:56:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| db57bd08-c5c8-3c40-9905-6626c8996db7 | -10.3632 | -55.8554 | 2024-10-11 00:56:05 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| c58a668e-c899-3a1b-8703-4d4c3fd48184 | -10.6171 | -47.704 | 2024-10-11 00:56:06 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 585f2e49-e46d-3529-8d2a-3859aa376f3d | -10.6962 | -53.0354 | 2024-10-11 00:56:07 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 156.2 |
| e47ef3bb-e7d0-3a62-b8da-9e307d916403 | -10.6965 | -53.0147 | 2024-10-11 00:56:07 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 139.9 |
| 75588f89-cd6c-3616-9702-67169882dd2e | -10.7059 | -64.1138 | 2024-10-11 00:56:08 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 67.7 |
| e0e4e258-bbc6-3098-9f09-5b3d4326a6cb | -11.158 | -50.9564 | 2024-10-11 00:56:09 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 30b61c70-66df-3f58-a018-bf4446820b22 | -11.2526 | -50.9675 | 2024-10-11 00:56:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 74e2e6d7-3601-373a-9ffc-22bbb6bb1e77 | -11.2407 | -53.2738 | 2024-10-11 00:56:10 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 0f6f18a1-b8d9-3807-9d6c-b8a82754b08a | -11.2597 | -53.272 | 2024-10-11 00:56:10 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 1a3a1ef1-f4c3-3dcc-b12c-6f04e77ec3a0 | -11.2912 | -50.9208 | 2024-10-11 00:56:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 59.0 |
| d5d9ad24-4600-36c9-8d77-8c3bf5beb87b | -13.368 | -44.7676 | 2024-10-11 00:56:21 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 69.8 |
| aa2a5141-235e-3f5c-add5-ad49faf8bcf1 | -13.7346 | -60.6079 | 2024-10-11 00:56:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 8da25c2b-436b-3b3d-9d6a-1d2846268a1b | -15.429 | -60.0156 | 2024-10-11 00:56:34 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 0868f83f-5837-3bb6-8712-8fa736115984 | -1.99498 | -47.263 | 2024-10-11 00:58:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| d2681686-6c7a-3ca1-81c3-8378f4c6ba24 | -1.99358 | -47.2531 | 2024-10-11 00:58:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 086e47e4-d678-3cf1-a528-662c8b12dd76 | -1.9074 | -47.88407 | 2024-10-11 00:58:00 | TERRA_M-M | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 98093d1e-d1ef-3e43-a736-6b6b0e3090b6 | -2.24062 | -48.02589 | 2024-10-11 00:58:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 76d75e75-402b-35fe-9104-542458cbbd2d | -2.23934 | -48.01672 | 2024-10-11 00:58:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 143e57f2-6e7d-31c3-a680-ee55279a17a1 | -2.23161 | -48.02719 | 2024-10-11 00:58:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1a3c131e-dd39-3f9b-b038-6d168e6c48cd | -2.46972 | -50.25956 | 2024-10-11 00:58:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 46d3a1bf-19e3-3016-a79b-c2b4b5263b2f | -2.38885 | -50.41249 | 2024-10-11 00:58:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 3d9e3f5f-d435-3bb9-84fe-0e7e286622de | -2.37741 | -50.33075 | 2024-10-11 00:58:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 272e3e79-c3b1-3938-a325-4f62fc6a3c40 | -2.37615 | -50.32169 | 2024-10-11 00:58:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 1c0027a8-6b93-33ea-a1e3-2fdf6eaf60ea | 2.4857 | -50.82004 | 2024-10-11 00:58:00 | TERRA_M-M | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f3d24d87-396b-3358-aaf9-780417d0c99c | 2.48446 | -50.82888 | 2024-10-11 00:58:00 | TERRA_M-M | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 8.6 |
| edf0b29b-e9d1-3677-8062-bf9fdc860575 | 2.47685 | -50.81879 | 2024-10-11 00:58:00 | TERRA_M-M | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f37d124a-89f7-31b3-a799-14eb4ca886c9 | -1.9774 | -51.09868 | 2024-10-11 00:58:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ad51bdb8-4c16-3647-9f4e-2f8c43aa9644 | -1.493 | -51.06131 | 2024-10-11 00:58:00 | TERRA_M-M | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 23847d99-fc69-3fdd-8135-4a2e9df04260 | -1.49169 | -51.05188 | 2024-10-11 00:58:00 | TERRA_M-M | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 72374d11-124a-36c2-8281-79e415c088d3 | -2.64322 | -51.70798 | 2024-10-11 00:58:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 5bb1b425-3873-31a2-a469-26933f372f08 | -2.25375 | -50.70002 | 2024-10-11 00:58:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| dd63f057-7ced-3eca-bdbf-8de9694fd0f3 | 2.34518 | -51.56086 | 2024-10-11 00:58:00 | TERRA_M-M | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 7.4 |
| ad140f16-7ed1-3df7-9e04-ea55867cf467 | -0.38147 | -52.07083 | 2024-10-11 00:58:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 35ec071d-8279-301b-81cc-a290c6d683c6 | -0.06579 | -51.65771 | 2024-10-11 00:58:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 09c7d075-f688-3fd7-8820-b47227002eec | -2.84341 | -52.94054 | 2024-10-11 00:58:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 6c50c87b-4d58-332b-9950-b8d627aef673 | -2.78357 | -52.49587 | 2024-10-11 00:58:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 3f189637-c455-3509-820f-d731317dfa06 | -2.782 | -52.48426 | 2024-10-11 00:58:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 450.4 |
| 7c2c4ba6-6dd3-30e6-8031-2bbe865bad57 | -2.78045 | -52.4727 | 2024-10-11 00:58:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 27f131c1-0203-3fad-9f22-9d12f56ade6f | -2.77294 | -52.49179 | 2024-10-11 00:58:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 1769543b-86b5-3706-9acf-c5faa6e71375 | -2.77195 | -52.48566 | 2024-10-11 00:58:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 98fa5bee-8e6c-3e82-977c-8950279871f3 | -2.77131 | -52.48023 | 2024-10-11 00:58:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| f23343b7-885a-33db-8313-fde46dc78c38 | -2.67682 | -53.34778 | 2024-10-11 00:58:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |
| 8b83c904-2b1b-30c0-87fc-464c490e57f9 | -2.66795 | -53.3625 | 2024-10-11 00:58:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 925c3982-2506-30ba-bd62-c3e7f52e4db4 | -2.66613 | -53.34926 | 2024-10-11 00:58:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 124.4 |


[Clique aqui para ver as próximas entradas](README20.md)
