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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dc36bd45-3248-381e-a370-177401d49d66 | -12.075 | -50.5974 | 2026-08-23 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 327a65c8-192a-3af5-abeb-dcd07e780003 | -10.4905 | -49.9604 | 2026-08-23 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 2c12ec57-e08a-35b5-9d30-859c235c3bf9 | -11.9872 | -45.5187 | 2026-08-23 13:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 2d39067c-fab7-309a-bd02-e9fc8efb7458 | -6.8992 | -55.6977 | 2026-08-23 13:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 93.1 |
| d383e6ab-34fe-3d2e-9887-5ad807f85556 | -16.0509 | -50.4363 | 2026-08-23 13:50:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 9627c025-f814-30ae-8056-949558dbe90d | -8.5404 | -54.8398 | 2026-08-23 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 2894e462-5045-38d9-b9a0-f3d18e21d097 | -6.1285 | -57.8393 | 2026-08-23 13:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 143.4 |
| 0b28c060-7f9b-3e89-923f-84341a3b426a | -14.3168 | -51.7901 | 2026-08-23 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 139669c3-1b86-39e2-b834-7f4b0c5ca7df | -11.5804 | -46.9369 | 2026-08-23 13:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 68120f59-13f9-3b0b-98c3-b4bae81bf647 | -14.3547 | -51.8278 | 2026-08-23 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 57.0 |
| a6bc3683-5dcd-3233-b59f-d14fefb8b021 | -14.3543 | -51.8491 | 2026-08-23 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 19a36d03-21a1-3204-b3f9-bec853c26bc1 | -12.075 | -50.5974 | 2026-08-23 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| c56bbc3a-e729-3d9a-ace6-87ab4c8a7418 | -10.8358 | -50.9903 | 2026-08-23 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 4df23405-4229-3010-85f5-b297e884e2f4 | -11.638 | -50.5625 | 2026-08-23 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 1a07c5d7-f71c-34cb-b632-fa2e223ff8ff | -12.0559 | -50.5996 | 2026-08-23 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 1cae5ff2-b568-3775-96ee-166f2d5784ab | -8.56 | -54.7377 | 2026-08-23 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| ad2c5176-f0bb-3904-b484-8e844069664d | -12.2999 | -43.1781 | 2026-08-23 13:50:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 99.3 |
| ebea0e20-4bef-34b7-b89c-9300ff70ef9b | -16.0706 | -50.4332 | 2026-08-23 13:50:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 0a0df164-9584-3ed4-8d47-cd5f8d5311ef | -11.85 | -51.6648 | 2026-08-23 13:50:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 282.2 |
| 7dec8387-caab-3c98-96f9-de04f5b2ff5f | -14.2971 | -51.8141 | 2026-08-23 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 54.3 |
| ffc52fb4-8fae-3834-b8ea-58721caf0e6b | -11.9876 | -45.4957 | 2026-08-23 13:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 91.6 |
| e23e79b7-bee6-36de-ac59-fb27792c04a2 | -10.8361 | -50.9691 | 2026-08-23 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 103.3 |
| f411af12-dece-3859-a7cd-9e062135f6ce | -10.3902 | -50.3984 | 2026-08-23 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 149.3 |
| 02e3cd72-918e-3922-977b-43baf99c3662 | -14.3737 | -51.8466 | 2026-08-23 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 75.5 |
| c5c9a169-6d71-326a-880c-8ee0c58ba492 | -9.1331 | -65.9746 | 2026-08-23 13:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 7438d182-c7e8-329f-9b33-c2d23fecde9e | -9.1332 | -65.9559 | 2026-08-23 13:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 198.6 |
| 2356e84e-2861-38c8-a811-245a7a5c12a7 | -11.8497 | -51.6859 | 2026-08-23 13:50:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 362.8 |
| ff5b8120-2eb0-3186-988c-b34438b3cd17 | -14.3941 | -51.7799 | 2026-08-23 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 73656289-377a-3b22-b53c-a0be7e09207e | -6.1286 | -57.8198 | 2026-08-23 13:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| cb6bf6eb-fb85-3591-bd3c-583a1d206f16 | -11.869 | -51.6627 | 2026-08-23 13:50:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 97.5 |
| caedfdfd-14db-3d12-9815-75ebced62c05 | -13.6806 | -51.8511 | 2026-08-23 13:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 84.1 |
| ccee9489-158e-3d5b-aebd-f6f957eb8c58 | -12.2613 | -43.1845 | 2026-08-23 13:50:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 112.1 |
| 35a1f420-b308-3a41-8e7c-45e26560fb4a | -13.5096 | -51.7451 | 2026-08-23 13:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 0be2d770-11b9-3cfd-a710-851478c1b90a | -6.7162 | -52.8824 | 2026-08-23 13:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 2364d24e-b692-31f7-bad8-8c1430b38dd7 | -10.8547 | -50.9884 | 2026-08-23 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 52c3e30d-5b61-3cd7-b04f-c4b22d10d50f | -14.374 | -51.8252 | 2026-08-23 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 53ad3612-0b77-3871-a9b7-67760687f911 | -9.1332 | -65.9559 | 2026-08-23 14:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 346.0 |
| bab9e7de-c894-34e1-99a7-d5392d073291 | -12.075 | -50.5974 | 2026-08-23 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 49f48a8a-2e72-33db-9cef-3d405fda8cc3 | -14.2971 | -51.8141 | 2026-08-23 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 71.1 |
| b2f38d8c-81c9-32fb-b6c8-7b9df4e6b13c | -14.3543 | -51.8491 | 2026-08-23 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 98.8 |
| fba3bd05-4592-30db-aa05-91059399a8f5 | -13.896 | -54.0092 | 2026-08-23 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 77935440-cc57-33a1-99c5-2f3fd29ac29d | -9.1331 | -65.9746 | 2026-08-23 14:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 103.3 |
| 9b737422-7ae6-3218-bf71-6cb5e34540d8 | -6.7162 | -52.8824 | 2026-08-23 14:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 49c0aeaf-b38e-3fb9-8b75-cb02c577be75 | -10.8174 | -50.9498 | 2026-08-23 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 89.0 |
| ca3ca46d-8f18-31e4-83a3-fe8005c1d308 | -6.716 | -52.9028 | 2026-08-23 14:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 954d9b45-0ca8-34ce-92b7-50d8a026dde5 | -16.0509 | -50.4363 | 2026-08-23 14:00:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 7d018243-28f2-347e-a695-e596f67c5df8 | -11.8497 | -51.6859 | 2026-08-23 14:00:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 295.0 |
| cc7dd0ca-94ec-3d31-bb4d-38eb11aed23f | -11.638 | -50.5625 | 2026-08-23 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 237fbfc3-de5a-3418-a92d-ec2693d0fb0f | -8.5788 | -54.7162 | 2026-08-23 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 311f9365-dcd4-387b-ad97-60f8111b1d19 | -13.5096 | -51.7451 | 2026-08-23 14:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 111.9 |
| cdc09397-a8d0-32d6-b533-e98369cb8a24 | -8.1577 | -46.7025 | 2026-08-23 14:00:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 704857fc-04ed-304f-9cbc-5275da8a5b2c | -13.6806 | -51.8511 | 2026-08-23 14:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 96cd96aa-05b3-3087-ac01-e56397e5f098 | -12.2613 | -43.1845 | 2026-08-23 14:00:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 116.4 |
| edd273de-64bc-316b-948e-997fe509bf9e | -10.7977 | -51.0155 | 2026-08-23 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 54.0 |
| e74f2767-5ea3-3b6e-baaf-3c3dd8294463 | -14.3365 | -51.7662 | 2026-08-23 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 3c8f01bf-0720-3817-9661-fbabc4e5f044 | -10.8358 | -50.9903 | 2026-08-23 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 94.1 |
| d2d1e9ac-da79-3655-b172-d47376f8e428 | -10.3902 | -50.3984 | 2026-08-23 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 149.0 |
| 27330d80-9e45-39f6-b75d-5aef504d586b | -10.8361 | -50.9691 | 2026-08-23 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 217.2 |
| d3e75908-948d-35cc-bdf5-4fad912fb65e | -10.7687 | -50.359 | 2026-08-23 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 4ff839dc-88b9-3987-8a7f-12adadf5edcf | -12.2999 | -43.1781 | 2026-08-23 14:00:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 111.2 |
| bf804fbf-0c0b-398a-bb99-3fbe15c053a1 | -6.1285 | -57.8393 | 2026-08-23 14:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 166.6 |
| c2b0ce3e-f374-3a23-9ed2-cfd25e4a5464 | -10.4905 | -49.9604 | 2026-08-23 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 889b3746-7590-32da-bc24-aeef332363b2 | -6.1286 | -57.8198 | 2026-08-23 14:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| fca17959-94d8-35ea-befd-41a1807ddee9 | -10.8364 | -50.9479 | 2026-08-23 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 162.9 |
| 76f18ae0-235b-3470-b1c1-9775a506abe4 | -16.0706 | -50.4332 | 2026-08-23 14:00:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 88.7 |
| fb3f50fa-b87b-3937-8025-f816087c6924 | -13.4904 | -51.7475 | 2026-08-23 14:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 378db864-4159-3d75-b81d-28685ad09000 | -11.85 | -51.6648 | 2026-08-23 14:00:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 152.9 |
| 4f573afa-b56f-3026-aa6f-fbcae9377c5a | -14.2572 | -53.0468 | 2026-08-23 14:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 5deb26d1-d929-35a0-972b-901182d7fbc0 | -6.8992 | -55.6977 | 2026-08-23 14:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| a9d295dc-c926-3b47-bbbf-dc1aa6ad35ab | -14.3168 | -51.7901 | 2026-08-23 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 61.8 |
| e8ab319f-1135-3600-9f65-6564ac6aa180 | -9.1517 | -65.9554 | 2026-08-23 14:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 81.2 |
| b0a734f6-aaee-3db5-a7bc-c4d0c765d02c | -14.3547 | -51.8278 | 2026-08-23 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 3a5d48b2-b569-3e2c-86b0-9427377df863 | -10.8547 | -50.9884 | 2026-08-23 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 138.7 |
| 2e853085-4fa3-3fe3-9d1f-60ad85500151 | -9.4339 | -51.6088 | 2026-08-23 14:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 2e2a8ff2-e225-3889-a889-7eabf3c5705e | -16.0706 | -50.4332 | 2026-08-23 14:10:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 7d607f7e-6783-3439-a8c7-77a928066ad3 | -8.5788 | -54.7162 | 2026-08-23 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| df6032f3-7982-3272-b3f7-c20750555907 | -9.1517 | -65.9554 | 2026-08-23 14:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 364c47ae-0968-3136-ab3e-5b1c99cbde32 | -12.075 | -50.5974 | 2026-08-23 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 80328b56-50ab-3481-a8f2-b0c736f93723 | -16.0514 | -50.4144 | 2026-08-23 14:10:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 5c51cb9a-1157-35ee-9264-619c6e644796 | -11.85 | -51.6648 | 2026-08-23 14:10:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 6d49316a-394f-35f2-8c6a-ae6edaaebc0d | -9.4995 | -60.5085 | 2026-08-23 14:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 58.7 |
| a8abf67b-bcb0-3ac6-8873-00714c40d0e7 | -14.3168 | -51.7901 | 2026-08-23 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 66.1 |
| e58c3171-ffad-3d1c-a305-24d4f3ea4c95 | -8.5175 | -55.324 | 2026-08-23 14:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 388da8cf-d22d-37aa-b502-9362083e3387 | -11.5613 | -46.9395 | 2026-08-23 14:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| c38206ef-0774-3203-a8b7-f6c874c69be8 | -9.1332 | -65.9559 | 2026-08-23 14:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 230.9 |
| fc6412b2-6abd-321d-be69-10d1916a135d | -10.4905 | -49.9604 | 2026-08-23 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 127.5 |
| 7d96f6af-120b-3a7c-8e87-a16f05a757f6 | -14.2971 | -51.8141 | 2026-08-23 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 57.7 |
| e01c5acc-faa4-3cdd-b175-8d62771eb766 | -10.3902 | -50.3984 | 2026-08-23 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 234.8 |
| 5e400111-55e0-3030-ab9e-31d812d50354 | -14.3558 | -51.7636 | 2026-08-23 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 11233743-22e5-3ca5-b08c-47f198937238 | -10.6928 | -47.7171 | 2026-08-23 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 231.1 |
| e225d225-f798-311b-8680-5bf699a58d8e | -14.3543 | -51.8491 | 2026-08-23 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 70.5 |
| f057c5d8-00c8-316b-888b-6d9f68376b52 | -10.4716 | -49.9624 | 2026-08-23 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 4872ef8d-acc8-3574-9a8f-62e61cf29f9b | -12.8362 | -48.4567 | 2026-08-23 14:10:00 | GOES-19 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 40d23762-c2f0-3e51-9c9b-7bd8f2614c4d | -11.638 | -50.5625 | 2026-08-23 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 7ed85bb5-dc48-3cd4-8cb2-2976586bd657 | -9.4996 | -60.4892 | 2026-08-23 14:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| cfa67f89-ca9a-3e10-a202-733b5f527188 | -6.7162 | -52.8824 | 2026-08-23 14:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 8291853b-032e-3598-b011-be69730afed1 | -14.3941 | -51.7799 | 2026-08-23 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 51.0 |
| a28b5b56-bf58-383a-9b57-af48f3b53dac | -10.9174 | -50.5565 | 2026-08-23 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 2faad857-2071-324d-9908-70fbf4cc5cde | -14.3164 | -51.8115 | 2026-08-23 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 1a0725e9-ac22-3d13-831a-12a68cb58186 | -8.579 | -54.696 | 2026-08-23 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |


[Clique aqui para ver as próximas entradas](README76.md)
