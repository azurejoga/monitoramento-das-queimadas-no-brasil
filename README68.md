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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 92087237-7ca9-3bed-834c-d5209ef2b0b0 | -15.17079 | -50.0913 | 2025-09-29 04:59:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dfa3edcb-8113-33ca-a8a3-5273e3bad15f | -14.57822 | -48.27797 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2a6312fa-fa05-327a-a976-e261756070ca | -13.60709 | -48.05834 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a30aa821-2488-31c9-853d-8a402c85671a | -14.54477 | -48.43362 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e3d22049-bfa0-3ed7-b433-1f717d6eaba5 | -15.21612 | -50.09733 | 2025-09-29 04:59:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2b5f3c9d-3615-37b8-b6b2-30e629af5ad0 | -13.64064 | -48.0584 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cbb6f094-112f-3c2d-b461-ced7d9db7092 | -12.65731 | -51.66754 | 2025-09-29 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dd6411e2-5225-3008-a89c-efd299ea021e | -17.08558 | -48.57099 | 2025-09-29 04:59:00 | NOAA-21 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 877d153a-ef33-3945-be9e-cb5813dd6dbd | -12.42454 | -44.10764 | 2025-09-29 04:59:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 064a4b6e-54ba-37a7-9c82-96c1e7430365 | -12.76953 | -46.8569 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0d3e7194-875d-3f81-8fe2-5327fe0c8dc6 | -15.54797 | -47.88084 | 2025-09-29 04:59:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 03a7040d-9231-3520-b58e-b105c3f27875 | -13.58649 | -48.10411 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2de35678-5678-3325-a600-ff88bd272fcc | -15.27989 | -48.03498 | 2025-09-29 04:59:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 04d6da33-b283-3ae6-b123-8082ab170909 | -14.5346 | -48.43737 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 14.5 |
| f78d743e-ede9-3af8-8957-413d44a7fc11 | -15.27846 | -49.26342 | 2025-09-29 04:59:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e12e6527-005b-3408-8c8e-db3d42146c87 | -10.99631 | -57.0649 | 2025-09-29 04:59:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 57b49cd7-36ed-3825-ad8e-a3ca5f7a87cd | -12.94119 | -46.76934 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2621a43e-1ca1-3c6a-bcd5-d5e844d74245 | -15.19202 | -48.47907 | 2025-09-29 04:59:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f441fded-6f11-31ce-bca9-bdc134d53db9 | -11.43964 | -46.63539 | 2025-09-29 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 37559bd3-eb5c-3392-9236-46a17b71bd8a | -11.80412 | -51.81081 | 2025-09-29 04:59:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1b95d2f-65f8-33a0-b212-50fe7b6ba844 | -15.07768 | -48.33374 | 2025-09-29 04:59:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b86dad29-0869-36aa-a2a1-29e01f114ad4 | -12.17596 | -43.55783 | 2025-09-29 04:59:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f017d252-7d6c-385d-8b94-e9b292c3baec | -13.63758 | -47.3292 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 040a6f93-111c-3c3f-b299-9f5141bc6582 | -11.37586 | -55.14156 | 2025-09-29 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c34ad482-d4b2-3d4c-9e06-618a72a93d1c | -12.9452 | -45.16892 | 2025-09-29 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 64d365e3-399e-3e68-b515-900cf3a39a17 | -12.00349 | -46.61241 | 2025-09-29 04:59:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c12d6a19-f37a-36e1-a42d-f15deb3e404e | -12.93633 | -46.76556 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f1249405-a2d8-373d-8159-372e62eed823 | -12.75877 | -46.85859 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 313af022-a09b-3990-8c94-c524759c600a | -11.43658 | -55.03697 | 2025-09-29 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e7d068bf-44b6-38b1-bf66-ed1734dbe658 | -12.2225 | -54.29813 | 2025-09-29 04:59:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 170eadfa-8bcf-315e-8ea4-270f8d925c03 | -11.927 | -48.03386 | 2025-09-29 04:59:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| d67221b6-3f19-3d4c-8f6d-58ca973d53e0 | -13.83317 | -47.48155 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4aa42b13-de39-33d9-bcf0-b805a322c868 | -13.02686 | -49.4409 | 2025-09-29 04:59:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 417f964a-faee-3c0d-816c-a30cad4fcadc | -13.76535 | -47.91455 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| b1a3cab1-35fa-302b-abd3-28aa0640ae2c | -12.89232 | -47.08738 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 666a3053-5c68-3022-b85d-db9ef14b0dab | -17.09344 | -48.56631 | 2025-09-29 04:59:00 | NOAA-21 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| d7a3cfe0-80e0-32db-9a64-270accae46ff | -11.98532 | -46.58729 | 2025-09-29 04:59:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 82f3a92c-e1ec-3fa5-a1bf-b38fd799f95f | -15.26566 | -48.75937 | 2025-09-29 04:59:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0586befa-8e1d-37a7-af3b-1e2f15eccfea | -12.85246 | -47.61965 | 2025-09-29 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4a73e160-b211-3318-b75c-350569a2f618 | -15.22367 | -50.10696 | 2025-09-29 04:59:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 88d3cce5-c35c-3ba8-a5bb-1a045efb0dc1 | -11.807 | -48.24206 | 2025-09-29 04:59:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea5d20b5-90c5-3b23-b74a-38efb6bdb69b | -13.61045 | -48.06378 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a37cd919-3350-3f31-8572-8fcb18a4f43c | -11.14485 | -51.89635 | 2025-09-29 04:59:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ac12109-4d03-351e-98e7-a082a8982051 | -16.41525 | -47.02531 | 2025-09-29 04:59:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 07daaaca-1b64-3e99-b0a8-60a9c9a1c122 | -13.57708 | -47.28846 | 2025-09-29 04:59:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e38cf3c7-b493-339f-b3dc-a480044f3651 | -13.79736 | -47.89736 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2fedb8fc-0ba9-390f-96f6-cc5701e064a1 | -13.84451 | -47.94022 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8c6557b2-cfd9-3166-9e95-f24edf2630c4 | -11.37201 | -55.14454 | 2025-09-29 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3523dd25-7959-3bc4-b693-7bb0a8d0927f | -15.2562 | -48.75819 | 2025-09-29 04:59:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| c08fab5b-afc0-3962-a6b6-5e5d950ba188 | -15.70696 | -59.4824 | 2025-09-29 04:59:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2ac95e7f-4be4-31e7-b8d0-db5e26468371 | -12.85248 | -46.87995 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 93c207e9-11f2-3aaf-b8a4-0db81d929f9c | -13.18051 | -47.44088 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f7f6c77a-f643-33ef-a458-b3e4df99cb30 | -14.68009 | -48.15839 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 080c3b49-1b3c-3ae3-9689-eb418c43f75e | -13.57543 | -47.30166 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 113bf059-eb3d-3c57-a636-0e3b2f03f581 | -12.00309 | -46.61559 | 2025-09-29 04:59:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a88680a0-99f4-3700-8381-e3cc667083dc | -13.57514 | -47.30402 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 900d7bca-6aeb-309e-a3a7-92205019e7bc | -10.53647 | -54.38942 | 2025-09-29 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8602d39f-3eaf-3c1a-9d0c-07c2446a00ef | -15.5535 | -47.87472 | 2025-09-29 04:59:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 086a57d0-7842-36b3-b065-beb5197a2809 | -16.41025 | -47.021 | 2025-09-29 04:59:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 116ee347-0393-3ed8-b6b0-b0b89a0b5b5d | -15.25916 | -48.77346 | 2025-09-29 04:59:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 4c9d02cd-9928-3d85-92fc-2c961ad9d52c | -13.57957 | -47.29509 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 858fc2bd-15a4-3c81-9388-aaa83549da99 | -12.90001 | -47.1097 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e81d31f0-498b-33d0-963f-35a37c09b4ce | -11.41479 | -55.06528 | 2025-09-29 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3264d791-b1e3-3760-b341-a717c8dfa7f4 | -13.57481 | -47.30666 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 60b485ab-d9d5-34b9-ac60-d2d2bb4ef355 | -11.83548 | -51.79482 | 2025-09-29 04:59:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c840fc79-9124-398a-8db6-cf1c18b8e943 | -12.84683 | -46.88306 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3a80a999-8eab-3525-94b8-017208faafb6 | -13.79645 | -47.90475 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b67d7af4-7547-3400-a60e-de513ac713ba | -13.61197 | -48.05869 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6a4f59a8-f5c2-3d66-8137-c579d456bf42 | -12.75918 | -46.85525 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8ba1150a-bb92-3d1f-a998-39092da1d263 | -11.94318 | -46.53827 | 2025-09-29 04:59:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 825798c1-671d-38fc-bc0e-7aa4ed1ba1a0 | -13.58367 | -48.08773 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7f73cbe0-6baf-3d34-9b4a-cee9515dcc39 | -13.24556 | -48.45486 | 2025-09-29 04:59:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b1fa82b7-1047-362c-a9cf-9193ca3f4403 | -13.83696 | -47.93904 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a0504379-a7ed-3921-8957-9f057a2dc78d | -13.02072 | -49.45398 | 2025-09-29 04:59:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 01c7599a-aabb-38e8-a4f3-b2a739240f63 | -12.89672 | -47.09402 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c0919687-e78b-33be-85ff-67f28cbbe050 | -15.27874 | -47.87419 | 2025-09-29 04:59:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9bba07b6-9cd2-3a57-a2bc-cc52eb5e0b66 | -12.77047 | -46.84939 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d7ef325c-6d59-3328-a1ba-b1681cb88be1 | -10.72324 | -53.79216 | 2025-09-29 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f0fea4a3-99aa-3d80-b13e-05552ada601c | -13.81316 | -47.93046 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 842e2b6b-b1bb-3069-865a-0df59386e430 | -14.39306 | -54.93089 | 2025-09-29 04:59:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 01d3407f-08d2-3a95-8942-a8155b2d3868 | -10.9975 | -57.05748 | 2025-09-29 04:59:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d4bbf057-3671-3fa7-8a4f-c92e4bd8fc11 | -15.28499 | -49.51492 | 2025-09-29 04:59:00 | NOAA-21 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 7ae72ff1-6f70-3f33-8860-02d0013e2cdc | -12.99911 | -49.44056 | 2025-09-29 04:59:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 609dc3fb-1fc5-350b-8559-d992cd3ca386 | -14.62107 | -48.28907 | 2025-09-29 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 52416c01-abfe-3923-b0ab-0b0261b04b4b | -12.86812 | -46.9656 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| d6dbcd8f-8797-3c73-b555-9d77aa8acb36 | -13.22944 | -50.95409 | 2025-09-29 04:59:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 80cbb6a7-dad5-342d-819b-894b851ad374 | -13.63139 | -47.33753 | 2025-09-29 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 23c6b7d9-fc2c-3489-8281-1ca69c632e92 | -13.00555 | -49.43364 | 2025-09-29 04:59:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| dfdd1976-b380-3f6b-8856-059055a16700 | -13.01248 | -49.44904 | 2025-09-29 04:59:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3d12ace4-ff6c-37fd-ba42-4749f0032d08 | -17.50678 | -43.48143 | 2025-09-29 04:59:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ee096977-1da2-38d0-b739-6c78689d6cdc | -12.86049 | -46.90043 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a1cddd43-c59c-357c-9088-d09233e472c2 | -15.88003 | -46.22458 | 2025-09-29 04:59:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a9b49507-00f3-353f-aa20-d0d65258225f | -12.96855 | -46.24397 | 2025-09-29 04:59:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0d528757-917d-3710-8403-b52055ae3ed9 | -12.80209 | -47.74397 | 2025-09-29 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3440bbe3-34e9-37e2-be0e-c97cb84c3aca | -16.50855 | -46.02984 | 2025-09-29 04:59:00 | NOAA-21 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6a49f0c3-d7c0-3c72-b1ac-b760e9d866c5 | -12.69966 | -46.91151 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e9861ab0-b710-3817-a332-f912c483007a | -11.9976 | -47.10866 | 2025-09-29 04:59:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 538dbe8b-95a6-3e80-bdca-fcf2f765733b | -15.21506 | -50.10569 | 2025-09-29 04:59:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 12d3fc3c-14df-3602-9226-1654e9608ed5 | -12.66643 | -46.9262 | 2025-09-29 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 45609c12-8a1c-39f5-93dc-7279a1de27b3 | -14.46924 | -42.16824 | 2025-09-29 04:59:00 | NOAA-21 | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |


[Clique aqui para ver as próximas entradas](README69.md)
