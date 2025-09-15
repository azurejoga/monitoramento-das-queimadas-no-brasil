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
| ca9d2e58-9ebd-358d-a30a-7949b6277fd9 | -7.67376 | -44.48938 | 2025-09-15 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2a2cbcd3-67aa-3a76-b085-a647f56995c4 | -8.64173 | -45.69555 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f4bf5166-7dee-3767-88b2-97ad84f6a477 | -3.79508 | -52.17324 | 2025-09-15 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 56e2efe7-a7d5-3d33-a0c8-3a1432eafaf5 | -8.91358 | -45.48909 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0aa18482-cb25-3a21-9e7d-8d8c2cd56ee2 | -7.70973 | -50.36042 | 2025-09-15 04:49:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 478dfd26-d8c0-3404-824b-290e9750a196 | -7.4865 | -46.1245 | 2025-09-15 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 23e4fc2d-d6a3-3ec6-bffc-86c57f4e175f | -6.43472 | -42.60974 | 2025-09-15 04:49:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4c78670c-768e-303f-9e09-4c5cb6196717 | -7.87885 | -43.58691 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 8c79bd65-3e5a-33d9-8d90-3a9152e8f1c4 | -7.63836 | -49.74208 | 2025-09-15 04:49:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5908b2d-f73d-39c7-8f2c-f0ea77cac0e3 | -8.95933 | -45.80885 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 37ada9c5-01ef-3921-b5f6-9f945b3084cd | -6.17222 | -41.19246 | 2025-09-15 04:49:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e69df371-5806-33bf-ba0b-ebdc99ba0148 | -8.61738 | -45.74348 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 95b2ef24-44b6-3e02-9a19-481b608cfdf8 | -7.8676 | -43.5752 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 49c83959-66a9-3d7b-94a7-21475173ad7a | -10.17805 | -46.15239 | 2025-09-15 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e3ff6c1d-e0eb-36f7-a71a-49f69a09e80c | -7.85903 | -46.11912 | 2025-09-15 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ad61f0f7-0500-3299-8dba-e14456a9c825 | -8.91183 | -45.50168 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 849453ae-afb5-32c5-80ef-e7659e922626 | -8.10809 | -50.15874 | 2025-09-15 04:49:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 300de557-a4e7-3043-8590-8e42feda865e | -10.19014 | -46.15842 | 2025-09-15 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f61a58ed-631d-3263-a681-0350e1c92944 | -8.98325 | -45.82401 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2e46bd4b-80b7-327f-a299-3e743bf88f31 | -7.30916 | -43.93258 | 2025-09-15 04:49:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 00460dc4-5165-31c8-b8e9-76b50cf7593b | -8.96261 | -45.78514 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fba49474-8c18-346e-8d54-c7e8cc5cbc2b | -8.65017 | -46.36989 | 2025-09-15 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0cb7361a-3f9b-348a-8f36-b3a987e2d2d3 | -10.18227 | -46.15305 | 2025-09-15 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2a5742e4-4ae5-3d0e-aac4-6f634ef3ae09 | -7.8472 | -46.11393 | 2025-09-15 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 10787a89-e241-3c38-be98-0d390a6b3182 | -8.64769 | -46.35843 | 2025-09-15 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 625e9a82-4cb4-3ba0-b02c-65bcc661b6b6 | -7.88039 | -43.57618 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 7e16afb9-d39b-3ef8-83be-fab967be4c92 | -6.40779 | -46.93198 | 2025-09-15 04:49:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 95fa6030-8168-3dc1-8705-1d821b699ac6 | -7.90408 | -46.23998 | 2025-09-15 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8996e26d-f9a3-3182-a88a-74e952944c57 | -6.68129 | -46.7128 | 2025-09-15 04:49:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 00dfa114-41db-371d-933b-038c8c6f5fdb | -8.95616 | -45.80038 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e07d0a2b-0ab9-3c22-b307-ded8ff3e6c9e | -9.01589 | -48.02996 | 2025-09-15 04:49:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 88234476-a377-3ca3-9dca-3ef3080fea9c | -6.51704 | -43.24567 | 2025-09-15 04:49:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c0b8932c-663d-3fb7-8837-2deecb3173f7 | -6.52662 | -51.19111 | 2025-09-15 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eb20ae0c-92b6-3b49-8318-009625ec7383 | -10.80133 | -45.98637 | 2025-09-15 04:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 675dcd82-8d00-307c-bbbf-507b867b88db | -7.30405 | -46.57231 | 2025-09-15 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b124c412-0581-3046-8965-aebfa2a74588 | -8.78495 | -46.04004 | 2025-09-15 04:49:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4e619655-272f-33c4-ab5a-d329ec2699b2 | -6.40407 | -42.62095 | 2025-09-15 04:49:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7f518adb-4177-32a6-a644-f34f2b82e4b4 | -6.52607 | -51.19458 | 2025-09-15 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b65d79ce-bc5e-3c35-ad59-c7365c30977e | -9.91376 | -50.29685 | 2025-09-15 04:49:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dd4af265-34da-3f3c-9bde-4e05f21cb4d5 | -8.63808 | -45.69064 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 444cc206-b3d8-3889-bd96-c7f925ac845f | -5.18812 | -45.17426 | 2025-09-15 04:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a23e60ad-6af7-3e41-8b9d-2df0da622166 | -8.59716 | -46.36189 | 2025-09-15 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5d7b93dc-3ee7-3d2c-9aa6-7b02039613d0 | -8.9925 | -45.78905 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f795d1da-3bba-3487-aca1-d81c577b6b2b | -6.91824 | -46.15969 | 2025-09-15 04:49:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aff52f2b-f636-3f34-87de-a544e87451f6 | -7.8837 | -43.56657 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 67.5 |
| d0c8ba29-7a7c-356e-9cf6-3436360f748b | -5.47719 | -44.69264 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 46f599f9-5ea2-3585-b6c1-2665c160ede3 | -7.89421 | -43.56255 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 46faf403-5871-3d18-84ec-9cd42f7527f3 | -8.91619 | -45.5022 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| fc5b9f59-ba3e-39a9-978c-95474bf08db1 | -7.69324 | -48.86035 | 2025-09-15 04:49:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f3741035-9867-32d9-8fe4-968c3793396c | -6.20099 | -55.63329 | 2025-09-15 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c2cfc9cf-d439-3ab1-88ac-0b45a527994d | -7.51816 | -44.66846 | 2025-09-15 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0416eeee-5fba-33a7-bb9e-dbae5e7f3d4e | -7.98882 | -45.6628 | 2025-09-15 04:49:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 409fa3f9-b092-3547-931f-b7ea5b749286 | -6.55149 | -43.99114 | 2025-09-15 04:49:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8b1f010a-391f-39ca-9349-d17c74b0aa21 | -7.73094 | -45.30965 | 2025-09-15 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4fc7b3f6-e1ec-3664-950d-a88ea78d737c | -8.4207 | -44.9657 | 2025-09-15 04:49:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fe3316cd-bb00-327b-aa38-14f5fee81dd6 | -10.68796 | -46.25159 | 2025-09-15 04:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3187f415-eb2e-386c-8df0-b521db8ecfef | -9.91431 | -50.29319 | 2025-09-15 04:49:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 44e91c98-14d8-3787-9829-5867e4d45777 | -4.63961 | -50.93185 | 2025-09-15 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bcf9e30c-050a-3372-8ce9-3fb39ee2f38a | -7.49794 | -44.67291 | 2025-09-15 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 32b19032-cb29-309a-9b4d-ec34e379eb58 | -9.0529 | -47.01842 | 2025-09-15 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4b0774d9-867b-3a9a-ae02-2a4d6eab257c | -8.99307 | -45.78503 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ccb7464f-e5c0-30a6-a6c4-b5d68e95f261 | -8.64715 | -46.36209 | 2025-09-15 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 04c920f0-6b73-3f2a-866b-b1f50a8efa37 | -6.157 | -41.17904 | 2025-09-15 04:49:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4a0afbf4-6eb3-37cc-82c6-3b35ef55bc90 | -8.96225 | -45.79459 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1caf29d1-4858-379c-8020-10b5764e9e8e | -9.09129 | -50.27228 | 2025-09-15 04:49:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d7a5565a-fb62-3487-893f-ed2a820c4298 | -8.9838 | -45.82008 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4c2efe62-896d-386c-87c6-b1d45d2933cc | -7.05634 | -43.89018 | 2025-09-15 04:49:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba6dfa35-2633-3c4c-addf-3a601ca66a3c | -6.66852 | -45.54865 | 2025-09-15 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2c1ce757-5198-331c-b70f-fc090836b138 | -5.28774 | -45.25554 | 2025-09-15 04:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a43c11ab-76a4-3bd6-a210-089d0f6ca87c | -8.91067 | -45.51003 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 55db6f58-d041-34ea-bdbe-8b4ae03e045e | -8.91972 | -45.4768 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d93a2d7c-89ff-3e94-a5c3-a7ad321bb415 | -5.18392 | -45.1707 | 2025-09-15 04:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a7738a7c-a4ae-3397-8069-015005cabe03 | -9.00998 | -47.03751 | 2025-09-15 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| da90d377-a86e-357f-9e63-7370c02da65b | -6.4193 | -42.60827 | 2025-09-15 04:49:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9e2b5c56-b1a1-3037-ad15-35c051421377 | -10.78887 | -45.98093 | 2025-09-15 04:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f8f35cb3-1ddb-39ee-bdbc-f4f481a83e56 | -7.39326 | -49.99715 | 2025-09-15 04:49:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b3a1e737-c742-34c1-bf3d-f70675eebaf6 | -7.05985 | -44.11782 | 2025-09-15 04:49:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e618e794-f809-302a-b83f-a2d47dfb2161 | -10.63822 | -46.23649 | 2025-09-15 04:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 028bc457-65d7-3eb7-9520-9ca811573bfe | -7.84921 | -43.85567 | 2025-09-15 04:49:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0f9f1195-d5e8-35bb-ab95-23f1fe9e8e2d | -8.91299 | -45.49331 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9dc8a888-ced1-3289-86cc-2b59ee422edb | -8.41973 | -47.22653 | 2025-09-15 04:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b3963c5f-8699-3de2-a672-7a4e6393043d | -6.40567 | -46.94594 | 2025-09-15 04:49:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 26b637b6-49fe-3d4e-b70e-2d6e2503c43f | -6.9202 | -46.17439 | 2025-09-15 04:49:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6a63d48f-cdf7-364d-b5a1-65da3f60010d | -9.10031 | -44.8089 | 2025-09-15 04:49:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 58db5e12-4d07-38f0-a818-3e7e27fddaa8 | -7.69318 | -44.67862 | 2025-09-15 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 37daf0a3-3a1b-33ae-8b95-ac4ff4d855c7 | -8.19178 | -47.12461 | 2025-09-15 04:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 83a6ab89-9a4c-39d4-a136-ad66a643db9a | -6.4074 | -42.61899 | 2025-09-15 04:49:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bcc3fad0-0674-35ad-8419-83f5182cbf45 | -7.48243 | -46.12386 | 2025-09-15 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5e84d6f1-6e71-35dc-b909-46ca2583c478 | -5.84591 | -44.16879 | 2025-09-15 04:49:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 4aac8cac-d014-3f55-bd7f-6fb799e39054 | -9.00207 | -47.03933 | 2025-09-15 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ffb8f035-590c-3b94-bc7e-36606a570931 | -7.39774 | -49.9905 | 2025-09-15 04:49:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9637744f-3049-3f62-925c-b445a243c191 | -6.66797 | -45.55245 | 2025-09-15 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b0a414a3-4a64-362f-a965-eeb8824d055f | -10.86447 | -45.4574 | 2025-09-15 04:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| de0003b4-fb46-3baa-8f1d-169c19f01124 | -6.40327 | -46.93606 | 2025-09-15 04:49:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fe03ae84-69a9-3b87-a25f-a42468b0ff55 | -5.76481 | -43.92588 | 2025-09-15 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c3cb3628-0e9e-33e1-903c-9be93001b3fa | -7.8714 | -43.56941 | 2025-09-15 04:49:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2f84e4ee-5f21-398d-b502-9b4e88ce5eaf | -5.28356 | -45.2549 | 2025-09-15 04:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ed34ea85-c3d5-3931-a5ab-2961f04e02df | -8.96516 | -46.22229 | 2025-09-15 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9365ec49-22e2-303d-a367-4eafd93d8918 | -8.98435 | -45.81616 | 2025-09-15 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ac6d40e0-0b85-3775-a140-593c49eddccc | -9.00329 | -47.0562 | 2025-09-15 04:49:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README40.md)
