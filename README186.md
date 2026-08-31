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

## Dados Diários - Página 186

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 740d0b14-c5eb-32fb-9546-3f7d27cd26bf | -4.1516 | -60.6878 | 2026-08-31 18:30:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 83.4 |
| f33951a4-b5c7-36e9-9079-be342b0d016f | -11.6247 | -50.1783 | 2026-08-31 18:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 93a8880d-caaa-3b4b-a0ec-416952cfb209 | 0.1914 | -60.4878 | 2026-08-31 18:30:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 48eb1f6a-b463-369c-aabd-a8e22eb1b506 | -3.6398 | -60.5656 | 2026-08-31 18:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 106.9 |
| 18f29c24-d64b-3381-a453-90acb4c89577 | -13.967 | -54.395 | 2026-08-31 18:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 5c5a8b44-0e3e-39c7-986d-36e52619189a | -8.9967 | -60.5916 | 2026-08-31 18:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 7a4aa746-ff6b-3521-a4fc-835363bebcfa | -5.9451 | -57.6906 | 2026-08-31 18:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 147.3 |
| 31620763-5c2f-30b2-ba97-8aaeacbcd04f | -10.3199 | -49.9996 | 2026-08-31 18:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 280.2 |
| 7fed9bc0-001b-366a-8c0a-d7fd10c5679f | -11.2482 | -45.1194 | 2026-08-31 18:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 92.0 |
| e82005c1-f6e7-3610-8100-ba4f75b8ebaf | -10.3202 | -49.9782 | 2026-08-31 18:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| b502c65d-af77-393a-b726-a060217d035e | -14.6338 | -53.5876 | 2026-08-31 18:30:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 42.2 |
| c1779cc0-03b0-3057-9749-6dcb0437eaf0 | -10.5719 | -57.495 | 2026-08-31 18:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 114.1 |
| cb4e5cd1-190f-31b6-97c0-b505b69a6006 | -4.9604 | -55.8424 | 2026-08-31 18:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 64208dcf-9018-3eed-bca5-b730de5295df | -9.153 | -59.5415 | 2026-08-31 18:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 137.7 |
| 599312b7-b01f-3ce9-8402-84f394d96803 | -12.1113 | -45.0163 | 2026-08-31 18:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 07bd4137-777b-3a56-a1e3-31b07720d819 | -6.8571 | -59.4179 | 2026-08-31 18:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 2b05f375-5433-309a-b743-451db34d8ad3 | -15.6142 | -56.3898 | 2026-08-31 18:30:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 84.9 |
| afd02349-3b75-3d71-871b-c4c6a689abf0 | -6.1294 | -57.6833 | 2026-08-31 18:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 96.4 |
| 258993a0-0e25-3210-91d2-03370a8d46ba | -7.6251 | -55.2987 | 2026-08-31 18:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 280.6 |
| 5d9ef6f7-d657-376e-899b-caf0c3ac9594 | -19.4706 | -57.5636 | 2026-08-31 18:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.1 |
| 0b171185-2217-357b-afec-18eb544b0cfb | -6.3875 | -54.7646 | 2026-08-31 18:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 139.9 |
| 38b9db2e-8512-35a2-850a-d9508b35ad97 | -6.8015 | -59.4586 | 2026-08-31 18:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 41aa08d7-eae1-329a-8104-2e404a742d4a | -14.4835 | -52.1938 | 2026-08-31 18:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 305d0888-c698-31c8-876e-fb2fa9b0fd25 | -6.7885 | -55.6436 | 2026-08-31 18:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 161.7 |
| ce3f2625-086c-3703-8e92-5349828bb4f7 | -15.6336 | -56.3876 | 2026-08-31 18:30:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 7de8ae37-6bc6-3df4-a097-563908c7f65c | -6.6541 | -59.4452 | 2026-08-31 18:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| f206c1d3-1bb5-3010-ac62-f1ccb2938a13 | -5.8692 | -52.0868 | 2026-08-31 18:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 2846fca9-e2f8-39b3-9c71-7d73603d8240 | -7.3453 | -72.9539 | 2026-08-31 18:30:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 64291e6f-f33d-3f3f-bcd6-4c2a58cb7912 | -12.9221 | -45.8582 | 2026-08-31 18:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 0a422d7f-e20c-3f0f-82ea-b07660edc362 | -7.4734 | -61.4037 | 2026-08-31 18:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 21dd64cc-4d6d-317f-85aa-8e638e249768 | -11.2506 | -53.9941 | 2026-08-31 18:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 54.1 |
| f2cf8679-6fc4-3fae-96c6-7913d8e3365e | -3.6216 | -60.547 | 2026-08-31 18:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 153.4 |
| 35fd9205-1ba3-3041-921d-aa00a9fbd5b2 | -10.3394 | -49.9547 | 2026-08-31 18:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 8a3d8c22-e85d-3228-97e8-37c16dda754e | -9.0245 | -65.3994 | 2026-08-31 18:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 5f07c466-2571-38b7-8789-8235058ab573 | -10.7407 | -54.0401 | 2026-08-31 18:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 266.3 |
| bc209aa4-465a-3f89-b468-e80fdf658acc | -3.6215 | -60.566 | 2026-08-31 18:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 271.6 |
| 2480e8e9-c4fd-3117-868c-a9a70c2fd5db | -5.2548 | -55.8907 | 2026-08-31 18:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| c8c1a875-8980-35e3-be55-2dd23f354d68 | -10.7271 | -50.6405 | 2026-08-31 18:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 115.9 |
| de96b9e4-7366-35ca-9332-c0032ba6ac69 | -15.8844 | -56.4819 | 2026-08-31 18:30:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 128.9 |
| e251cb10-1f32-3de8-8bcc-c8866bcc59f1 | -4.1699 | -60.6874 | 2026-08-31 18:30:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 344b57db-2ad3-3339-8ff1-d9a0221ada68 | -9.0058 | -65.4373 | 2026-08-31 18:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 106.6 |
| cba3416b-8109-31f4-9621-f036f56d2f52 | -3.1997 | -61.1799 | 2026-08-31 18:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| df633d1b-e75d-3be8-be4a-d5fa1ccab17a | -9.208 | -65.8044 | 2026-08-31 18:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 113.0 |
| 8eefbf3e-bb99-336a-9cc3-260900d05499 | -9.2098 | -59.4221 | 2026-08-31 18:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| b885ef77-e45e-3fdb-96ad-218670d19908 | -8.8705 | -66.7822 | 2026-08-31 18:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 244.9 |
| 896cbe03-89fc-368a-8416-49cdb88bac72 | -14.5627 | -52.077 | 2026-08-31 18:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 106.3 |
| b29d10fc-9013-3308-949f-9afa3cde24ac | -14.5623 | -52.0984 | 2026-08-31 18:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 214.0 |
| d8aba13a-6dbe-3b6d-94e9-3043fc928360 | -11.9378 | -45.0656 | 2026-08-31 18:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 485758b5-f1c5-3be6-9fa8-02218454bbdc | -11.2103 | -45.1017 | 2026-08-31 18:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 119.6 |
| c73f4f71-074c-3384-9965-18fae94e0283 | -10.358 | -49.9742 | 2026-08-31 18:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 78797899-765a-3af9-a395-e52591cb774a | -8.4341 | -70.7166 | 2026-08-31 18:30:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 06783a63-892f-3f56-8051-1acc46e9e06c | -3.9708 | -60.0067 | 2026-08-31 18:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 7b2f5ac9-f988-30f0-8549-636895ce4334 | -9.2277 | -51.5847 | 2026-08-31 18:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 85a7ae84-8f24-3303-9bd8-1d7edda731f0 | -11.7973 | -47.6672 | 2026-08-31 18:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 100.8 |
| fe491ca3-c7e8-39f3-a680-d24708080562 | -3.3504 | -59.4274 | 2026-08-31 18:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 11a08fe7-5d80-3dc1-9e9f-6f6644d71bb3 | -7.4401 | -60.7567 | 2026-08-31 18:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 39.6 |
| de79e564-a396-39a2-976f-37556feb3161 | -9.8927 | -60.2752 | 2026-08-31 18:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 750c5ab5-88b3-3e09-a97f-2a39bfa6cc2e | -2.6559 | -59.3631 | 2026-08-31 18:30:00 | GOES-19 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 5f996fd7-c5fc-3b8d-86a9-869ee146b2dd | -3.9707 | -60.0258 | 2026-08-31 18:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 52.6 |
| fe1af0eb-69f3-363f-9dec-6f857867dc16 | -12.9589 | -45.944 | 2026-08-31 18:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 422860d3-e627-35ba-a5cd-b91616a57320 | -11.2478 | -45.1425 | 2026-08-31 18:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 913ce0a3-b755-3ebb-b7c2-3b476970eb11 | -9.1709 | -59.6374 | 2026-08-31 18:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 51c926ef-028a-3159-a4c5-5aece3ac3a91 | -6.8193 | -59.5734 | 2026-08-31 18:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.5 |
| e23bd3c4-db66-3d0e-b0f1-1050b90d3edb | -10.8043 | -50.5259 | 2026-08-31 18:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 262.4 |
| 95717046-0516-3b74-8905-bdfc3c2b58d6 | -9.694 | -65.0958 | 2026-08-31 18:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 9b59e5dc-570a-3803-84a3-500bc1563ae0 | -9.0059 | -65.4186 | 2026-08-31 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 3e7f51ce-4115-3339-892c-e7b70b5b96e0 | -11.5279 | -45.5162 | 2026-08-31 18:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 177.5 |
| 0447231a-63af-3489-bafb-59381c507bd9 | -9.1709 | -59.6374 | 2026-08-31 18:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 06d058b2-1fb1-3420-9876-d444aae2f6d9 | -6.6541 | -59.4452 | 2026-08-31 18:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| a27801fe-d903-3d3e-b842-cfe66e9a2d96 | -8.2605 | -62.758 | 2026-08-31 18:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 319170aa-a87e-3c0d-8b39-006be8581416 | -6.1183 | -53.5472 | 2026-08-31 18:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| eaee4952-f22e-3b4a-bff8-4e1f93711ada | -8.9664 | -62.4076 | 2026-08-31 18:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 40.7 |
| b1465328-f1a9-3077-ab9f-dc14d6fdd2e3 | -7.5656 | -61.4191 | 2026-08-31 18:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 71603439-e933-3837-bbf7-0b437eddc9f2 | -10.5906 | -57.4936 | 2026-08-31 18:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 48.7 |
| b4c63057-3361-3d55-b7df-db4a00fdedc8 | -15.6336 | -56.3876 | 2026-08-31 18:40:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 118.4 |
| f2f06f92-ca06-3b55-b128-4883b91b227f | -8.3601 | -70.8641 | 2026-08-31 18:40:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 07833a29-fb6c-3c84-9df5-95765dbb64da | -10.8215 | -50.6519 | 2026-08-31 18:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 8991c5e7-23cb-39a1-8488-365a2d1ff2c9 | -5.8537 | -57.5576 | 2026-08-31 18:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 72493b53-824e-37ba-8934-0a9533ed4afb | -8.9295 | -62.3712 | 2026-08-31 18:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 43.9 |
| a812d18d-6430-37ab-8fdd-c8322699b50d | -3.6847 | -64.6138 | 2026-08-31 18:40:00 | GOES-19 | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 5d552f8f-4518-3e46-ba39-f98992cd8cc0 | -3.4002 | -61.3276 | 2026-08-31 18:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 5324c170-c63d-3ae6-91d8-daaabb4d9b9e | -11.5275 | -45.5392 | 2026-08-31 18:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 12cf3923-605b-393c-8d71-25d7a8f9c63d | -16.0157 | -54.3958 | 2026-08-31 18:40:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 848d1837-dced-3521-a93f-a3214c5aeeae | -3.1449 | -61.1808 | 2026-08-31 18:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 100.4 |
| dbc3480b-ba8b-38e0-bc1c-0e616cc4a76d | -10.3199 | -49.9996 | 2026-08-31 18:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 111.2 |
| c8464098-f9a6-3c2f-b1ce-b14d73fc206d | -7.6066 | -55.2998 | 2026-08-31 18:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 789e2b5b-c895-3a09-ba62-10279bd00909 | -4.3138 | -49.1012 | 2026-08-31 18:40:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| b7cdeacc-1114-3963-92b9-fe5d8fa1c412 | -8.5363 | -67.1617 | 2026-08-31 18:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 41.6 |
| f99af9ed-95e5-3518-ac70-3525d32b6be7 | -3.6398 | -60.5656 | 2026-08-31 18:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 133.2 |
| 6d0fb196-0957-3bc2-a2c3-0abaa0d271ad | -14.2599 | -52.8782 | 2026-08-31 18:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 90.4 |
| c15bd2de-fbb6-3ac7-aabb-98834cba5c20 | -4.1515 | -60.7068 | 2026-08-31 18:40:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 102.8 |
| 484eae22-d92d-3980-87c6-acae45080388 | -2.7303 | -47.0644 | 2026-08-31 18:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 5ea37eba-bb12-361c-a25f-94ea7ba3ad64 | -5.9451 | -57.6906 | 2026-08-31 18:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 114.0 |
| a7cd6fbf-fa99-3175-b64d-b7ed294f2143 | -14.5868 | -54.1153 | 2026-08-31 18:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 63c395a9-058d-3e17-831e-7da07ee7326a | -15.2275 | -56.3716 | 2026-08-31 18:40:00 | GOES-19 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 142f3857-dcf8-3e83-a768-91bbbb0daebd | -3.6216 | -60.547 | 2026-08-31 18:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 152.6 |
| 75a9b4b3-6101-3db7-bbec-ea87023173c0 | -7.3453 | -72.9539 | 2026-08-31 18:40:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 98071f4f-673c-3ef9-a011-1922fa2d48b7 | -9.971 | -53.9214 | 2026-08-31 18:40:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 99.9 |
| d6a34c69-9c2a-3057-ae25-2a5f5dfa224c | -10.5719 | -57.495 | 2026-08-31 18:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 113.1 |
| 9f096ad9-0508-3d9e-b3c9-c759b239ea8d | -11.3236 | -45.1778 | 2026-08-31 18:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 63.3 |


[Clique aqui para ver as próximas entradas](README187.md)
