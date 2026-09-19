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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 62809c3e-0379-3840-8852-f2d1704cbf91 | -3.34786 | -59.85865 | 2026-09-19 04:57:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e01d541e-41e8-3095-bb1d-c71ece939e3c | -8.82625 | -44.90381 | 2026-09-19 04:57:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a748c2a1-531a-3a72-b784-29ebc3bb255c | -8.76714 | -48.66737 | 2026-09-19 04:57:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 6.7 |
| fe462774-402e-3aca-9712-c76b93d7790f | -8.16062 | -54.73732 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bdcfe587-f7fa-348e-89aa-9a54c32433eb | -9.71035 | -45.99105 | 2026-09-19 04:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| baaea94b-2fc8-3b60-8fb0-030adbc8ae51 | -9.70138 | -54.83896 | 2026-09-19 04:57:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 570818f0-96e1-3642-ac78-629c8b63dbda | -10.9811 | -49.70277 | 2026-09-19 04:57:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1967d157-1c5e-3f4d-9625-0a260bc5b530 | -9.90307 | -46.57085 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 279b80aa-8b62-3d29-baa6-26e96584c38a | -9.47435 | -40.31563 | 2026-09-19 04:57:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| ce9bd0b1-0c7a-3408-9865-03f1b2f8956b | -11.07664 | -48.30971 | 2026-09-19 04:57:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 980ed002-3db5-3f75-8f90-93e301502156 | -8.83383 | -46.93288 | 2026-09-19 04:57:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2e90fa8b-6d59-302d-a665-fb9ee34832cd | -6.44783 | -59.9808 | 2026-09-19 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e83c2c14-2bd6-3246-8321-b52c97fe5f3f | -6.97865 | -42.18406 | 2026-09-19 04:57:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f0a5ee1b-961a-302d-afe5-2cb2221fd21f | -8.42411 | -54.73176 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 88f544ee-4674-3042-b3be-09fd495994ca | -8.49254 | -57.62374 | 2026-09-19 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 9e99c323-40d0-3523-a64b-617ebbfbacb6 | -7.06483 | -47.5394 | 2026-09-19 04:57:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d2121bb9-67c4-334e-877f-2a0b4f23388e | -2.90199 | -57.8085 | 2026-09-19 04:57:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2a31cf63-c113-3085-8d32-94006265576f | -11.04095 | -48.31179 | 2026-09-19 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| eb4d93f4-09f5-3127-b530-7d5c2ae64bde | -11.00081 | -48.32571 | 2026-09-19 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| a8ce5aa8-d8d7-3efc-98da-5dd38d30a2c6 | -6.66242 | -55.3576 | 2026-09-19 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3fc080ad-4c8c-34f7-826a-fb03084eb6d5 | -7.85715 | -44.86424 | 2026-09-19 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ea1377f7-44ac-3596-9f2e-b3b13d910d00 | -9.91617 | -46.57444 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e906b834-26c3-312a-a0c1-3445ead913e0 | -10.14119 | -47.68837 | 2026-09-19 04:57:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a1388baa-2c16-3ab8-9d5b-59b12f3e7641 | -5.86919 | -52.04596 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 442e868d-f2ba-3afc-bd65-2769092a1cba | -5.74311 | -57.58319 | 2026-09-19 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3241b137-8973-3284-bdd1-81030df73ccf | -8.15987 | -54.82698 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b275207e-b932-331e-9062-bc30edc32526 | -5.86378 | -52.03763 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fb46ea5b-3769-3503-b952-e7961e61879a | -11.00496 | -48.32634 | 2026-09-19 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 664d8b02-3cda-3b63-aaa6-7fa25449f9b7 | -6.31979 | -57.74934 | 2026-09-19 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 01a734d8-e92c-38e5-96a4-54d29094b3a2 | -5.75971 | -57.4458 | 2026-09-19 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ad923d22-ec1b-37c9-b369-ab60dc627b8c | -6.66831 | -50.93238 | 2026-09-19 04:57:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 105df8ed-df01-37a4-b764-0a85a5c5bc34 | -2.90134 | -57.81243 | 2026-09-19 04:57:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 11.5 |
| c5e4db5c-ad80-3ddd-8249-cb2969ef614a | -9.40604 | -50.2011 | 2026-09-19 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| af71fc7f-9916-3ae7-935f-42567c829dbd | -9.04442 | -48.71407 | 2026-09-19 04:57:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3a1908e1-f54e-35ff-8cf9-f25fd9f116ae | -8.32959 | -50.85675 | 2026-09-19 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 408ec4ce-e579-35e3-a5a0-df5925bf955b | -7.88344 | -46.43089 | 2026-09-19 04:57:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 47f2025f-a635-367f-9131-b602a47f1f42 | -11.0533 | -47.94366 | 2026-09-19 04:57:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a59e1791-956c-35d2-8b8a-4c9fb8397667 | -9.92934 | -46.58455 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1bbf8d5a-ff82-3307-a727-8c2f2aeab85a | -6.36579 | -58.28935 | 2026-09-19 04:57:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 65cfb166-44b8-3d38-a69f-d4534aefc330 | -8.08905 | -50.96267 | 2026-09-19 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ad3bc23-bebf-34c1-8ea8-d69ad3a4dde2 | -7.57484 | -57.69662 | 2026-09-19 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6ed0fe5-80c0-3e00-8aea-bab09fdc8ef9 | -4.87746 | -56.06969 | 2026-09-19 04:57:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f0d9e12d-22c9-3089-8212-99ee6327293b | -4.3638 | -47.78615 | 2026-09-19 04:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fa2e383a-9c79-3d72-b99f-235c3e8a498c | -11.29982 | -46.76681 | 2026-09-19 04:57:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5e5016ec-0dda-3c7f-9d39-3fe299111691 | -3.7348 | -54.64223 | 2026-09-19 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 92214232-4750-3c19-9d0a-098c89b42b18 | -8.12202 | -44.835 | 2026-09-19 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a4a4c8e0-c9cf-3c86-b960-4f76d77f1f6d | -4.48856 | -55.48815 | 2026-09-19 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b2343860-aa08-3047-9572-602a28830ecd | -10.24011 | -48.84806 | 2026-09-19 04:57:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 101f63f8-dc9d-34ac-a7f1-627c739cd9bc | -4.36063 | -47.78054 | 2026-09-19 04:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8d8de5d3-890b-3584-833f-7c930bf6c688 | -11.30267 | -46.78107 | 2026-09-19 04:57:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cee58185-2999-3974-b00d-ce227a6ceb4b | -5.99631 | -51.80057 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45241ecd-4369-34d1-a264-7689f62508a4 | -7.57973 | -43.44869 | 2026-09-19 04:57:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2b2543fc-266d-3e02-9d00-929b59fed399 | -3.47761 | -51.18863 | 2026-09-19 04:57:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 95cc0f41-6a71-3c51-8b30-7512b00d0052 | -10.76503 | -46.19669 | 2026-09-19 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2c2070c7-42a8-397d-ad3f-6177515ac5c3 | -5.8858 | -52.04854 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f494b30c-9d5d-35a9-90f1-e565b68482e1 | -6.98107 | -42.18634 | 2026-09-19 04:57:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 76e20b2a-af09-3328-8d4f-836ff63a952f | -9.02968 | -48.7323 | 2026-09-19 04:57:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 7bebda2b-fe6c-361c-a6cf-c4406efcee24 | -11.08294 | -48.29461 | 2026-09-19 04:57:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b80d23b1-78ab-30f2-bb54-670c115a84d9 | -9.34678 | -50.17474 | 2026-09-19 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 488bdffd-9dd8-31a2-96db-b49ed5f9f5af | -11.07766 | -48.30219 | 2026-09-19 04:57:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a8629060-ccf4-3e11-8d25-6767d88b38bc | -3.26169 | -54.27219 | 2026-09-19 04:57:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0b5cd3ba-7e7a-39f7-ab33-3dec70653420 | -6.35966 | -58.28848 | 2026-09-19 04:57:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 90e6460a-49d9-3147-bdec-297f5326ce8c | -3.15397 | -53.93877 | 2026-09-19 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9dba46f9-ca76-39d8-ad6e-4182add34355 | -7.05073 | -47.49147 | 2026-09-19 04:57:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a1661c5b-cf6f-3ae7-aae8-dcf1c71ed960 | -6.20214 | -57.77893 | 2026-09-19 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd1966e3-01e1-3f2d-b699-65fa4e1ea7ad | -9.23755 | -46.2068 | 2026-09-19 04:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 392f3e69-4bf2-320d-b9e4-9825c6b31195 | -10.53799 | -46.74223 | 2026-09-19 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 699cb134-361e-3ce7-9bd8-4ea716b89220 | -6.37019 | -58.31337 | 2026-09-19 04:57:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 13fe3141-aa2c-305d-8c21-0e4f37034ec6 | -9.74684 | -46.08003 | 2026-09-19 04:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cdf79f3f-aa4c-3201-9c60-6ae0382cfb14 | -8.08499 | -50.96595 | 2026-09-19 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6c249f3e-8654-3a19-aa67-7dbb3378b91e | -3.56108 | -50.05865 | 2026-09-19 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 788fe4f7-fc4a-3199-988d-bc609d5dceba | -11.13251 | -49.04517 | 2026-09-19 04:57:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7b7c5f9a-77eb-36a0-8726-d1a0495d06d0 | -8.36681 | -47.22164 | 2026-09-19 04:57:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ad7ad51e-85f3-3c09-a152-f5349cddbbf1 | -10.53531 | -46.72945 | 2026-09-19 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8f96841e-cc2f-3720-9992-ce4794a36cda | -4.4911 | -54.98079 | 2026-09-19 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ae6081f-d5af-31b5-8005-2d1ade9eeb2e | -7.05541 | -47.48849 | 2026-09-19 04:57:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b36a313a-82e7-38ef-b2d9-5a97299c6050 | -9.937 | -53.98767 | 2026-09-19 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| fcef43a5-0c76-3784-a1b7-c3d94d729298 | -9.72405 | -48.14577 | 2026-09-19 04:57:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d82ee3f1-0b7d-3695-9535-9693dd11f1d5 | -11.29866 | -46.77564 | 2026-09-19 04:57:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 11996beb-92d7-3364-8ca2-ffc94c028cb9 | -8.92112 | -49.99859 | 2026-09-19 04:57:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 683511a7-bc86-34c1-bc86-70a0cabbf31f | -5.84215 | -52.00215 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b79747c7-8ae5-339d-a2b4-8e80b431358e | -4.59364 | -42.95805 | 2026-09-19 04:57:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2100425b-88eb-3cd4-b5eb-56a8ae1558a8 | -3.20889 | -53.94717 | 2026-09-19 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1d501823-8fae-3d95-aeb4-31ac3bfa394c | -6.01075 | -51.79565 | 2026-09-19 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 132a0b46-0f7d-3e43-8dfd-1924dfe573ae | -8.16843 | -54.81712 | 2026-09-19 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63bb674e-4f7b-386c-9520-86a651b27995 | -3.55574 | -50.29342 | 2026-09-19 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 973cab03-23b0-3b53-aac6-f8c0eb2ce1e4 | -9.72235 | -48.03635 | 2026-09-19 04:57:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c3b00afb-593a-3a3c-bcee-dfccb78e1375 | -11.33516 | -47.34946 | 2026-09-19 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2f975df8-7a8b-31ec-803f-89dca65e766a | -10.49557 | -46.2767 | 2026-09-19 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4f4e9afa-5216-338b-8214-f635d443b097 | -9.15744 | -49.99123 | 2026-09-19 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 23bb4b90-a240-342b-9239-814a924fd53f | -3.72627 | -49.04223 | 2026-09-19 04:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f6f5b1b0-46da-37a5-9716-9b5e5b215fff | -4.50291 | -54.97461 | 2026-09-19 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a26b975f-4054-31c0-9dc1-00370aba2891 | -9.68814 | -54.33277 | 2026-09-19 04:57:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3c959311-15cd-3b77-9f34-38501db6659d | -4.50227 | -54.97861 | 2026-09-19 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43dc3f63-d125-3298-b9d5-35d28cef74fa | -10.7924 | -46.65493 | 2026-09-19 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dceeb61b-0ba4-38a5-90b7-b3f26a6935c3 | -3.84885 | -50.00861 | 2026-09-19 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4b38a6bd-34f8-3b23-986d-d2d3fc33e9cd | -4.50067 | -54.96612 | 2026-09-19 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 0b6f11d0-d05e-393a-b3ac-334028b2f9d6 | -3.94411 | -60.53188 | 2026-09-19 04:57:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 88b36e01-d89e-3465-bbe2-0798687c46ef | -10.92433 | -47.85561 | 2026-09-19 04:57:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c8a55678-73af-3777-b84e-ee9865bf5b4b | -10.62673 | -48.71813 | 2026-09-19 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README73.md)
