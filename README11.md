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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0c220df2-674a-3383-bba0-95fb4efa5409 | -21.26216 | -49.47613 | 2026-05-26 04:34:00 | NOAA-20 | IRAPUÃ | SÃO PAULO | Brasil | 3521507 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| fbe0c207-6aaf-376d-a800-25f01463d186 | -19.75986 | -54.07568 | 2026-05-26 04:34:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2d05cb30-bc1a-3fe7-ba87-63ed92e27b03 | -21.32491 | -47.06812 | 2026-05-26 04:34:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 10aaa6da-8213-34a2-97be-351549a1012c | -21.28835 | -56.10447 | 2026-05-26 04:34:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2199728b-aac7-3988-9582-289ad2bba1df | -21.32432 | -47.0723 | 2026-05-26 04:34:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| acf2a669-d8da-37a6-b65a-acbe4404f44e | -19.76757 | -54.07743 | 2026-05-26 04:34:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 596d0d8a-5b34-3502-89ab-7eea20dcbcce | -21.28409 | -56.10356 | 2026-05-26 04:34:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7684209f-dcde-3f6c-a3d1-142b9a56135f | -19.7597 | -54.0782 | 2026-05-26 04:40:00 | GOES-19 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 59.0 |
| c5ff4bc6-9bb9-3eca-9e28-b05b27e71ea6 | -11.3584 | -52.9514 | 2026-05-26 04:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 118.5 |
| 5919c22b-51e6-39d3-80f2-7e5c2d8d05dc | -11.3584 | -52.9514 | 2026-05-26 04:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 6554a3da-3241-304e-bb10-bdb7b85fe03c | -11.3584 | -52.9514 | 2026-05-26 05:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 115.7 |
| 70d949da-6427-37ad-87a7-f20ece7093a9 | -11.3581 | -52.9722 | 2026-05-26 05:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| e3df1887-d8f5-3ddc-a1f3-4646e4d7d5f5 | -11.3584 | -52.9514 | 2026-05-26 05:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 101.3 |
| e915ca31-8d98-3422-b673-93647f4036a7 | -5.7949 | -45.12619 | 2026-05-26 05:16:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ee774274-0976-3f6b-9709-b8dbcf1b8edd | -5.79193 | -45.13326 | 2026-05-26 05:16:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d562e076-8a88-3de8-b475-4272e406de8d | -5.78783 | -45.12535 | 2026-05-26 05:16:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2a44155c-c7d6-3feb-908e-07e84020e60d | -5.79364 | -45.12024 | 2026-05-26 05:16:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 326412db-3cd8-332b-904a-1374eaea088e | -5.68368 | -50.10215 | 2026-05-26 05:16:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72a190a6-0d98-3f48-9184-8914e6f9eada | -5.79401 | -45.13263 | 2026-05-26 05:16:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c356c055-6c31-3141-ac79-73ebd425592f | -5.78875 | -45.11872 | 2026-05-26 05:16:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 7a0bd3fd-271b-3d42-b244-4d52168c2e35 | -5.79278 | -45.12681 | 2026-05-26 05:16:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| a8d0cd3d-ade3-3794-9004-cfe3e0cb321c | -5.7958 | -45.11967 | 2026-05-26 05:16:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 4f7aaaeb-b7c1-3652-afa4-fbd573be63e6 | -8.99038 | -46.82485 | 2026-05-26 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 77a80f58-019e-3c72-9856-a42d3e31fbbd | -6.52252 | -55.06703 | 2026-05-26 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dc29026d-236e-3617-83f4-63c3ac110d17 | -11.36511 | -52.95062 | 2026-05-26 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| c88a6b50-8ed1-3c08-84f6-fe367228ac40 | -11.27581 | -53.97274 | 2026-05-26 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 11c466fc-ee4e-38db-85b4-0425229f1ea0 | -11.18064 | -55.91395 | 2026-05-26 05:18:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 2ae92ebf-8071-3ae2-b175-3d2e1d638d81 | -11.17687 | -55.91335 | 2026-05-26 05:18:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 18.1 |
| ebf1ac9f-ae03-38a7-a04f-f05074648f5c | -8.52301 | -54.76888 | 2026-05-26 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9d0c2b68-f4f5-3a5d-86f2-8f3d7ca5723e | -10.63856 | -48.33292 | 2026-05-26 05:18:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e74702c7-a17e-3ee9-8015-86953066161a | -9.55616 | -64.62879 | 2026-05-26 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 63d8cb20-289a-3fcd-aec4-214bfcdfaaeb | -10.6324 | -48.32763 | 2026-05-26 05:18:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ce428c88-a9c7-3d30-a580-2bcef47169bc | -10.63805 | -48.33308 | 2026-05-26 05:18:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| aa0c148a-9291-36e9-be7b-9cbf428d5274 | -10.34281 | -59.06397 | 2026-05-26 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f95f3d71-623c-393a-9800-c1e10d12ce2b | -11.2182 | -53.82829 | 2026-05-26 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| bc831e78-6534-3fd1-9608-81795283bb32 | -11.27636 | -53.96872 | 2026-05-26 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c4114d68-ed80-3751-8626-c183d90838fe | -6.52693 | -55.06314 | 2026-05-26 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c96092f4-0821-38e0-97eb-f33d44e6836d | -11.35987 | -52.9548 | 2026-05-26 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 98e00cd0-fbe0-3e76-ac0a-258f9b408c78 | -6.52456 | -55.06487 | 2026-05-26 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 71da9f8e-5e23-3ff4-9bf6-ab0b87a862a5 | -11.3651 | -52.95189 | 2026-05-26 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 014897fc-b57d-3891-a4a2-3aa26a361fd6 | -11.35464 | -52.95894 | 2026-05-26 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d843626b-4fc6-33f0-ab28-007a97fc23d0 | -8.52353 | -54.77053 | 2026-05-26 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ec9a07bf-6402-319e-bcbe-6aa0ef4fda85 | -11.17622 | -55.91805 | 2026-05-26 05:18:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 672be10e-d61e-328e-a495-ea06a13dce20 | -8.98252 | -47.98895 | 2026-05-26 05:18:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3648021f-ef52-3126-b729-edda8bfc7445 | -9.02914 | -63.33779 | 2026-05-26 05:18:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 40ea167d-b8ba-3bce-9a28-8906b295b9a4 | -10.03598 | -59.35646 | 2026-05-26 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e8665255-2a4c-387a-be04-9e8d82a940b8 | -11.36448 | -52.95671 | 2026-05-26 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 91b020b6-4a9d-385e-9989-fd5ad3f21b32 | -9.449 | -50.84624 | 2026-05-26 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8a9a589a-8fd3-301f-939b-1f3458822aea | -12.0383 | -47.3373 | 2026-05-26 05:18:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8b0aab54-ae3f-3403-8f55-f7094582ed4a | -11.21877 | -53.82412 | 2026-05-26 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 01b424f9-9d4d-30a4-bc97-09e577c984f7 | -8.90766 | -51.86278 | 2026-05-26 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ccd88e6c-1652-3d75-8143-a5a319830213 | -5.20446 | -56.04524 | 2026-05-26 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5c2dfdbb-7d7f-3919-8592-16f25e2621ad | -11.35857 | -52.96437 | 2026-05-26 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| ef86709a-d053-3276-b2ea-201a214e90a4 | -11.36053 | -52.94995 | 2026-05-26 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 7cf7649e-0a9e-3607-9ded-6e68992b2b89 | -10.91948 | -54.11839 | 2026-05-26 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3979628e-a6b0-3796-9b3c-874917616358 | -10.92001 | -54.11448 | 2026-05-26 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3bc013bc-0d57-3ac4-803d-0b863c79bc54 | -8.97694 | -47.98317 | 2026-05-26 05:18:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fe83eefe-e934-3bcb-a00a-29a12614ad69 | -11.61689 | -47.9054 | 2026-05-26 05:18:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fe207e23-d995-34f0-9079-6f5978bd3284 | -10.03544 | -59.35995 | 2026-05-26 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9901294c-5f3f-3c23-9068-ee0f9db5fb01 | -11.35922 | -52.95959 | 2026-05-26 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 40.2 |
| c4e220c3-ba5a-3be6-a4d3-e1028338b65d | -6.5232 | -55.06258 | 2026-05-26 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c34c7e6f-397c-3ec9-ac1f-30d898b8a829 | -8.71187 | -54.9978 | 2026-05-26 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 60d5ad98-59bd-392d-ba4d-f28aea839412 | -11.35531 | -52.9554 | 2026-05-26 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 41.8 |
| c0dd8c52-c124-302d-a2d4-d7ae36b2e1eb | -9.83062 | -62.89111 | 2026-05-26 05:18:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29ceef9a-c3bf-35ca-b886-debb27bdab78 | -11.36051 | -52.95122 | 2026-05-26 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 41.8 |
| f074b511-4f88-361e-9f43-a3c5aeeed5e2 | -10.63186 | -48.33236 | 2026-05-26 05:18:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b4816b0b-6864-35be-9456-b6d90c9c08c5 | -6.52148 | -55.05983 | 2026-05-26 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb662a3c-6885-3a8b-9ebe-5215a5292841 | -10.63238 | -48.33221 | 2026-05-26 05:18:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bc56eef7-3680-3e4c-acf2-69493033e6bf | -11.3547 | -52.96021 | 2026-05-26 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 31.8 |
| f3bddcd2-504d-3b98-bbdb-8548b9de97e5 | -11.3638 | -52.96024 | 2026-05-26 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 17e41c3a-6afe-38b5-8ba1-2fa46264e102 | -11.36446 | -52.95545 | 2026-05-26 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 40.2 |
| aa8209d1-69e7-3ec5-8e47-79cb0514ce8c | -9.568 | -62.47951 | 2026-05-26 05:18:00 | NOAA-21 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b069d481-3166-384f-9d2a-5feb3f2a7597 | -8.97717 | -47.986 | 2026-05-26 05:18:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4bbd69c3-0bee-3900-aedc-b89a0263db22 | -11.46285 | -55.11948 | 2026-05-26 05:18:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3c3b24a1-70fd-3792-832d-ba18dd194479 | -6.52083 | -55.0643 | 2026-05-26 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f946b54f-2626-3956-892e-1df70717af91 | -10.92423 | -54.11504 | 2026-05-26 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f455b06-553a-31ef-9c77-83a82849a5ff | -6.51946 | -55.06202 | 2026-05-26 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30c08da7-f385-3b95-97f1-2d6d77987dd1 | -9.44942 | -50.8431 | 2026-05-26 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aa679680-2aa8-3374-a0d5-d3ae9f2e45aa | -10.87637 | -53.73764 | 2026-05-26 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d2220a12-9d7e-3f15-9c5a-f1b0de6fd0eb | -8.55867 | -45.98335 | 2026-05-26 05:18:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| ffce9bcd-e92a-3d22-b23c-04957425271c | -8.98333 | -47.98699 | 2026-05-26 05:18:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0944040a-6caf-33cb-9972-f03cc769eb93 | -8.9831 | -47.98418 | 2026-05-26 05:18:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7f27f645-cb1d-3621-980c-9c16663ce63c | -9.02989 | -63.33324 | 2026-05-26 05:18:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9702d84-4eec-3346-90b1-83f708dce2bb | -9.29604 | -48.58281 | 2026-05-26 05:18:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 489ea57d-10b9-3b80-8958-17ec31fe45e2 | -10.03045 | -59.34844 | 2026-05-26 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2cce9429-7451-38a4-b7f5-ee093e7bc80d | -10.34613 | -59.06451 | 2026-05-26 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f8cb371d-588e-31b2-888c-ddf393f4170c | -9.55675 | -64.62529 | 2026-05-26 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a7c71db-2008-31d0-951a-8263942b7fae | -11.35529 | -52.95414 | 2026-05-26 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3bec28aa-f294-305b-94d3-abb899dd19e2 | -8.89855 | -51.82267 | 2026-05-26 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a8756b32-34c1-35fe-80f1-1d08547e1bf6 | -11.17245 | -55.91743 | 2026-05-26 05:18:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 441dcafa-b4d8-3698-b49e-6a75cb33d049 | -6.52018 | -55.06876 | 2026-05-26 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8fa54a1b-88fa-3881-8e71-ae6932dd680c | -10.63295 | -48.32749 | 2026-05-26 05:18:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a74534bf-142b-314a-83ef-7df81d395b72 | -9.30201 | -48.58361 | 2026-05-26 05:18:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dc5746a6-2e6e-3c6f-89d2-05d12b47fd51 | -9.30801 | -48.58429 | 2026-05-26 05:18:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 495bebba-7cdc-3903-890f-999b0da734a3 | -10.9158 | -54.11389 | 2026-05-26 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 98ab4228-0649-3d17-8587-ca664035259b | -11.18441 | -55.91452 | 2026-05-26 05:18:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e60da22c-5745-3bc5-9d00-8392e41d1906 | -11.35989 | -52.95605 | 2026-05-26 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 41.8 |
| c5c9264e-8736-36bb-b8c9-ad2c2bd5bdba | -9.03053 | -63.33689 | 2026-05-26 05:18:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a48bedd9-71ea-358f-935a-7cbc667a0de0 | -10.85196 | -53.75563 | 2026-05-26 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7294f7af-1ac7-3d54-b6f0-1ba910573439 | -6.52392 | -55.06933 | 2026-05-26 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README12.md)
