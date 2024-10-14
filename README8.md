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
| 9f5f62be-2a12-3b31-991e-8a489f10e7aa | -8.4963 | -41.3978 | 2024-10-14 00:37:19 | METOP-C | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f3ea1197-037b-3e3f-abce-b72fdf5c8e31 | -8.4984 | -41.407001 | 2024-10-14 00:37:19 | METOP-C | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 06464a15-bc35-3355-bab2-1ebb6c6109cf | -9.4542 | -45.508499 | 2024-10-14 00:37:19 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f1c90ceb-b674-37bb-9b53-3fbd3d699df1 | -9.4361 | -45.519901 | 2024-10-14 00:37:19 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 16f87385-839d-38dd-9f6a-0b9d12473f66 | -9.4377 | -45.526901 | 2024-10-14 00:37:19 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5fb50478-96cb-384e-86bd-16d10ec71ee8 | -9.4393 | -45.533798 | 2024-10-14 00:37:19 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ba87621d-6966-3730-bc2c-36ff528f817b | -9.4727 | -45.818199 | 2024-10-14 00:37:20 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cd5dbf50-6429-33ee-b1ae-80d217460781 | -9.4743 | -45.8251 | 2024-10-14 00:37:20 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7be44a28-564f-38d3-aa9d-d5c895a3ea7e | -9.4759 | -45.8321 | 2024-10-14 00:37:20 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c954695b-45bc-3995-8b61-3da63de7083c | -9.9009 | -47.7416 | 2024-10-14 00:37:20 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b31cb8ce-c94a-3d28-90b0-da629518851c | -9.4598 | -45.8064 | 2024-10-14 00:37:20 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 78e16564-8b4e-3bb9-9b0d-8b692e5cda15 | -9.4613 | -45.8134 | 2024-10-14 00:37:20 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d1bc73a0-f608-3fd5-b487-613fca75d84a | -9.6749 | -46.903999 | 2024-10-14 00:37:20 | METOP-C | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8f284bc4-826a-37c7-8b1d-5e6d5e0ca695 | -9.6765 | -46.9114 | 2024-10-14 00:37:20 | METOP-C | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3695677d-148c-3afe-b219-ba073cc5cdac | -10.5439 | -50.837898 | 2024-10-14 00:37:20 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 40b3c752-f7fa-39d2-a883-32af432202ec | -9.2675 | -45.231201 | 2024-10-14 00:37:21 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ae79fc24-bf96-326e-a145-acf6a5e295de | -9.2561 | -45.226501 | 2024-10-14 00:37:21 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 82b79729-776e-3fe3-afba-7299293f3f18 | -9.2659 | -45.2243 | 2024-10-14 00:37:21 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f8b7d396-09cf-34d4-bda1-b8e81f2f3b50 | -9.9254 | -48.134602 | 2024-10-14 00:37:21 | METOP-C | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2906a791-c770-36ec-921a-8fdf95770314 | -9.9272 | -48.142899 | 2024-10-14 00:37:21 | METOP-C | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dcca3cdd-3730-3c3e-946f-b8856352afaa | -9.2644 | -45.2174 | 2024-10-14 00:37:21 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e2750546-9c28-3b19-875b-231750e468e4 | -9.4185 | -46.0802 | 2024-10-14 00:37:22 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a90d5644-c2de-345d-9d8d-137dc376d026 | -9.7065 | -47.465 | 2024-10-14 00:37:22 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ddff42c9-cb2e-362e-ad71-005d69f8f494 | -9.7082 | -47.472698 | 2024-10-14 00:37:22 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 02d6f46d-702e-36d7-9537-393d3038669a | -9.7099 | -47.4804 | 2024-10-14 00:37:22 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c39a07ee-665a-377a-a305-a069fa60e86f | -9.6967 | -47.467098 | 2024-10-14 00:37:22 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 60cee2de-7d9a-3f34-9ef7-3eb4906836dc | -9.6984 | -47.4748 | 2024-10-14 00:37:22 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9780e942-9e7a-3eb5-9c52-b9600900d544 | -9.7001 | -47.482498 | 2024-10-14 00:37:22 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 69c781d8-3715-35c8-80bc-fb9251f6a664 | -9.6869 | -47.469299 | 2024-10-14 00:37:22 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bb4542a7-0b72-373a-bb0d-e128109e9b39 | -9.6886 | -47.477001 | 2024-10-14 00:37:22 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c722b644-c497-31b0-82f5-095d061cab70 | -9.6903 | -47.484699 | 2024-10-14 00:37:22 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8a9cf036-c7fd-3963-ba64-747dcd9b214e | -9.9886 | -48.8507 | 2024-10-14 00:37:22 | METOP-C | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0fd9e315-6903-3442-bb46-6c1ec3fe4afe | -9.9906 | -48.859699 | 2024-10-14 00:37:22 | METOP-C | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cfde4751-7083-3eaf-8b6b-e4fa890334d4 | -9.3091 | -46.097401 | 2024-10-14 00:37:23 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7810fd39-b21b-30f3-8a25-6733155a9ec6 | -9.3107 | -46.104401 | 2024-10-14 00:37:23 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 10c7d518-a2f5-3643-bb5c-ca68da91a81a | -9.7334 | -48.2896 | 2024-10-14 00:37:24 | METOP-C | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 99c616d8-a722-3b52-9ba1-0d2df5debdea | -8.4492 | -42.503601 | 2024-10-14 00:37:24 | METOP-C | JOÃO COSTA | PIAUÍ | Brasil | 2205359 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 35d25a67-9ffa-3657-859e-19bbfa56c7b7 | -8.4511 | -42.5116 | 2024-10-14 00:37:24 | METOP-C | JOÃO COSTA | PIAUÍ | Brasil | 2205359 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f83e1092-cef5-39c0-aa39-26e1e338a57a | -9.5614 | -47.6922 | 2024-10-14 00:37:25 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e13e2074-f12f-3ff4-9f73-66d2534f0f91 | -9.5631 | -47.700001 | 2024-10-14 00:37:25 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8ed08cc5-1663-30c7-9949-3e3450b5ea6d | -9.5327 | -47.608601 | 2024-10-14 00:37:25 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2af326b6-6957-3474-800e-9b82a0541d91 | -9.5344 | -47.616299 | 2024-10-14 00:37:25 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5e134a34-8289-3c2b-b21c-a181bef16bf9 | -9.5361 | -47.6241 | 2024-10-14 00:37:25 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 783c61b5-36a4-3fae-b818-a38a241ae8fd | -9.5246 | -47.6185 | 2024-10-14 00:37:25 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1b03ba55-68a6-32ab-8293-0305abf91965 | -9.5332 | -47.797298 | 2024-10-14 00:37:26 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a70d0425-0582-3445-a7e6-fd2307fe5299 | -9.5349 | -47.805199 | 2024-10-14 00:37:26 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 23873527-c6ac-360f-8aa6-44b9923321d3 | -8.3262 | -42.726299 | 2024-10-14 00:37:27 | METOP-C | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7608b437-5420-3fd6-ade9-799f116cbe6d | -8.3281 | -42.7342 | 2024-10-14 00:37:27 | METOP-C | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e7b59ed8-222f-3440-9d59-cc8ff3e47efe | -8.3299 | -42.7421 | 2024-10-14 00:37:27 | METOP-C | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b5a39192-a341-363b-b5fe-584354533230 | -8.3318 | -42.75 | 2024-10-14 00:37:27 | METOP-C | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 63418a06-c9c9-371e-b5bf-e6b7a326f48e | -8.3164 | -42.7286 | 2024-10-14 00:37:27 | METOP-C | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 71afdd2e-9a3c-3a8d-9e35-14cc7954cb90 | -8.3183 | -42.7365 | 2024-10-14 00:37:27 | METOP-C | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3fd51af8-3d97-3614-b0c8-f94cd9c85579 | -8.3201 | -42.7444 | 2024-10-14 00:37:27 | METOP-C | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e5b444c1-7b25-355c-8faa-8a86f42a40f9 | -8.322 | -42.7523 | 2024-10-14 00:37:27 | METOP-C | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f08f257d-5c4f-3a58-9262-2f42b3a9a457 | -9.0995 | -46.493099 | 2024-10-14 00:37:28 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e16aa3a6-fc9e-30d8-891f-5e1497577057 | -8.139 | -42.326599 | 2024-10-14 00:37:28 | METOP-C | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 484e784e-b95f-39c2-87a3-c755595c82f5 | -9.3903 | -47.895 | 2024-10-14 00:37:29 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 987a176c-ce6e-3dac-a14c-0c46a0af9dfa | -9.3921 | -47.903 | 2024-10-14 00:37:29 | METOP-C | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0839ccd8-ecd0-3472-aca1-073abec10882 | -9.6165 | -48.9781 | 2024-10-14 00:37:29 | METOP-C | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0e7fa974-0cf7-32f9-bd5f-e0ebcaceced9 | -9.6184 | -48.987099 | 2024-10-14 00:37:29 | METOP-C | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cef5e30c-631f-3402-a6fe-0fcd6d521f8e | -9.4984 | -48.6702 | 2024-10-14 00:37:30 | METOP-C | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5c412a60-a997-313d-beec-9fa6ac1a3027 | -9.2929 | -48.246601 | 2024-10-14 00:37:31 | METOP-C | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8df98b1a-7445-3991-b6d1-978b77164f89 | -7.5189 | -40.509602 | 2024-10-14 00:37:31 | METOP-C | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| d37ca0f0-78da-362e-a9dc-eb899ae9f17e | -7.1534 | -39.3027 | 2024-10-14 00:37:32 | METOP-C | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 8f834c79-7bb5-3b5e-876e-ada3df120494 | -8.4989 | -44.8904 | 2024-10-14 00:37:32 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 78ad4562-045c-3dd6-8607-c94a0defb147 | -9.3161 | -48.727901 | 2024-10-14 00:37:33 | METOP-C | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ffd8b7bd-54f2-365c-b560-faf4b33c61ea | -9.0974 | -47.777599 | 2024-10-14 00:37:33 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 00439299-d7ed-3ae2-aac0-9a4e27712946 | -9.0876 | -47.7798 | 2024-10-14 00:37:33 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 23a659d7-4959-3680-bba9-6ff34c57a4f8 | -9.0555 | -47.680901 | 2024-10-14 00:37:33 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 88c0823c-bb64-373e-b7ff-c3470ffc28c7 | -9.0572 | -47.688702 | 2024-10-14 00:37:33 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 31123c73-3b11-3cfd-b3df-50064b04d131 | -9.0778 | -47.781898 | 2024-10-14 00:37:33 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 41be8845-b7e4-3d54-b0de-0877cecbb644 | -9.0992 | -47.925499 | 2024-10-14 00:37:33 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c51ae794-0629-3a9f-a947-44454aa94b53 | -8.527 | -45.283401 | 2024-10-14 00:37:33 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 611f21f0-b74c-36d2-80eb-62875755912d | -9.0877 | -47.9198 | 2024-10-14 00:37:34 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fc0c85fa-e956-3c3f-95fa-e81442245ae6 | -9.0894 | -47.9277 | 2024-10-14 00:37:34 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4d3b4ae2-fdec-33e0-a4c1-6a850277b50b | -9.0912 | -47.9356 | 2024-10-14 00:37:34 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 65180c31-9e3c-3f87-ae05-96d3c577cbd3 | -9.0929 | -47.943501 | 2024-10-14 00:37:34 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7aab3d3d-c934-30f5-a871-9220ad52599f | -8.7186 | -46.630501 | 2024-10-14 00:37:35 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aceb2921-6764-34e9-bc90-79d32b89fdf7 | -8.972 | -47.675098 | 2024-10-14 00:37:35 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a440a07a-83c4-3f0d-a3d7-f16f8912d9a9 | -8.9737 | -47.6828 | 2024-10-14 00:37:35 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 00b8f8ba-2acc-323d-900a-ddd644bde404 | -8.9758 | -47.738998 | 2024-10-14 00:37:35 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bb1b6f62-41d2-37bb-86ef-66157e6c9318 | -8.9776 | -47.746799 | 2024-10-14 00:37:35 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 08966bfb-e033-3336-9af1-28c69d70b7e3 | -8.9793 | -47.754501 | 2024-10-14 00:37:35 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a5e62ffa-32b4-3166-9306-ac8f7a835072 | -8.7072 | -46.625599 | 2024-10-14 00:37:35 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b3224267-b6d9-3c2f-9c6e-79e2f5eb4484 | -8.7088 | -46.632702 | 2024-10-14 00:37:35 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c5da4f27-6bf4-3dfb-ac2c-502583e5d5d4 | -8.7104 | -46.639801 | 2024-10-14 00:37:35 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 787d699d-2767-37ad-b7a1-cbdddb83331d | -8.7006 | -46.641998 | 2024-10-14 00:37:35 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4cd2dfda-2fe9-3967-a045-f81b8031d871 | -7.2876 | -40.406101 | 2024-10-14 00:37:35 | METOP-C | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 97ee79bb-4530-3ee9-882f-9e0fa60691d5 | -8.9204 | -47.906799 | 2024-10-14 00:37:36 | METOP-C | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c639d7c6-a896-38b8-a084-ab3ae906ffe4 | -8.9089 | -47.9011 | 2024-10-14 00:37:36 | METOP-C | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b92313e0-18f5-3576-a8fc-3176fe9c7f41 | -8.9106 | -47.909 | 2024-10-14 00:37:36 | METOP-C | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bacfd563-97d5-3eb8-941c-685620611928 | -8.9124 | -47.916901 | 2024-10-14 00:37:36 | METOP-C | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 28596748-514d-3e13-a8db-cc1ce21b6499 | -8.9008 | -47.911098 | 2024-10-14 00:37:37 | METOP-C | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 91150396-80be-3901-b008-f68aa0dd1a93 | -8.7953 | -47.8521 | 2024-10-14 00:37:38 | METOP-C | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 51ce6b2d-63cc-3e5d-a26c-601cb3cf2056 | -8.797 | -47.859901 | 2024-10-14 00:37:38 | METOP-C | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b4cab393-9386-33f0-9633-c4db5dbb02f5 | -9.4809 | -50.972698 | 2024-10-14 00:37:38 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b51091bb-e8fc-3584-b62b-ba9596c5143a | -7.8354 | -43.9827 | 2024-10-14 00:37:39 | METOP-C | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 573cd565-4891-3c4a-bdcb-a4b5731a7eba | -7.8371 | -43.989899 | 2024-10-14 00:37:39 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e5ad520e-cf1d-3ee1-8f99-13043be6f11a | -7.8388 | -43.997101 | 2024-10-14 00:37:39 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b571f938-d760-38cc-bbb6-03206b5ef722 | -9.7182 | -52.839901 | 2024-10-14 00:37:40 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README9.md)
