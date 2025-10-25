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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4ab77e0b-185d-3bcd-b8fd-dee1349118d4 | -6.79677 | -46.46558 | 2025-10-25 03:57:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 575fee7a-0bca-3e21-aa2b-a7c341ec623d | -6.44856 | -44.28363 | 2025-10-25 03:57:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fcb71e12-817f-30bf-84e8-76d3a76cf699 | -6.76321 | -44.20856 | 2025-10-25 03:57:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9450358d-4b3d-341b-9f8e-7aa2214ff720 | -6.01619 | -38.43545 | 2025-10-25 03:57:00 | NPP-375D | PEREIRO | CEARÁ | Brasil | 2310803 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d1150af2-2f1e-3b3d-acaa-4c53879b129b | -5.01704 | -47.15426 | 2025-10-25 03:57:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 159e5f1c-c491-339f-a321-ae2b12625c95 | -3.16139 | -49.17351 | 2025-10-25 03:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d4a51527-f2de-3247-8503-005ff91d06bc | -6.9657 | -43.50259 | 2025-10-25 03:57:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e55cf16c-43b5-313c-bb57-788ac7904502 | -8.10992 | -44.49874 | 2025-10-25 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e1d3b5b1-28c8-3457-8f46-c4fb2de384e7 | -6.88864 | -43.6137 | 2025-10-25 03:57:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 65c8e927-de82-3577-99c8-40c01f9708e5 | -5.54466 | -46.53009 | 2025-10-25 03:57:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6dffe9f6-b600-3e69-b2e2-f103652ab132 | -6.06813 | -42.14873 | 2025-10-25 03:57:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2cd3eed9-3481-36a4-a3c0-6d76ab984f33 | -7.79412 | -45.40231 | 2025-10-25 03:57:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 24b323d2-3848-336d-a0c4-e26f6d4b89b7 | -4.25749 | -44.57832 | 2025-10-25 03:57:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| a98b1b2a-2c9c-3c45-b3e3-9d5bd9d487c7 | -5.70475 | -49.31872 | 2025-10-25 03:57:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9fb12eb6-b22b-3123-8a30-72d5b6be477c | -7.54179 | -42.51678 | 2025-10-25 03:57:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| be7b1678-9bcb-3f54-b5de-4eb419ec0b24 | -6.82015 | -45.44072 | 2025-10-25 03:57:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3ad01a7f-b7ef-3cd1-92ea-648b41a465f9 | -6.88803 | -43.61733 | 2025-10-25 03:57:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1ef37b1c-30a5-3a33-8dd8-229547867a56 | -7.84989 | -40.41016 | 2025-10-25 03:57:00 | NPP-375D | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 437ce236-e642-3e4a-938e-56fbbc554e9a | -5.6528 | -45.97368 | 2025-10-25 03:57:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5127dc2d-31e8-30ac-b13f-74ac2c44108e | -3.60285 | -45.97778 | 2025-10-25 03:57:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| daac0a12-357c-37d8-9779-d3725dfbf42c | -7.14947 | -44.12392 | 2025-10-25 03:57:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6589e186-c257-32ec-b09f-b98595730a5d | -3.42952 | -50.26304 | 2025-10-25 03:57:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0ad615ec-fb4a-3627-8f28-ce5ae0b6495f | -6.10322 | -40.58828 | 2025-10-25 03:57:00 | NPP-375D | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 1e3ae014-223e-3124-977e-34d957506697 | -5.54691 | -41.37977 | 2025-10-25 03:57:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a7290786-2b31-3b85-b4d6-3e465af2e9f1 | -5.54517 | -46.52719 | 2025-10-25 03:57:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ab77a387-7b87-3235-894a-f2891afc7a24 | -6.83337 | -41.55186 | 2025-10-25 03:57:00 | NPP-375D | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9f3dd7f9-a250-335e-8470-1058876092f9 | -4.81537 | -45.58035 | 2025-10-25 03:57:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f3e7906e-b7d5-399d-b6a9-4672f0b31599 | -6.36254 | -44.27221 | 2025-10-25 03:57:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 35696d0e-532b-3b79-be4e-1e096a5afde3 | -5.72445 | -49.0951 | 2025-10-25 03:57:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 476f48af-f3d8-3de2-9f01-95030810f40a | -4.25671 | -44.58285 | 2025-10-25 03:57:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 91601112-4225-39fe-9108-fc6cfb4b5537 | -4.27373 | -44.39068 | 2025-10-25 03:57:00 | NPP-375D | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ae772598-47d9-3c31-8bf3-eb738f6d0458 | -5.54676 | -46.52673 | 2025-10-25 03:57:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eef511df-5f76-30fb-a148-be6270b91420 | -5.46911 | -40.87408 | 2025-10-25 03:57:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 49450840-8370-3a26-9d8b-a3fb1b079c57 | -6.59375 | -42.07813 | 2025-10-25 03:57:00 | NPP-375D | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 807c9c26-4460-3f60-870a-d72aa7f16904 | -6.92502 | -45.16072 | 2025-10-25 03:57:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 257efd02-b755-35bb-ae82-acf88351c8e3 | -3.99275 | -50.52743 | 2025-10-25 03:57:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa68904d-b9a6-324b-a474-f7b38d970acc | -7.93704 | -43.21019 | 2025-10-25 03:57:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5e4349a2-51b2-356e-b1ad-7794748f7622 | -7.16494 | -45.84129 | 2025-10-25 03:57:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| be9742d7-f278-37a1-8146-572d51100eaa | -4.80254 | -46.73962 | 2025-10-25 03:57:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54113811-5e63-31ab-8358-252d19886792 | -1.48757 | -47.81432 | 2025-10-25 03:57:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b481f53b-b300-36d0-b777-f1c6e48a149b | -9.67227 | -35.82933 | 2025-10-25 03:57:00 | NPP-375D | MARECHAL DEODORO | ALAGOAS | Brasil | 2704708 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f5a7089a-2f75-38bc-bce6-94ab83819c37 | -6.30259 | -40.87618 | 2025-10-25 03:57:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 599a70be-e9fd-357b-aa56-13133cfefd9e | -7.93776 | -47.20143 | 2025-10-25 03:57:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ca8bdeff-58e8-3d9d-a5d7-b6341c42c511 | -3.86612 | -51.89248 | 2025-10-25 03:57:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d8466b03-08d5-3de7-bdda-539ef6ba3465 | -5.29872 | -41.14175 | 2025-10-25 03:57:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 91671de6-b698-3efa-a8b3-b547fba22b51 | -6.24003 | -46.39669 | 2025-10-25 03:57:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9d342b57-1b9d-3578-bb77-ceacc411464d | -4.27004 | -50.51207 | 2025-10-25 03:57:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c9ab532e-e092-3246-ab90-8038cc42a9a9 | -4.25194 | -44.57989 | 2025-10-25 03:57:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8a234bfe-a02a-3a46-b005-b7145c387729 | -6.10511 | -45.85237 | 2025-10-25 03:57:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 26a1c432-b47d-34cb-9160-7decbda356e7 | -3.91775 | -47.68774 | 2025-10-25 03:57:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 95e31305-0da7-3fc5-8f42-a4aab41c9d3c | -6.12939 | -41.72346 | 2025-10-25 03:57:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| aaf4606e-f61d-3fd2-86c6-8b47c0d0fe0c | -3.15517 | -49.17234 | 2025-10-25 03:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7d6e953c-dae5-35c7-9a22-1ee8d420a6bf | -3.70526 | -40.42397 | 2025-10-25 03:57:00 | NPP-375D | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 51e4f44d-ac11-3712-b5c6-4e9db5e38233 | -4.24816 | -44.57455 | 2025-10-25 03:57:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ab56d8d0-9dea-3dc4-baaf-ac2aab06aa7e | -7.63863 | -42.16732 | 2025-10-25 03:57:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ee3d1b63-317d-3336-bbee-aa792f150028 | -2.89674 | -41.63262 | 2025-10-25 03:57:00 | NPP-375D | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8eaaa155-0a57-3a05-910b-34e9641e0989 | -5.61222 | -41.1225 | 2025-10-25 03:57:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| dafeab5e-687a-3d72-837e-f9ab7f751ada | -4.8313 | -37.25645 | 2025-10-25 03:57:00 | NPP-375D | ICAPUÍ | CEARÁ | Brasil | 2305357 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ece9d886-d642-3465-852d-dc8e9a7601cf | -6.16556 | -47.09085 | 2025-10-25 03:57:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3806c219-4ae7-3ddd-bb0e-2724825eaea9 | -7.79372 | -45.39906 | 2025-10-25 03:57:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2bddfb42-8e73-3427-b625-408267383f71 | -6.9381 | -43.64044 | 2025-10-25 03:57:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5531db9d-24a1-3ddd-ae5f-9ccf1d2d1d07 | -1.49345 | -47.81527 | 2025-10-25 03:57:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7698f441-6a69-3fa1-a363-c41cdecaebce | -4.81449 | -45.58558 | 2025-10-25 03:57:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a63f119d-9b68-3c96-a251-6012f5166506 | -7.78093 | -45.39245 | 2025-10-25 03:57:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| be822d76-3e64-3086-a0df-60d01d804d79 | -4.59755 | -49.58545 | 2025-10-25 03:57:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| edf8dc91-6815-3f64-b526-88204f973c7e | -2.26311 | -47.84852 | 2025-10-25 03:57:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8e01c149-ce5f-35ef-a7b2-73e8bf14f590 | -7.48282 | -46.88068 | 2025-10-25 03:57:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 02c9ed5c-5755-30b0-a8bd-88aa7a68623e | -4.55867 | -46.68994 | 2025-10-25 03:57:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a667d7a0-4cef-30df-973f-cc873ba8f517 | -4.24891 | -44.57001 | 2025-10-25 03:57:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 12c39b75-4167-3b60-a10b-2304264f91e7 | -3.11982 | -51.21427 | 2025-10-25 03:57:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c8f1095f-fcaa-3e94-bddf-4d550232b489 | -4.77771 | -46.50529 | 2025-10-25 03:57:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b2c6fa77-5e55-3d36-a9b0-01a610701345 | -5.67175 | -46.65543 | 2025-10-25 03:57:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e08436c4-5ccb-37bd-8ef0-5e2915665601 | -5.54616 | -41.38751 | 2025-10-25 03:57:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b16b4355-0e56-3b7d-b8a8-abea70ae5c1b | -7.7847 | -45.39756 | 2025-10-25 03:57:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4c9ad6a3-4488-35bd-a8d1-5b81024e494c | -7.58901 | -43.58137 | 2025-10-25 03:57:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fa302516-25e2-3faa-a28c-df3167fd963a | -4.22762 | -48.60837 | 2025-10-25 03:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c1416423-dced-37e0-927d-b4d530df8589 | -5.03562 | -41.19706 | 2025-10-25 03:57:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5c9f1feb-7969-3025-96cd-0eb6b8c85777 | -6.12799 | -41.7321 | 2025-10-25 03:57:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0b2945c8-addd-33e8-858b-42198dfe1242 | -1.49412 | -47.81107 | 2025-10-25 03:57:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 55d25724-7668-3db4-90c5-171b145158ff | -5.45867 | -46.4134 | 2025-10-25 03:57:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 265e6ac0-7f6b-316c-9c04-2fedfe661af0 | -3.11777 | -49.1043 | 2025-10-25 03:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f2d608c9-1abd-342b-895b-fffe61677b28 | -6.1431 | -44.73715 | 2025-10-25 03:57:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b79a6e62-17f1-3500-a108-12af10fc2154 | -7.65081 | -44.57797 | 2025-10-25 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc2c06a4-71c7-3400-9af8-b92831d8ce6b | -7.78923 | -45.39819 | 2025-10-25 03:57:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 979b3386-90e1-31ad-b793-ca2487375985 | -6.92023 | -43.49851 | 2025-10-25 03:57:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8e900f35-6070-3575-ae96-25198a911e89 | -7.18473 | -40.2889 | 2025-10-25 03:57:00 | NPP-375D | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1c3e1757-0faf-3bbf-905a-01b554824049 | -5.29325 | -48.36892 | 2025-10-25 03:57:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 435409ff-2696-3a27-99bc-933c1cc794b5 | -7.49208 | -47.03483 | 2025-10-25 03:57:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 27135a76-3c4f-38e2-878a-949a1e9b4947 | -6.31859 | -41.86743 | 2025-10-25 03:57:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 00542cd4-43aa-3166-9283-c20168629b4b | -6.2563 | -47.03301 | 2025-10-25 03:57:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b553da55-5866-3152-a8bc-ce7dd1148898 | -4.55842 | -46.69025 | 2025-10-25 03:57:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9ba38008-7bed-3068-9cf1-925ef45e173c | -7.58501 | -43.58065 | 2025-10-25 03:57:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a4874c57-a665-3c08-8235-ac999d95c9dd | -8.59961 | -44.81695 | 2025-10-25 03:57:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f60da73b-33c9-384e-bc0e-bb64eb7fbd49 | -6.80413 | -42.39463 | 2025-10-25 03:57:00 | NPP-375D | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d468049d-fae7-3667-8706-524306a96deb | -5.68278 | -42.76989 | 2025-10-25 03:57:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| b2156779-4a98-3008-8dc9-70b0d7f3bd34 | -2.79834 | -49.14333 | 2025-10-25 03:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 04c55e75-d517-35fd-9cb9-5b1d39eba00d | -6.2209 | -42.53928 | 2025-10-25 03:57:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b9790294-cdd4-3fa9-8cb7-610b8362fea1 | -8.6046 | -44.81359 | 2025-10-25 03:57:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| db426e1c-1bbb-3cd9-994b-1ef13e148dd5 | -5.58028 | -41.31622 | 2025-10-25 03:57:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 23144dde-9867-3efe-9c8c-29269dd28582 | -4.60463 | -47.02206 | 2025-10-25 03:57:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |


[Clique aqui para ver as próximas entradas](README15.md)
