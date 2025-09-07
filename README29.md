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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1ab21f5f-3ead-3b63-9281-e3ce76b8c388 | -11.59948 | -47.16269 | 2025-09-07 03:57:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 1aba3fdb-c106-3c42-b3ff-fe57eeb8b6fb | -6.72147 | -45.15248 | 2025-09-07 03:57:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a5e03b9d-cccb-3884-a495-79f460b39f73 | -10.58566 | -48.46893 | 2025-09-07 03:57:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0c9cb49f-46f5-34aa-95b3-155e163639e2 | -13.05388 | -48.06015 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b6b25ffe-3591-3fc6-9673-1ec920a1f17e | -8.03502 | -44.09013 | 2025-09-07 03:57:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 689b7e2a-add9-3665-8d4b-a09d3fc722ff | -6.88296 | -45.60811 | 2025-09-07 03:57:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 423cc734-bb4a-3aa9-ae19-712eea641fa1 | -7.74359 | -48.81517 | 2025-09-07 03:57:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3cd75ac4-aef7-38ea-82a6-3c91ab80d84f | -8.03574 | -44.03712 | 2025-09-07 03:57:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bf0e0b35-cb44-3dd7-b942-d13f12aeba94 | -13.05467 | -48.05352 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cbea8dca-f67c-34be-a43a-ac059906d9ae | -11.40391 | -43.62738 | 2025-09-07 03:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 79c10dcb-b883-38e0-9dbb-b6a5b52a3114 | -13.39807 | -42.41773 | 2025-09-07 03:57:00 | NPP-375D | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5a3cdb5a-f6e5-3593-8449-db324007cd4c | -8.49504 | -45.11175 | 2025-09-07 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d3ae4cfc-ae82-31d7-882c-3815786b8fa5 | -11.14778 | -48.36658 | 2025-09-07 03:57:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1600c16b-ae54-3fcf-ac1d-794d2b56a118 | -8.68492 | -45.28499 | 2025-09-07 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| da337d54-afa7-317f-8eec-cec9402a0736 | -6.53834 | -44.82666 | 2025-09-07 03:57:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 511bec60-89ad-3c83-a503-3aaa9f9309aa | -6.60107 | -43.97769 | 2025-09-07 03:57:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fe30e3d1-8a41-30c1-ad76-509c97dc207d | -11.80881 | -48.23529 | 2025-09-07 03:57:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ae4a6068-0962-3d53-be3d-0b7a8c3fb190 | -11.40801 | -43.60358 | 2025-09-07 03:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 69cd856f-7ddd-36f4-a061-24f0235e9cd3 | -7.74212 | -48.81597 | 2025-09-07 03:57:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 257a2346-5c68-341a-a752-4b8bc3f2214c | -10.38212 | -44.96688 | 2025-09-07 03:57:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| bc869dda-722c-33da-b350-059331d44651 | -8.68205 | -45.28701 | 2025-09-07 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| db4d88da-0fdc-3090-b41c-690d3d2eb3af | -10.57749 | -48.47149 | 2025-09-07 03:57:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 36c04d37-c541-3e31-9ebe-b6a994e4b6f9 | -7.80738 | -45.43674 | 2025-09-07 03:57:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 59d958e6-02a4-3db9-84fe-41448a2f2d5e | -6.43294 | -43.6164 | 2025-09-07 03:57:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1de52119-b041-3bed-b686-a5168e615058 | -10.74624 | -48.18286 | 2025-09-07 03:57:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b462848d-1f8a-3e3f-9527-e9f685912c8e | -11.14368 | -48.38788 | 2025-09-07 03:57:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dfc18164-9fce-3e02-8fe3-56390f3dbfd7 | -7.01019 | -44.94027 | 2025-09-07 03:57:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 96b85a14-61e7-3244-aa68-577e1e54a5f6 | -12.612 | -44.63496 | 2025-09-07 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 751a5a1e-ae15-37d7-a4d0-68ebde791cb8 | -12.35125 | -43.78894 | 2025-09-07 03:57:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 714da7a3-054c-39ff-9576-8e6c22f3c825 | -6.22398 | -43.57328 | 2025-09-07 03:57:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e7e57e69-5109-3661-a33d-0dce8cd871c0 | -11.58651 | -47.17251 | 2025-09-07 03:57:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c201c1a1-ae15-3da8-b749-8af69c4ff6fd | -11.57038 | -47.74662 | 2025-09-07 03:57:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| da63fc67-048c-3256-8a61-90d60c159b84 | -11.57841 | -47.73096 | 2025-09-07 03:57:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0ba99d13-631e-3db6-b23a-83a261b689e3 | -11.90275 | -46.64946 | 2025-09-07 03:57:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9b048e90-e458-3e74-88ae-30ae7c8a808c | -10.06847 | -49.29883 | 2025-09-07 03:57:00 | NPP-375D | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 6e829367-4d92-3675-b0cc-6aeb47617a6a | -11.40226 | -43.63694 | 2025-09-07 03:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c1aebc6f-a032-3ead-8d40-ff2069ec306e | -6.60201 | -43.99793 | 2025-09-07 03:57:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 8a358ccc-6019-3bae-b429-d250c3dbc880 | -10.72729 | -48.5971 | 2025-09-07 03:57:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be10f3d1-8213-3ac1-8e84-98845cac8a62 | -8.31199 | -44.97805 | 2025-09-07 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dc9ac6c2-9d37-363f-ae11-cf874778e5b9 | -6.59495 | -43.98832 | 2025-09-07 03:57:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 62934c96-1553-3bc3-8bcb-72123489e133 | -7.67589 | -50.29725 | 2025-09-07 03:57:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cff4327d-8071-36a6-8882-745bb5552309 | -10.80676 | -47.73832 | 2025-09-07 03:57:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 45df409e-a460-3512-b169-354db68eeb6f | -9.97448 | -51.65961 | 2025-09-07 03:57:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e8bdb1a1-1e76-3da4-ac2a-f07df48f9fb0 | -10.05713 | -48.06405 | 2025-09-07 03:57:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eb8bc18a-3f5a-3a31-b679-dcd5daee19eb | -6.19612 | -43.37102 | 2025-09-07 03:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 776fc7fb-e417-32af-b5f2-80bfd0803a0e | -11.61458 | -47.155 | 2025-09-07 03:57:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6d097c6e-9956-3fa5-a834-bdfb79f243cc | -8.6835 | -45.30531 | 2025-09-07 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1587dfff-b944-335c-8102-9834784bcc8e | -10.58506 | -48.4722 | 2025-09-07 03:57:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1348f5c8-8a0a-33ff-b64f-fe36003b094b | -10.74088 | -44.35364 | 2025-09-07 03:57:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 467407dd-1d1c-3f7d-8db2-be75a5c4ab8f | -12.61971 | -44.61475 | 2025-09-07 03:57:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 235f386a-e9ce-3e96-b1b3-dbb17b81a49e | -6.20031 | -43.58788 | 2025-09-07 03:57:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c5747b18-8672-36bd-a59e-387c954bb0d3 | -11.40256 | -43.61234 | 2025-09-07 03:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6e400c98-633d-3f41-9c59-16ea074f1c1e | -8.68795 | -45.30608 | 2025-09-07 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c657ee45-594e-3ea3-ad16-4ae72c67138b | -11.38731 | -43.5416 | 2025-09-07 03:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7d612903-7e95-3d06-8616-a53f5e033974 | -13.82506 | -43.85983 | 2025-09-07 03:57:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 66dfb445-5bb5-3787-a915-4df74b946a87 | -10.43266 | -42.533 | 2025-09-07 03:57:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c325dd13-8eaa-30ff-accc-18f2f2d616e3 | -7.74996 | -44.01173 | 2025-09-07 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| b38c5619-e545-300b-8ef8-acf420a7456f | -8.46229 | -47.3364 | 2025-09-07 03:57:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7cbc92a7-f3ba-3900-b394-44a57d7da433 | -11.58422 | -47.7555 | 2025-09-07 03:57:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f703dc88-b14c-3d5c-8a27-9935cb33f274 | -10.34295 | -46.46069 | 2025-09-07 03:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 367534ea-c8e6-32b7-975b-dd7645d7c298 | -12.82542 | -48.01678 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 64fef532-8b0b-32e9-b6f6-ed47be0a516c | -13.02964 | -48.05272 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e7cc1e1e-84f0-3ba0-aaca-bc5214b426c4 | -6.27498 | -43.49532 | 2025-09-07 03:57:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 531890ab-643f-3c37-b8ed-4f2a6e32901f | -6.6024 | -43.96978 | 2025-09-07 03:57:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 880daeee-90df-373c-ba06-3c1ea371e47f | -8.89212 | -47.2561 | 2025-09-07 03:57:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a858956c-eee4-3369-abbe-a8c0d6b8091c | -7.54566 | -45.35127 | 2025-09-07 03:57:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bb4e595b-d032-33ea-beda-a9ae6dcd0679 | -10.14986 | -48.74653 | 2025-09-07 03:57:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 46bee127-4c53-3655-9a1c-b8c5e9aebeb3 | -7.01838 | -44.95745 | 2025-09-07 03:57:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 663becd1-f14e-3f99-894e-f458586d5bbd | -8.4305 | -47.30803 | 2025-09-07 03:57:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 62d27f76-9463-3b3f-9574-9fe221f2090f | -13.03958 | -48.07941 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 574db893-0e49-3b64-9cda-c186e88a9817 | -11.14276 | -48.369 | 2025-09-07 03:57:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cc7bd392-89e3-3ea8-86ef-84b054287fd5 | -11.41372 | -43.63905 | 2025-09-07 03:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a31548da-2f67-3f3d-a457-c70aab772554 | -12.94027 | -48.03411 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 97d4837a-ab11-3a4b-b468-189a82321242 | -13.04234 | -48.04023 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f5a12379-d62a-38e5-a068-6c81fd80bc74 | -11.79867 | -44.94087 | 2025-09-07 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b398a2f6-a8b1-35b4-8e5c-284c0f64c237 | -7.67225 | -47.32797 | 2025-09-07 03:57:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 059cdc30-7198-3ad8-84cb-a0aac9a1081e | -8.15273 | -44.85667 | 2025-09-07 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d6d2274a-078c-30a8-af27-bc5212693604 | -6.65792 | -44.81075 | 2025-09-07 03:57:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b100ef31-54c7-3e45-8948-e13475e4ee6e | -6.59408 | -43.9678 | 2025-09-07 03:57:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 51f01d53-cab5-3c70-b440-5a83dcd617ad | -9.77941 | -46.89088 | 2025-09-07 03:57:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 40a30182-2cf7-34a0-b556-d097e6a90bdb | -10.58283 | -48.47239 | 2025-09-07 03:57:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d4874f82-93fd-397c-8bbd-6db339c446a6 | -8.93423 | -48.65154 | 2025-09-07 03:57:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e7bef4c2-e205-3f64-bf8e-1fc70ea59fea | -13.0396 | -48.08078 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 81eb6dfa-4029-3f70-ac80-658a79633e45 | -10.60567 | -44.33956 | 2025-09-07 03:57:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b012d0b3-dc3a-3d6c-8c3e-cc880a3905b6 | -8.48804 | -45.1765 | 2025-09-07 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 38f4f94a-3df3-38ee-95ab-10a4bae6ee27 | -12.54737 | -48.07243 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c017237c-b04a-3542-bcbf-784bb2e8aa61 | -11.30091 | -46.54096 | 2025-09-07 03:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 450c61b1-73ce-35fb-b183-2a3b2d50dd0d | -6.43706 | -43.61711 | 2025-09-07 03:57:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 40f86406-2463-3f9e-938b-bcbbb9dda45b | -8.45657 | -45.0264 | 2025-09-07 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 13.7 |
| d97d3125-e929-3872-93de-b1b62f82e1a1 | -11.59911 | -47.15828 | 2025-09-07 03:57:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 3fef24fb-6f5c-3891-b183-85e45e6a9559 | -7.75059 | -44.00807 | 2025-09-07 03:57:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 682cefd9-7f0a-3293-93bf-1008d02d60c6 | -6.60377 | -43.96164 | 2025-09-07 03:57:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 58a07b5e-5f9a-3882-8ba4-ac6f1fe12bfa | -6.19961 | -43.37525 | 2025-09-07 03:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1a05c21a-68c7-3880-9685-e08c8320c631 | -8.67266 | -47.45099 | 2025-09-07 03:57:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8838d026-289b-3d83-ad3f-ea0801a45f03 | -11.31849 | -46.54919 | 2025-09-07 03:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e31e767f-c9d6-3a5c-a84d-4a9a19d12f5a | -13.04455 | -48.0818 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f18dcd79-4776-3f9d-aeff-6d2aa76a5b42 | -9.88075 | -39.96339 | 2025-09-07 03:57:00 | NPP-375D | JAGUARARI | BAHIA | Brasil | 2917706 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 271fc76d-d3bf-39ad-9acb-8655b5b565a7 | -7.89386 | -44.92102 | 2025-09-07 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 34721772-93bb-367b-b6bb-95f8bfabfbf4 | -11.15409 | -48.39021 | 2025-09-07 03:57:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e724f3b3-a7c3-3e99-9083-201e978ca1df | -11.34381 | -43.50787 | 2025-09-07 03:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README30.md)
