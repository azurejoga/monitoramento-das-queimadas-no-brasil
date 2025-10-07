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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 675f6c18-fb7d-3274-a117-8c868c6fb570 | -22.1536 | -49.3834 | 2025-10-07 04:40:00 | NPP-375D | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0c5d471a-d55c-3074-beb6-2487cef2c55e | -21.51548 | -45.60327 | 2025-10-07 04:40:00 | NPP-375D | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 2ec50859-19b5-3f5b-8c87-1a62f5279933 | -18.15592 | -53.38171 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 502384e4-c4c7-3fce-a87c-3de2389b2e19 | -22.54548 | -44.44962 | 2025-10-07 04:40:00 | NPP-375D | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 19.5 |
| dde2fda0-fcb7-3c02-b3ab-68270ef55617 | -18.113 | -53.3559 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 09afbc96-7cde-389d-a90d-14c7c4850e06 | -22.90277 | -45.58822 | 2025-10-07 04:40:00 | NPP-375D | TREMEMBÉ | SÃO PAULO | Brasil | 3554805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0069d9f3-0f02-3c03-966b-32703b4ade66 | -21.77052 | -47.78488 | 2025-10-07 04:40:00 | NPP-375D | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5bf081b9-28e4-365f-b5dc-9ef2f6d99712 | -22.18027 | -49.37115 | 2025-10-07 04:40:00 | NPP-375D | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 12.8 |
| a5f7c2f4-f700-38af-b574-803a50863f7e | -18.16089 | -53.374 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3fb99938-36dd-3e27-a2bb-3bf0c3597a18 | -19.63202 | -43.77343 | 2025-10-07 04:40:00 | NPP-375D | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3972f87a-d04b-3899-8678-ce62191a84fb | -22.0187 | -49.5483 | 2025-10-07 04:40:00 | NPP-375D | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 4d963771-dbc0-334f-a678-d0be5749799c | -20.20438 | -43.91386 | 2025-10-07 04:40:00 | NPP-375D | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ca0921d4-1c60-31f2-a7cb-b879c2f4b52b | -22.543 | -44.98908 | 2025-10-07 04:40:00 | NPP-375D | CRUZEIRO | SÃO PAULO | Brasil | 3513405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| c8e1f863-2721-3a1b-a064-160dfb3d3969 | -18.11518 | -53.34339 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 10.3 |
| bd7f2ede-c10a-303b-8678-19ed5d06b063 | -22.17909 | -49.37925 | 2025-10-07 04:40:00 | NPP-375D | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3c9e6505-a43e-3ded-babd-491e327dab78 | -22.54728 | -44.98592 | 2025-10-07 04:40:00 | NPP-375D | CRUZEIRO | SÃO PAULO | Brasil | 3513405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| cda43139-0d11-3b24-85fd-d5ca5393de3e | -20.07566 | -49.59508 | 2025-10-07 04:40:00 | NPP-375D | RIOLÂNDIA | SÃO PAULO | Brasil | 3544202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a282d88f-f002-3a8f-95eb-59fdf5b7143d | -18.56959 | -49.25764 | 2025-10-07 04:40:00 | NPP-375D | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 17459c36-573f-30ec-8695-3a7980a7373c | -21.90278 | -44.87537 | 2025-10-07 04:40:00 | NPP-375D | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b02ee634-b91a-38e6-80f3-d260409ee49e | -18.13981 | -53.36941 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6bc8929f-f57b-37a2-bd59-e32b7d9a4917 | -20.05534 | -49.54447 | 2025-10-07 04:40:00 | NPP-375D | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| 2e204640-29d2-3d30-ae11-f9e106bcd2f8 | -20.51466 | -42.84608 | 2025-10-07 04:40:00 | NPP-375D | AMPARO DO SERRA | MINAS GERAIS | Brasil | 3102506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 46e15c7a-5f09-35fb-916a-15c3e06105eb | -18.97313 | -47.82957 | 2025-10-07 04:40:00 | NPP-375D | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| e2760444-dca0-3506-a70b-501fba927734 | -18.10661 | -53.35077 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2825ad79-4ef7-347c-bb37-83162843cb79 | -22.17331 | -49.37006 | 2025-10-07 04:40:00 | NPP-375D | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2e1c5a12-4198-34f1-92f1-6bec5b057017 | -18.11153 | -53.36432 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 916553ba-9be4-3303-bbaa-48bef2a3269d | -20.48687 | -47.02688 | 2025-10-07 04:40:00 | NPP-375D | CÁSSIA | MINAS GERAIS | Brasil | 3115102 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0d80fb73-cdb5-37b6-8d6f-b80cffd76946 | -21.91003 | -44.88984 | 2025-10-07 04:40:00 | NPP-375D | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 4353aa98-a020-3d7a-9f2b-1ba4c1ac58ca | -18.11092 | -53.34696 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 6c04f625-496c-33d5-bae7-81d06d79715f | -22.94501 | -49.29909 | 2025-10-07 04:40:00 | NPP-375D | ÓLEO | SÃO PAULO | Brasil | 3533809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 697b700f-4bc6-3c21-aa8e-73665ce22f4b | -21.90668 | -44.88035 | 2025-10-07 04:40:00 | NPP-375D | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 19910ada-6c5b-38eb-90ce-59f5b55ee0ca | -19.85351 | -49.07508 | 2025-10-07 04:40:00 | NPP-375D | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 838ee1da-5d54-3629-a24d-e684e0aff83d | -21.48222 | -46.72133 | 2025-10-07 04:40:00 | NPP-375D | TAPIRATIBA | SÃO PAULO | Brasil | 3553609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| aac5f94f-7246-3062-bdab-a4a5ebbcada9 | -18.16238 | -53.36533 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0fbc48f4-1be1-3a12-87ba-2214d63cf82f | -22.00281 | -49.72924 | 2025-10-07 04:40:00 | NPP-375D | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 8e7296e1-10a1-3194-8e9a-a52f7ccffe25 | -18.11374 | -53.35168 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3d09ec03-2558-37c0-aa54-1e12763e56d8 | -22.54798 | -44.98494 | 2025-10-07 04:40:00 | NPP-375D | CRUZEIRO | SÃO PAULO | Brasil | 3513405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 6a724357-3e0a-3079-a1a6-fa4f2a725c62 | -20.11772 | -44.41085 | 2025-10-07 04:40:00 | NPP-375D | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| a4ea4a23-c467-336a-b1b2-92cca3c35152 | -21.62351 | -44.00295 | 2025-10-07 04:40:00 | NPP-375D | SANTANA DO GARAMBÉU | MINAS GERAIS | Brasil | 3158706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 67d6cb55-e305-318c-90a5-18c1208ead65 | -18.83961 | -48.29245 | 2025-10-07 04:40:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6fa57901-471e-3929-9b9f-97bfa9059d13 | -23.3931 | -47.01057 | 2025-10-07 04:40:00 | NPP-375D | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| edaafae5-0947-323d-a7ea-16dbd51c8a85 | -22.01525 | -49.54777 | 2025-10-07 04:40:00 | NPP-375D | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f9286817-5a88-329a-86c7-27ec89474ba8 | -22.5268 | -49.11155 | 2025-10-07 04:40:00 | NPP-375D | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| adfc93a4-2fb1-3395-bc47-aad19730bbc0 | -22.01142 | -49.71849 | 2025-10-07 04:40:00 | NPP-375D | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 90717bb1-c426-31b2-a630-3fa7327e836a | -18.15108 | -53.36745 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eb5ed607-2eb8-3240-b976-f23c3dd8deff | -21.4324 | -46.67629 | 2025-10-07 04:40:00 | NPP-375D | TAPIRATIBA | SÃO PAULO | Brasil | 3553609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 012fb67e-c07e-38bf-a95d-73e263311428 | -20.84844 | -49.47958 | 2025-10-07 04:40:00 | NPP-375D | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 41d4bc05-6dd3-3e93-ab73-5d9496ea7818 | -18.15811 | -53.36895 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3cb8d251-db92-3b7f-a2e7-be170f92658d | -23.23714 | -46.7102 | 2025-10-07 04:40:00 | NPP-375D | CAMPO LIMPO PAULISTA | SÃO PAULO | Brasil | 3509601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3cad814f-d36b-39c8-a5c1-e11381d64512 | -18.12008 | -53.35712 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 660b93e9-c403-3c4b-92f8-5b009ab7d51a | -18.6025 | -46.8 | 2025-10-07 04:40:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2e3887b9-0b20-35cc-8455-b8d92192a81c | -18.11873 | -53.34396 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 749c4219-42a7-3cfe-a118-28d471355dd1 | -20.41278 | -46.045 | 2025-10-07 04:40:00 | NPP-375D | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9b14ddfd-44e6-379c-a970-c20bd263225a | -22.14955 | -49.38689 | 2025-10-07 04:40:00 | NPP-375D | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1a1985f0-458e-3e6f-b64a-639f27ec7fa6 | -19.59661 | -44.8634 | 2025-10-07 04:40:00 | NPP-375D | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dc2e19f8-b8b6-39a2-9d17-718c6fafa5d8 | -21.39265 | -45.05471 | 2025-10-07 04:40:00 | NPP-375D | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 5edaffd2-2623-39a9-8dde-c8d55d49ad77 | -20.82518 | -42.48316 | 2025-10-07 04:40:00 | NPP-375D | MIRADOURO | MINAS GERAIS | Brasil | 3142106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| f46c49cf-115e-37b3-a5a7-b12cdf76f23f | -21.74318 | -44.41879 | 2025-10-07 04:40:00 | NPP-375D | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 7db35312-7081-376a-a6c4-02e7e6415b0f | -20.05137 | -49.54774 | 2025-10-07 04:40:00 | NPP-375D | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 17.4 |
| c0429242-8a1d-33ea-b729-d339fed460fc | -21.51529 | -45.60499 | 2025-10-07 04:40:00 | NPP-375D | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 69ada16f-e969-3fac-bbf1-f5418669eed5 | -22.01812 | -49.55228 | 2025-10-07 04:40:00 | NPP-375D | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 66817d93-d085-3d48-827f-9be77d879555 | -18.14681 | -53.37109 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a7893e56-cee9-3da5-aeff-cc379c711cbf | -18.15943 | -53.38247 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| efdbb898-2bb4-3b18-ac14-61dad28a3f5e | -21.49027 | -46.0215 | 2025-10-07 04:40:00 | NPP-375D | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 5f32d97c-40d8-32e1-9b7b-a578e84b22c5 | -20.05931 | -49.54117 | 2025-10-07 04:40:00 | NPP-375D | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.7 |
| 374d9f14-8787-37d0-b0de-2b3b6bdab7d9 | -18.10549 | -53.36079 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| debccd80-7785-3137-8e6d-92245e37e897 | -20.05591 | -49.5406 | 2025-10-07 04:40:00 | NPP-375D | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| 1338c94c-6f46-3360-a69c-16c4ab755517 | -22.54952 | -44.45505 | 2025-10-07 04:40:00 | NPP-375D | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 19.5 |
| a04548ef-bc6b-3054-805b-410e52dec158 | -18.88399 | -48.03275 | 2025-10-07 04:40:00 | NPP-375D | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 839ab83e-bed9-3b6b-ac47-c119bce84e12 | -23.07184 | -45.99794 | 2025-10-07 04:40:00 | NPP-375D | SÃO JOSÉ DOS CAMPOS | SÃO PAULO | Brasil | 3549904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e3d5a73b-db54-39a5-82df-6a4cbcb2d630 | -22.17679 | -49.37061 | 2025-10-07 04:40:00 | NPP-375D | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 8243f918-80d9-3e47-a941-5ed4b006a17a | -23.32089 | -45.75963 | 2025-10-07 04:40:00 | NPP-375D | JAMBEIRO | SÃO PAULO | Brasil | 3524907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1c119541-e02e-387a-83f9-5fb466764390 | -22.67813 | -49.18462 | 2025-10-07 04:40:00 | NPP-375D | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6200da75-35b9-34d4-b933-fcd9a828fc58 | -20.58575 | -46.3086 | 2025-10-07 04:40:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 742d2a56-272f-3dfd-996a-8d040b6bb7d4 | -22.11957 | -44.99545 | 2025-10-07 04:40:00 | NPP-375D | SÃO LOURENÇO | MINAS GERAIS | Brasil | 3163706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f9531db5-6a6d-3645-89f8-10fccd81197f | -19.04844 | -48.13783 | 2025-10-07 04:40:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cb580426-5dd2-30e0-b94e-1d7f5d394757 | -18.97478 | -47.83179 | 2025-10-07 04:40:00 | NPP-375D | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 24f22b18-9307-3aa8-8d52-1d2547ebcd22 | -18.18273 | -53.37416 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2aef1534-a030-3e5d-b32a-768122acc9c3 | -19.0182 | -49.74985 | 2025-10-07 04:40:00 | NPP-375D | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| adb12e9d-5a3e-3ba3-8c82-2261be2c2d6d | -23.20613 | -47.24296 | 2025-10-07 04:40:00 | NPP-375D | SALTO | SÃO PAULO | Brasil | 3545209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e9ec56c9-6944-31a8-a8ea-0408ef3e0c99 | -22.58265 | -44.44987 | 2025-10-07 04:40:00 | NPP-375D | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b4563680-c59f-3235-b5fe-a73f3a65446d | -21.73864 | -44.41817 | 2025-10-07 04:40:00 | NPP-375D | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 2c444d98-327e-3647-bb70-79fa9920cadd | -18.99331 | -48.37367 | 2025-10-07 04:40:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 87a3bc18-aac0-3b39-b204-bf129c8205c1 | -18.11801 | -53.34809 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8a4c0a76-4b1f-33ec-9fe8-0b4eb7b0eca1 | -20.28073 | -48.51006 | 2025-10-07 04:40:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 35267dc8-3b50-3c2d-bd88-3622de34b100 | -18.97014 | -47.82473 | 2025-10-07 04:40:00 | NPP-375D | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 864e367f-b206-3eea-8dd5-c087bc8278cc | -20.32192 | -45.11528 | 2025-10-07 04:40:00 | NPP-375D | PEDRA DO INDAIÁ | MINAS GERAIS | Brasil | 3148905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 7dbb7e36-e9d3-301b-9db4-0304b195442e | -19.93436 | -44.63957 | 2025-10-07 04:40:00 | NPP-375D | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 5027f715-0d7b-3597-b482-295d8839213f | -20.09705 | -44.19971 | 2025-10-07 04:40:00 | NPP-375D | MÁRIO CAMPOS | MINAS GERAIS | Brasil | 3140159 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 01794214-ab01-39ee-96f3-04768e0b4614 | -18.10763 | -53.34816 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 42bbcb7d-10a0-3675-aebb-f893c84f0ecf | -21.76976 | -47.7777 | 2025-10-07 04:40:00 | NPP-375D | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3646e0cd-8d4b-3f84-80b3-47e39c8aed3d | -23.07162 | -45.99409 | 2025-10-07 04:40:00 | NPP-375D | SÃO JOSÉ DOS CAMPOS | SÃO PAULO | Brasil | 3549904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1643b265-05d0-36e6-9be7-972a4c619072 | -19.39497 | -44.39257 | 2025-10-07 04:40:00 | NPP-375D | CAETANÓPOLIS | MINAS GERAIS | Brasil | 3109907 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d1a5cbf3-3f83-3963-bda6-694413781ba6 | -22.17444 | -49.38678 | 2025-10-07 04:40:00 | NPP-375D | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 17.7 |
| f8d5329b-82ae-3a08-ad91-a83642491e5b | -18.14259 | -53.37441 | 2025-10-07 04:40:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 37eccded-da1a-3dc5-8a62-15c9a43fd94d | -21.52015 | -45.5998 | 2025-10-07 04:40:00 | NPP-375D | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| a4b1c875-bff1-345a-87ea-04d69fd4c761 | -21.79881 | -46.15907 | 2025-10-07 04:40:00 | NPP-375D | CAMPESTRE | MINAS GERAIS | Brasil | 3111002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3ae626b5-1fa0-302f-8d72-964716043f70 | -21.5158 | -45.60093 | 2025-10-07 04:40:00 | NPP-375D | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f25f1f03-35ee-3dbc-9fc8-5b77aaec5e85 | -21.60951 | -44.00143 | 2025-10-07 04:40:00 | NPP-375D | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 165d60f5-cc58-3139-8cb9-bcf2ec92f5a0 | -22.54496 | -44.45425 | 2025-10-07 04:40:00 | NPP-375D | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 19.5 |


[Clique aqui para ver as próximas entradas](README81.md)
