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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a8070718-1421-3d54-8cb7-21e08ba053dc | -10.21504 | -44.8214 | 2025-10-27 00:13:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 15.8 |
| bf0af382-7ec9-3722-8616-1a3600d93393 | -7.6858 | -46.33741 | 2025-10-27 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| c81fd007-4682-3f68-99bd-3fa071e13122 | -6.62703 | -46.13217 | 2025-10-27 00:13:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 65aa93e8-a10e-3303-bfe0-7f43236c3a57 | -9.13436 | -51.30665 | 2025-10-27 00:13:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 82dd0966-359b-3b78-a48d-001d61bc15b1 | -6.8505 | -46.28679 | 2025-10-27 00:13:00 | TERRA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f6f2cb82-d543-37d9-8839-b7302969e653 | -6.87259 | -45.1661 | 2025-10-27 00:13:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| d5eac1c8-d6b7-34e8-9edb-48b85a3ed9c9 | -7.75778 | -46.52355 | 2025-10-27 00:13:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 518bd271-c16f-3a93-8371-f56cd49b8d64 | -10.4918 | -44.21801 | 2025-10-27 00:13:00 | TERRA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| b5df0e15-48b9-3d26-a209-f5af79851179 | -9.48209 | -46.85028 | 2025-10-27 00:13:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 45efa016-290f-3e3f-8aca-a2a9307989c1 | -4.80553 | -38.64506 | 2025-10-27 00:13:00 | TERRA_M-M | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 22.0 |
| 1fde16f9-b311-3d49-ae71-201faae85b0a | -10.70006 | -48.06332 | 2025-10-27 00:13:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 64aa23ec-d75f-32d8-9a11-176d77af0f06 | -11.7286 | -50.22494 | 2025-10-27 00:13:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 782e0e05-a0dd-3448-b06e-74e4e3435d42 | -9.5819 | -45.1815 | 2025-10-27 00:13:00 | TERRA_M-M | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b6e46769-f6a4-329e-8345-693144c1a3da | -4.46416 | -43.4244 | 2025-10-27 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 41.6 |
| 6a6a6989-2333-3e78-bb39-61e7999e4088 | -6.16669 | -41.57221 | 2025-10-27 00:13:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 29.5 |
| fe212c2c-1c94-3941-91c0-989ea5324a91 | -6.82815 | -41.20276 | 2025-10-27 00:13:00 | TERRA_M-M | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 1c50d2d6-e0f5-34f8-bd8a-463a7e63e310 | -10.75392 | -44.19525 | 2025-10-27 00:13:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 83.6 |
| b8c570bc-cb99-328e-92ad-4907a0a72530 | -11.42548 | -46.10166 | 2025-10-27 00:13:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 51fb6c65-effa-38e7-b24c-671698987dd2 | -7.86977 | -45.72381 | 2025-10-27 00:13:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ae0e6180-dc4c-3cdf-922d-6ccbc2ad3b74 | -5.82253 | -40.81845 | 2025-10-27 00:13:00 | TERRA_M-M | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 11.6 |
| b15810fd-3ec7-38a7-a01f-95ac31c1b2c2 | -4.44701 | -43.43681 | 2025-10-27 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 876010e4-be52-36ef-80f2-764790c6858b | -4.45064 | -43.66236 | 2025-10-27 00:13:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 23314cd9-9955-3c11-b666-57687c6a25f6 | -5.55063 | -41.40971 | 2025-10-27 00:13:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 7affc9b0-3272-380c-b9d0-5bbb0fb02cc1 | -9.56545 | -44.71882 | 2025-10-27 00:13:00 | TERRA_M-M | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f56e3ed1-c15e-36b0-a541-2f967f82008a | -4.47343 | -43.4231 | 2025-10-27 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 143.4 |
| e39152a2-92af-36ea-a2ce-e5882dc62ba9 | -6.8909 | -43.58216 | 2025-10-27 00:13:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4aab05ef-773f-3052-9597-3bdc60a6e25a | -4.46553 | -43.43418 | 2025-10-27 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 25.9 |
| cad05e4f-6e3a-3f96-b50a-c8f6546fb14b | -8.6507 | -44.76466 | 2025-10-27 00:13:00 | TERRA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| e41e6abe-98a7-3321-b629-52395453767e | -6.13067 | -42.45187 | 2025-10-27 00:13:00 | TERRA_M-M | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| c7736d62-5f7c-3aa2-9a8b-d4fba3f03ed7 | -8.6222 | -41.41447 | 2025-10-27 00:13:00 | TERRA_M-M | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 23378a28-e6e7-390e-b7e1-e31fbb066ed0 | -5.59803 | -41.32077 | 2025-10-27 00:13:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 19.2 |
| 38a975b1-f2aa-3e71-823e-fa21ab2589ea | -10.883 | -45.13654 | 2025-10-27 00:13:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 56fbf8b7-08f2-39de-98fc-8d41f2bf010f | -6.26381 | -41.81784 | 2025-10-27 00:13:00 | TERRA_M-M | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| b29613a5-ba55-3446-8001-1dce193fb08a | -11.29039 | -45.15275 | 2025-10-27 00:13:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| d0093901-0edf-30cc-bb76-22e8317f1471 | -7.59776 | -45.68718 | 2025-10-27 00:13:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| cd4467c6-dc8f-3f22-a152-c4cac6c1ead3 | -4.4549 | -43.42575 | 2025-10-27 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 53c5f0e0-dc9e-39a1-9c45-071ad6800b0d | -6.99758 | -46.97807 | 2025-10-27 00:13:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 737e02cd-a851-3c4a-942d-141c2fd87021 | -6.16087 | -44.21912 | 2025-10-27 00:13:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c25c9c3a-3b1b-3c9f-b666-3dc3e5339d6d | -4.39182 | -43.31476 | 2025-10-27 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 68d82284-b019-3f4c-b4e7-c490a6d0218a | -9.99559 | -47.19161 | 2025-10-27 00:13:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| d52584c5-dfc9-360d-b88d-db1460759b7b | -9.47987 | -40.38049 | 2025-10-27 00:13:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 21.9 |
| 2424b1f7-daef-3331-8089-faee63642dcc | -10.86471 | -44.59405 | 2025-10-27 00:13:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d19580df-aa7d-3d6a-9dfa-95bed67ad55f | -7.80764 | -45.40024 | 2025-10-27 00:13:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8e51964c-e49c-36aa-8d1d-df582929c7d8 | -4.39322 | -43.32462 | 2025-10-27 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 649dc6ed-0b86-35d0-9282-f3b99d492868 | -4.93529 | -44.75807 | 2025-10-27 00:13:00 | TERRA_M-M | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5915bff7-876d-354e-857b-ff312f9a768b | -5.33602 | -44.71613 | 2025-10-27 00:13:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 3dab7866-7022-33cc-9334-d582ec35b69f | -9.86463 | -44.88633 | 2025-10-27 00:13:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| acd4bb51-6151-3ca6-92bc-d60d55b837f9 | -4.26309 | -40.68736 | 2025-10-27 00:13:00 | TERRA_M-M | PIRES FERREIRA | CEARÁ | Brasil | 2310951 | 23 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 15953a7e-7a12-3c47-883f-c15f9cf4bbee | -7.85 | -46.46896 | 2025-10-27 00:13:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 1378c120-17bd-3766-ae86-68d0dec7af4f | -6.98596 | -39.10709 | 2025-10-27 00:13:00 | TERRA_M-M | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 18.1 |
| 09290159-2339-30b9-b0da-2086e8e44580 | -6.01261 | -48.11752 | 2025-10-27 00:13:00 | TERRA_M-M | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 1d1e16df-83e8-3674-9534-cff6346c8c39 | -7.30453 | -42.48333 | 2025-10-27 00:13:00 | TERRA_M-M | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| a83808b7-eca6-32de-824a-49b8a25cc415 | -7.23546 | -46.95327 | 2025-10-27 00:13:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0ceadc12-ebf2-37d8-9550-695941357cbd | -5.10239 | -43.19354 | 2025-10-27 00:13:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| efbef335-de24-3341-8e74-2df5316bbcd9 | -5.53851 | -41.39896 | 2025-10-27 00:13:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| a043a8cd-dfde-3253-bb96-d20702cf29b9 | -9.57986 | -46.89494 | 2025-10-27 00:13:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 55c02273-4175-3f6d-b00c-0ba57ad37fc7 | -5.23138 | -43.31829 | 2025-10-27 00:13:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 0f29ee6e-c21f-3c99-87ba-b25e405caec2 | -10.73627 | -44.1978 | 2025-10-27 00:13:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b7cce513-3793-3c4e-bbd2-63f892813f35 | -7.84199 | -46.46646 | 2025-10-27 00:13:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 6b1ddb91-5e4c-3ecf-88e5-0c8439155a35 | -9.12268 | -45.86664 | 2025-10-27 00:13:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 37.8 |
| deb6c2d5-e630-317b-a6ef-30a99d044486 | -6.16838 | -41.58368 | 2025-10-27 00:13:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 16.9 |
| 643c04a8-7cc8-3263-ac41-9afd549403b8 | -7.80642 | -45.39121 | 2025-10-27 00:13:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 322f97a7-031f-3e8b-9015-c98064dc4ab7 | -8.36041 | -46.15596 | 2025-10-27 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 021995d3-5c94-386c-a3f2-a27c35fce7ca | -7.44352 | -47.20414 | 2025-10-27 00:13:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5eb96a98-1712-36fb-af49-c90ef1881e9b | -9.18561 | -44.57019 | 2025-10-27 00:13:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 1104d759-67c4-3b1e-95dc-94c541c3c189 | -6.90438 | -46.14048 | 2025-10-27 00:13:00 | TERRA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| dbfa177f-5d6b-3614-b0ba-03c7fa7e9512 | -10.63309 | -52.19431 | 2025-10-27 00:13:00 | TERRA_M-M | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 20.1 |
| ced66574-40be-3aaa-bfcb-5714321cf86d | -6.43118 | -42.34624 | 2025-10-27 00:13:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 96fe7df1-c88d-33e8-9f84-27108e9d5842 | -8.48268 | -45.55791 | 2025-10-27 00:13:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9c89e9b8-bd0b-3e4f-bcff-e31e5fb192f2 | -8.03586 | -46.74823 | 2025-10-27 00:13:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 23.4 |
| df253adc-9139-3790-972f-cc0a3127f43e | -8.11038 | -44.39913 | 2025-10-27 00:13:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e4f7af0d-44bb-3ae2-a55d-ec16530f7ab7 | -6.37915 | -44.26705 | 2025-10-27 00:13:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| dd68d03f-eb57-32af-9599-44c0f94f8e53 | -7.38381 | -46.55025 | 2025-10-27 00:13:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ac887d07-aa64-3abd-8013-8529e7ee9d80 | -6.51076 | -46.22618 | 2025-10-27 00:13:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 403a9a16-beda-39da-ae84-7dbc53948306 | -10.6039 | -46.62366 | 2025-10-27 00:13:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 195948f8-f9cc-371d-8567-1565a5d7463c | -10.34127 | -44.00626 | 2025-10-27 00:13:00 | TERRA_M-M | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c33d2c81-a39d-3112-a8ac-53abd8fe4ed3 | -6.63292 | -44.63568 | 2025-10-27 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b12e6fab-8ccb-372a-8952-53bfa5198b63 | -7.53816 | -46.26389 | 2025-10-27 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| a297b404-3b9d-3137-b6f2-4da16a4e8d7c | -7.85257 | -46.48841 | 2025-10-27 00:13:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 5cef2165-e350-3797-995e-55adf121b6d0 | -5.63145 | -47.62612 | 2025-10-27 00:13:00 | TERRA_M-M | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 4129b72b-1055-3611-839f-b8a087f3f457 | -4.48097 | -43.42556 | 2025-10-27 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 26.1 |
| c5322cc1-a9ff-3d95-9ba9-5af203538b69 | -6.43857 | -42.03201 | 2025-10-27 00:13:00 | TERRA_M-M | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 51a22bce-25c5-3767-84a2-1d3000284900 | -7.97305 | -45.47176 | 2025-10-27 00:13:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5a955639-7cf4-31b5-9f1f-9b2a06827db4 | -4.47957 | -43.4158 | 2025-10-27 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 1e611095-7fd3-33b6-a21b-1c614d6e8a51 | -5.82451 | -40.83206 | 2025-10-27 00:13:00 | TERRA_M-M | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 08e4b3ee-3b30-316a-9ab2-ec91b93b67b2 | -7.82749 | -46.42886 | 2025-10-27 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 4abda6a9-ae79-38a1-b837-a2b7e905dcb8 | -4.48995 | -43.67612 | 2025-10-27 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| ad6221a4-3036-3f8d-a8d4-eca82483ed76 | -7.05964 | -46.75207 | 2025-10-27 00:13:00 | TERRA_M-M | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 81efa7e5-6ca4-3f60-be39-7812a5710e97 | -7.76898 | -45.39315 | 2025-10-27 00:13:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 14.6 |
| d035a7fd-5525-301b-b340-cefd1162ed31 | -7.38249 | -46.54061 | 2025-10-27 00:13:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 7c161ea8-53a2-3233-83ea-66a51a5edd79 | -9.5872 | -44.94429 | 2025-10-27 00:13:00 | TERRA_M-M | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 51f13de2-3e74-30d4-a465-9c87edd64032 | -9.99126 | -47.15812 | 2025-10-27 00:13:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 152bf934-bdb8-3113-bc4f-760c3d57cfc3 | -5.78923 | -35.37383 | 2025-10-27 00:13:00 | TERRA_M-M | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 41.5 |
| 12c95089-5ddb-328b-8076-794a8f8eafe6 | -7.33814 | -48.48864 | 2025-10-27 00:13:00 | TERRA_M-M | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| dcafa213-6104-3565-9026-7ac4af097db2 | -9.65673 | -44.58106 | 2025-10-27 00:13:00 | TERRA_M-M | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b83c49b1-6850-38db-becc-b61074301fe7 | -7.00023 | -46.99816 | 2025-10-27 00:13:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 26.6 |
| a2948759-596a-389e-9961-5c2e0c4d7965 | -4.47479 | -43.43286 | 2025-10-27 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 578489c7-265b-320b-b4dd-9f8724f9bc84 | -8.60516 | -41.44615 | 2025-10-27 00:13:00 | TERRA_M-M | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 31.3 |
| 41f465c0-18dd-3236-b5fc-df5be0bf755b | -5.65964 | -46.46566 | 2025-10-27 00:13:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| db55ca74-29cf-3d66-ba6b-af2c9ded3ca9 | -6.79263 | -41.01104 | 2025-10-27 00:13:00 | TERRA_M-M | MONSENHOR HIPÓLITO | PIAUÍ | Brasil | 2206506 | 22 | 33 | nan | nan | nan | Caatinga | 33.0 |


[Clique aqui para ver as próximas entradas](README6.md)
