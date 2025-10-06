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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 34732f2b-2217-355b-a01c-82342ab42ffe | -9.27882 | -51.8001 | 2025-10-06 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 435e85b7-a678-3e20-b256-05c2a2afa9b9 | -12.78913 | -56.96033 | 2025-10-06 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9e2264c8-d339-3b33-b386-0360433a3e0c | -13.35967 | -47.5693 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2cf997b1-a7fc-3967-9c4c-2ca613cd8f62 | -14.68424 | -48.3877 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0e62853d-4080-32c7-a4d8-a4f2c2f08e33 | -10.22035 | -48.18182 | 2025-10-06 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1c5d2651-2ac1-3e67-af42-22974fdbc333 | -12.25095 | -47.84906 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 149e2ddb-2631-33de-bee0-c94dd26d964b | -9.39894 | -46.28131 | 2025-10-06 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 22668490-24b3-3420-b3d7-6b069ffc83df | -15.56199 | -47.259 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5dd4b519-a79f-3ae2-ac75-38170e029729 | -13.60423 | -48.6958 | 2025-10-06 04:27:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8bd257e4-57a0-3533-84ed-1b45a6a78c67 | -13.26789 | -47.80665 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7de2a2a3-a394-3da1-8f00-7673ad79495e | -14.75459 | -54.68067 | 2025-10-06 04:27:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 32afe7d2-2985-3c0d-a559-5ba3e2bf6ccd | -13.27798 | -47.17158 | 2025-10-06 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c1404e40-4ee1-3c9a-9603-6da043d9aee1 | -10.6262 | -48.68928 | 2025-10-06 04:27:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 51ec326a-4d3a-3bbb-9714-b7e284ef8285 | -10.85705 | -47.96671 | 2025-10-06 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 63923c53-dd31-3c4a-af17-59f7a5354606 | -14.69046 | -48.28343 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ac2e3178-af8c-3358-a37e-51e3de9ac9da | -12.4064 | -45.1587 | 2025-10-06 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7c752c41-9a64-3db4-916b-abda8a28d534 | -15.22657 | -49.28101 | 2025-10-06 04:27:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 040834e4-264e-3ad5-aa23-4a02ccb19d51 | -14.919 | -46.86123 | 2025-10-06 04:27:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3bd0a7c1-83f5-30cd-8944-545aa9d3b328 | -11.01034 | -50.71107 | 2025-10-06 04:27:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5bad1dd5-918f-3bf3-b975-22a8716d360f | -12.40567 | -51.12883 | 2025-10-06 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d2acfcf-122e-349c-9314-8e92b053b560 | -14.53945 | -46.96622 | 2025-10-06 04:27:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3f2c2fa6-98b7-3100-8b0d-69fbb2c6724b | -13.33287 | -47.78514 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd38c9aa-0903-3ebe-8e87-1c7787abcc0c | -13.63394 | -48.72267 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9bb0788f-e370-3d6f-9f84-646db8089a26 | -13.28705 | -47.57509 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 76a738d2-24cd-3349-abaf-863e6c09e68e | -11.65476 | -47.02374 | 2025-10-06 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 77472dc8-5d33-3509-8dd6-ba2844e67b00 | -14.68988 | -48.30873 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0aa8b4e8-7b1b-3585-9970-bfddf4cf3865 | -11.18735 | -49.99786 | 2025-10-06 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f9612d3-2837-342f-9133-5082236dd423 | -12.90815 | -46.81322 | 2025-10-06 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ca2219a0-8171-390c-9eb6-e0d64a5e83a8 | -13.14586 | -50.87106 | 2025-10-06 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e3866205-7e19-3dce-a349-99080f96233c | -11.23093 | -47.77609 | 2025-10-06 04:27:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 157d2e91-151a-333d-9e86-e1e64e5a67b2 | -15.36111 | -47.99733 | 2025-10-06 04:27:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 135e6734-d79e-3c70-961d-66ca46a5cd18 | -15.61613 | -52.53255 | 2025-10-06 04:27:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0663b0df-f18f-369f-a758-e6136752ae6a | -13.30523 | -48.06932 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 267b347c-438f-30fe-96fc-7c5d969f6cdd | -13.34055 | -47.18481 | 2025-10-06 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e14e2c2d-65c7-30fc-826a-65aca4f8eca4 | -14.93173 | -46.82236 | 2025-10-06 04:27:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8c77d5e9-47ec-3cf7-99ad-aed628821e6f | -11.49026 | -45.03481 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a007c5fe-11e5-39f0-be97-c223dd46cf5c | -13.12488 | -48.00336 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 95abfb08-dfe1-3dc7-882a-4254e0358714 | -11.14339 | -47.16447 | 2025-10-06 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 75ea7ccd-b3f9-3e90-9e81-185dbee1b74d | -11.67587 | -47.47909 | 2025-10-06 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 17b8ef6f-9639-3c5d-b127-19db97447a26 | -14.64197 | -56.01595 | 2025-10-06 04:27:00 | NOAA-21 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 151eda60-6db0-37aa-81db-2b47901ae1f3 | -11.50643 | -54.45877 | 2025-10-06 04:27:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9f7eafc7-2899-391c-a48d-f994bf940a27 | -11.67917 | -47.47962 | 2025-10-06 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 98be9e5f-e5d1-3c20-9c63-aad68a224620 | -11.91761 | -46.23815 | 2025-10-06 04:27:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3fb561b2-0ae7-31cd-84e4-124272f48fff | -9.56206 | -50.78428 | 2025-10-06 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9e343a30-f752-36f9-b75e-0145b2456861 | -11.65091 | -47.02672 | 2025-10-06 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 01ca9b83-15e6-3160-aad7-d94f6775c197 | -11.35082 | -47.66267 | 2025-10-06 04:27:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f759d90b-dbc5-3eba-8d51-7e256ad0677f | -12.98906 | -51.0425 | 2025-10-06 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7a52f42a-17e3-31d8-b1df-c1f82ca1f5b8 | -11.67776 | -45.30688 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 28d98f09-0e2c-3c49-9f49-c16c4a569736 | -9.88879 | -43.70548 | 2025-10-06 04:27:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| d11b9d3e-463b-39dd-b3cb-53af99f08df8 | -11.81563 | -44.89131 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a17a4278-37d7-3d07-888c-ddca114e379e | -14.74266 | -54.66593 | 2025-10-06 04:27:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9691a3ae-b107-37f6-87ad-e425278c945f | -14.61214 | -46.73385 | 2025-10-06 04:27:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a8159778-55dd-375a-909b-5062a73e6e44 | -10.41899 | -45.40583 | 2025-10-06 04:27:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 17aaaedd-fc7d-3f01-9a8f-4804bda46dae | -13.27551 | -47.58407 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5e06be77-9138-3040-94f1-4bc985d04f59 | -13.26641 | -47.18059 | 2025-10-06 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 301d2698-27cf-3e19-b2da-f47d120b10d8 | -15.50153 | -46.85406 | 2025-10-06 04:27:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d9e212bd-020c-3e9b-836c-e2783e2a9f6e | -10.2789 | -44.36575 | 2025-10-06 04:27:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b7d54437-81c2-3dde-8e34-0597e6b1bb13 | -14.86184 | -51.49808 | 2025-10-06 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49418861-ff38-3171-8853-578191568c26 | -14.56263 | -46.67305 | 2025-10-06 04:27:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 36e1d06a-4795-3c18-a818-5532da0b6c5b | -8.15722 | -54.8446 | 2025-10-06 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 32ad7707-cfc6-3377-ae75-72b57e8f29c8 | -11.1832 | -50.00123 | 2025-10-06 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b7165e27-1662-39bf-93c4-ba25ac4dc9a0 | -13.65486 | -47.28611 | 2025-10-06 04:27:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| efd01ea8-a715-3abd-9f83-2300b5aa4e82 | -11.22145 | -54.86377 | 2025-10-06 04:27:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 800c23d4-6010-3250-a4bd-bed37dc7b9f5 | -12.98543 | -46.79583 | 2025-10-06 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5bb26c6f-ff44-3cde-a945-4143f25e95be | -11.16198 | -47.9339 | 2025-10-06 04:27:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ca701550-3490-3b1d-99ba-a11d806bb275 | -11.80638 | -45.12468 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 86ae10ee-e06d-3186-b8bf-45312f8d417a | -15.16809 | -45.71511 | 2025-10-06 04:27:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9e6baa52-8de7-3a31-9112-5e3ba4a7b9b3 | -11.22379 | -47.73538 | 2025-10-06 04:27:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2e14364c-4d6e-33ec-87fd-b9a13142ccc7 | -13.08978 | -47.839 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 11d1ff65-482d-328a-bc8c-d68a3ba404f4 | -13.26311 | -47.18002 | 2025-10-06 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e9798322-d9fc-3fab-848f-12b72f5ce77e | -13.07712 | -47.96306 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c2c17259-39bf-3c12-ae42-cfbab75a1208 | -15.52961 | -46.86176 | 2025-10-06 04:27:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f3fd3091-eb4c-3b2a-9d94-8e02c40b2c13 | -13.33724 | -47.18426 | 2025-10-06 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 86838a06-ecce-3952-8701-0788a0570975 | -11.15258 | -47.95039 | 2025-10-06 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f3897e40-e012-3f61-bb62-273bd4819119 | -10.21536 | -45.49917 | 2025-10-06 04:27:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bac0c121-d321-32b3-b813-2bda31eadae9 | -8.61686 | -54.99345 | 2025-10-06 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0050fa92-f01f-3957-b051-182b15ec4abf | -10.36092 | -48.15405 | 2025-10-06 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8ca21072-79ec-3bcc-9984-59749e29d5e3 | -13.72328 | -48.07293 | 2025-10-06 04:27:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6a5b8f42-9cab-3741-aa0e-b2ab5a6dcc85 | -13.68857 | -47.35366 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d6dc993a-058f-3683-b5f3-a19d6d97edcd | -14.628 | -52.54422 | 2025-10-06 04:27:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f2e5c851-463a-3f99-a7ce-f9d28dd52fc7 | -13.07991 | -47.92384 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b95f7660-8fc7-39b8-862e-afde4c927ec6 | -15.30915 | -47.31555 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c72afdc9-2614-37fa-8f4e-eaf969e10bdd | -15.22325 | -49.28043 | 2025-10-06 04:27:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 4c6e0cc3-690e-39b3-b3f5-58a0d5510939 | -14.852 | -48.74751 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d65eebd4-265d-33d0-922b-f0f545c2fcfc | -15.94873 | -48.6132 | 2025-10-06 04:27:00 | NOAA-21 | ALEXÂNIA | GOIÁS | Brasil | 5200308 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 36cadabf-5973-3cc2-b541-67afa876b718 | -11.81278 | -45.10542 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 114dd7b7-250d-3627-80c8-260a228a4786 | -12.25422 | -49.21237 | 2025-10-06 04:27:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7f3315b5-431b-33ff-bdff-30dd2cfd2ab0 | -11.07607 | -47.91651 | 2025-10-06 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 57438cd3-ce3a-316a-9632-a02623b79418 | -16.03911 | -50.95856 | 2025-10-06 04:27:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e2eb7883-59ce-3cc4-86fc-ba7e2617702d | -13.55682 | -47.23772 | 2025-10-06 04:27:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dcdf2f60-3ec1-348b-87dd-4f25cab82329 | -12.91221 | -47.29401 | 2025-10-06 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7c0787b8-1a25-32cb-85e4-ba3878036461 | -11.05197 | -47.7689 | 2025-10-06 04:27:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a7c8c10a-8560-3d2f-a292-468395bd3d55 | -10.27216 | -44.95498 | 2025-10-06 04:27:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d01fbd7b-01f2-35fa-b055-6d8d8683131b | -13.23947 | -48.46386 | 2025-10-06 04:27:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| fe74a733-f1aa-3782-9857-7f142be0f2e1 | -9.66819 | -45.65794 | 2025-10-06 04:27:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c6e81efb-ad90-328b-a1de-1880e88e1ccd | -13.08703 | -47.83495 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 38760ec4-ed69-32f8-9c09-83560af556dd | -12.47877 | -45.55106 | 2025-10-06 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e0f78272-d860-345f-94eb-13ba308d0f88 | -9.05902 | -51.36355 | 2025-10-06 04:27:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3d808f67-26de-38fc-9f1e-42193942a84a | -13.56484 | -48.14782 | 2025-10-06 04:27:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cab15170-c286-344f-b6dc-6b831d96d17c | -13.10728 | -48.00772 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |


[Clique aqui para ver as próximas entradas](README53.md)
