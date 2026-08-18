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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9db8f5e7-3ee4-3c23-9cfa-c21cf2bfd9a8 | -6.8411 | -58.9939 | 2026-08-18 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 33.9 |
| b35a2713-65cb-38c4-bcf7-e6e8fdc9d99c | -6.7477 | -59.1909 | 2026-08-18 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 7ad28100-a65b-3a4b-bc25-21e008aaab4b | -8.604 | -50.3527 | 2026-08-18 03:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 1571d32e-e160-354a-b77f-0918c0c421a0 | -8.5853 | -50.3543 | 2026-08-18 03:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 96b18c92-2755-330f-af08-7419e0b4549e | -6.8594 | -59.0125 | 2026-08-18 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 54daba30-e19d-3aca-afbc-45d5fe6fe82a | -8.5855 | -50.3331 | 2026-08-18 03:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 0101cc5a-475f-34a7-9e1d-0a02c17a3d2b | -9.4256 | -60.4353 | 2026-08-18 03:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 543922f6-dbef-314a-abba-0c85875beb11 | -6.841 | -59.0132 | 2026-08-18 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| c2ae54f2-8eac-351a-96b5-359a418578f7 | -14.8233 | -46.619 | 2026-08-18 03:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 8f68bfc2-3b5c-3b47-8922-0de3f23958fa | -8.5853 | -50.3543 | 2026-08-18 03:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| b629098d-005c-3175-8047-ba5b9ce0f42f | -6.8594 | -59.0125 | 2026-08-18 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 4f4c878f-16c7-34ce-8846-92aa70858c09 | -6.748 | -59.1523 | 2026-08-18 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 2a654f06-1e40-3d7f-ae66-2be4a617c7b3 | -14.8228 | -46.6419 | 2026-08-18 03:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 54ded26b-29ca-39bb-8b80-41eb050bd75c | -14.8033 | -46.6453 | 2026-08-18 03:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 104.2 |
| c276a29f-13ab-386d-b59d-79c0feed1191 | -6.7477 | -59.1909 | 2026-08-18 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 34.2 |
| 723ea36b-8cdb-3147-90c4-d73a6aca5e5c | -8.6042 | -50.3315 | 2026-08-18 03:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 3efe9cc0-1dcc-3893-b42e-62a64cd4c282 | -6.7478 | -59.1716 | 2026-08-18 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 422e4e60-bc7f-31dc-9ccb-946764045fc2 | -6.8411 | -58.9939 | 2026-08-18 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 081c11c2-cd44-38c3-8edc-7cb75f3a4db1 | -11.5282 | -46.6292 | 2026-08-18 03:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 91.2 |
| f293fb0d-cb7d-31cd-afbb-c5803aa8267b | -6.841 | -59.0132 | 2026-08-18 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 888d349d-f922-3c0b-96b6-63be6e6c66e5 | -8.604 | -50.3527 | 2026-08-18 03:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 3adf4d80-9c14-3a59-a13e-bc4ff13998f9 | -11.5279 | -46.6518 | 2026-08-18 04:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 075d3cea-729e-35a0-92f6-4ec61407b7c1 | -14.1821 | -52.93 | 2026-08-18 04:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 191.2 |
| 74cf4658-e6ee-37fb-b262-11113d7ac513 | -14.1628 | -52.9323 | 2026-08-18 04:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 64.8 |
| b46e46a8-2dd3-3e0f-a0c8-67fda4e9a7bd | -6.841 | -59.0132 | 2026-08-18 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 03e8885b-73f4-3e16-b864-e5d97955e902 | -14.1631 | -52.9113 | 2026-08-18 04:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 9e65e505-7896-34b3-82b1-fe4b3dc6a182 | -14.8033 | -46.6453 | 2026-08-18 04:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 9f043bf2-c021-3443-b885-dae7dc38c2b0 | -11.5282 | -46.6292 | 2026-08-18 04:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 153.5 |
| a4a95db7-5eb1-31bc-b71a-cb5b3bff5382 | -14.1824 | -52.9089 | 2026-08-18 04:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 0cdab56f-f0a1-3461-a3cd-cce6bf6f6e75 | -14.8228 | -46.6419 | 2026-08-18 04:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 147.1 |
| 516f3041-2a61-3954-9c6e-7e325d7bdd46 | -6.7478 | -59.1716 | 2026-08-18 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 217fe656-45ad-37f4-8586-694c907056d3 | -8.604 | -50.3527 | 2026-08-18 04:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 2c31c3b0-a058-3863-9672-1cd414815d1f | -8.5855 | -50.3331 | 2026-08-18 04:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 06261c8f-cfc9-3f30-adb5-5afa6e9fecac | -8.5853 | -50.3543 | 2026-08-18 04:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 0bbf50b0-d2a1-3db7-af6d-9fec4ddebbb9 | -6.7663 | -59.1708 | 2026-08-18 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 26dd34b2-5433-3481-8e43-c24abde7f7a4 | -8.6042 | -50.3315 | 2026-08-18 04:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| b3bdb33f-f309-3ef8-b13c-b6707eb403d3 | -6.8594 | -59.0125 | 2026-08-18 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.6 |
| f4f08c2f-3806-3978-87cc-4f8acd7a66c9 | -6.748 | -59.1523 | 2026-08-18 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 64f99118-0625-3b16-b464-995960d3b934 | -6.8411 | -58.9939 | 2026-08-18 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 7e43fdec-2426-3b6d-94c2-c08898bd2eef | -14.8233 | -46.619 | 2026-08-18 04:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 4f4beaaa-1586-32ae-b186-4cdea0d1e800 | -3.24009 | -43.22517 | 2026-08-18 04:00:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 968d08f2-9241-304b-a4ed-817996afbd61 | -2.57844 | -49.4443 | 2026-08-18 04:00:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f5e33c24-750a-3ebb-bc52-3ac88bb85d10 | -2.49683 | -48.13468 | 2026-08-18 04:00:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7d82d832-04be-3fb0-b737-b2a50b5da4cf | -4.15511 | -38.41589 | 2026-08-18 04:00:00 | NOAA-21 | PACAJUS | CEARÁ | Brasil | 2309607 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 478f3caf-86f0-3b09-9f54-b61b20abe340 | -2.89064 | -40.52269 | 2026-08-18 04:00:00 | NOAA-21 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 248a5114-c9da-3f52-a95d-8c780105d29a | -3.37098 | -39.49996 | 2026-08-18 04:00:00 | NOAA-21 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 760ccea4-8523-37f0-ba11-67398cd047e0 | -3.25752 | -42.83815 | 2026-08-18 04:00:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3abe7fbe-5333-333c-b9fd-e6276f415746 | -2.49631 | -48.13792 | 2026-08-18 04:00:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7560b465-5cd5-3fd9-a425-ebb5821f0972 | -2.49559 | -48.13827 | 2026-08-18 04:00:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 447d7b3d-3fd3-3dcf-a9e8-45ad4e9f7340 | -4.15177 | -38.41538 | 2026-08-18 04:00:00 | NOAA-21 | PACAJUS | CEARÁ | Brasil | 2309607 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 53d9dff5-d6c8-3388-b034-bbbea69cca52 | -2.50089 | -48.13902 | 2026-08-18 04:00:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 40d9e5a4-49af-334e-a8c9-755e1a26594a | -2.50144 | -48.13579 | 2026-08-18 04:00:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8ccafd34-8bc5-3c1f-b7ba-362397a5bd42 | -7.16937 | -43.14227 | 2026-08-18 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| c5e0c914-56a8-361e-8c2d-27901a4edcfa | -4.63795 | -40.40017 | 2026-08-18 04:02:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 76f4cbdb-6644-36da-8a9a-0bc48706ee5d | -9.07224 | -50.85709 | 2026-08-18 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d5febc7-8aa6-3e06-baef-baddf95472d4 | -8.36765 | -46.36028 | 2026-08-18 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 12f8ef4f-2e96-314f-ae89-c9b5add2ef27 | -8.36061 | -46.37572 | 2026-08-18 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cc0795ed-6fda-3c09-adee-50ac21ceb708 | -9.40734 | -48.25078 | 2026-08-18 04:02:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a0f89c1a-713d-3cde-9b6a-04def976478d | -5.2686 | -49.05003 | 2026-08-18 04:02:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 472f9fa0-5a11-32f9-bfd6-c04d682ac831 | -9.19969 | -49.96569 | 2026-08-18 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cfd7822b-9d7b-3fbb-9288-14e1ada9ece7 | -9.12541 | -46.04181 | 2026-08-18 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 58287502-b9b4-3d97-a1ca-602e59523a6c | -5.66587 | -43.57191 | 2026-08-18 04:02:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 90f787e2-8dbf-3d94-a434-b736056373a5 | -8.48961 | -44.73194 | 2026-08-18 04:02:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0c63ba42-151d-34dd-a455-53d09c7185c0 | -7.80949 | -44.09376 | 2026-08-18 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9fe6227c-b12e-315e-b2de-ba51a68e32cc | -3.26413 | -49.52447 | 2026-08-18 04:02:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c5e5564-e1ab-3aad-b480-58a6a268b6ac | -6.17451 | -47.81138 | 2026-08-18 04:02:00 | NOAA-21 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1c100113-3b34-3170-a0a6-e3b846e209c8 | -9.19656 | -49.96436 | 2026-08-18 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 066cfbd8-b2e7-3f25-a357-04acbe007b0c | -4.84799 | -42.05967 | 2026-08-18 04:02:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 1865ba35-4bf0-38fc-8a63-1f1165b74c68 | -7.13471 | -47.52011 | 2026-08-18 04:02:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2bf1a834-6337-3dfe-8c58-d3bfc153127a | -8.64894 | -43.89465 | 2026-08-18 04:02:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 593186cb-e136-3c9f-9dd6-41a466826235 | -5.57169 | -47.45176 | 2026-08-18 04:02:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 62640ee2-7cac-3117-ac12-2b4aa329b4a5 | -6.17227 | -47.33384 | 2026-08-18 04:02:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| f30810ba-06de-3727-b3fd-715a72bd08a7 | -7.1719 | -43.42265 | 2026-08-18 04:02:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 895b6cd2-6aee-329e-9042-2950457bcab8 | -7.15735 | -43.14864 | 2026-08-18 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6e0dac60-ea9c-3838-a5db-a9a0c71f3b75 | -3.50502 | -48.03898 | 2026-08-18 04:02:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1b63f901-3c03-34f0-97d7-5a99b8e88c86 | -6.53397 | -43.12471 | 2026-08-18 04:02:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 0cab69a7-9247-36bd-bef9-8070133831ec | -10.27534 | -50.41724 | 2026-08-18 04:02:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fbba6e8f-2244-338c-8948-00810532843e | -8.33043 | -46.47403 | 2026-08-18 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5c0c9ea4-3286-3d1b-82b6-d191150fa19f | -5.55757 | -43.42986 | 2026-08-18 04:02:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 652ff52d-b1f0-38bd-b02e-322180595eb0 | -8.59778 | -50.35122 | 2026-08-18 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| a151d980-d4ec-30b9-9a2f-14e8efb634bf | -3.51074 | -48.03654 | 2026-08-18 04:02:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 031b2738-ad6d-3986-87c8-6524fd6dbf48 | -5.7953 | -43.91891 | 2026-08-18 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e6af3bdb-9477-3a7e-9b25-182a4c16d921 | -8.48875 | -48.81763 | 2026-08-18 04:02:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bdc5d92c-25a3-3562-9211-25ffba587b56 | -5.57907 | -43.79093 | 2026-08-18 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| eb70b982-d71c-3d54-a016-a8d98f2e283a | -6.17844 | -47.81763 | 2026-08-18 04:02:00 | NOAA-21 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| cc6f68d7-1f93-3f94-854c-dbd86298e131 | -6.99597 | -46.2272 | 2026-08-18 04:02:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5f612383-54d9-30b2-8653-0a697b1fd48f | -7.28401 | -44.07555 | 2026-08-18 04:02:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 78c402fc-4f30-3898-8ef9-d7e458f791e8 | -4.97108 | -42.21704 | 2026-08-18 04:02:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 08a58b01-b8d7-3aee-96b7-f0aab79f75b3 | -8.74413 | -45.31081 | 2026-08-18 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ba2d55af-0f49-37df-946d-51a3090d94f8 | -8.59296 | -50.34863 | 2026-08-18 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| ce90c359-482a-3256-acbf-a7a05355e4f4 | -7.17268 | -43.1219 | 2026-08-18 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 4e895278-bf79-3e27-840c-8c5947d81cf0 | -6.72541 | -48.65186 | 2026-08-18 04:02:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b6372b7b-77f1-3d69-babb-f8ac560e0194 | -6.30445 | -47.89015 | 2026-08-18 04:02:00 | NOAA-21 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a94f4b1a-c227-3f54-a379-3788cae6ec50 | -7.20586 | -41.54161 | 2026-08-18 04:02:00 | NOAA-21 | AROEIRAS DO ITAIM | PIAUÍ | Brasil | 2200954 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6e092132-1e7e-3be9-9556-f81cc36a86c4 | -4.49473 | -42.56437 | 2026-08-18 04:02:00 | NOAA-21 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a00bf16a-012e-372c-996d-054573b53904 | -9.79688 | -47.30315 | 2026-08-18 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2cbfd7d2-03dd-3ba1-b85d-c7df4ebc2631 | -7.45996 | -46.15461 | 2026-08-18 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| bf205765-438a-3913-91e4-4e3ec0632343 | -9.7752 | -47.30002 | 2026-08-18 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 71901f9a-41c4-39d8-9434-b88a6e1f479e | -5.2692 | -49.04663 | 2026-08-18 04:02:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 623415db-2a03-3228-9f70-9e20d9f2ae57 | -10.2816 | -50.44369 | 2026-08-18 04:02:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README9.md)
