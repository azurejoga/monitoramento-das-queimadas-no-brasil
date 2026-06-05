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
| 0f204649-15d6-3a91-96ee-d16d9b7ed326 | -11.5496 | -52.8076 | 2026-06-05 03:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 46d0a6d0-1220-308f-bcc6-46402b420fd1 | -11.5496 | -52.8076 | 2026-06-05 03:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 23b7719a-67b0-368d-b3be-eea0bdf5b6e7 | -4.63325 | -43.0524 | 2026-06-05 03:47:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 93ef7917-fe79-31d9-97a3-4af66b9f8c1f | -5.93213 | -43.48275 | 2026-06-05 03:47:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6d600946-9a71-30e6-9347-b5436b1f8f77 | -5.72617 | -45.02893 | 2026-06-05 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8ed7654d-f8f2-3062-b003-703fe1666e01 | -5.93292 | -43.47805 | 2026-06-05 03:47:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 84e8f77b-640b-333d-8de8-7fd9cb1bed7d | -5.81481 | -43.79285 | 2026-06-05 03:47:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f90e6dfa-e6b9-37e9-9562-fb3d6c654a46 | -5.81328 | -43.78955 | 2026-06-05 03:47:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6d6e8533-a92d-3289-9e10-f61b26e20cb1 | -4.63678 | -43.05021 | 2026-06-05 03:47:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 34b627db-cb6f-3ae8-a45e-049698801096 | -5.93134 | -43.48747 | 2026-06-05 03:47:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| eec6b337-c1ea-3bc0-933c-9210ceef20c8 | -7.21869 | -34.95805 | 2026-06-05 03:47:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4556ae07-4fe8-3a92-b0fb-457520ebcf95 | -5.72511 | -45.035 | 2026-06-05 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d4046bda-73cd-3267-8f23-4489c80b505d | -3.95796 | -43.11444 | 2026-06-05 03:47:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2b8d918f-a110-381f-a87a-6100fb008c51 | -5.81243 | -43.79447 | 2026-06-05 03:47:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3829e0f8-4970-3a65-b16d-d5b401042e83 | -4.63225 | -43.04947 | 2026-06-05 03:47:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a952aae-3a30-33a8-8aa2-458fbe8bbbaa | -5.72107 | -45.02811 | 2026-06-05 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cd9171a4-46fa-3369-8261-f9ae0c7ca1f5 | -5.72458 | -45.03802 | 2026-06-05 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b07201fe-57ce-305a-a275-51df8e27d3a0 | -5.92837 | -43.47719 | 2026-06-05 03:47:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4db4c6bb-9bd9-3a6d-af83-1597a766b82b | -5.92758 | -43.48191 | 2026-06-05 03:47:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 487aee61-3f8e-3925-9e57-29654b21062b | -3.96256 | -43.11518 | 2026-06-05 03:47:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a45f69ff-584d-368c-92ba-6480b5d7db30 | -12.5264 | -46.27826 | 2026-06-05 03:49:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d4028df5-74eb-39bd-adc1-da17c4aec94c | -12.00399 | -45.35605 | 2026-06-05 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d9b28738-8959-3f2f-8821-790df841eb33 | -12.03011 | -45.88755 | 2026-06-05 03:49:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c3bc67df-dae0-3f06-9770-b1043b789713 | -9.08197 | -50.61378 | 2026-06-05 03:49:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6a9ad08c-df68-31d9-abe1-0b9789b1d35f | -10.93316 | -46.94886 | 2026-06-05 03:49:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 10568246-a784-34c9-9303-9cfd27aa799c | -11.03993 | -44.32288 | 2026-06-05 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a772cf35-1822-3854-a4b8-7a84c67b3531 | -9.08074 | -50.62009 | 2026-06-05 03:49:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c030bfc5-18a9-32c9-a45d-c2c8bb13408e | -9.37454 | -50.54649 | 2026-06-05 03:49:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 026b139b-103b-3de6-8a97-2bb8e4ba6bb7 | -9.08979 | -50.61525 | 2026-06-05 03:49:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| faa65555-3352-3824-8f23-14518d997e8c | -8.73272 | -48.33203 | 2026-06-05 03:49:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| ebbd16bc-8b15-383a-aefc-8e4ac874b050 | -11.3895 | -47.81475 | 2026-06-05 03:49:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 98e7d60c-3059-30b5-aa3e-53d6cb6dd88f | -10.5118 | -42.36949 | 2026-06-05 03:49:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| dc27b51d-246e-3f4a-9bee-d0dcbca708c7 | -11.03473 | -44.32035 | 2026-06-05 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 33558631-3070-361e-a97a-982480e405e6 | -8.47988 | -46.27671 | 2026-06-05 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d7d1defa-fc37-3bbe-b1f7-23b91dccff99 | -8.32134 | -46.99598 | 2026-06-05 03:49:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ba95276f-8588-31e2-b6be-9508540e58ec | -12.50463 | -46.34723 | 2026-06-05 03:49:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2596c5c7-fb90-379a-8f28-86d845aea241 | -11.04358 | -44.32201 | 2026-06-05 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a55c85fa-e4e2-3555-a0f1-81c0508f9321 | -6.98725 | -42.88383 | 2026-06-05 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 19.1 |
| 3a40a0e4-1102-30ee-858b-c9ca00b54a47 | -9.08166 | -50.62039 | 2026-06-05 03:49:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 593c9b2c-65d1-3908-af75-1000728826c0 | -12.52266 | -46.28012 | 2026-06-05 03:49:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 82a8926b-ee09-3c43-be18-b9aacfb033c6 | -8.32199 | -46.99242 | 2026-06-05 03:49:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7b4983ec-9ef6-356e-8c7b-c7113e17c375 | -11.63477 | -47.87513 | 2026-06-05 03:49:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0499b153-89c5-34ad-b3e1-acda18020d7d | -8.72755 | -48.3265 | 2026-06-05 03:49:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 767de27a-bd43-3546-b8b1-de60ea39b6cd | -9.37577 | -50.54031 | 2026-06-05 03:49:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 17b40ea5-626f-3745-98f6-c264229947e9 | -7.95167 | -46.84129 | 2026-06-05 03:49:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c15b2a25-3613-3b24-8670-be175fcd6836 | -7.34483 | -49.83231 | 2026-06-05 03:49:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 5f7f0866-d28f-3fac-aff1-c773393fa8a0 | -7.35651 | -49.82304 | 2026-06-05 03:49:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 33e6a6a4-ee9d-3eb6-b378-908c9d488bdb | -10.88274 | -46.99124 | 2026-06-05 03:49:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3c2970d0-ceb4-35de-8b3f-26572139b79c | -11.99627 | -47.77391 | 2026-06-05 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f259a846-9a78-3e0a-b32f-3db5f2ddd7f0 | -11.38807 | -47.82214 | 2026-06-05 03:49:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 565cc89e-2cb5-3120-a0bc-440562cbed08 | -11.11889 | -46.00885 | 2026-06-05 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 441d9028-8730-3048-a5a5-61558cecb344 | -8.72671 | -48.33097 | 2026-06-05 03:49:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| aa899c6c-ed9b-3ef0-8879-06eeb015fa2b | -12.53242 | -45.67878 | 2026-06-05 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a26d9f7-a02c-32b8-b623-0f31033eccf5 | -12.00491 | -45.35102 | 2026-06-05 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5e3ec8ed-d309-37bf-9eae-2c707eee1ac5 | -10.79222 | -47.03349 | 2026-06-05 03:49:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9a223f21-985d-33d6-9d32-9631c6a737ea | -10.51203 | -42.37165 | 2026-06-05 03:49:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2bdefd2a-8b3a-3443-ab41-e79dd5bf3e58 | -10.58635 | -46.77328 | 2026-06-05 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 985c66a5-f4a8-393f-ad12-e79e2ad2bf15 | -12.52381 | -46.27417 | 2026-06-05 03:49:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 305c2493-442e-3228-ae49-58b94af01599 | -9.93364 | -48.00511 | 2026-06-05 03:49:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d7173c0b-c7cb-393d-94e7-75e8c36b46ff | -11.54646 | -48.27105 | 2026-06-05 03:49:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ffd4e112-bccb-352e-a330-c31ad58a2f55 | -9.08293 | -50.61408 | 2026-06-05 03:49:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 824cc277-5dd8-36a8-b812-936c3deaa7cd | -8.24753 | -47.09268 | 2026-06-05 03:49:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 78338219-8d58-3161-b1f3-aeb8261f069e | -7.64446 | -45.23256 | 2026-06-05 03:49:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e55a6b9a-d9fe-34f2-89f9-cf3424cf1e2c | -12.50577 | -46.34134 | 2026-06-05 03:49:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7146aa25-e622-3ef3-be6b-ecc4ba597def | -8.73356 | -48.32758 | 2026-06-05 03:49:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| cb63f94e-6923-3b15-9495-2a4828e0ed2d | -7.95651 | -46.84617 | 2026-06-05 03:49:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0741ee03-a588-3d11-b94b-560789eb15ad | -10.39018 | -49.44419 | 2026-06-05 03:49:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e69437e0-74ee-395e-b1c9-a96e160a7579 | -11.03915 | -44.32117 | 2026-06-05 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4f3fa625-92dd-34d5-a8a1-4aca07fb19a8 | -8.64216 | -45.76879 | 2026-06-05 03:49:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e06ba68c-ad2b-3ff8-b144-0e5ce58a3501 | -12.0311 | -45.88215 | 2026-06-05 03:49:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 85907bb0-28e8-3e76-9088-82e8d7729c35 | -9.49708 | -40.31443 | 2026-06-05 03:49:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1a92fb5c-d9af-31dc-b093-9a6797d59e79 | -10.93378 | -46.94556 | 2026-06-05 03:49:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7f439b1d-b225-39d9-a930-417ddc0e2318 | -9.49775 | -40.31033 | 2026-06-05 03:49:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c4b2310f-2810-374b-81d1-a91834b6299b | -9.08883 | -50.61494 | 2026-06-05 03:49:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e7d67eda-efca-35e4-bd25-764f118c44d2 | -7.95717 | -46.84247 | 2026-06-05 03:49:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5d61f399-c905-32fd-94ce-a54b2f055e2b | -11.63405 | -47.8789 | 2026-06-05 03:49:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6aa0b63a-1e10-33fb-bca4-bc8c2140b5b2 | -8.64105 | -45.77488 | 2026-06-05 03:49:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 17bc58f2-a307-3cc5-9918-14ed5f52f1f4 | -8.48047 | -46.27344 | 2026-06-05 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f762d449-3667-3828-8aff-3c48dab97714 | -8.72585 | -48.33553 | 2026-06-05 03:49:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 80631352-e96c-3369-978b-62a53b01341f | -10.79155 | -47.03702 | 2026-06-05 03:49:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1af4b92d-d41e-313b-9a62-1cb0650ce626 | -12.53305 | -45.68122 | 2026-06-05 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2e7d7fa5-7368-396e-8aed-f5e47a617876 | -11.99932 | -45.35518 | 2026-06-05 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4df4d439-5413-3226-841b-96147aa18f12 | -10.93973 | -46.94305 | 2026-06-05 03:49:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3d6447fb-8ca8-3ced-ad0c-9b8550c5d623 | -8.24385 | -47.10295 | 2026-06-05 03:49:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f20a332b-399c-34f1-9c92-e1387cc8adb3 | -7.64947 | -45.23339 | 2026-06-05 03:49:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f0568535-5bc4-3416-b58e-a1631b5b0525 | -9.08236 | -44.36575 | 2026-06-05 03:49:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fc15df57-4279-36e3-828e-7993f0aa0677 | -11.03551 | -44.32204 | 2026-06-05 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b2cad311-0568-3703-bee9-11fffd6ec684 | -10.38918 | -49.44932 | 2026-06-05 03:49:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ebd02e4a-93cf-3f6d-b374-a34d83cb38ed | -8.64049 | -45.77796 | 2026-06-05 03:49:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c8c28ada-6b39-3572-967e-9cce84cfdae9 | -8.37508 | -46.79525 | 2026-06-05 03:49:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5ec8076f-c1e6-3fe6-8c82-797b2a6ce9b6 | -8.6478 | -45.76666 | 2026-06-05 03:49:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2d2a831c-46a6-327e-a10c-5f306ea595e2 | -8.24548 | -47.10408 | 2026-06-05 03:49:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 241a0885-816b-356f-80e1-4977d0627729 | -12.06258 | -48.07417 | 2026-06-05 03:49:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ee811984-293f-3c52-9fcc-7de3054ce8d2 | -7.64894 | -45.23632 | 2026-06-05 03:49:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d3121cdf-1d27-3c46-bc7b-f0eecea97a8c | -10.88118 | -46.99132 | 2026-06-05 03:49:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6793db99-d79c-3b20-ad60-ce1590994154 | -8.24595 | -47.09176 | 2026-06-05 03:49:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0fb0c930-c236-3a85-83a0-3b7d69a93107 | -10.38642 | -49.45105 | 2026-06-05 03:49:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5765932b-9970-30fc-85a2-d2598ee57e1c | -12.92733 | -43.61792 | 2026-06-05 03:49:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0d1697b6-2f8d-3d7f-b40a-db08850078e0 | -10.38746 | -49.4459 | 2026-06-05 03:49:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| aecd0d21-a4cd-3997-961a-7a8080f40c20 | -9.369 | -50.539 | 2026-06-05 03:49:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README5.md)
