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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 77ae33e8-458e-343c-bead-5d2bf80acf9f | -10.44656 | -50.26426 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 232678b5-2e3d-3827-9307-af4d8806e5bc | -11.45763 | -50.24564 | 2026-09-21 04:21:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ee5dece2-8f3d-3534-9338-82bd8344b4ed | -14.17821 | -47.87367 | 2026-09-21 04:21:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9ffc52e0-202b-3982-8c1f-58cd768779b9 | -10.81719 | -50.78006 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fcf472d3-d992-322d-8cb4-e3963dcd8c7c | -13.26789 | -51.80616 | 2026-09-21 04:21:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2380b1c4-a04e-3816-ae81-79779e7cc0d0 | -10.45583 | -50.28711 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4bbfb158-e8cf-3548-a485-8c8c9a7c7ad6 | -9.75207 | -46.23833 | 2026-09-21 04:21:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 505c6acb-651e-3dc0-a2ae-eb31e16bc78b | -15.85765 | -49.90365 | 2026-09-21 04:21:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fbf446f9-8210-3154-9a8a-4b2b95ceff4e | -11.16472 | -54.12328 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa526bd7-87d5-3a8b-a9e9-c15221dbee35 | -15.85532 | -49.90519 | 2026-09-21 04:21:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 65a3ab91-7a91-3791-9d89-75d9c56806d8 | -9.9539 | -45.7186 | 2026-09-21 04:21:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f1cbd608-76bb-30c2-be82-4b164666fc23 | -10.09168 | -50.25458 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 7a9fc42f-2563-3771-b02c-9a25184c4678 | -10.36904 | -50.45126 | 2026-09-21 04:21:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01a81294-f3a1-3e3d-a4aa-7eb4266f125b | -11.02375 | -54.14691 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 94f9af12-652a-342c-8b09-bfe0f31a7f18 | -16.03833 | -52.53153 | 2026-09-21 04:21:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 414c7d3d-d655-311b-9ad5-3f9625154c87 | -10.79982 | -50.74982 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 56119680-b343-3ba0-913e-18eb115060ee | -9.82619 | -48.42818 | 2026-09-21 04:21:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 67a33c2c-ddaa-32c5-9a51-0de0199108cf | -11.01141 | -54.15199 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aa502135-5c27-3c8f-9fc6-0e2902074ee4 | -10.75298 | -50.80864 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ad88f8cb-9f50-3446-a00b-a8be550a4fde | -9.83012 | -48.31473 | 2026-09-21 04:21:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 48c3af06-2927-32f1-bf78-593a0073c0e3 | -10.98155 | -50.59512 | 2026-09-21 04:21:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d2f0d7bb-cc4d-3d5a-8866-2282e210e0b9 | -14.04526 | -52.07333 | 2026-09-21 04:21:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5d6ad0e9-41b7-3b58-9b35-c5ca606f33e0 | -10.87885 | -54.07286 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a99983e4-d2bb-36dc-bfc5-b5ddd349206c | -9.65823 | -54.33163 | 2026-09-21 04:21:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aee49fbf-047f-33f4-bdd8-ab07b2b333ba | -10.92325 | -53.95931 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b37f5cc4-c287-3dea-abf9-2b8493c6c444 | -11.67254 | -43.41871 | 2026-09-21 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 96121e72-989d-3a52-a959-a2eaec8a9929 | -10.76258 | -50.80593 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1e35726f-c5f7-3650-91ac-26875121b8df | -10.47484 | -50.29406 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 5c07f74b-5aab-3ef8-b38f-d57fc046a5d9 | -11.47036 | -47.77187 | 2026-09-21 04:21:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| e14f0d3a-58fa-39b5-b4f2-b5ba06e5d172 | -11.12471 | -54.00747 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a69eab2-b214-3304-a933-72ab99209751 | -11.86185 | -48.97338 | 2026-09-21 04:21:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 361f552f-921f-34ef-876f-219b4b267854 | -13.86796 | -48.58447 | 2026-09-21 04:21:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a9bd6f4a-ee71-3499-a7f7-d05910e68006 | -15.45535 | -48.47408 | 2026-09-21 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f8d8694e-9e3d-31c2-88c8-58dbbb99ecc8 | -11.4776 | -47.77322 | 2026-09-21 04:21:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 85059fa7-29e7-38c8-a943-bc3bb4b3398c | -11.33882 | -43.38106 | 2026-09-21 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f3c9bcaf-b5c0-30ab-86b7-dc1610c13567 | -16.182 | -51.12721 | 2026-09-21 04:21:00 | NOAA-20 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e903c5a-1980-3536-8b84-56b5ba0631de | -8.18694 | -54.73868 | 2026-09-21 04:21:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f9f873d-65f0-356d-bcd0-a63cfc3b207d | -13.5849 | -43.71137 | 2026-09-21 04:21:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2b23481f-ee23-381b-b857-9a4c64199d0b | -15.45251 | -48.4691 | 2026-09-21 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ca8d0194-a133-343e-ae47-2c703fdd91b5 | -14.91949 | -49.90011 | 2026-09-21 04:21:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c74e67e6-30da-3ea7-a61c-c0bee11ee7cf | -9.76151 | -46.05712 | 2026-09-21 04:21:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b5e53fc1-2443-311e-9c48-c88ac047c9f4 | -11.40713 | -47.33757 | 2026-09-21 04:21:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f81b4ba6-6c28-382e-8362-0753b9b14715 | -11.75973 | -47.43715 | 2026-09-21 04:21:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 334ba24c-dbd7-3c39-a812-c0bc09c09e26 | -10.47278 | -50.281 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 32.1 |
| f05cb200-5484-3516-9d0d-961a06f4c46f | -11.80056 | -49.80705 | 2026-09-21 04:21:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 8f90efa5-c730-321b-9619-ce1756589b98 | -10.91989 | -53.9475 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 91d46e87-1b8f-3020-ad11-67157ce4cc97 | -10.86755 | -50.92902 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 727a5549-8608-3ccf-8000-44e620c2b268 | -15.47389 | -48.4081 | 2026-09-21 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d69dce04-d13b-32cd-95fb-155a459f41ff | -11.02711 | -48.31601 | 2026-09-21 04:21:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 810e4f38-d915-3079-9a38-e019e0463558 | -13.07167 | -50.62932 | 2026-09-21 04:21:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1326f5cf-e367-3ebe-a5ce-4a09bb5a5420 | -9.84282 | -46.45428 | 2026-09-21 04:21:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d121e2b2-f3da-360f-a783-33b476b4b55d | -16.03464 | -52.5328 | 2026-09-21 04:21:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a2d563fe-0cbd-3ab7-9004-abea960e0dd8 | -14.98425 | -43.08905 | 2026-09-21 04:21:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 87a0178f-5805-3fc7-82a5-7a0bce0ef0fd | -10.80385 | -50.77628 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f5f3eb3e-d0b5-3b9e-8382-11ae58187206 | -16.03827 | -52.51418 | 2026-09-21 04:21:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 164.8 |
| 436f4009-e650-3fd8-a03e-ec851fef7ac3 | -10.68049 | -48.72596 | 2026-09-21 04:21:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2db0f51f-f2f9-344f-b8b7-7558ccbf15ab | -10.37171 | -50.22341 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 92275d97-40fb-3a8b-8d05-d8d0c607d7dd | -10.42024 | -50.23835 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 934e6318-5594-3dd2-8d27-4efa69c86970 | -12.28176 | -50.15937 | 2026-09-21 04:21:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 72399d62-52a4-3912-a7a4-bb3beff3808d | -10.9192 | -53.95112 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fd5ae0e7-c224-32fb-bef7-e0b66b36af3a | -10.30933 | -50.55727 | 2026-09-21 04:21:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 272b3654-7f46-3da2-ae1d-961644a83c77 | -16.03736 | -52.51884 | 2026-09-21 04:21:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 164.8 |
| 15f8fb97-b38a-3f35-8cb3-03d0d582e311 | -7.57103 | -57.688 | 2026-09-21 04:21:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| bd95cd8b-693a-348a-b510-6bce82fdb804 | -11.09487 | -48.30408 | 2026-09-21 04:21:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0d95b967-c02e-34d1-a16c-870855d3df36 | -11.09895 | -51.06866 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2d7d5941-b4fd-3da1-96f0-2f5838c5562d | -11.34128 | -51.36546 | 2026-09-21 04:21:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6355849e-9a4f-3cbe-98c4-4443f891d9e7 | -15.44395 | -48.45451 | 2026-09-21 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9d8ebcc5-881d-3243-8886-94e1feeb91c8 | -11.02988 | -54.14453 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b79a7e99-83fd-3a35-93ac-8003098a53df | -10.83444 | -50.1562 | 2026-09-21 04:21:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 895d5998-77c7-3ebd-b38e-d1efba7cb02f | -9.78543 | -46.07997 | 2026-09-21 04:21:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 813814f5-2d79-3e96-ad92-2338f126e96f | -11.10636 | -54.01509 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 42f8341c-5316-3b30-a128-772267bd83d1 | -10.58682 | -57.48624 | 2026-09-21 04:21:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 99aa9650-bab7-37fc-a868-c56a9e49e03c | -10.6949 | -50.75577 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f21218f2-663f-3d14-8ab3-3a89eb1c4bf2 | -10.53786 | -57.44128 | 2026-09-21 04:21:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 419cbebb-dd44-3e8c-a91a-46396c89c66b | -10.67161 | -50.73339 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 08aa0d65-4024-3592-9654-cc1f67157db1 | -11.79056 | -46.83992 | 2026-09-21 04:21:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e4bcbf94-a9c5-3692-ab3f-7eab6d9bd6e0 | -12.90537 | -50.97137 | 2026-09-21 04:21:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| afb59bcd-2ff6-37dd-bda3-7a34a29e8e66 | -11.12402 | -54.01102 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ddddeff-d901-327a-b8cf-57678602ef15 | -13.17941 | -43.56961 | 2026-09-21 04:21:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c9e2be97-5773-3f30-a47d-01ffeb686258 | -10.80645 | -50.84142 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7e9aa178-f276-3242-87c1-14016bf33703 | -10.86906 | -57.16287 | 2026-09-21 04:21:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| aefa77e8-774a-3071-a5ee-d2aeb0a24f68 | -12.80598 | -54.05076 | 2026-09-21 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 37b086e2-e0f0-3878-a4cf-02822aa72527 | -12.79943 | -54.0564 | 2026-09-21 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b76171f-ba64-33e8-acc7-5dc74e5f137c | -13.27112 | -51.76397 | 2026-09-21 04:21:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7f44b48c-29c6-3a15-a035-e33a90fe4a4e | -11.02687 | -48.33719 | 2026-09-21 04:21:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bb77a08f-1bcc-3a9c-a8a9-66f38feb1ecd | -10.88016 | -53.97224 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a22f6e02-791e-321c-abbe-d65122e1993a | -16.03375 | -52.50618 | 2026-09-21 04:21:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 212.1 |
| c6fa982b-ed38-3ef3-b138-da76b9c117c3 | -10.75974 | -50.79635 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1275aedc-15f5-3fc4-93de-a49f05d5e418 | -11.65229 | -47.78097 | 2026-09-21 04:21:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7be224c3-ebdb-3c94-91b5-7904c996ebf9 | -11.84959 | -48.86116 | 2026-09-21 04:21:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f341e2d9-9503-3550-8e7e-773621584eee | -11.84348 | -46.89647 | 2026-09-21 04:21:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dcad2457-6b98-3deb-9b51-c2777df784c8 | -10.47706 | -50.28179 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 019aca88-0773-3198-800c-6ceb24888a47 | -10.9036 | -53.97375 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d1f04890-e934-354b-a6fc-badfa99ebed1 | -13.93265 | -47.84658 | 2026-09-21 04:21:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ff38cfd4-1139-38ee-8bd2-3d7245028526 | -11.84875 | -48.86598 | 2026-09-21 04:21:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7606cc40-750d-3e9d-921c-c7bb7a14feec | -10.39108 | -50.22878 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 4fcd4dbf-0a74-306e-9ed4-82801bb49c89 | -16.0445 | -52.53022 | 2026-09-21 04:21:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e9491bc0-1037-3d01-95e2-fa694b5ddbb3 | -14.07631 | -52.13255 | 2026-09-21 04:21:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a164ac90-22c4-3475-9f8d-39c596dabedb | -10.46469 | -51.33615 | 2026-09-21 04:21:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0d2cb877-842a-390b-81b4-45197b30a7e9 | -14.22597 | -44.63212 | 2026-09-21 04:21:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README45.md)
