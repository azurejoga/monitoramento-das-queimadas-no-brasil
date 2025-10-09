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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 220446e7-b93a-3a6f-8001-b78ca1d9df82 | -12.425 | -45.7056 | 2025-10-09 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 150.4 |
| 68b6bfaa-6240-3322-b06c-17de3c068d69 | -13.7913 | -45.8321 | 2025-10-09 12:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 165.8 |
| dd245bc7-2592-34c2-ab38-942ed0633109 | -13.7904 | -45.8782 | 2025-10-09 12:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 486.8 |
| 9e3eca29-dd3b-30af-8c69-56003ed187a3 | -13.8103 | -45.8519 | 2025-10-09 12:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 613.5 |
| 36189741-9608-3821-bfda-2117a8a2115a | -14.2559 | -45.8681 | 2025-10-09 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 144.8 |
| e8759970-7a04-34b8-8a5f-deae9236c330 | -12.6964 | -47.6776 | 2025-10-09 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 171.3 |
| 77003d24-b388-3999-8429-f0369bc15e85 | -11.7833 | -45.1347 | 2025-10-09 12:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 105.9 |
| a682144d-cdc2-32ce-9353-bacda205f9ac | -13.7909 | -45.8552 | 2025-10-09 12:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 496.9 |
| de3b27a2-744d-31cf-8bf0-0154b6fbea75 | -14.2754 | -45.8647 | 2025-10-09 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 9a5b9f96-4e07-342e-a66b-c354224b4d54 | -11.993 | -45.1958 | 2025-10-09 12:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 1520ea2f-3e89-3a43-87f2-120c3942296c | -13.8302 | -45.8255 | 2025-10-09 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 196.2 |
| d3bed1b2-2e97-34f2-8ac7-aef8c901dfd4 | -14.2754 | -45.8647 | 2025-10-09 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 106.4 |
| d65a521a-13b0-3a85-aed1-7c8192ff49ef | -10.1905 | -44.5471 | 2025-10-09 12:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 4d404652-4b3b-38b0-82d9-d4fa70f803bb | -12.6968 | -47.6552 | 2025-10-09 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 132.7 |
| 6d05f27c-91b6-3a8c-b72b-67d94e9c2371 | -11.9926 | -45.2189 | 2025-10-09 12:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 117.6 |
| d0ef63df-17fa-3c00-817b-f6789e836c7f | -11.993 | -45.1958 | 2025-10-09 12:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 146.3 |
| 17f32551-e611-3c86-89cc-579175cfcce0 | -14.4079 | -46.026 | 2025-10-09 12:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 9b7b9aee-48a6-34d0-a14f-157b9d50490e | -12.425 | -45.7056 | 2025-10-09 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 143.4 |
| 0eed19a8-e041-3a17-a2f6-2a04749bdbeb | -14.2559 | -45.8681 | 2025-10-09 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 128.9 |
| 620aa92a-a60f-3d26-97c1-795f9f28f522 | -12.6964 | -47.6776 | 2025-10-09 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 180.1 |
| 99d6e885-d97f-3e66-8bb3-ce908bf0cc1c | -17.6415 | -47.2103 | 2025-10-09 12:40:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 107.1 |
| ea7514f4-88aa-3685-a5a2-f610cfc2f051 | -11.7829 | -45.1578 | 2025-10-09 12:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 1ad5a59b-8a82-3cbe-8ee3-330859113115 | -11.9926 | -45.2189 | 2025-10-09 12:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 114.2 |
| df6f621d-7502-3677-9cf6-a2a3130239ce | -11.993 | -45.1958 | 2025-10-09 12:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 145.7 |
| 3042cabd-2f3e-3178-8663-45cbadc7cfc1 | -11.7833 | -45.1347 | 2025-10-09 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 0b4d5a66-c73f-3680-8c4e-1c7ea513a9e7 | -12.6964 | -47.6776 | 2025-10-09 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 190.2 |
| 424ec19f-2cad-316f-ab8f-9dc3d54cc155 | -11.7829 | -45.1578 | 2025-10-09 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 101.5 |
| feed238b-ed5b-35d3-b695-0bc767ebda43 | -14.2754 | -45.8647 | 2025-10-09 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 109.2 |
| d89ac464-c2b9-3c06-b4c0-82c11095ad37 | -10.1905 | -44.5471 | 2025-10-09 12:50:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 83f7fc87-3d00-3f3c-b177-8107787e0583 | -12.425 | -45.7056 | 2025-10-09 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 145.8 |
| 09b3f308-2bc9-3d33-8e40-69cb3950f0ba | -11.785 | -45.0421 | 2025-10-09 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 103.1 |
| fd6126f2-7995-3d73-9e68-d1c7a18df0e9 | -14.2559 | -45.8681 | 2025-10-09 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 0c508b96-93bc-3edd-a077-d07b2ff50bb6 | -14.4079 | -46.026 | 2025-10-09 12:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 269a3d64-fcd7-3327-9ddf-585e787cb2ce | -15.2384 | -46.3616 | 2025-10-09 12:50:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 110.4 |
| d017ff77-bde2-3dcb-916b-f5d89c8401f9 | -12.6964 | -47.6776 | 2025-10-09 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 176.6 |
| 6232a8de-3538-3b6e-91de-d10eeaa3f2df | -11.7215 | -44.3084 | 2025-10-09 13:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 6a66abfa-fc7b-3d23-a050-d4277ca9d0bb | -15.3988 | -47.9712 | 2025-10-09 13:00:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 171.7 |
| e2404c8f-5aac-3110-b8e6-8c885d9e0958 | -12.4434 | -45.7486 | 2025-10-09 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 112.4 |
| e878170a-ee9f-3270-840f-9374ca0e97b3 | -14.2559 | -45.8681 | 2025-10-09 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 38f7ed48-87ae-363b-8460-561ad5f27c02 | -11.785 | -45.0421 | 2025-10-09 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 105.6 |
| db8ae232-1fcf-32e8-8b14-7a4e22b2a279 | -15.2384 | -46.3616 | 2025-10-09 13:00:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 118.5 |
| f44158db-7550-322f-bf70-88c5ee2104c1 | -11.993 | -45.1958 | 2025-10-09 13:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 139.0 |
| 1426468d-d91e-322e-8449-47f7dfecd651 | -17.5828 | -47.1762 | 2025-10-09 13:00:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 93.5 |
| e720314f-fa0f-3076-a9b5-8e1800455b29 | -10.1905 | -44.5471 | 2025-10-09 13:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 140.6 |
| 5fc9be07-dfb2-3651-8732-c6ac51bebb78 | -12.425 | -45.7056 | 2025-10-09 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 296.4 |
| c68dced6-72fc-374e-b325-e927efc93edd | -11.7829 | -45.1578 | 2025-10-09 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 3cbbf557-81ba-30e9-abe9-6ef6f06a0012 | -10.1901 | -44.5703 | 2025-10-09 13:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 2f86c212-5941-3f82-8ab1-5d30a17e4010 | -15.3984 | -47.9938 | 2025-10-09 13:00:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 185.9 |
| 4b0dc770-da60-3d48-a5bd-75d88f273c60 | -11.7833 | -45.1347 | 2025-10-09 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 61f1350f-1ee6-300a-bff5-3ea7d7604c89 | -13.2971 | -48.4579 | 2025-10-09 13:00:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 4807bcdd-cc2a-3250-acc4-7a71f24b708a | -14.8456 | -48.3547 | 2025-10-09 13:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 115.1 |
| a00fd2be-048c-36e6-9ada-3f1af326672f | -11.785 | -45.0421 | 2025-10-09 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 107.7 |
| a2112144-afb7-3faa-9604-862af4054b3f | -11.4992 | -44.9684 | 2025-10-09 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 353.4 |
| 218c78ee-7dc1-3488-bdaa-d9650af08937 | -10.1905 | -44.5471 | 2025-10-09 13:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 97716372-4724-303d-80b7-92ae5bff2ec6 | -11.7238 | -46.354 | 2025-10-09 13:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 140.3 |
| c8244289-c6be-3adb-8b01-773a0e9c281b | -11.7215 | -44.3084 | 2025-10-09 13:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 127.1 |
| 46ebd48e-4fad-3029-8b49-bc1341c74bac | -10.1901 | -44.5703 | 2025-10-09 13:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 0808c398-eacb-3e9f-b1e2-8096ee47f288 | -11.7833 | -45.1347 | 2025-10-09 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 116.8 |
| ffe5737a-0d5b-3f86-a556-b6eb1ba1bcde | -11.4988 | -44.9915 | 2025-10-09 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 126.0 |
| e9a7187a-5369-3b22-a53b-c1dc45ef3a95 | -11.7829 | -45.1578 | 2025-10-09 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 123.0 |
| b1351c79-8bdc-3401-a176-d0a7fa0ab218 | -14.4084 | -46.0029 | 2025-10-09 13:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 180.3 |
| 87f9ae22-1da0-3ef9-ac1d-e2782c41f1a4 | -12.6964 | -47.6776 | 2025-10-09 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 161.4 |
| c4a016c6-b5b2-3701-a803-1541d57ba5bc | -14.8832 | -51.4561 | 2025-10-09 13:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 051bc8df-63ea-37c8-b98c-3980dcb170d7 | -15.3988 | -47.9712 | 2025-10-09 13:10:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 128.8 |
| e9a64d2e-2e4b-3d3a-9a6d-3882f61963ed | -12.425 | -45.7056 | 2025-10-09 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 183.6 |
| 6b70b9c2-6658-3d9e-8ce2-a6e7719a78b2 | -13.2967 | -48.4801 | 2025-10-09 13:10:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 0d63eeb8-1e9b-3423-834a-c5570d23d91f | -14.2559 | -45.8681 | 2025-10-09 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 160.7 |
| d38824cf-f166-3af9-9153-84475cdc05eb | -13.2971 | -48.4579 | 2025-10-09 13:10:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 140.0 |
| e3edeafe-0d80-30f4-ba21-30469154985f | -16.0946 | -45.7829 | 2025-10-09 13:10:00 | GOES-19 | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 124.8 |
| d04fd7cc-aa72-3b03-b71a-009c5549613e | -13.8307 | -45.8024 | 2025-10-09 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 174.9 |
| c222726a-1840-3ee9-aeef-f9b3314b2c88 | -11.48 | -44.9711 | 2025-10-09 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 172.5 |
| 1f9f1f49-74b8-3918-8636-c47bdb696b35 | -10.2092 | -44.5678 | 2025-10-09 13:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 6687b633-a012-32a0-8dcd-3beb3a0f42fc | -14.4079 | -46.026 | 2025-10-09 13:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 275.7 |
| faa1e087-6198-3941-bfb5-de6b17188b32 | -15.3984 | -47.9938 | 2025-10-09 13:10:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 120.5 |
| f7a79e73-819d-3ed9-8d7b-8dff570d7156 | -11.993 | -45.1958 | 2025-10-09 13:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 7c4a4e4a-0d63-320f-b4fa-e0128cca20b8 | -14.8835 | -51.4346 | 2025-10-09 13:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 109.3 |
| a25e51fb-6985-3e2c-9ca3-61b60519331e | -10.2092 | -44.5678 | 2025-10-09 13:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 148.9 |
| 5d5d04a4-2d91-359e-98c9-cf919d563256 | -15.3984 | -47.9938 | 2025-10-09 13:20:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 112.6 |
| e7e5c868-9940-3470-97d8-0028c253c50b | -13.2971 | -48.4579 | 2025-10-09 13:20:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 150.3 |
| 7c446640-bf8a-38b1-a1d3-d2973c6dc47b | -13.2967 | -48.4801 | 2025-10-09 13:20:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 7de38855-56af-3e29-b45f-a2b276809b37 | -14.2754 | -45.8647 | 2025-10-09 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 204.9 |
| 6cb9c0d2-34e8-3aac-851a-a1f9f90ffb6a | -9.3019 | -45.6628 | 2025-10-09 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 503180b6-6422-3737-9f6f-a2b6d3939ee9 | -8.6292 | -45.1228 | 2025-10-09 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 108.8 |
| f060c8e3-a144-33ce-95db-d399827ca8c3 | -13.7553 | -45.6999 | 2025-10-09 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 135.6 |
| f70e645b-d297-3a74-b413-4287169afedd | -16.0946 | -45.7829 | 2025-10-09 13:20:00 | GOES-19 | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 118.3 |
| fa7a40e2-3ea0-37fb-99cc-3a51acd86d81 | -8.2083 | -44.1105 | 2025-10-09 13:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 89.8 |
| f799919a-12f5-3906-8ed0-34b1cd63ec3b | -8.6106 | -45.102 | 2025-10-09 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 123.4 |
| bd7ce0ce-49c7-37f8-bc36-94926796f8ea | -8.199 | -43.3659 | 2025-10-09 13:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 100.3 |
| a8256a2a-afe6-30dc-b5cd-6b975dd336ad | -10.1905 | -44.5471 | 2025-10-09 13:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 133.8 |
| 54bb4bec-173c-35c6-aabb-709f4b36b0ee | -8.1807 | -43.321 | 2025-10-09 13:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 187.9 |
| d71c72af-241d-3c62-b58a-5bb7ac6c8fc9 | -11.7829 | -45.1578 | 2025-10-09 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 128.4 |
| 6ed16798-676a-390c-a944-4890a4d91be3 | -14.8832 | -51.4561 | 2025-10-09 13:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 370233f9-b670-3fd1-9262-d2ec42874eda | -8.6103 | -45.1249 | 2025-10-09 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 89e21356-2874-3d7c-a434-fd6334779d1f | -14.2559 | -45.8681 | 2025-10-09 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 227.5 |
| 8025ef42-2d7d-37f8-9dde-45c8546da5c5 | -8.6295 | -45.1 | 2025-10-09 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 118.8 |
| c820be97-436f-39a3-9ef8-2eeb920edb8b | -8.1804 | -43.3445 | 2025-10-09 13:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 151.5 |
| 95f49e98-6fbc-3016-8c7e-65787ec5f1dd | -10.1901 | -44.5703 | 2025-10-09 13:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 135.4 |
| 376a2849-127b-3ce2-b37c-ffa13755648f | -11.7833 | -45.1347 | 2025-10-09 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 5c3e92e1-c779-3fc1-a91c-d91e24468575 | -12.6964 | -47.6776 | 2025-10-09 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 162.3 |
| 724aabf3-b5e3-378f-ac1b-6526134015df | -9.3209 | -45.6607 | 2025-10-09 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 138.1 |


[Clique aqui para ver as próximas entradas](README67.md)
