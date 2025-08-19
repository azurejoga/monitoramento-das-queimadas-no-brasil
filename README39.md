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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 174e9fab-ad0a-32b2-adc7-e57cf1d47695 | -10.037 | -59.35531 | 2025-08-19 04:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c2352cc1-cd8b-3178-8aae-4d012d041458 | -12.65821 | -45.80692 | 2025-08-19 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f350d48e-c44d-3bab-82ca-8c365d164cf7 | -7.38687 | -44.27755 | 2025-08-19 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 32b14f61-8617-38b7-8b85-ebe7589eb065 | -12.09612 | -47.91546 | 2025-08-19 04:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 032248a1-888f-37e1-9f24-7ce59cddf407 | -7.599 | -44.39948 | 2025-08-19 04:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a10e22c2-32db-384f-9bd1-9e4b4e47491d | -11.57348 | -44.85244 | 2025-08-19 04:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f420174b-5681-3200-9b55-d660215a12fd | -12.96247 | -46.17958 | 2025-08-19 04:53:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d2271ce9-7cd7-3039-b65a-c7a91ac02657 | -12.11526 | -47.90231 | 2025-08-19 04:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 12009243-ab49-3e0b-a07d-58fb4106650a | -7.2578 | -50.15692 | 2025-08-19 04:53:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35bfdeb3-8371-341e-bc6c-400282e99d61 | -7.29659 | -43.68832 | 2025-08-19 04:53:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 134128df-97e6-38b3-bb67-bba1d4cdd74f | -9.19929 | -59.63701 | 2025-08-19 04:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 385b3320-1305-3046-b6eb-123ff98b6b7c | -12.99366 | -45.19238 | 2025-08-19 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ea1010a7-6439-3072-94c1-9e29c9ae4ffd | -9.11702 | -60.33266 | 2025-08-19 04:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1af9dc9c-d0ef-3f11-8e84-b622a2d54416 | -12.7334 | -45.05632 | 2025-08-19 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2684d404-784e-3000-8e5c-a1d5c8303941 | -8.77473 | -49.99749 | 2025-08-19 04:53:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c3ccc8bf-9340-3747-8c3a-c96df2d655cf | -7.62991 | -46.21886 | 2025-08-19 04:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 23cd6da9-be6f-321a-8b6d-0baf251bb2c4 | -11.08984 | -58.94533 | 2025-08-19 04:53:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cd6c877e-227a-3236-b7a5-d938c424c621 | -11.4483 | -47.32114 | 2025-08-19 04:53:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2718bdcd-817c-3290-b424-a850c70b0604 | -12.99885 | -45.19305 | 2025-08-19 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bb70e69a-1b56-3203-861a-d7be502f1575 | -10.60639 | -52.78526 | 2025-08-19 04:53:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 02ecb9cc-cde8-31dd-a073-4774e61d7183 | -7.29525 | -43.69834 | 2025-08-19 04:53:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f6720055-f119-35c2-85e3-d2291e359bd0 | -10.96579 | -49.56869 | 2025-08-19 04:53:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 177ff533-1876-3289-8571-90ea0614b2d7 | -9.51363 | -60.51996 | 2025-08-19 04:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cbed4cba-95b9-335d-af92-74f8c00d2a2b | -7.25429 | -50.15639 | 2025-08-19 04:53:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb55a1d4-fd79-3a42-a3ff-f01066b7cb36 | -8.62151 | -62.62661 | 2025-08-19 04:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3989e6b5-ab07-3107-9eb9-09ac697bc2a8 | -7.2584 | -50.15298 | 2025-08-19 04:53:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b651c056-ceae-3684-9740-d1a7a7936c69 | -10.29429 | -59.45729 | 2025-08-19 04:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e62890a2-9fa2-39b1-acd1-c263371c6584 | -9.0705 | -60.41948 | 2025-08-19 04:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 99461fe7-3b5e-3e05-82d4-605a396a14d9 | -8.22095 | -47.28978 | 2025-08-19 04:53:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9256fe38-2f5a-36a9-8f6d-82fdf669f923 | -8.32003 | -55.13969 | 2025-08-19 04:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 16f4cf35-2441-38a4-9818-4e9b31ca1983 | -8.82203 | -52.03771 | 2025-08-19 04:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5b607a79-c608-300f-af98-b4797b5fdfe1 | -11.85682 | -51.57582 | 2025-08-19 04:53:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 57160e7b-3a88-31d8-bf1a-d69bdbb14c90 | -9.52037 | -60.53681 | 2025-08-19 04:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 90515665-4813-3412-89ee-a640c88d416a | -12.98847 | -45.1917 | 2025-08-19 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ed401806-cf85-31e5-8731-2e0ee9cfe72a | -9.51949 | -60.54183 | 2025-08-19 04:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c20924e-1e64-31e7-b037-e2b153d768fc | -9.51572 | -60.5431 | 2025-08-19 04:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 50244790-1059-3f3a-9d70-857031f45d8e | -12.95456 | -46.12397 | 2025-08-19 04:53:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 52c2fde5-cc2a-35a5-b420-d4cfc4637afc | -6.49457 | -53.39363 | 2025-08-19 04:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a71b146-94ff-3c85-a8d6-fcb5befcab61 | -9.18247 | -59.60247 | 2025-08-19 04:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 04de1d24-72e4-3d4a-b493-981155c1d170 | -7.29766 | -43.69406 | 2025-08-19 04:53:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e2c86daa-1e6d-3d63-9bce-21d20a33b3ed | -12.95238 | -46.12323 | 2025-08-19 04:53:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 20074761-eceb-30b3-82c9-6fa081e9f583 | -7.12394 | -50.42273 | 2025-08-19 04:53:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c63f6717-5d3e-361d-9edd-7682371c4913 | -9.18358 | -59.64795 | 2025-08-19 04:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a31bdbec-c541-3c69-b65e-98336fac1a1b | -7.15176 | -44.20755 | 2025-08-19 04:53:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 75a6c8f0-78d1-3800-b06a-ac9be448ce89 | -12.29697 | -50.01729 | 2025-08-19 04:53:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9f376bbb-c5a9-3973-8eb6-437d2e275799 | -7.26538 | -50.17809 | 2025-08-19 04:53:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39cf0ee0-15ba-3725-898c-cde885a7ef8f | -7.25488 | -50.15246 | 2025-08-19 04:53:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f760822-d671-375f-930c-4b54883cf3e2 | -9.72505 | -51.97202 | 2025-08-19 04:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6cf17ff0-ab7c-308c-952d-6924a5f173f5 | -10.96201 | -49.56813 | 2025-08-19 04:53:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2f44360d-39b2-354a-bc33-3df6dd67e21a | -6.63052 | -55.27425 | 2025-08-19 04:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6def43a4-2251-39dc-aee1-2f0f53355b8e | -7.68348 | -46.75483 | 2025-08-19 04:53:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d504c615-b9d6-3983-9ee0-7a9c184e8ff8 | -12.49658 | -45.56735 | 2025-08-19 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a7f87f15-af3b-3a34-8c1b-db06a01d1525 | -10.03772 | -59.35119 | 2025-08-19 04:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 49bb3397-a7a8-3c46-9101-1bea0b712191 | -7.38179 | -44.27674 | 2025-08-19 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 172b81ed-df82-3146-aa0e-bfb8cc6d27ad | -7.29236 | -43.69331 | 2025-08-19 04:53:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b4583002-e384-39a2-95ec-1e69fdfeb841 | -7.25721 | -50.16084 | 2025-08-19 04:53:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 166d282c-c58d-31ed-9553-f2949efa9c8a | -7.59089 | -45.42722 | 2025-08-19 04:53:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 424d0f0e-ce65-316e-9e45-8265bdd1ba98 | -7.97499 | -55.30421 | 2025-08-19 04:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ebdec040-8ea7-3caa-aaab-8efe763a75f9 | -9.8561 | -57.17627 | 2025-08-19 04:53:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4d1cf29-903e-3ddc-b398-89eb9d4bf79b | -8.82098 | -52.06654 | 2025-08-19 04:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54a26faf-a0f7-3a8a-823a-df9ab6b16509 | -12.95856 | -46.15145 | 2025-08-19 04:53:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3b06578a-73b2-3e5c-9419-e69ab24bfbb6 | -8.81593 | -52.05491 | 2025-08-19 04:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d3f6ef5-605f-3c36-bd59-bcee4f4b9780 | -9.85402 | -44.69189 | 2025-08-19 04:53:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 541f111e-9f93-37e7-9efa-6b82105075d4 | -11.58389 | -44.85388 | 2025-08-19 04:53:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0c3c6730-ebe8-3499-9e24-bfb44c3d2835 | -9.19193 | -59.62671 | 2025-08-19 04:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e490ff10-b090-3754-83af-44ea42f2c40a | -8.96769 | -60.50214 | 2025-08-19 04:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7e1f3095-cc64-3d98-9220-158e821ec7bf | -12.73223 | -45.06568 | 2025-08-19 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 83129f60-ecd4-3b28-95b5-c5fbca40cbbe | -11.85394 | -51.57144 | 2025-08-19 04:53:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c681c179-87d8-387f-bf85-4200961be976 | -9.18436 | -59.64355 | 2025-08-19 04:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6f3afcfd-7e8f-39a5-91da-95e857abeedd | -9.17832 | -59.65173 | 2025-08-19 04:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 515d1558-5827-3f0f-b57a-8e1047ffbf84 | -6.19652 | -53.51637 | 2025-08-19 04:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d8db988a-37cb-346e-8ac8-75c73953abc8 | -12.041 | -44.01909 | 2025-08-19 04:53:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6fe24814-42a9-37c7-bc2d-9e133ceedf0a | -5.88732 | -57.75151 | 2025-08-19 04:53:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2b42701b-6fcb-37ff-8057-03327c427b04 | -9.51186 | -60.53001 | 2025-08-19 04:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 066e7407-b41e-34f5-941a-8f784cfb2048 | -11.7565 | -51.93626 | 2025-08-19 04:53:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8ff2f19e-b181-3f4a-90ae-6b4167bf0072 | -11.85336 | -51.57528 | 2025-08-19 04:53:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ca8e84be-f192-3b28-b623-3e9526662021 | -7.78786 | -66.95663 | 2025-08-19 04:53:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ee842044-4abd-3525-8a20-d05f77c50c2e | -12.73301 | -45.05942 | 2025-08-19 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fb0f7e37-59e7-3a00-a5a0-c7428b4db20e | -11.85741 | -51.57199 | 2025-08-19 04:53:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 55f7d50b-9c9a-3493-b5b4-4a8ea81e6321 | -9.89103 | -64.26143 | 2025-08-19 04:53:00 | NPP-375D | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f50cb76-cd98-33c4-9570-019ccc0510b2 | -8.82763 | -52.04585 | 2025-08-19 04:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7ff4bf20-df64-310b-b501-8c3f812fe38f | -7.5935 | -44.40182 | 2025-08-19 04:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2b1d2062-673c-35e7-92fc-89fa8ef4305c | -9.72168 | -51.97148 | 2025-08-19 04:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d92aabb0-76d2-3703-a57f-225d7e2ad22a | -9.15015 | -60.82106 | 2025-08-19 04:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b76f2d4-e949-3163-9662-d1749aeeae96 | -9.71831 | -51.97096 | 2025-08-19 04:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| dcff27b6-3483-34f1-93b1-5a23223e60ad | -9.18513 | -59.6392 | 2025-08-19 04:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e559e8d0-97eb-305a-ba9d-599e894c0f5c | -10.50282 | -54.63124 | 2025-08-19 04:53:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8011e804-78e7-30b2-9e44-eb8fb9df239e | -12.03586 | -44.01495 | 2025-08-19 04:53:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3be000c8-793b-3b4d-b60e-4d151c77e541 | -9.51451 | -60.51492 | 2025-08-19 04:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d0ccbbc-be86-3e99-9f32-4fd32f9cabac | -12.99769 | -45.20254 | 2025-08-19 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bfb008fe-b117-3b1a-bcd1-ef62f9a298bb | -7.53276 | -50.52975 | 2025-08-19 04:53:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 91783ef8-1599-38f7-99af-8ea4f0602eac | -10.36195 | -49.92839 | 2025-08-19 04:53:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| de173dd9-c2e0-31bd-b281-cde831810a1b | -9.82329 | -49.22226 | 2025-08-19 04:53:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 077c6a98-e3cb-398a-9dcf-eced9dacbf2e | -7.27419 | -50.1674 | 2025-08-19 04:53:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 279362bd-94ca-315c-b0f8-a44b8958e6cc | -10.1147 | -57.75892 | 2025-08-19 04:53:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d10281ec-64b2-3ad1-8adf-622af767c6e3 | -8.7681 | -50.01757 | 2025-08-19 04:53:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 47b2f511-a066-3271-ab2e-064a617d0444 | -7.2933 | -43.68666 | 2025-08-19 04:53:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 716029bf-9cdf-39bb-a218-6219c307d17a | -12.98808 | -45.19486 | 2025-08-19 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b4bed345-edca-38f7-927e-6aeac6cdeea9 | -6.54555 | -49.51654 | 2025-08-19 04:53:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 697d3727-6617-36b4-9d18-5bc0673f70c8 | -10.50677 | -54.62817 | 2025-08-19 04:53:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README40.md)
