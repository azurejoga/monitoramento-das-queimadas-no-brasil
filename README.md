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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3782b7ed-3063-3d4e-a322-41474b06b32e | -7.0079 | -45.4383 | 2026-07-24 00:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 1267fc65-f347-3ca6-9990-92ff3e0b5672 | -13.4362 | -51.5416 | 2026-07-24 00:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 80.8 |
| fa3c35ff-3376-3090-b5bf-a631924c4f5b | -4.3774 | -47.7627 | 2026-07-24 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 93c77106-4361-3dc4-93ef-3c85f465cece | -13.4554 | -51.5392 | 2026-07-24 00:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 2de04060-b897-3564-b01c-24c57d61639b | -7.0079 | -45.4383 | 2026-07-24 00:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 16f3efa0-0808-3f37-ac8e-0ad772a9c80b | -13.4362 | -51.5416 | 2026-07-24 00:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 2ab7846e-8e00-3f3d-9e36-52b0ac005c42 | -13.4362 | -51.5416 | 2026-07-24 00:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 80f06355-f796-3fdc-9337-c98721549f30 | -21.3295 | -44.2239 | 2026-07-24 00:20:00 | GOES-19 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 56.5 |
| d6647d40-042c-3218-abb7-0206958a2677 | -7.0079 | -45.4383 | 2026-07-24 00:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| e1ac5f43-232e-3bc8-8cf7-961022ff23f1 | -13.4554 | -51.5392 | 2026-07-24 00:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 5287934c-d04e-3e7d-b5ad-41f59809df89 | -3.9934 | -43.284599 | 2026-07-24 00:22:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a40dcec9-547e-3889-ad05-8a1e815dc030 | -7.0085 | -45.435902 | 2026-07-24 00:22:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9f89b68a-2210-3f1a-83a1-ad408250d24c | -7.0101 | -45.4431 | 2026-07-24 00:22:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 05441a1e-76ae-30b7-8161-6264ae37359d | -4.0113 | -43.273102 | 2026-07-24 00:22:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1e92a3d1-4ac4-3c1a-8238-d2adf8be1d9e | -21.3316 | -44.220299 | 2026-07-24 00:22:00 | METOP-C | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 19eb95af-000d-30ec-8ef6-4d34dcc27ee5 | -6.2676 | -46.355099 | 2026-07-24 00:22:00 | METOP-C | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3b6a191d-9967-345f-8d42-a182ede88ef7 | -9.5189 | -47.128899 | 2026-07-24 00:22:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 941fd678-439e-3c79-b857-616b662ba7a7 | -14.3684 | -50.329102 | 2026-07-24 00:22:00 | METOP-C | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 163f35bd-a14b-3ebb-a3ff-425ccb358846 | -21.333401 | -44.229401 | 2026-07-24 00:22:00 | METOP-C | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f4ab6004-6aeb-3494-85ff-b2e02d32488c | -7.0069 | -45.428699 | 2026-07-24 00:22:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 444d5561-90b0-3811-8f4f-94c07af73971 | -4.013 | -43.280201 | 2026-07-24 00:22:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 42a96ff0-00c1-326b-b0f6-78f0abd38356 | -5.617 | -45.977798 | 2026-07-24 00:22:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b25980f2-32f9-33c3-aeae-8c0f0ee70702 | -13.4215 | -51.552502 | 2026-07-24 00:22:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2b6c08df-b8ec-35aa-a981-d0f09d7efe98 | -4.7743 | -41.799999 | 2026-07-24 00:22:00 | METOP-C | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6318325c-0291-31eb-80d9-2ea32f6baa8a | -4.0146 | -43.2873 | 2026-07-24 00:22:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c9c62a80-18ea-3fb1-9352-8f084eee83e0 | -7.0242 | -42.784199 | 2026-07-24 00:22:00 | METOP-C | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 953e06e9-b223-3e0b-a5fc-734dd1c00cb9 | -8.8304 | -47.074402 | 2026-07-24 00:22:00 | METOP-C | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b0cb596e-c1f0-300b-bc1b-77acc7ae9ce8 | -21.323601 | -44.231602 | 2026-07-24 00:22:00 | METOP-C | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8e1d4977-dbaa-3363-993f-5144e405721e | -3.5281 | -42.698399 | 2026-07-24 00:22:00 | METOP-C | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3e3a8fd9-9e81-3746-8a08-d7feb12d5906 | -7.0053 | -45.421501 | 2026-07-24 00:22:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 40536684-df35-3fac-9786-4dee6c87dd8d | -13.4371 | -51.5289 | 2026-07-24 00:22:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1e7667fa-012a-3d57-8434-7a45ea05bdde | -21.3218 | -44.2225 | 2026-07-24 00:22:00 | METOP-C | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| edac9fbf-9125-37e6-87ee-ba2c25471fbd | -17.587999 | -46.685699 | 2026-07-24 00:22:00 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d3e0f667-811d-393a-9ee2-23e02c932ce0 | -13.4177 | -51.5327 | 2026-07-24 00:22:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 58c54ea2-07cf-313a-b721-4e8bfe64f710 | -17.585899 | -46.674801 | 2026-07-24 00:22:00 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3dfd812a-70fb-3d3b-9b6f-73aab4f47c20 | -5.7525 | -43.264198 | 2026-07-24 00:22:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c919b2ee-ebf9-31e6-8117-62237ec171f5 | -4.7725 | -41.792198 | 2026-07-24 00:22:00 | METOP-C | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ab62edb4-bb55-361d-a19e-be868521b291 | -3.9917 | -43.277599 | 2026-07-24 00:22:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d210c00a-7e36-3ca1-98ba-d90fc91548f5 | -5.3248 | -43.557701 | 2026-07-24 00:22:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7df6ba2f-ceac-36ca-b37b-d760e7861f34 | -12.6571 | -48.1964 | 2026-07-24 00:22:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9678e0eb-ecd7-3ba6-83ac-ae42f095fe30 | -5.7426 | -43.266399 | 2026-07-24 00:22:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d0b7ab62-48d1-317d-9927-dfd6060fd15f | -21.2369 | -41.8559 | 2026-07-24 00:22:00 | METOP-C | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6d6dcf60-3b7b-3e5a-bcce-d7b8cc87feef | -5.7442 | -43.273399 | 2026-07-24 00:22:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4192a88c-9cd4-35aa-b8f1-9d6ba44e2d71 | -7.4335 | -46.882801 | 2026-07-24 00:22:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8cef806b-745d-3b1a-9888-0dd2f195651d | -9.517 | -47.119999 | 2026-07-24 00:22:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bc7c48ae-2444-316b-bcd5-5304d37e845b | -4.3703 | -47.757401 | 2026-07-24 00:22:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aff621f7-0102-3b24-8550-c1add2ba32fb | -3.5264 | -42.691002 | 2026-07-24 00:22:00 | METOP-C | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0d4bb611-5702-3a2c-b72a-d5c3f9076144 | -13.4409 | -51.548599 | 2026-07-24 00:22:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7120c239-e997-3073-9857-6a0c767b6e3d | -13.4274 | -51.5308 | 2026-07-24 00:22:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 75c326a8-f033-384d-bae3-cd149ac6b9c3 | -4.3722 | -47.765701 | 2026-07-24 00:22:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3bf18d21-1f19-39f8-86ab-37b6cf45cc1f | -6.2693 | -46.362701 | 2026-07-24 00:22:00 | METOP-C | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6ab938a9-d78e-3aad-bcf4-e5b1359052fb | -4.3741 | -47.774101 | 2026-07-24 00:22:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 519a242a-d0bb-386a-80c2-d7b46bb1f17d | -7.0226 | -42.777199 | 2026-07-24 00:22:00 | METOP-C | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| fec211b2-ddf8-3b1d-8444-73d4da3f86e9 | -21.238501 | -41.8634 | 2026-07-24 00:22:00 | METOP-C | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b9944b5b-3db2-32bb-aeef-0c55ace6826c | -13.4312 | -51.550499 | 2026-07-24 00:22:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2822b38d-ed02-3823-8da0-e8c7050835b8 | -3.995 | -43.291698 | 2026-07-24 00:22:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f90ef223-f580-3ebc-8341-541bfb984cbf | -7.0079 | -45.4383 | 2026-07-24 00:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| e9e91a29-e24b-3cf2-badb-0928345c0a62 | -13.4362 | -51.5416 | 2026-07-24 00:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 152.8 |
| eef2aaf8-19b3-3e5f-b40c-d8054574b159 | -13.4554 | -51.5392 | 2026-07-24 00:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 8839aec9-986e-3d03-a07c-006bb5a78deb | -13.4362 | -51.5416 | 2026-07-24 00:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 139.2 |
| f68c4db3-b769-3925-ae0f-7f3d7f6b0753 | -7.0079 | -45.4383 | 2026-07-24 00:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 91fd0fc3-0997-3faf-90cf-ca50dc79d1a2 | -13.4554 | -51.5392 | 2026-07-24 00:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 5423805b-b5d5-3a35-9ba4-998efd0c10ab | -7.0079 | -45.4383 | 2026-07-24 00:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| ddf23de8-4d2b-3a3d-ae04-ed7f70b5f645 | -13.4554 | -51.5392 | 2026-07-24 00:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 64.3 |
| f51b4d37-79b1-306b-8651-13395c159ef8 | -13.4362 | -51.5416 | 2026-07-24 00:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 80.2 |
| abecc1a3-a01a-3ba9-8ecc-8d85c402c8fd | -13.4362 | -51.5416 | 2026-07-24 01:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 129.2 |
| ac1ee981-b523-33a2-a66a-5aa0735d6f96 | -7.0079 | -45.4383 | 2026-07-24 01:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |
| ce66e3c5-0600-3c9a-b4c4-58e55115d6b1 | -13.4554 | -51.5392 | 2026-07-24 01:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 17a525f2-76ff-3abe-a440-66dc700cb756 | -7.0079 | -45.4383 | 2026-07-24 01:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 73.9 |
| e792c6db-7ccd-36f5-ac4b-c3f5bef4fd31 | -13.4362 | -51.5416 | 2026-07-24 01:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 668fe974-ab99-3835-85db-31c450dc4f11 | -13.4554 | -51.5392 | 2026-07-24 01:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 60.3 |
| cfe8f7a0-728d-35e9-a168-f5a2e5e769be | -13.6806 | -59.63998 | 2026-07-24 01:13:00 | TERRA_M-M | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 17.1 |
| e3f510f6-5a4e-349b-9ef0-0ce03c277323 | -13.67295 | -59.62888 | 2026-07-24 01:13:00 | TERRA_M-M | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 20.4 |
| d72d07fd-7583-3dd3-9f16-e4a1034738c7 | -9.16463 | -58.33642 | 2026-07-24 01:15:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 25.5 |
| af5112b1-b79b-3d98-b330-5343221a0277 | -10.02953 | -65.05341 | 2026-07-24 01:15:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 280cd233-554e-391c-b2af-7280142a99fb | -9.12909 | -61.06205 | 2026-07-24 01:15:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 45fa0f6a-c55c-354f-a958-cfb3ebe981a0 | -10.02056 | -65.05476 | 2026-07-24 01:15:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c43db6b3-4d35-38ab-8ad2-451a81530aea | -13.4362 | -51.5416 | 2026-07-24 01:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 99.1 |
| ac7decbb-8f67-3de4-95da-eee952a48fcc | -13.4362 | -51.5416 | 2026-07-24 01:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 54.0 |
| e17d69d5-3779-30bd-a6b8-a3688f528516 | -7.0079 | -45.4383 | 2026-07-24 01:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 458ccde7-61fc-3b04-86a0-78c0b4fbc53a | -7.0079 | -45.4383 | 2026-07-24 01:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 50ea66a9-5258-349e-8823-388e35797a3e | -13.4362 | -51.5416 | 2026-07-24 01:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 49.7 |
| f208865e-b752-39ef-96c0-73669131eb6d | -7.0079 | -45.4383 | 2026-07-24 02:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 61.1 |
| b95f5da8-020b-3b4f-9178-bd5a9a205d94 | -10.0119 | -65.0495 | 2026-07-24 02:02:00 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 12c7631a-e160-3103-adcd-ca44e040ccb0 | -7.0079 | -45.4383 | 2026-07-24 02:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 66.6 |
| d5e0e7da-9c01-3de3-85e6-8812eee3f0c8 | -2.90503 | -40.39488 | 2026-07-24 03:28:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 06bd2a45-9d6e-31db-9677-47eb93853c1a | -2.90446 | -40.39824 | 2026-07-24 03:28:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 3128060b-06b6-3e51-848e-038b0e420711 | -3.99416 | -43.28563 | 2026-07-24 03:30:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4dfcb9a1-34ad-3f4f-8f9a-85244e7020bb | -7.00874 | -45.43447 | 2026-07-24 03:30:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 96925fbd-74ef-37cd-a369-5faba2bd4914 | -6.48521 | -43.78767 | 2026-07-24 03:30:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| e36f078b-9ba6-3577-a3ab-09aab5d6b0b8 | -4.01228 | -43.27588 | 2026-07-24 03:30:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e78e8433-839f-3943-8828-91dabfc11051 | -4.01052 | -43.28624 | 2026-07-24 03:30:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d640df37-61db-3142-bd20-ee4342f25d71 | -4.77087 | -41.79502 | 2026-07-24 03:30:00 | NOAA-21 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 5312c7f6-34d0-3c79-9fb4-e57d8ece83da | -4.01141 | -43.281 | 2026-07-24 03:30:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bf21c6e2-d795-3089-ad72-e954d3139660 | -5.35925 | -43.1391 | 2026-07-24 03:30:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d2f6f60b-d29c-38c9-a36f-2b6059ec83eb | -4.01401 | -43.28386 | 2026-07-24 03:30:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 11e20a50-23f8-3804-81de-4cb7bdee3587 | -3.99325 | -43.29074 | 2026-07-24 03:30:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4ad888a3-0066-3cde-b1e0-4d713373fd2f | -7.00994 | -45.42805 | 2026-07-24 03:30:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 36fcec65-76c3-3928-9c0e-f696a4787832 | -7.01961 | -42.78446 | 2026-07-24 03:30:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cabfbc2f-bd17-354e-9828-7c3d6cdf9116 | -6.48761 | -43.78868 | 2026-07-24 03:30:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |


[Clique aqui para ver as próximas entradas](README2.md)
