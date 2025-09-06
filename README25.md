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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e0c96ad8-0265-3fbb-b4bf-3b9af054058a | -13.28852 | -46.81686 | 2025-09-06 03:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bf8347a5-38d3-3326-86df-4015cd1b2b2e | -8.02185 | -45.42246 | 2025-09-06 03:49:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5d631acb-5ef9-309c-bc8e-d1a9cebcb6fa | -9.70947 | -49.49393 | 2025-09-06 03:49:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 9d3f607b-3a27-357f-87c8-0c6055ccc0c0 | -12.98559 | -48.05119 | 2025-09-06 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0b0acf26-5f56-3085-b1ea-508c53e88ee6 | -7.28523 | -43.70277 | 2025-09-06 03:49:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6c68d709-290f-3e01-baf1-e74b2e6c4819 | -13.26951 | -46.80906 | 2025-09-06 03:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fb8aedf7-629a-3ed2-b9aa-ee9060e3d69e | -7.34437 | -43.96087 | 2025-09-06 03:49:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 00933b56-b465-32db-bab1-53c7508edb2c | -10.79184 | -47.73938 | 2025-09-06 03:49:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8591ab06-8061-3604-a4c7-570f36ee5798 | -10.21599 | -49.7244 | 2025-09-06 03:49:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 644f0b41-f024-32fe-9124-f0ab616c1c34 | -13.59107 | -43.35136 | 2025-09-06 03:49:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c6066a16-2e34-38e0-944b-ffeda328e747 | -9.68102 | -51.09093 | 2025-09-06 03:49:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 296154ed-7593-3991-a98b-e814e7e0dda2 | -10.15665 | -46.23257 | 2025-09-06 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e28552f6-38ea-3703-858b-f3cf321cae39 | -7.04452 | -44.35231 | 2025-09-06 03:49:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 947fdf62-ea2c-3fba-b249-8c1994a79667 | -6.53345 | -49.49941 | 2025-09-06 03:49:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e7248f13-e2e3-3d8f-b183-10058876e7c0 | -9.68284 | -51.11608 | 2025-09-06 03:49:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f68766a0-feeb-3aee-aa12-2666f4ad4b89 | -6.42439 | -45.895 | 2025-09-06 03:49:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6b7c82c1-7ee8-38dd-be5a-649a11286a96 | -6.25017 | -46.12051 | 2025-09-06 03:49:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 85925ad6-6f82-3b91-8a18-c356287715dd | -10.22704 | -50.52559 | 2025-09-06 03:49:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f530f11b-45b3-3c1f-a455-968f1c6a4cae | -6.54458 | -49.51286 | 2025-09-06 03:49:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 74031a8d-7c99-3352-ac18-1558e53e25f6 | -6.80859 | -45.65319 | 2025-09-06 03:49:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| db6d4e69-137a-3332-98b2-a7005f1a0409 | -11.91391 | -46.6459 | 2025-09-06 03:49:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bc5735c0-9583-37e6-967f-495e9fae2ed3 | -10.60334 | -44.32849 | 2025-09-06 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 3bfdeb94-22c7-3f6b-8d16-cde320042218 | -13.60279 | -43.12371 | 2025-09-06 03:49:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 5b6488e3-cea0-3702-a980-d46b79aa6a51 | -12.5371 | -48.06656 | 2025-09-06 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4477740f-bbca-3eca-88f3-064aae522af6 | -9.08899 | -47.01044 | 2025-09-06 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f1295ab9-4b3c-3926-b260-0a496be66b18 | -9.6922 | -51.10462 | 2025-09-06 03:49:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7a2b7015-dff9-33cb-a72e-b1087ca508b9 | -11.93539 | -46.67013 | 2025-09-06 03:49:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 35bfb379-4abe-381d-b9ac-6a0aec43f403 | -7.21325 | -43.98307 | 2025-09-06 03:49:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d1f7bba4-a0ad-3ec4-a8b6-4a079e1c6921 | -8.8836 | -47.2585 | 2025-09-06 03:49:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 51edfc29-3e03-3168-a2dc-24e941e915aa | -13.27937 | -46.81108 | 2025-09-06 03:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 16fced5e-7cf6-3160-a519-1eac222ba0fe | -11.54891 | -47.32302 | 2025-09-06 03:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ac4f800a-1d03-30fb-a633-1b523284bb78 | -13.27353 | -46.81485 | 2025-09-06 03:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1473ace8-5e69-386f-b8d8-7516b45a5672 | -12.90616 | -48.01646 | 2025-09-06 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f11a38c7-ff3c-302e-b052-35aa95bf202d | -6.40181 | -46.08933 | 2025-09-06 03:49:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3a3f7be6-d0f7-313e-ba6e-367f5d1f955c | -12.08975 | -45.68941 | 2025-09-06 03:49:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 3eda29de-4a39-3c79-b42e-791972736b2b | -11.54491 | -47.31533 | 2025-09-06 03:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| be56d30e-ee65-3a1b-817d-de41abf20a4a | -7.72616 | -50.30901 | 2025-09-06 03:49:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| bbb07a55-9076-36b3-9eba-14054e9522a3 | -8.34145 | -47.48206 | 2025-09-06 03:49:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| db2df2b5-b880-3244-8a65-ec3eda2328ee | -11.93397 | -46.6482 | 2025-09-06 03:49:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 854514c1-a977-3cd4-99c2-016a798fd7db | -10.75057 | -46.34402 | 2025-09-06 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f5c5af21-e12a-3242-94ee-620cdc3dd35e | -6.86349 | -44.82093 | 2025-09-06 03:49:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 169bdace-c2f0-326c-8ad6-516885547118 | -13.05675 | -47.10714 | 2025-09-06 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 75e0f7d5-ce33-3b99-a831-6c8f6678c2da | -6.4048 | -46.09549 | 2025-09-06 03:49:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3b359db3-40b1-3ce4-8259-275f08f6cdef | -13.27442 | -46.81013 | 2025-09-06 03:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fdd40ca1-2e27-3a26-b019-5881536a6d55 | -9.53384 | -40.32266 | 2025-09-06 03:49:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d87173b1-c104-339e-88fd-4f39228e47dc | -10.30812 | -46.41935 | 2025-09-06 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b0f6bd30-3d5a-32cf-8229-11335452e3e0 | -8.01759 | -45.43893 | 2025-09-06 03:49:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 1345b502-c644-3668-888e-d9b6c3780503 | -9.67849 | -51.10341 | 2025-09-06 03:49:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 420a595d-962b-3991-9ccd-03e3aa4a5d37 | -10.60696 | -44.33366 | 2025-09-06 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 33c5fb88-4975-3be7-84dd-5ec3354aaba3 | -12.90081 | -48.01529 | 2025-09-06 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bd96494b-98e8-391e-9a1e-35063e4d0566 | -8.08549 | -45.32319 | 2025-09-06 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 713aa4f6-d825-3aa6-82f9-689199e9bc38 | -6.40122 | -46.0928 | 2025-09-06 03:49:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 976305f7-fb05-3b1a-b247-82dcbc9b3801 | -13.18544 | -44.48817 | 2025-09-06 03:49:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a4eef251-b01b-3e03-8b35-be1f9a4dbbb6 | -6.53913 | -49.49654 | 2025-09-06 03:49:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a16a2140-e8f8-3613-a5b6-d01b1d031eae | -10.79115 | -47.74296 | 2025-09-06 03:49:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 62f153d2-c18e-3da2-801a-34139daf3ee8 | -13.98071 | -42.58223 | 2025-09-06 03:49:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c7850ab7-7ac9-3d33-a53f-748863dc180e | -9.82673 | -46.53524 | 2025-09-06 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 335caf13-6d3b-3038-a012-0479e5724584 | -12.5592 | -41.30565 | 2025-09-06 03:49:00 | NOAA-21 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 5f8b489f-ad9b-3113-b46b-86010b1f69d9 | -11.01298 | -45.93355 | 2025-09-06 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 170a4d29-47d1-378f-aa74-bffdee5c0de3 | -12.68681 | -44.97083 | 2025-09-06 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2a8bcf61-fb2d-3ea9-aa43-3554371a3581 | -10.75502 | -46.34803 | 2025-09-06 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 28fd6cde-99d9-3672-a6b3-9727ea1702a7 | -9.011 | -49.8011 | 2025-09-06 03:49:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 03751987-1a26-3b78-9c85-22231547b44f | -10.61135 | -44.33447 | 2025-09-06 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e2665d46-47d6-3611-8216-2cf218592fbf | -8.91162 | -45.78122 | 2025-09-06 03:49:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 52b623bf-3dfe-3da9-88d2-ed41884ea8f2 | -10.31595 | -46.40524 | 2025-09-06 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| eab39181-3266-3d3d-b480-968d0a11fb0b | -10.6062 | -44.33805 | 2025-09-06 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 31a79570-d63c-38e9-bf9c-8baf9662c53c | -11.40464 | -43.59569 | 2025-09-06 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 46e59e2a-7785-3da7-b33c-7c714c270c3d | -10.76734 | -48.27681 | 2025-09-06 03:49:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9e064525-3e64-3b1d-b0cb-f4617063b563 | -7.41443 | -44.94003 | 2025-09-06 03:49:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6cff923e-689a-3fd8-a120-2819d56305e9 | -10.16069 | -46.23492 | 2025-09-06 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2c61bbcc-8f4d-3bf0-8194-67701610f431 | -8.01866 | -45.43283 | 2025-09-06 03:49:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5dc4b52c-434c-36c7-8f74-bf4950a0ec1f | -8.75546 | -39.81624 | 2025-09-06 03:49:00 | NOAA-21 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 254de7fd-669f-339b-8285-a669bdebe6ec | -7.25988 | -41.89304 | 2025-09-06 03:49:00 | NOAA-21 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 50e12e8f-1be2-3973-a6cb-e377fd86e4eb | -9.84213 | -48.84015 | 2025-09-06 03:49:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 89738b11-1268-3259-981e-b82072d2e3ee | -6.539 | -49.50622 | 2025-09-06 03:49:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8cff3dfa-32e4-337a-bdba-554ef64c5edf | -10.16969 | -46.24679 | 2025-09-06 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 470a5182-3ba8-3433-acf2-a53cfeed811b | -7.30296 | -43.73307 | 2025-09-06 03:49:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 94221c1d-6899-3b7e-93d3-e752a65a55c0 | -8.10491 | -45.32772 | 2025-09-06 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8fbd312a-7a7a-3951-8b76-856093a38412 | -11.64657 | -47.15213 | 2025-09-06 03:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f8760a1f-145e-3842-bfdd-d8806c630849 | -12.72789 | -45.09293 | 2025-09-06 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f8338380-52b6-3c81-962a-f72d8ffbd148 | -12.91156 | -48.01742 | 2025-09-06 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ec9c8868-b2db-38be-9d08-292c497fa9ef | -12.6909 | -44.9696 | 2025-09-06 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 33192326-3ca6-3e07-99d9-c195f2e1fd88 | -7.67702 | -50.29915 | 2025-09-06 03:49:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| da3ba517-aa45-3acd-a54c-7f34e88ca098 | -10.30922 | -46.41336 | 2025-09-06 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d2ff2f5c-1731-3617-8c43-84e92a6e0710 | -9.69226 | -51.10574 | 2025-09-06 03:49:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cacaf99c-bf35-35dc-a45f-64dc9da2e062 | -10.97722 | -46.81818 | 2025-09-06 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0d4bbb0f-f685-3ea2-bab5-40fbd5adefb5 | -9.08562 | -46.99855 | 2025-09-06 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1fbb6625-88eb-30ea-a2e0-ac9b95771431 | -7.99176 | -45.4697 | 2025-09-06 03:49:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a5e846b8-2f10-373a-8f03-0f9fd67185b1 | -6.53798 | -49.51181 | 2025-09-06 03:49:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d5218884-750f-3ffb-b10e-c15e12ee5a68 | -10.77396 | -48.27312 | 2025-09-06 03:49:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f1faebef-c745-318a-9b61-1df8cfa597d1 | -13.06238 | -47.10512 | 2025-09-06 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aa564a26-4f3d-38f3-8317-ce3c8aea3d72 | -7.64051 | -46.56033 | 2025-09-06 03:49:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d08ef869-8688-3bca-b35f-89d8a27c1a7f | -8.64346 | -45.75156 | 2025-09-06 03:49:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0ca82a3f-0d2f-3bed-8d2a-7bd6dbfa7922 | -7.21163 | -43.9923 | 2025-09-06 03:49:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0409fd86-60c6-37ef-b5cf-e7aa4c56d344 | -11.92986 | -46.67194 | 2025-09-06 03:49:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7e37ed90-c6e0-3b0f-9e39-e30ddb4a9cc8 | -9.01742 | -49.80235 | 2025-09-06 03:49:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c155c113-d0db-38ab-9038-2475f8c99281 | -13.00885 | -45.21537 | 2025-09-06 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1abd5182-7adf-3b6a-86c8-a78658593b9c | -2.77983 | -41.802 | 2025-09-06 03:49:00 | NOAA-21 | ILHA GRANDE | PIAUÍ | Brasil | 2204659 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a2289942-09cc-3d81-a090-b32c85a848a7 | -12.93153 | -48.02964 | 2025-09-06 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a1b90e71-a5c4-33fb-ba18-7bdff1e2c187 | -11.62895 | -47.80476 | 2025-09-06 03:49:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README26.md)
