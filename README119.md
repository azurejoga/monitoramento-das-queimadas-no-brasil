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

## Dados Diários - Página 119

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7f2ac073-0f64-3477-a803-2c1d9cd479e6 | -23.14122 | -49.65563 | 2025-09-12 06:12:00 | AQUA_M-M | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 28.7 |
| ad68f895-0a02-3937-b2ef-9bb6fea53956 | -11.5425 | -50.5947 | 2025-09-12 06:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 50.8 |
| a05d4aac-8fa5-3d29-9b29-ccf0391159c0 | -11.79 | -50.5664 | 2025-09-12 06:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 74c96452-7804-3745-a6aa-02abe13df140 | -12.9292 | -54.7538 | 2025-09-12 06:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 44ffe64f-04d3-36d3-b645-191ca2257f6e | -11.809 | -50.5642 | 2025-09-12 06:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 3f4586fc-b9fc-3d50-8c0f-14e9d7210013 | -11.79 | -50.5664 | 2025-09-12 06:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 09eec4ed-9b63-3d87-9448-a6e0d2bc9cbd | -11.5425 | -50.5947 | 2025-09-12 06:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 91f1f24f-6011-35f3-8b9a-8b05f0f059bd | -11.6567 | -50.5817 | 2025-09-12 06:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.5 |
| e7fa1216-f3a8-3fe6-9064-0eedaca05d34 | -15.9068 | -51.803 | 2025-09-12 06:30:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 3bc9f68c-dfce-3abc-bb32-b019c0a6faa8 | -11.809 | -50.5642 | 2025-09-12 06:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 2ed72db4-497d-3b14-91a2-3da4c86179f9 | -15.9268 | -51.7785 | 2025-09-12 06:30:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 61.2 |
| bd83a8b7-b224-38a6-86d8-51344b01f07f | -15.9264 | -51.8001 | 2025-09-12 06:30:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 57.8 |
| a8d8fd06-8a73-391f-90ee-ffe950f2e421 | -10.0884 | -50.3862 | 2025-09-12 06:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 31505f17-da1e-3346-a036-213104bb19dd | -15.9073 | -51.7814 | 2025-09-12 06:30:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 6464a2ee-e3e3-3cf9-9bb4-0d8681871370 | -11.5428 | -50.5733 | 2025-09-12 06:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 30e74be7-8565-3408-9b67-c4ab502586bc | -9.9004 | -51.8811 | 2025-09-12 06:30:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 05067b92-8079-3832-a724-d74ee1f66298 | -11.6809 | -46.631 | 2025-09-12 06:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 5ee26145-7605-3887-b692-f562373434b2 | -11.7008 | -46.5832 | 2025-09-12 06:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 7f4d4a65-eb7d-338e-9f4d-9b9da6b55311 | -9.9007 | -51.8602 | 2025-09-12 06:40:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| a706e10d-f50e-30e5-9d29-e97f4cd749c9 | -15.9268 | -51.7785 | 2025-09-12 06:40:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 89c8ae7d-e0b1-3fb8-bbde-349d0949bd24 | -11.79 | -50.5664 | 2025-09-12 06:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 952db6f9-33d7-32cf-b6fe-ec28699a7709 | -10.0884 | -50.3862 | 2025-09-12 06:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 108.8 |
| 617e54ae-9518-39d8-aee5-e44bd3c2bb30 | -15.9068 | -51.803 | 2025-09-12 06:40:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 9f6de0bf-f99c-3a82-adff-52d24553aa36 | -15.9073 | -51.7814 | 2025-09-12 06:40:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 0f50f90d-fcc8-374a-99ec-68aed442454d | -11.6813 | -46.6084 | 2025-09-12 06:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 193.4 |
| fa697ca3-cb88-3255-a754-d55c7182e5ec | -11.6817 | -46.5858 | 2025-09-12 06:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 170.1 |
| 3e097c08-f8f7-3d67-91c7-0f8429ac1d1c | -11.7005 | -46.6058 | 2025-09-12 06:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 147.2 |
| 6f858fe2-3d51-3e97-b891-a8c7c85f96ab | -11.5238 | -50.5754 | 2025-09-12 06:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 27174f6e-572c-3f52-8c9d-7fd981ba9b73 | -11.5428 | -50.5733 | 2025-09-12 06:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 54.9 |
| ac163a41-8724-3cd6-b607-2cb72d618e70 | -11.809 | -50.5642 | 2025-09-12 06:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 47.1 |
| cfd3e938-382a-3ab2-8cab-bceece48bc3e | -9.9004 | -51.8811 | 2025-09-12 06:40:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| bd8d7fe8-a9fe-3497-971c-8226b20c169c | -11.7001 | -46.6284 | 2025-09-12 06:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| fc128739-0c1d-309c-acd9-e441f5d18326 | -15.9264 | -51.8001 | 2025-09-12 06:40:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 77.4 |
| baffdcd5-1974-3214-99fa-2bfa1050f06c | -11.7903 | -50.545 | 2025-09-12 06:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 8b1228b5-452a-3ae3-938c-cdeda9625e71 | -9.9007 | -51.8602 | 2025-09-12 06:50:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 0dc98609-69dd-3d61-87f3-e74c46d9891c | -15.9264 | -51.8001 | 2025-09-12 06:50:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 59.5 |
| a7305e41-ecdc-336c-a6ab-a11e705b897b | -12.9292 | -54.7538 | 2025-09-12 06:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| b8bedb5c-5a08-3f2f-8f97-a8fb6a0384c9 | -11.809 | -50.5642 | 2025-09-12 06:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 104.2 |
| c0c754f9-bd31-32d7-9fa4-f4e8ce057acd | -15.9268 | -51.7785 | 2025-09-12 06:50:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 79.8 |
| c770cb16-69a5-30ed-b0aa-c861c779397d | -10.0884 | -50.3862 | 2025-09-12 06:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 141.2 |
| 79be714f-752d-32ba-bccf-dac9704ec5e8 | -9.9004 | -51.8811 | 2025-09-12 06:50:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| f9a65bfa-b195-315e-b0ac-a136496a13dd | -11.79 | -50.5664 | 2025-09-12 06:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 97ac7482-8776-3b47-a3a0-a7590a6a0532 | -15.9264 | -51.8001 | 2025-09-12 07:00:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 78.7 |
| bfcce7e3-b750-3b42-a563-5c9d284f8095 | -10.3509 | -50.5089 | 2025-09-12 07:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 47.1 |
| f59aaa3c-b41c-34b6-8fa9-0195f601b1cf | -15.9268 | -51.7785 | 2025-09-12 07:00:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 97.9 |
| cc8559de-509f-3b9e-afe0-ba1659bd1b9f | -10.0884 | -50.3862 | 2025-09-12 07:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 110.4 |
| c42545c7-fb5e-3e4a-ad18-c3b5d448d51d | -9.9004 | -51.8811 | 2025-09-12 07:00:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 359291c1-0f74-3ad2-ba63-e8af5d6c259c | -15.1406 | -50.1409 | 2025-09-12 07:00:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 2267e8e4-2be4-3a3a-b583-7dcb696c1da0 | -11.79 | -50.5664 | 2025-09-12 07:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 5ad707e1-506d-3bea-a389-7616214d2928 | -10.3699 | -50.507 | 2025-09-12 07:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 52.9 |
| db2b7edd-60df-332a-9fea-4a99d2a291fa | -9.9007 | -51.8602 | 2025-09-12 07:00:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 6a30ffe0-f6b2-36a8-948e-281b225496b6 | -14.1713 | -46.2045 | 2025-09-12 07:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 1f3f260e-183c-3ea5-9c95-e0613e6ad2d9 | -15.9268 | -51.7785 | 2025-09-12 07:10:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 9588d713-5bfd-3601-8c80-46e0ea0f1a42 | -9.9007 | -51.8602 | 2025-09-12 07:10:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 80.6 |
| b4425733-f618-3b28-950b-934e8939b048 | -11.6377 | -50.5839 | 2025-09-12 07:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 51.4 |
| ec51defc-cb15-378d-81c5-76758c5ba4fc | -11.771 | -50.5686 | 2025-09-12 07:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 42.1 |
| ad0f2070-0ebd-3cbf-9d2c-ab144bdd7613 | -9.9004 | -51.8811 | 2025-09-12 07:10:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 37acd46a-1b2c-3303-b2ef-1ec4a00faafa | -19.2402 | -48.0496 | 2025-09-12 07:10:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 40.2 |
| d31fbbe5-fdc1-3d9a-ab8f-9550eac1dfdb | -11.79 | -50.5664 | 2025-09-12 07:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 6445f1c8-806b-3d49-a52b-b8d8c65a758c | -12.9292 | -54.7538 | 2025-09-12 07:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 68beddbe-e369-3b57-a155-31ff051e1a33 | -10.0884 | -50.3862 | 2025-09-12 07:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 50.7 |
| ca6339a8-9f8c-31f5-a686-2e940dda5772 | -14.1713 | -46.2045 | 2025-09-12 07:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 57.6 |
| d739341d-1860-3819-bd44-4ad96f48ca4a | -11.79 | -50.5664 | 2025-09-12 07:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 48b646da-5b35-32e8-a925-b31add64fb0d | -12.9101 | -54.7558 | 2025-09-12 07:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 6989f2a2-2b9a-3b5f-aed1-d7bace23d5b1 | -12.9292 | -54.7538 | 2025-09-12 07:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 354b7398-3f82-3507-a70a-bcb1c2394bd6 | -12.9292 | -54.7538 | 2025-09-12 07:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| de071c79-8604-3b97-a50a-1a1c35c04847 | -14.1713 | -46.2045 | 2025-09-12 07:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 95893d06-eb86-3815-8c46-a03ff695dcbd | -9.057 | -47.0355 | 2025-09-12 07:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 26.8 |
| e9e03243-38b8-3801-9d39-eae40d4a398a | -14.1713 | -46.2045 | 2025-09-12 07:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 6a049585-0d88-3ef9-b885-c1e7b66f560a | -9.057 | -47.0355 | 2025-09-12 07:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 9fb6809d-5cf1-3988-a882-49cf6af38818 | -12.9292 | -54.7538 | 2025-09-12 07:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 0d60253c-d626-31f1-8625-b8ad8127c914 | -15.0246 | -50.1148 | 2025-09-12 07:40:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 44.7 |
| e87ba27a-385a-32d4-a297-d7fe716b1c82 | -12.9101 | -54.7558 | 2025-09-12 07:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 1fee506a-8109-3e8c-a117-2df42d4ffbe2 | -12.9292 | -54.7538 | 2025-09-12 07:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 85.9 |
| fdc1f529-4771-33e7-a984-c51a51ba282b | -12.9294 | -54.7333 | 2025-09-12 07:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 30.6 |
| b742fe3b-4570-3a07-95a6-1296724cd09c | -12.9101 | -54.7558 | 2025-09-12 08:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 37.5 |
| ea16e723-cba0-3524-9d88-27cb9fb61d0f | -12.9294 | -54.7333 | 2025-09-12 08:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 970c0488-3de1-3ca9-a18f-09d4f9d92eac | -12.9292 | -54.7538 | 2025-09-12 08:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 2fe90526-b455-3ef3-b4ae-da27e7634ef5 | -14.5132 | -53.8949 | 2025-09-12 08:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 83afaca6-f34a-39e3-a8a3-1c43430a5c3b | -12.9292 | -54.7538 | 2025-09-12 08:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 3e5e0cf2-b34a-3431-ab27-060dad0c6cb7 | -11.9713 | -51.164 | 2025-09-12 08:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 45.7 |
| fd9ef512-076c-3f8d-8583-7f1c40c1fa19 | -14.5128 | -53.9158 | 2025-09-12 08:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 569648f6-b53f-3cfa-b919-4c8b3fc745c6 | -8.9478 | -46.7354 | 2025-09-12 08:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 15e4177c-7a81-3f9f-90f9-004c0cc9f84b | -12.9101 | -54.7558 | 2025-09-12 08:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 3a579da4-c059-3a0a-83d7-01c7f3732ded | -12.9292 | -54.7538 | 2025-09-12 08:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 51.9 |
| e882db55-1855-3fb6-b745-aaa7cc691c7c | -14.4133 | -52.9221 | 2025-09-12 08:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 133.2 |
| 04a390ec-8238-3c08-bc00-18a0fab3cde3 | -14.5128 | -53.9158 | 2025-09-12 08:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 45.1 |
| c4dc2550-e40c-385c-bf8f-8aabd87f8e0f | -9.0376 | -47.0819 | 2025-09-12 08:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 650f9b69-3d36-3f36-b846-22a5bda03250 | -14.413 | -52.9432 | 2025-09-12 08:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 217e3032-65bc-3fe1-b846-e87c1f4f5a52 | -9.0379 | -47.0597 | 2025-09-12 08:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 5dd84db7-2b17-3ad4-8749-856da3e38d53 | -14.3937 | -52.9456 | 2025-09-12 08:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 96724de4-02e5-3744-a485-d591ebb47a53 | -12.9101 | -54.7558 | 2025-09-12 08:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 874cf5f1-8e57-33f4-bce8-568598ff903f | -14.5132 | -53.8949 | 2025-09-12 08:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 94.1 |
| f3cf12bf-cf5e-3340-8d16-3a827fe1157c | -14.394 | -52.9245 | 2025-09-12 08:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 1b146e79-ad5c-3df2-9058-4755910fb442 | -12.9101 | -54.7558 | 2025-09-12 08:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 900f2288-3c90-3ffa-986d-2cb6a22c811f | -14.4133 | -52.9221 | 2025-09-12 08:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 13092f5d-21c6-3ca3-bf10-c9a7327967f7 | -11.9523 | -51.1661 | 2025-09-12 08:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 962a6912-8b8c-3a38-bc1f-bf2ffa3920aa | -14.394 | -52.9245 | 2025-09-12 08:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 5ff41032-16d2-31ca-87da-dc25036f88d5 | -12.9292 | -54.7538 | 2025-09-12 08:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 88.3 |
| fe2b6374-3383-3069-a412-32050367a97c | -14.5132 | -53.8949 | 2025-09-12 08:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 56.5 |


[Clique aqui para ver as próximas entradas](README120.md)
