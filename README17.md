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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a698a90e-09c7-3f5f-a735-300cc6cd3259 | -10.81789 | -50.95175 | 2026-08-24 04:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ce397c92-4d7b-3162-9d68-b3afc9f4f444 | -10.70108 | -47.75523 | 2026-08-24 04:25:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 33217208-289c-3da6-8e8b-52c30c7c2c29 | -10.73549 | -47.97997 | 2026-08-24 04:25:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b2d7f985-b340-3f4a-aae8-e757bd41a374 | -10.82408 | -50.56535 | 2026-08-24 04:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4ee6593e-7004-3f00-a5ed-e7cea86d4c41 | -6.62499 | -53.35137 | 2026-08-24 04:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9d261205-fa8c-31da-b071-a9491cd7d9c0 | -6.18206 | -53.5319 | 2026-08-24 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1032b9a0-7907-359a-8729-7e4a542b4892 | -6.19428 | -53.52758 | 2026-08-24 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 26416fec-16f9-3be4-99e7-7f3677090b51 | -7.26625 | -49.89377 | 2026-08-24 04:25:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b67c06ab-ef95-3df3-9cd6-2d2db62081cf | -6.9501 | -42.69291 | 2026-08-24 04:25:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f9958950-5679-37c1-9c9a-3436d1e68693 | -10.45785 | -49.964 | 2026-08-24 04:25:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ec205d97-15f7-3b45-af00-c55f31fdc56c | -7.38028 | -45.82265 | 2026-08-24 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c5c342df-2ae6-3167-ac3b-aad41daa10b4 | -6.94406 | -42.69574 | 2026-08-24 04:25:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7449ec66-9a4d-3263-a1c5-6fdc4c304184 | -7.35838 | -45.80313 | 2026-08-24 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| be5de424-582b-3eea-ad85-7717a5fab430 | -7.16204 | -42.76535 | 2026-08-24 04:25:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 87b85381-8e0d-3c0f-882c-a6b27d922572 | -6.22708 | -55.62288 | 2026-08-24 04:25:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 083fa987-d177-3d8f-9475-e3e186794b76 | -11.63262 | -50.53586 | 2026-08-24 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0e3148bf-234a-3d32-8e74-2e842a18c3fe | -6.21583 | -55.92472 | 2026-08-24 04:25:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d4107486-c5d4-3fb6-804a-2980e7863787 | -10.80973 | -50.94552 | 2026-08-24 04:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c870d1d0-5975-3329-bd52-11de99243aa6 | -9.37191 | -45.41658 | 2026-08-24 04:25:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 13b3296a-cb46-3b3b-9164-af50cbd6e0ff | -8.09771 | -47.47675 | 2026-08-24 04:25:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e2a999b8-fd3d-3eb8-af54-e52b917805ab | -8.54773 | -55.28963 | 2026-08-24 04:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e53ea1a-4b38-3385-a10f-56443d58e3db | -8.8104 | -46.60811 | 2026-08-24 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2a1d626e-a7ae-3af3-9bdb-4ae875e94ad1 | -7.9746 | -45.26271 | 2026-08-24 04:25:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 4c233535-00ed-3f5c-8dfb-17d91b9d56c3 | -7.48267 | -45.12785 | 2026-08-24 04:25:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f6a428ed-e8bc-32e1-8292-abc5be0fef1d | -7.15263 | -42.78181 | 2026-08-24 04:25:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e6744646-ba9b-39e0-8a72-caa1704f1b07 | -8.95443 | -50.75484 | 2026-08-24 04:25:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| aa217035-bd35-3022-8d15-38a660ab0577 | -7.24968 | -49.86904 | 2026-08-24 04:25:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 759849af-ebc8-368e-8995-bd2124fac7bf | -6.19432 | -53.52998 | 2026-08-24 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f292f57-18c9-327e-925f-77e3673338fd | -9.30563 | -40.22254 | 2026-08-24 04:25:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4e75a303-43cb-36c8-bdef-faffb5f5a26d | -7.89632 | -46.32774 | 2026-08-24 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 88d29308-dc00-345b-b01f-66bc5c993d20 | -7.35425 | -45.80642 | 2026-08-24 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 124e9731-f61f-3490-bc9d-9d7821d09f25 | -12.12995 | -43.40041 | 2026-08-24 04:25:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c72ef3f6-9ecd-30d1-a38c-3317f4c73957 | -7.4889 | -45.1325 | 2026-08-24 04:25:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ea1bad43-e03b-3aa0-9b78-d7bd85819988 | -7.15765 | -42.79336 | 2026-08-24 04:25:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 77c7da91-f381-3b33-9494-2c94c0a9264a | -7.1493 | -42.78128 | 2026-08-24 04:25:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5cbca200-15e6-3a03-b0a0-6f1cc4e9c326 | -8.57602 | -49.97839 | 2026-08-24 04:25:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ea83160d-c16f-36f9-8824-f44cb1533030 | -10.81056 | -50.94099 | 2026-08-24 04:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5451d301-3675-3615-b4f1-3d57519b693b | -5.77839 | -50.18894 | 2026-08-24 04:25:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21fb3b03-0bf6-31be-9306-e6d61ff8c9cc | -7.78769 | -56.28589 | 2026-08-24 04:25:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 08d9c762-9939-3ed4-ada9-11a98bcea850 | -6.59177 | -52.45502 | 2026-08-24 04:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5ef0118a-6d28-3a53-b5d0-792091d899d8 | -7.89985 | -46.32842 | 2026-08-24 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ec6818d6-1d8b-32b1-b059-b6cc8d25a3d0 | -8.10748 | -47.48779 | 2026-08-24 04:25:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cc2ee3da-586a-3a82-82ec-47e1792b97cb | -6.22254 | -55.92582 | 2026-08-24 04:25:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 93f3034f-5e8f-31a0-a982-06c74f7276ef | -9.72451 | -45.99626 | 2026-08-24 04:25:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3b89eba3-a7a9-323b-9df2-5a072defdbbd | -12.41247 | -42.90429 | 2026-08-24 04:25:00 | NPP-375D | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3b844ddc-4113-3d1b-a30b-75959b1c8ab8 | -11.78976 | -47.26611 | 2026-08-24 04:25:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c5052a19-33da-3aca-afd2-c069b34a2784 | -9.67869 | -47.89443 | 2026-08-24 04:25:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f02c8477-f7c2-3507-a961-619a72e619e3 | -7.19088 | -42.7556 | 2026-08-24 04:25:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a46a4f7c-8c78-3fe1-a00a-bf625f73667d | -8.31567 | -47.58418 | 2026-08-24 04:25:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 024ff3bc-0bb7-36bf-8f45-f3435fa319e4 | -7.68826 | -50.74509 | 2026-08-24 04:25:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 7249db04-b371-3ade-bad4-1be75bee7cbe | -7.26869 | -49.9188 | 2026-08-24 04:25:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 226bde57-01a7-3cae-b35d-3c984296f0cd | -11.1465 | -46.17399 | 2026-08-24 04:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df16de76-256a-3186-af30-ffe3d58313ba | -7.1515 | -43.09234 | 2026-08-24 04:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6843c527-903f-3e97-baa9-ec3a811a0871 | -6.70407 | -52.088 | 2026-08-24 04:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef8a0fb9-cfad-305a-afe5-dd35209dc225 | -5.9153 | -52.13835 | 2026-08-24 04:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 067692f3-1881-39e0-821b-10690693ccea | -6.33241 | -54.75996 | 2026-08-24 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc74ee51-b189-318e-9c80-bb5b770b58e5 | -6.33971 | -55.8703 | 2026-08-24 04:25:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2f9f4af3-ceb7-3f83-8e8c-734977a95589 | -12.21218 | -43.16726 | 2026-08-24 04:25:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8ffb45ed-ab1a-3fe2-9afd-89165594ed17 | -8.11049 | -47.49301 | 2026-08-24 04:25:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5207da5f-9c7a-384c-ba11-23f790575468 | -7.37234 | -45.80541 | 2026-08-24 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| aae4635a-dcb7-3b9a-a30b-ce695e7261b3 | -9.05911 | -50.77245 | 2026-08-24 04:25:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dd0acc6d-9096-329d-a7e8-676d106722ff | -11.5819 | -46.95436 | 2026-08-24 04:25:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| da53c2bc-67a5-36fb-9040-32163f0d3fcc | -6.41207 | -48.58522 | 2026-08-24 04:25:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e9e0b2ad-0cbf-3720-a7c1-86bbf610bf74 | -6.75382 | -45.25086 | 2026-08-24 04:25:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 251442be-0e8f-3cc8-bb2c-4826412ae1c1 | -6.94677 | -42.69238 | 2026-08-24 04:25:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8b88be85-96b6-351f-a094-00129179249f | -12.25499 | -43.1366 | 2026-08-24 04:25:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 01a110d6-1b63-3b17-b585-fe0e93f75555 | -5.63213 | -48.42048 | 2026-08-24 04:25:00 | NPP-375D | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5da92aba-0b6a-3112-b790-5da37966fd90 | -9.71672 | -46.02217 | 2026-08-24 04:25:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 97e78fc5-2315-3bbb-be3a-5b69d2f56019 | -12.10902 | -44.96767 | 2026-08-24 04:25:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c44d2f9a-3be7-39b5-ad2e-d76e4cf3cef4 | -6.78509 | -42.77753 | 2026-08-24 04:25:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 59a8c853-6984-39a4-b755-0ee64ee5581c | -10.04213 | -46.43745 | 2026-08-24 04:25:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d88d04c9-3344-3aa8-836e-cad22b963874 | -6.80492 | -42.67331 | 2026-08-24 04:25:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 75c28b23-ea7e-3558-9cf5-df1e06e632ef | -9.67647 | -55.09169 | 2026-08-24 04:25:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8012d03a-10dd-3d2a-b72a-a3fe6dfe4498 | -7.15542 | -42.78584 | 2026-08-24 04:25:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 63e5ef40-4c9f-3159-8ba9-edaca34d2ab6 | -5.47244 | -44.41635 | 2026-08-24 04:25:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cca73ea6-f2fa-3cee-a9da-41f28ab9a36e | -7.39664 | -45.98897 | 2026-08-24 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 31370004-b100-31a9-9f2f-e2dba8a4b452 | -7.1792 | -42.74298 | 2026-08-24 04:25:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f11bf0c1-a24e-3336-b073-6b665d3b6281 | -5.06705 | -49.37429 | 2026-08-24 04:25:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 33824f3e-ad83-3867-b936-9951c2ac436d | -8.5764 | -55.28348 | 2026-08-24 04:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a63e1518-181c-3a42-b1f4-9b8f08ebd041 | -5.68564 | -53.74627 | 2026-08-24 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f48d9262-a4c2-3a21-9264-7580cc243352 | -6.97353 | -43.7476 | 2026-08-24 04:25:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 042b42d7-9176-3cd3-a1c1-1a58f5cc6dd1 | -7.28577 | -45.37024 | 2026-08-24 04:25:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 22712deb-4ac6-3b50-818f-bcd5eccfa35c | -4.98771 | -47.48057 | 2026-08-24 04:25:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fea8f793-7be1-310f-a784-378b5964fa02 | -7.28233 | -45.36967 | 2026-08-24 04:25:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fc19774f-668a-3c59-bdb7-ceeae6fa7077 | -8.98182 | -46.01003 | 2026-08-24 04:25:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0a9667e1-13f0-3937-a4f8-b13609f4c7e4 | -7.29812 | -43.00196 | 2026-08-24 04:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| cdbb50a1-f856-3c87-a265-b6b30904fd80 | -9.05487 | -50.77446 | 2026-08-24 04:25:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e757b79c-edd2-35fe-9893-b221dca85101 | -7.36536 | -45.80427 | 2026-08-24 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9463fc2d-f53c-3349-9f14-b923b1f6420d | -7.24458 | -49.8721 | 2026-08-24 04:25:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| a18a8a17-a2ba-38d3-91cf-2ba498890771 | -7.26792 | -49.92335 | 2026-08-24 04:25:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 5a6c2d7f-97e5-3e55-b36b-2be7cb312c5f | -9.67748 | -55.09451 | 2026-08-24 04:25:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 88f39c75-c64a-3634-afdb-c191c0b32dbb | -4.99929 | -56.13867 | 2026-08-24 04:25:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 753c26f2-f854-3295-a69c-b058a86e3536 | -7.25986 | -49.91677 | 2026-08-24 04:25:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 912d52b6-0c80-3bac-8bfb-025334c50285 | -7.7555 | -46.15484 | 2026-08-24 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ac9f3d2e-d6a9-3f8a-b400-cf27b016c986 | -7.3733 | -45.82149 | 2026-08-24 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 79091899-e819-3db4-a66f-389d09bd0cdb | -8.57729 | -55.27868 | 2026-08-24 04:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f37e05ce-4be1-35c5-890f-1d8a46e534e5 | -6.22814 | -55.61706 | 2026-08-24 04:25:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 003b5d1a-a666-35de-b07c-ae0a4b5bcb80 | -10.04342 | -46.42973 | 2026-08-24 04:25:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 32b85775-ee61-3c9d-a66b-2c3d39c480d6 | -5.77922 | -50.18405 | 2026-08-24 04:25:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 001396b5-4923-36df-b3b7-1d8693fb7c1c | -7.48868 | -44.91909 | 2026-08-24 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README18.md)
