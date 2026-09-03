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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5b7db804-c7c2-39ac-887e-4a9fecdf46d0 | -8.70587 | -52.36027 | 2026-09-03 04:02:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5d108a0f-6ff2-3356-acb1-73363d0a2164 | -9.4153 | -45.6129 | 2026-09-03 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4dc6ebb8-9c9c-3ec8-b662-4610ca759d61 | -9.59794 | -40.34354 | 2026-09-03 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| eb7299c5-919d-3832-9c0a-a60910c23a94 | -6.95123 | -45.20985 | 2026-09-03 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1b18a1e4-70b7-3a24-8610-6b0e9c4a9ebd | -8.87939 | -41.24258 | 2026-09-03 04:02:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2655b68d-fe00-3e9d-b26d-5d66c0bae4de | -10.87533 | -45.31696 | 2026-09-03 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| bda7a14b-3bc8-3d6e-9c12-bbb2f96e6354 | -10.99996 | -45.08263 | 2026-09-03 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d97ee67e-73cf-3f8d-9563-aca51898c9c8 | -8.08727 | -50.9851 | 2026-09-03 04:02:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 190b6f2c-cdf5-3431-8ae2-da113dac887d | -3.97175 | -41.5254 | 2026-09-03 04:02:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6f31142d-79d4-3e3d-a784-3973304146ee | -10.88325 | -45.31183 | 2026-09-03 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4313d702-1acd-3bf3-b8e4-a25a417f8e83 | -8.4703 | -54.64737 | 2026-09-03 04:02:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 50f156f7-2070-3f6b-a4e1-783cb238e4a8 | -8.51622 | -37.8948 | 2026-09-03 04:02:00 | NOAA-21 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 67b178f8-1ee5-34a4-8351-fa0294606dff | -10.77849 | -44.74065 | 2026-09-03 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b36a6e5-83a1-3dc0-a088-e68465956f57 | -4.94642 | -47.65612 | 2026-09-03 04:02:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1e0365e-5260-3b21-9ac7-242b8770fa2b | -8.79339 | -47.985 | 2026-09-03 04:02:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4a23f975-7ba1-35f1-88ba-efa99b16fccb | -3.21699 | -48.81239 | 2026-09-03 04:02:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b794907a-82b1-30c1-8361-cc7d81423c1a | -8.07994 | -50.99246 | 2026-09-03 04:02:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1a52aadc-a7d9-305c-84af-b8e5e41538e7 | -7.07489 | -44.35915 | 2026-09-03 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 67b941f0-1a2f-3012-baf3-3d54f08a125e | -9.61134 | -40.34564 | 2026-09-03 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 93eda124-0ba5-3ad9-bf1a-179ca330c13d | -7.12044 | -45.82107 | 2026-09-03 04:02:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dad070a8-5e90-3a56-ad4a-fae9bc543b7b | -3.97292 | -41.51794 | 2026-09-03 04:02:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| df1c52a4-8ac9-36bd-b17f-056b7caecfc2 | -10.88705 | -45.31251 | 2026-09-03 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| a6ec1de7-84b7-32c5-ba32-35235468b9a9 | -7.82628 | -47.67141 | 2026-09-03 04:02:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 50e4ad7d-44ce-3255-9d86-ebe1b161cec0 | -5.4189 | -44.80334 | 2026-09-03 04:02:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa34336a-c95f-398c-8ac6-2647f025486b | -9.41312 | -45.61023 | 2026-09-03 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8c7be35e-8039-3f72-9b79-b56b69fd0e8d | -8.08148 | -50.98405 | 2026-09-03 04:02:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 01794ca3-4eda-344c-babe-b1b1d870f271 | -6.67696 | -43.41819 | 2026-09-03 04:02:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4045611b-9b83-3a32-87cc-1539b4fa30e0 | -10.87152 | -45.3163 | 2026-09-03 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| af8a3a5f-55e7-35dd-b11e-8c293189b771 | -2.82943 | -48.65464 | 2026-09-03 04:02:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07313e79-5f1b-3269-99a0-e5db02754b17 | -3.80613 | -49.11265 | 2026-09-03 04:02:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ebef051d-de20-3df9-aaf4-2c13fb77f296 | -5.20802 | -38.03528 | 2026-09-03 04:02:00 | NOAA-21 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c9b2c53c-496d-398d-b618-c94aecd04688 | -10.87727 | -45.30103 | 2026-09-03 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 63b8a8b2-c699-36b3-a35d-6564c1090d4d | -9.22168 | -45.76029 | 2026-09-03 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 630e2141-b9ea-30bb-898e-6920ddbeb50c | -6.81324 | -43.59557 | 2026-09-03 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 11cf4cf5-6398-3e3e-a0e3-c1b5c4258214 | -9.12658 | -40.64357 | 2026-09-03 04:02:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 816128f7-503a-34ab-8283-fbe43c4a8ed9 | -8.07494 | -50.98715 | 2026-09-03 04:02:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1d0f4e35-b2c0-35fe-b44c-76b6cfb87c91 | -10.99544 | -45.08656 | 2026-09-03 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 9d5c4996-4445-3296-84b7-6560cc6679e4 | -5.7318 | -43.27673 | 2026-09-03 04:02:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c03a5e42-4e31-3d36-8a93-567e45dce21d | -7.23712 | -42.75712 | 2026-09-03 04:02:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 9b5e3fe3-87c9-314f-b766-e5a8dc62b490 | -8.08521 | -50.96374 | 2026-09-03 04:02:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| b9c1454d-45b4-3fd1-96df-29bc4b351948 | -7.24 | -42.76155 | 2026-09-03 04:02:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| c8e8d438-f3bc-38ed-8f35-275126e11c97 | -3.18419 | -48.01905 | 2026-09-03 04:02:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8504dcd1-2064-391d-b8a6-aac5f073c940 | -10.78142 | -44.74576 | 2026-09-03 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d5497f69-1cbf-3697-bf68-62ae355041ef | -8.08949 | -50.97297 | 2026-09-03 04:02:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bfc938b4-a39a-3682-919f-3ae8b15bd935 | -10.56491 | -47.72417 | 2026-09-03 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 34d65ca1-a88e-3625-85c4-e8b0ea450f78 | -8.08298 | -50.97589 | 2026-09-03 04:02:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| e0d5785d-f739-3e30-84cf-c4e7415b1cf2 | -8.70489 | -52.36549 | 2026-09-03 04:02:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6fa8cf5f-d4e1-37d7-b1c5-95aa91dd475e | -6.56355 | -43.90343 | 2026-09-03 04:02:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| be5b70d8-e127-3c26-a871-b5f7c326898c | -8.40181 | -45.71061 | 2026-09-03 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d5bd421f-2214-3d84-a7d6-aeb834124e89 | -8.95725 | -44.42481 | 2026-09-03 04:02:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7cf0a311-0055-3bfe-a5a7-d7178d767266 | -9.78357 | -42.03827 | 2026-09-03 04:02:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 40ea6916-7b3d-37c5-b3e6-d93c74e2dcfd | -11.00371 | -45.08329 | 2026-09-03 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ba310a03-821e-3e17-a233-fb1a16654a8e | -10.56412 | -47.72854 | 2026-09-03 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1b9e0153-8141-3609-9c76-2b01073a2292 | -5.41489 | -44.80272 | 2026-09-03 04:02:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 707ece11-2f72-3aec-ae65-6272cf68fee2 | -8.46889 | -54.65434 | 2026-09-03 04:02:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 37b4b288-4876-378f-a00b-cf289c4eb1c6 | -10.56577 | -47.7306 | 2026-09-03 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d825be17-39ed-3e25-ada2-7df959830038 | -3.03277 | -48.41256 | 2026-09-03 04:02:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d62ba65-9eaa-3ea4-9257-2e07420005d7 | -9.27991 | -35.53429 | 2026-09-03 04:02:00 | NOAA-21 | PASSO DE CAMARAGIBE | ALAGOAS | Brasil | 2706505 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 57acf304-37ff-377e-b87b-d0aeadb34639 | -4.17598 | -42.43835 | 2026-09-03 04:02:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| d8dd71fc-e169-3a0b-9c9d-cdcb30e9cfa1 | -5.41089 | -44.80209 | 2026-09-03 04:02:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1dd242f1-d1bf-3ed3-9f9b-e9284636e04a | -7.61305 | -49.93524 | 2026-09-03 04:02:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a89f6105-c033-3663-ae47-3d7ae5082106 | -3.22245 | -48.81322 | 2026-09-03 04:02:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 564162e7-cc7e-3efa-bd7b-35e78c8a3a1d | -16.55487 | -46.69744 | 2026-09-03 04:04:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 33b86be5-47ea-3805-889c-fe1d6d1bbb66 | -12.09381 | -47.0715 | 2026-09-03 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1d033e70-872c-3d00-b523-d92e972f2d1b | -10.35497 | -49.96498 | 2026-09-03 04:04:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4d322c0d-44a2-3804-be74-607117854f00 | -11.28528 | -45.12132 | 2026-09-03 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f483a8e4-c946-30e1-8456-f88a1d08281c | -11.30545 | -45.13887 | 2026-09-03 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 501f00cd-14ef-30be-9c87-2e38c534e547 | -12.40187 | -44.80515 | 2026-09-03 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 3699fb70-3e0c-3e43-8dc2-0e27a5b9d557 | -12.19707 | -47.07874 | 2026-09-03 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b5342f61-2f2a-3989-9727-d29b7c5f7350 | -10.35094 | -49.95759 | 2026-09-03 04:04:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 85bc220b-8211-3dff-a42d-dd68dfa3ec6c | -11.30089 | -45.14302 | 2026-09-03 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 11a9059d-9671-3da1-885c-2fb104ad5e49 | -12.08963 | -47.0708 | 2026-09-03 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f647b29b-33d0-31c9-b90d-a9ab9ed8bb1a | -13.65156 | -43.35928 | 2026-09-03 04:04:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7db52aa0-9ba6-36ea-8a99-2c72be312d91 | -12.4084 | -44.81067 | 2026-09-03 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 42.7 |
| bdcda1e5-3821-3862-95cc-100dfb52eced | -9.62433 | -54.31254 | 2026-09-03 04:04:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b6dcf283-a0aa-3350-9a85-ce02966da1d7 | -11.17809 | -45.04351 | 2026-09-03 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 672f7788-70a9-3e4d-9890-a8e0c0221ec3 | -10.18116 | -50.26308 | 2026-09-03 04:04:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 60efd8d0-082b-37c9-97a4-8f5bed74cfe6 | -13.78797 | -43.64404 | 2026-09-03 04:04:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 23106dbf-edaa-3332-bd63-cdd692009a28 | -16.94114 | -49.37996 | 2026-09-03 04:04:00 | NOAA-21 | ARAGOIÂNIA | GOIÁS | Brasil | 5201801 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8027ac89-2757-37be-87b9-d314283f374e | -16.07881 | -46.07452 | 2026-09-03 04:04:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 488fbc16-add7-3f49-ae2c-40ba63d3733e | -14.95908 | -48.08873 | 2026-09-03 04:04:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 82abad91-80b2-3ebe-9f15-3a3e8c9302cf | -15.33513 | -47.03728 | 2026-09-03 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 884f1a6f-77b4-3f9b-9399-7e4422ad3490 | -14.60679 | -48.87397 | 2026-09-03 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 82cb119a-5591-35a9-a0af-8488df1bf159 | -11.28129 | -45.16762 | 2026-09-03 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 655078c5-437d-3031-8a48-5c29d88ca692 | -12.54421 | -44.71825 | 2026-09-03 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c24f4f4-64b7-30f7-874a-2e5521957e97 | -10.31509 | -49.94757 | 2026-09-03 04:04:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| abe4072c-3242-336b-bca8-96737f4c80d2 | -10.75415 | -48.97733 | 2026-09-03 04:04:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2edf8bf9-9fe4-3cff-a257-302d167acaa1 | -12.13354 | -44.20021 | 2026-09-03 04:04:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e4a1c60a-3e72-37c9-be3f-accd49366453 | -17.48844 | -47.84433 | 2026-09-03 04:04:00 | NOAA-21 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2c5949a5-a0ba-3f94-bc33-0c3ce920ff7e | -11.33463 | -50.54253 | 2026-09-03 04:04:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7c79dc25-1dc6-3750-9dd5-41fbe708e9cc | -17.48779 | -47.84791 | 2026-09-03 04:04:00 | NOAA-21 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 32fa9042-f404-3386-9d00-d738927af88b | -11.33864 | -50.55029 | 2026-09-03 04:04:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8eb8d19c-4416-3038-9615-4ca9e1bb7a6c | -10.75999 | -48.97287 | 2026-09-03 04:04:00 | NOAA-21 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 412baac5-daa2-328d-b0db-a21de64a8fb9 | -16.07752 | -46.07313 | 2026-09-03 04:04:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b985e180-8e4b-3ca7-947b-80505cc05145 | -14.05517 | -48.40314 | 2026-09-03 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8ecf3a3e-f07a-3d37-aaf1-e0c45fb0bfbc | -16.76527 | -49.62976 | 2026-09-03 04:04:00 | NOAA-21 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ae9c528d-c8e1-3931-bebb-9946e693470d | -11.23989 | -45.16101 | 2026-09-03 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ef66ac09-14be-36a9-99c6-f65b40e1c15b | -17.57869 | -44.96829 | 2026-09-03 04:04:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 45f7cf3d-6ec1-3f4e-b7ba-a2bcf4d438b4 | -15.02862 | -46.85313 | 2026-09-03 04:04:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 349f2553-9641-3e3e-85cb-7eb1cf7f5712 | -13.75376 | -43.82973 | 2026-09-03 04:04:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README20.md)
