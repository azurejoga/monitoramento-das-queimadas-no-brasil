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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0f783f99-4be5-3bfa-96f8-ad4ede924f9d | -8.54867 | -55.2848 | 2026-08-24 04:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c1e6c16-6cc3-3cc6-8ef2-1a4b615ea349 | -9.37251 | -45.41285 | 2026-08-24 04:25:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f4b8a48f-5616-3953-968c-581550e510c1 | -12.27641 | -43.13258 | 2026-08-24 04:25:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b1d40874-74f7-34d8-8154-3df2b8f02626 | -7.48491 | -45.13558 | 2026-08-24 04:25:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7430f4f7-88a2-3742-a869-a96a3c057830 | -7.26079 | -44.19155 | 2026-08-24 04:25:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 272fa562-1eea-3d90-a794-35b22c21e277 | -12.21445 | -43.1751 | 2026-08-24 04:25:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| a1470a02-1e44-3ac9-8cdc-b3a578e17620 | -10.72801 | -47.97878 | 2026-08-24 04:25:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d84f1f62-cef9-3d09-af11-e1f9e5b6aa35 | -7.36155 | -45.82752 | 2026-08-24 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 68a7d6f7-32d2-31ad-a008-a9d36f6a9c72 | -5.07078 | -49.37934 | 2026-08-24 04:25:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 385be38c-68ae-32f5-8cdf-2709b75e6230 | -11.5777 | -46.95778 | 2026-08-24 04:25:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4c1057c5-7765-3527-9b0e-59c2faf11c93 | -7.28638 | -45.3665 | 2026-08-24 04:25:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 29ab9016-30f2-323a-9cd7-d989171a53d2 | -11.9861 | -45.5028 | 2026-08-24 04:25:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d64540bb-ae33-387d-87ca-f6dc92a36060 | -8.3119 | -47.58353 | 2026-08-24 04:25:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8e071633-e01a-3154-a860-77f4e423887e | -8.07256 | -47.25983 | 2026-08-24 04:25:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b4844fad-e3a4-34c1-91dc-025931354a86 | -11.00593 | -45.21659 | 2026-08-24 04:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b2b5a1e-bf8e-3230-a59c-49d9d13e4f5b | -7.9758 | -45.25537 | 2026-08-24 04:25:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fbd6e11e-3fac-3df8-a2e1-900e758aec6a | -10.45708 | -46.21995 | 2026-08-24 04:25:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ca9050c3-a1b4-388c-8f6b-11b5ca8343bb | -7.28295 | -45.36593 | 2026-08-24 04:25:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c9e194ee-de53-3809-be4a-c0a094dbd910 | -12.15964 | -43.39738 | 2026-08-24 04:25:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 96d104e1-2d13-3ace-8db2-8dd4933fa4f0 | -6.59937 | -52.45661 | 2026-08-24 04:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aba613f4-fd05-3b93-98d8-8d7221c1c0fa | -4.73614 | -49.28316 | 2026-08-24 04:25:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f3a54e5c-081b-37b8-ae26-23619a4a414e | -6.83903 | -52.50394 | 2026-08-24 04:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 04ba6e1e-70a7-39dc-859a-9a93fd11452c | -11.11692 | -49.8857 | 2026-08-24 04:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a777fd73-601a-34d1-985a-ae5510bc04ef | -11.36087 | -40.05663 | 2026-08-24 04:25:00 | NPP-375D | CAPIM GROSSO | BAHIA | Brasil | 2906873 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d14819d3-a745-35f2-8f85-252b376d6b77 | -5.9515 | -51.96633 | 2026-08-24 04:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6553030c-cb6b-3722-a0ec-e10fd3b2370b | -7.83288 | -47.65006 | 2026-08-24 04:25:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b1b9fae-b89d-310c-a48b-b96a7f942ce5 | -8.31476 | -47.5863 | 2026-08-24 04:25:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f7ff00e6-33d6-36b4-988b-67494683ad05 | -6.44986 | -41.55305 | 2026-08-24 04:25:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 30ee5c82-9602-3b26-881c-0a6d85735e92 | -6.39758 | -43.83412 | 2026-08-24 04:25:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| e341e469-4c49-39ae-a503-549cac9b7489 | -8.54368 | -55.28681 | 2026-08-24 04:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8e828094-02ea-3862-87ed-74657b150a44 | -6.84376 | -52.50825 | 2026-08-24 04:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 936ddb58-d6a5-3566-9c92-571d389fcbf8 | -4.99922 | -56.14132 | 2026-08-24 04:25:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0b770fef-f807-3a4b-b786-089de570813e | -9.71609 | -46.02599 | 2026-08-24 04:25:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a183c34-0732-3f39-9c3f-3657f87adc5a | -7.65121 | -42.73447 | 2026-08-24 04:25:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c2fee587-3cff-320b-aa38-1473aa5a75ee | -7.97561 | -45.27799 | 2026-08-24 04:25:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0438aa53-5140-3cb7-8583-cb471ba00a4b | -7.15209 | -42.78531 | 2026-08-24 04:25:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 205a9098-9c70-3ea1-88f4-370b24c0dcf2 | -8.10448 | -47.48251 | 2026-08-24 04:25:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8d8150b4-0b6f-32d9-9a3d-4f75c68278f0 | -6.18278 | -53.52781 | 2026-08-24 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 536feea0-db4a-31d3-be9e-412eb5e509c2 | -7.29092 | -43.00439 | 2026-08-24 04:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 61389edd-9e85-3e41-9478-e64fc2de3847 | -6.19503 | -53.5235 | 2026-08-24 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 381179f9-a96c-38b4-8139-9093ab6789a1 | -7.13989 | -42.78354 | 2026-08-24 04:25:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 65005ec2-a4e1-34be-9e0e-6f3d44dc9b2a | -10.0099 | -46.82488 | 2026-08-24 04:25:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 512c2f31-7025-3617-a646-c75b326b1805 | -11.10637 | -46.18258 | 2026-08-24 04:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 95a14778-124c-32d1-bd4d-ce50d20cd67d | -11.57839 | -46.95372 | 2026-08-24 04:25:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0bbff1b2-9d0c-3c97-988d-96b5e0fe9799 | -8.56378 | -47.44319 | 2026-08-24 04:25:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 43f5d5c8-addd-3c6a-ba08-d74cb0da4634 | -7.16587 | -42.74087 | 2026-08-24 04:25:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 516c9033-6eff-32c7-999c-5b5fdb638ac3 | -10.62745 | -52.25353 | 2026-08-24 04:25:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 300ae05e-4979-3bff-bd93-044f230b8443 | -5.873 | -52.10727 | 2026-08-24 04:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 23666046-1068-3656-818f-2b114a04d1c5 | -6.70354 | -52.09098 | 2026-08-24 04:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e932f8f3-4f86-3f2f-88f5-8561886f4c5b | -7.36917 | -45.82481 | 2026-08-24 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 56f39236-91bd-3189-9ddc-11bb3d31d44f | -7.25034 | -49.86517 | 2026-08-24 04:25:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 0a3379ef-211d-3ebc-b5ef-22a4e984b964 | -8.09694 | -47.48137 | 2026-08-24 04:25:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 89616e2c-c80b-3c24-9d2e-4fea13012a96 | -7.36885 | -45.80484 | 2026-08-24 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 97c6d0cc-59e9-344f-bc68-e7443c4a976d | -10.86325 | -50.98383 | 2026-08-24 04:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e2f9f55d-c722-314b-ab38-7379b86bbf01 | -5.47187 | -44.41996 | 2026-08-24 04:25:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc142d7b-0d54-34ba-b142-363d3c2e9e95 | -6.35109 | -54.76332 | 2026-08-24 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6644f3b9-377f-3f2d-be65-67fb6ae8c89e | -4.93941 | -45.79828 | 2026-08-24 04:25:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4cebc49b-803a-3847-bdc8-77e282315fc3 | -10.6923 | -47.74005 | 2026-08-24 04:25:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1432cbec-0987-3b0b-bf42-7f1287d54008 | -13.43104 | -39.88533 | 2026-08-24 04:25:00 | NPP-375D | ITAQUARA | BAHIA | Brasil | 2916708 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 08675b36-4f90-314f-b34c-bfa5f60caf5f | -9.30191 | -40.22197 | 2026-08-24 04:25:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f40bd779-fbaf-306b-aa66-b618b86ff558 | -10.79993 | -50.94838 | 2026-08-24 04:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 78f0773e-fbdb-370c-b78e-f8de0883e46a | -7.25407 | -49.8701 | 2026-08-24 04:25:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f27371cd-9d08-3129-82d8-e031e91a012d | -7.2937 | -43.00839 | 2026-08-24 04:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 609df21f-4543-3aff-8559-a3bf556b05ce | -5.8788 | -52.1053 | 2026-08-24 04:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a4b0c51b-6127-3a5f-b500-4a841b628f70 | -11.62018 | -51.09595 | 2026-08-24 04:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| db60428d-53f2-35f4-82bf-518ba7164e90 | -6.39481 | -43.8301 | 2026-08-24 04:25:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e9ad2131-66a8-3a90-b416-95018955c8ba | -9.03076 | -50.7505 | 2026-08-24 04:25:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 71f3f533-3cb4-397c-b2ae-a42a8756694e | -12.15627 | -43.39685 | 2026-08-24 04:25:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 041bdc17-0ef3-369b-b680-b74e5a8c20bf | -10.69965 | -47.74143 | 2026-08-24 04:25:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7607b53d-81da-39eb-82a8-6e9523b0c632 | -7.35362 | -45.81028 | 2026-08-24 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8fb2b3ed-34eb-3ae4-a2a1-4b612bbc9474 | -7.35806 | -45.82693 | 2026-08-24 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 9c96576c-430d-393c-aa06-4304f54f62fd | -7.9752 | -45.25904 | 2026-08-24 04:25:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 7897a129-ada1-3ff0-a65b-cec651d489d4 | -7.2407 | -49.86811 | 2026-08-24 04:25:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c94ee961-d9b6-3a14-9970-1d6bc6a94b98 | -9.72672 | -46.00436 | 2026-08-24 04:25:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 57bc6eb0-5572-3e1f-a98b-ceab5c39e32b | -7.14818 | -43.09181 | 2026-08-24 04:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ae61fd6f-eaaa-356c-bb3d-73c70619a684 | -9.04654 | -50.7681 | 2026-08-24 04:25:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 507ebcaa-101c-39a4-8713-4176d806d6e4 | -6.78644 | -44.65821 | 2026-08-24 04:25:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 743d3ba0-16e0-35f7-8db4-0dd6cc04c22b | -7.29038 | -43.00786 | 2026-08-24 04:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| b13c2b63-3158-34ca-a37b-30df012c6688 | -10.47254 | -49.5186 | 2026-08-24 04:25:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d9614584-d9c9-39cb-b2b7-ff52042e251a | -6.78897 | -42.77456 | 2026-08-24 04:25:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e1ad29ce-356b-3816-971b-5da266b577b7 | -7.24833 | -49.87687 | 2026-08-24 04:25:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f5cecd1c-37b8-331e-8739-c7c5c71ebdc9 | -7.16258 | -42.76185 | 2026-08-24 04:25:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8e6d70ca-f872-30bf-b43a-68527746e913 | -7.65011 | -42.7415 | 2026-08-24 04:25:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0cf953fc-c44e-3eda-b78c-cf5b54a71333 | -5.91833 | -43.63657 | 2026-08-24 04:25:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f275fc53-ed25-32db-ba5e-79410ba30773 | -8.34116 | -47.70549 | 2026-08-24 04:25:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d059ea69-1fa4-3956-8485-3450944b22bc | -6.43114 | -52.75772 | 2026-08-24 04:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6dc265cd-0c6f-3a90-a7eb-476ce5234274 | -9.61636 | -39.31725 | 2026-08-24 04:25:00 | NPP-375D | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 103f3ce7-75bf-3158-ae71-48a7a9891afe | -7.974 | -45.2664 | 2026-08-24 04:25:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ee673a25-311b-3dcd-ae82-d15d1104978a | -9.75062 | -43.30351 | 2026-08-24 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6db7e5f9-0bef-35b1-b471-95028d5975dd | -5.00022 | -56.13567 | 2026-08-24 04:25:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bbbe0370-708e-306f-a099-8550de070dd6 | -7.26429 | -49.9177 | 2026-08-24 04:25:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 9e0719cc-4b75-3b08-8a28-4128376f62f7 | -7.25481 | -49.86578 | 2026-08-24 04:25:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 086507c3-097f-33f4-9f1a-5a3db08dbdfb | -9.71728 | -45.97572 | 2026-08-24 04:25:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2028cec7-1160-3538-be4c-729b608bda99 | -8.11062 | -47.49053 | 2026-08-24 04:25:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2a692d58-52df-3467-9432-4eaac6d512d5 | -7.2948 | -43.00143 | 2026-08-24 04:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 5328e1dd-fada-3af6-8e69-757d4ddb08b0 | -10.73175 | -47.97941 | 2026-08-24 04:25:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c27e1f9c-9196-39b3-a56e-9af33bdaa00c | -6.84026 | -52.49708 | 2026-08-24 04:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 047478af-1e71-392a-83ba-3f45d3b54e4b | -6.35198 | -54.75847 | 2026-08-24 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9255762f-8aff-335a-83ed-d14799a2d19d | -11.98552 | -45.50639 | 2026-08-24 04:25:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2b536ad5-4722-385e-8125-9c2a107f2b62 | -7.30529 | -42.9781 | 2026-08-24 04:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |


[Clique aqui para ver as próximas entradas](README17.md)
