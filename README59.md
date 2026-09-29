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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 41af2045-85aa-34cc-b492-ed0fa60e0b70 | -13.16156 | -48.56657 | 2026-09-29 05:12:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f8e49622-a042-3c62-9f28-bd90876a9d28 | -11.34732 | -54.11901 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b8e748eb-c0df-310f-ad27-ac9be693ce02 | -9.08537 | -49.88369 | 2026-09-29 05:12:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6080a10-fe30-312d-9f4e-8a8d522936cf | -12.59362 | -51.96683 | 2026-09-29 05:12:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e04210cf-f6e4-3d09-b82a-8381ef3bfa82 | -12.74585 | -47.28736 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a5bb011e-f845-3a2f-a3b6-64c4615fb5e0 | -12.00404 | -50.94413 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1a3c3b10-b430-330e-891a-e992d9293383 | -10.39703 | -61.25134 | 2026-09-29 05:12:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 8dcbce1c-feb5-3380-8f3d-ff66d3664162 | -10.81734 | -48.71888 | 2026-09-29 05:12:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c8e209b9-740f-37be-9a76-4cea016fd206 | -11.37506 | -54.05542 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e02e4a1d-8dfb-3e85-b4e4-c97996ca5733 | -11.36974 | -54.04185 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab18a260-af8f-31fb-ad7f-62fa8e96ad3f | -7.50274 | -55.03432 | 2026-09-29 05:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e1ec0874-da63-3fa6-8856-8fc99eb7d09e | -11.34435 | -54.11436 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aa32ebe2-e502-3cdd-a099-71516ac1ad59 | -11.55046 | -54.50131 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e30f2cea-7ba6-3b8d-bb31-e7145eef4b3a | -13.53837 | -49.18448 | 2026-09-29 05:12:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d318c08d-2fc0-347c-bcc3-f30d5018f518 | -11.33956 | -54.12203 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0c8ef3fa-9c4a-35f9-b702-155c4a51d686 | -12.0195 | -50.92878 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 35f3a8a2-1981-37cf-bf3f-c6d338274600 | -12.70247 | -46.97268 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4d835ca2-753a-367a-818f-e66f7d0237ed | -11.54754 | -54.4968 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 06ee4298-c4fe-3897-9709-51c79be4671e | -12.7512 | -50.6729 | 2026-09-29 05:12:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dae73ce5-982a-35e0-99c8-df2521af143a | -11.12883 | -48.33532 | 2026-09-29 05:12:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1701fbd3-6d02-3cf8-a0e4-253cab5f1685 | -12.91134 | -52.0369 | 2026-09-29 05:12:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d57e349b-e745-3cd1-b379-ce70ef5eab42 | -9.96046 | -59.25632 | 2026-09-29 05:12:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d1081506-79e3-3b52-949b-bad36f023ed7 | -12.67863 | -46.97618 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c68da443-58d0-3fe6-98bd-d18c3a321702 | -11.39647 | -47.45605 | 2026-09-29 05:12:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 39a542d9-11d8-36b8-979e-ffe06c310e7d | -9.79525 | -48.19841 | 2026-09-29 05:12:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e9eb2d9f-85d1-39d4-acf1-33e3606ea988 | -11.40389 | -43.44336 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 95309987-5c35-3c96-a436-96dfc5e78e4d | -11.36614 | -54.04131 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab57120f-c612-30e3-ae06-9c9e2997e473 | -11.4305 | -43.46 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 11508c3c-a77f-3512-a30b-583998d1f2f8 | -11.39487 | -54.04568 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 80065a9b-1c28-381d-aed2-b0ec100489ff | -12.67246 | -46.97895 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4e6ef397-8955-39c2-b150-a3d841718407 | -10.77145 | -68.27739 | 2026-09-29 05:12:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d04b740-a24f-3632-a3c6-4a7fefe2691e | -9.13012 | -49.97084 | 2026-09-29 05:12:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 45733f7a-f6c4-3e2d-854e-345b3cbc1f3a | -11.38548 | -47.45454 | 2026-09-29 05:12:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| baa6dc83-f8bd-30fb-99f7-91b497871353 | -11.44857 | -43.46885 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f4f80e30-c5be-344e-980e-6efbbaa7a153 | -13.16932 | -48.5466 | 2026-09-29 05:12:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7c3483df-473b-36cb-a042-5cb5fecf41d7 | -10.70926 | -47.82815 | 2026-09-29 05:12:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e8efe462-100e-3e6c-9996-d3fcdf40c77d | -11.98424 | -50.95882 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3caec9a8-aea5-3120-81b0-95b79b915e0c | -11.37865 | -54.056 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5d42570e-0f77-3182-829a-d43c1fb09a4b | -11.89939 | -50.61839 | 2026-09-29 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4d6beeb5-afeb-33fa-9203-7b81cda3eb49 | -12.69782 | -47.25672 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 41913b5b-cedd-3983-a476-28f8032c2776 | -9.28817 | -49.64161 | 2026-09-29 05:12:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e9514c83-384e-3a46-92cc-eee51cca04e5 | -9.95303 | -50.14325 | 2026-09-29 05:12:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b4b0e8f0-1979-3c0e-adb1-4ef821d719db | -12.02154 | -50.94658 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| df873813-3e99-32e0-86aa-62d392e8f6ec | -13.73816 | -43.6685 | 2026-09-29 05:12:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a059090a-adb1-3214-b116-19396e0979bb | -12.31365 | -46.41074 | 2026-09-29 05:12:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d0d23f73-6712-3b30-8d1e-8c105ec41580 | -11.90951 | -50.61064 | 2026-09-29 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ba2c17ba-abdc-318a-80ac-481765176d59 | -13.20416 | -48.56599 | 2026-09-29 05:12:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 858a46ff-6add-3436-995d-781b41d715e7 | -7.50441 | -55.02359 | 2026-09-29 05:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 25cebe3d-50fc-305e-acb4-ef61399c2e45 | -12.7868 | -54.02734 | 2026-09-29 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3c895ba-cc31-35cc-b7ed-03c57426147f | -10.39542 | -61.26061 | 2026-09-29 05:12:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 6dd8b9b6-2f17-3b9b-b4e0-79b3a4d71db4 | -13.8915 | -53.67913 | 2026-09-29 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 77d3b824-0c4c-33bc-ada3-12f0cd9bef41 | -12.73692 | -47.26646 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 3c168fa1-5f8f-3923-8bf4-f52d5d6850d2 | -14.10596 | -46.29388 | 2026-09-29 05:12:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 40996d8b-6d7f-334e-9005-b64146fc7815 | -13.47594 | -48.61368 | 2026-09-29 05:12:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6f13e0a5-170b-3e76-87c7-34209c979ffb | -12.01512 | -50.92817 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 94a58829-ccbc-3185-a4b3-350a491b2458 | -11.40228 | -43.43578 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8b26b057-20d0-322c-b481-270f3ff46a7c | -14.52716 | -48.29631 | 2026-09-29 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3c03bebd-25c8-3807-9b43-274fbdbcabe5 | -12.05396 | -50.93798 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e26a2c0d-aecf-3756-94bd-e1c347fe73ec | -12.75671 | -47.29243 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d9d4b209-08cb-30c3-b872-5fe80b2879dc | -11.96197 | -50.92508 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| deafbb8b-8f9b-3bd0-8a1d-728be571fae9 | -12.01659 | -50.95026 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9cf6d7d7-9d62-34b9-bc5c-9a57f516f6eb | -12.04402 | -50.94535 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| cf041c5a-9a31-3f30-ab99-e546e7fef0b8 | -11.42589 | -43.43857 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d84f3507-7f95-3d5d-89cd-066ad26f5e55 | -11.37996 | -47.45395 | 2026-09-29 05:12:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6e4fc081-c1c2-322e-bb11-91224963fae2 | -11.40075 | -43.44973 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5c353c42-35d2-37fe-bd65-68e31917c2eb | -13.43216 | -48.62429 | 2026-09-29 05:12:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e4ab76c8-acad-3468-a0ed-00145c586680 | -11.43213 | -43.44624 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| fa46ab58-b7cc-3f4d-96fb-3ce611750d6e | -12.73984 | -47.31548 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 268f7110-e2b1-313f-8ac0-f734c529a1c2 | -12.00585 | -50.99665 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 30243a38-dfb5-3596-b718-0425dcfea808 | -11.41802 | -43.44474 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 32e2c8db-7ae6-33aa-94cf-858fa6b7fe67 | -11.96141 | -50.92938 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6150985b-511d-3374-a946-38753a2757fe | -12.71689 | -46.99942 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0f8b8edf-9b71-399e-8789-b31c609f6326 | -12.01863 | -50.968 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a347361a-791f-32e6-b8cd-ff60385be50c | -9.14231 | -49.98174 | 2026-09-29 05:12:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b64665db-f044-324c-9312-b2a0527e93a9 | -7.5005 | -55.02665 | 2026-09-29 05:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b2367886-687d-358b-b134-6988c7bc714d | -11.99414 | -50.95148 | 2026-09-29 05:12:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f1fdb250-c2e3-3f30-a13c-2a3c4baaf993 | -9.28751 | -49.64639 | 2026-09-29 05:12:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| af27e0c6-bb73-3c96-910d-630ae71957b7 | -12.75949 | -47.2946 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 76023e64-dc4f-3370-9b15-5df7b922e7d9 | -12.59934 | -47.28849 | 2026-09-29 05:12:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1334fe96-2398-3ac1-88fe-b135acfcae68 | -9.07314 | -49.8727 | 2026-09-29 05:12:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 172d43b6-32a6-3d6b-bc92-0b8ba549c542 | -10.38468 | -61.25401 | 2026-09-29 05:12:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| f8ef512a-59ba-384a-b296-2127d355045e | -11.41964 | -43.43091 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5b86239d-d5e6-38d8-8c46-5f25e4c86e14 | -11.41717 | -43.43039 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8b77d5d8-af8a-3c79-a26e-12db9d800439 | -11.42427 | -43.45234 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| eae1e93e-4bee-36db-8e51-b55f8d72cead | -11.42345 | -43.45925 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 594182ea-129d-37d2-a7ce-487ae174e4bc | -11.36553 | -54.04545 | 2026-09-29 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c98827b-699a-367e-9445-8b020e749110 | -12.05735 | -46.50124 | 2026-09-29 05:12:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 643d562f-e056-3721-8f82-ad725f6f97d9 | -9.9633 | -59.26083 | 2026-09-29 05:12:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d0707f18-7f65-3113-b5c1-111051fc4722 | -12.76923 | -50.6754 | 2026-09-29 05:12:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b0582a39-8fbd-322b-a101-3fdcdc9f2ae1 | -12.90312 | -52.03555 | 2026-09-29 05:12:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bcf0895e-ac24-39a5-858d-e70706b61638 | -14.08535 | -46.31155 | 2026-09-29 05:12:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 555ce6fc-fd2c-3074-9a02-d723ebfe890a | -14.12495 | -46.29087 | 2026-09-29 05:12:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| e70626f0-51d0-3527-b494-adb6eb2314e5 | -11.40934 | -43.43654 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 39d2ed71-13c9-3858-b197-f61a9daddb8e | -11.86317 | -47.07901 | 2026-09-29 05:12:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d76f3d16-ff33-37ce-bcee-ff7f1e995943 | -12.7795 | -54.02624 | 2026-09-29 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4e45be3-15e4-3867-87f9-295902867e53 | -12.56039 | -47.16066 | 2026-09-29 05:12:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 98e073b2-c27d-39fb-9220-6b5cdd748235 | -11.4423 | -43.46124 | 2026-09-29 05:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bd268303-d568-350b-8b14-62d4ac6a4d73 | -10.77056 | -68.28191 | 2026-09-29 05:12:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e25c4957-0186-3536-990f-42e92d627290 | -12.05959 | -50.21476 | 2026-09-29 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0e7279e5-83ab-39d8-8651-5883f4c863a7 | -12.76983 | -50.6708 | 2026-09-29 05:12:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README60.md)
