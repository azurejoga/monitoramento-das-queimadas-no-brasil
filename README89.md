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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c4f853d0-80e2-3c8f-8051-9a28938abbe1 | -10.5462 | -50.43619 | 2025-09-03 05:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 43593287-3e3e-31a1-abf6-90dce55f5a67 | -8.36421 | -48.31519 | 2025-09-03 05:14:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ff1f0f6f-7f4a-3e8d-9649-5570c517bd0a | -14.97112 | -50.21201 | 2025-09-03 05:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5324343d-d44f-38b8-b671-7b0279490e16 | -7.68692 | -50.27433 | 2025-09-03 05:14:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| edb53689-56eb-333b-bf52-7a6d5178bb14 | -12.63852 | -57.00571 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 697447fb-44da-37d7-9c23-57d9238705f6 | -12.63225 | -57.0009 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2df1a0ba-4be8-3ab5-aabe-04f8e2ea0669 | -9.34783 | -55.2275 | 2025-09-03 05:14:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8934e80-612f-390d-8572-68a5a60264ea | -12.63567 | -57.00143 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1f32c302-8cc2-3883-bca5-8a41cbfa8689 | -9.6265 | -47.06169 | 2025-09-03 05:14:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dc9c17f0-0c6e-31b7-a953-797f63ae5f0f | -9.34194 | -55.21839 | 2025-09-03 05:14:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d349288-ae4e-319c-b0a1-e10be53786d2 | -11.8497 | -51.52316 | 2025-09-03 05:14:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 732869ba-28b7-3f14-a382-f67339422722 | -12.63339 | -56.9934 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 865bdfa7-c075-3fc5-a5f4-02c454b3fc30 | -12.89784 | -56.94846 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2b9baad5-30d4-3230-86b6-ffab6c971667 | -10.08952 | -54.7672 | 2025-09-03 05:14:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8bc2bc84-e3e0-3894-83b6-15a8d6efce74 | -11.86585 | -51.47164 | 2025-09-03 05:14:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0b338e4c-bb18-3b29-9d4a-eaa2bc0d7e83 | -12.93556 | -56.95449 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 6ccc0727-f7ee-3ca0-b4cd-2b43c9657fb7 | -11.91017 | -50.61633 | 2025-09-03 05:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 201731e3-bcbd-3bc6-8c96-1ec566274211 | -13.78 | -47.45477 | 2025-09-03 05:14:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| be123874-c3d1-3833-8ca8-777c4d6a94d3 | -9.62502 | -47.0647 | 2025-09-03 05:14:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e139f958-0ebc-3910-92be-064d183b9b64 | -14.84115 | -46.69361 | 2025-09-03 05:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e30a5c55-05ad-3700-8e36-2dec01def518 | -11.86185 | -51.46616 | 2025-09-03 05:14:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b8cbc09e-7f9b-3306-9b92-02806e83fb58 | -13.0921 | -57.11681 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 117c2f9a-bd51-33ab-981b-14eea70e3fca | -13.69997 | -46.93718 | 2025-09-03 05:14:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1b68d261-978e-3c65-936f-382c31f4c9b7 | -9.75568 | -46.91663 | 2025-09-03 05:14:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5f499afc-157d-3da8-a43e-094eef7fca2b | -14.83313 | -46.69558 | 2025-09-03 05:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| a67c670d-7294-3aa8-a15a-46c0b7f13437 | -10.46723 | -53.62702 | 2025-09-03 05:14:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23dd39f5-9a97-31ca-ae8f-f1ef4f12b358 | -12.98207 | -54.76538 | 2025-09-03 05:14:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26ae75b6-bcdb-38ec-ad93-488143497fc6 | -12.90926 | -56.94255 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 439140da-8d7b-31ca-ae26-0528ff89b2ec | -10.47666 | -50.3483 | 2025-09-03 05:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6b361c5e-c2c1-37e3-9688-1dbfb6fef9d5 | -11.86494 | -51.55011 | 2025-09-03 05:14:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 25cba9c9-9b79-3c0f-a877-0028890cfab1 | -11.61265 | -52.14055 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 14527631-53ea-30bd-9e0e-ccfb2ba2622a | -10.2497 | -61.76087 | 2025-09-03 05:14:00 | NPP-375D | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d96da4cd-6307-3a2c-a4e0-a9097664ff75 | -10.09076 | -54.75857 | 2025-09-03 05:14:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 69db1200-f38b-3b58-aff1-1d03df6eba2e | -10.04344 | -56.10124 | 2025-09-03 05:14:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 01c2dcee-d1ba-3466-9040-167a1ba6ec4e | -11.02961 | -45.06823 | 2025-09-03 05:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ba97d063-4c8a-389c-95d7-b38f43b4e696 | -12.92625 | -48.08792 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b90c7603-5634-3390-9d35-aba2e096c3dc | -12.94073 | -56.99001 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 3297fa60-e5d4-373a-80ec-f4cc69f9612e | -9.63453 | -47.03868 | 2025-09-03 05:14:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e14fafb0-3355-30ed-9d4a-95912274ab25 | -14.97862 | -50.19308 | 2025-09-03 05:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 530c1b70-d821-3d4d-a231-9601ead5f1d9 | -11.62648 | -52.138 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 75ddba30-a182-3fd9-8edc-be8d8b31fd0b | -10.12953 | -47.43897 | 2025-09-03 05:14:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a0152bd1-752b-3e05-875b-7563a49d2a52 | -14.34445 | -52.79674 | 2025-09-03 05:14:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0433fb89-6223-361b-ad24-4f17b8c18fbc | -13.49562 | -51.80914 | 2025-09-03 05:14:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a8153f1c-e190-34e0-9efa-ddf08163e84d | -11.86969 | -52.4187 | 2025-09-03 05:14:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c82f7499-a73d-36f2-8dc2-32dd60fc4726 | -12.92068 | -56.93661 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 64ae344f-3de1-399c-818f-eb8f1140ea0a | -14.79391 | -48.20103 | 2025-09-03 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f5821fff-27ee-399d-b8da-5caf6055bb27 | -9.4631 | -60.3167 | 2025-09-03 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 31b894e2-8faa-396a-9429-bf7cfc87d450 | -13.51145 | -47.0315 | 2025-09-03 05:14:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 072150b0-88af-3309-a90f-6ad059722e14 | -11.66522 | -57.35334 | 2025-09-03 05:14:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf789469-1f6d-3812-a8dc-801ec71b8a42 | -11.61156 | -52.08279 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf1f210c-63f4-3c60-b1f8-2abcf80d5b01 | -12.87512 | -48.03582 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 019c6253-26fb-3698-a201-2e35d3571c43 | -12.63624 | -56.99768 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d66fe0d6-6b48-3914-8472-e744a31f451e | -13.00574 | -48.10958 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 408ae8a4-667d-3c95-9e88-51ae9bb07158 | -14.77009 | -48.13927 | 2025-09-03 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6b3ba357-e05b-3395-aca4-1035411fc071 | -12.62542 | -56.99981 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7f34b92d-ef5d-30ab-b31b-6d2b3e08d5d0 | -9.75023 | -46.9155 | 2025-09-03 05:14:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 381545f2-e697-3ee4-bb62-2398d5adb38d | -12.90321 | -48.10091 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 41a31d9e-deb6-3fee-8572-7c0c83a538de | -12.8701 | -48.02753 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a938fbf8-19e6-3ddd-8109-5d8a18783afd | -10.94292 | -50.77321 | 2025-09-03 05:14:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fd630c97-9cd0-3202-a778-adb0a6dfac8a | -12.51579 | -49.57516 | 2025-09-03 05:14:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2c781947-a067-3f55-a647-72f01fffaf33 | -13.51089 | -47.03654 | 2025-09-03 05:14:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 467954d0-36a6-3640-a16e-fabd9f6d0f2a | -14.80383 | -48.22149 | 2025-09-03 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2a7e6207-b7a0-3ce3-81df-cf358d3fa1ac | -11.44178 | -47.30236 | 2025-09-03 05:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0961d792-cf09-3ec2-aee3-c5f48177bd22 | -7.7152 | -50.24693 | 2025-09-03 05:14:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d0435667-f834-3286-abf7-259632b9daa4 | -11.62707 | -52.1337 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 759992cc-4608-355e-811e-dff77156fd8e | -13.20659 | -51.80941 | 2025-09-03 05:14:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 369fdf6b-e20b-304c-b43f-01e2942074c5 | -11.92224 | -46.66772 | 2025-09-03 05:14:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6af08e20-3cb3-351d-b0e9-fe5210ad151f | -10.54693 | -50.43076 | 2025-09-03 05:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1589eccd-9fa0-383d-90e4-393ed2086041 | -8.38198 | -48.30721 | 2025-09-03 05:14:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| afe57053-45f1-39b9-9d03-f52c18025303 | -9.33656 | -55.22992 | 2025-09-03 05:14:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a77c170b-3f26-38b1-b69d-403dadb4a39b | -14.98127 | -50.21674 | 2025-09-03 05:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f6d20eb9-51da-311a-9282-bcd145920411 | -12.91449 | -57.00127 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 76cacf2c-7ab7-32af-ae89-fb7d1c1f8431 | -10.28184 | -54.26132 | 2025-09-03 05:14:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1580cfd-ec7d-38d2-b822-1776ad26a145 | -14.31079 | -53.09277 | 2025-09-03 05:14:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5cb690dd-8d05-3d46-b02f-55835ab7e1b0 | -14.98824 | -50.06136 | 2025-09-03 05:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8b4e8900-5c06-3f68-83e0-f44d762ac568 | -9.94725 | -51.62151 | 2025-09-03 05:14:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eee34dd4-a9a9-3233-bce1-08c3628959ad | -9.42141 | -48.35822 | 2025-09-03 05:14:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 838cc784-a4d8-3c7d-a73c-4e98627d8612 | -13.70635 | -46.93807 | 2025-09-03 05:14:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c5e519cc-c5de-38b3-8745-b94e96826495 | -14.976 | -50.21601 | 2025-09-03 05:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b9eb53d6-ee31-3433-965e-45c0c129786a | -9.76909 | -50.0153 | 2025-09-03 05:14:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 22f9d4ed-c754-3246-9f83-5618048027a0 | -11.80988 | -50.64109 | 2025-09-03 05:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| af0f61f1-59d5-3662-beb7-e8a15d095495 | -11.06725 | -52.08187 | 2025-09-03 05:14:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f3df330b-69e4-3ea2-ad2d-67afee5e6da6 | -13.33821 | -46.83263 | 2025-09-03 05:14:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0474ca85-f0ed-3f55-b8e1-b8b790e2774f | -6.79285 | -58.99715 | 2025-09-03 05:14:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 943be691-b25e-3915-87d0-41110b8079f8 | -12.91612 | -56.94364 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 55b00708-8a0c-3cc0-b560-06aad28aa290 | -10.99551 | -46.83149 | 2025-09-03 05:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dc6dd929-8253-3368-bf20-cc81eb52436b | -14.78059 | -47.51897 | 2025-09-03 05:14:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4d1ad041-f326-39e9-8193-d4a8498dd5b0 | -11.06285 | -52.08134 | 2025-09-03 05:14:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c370e93c-000e-30a4-941e-3118fafaff0b | -8.82392 | -52.01162 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 35ddd5dd-9dbd-3c65-8742-ca8654e34e1b | -11.62904 | -52.05416 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac3e57ed-6fe8-3dd1-b459-c27e14955f74 | -13.08986 | -57.13181 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e302e03-691b-35c6-99c2-0b2305f75d01 | -12.99481 | -48.11489 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c4c6362e-eeba-3166-811a-a17d4f77bd8f | -11.61395 | -52.06532 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fdc4f014-4cb2-3429-9196-242ee980c248 | -11.58737 | -52.12821 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 21985d37-bb04-3617-b837-f79018410818 | -13.00665 | -48.10162 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a5639cb0-7636-3340-a908-10eaf630f82f | -13.21058 | -51.81489 | 2025-09-03 05:14:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ad34b5b1-ea2e-3e25-988c-74e735f66500 | -6.43973 | -58.13303 | 2025-09-03 05:14:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92336928-cb07-3b7e-b494-d39c1404dd8d | -9.64175 | -47.03041 | 2025-09-03 05:14:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7a9ba81e-82d6-3087-abb4-1fcdffd1622e | -11.12103 | -45.11788 | 2025-09-03 05:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 58bbfc58-ac55-379a-ad71-668e314c82a2 | -11.57625 | -49.90652 | 2025-09-03 05:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README90.md)
