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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 904d08d8-ff4a-3726-b19a-e62d43a650b0 | -12.2281 | -50.5578 | 2026-08-30 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 2979b313-f76d-37db-86f7-13b9163207c4 | -7.9907 | -46.5177 | 2026-08-30 15:00:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 150.9 |
| d17db77f-98b8-3379-a534-e9fc5ce66f58 | -11.2634 | -45.3471 | 2026-08-30 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 3314964f-3b04-3a9c-9d6a-98e39d54ea95 | -10.3394 | -49.9547 | 2026-08-30 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 5e56e6bf-8478-3e1a-8b49-a4f345cec958 | -7.566 | -61.343 | 2026-08-30 15:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 10ccb4da-4932-38b4-8e61-eedf7c80e7ea | -10.7405 | -54.0606 | 2026-08-30 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 9a166b27-b9a2-35db-b314-bab6f1d9b61e | -16.2729 | -42.59 | 2026-08-30 15:00:00 | GOES-19 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 36578309-3751-3629-8c16-c4d02082e8e3 | -15.228 | -57.6719 | 2026-08-30 15:00:00 | GOES-19 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 63406843-dfe4-3d2e-b04c-518dcf1ff5d7 | -12.9032 | -45.8382 | 2026-08-30 15:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 3d3999c2-8409-32ac-8ebc-fff4a9d2a6f5 | -8.5925 | -66.9564 | 2026-08-30 15:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 3d0dc661-a3ce-3270-bbcf-fbb540079b5b | -9.9284 | -60.4856 | 2026-08-30 15:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 109.1 |
| 005ab0e4-77fe-3cce-a2c7-695017705003 | -4.1698 | -60.7064 | 2026-08-30 15:00:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 0434746e-b7fa-304c-8799-85b1822cba6f | -11.3427 | -45.1751 | 2026-08-30 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 0f5a7dab-f5b9-313e-a95c-613a3030af0d | -9.9281 | -60.5242 | 2026-08-30 15:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 114.1 |
| 13378568-0349-3ae9-8436-3b209266155e | -7.1315 | -42.7472 | 2026-08-30 15:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 97.6 |
| 347e8e24-066f-338a-aaf1-abe57a179f29 | -14.2027 | -52.8432 | 2026-08-30 15:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 8828ae54-36ea-3052-9593-409ddc94754f | -13.2842 | -51.4541 | 2026-08-30 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 477b3894-4357-3fd6-b550-eaa576fa17cb | -11.1919 | -51.2496 | 2026-08-30 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 50.5 |
| e8369ac2-2100-3326-92c6-8d8c4446ebbf | -11.1995 | -55.1008 | 2026-08-30 15:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 7024047e-3be3-394b-ac92-abe74e1f2750 | -10.844 | -45.3356 | 2026-08-30 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 148.3 |
| 442d3fd0-4ae6-3eb5-8442-14cec1e187b9 | -13.8756 | -54.0945 | 2026-08-30 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 4285acc3-8c58-321d-924e-f420603509e6 | -14.4387 | -52.56 | 2026-08-30 15:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 7fb64172-37fe-3ad8-9c62-7a777b5f9989 | -6.861 | -41.6772 | 2026-08-30 15:00:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 646.8 |
| 0939fff3-e680-3897-9d22-360bfc4d755f | -9.8927 | -60.2752 | 2026-08-30 15:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 132.5 |
| 7171a204-cba2-37e7-9faf-d7a17ab26a68 | -7.5272 | -44.3413 | 2026-08-30 15:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 2cb42c10-f9b7-34e6-974a-d1a460fd843c | -9.0615 | -65.4169 | 2026-08-30 15:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 102.0 |
| 9fade0b6-34a8-3327-ae15-b0eefe1e95e1 | -9.1533 | -59.5027 | 2026-08-30 15:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.1 |
| e63c599e-a9a7-33c7-a4fc-4de54b3c6333 | -11.2317 | -53.9958 | 2026-08-30 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 148.4 |
| 84d2b87c-d5c0-3be5-9a1e-393d349f425b | -7.9169 | -61.3671 | 2026-08-30 15:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 44.5 |
| d2f20816-1959-3fce-bbb3-c7da6516b845 | -11.2314 | -54.0164 | 2026-08-30 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 233.8 |
| b4c932f2-2ea8-3760-af0b-c10f9e4b3159 | -10.7245 | -50.8321 | 2026-08-30 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 8aaa30c8-a016-3a93-9c4b-bae149f196d5 | -9.1662 | -60.2752 | 2026-08-30 15:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 744f78b9-6a86-3144-b946-f767dcdd69b0 | -11.2638 | -45.3241 | 2026-08-30 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 9576531b-edb0-3e46-85d7-52572735fac1 | -10.1348 | -45.7006 | 2026-08-30 15:00:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 130.1 |
| 1bfeb8ef-6bbe-3c0b-85ab-2c35fd1cad4b | -11.2294 | -45.099 | 2026-08-30 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 151.7 |
| aa890d2a-873f-3d23-919e-55faee33bbd9 | -9.0723 | -60.4148 | 2026-08-30 15:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 106.2 |
| 51b4a9fb-9fe8-37a3-bb63-881ba59a984f | -15.2283 | -57.6517 | 2026-08-30 15:00:00 | GOES-19 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 512d2874-401f-31a5-8559-1d54c675e539 | -11.1821 | -50.592 | 2026-08-30 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 2300f5c0-38c6-32dd-8430-28b2cb2510e6 | -11.2443 | -45.3497 | 2026-08-30 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 241.7 |
| 59170af5-6373-3149-9a9e-e3fa42766cf6 | -5.9819 | -57.6892 | 2026-08-30 15:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 0a544c49-528d-3d66-af05-7f5c068ec708 | -11.2485 | -45.0963 | 2026-08-30 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 9972ab85-1811-3dbd-90b1-2ff5a197c20b | -9.2262 | -65.8784 | 2026-08-30 15:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 171.7 |
| 35880d1f-936a-31b4-ac13-2d84cebcfe2d | -11.3619 | -45.1724 | 2026-08-30 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 159.3 |
| 2587fee0-c784-3f3a-8ecb-841ce923893e | -12.9027 | -45.8612 | 2026-08-30 15:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 143.8 |
| 66f776fc-d9e4-3639-a84e-fe88e8fe72e9 | -8.574 | -66.9569 | 2026-08-30 15:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 9516d614-e001-345c-971c-5577c56ee7a9 | -12.2086 | -50.5815 | 2026-08-30 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.0 |
| dc681e08-58ca-3870-b04f-03fdcf319207 | -10.7407 | -54.0401 | 2026-08-30 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 198.1 |
| fd50e505-c6ce-352b-9097-17532d9a30c8 | -9.0614 | -65.4355 | 2026-08-30 15:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.2 |
| cb814ca1-214e-31ed-965f-c997156ab94f | -5.9635 | -57.6899 | 2026-08-30 15:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| c6eb9f65-c3b4-31d9-82f9-d6a15cc43c94 | -15.4048 | -52.6437 | 2026-08-30 15:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 167.0 |
| 6104a124-cf2d-382f-b5fd-9cffa3f693f0 | -7.5845 | -61.3423 | 2026-08-30 15:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 69.3 |
| d915eadc-a1d4-30f9-9a11-8497bad83230 | -21.0376 | -57.8284 | 2026-08-30 15:00:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 62.4 |
| 0361178d-38c8-3fc0-8fca-f7ac37655488 | -6.4101 | -51.6634 | 2026-08-30 15:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 26df64ec-c15c-3392-99a5-238a2a06f7a8 | -14.1459 | -52.7871 | 2026-08-30 15:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 148.9 |
| 46019806-49dc-31bf-a267-7fdc9060410c | -13.8563 | -54.0967 | 2026-08-30 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 151.3 |
| ce968a7d-4fae-38e4-87f4-6b3e20169b88 | -9.9468 | -60.5232 | 2026-08-30 15:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 0e64cb6d-6ada-3b1c-bde9-7af9557c88ef | -10.7647 | -50.6579 | 2026-08-30 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 577b90b1-43a2-393e-aac1-af0d42d0a749 | -12.9216 | -45.8812 | 2026-08-30 15:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 214.5 |
| c454a168-a4c4-3f89-8bc9-b32bdcd48e45 | -3.4943 | -54.6567 | 2026-08-30 15:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 1aef71e7-93d9-3aae-bf85-225f012ef6bd | -9.0722 | -60.434 | 2026-08-30 15:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 657dc6f6-69e0-3ca8-bd7d-4b377aa69329 | -12.3811 | -48.1877 | 2026-08-30 15:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 695fa5da-fb8f-3764-9789-60aae5f57ac7 | -14.2092 | -45.3207 | 2026-08-30 15:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 129.2 |
| a779d49d-c1d8-3046-852b-e2b6746df2e5 | -10.8025 | -50.6539 | 2026-08-30 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 36bff73b-9e34-30a5-9dcc-8da4fd6ea50b | -3.913 | -60.9395 | 2026-08-30 15:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 63551b21-7106-32e1-8aa3-33391f637dbd | -12.9221 | -45.8582 | 2026-08-30 15:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 119.7 |
| dfee8dea-9761-3542-b7fd-523b8850e173 | -9.9282 | -60.5049 | 2026-08-30 15:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 356.1 |
| 20e162f5-57e1-3765-9af5-a94440ccd981 | -12.209 | -50.5601 | 2026-08-30 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.4 |
| c2c865bb-918b-300f-bb71-4161f7544a42 | -9.043 | -65.4175 | 2026-08-30 15:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 94961b80-0e84-327d-8222-2021ce8e4cff | -10.7451 | -50.7025 | 2026-08-30 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 49.0 |
| e2a20e06-54ab-38f3-ade2-0ff191837543 | -13.8557 | -54.1383 | 2026-08-30 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 65d8c397-bc97-37db-a38a-03d2078ba359 | -11.1634 | -50.5727 | 2026-08-30 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 2349adfa-6ecb-3ec1-b4ff-98825497c0c5 | -3.1998 | -61.161 | 2026-08-30 15:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 841fe04d-417a-3a77-89bd-6fbdfc8c7c39 | -12.0921 | -47.1812 | 2026-08-30 15:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 132.9 |
| 6b1a78d5-a877-35fc-a518-914b56b624c4 | -7.1121 | -42.7963 | 2026-08-30 15:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 99.9 |
| b007f28e-c207-3797-9320-8ce11c01d976 | -9.8925 | -60.2945 | 2026-08-30 15:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |
| ef55d47f-d2f9-3bc1-82a6-9c97705fc0ba | -5.4876 | -57.1416 | 2026-08-30 15:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 142.0 |
| d2a07a83-fe7f-3071-a519-1b6bee6133ea | -7.1312 | -42.7708 | 2026-08-30 15:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 204.4 |
| dec7d20c-3e4b-3e44-a016-e3c499104ea8 | -11.2446 | -45.3267 | 2026-08-30 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 7d2b603a-f19a-35f5-880a-06e20cc23dca | -13.3799 | -51.4634 | 2026-08-30 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 70.4 |
| b8c75f88-f163-31c2-be49-2276a9c6175c | -7.566 | -61.343 | 2026-08-30 15:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 77.9 |
| c7ac1520-24d1-338f-911a-e0823cdb88e6 | -9.0722 | -60.434 | 2026-08-30 15:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| c5953054-00e3-3052-adac-1b27decddc66 | -10.3202 | -49.9782 | 2026-08-30 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 56.5 |
| cb449e55-92e8-3566-99fe-c54fb5fc90cc | -9.1739 | -56.9754 | 2026-08-30 15:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 7c5c286b-143d-356d-a603-0a0d672fa019 | -12.0921 | -47.1812 | 2026-08-30 15:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 8764394f-e7c0-3cdb-b437-d5dfb70b635b | -21.0172 | -57.8313 | 2026-08-30 15:10:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 64.0 |
| 3a00f1ec-3810-35c3-b835-a2b2c3f0ddc5 | -9.9284 | -60.4856 | 2026-08-30 15:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 123.3 |
| 037ad78f-b848-37bf-a5cf-ad9b1dd10610 | -9.2262 | -65.8784 | 2026-08-30 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 300.6 |
| fce20a0f-d244-3761-97b7-8df18165974b | -5.9635 | -57.6899 | 2026-08-30 15:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| ad324ab8-f2b2-3783-8065-3b1a2bcd2f3c | -14.1456 | -52.8082 | 2026-08-30 15:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 147.4 |
| cbc01cba-ad4d-350a-abdd-176ea584afe1 | -21.0376 | -57.8284 | 2026-08-30 15:10:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 54.4 |
| 5a95686a-14db-36de-ad03-2225d2af0419 | -12.209 | -50.5601 | 2026-08-30 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 18b9b799-5d9b-3e7b-bfdc-33681477d5c0 | -14.7601 | -48.7467 | 2026-08-30 15:10:00 | GOES-19 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 48b1cfd4-647b-39f9-b050-3e1adef3ade1 | -7.9907 | -46.5177 | 2026-08-30 15:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 268.2 |
| 881314eb-92f7-3ad3-b4ad-5c64ae2cc510 | -7.9422 | -44.277 | 2026-08-30 15:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 273.7 |
| ec34aecc-571c-33fb-8b48-a67216fdf31c | -6.0 | -45.0889 | 2026-08-30 15:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 18c109ba-c369-3ef3-b844-ce95e549974d | -11.3622 | -45.1494 | 2026-08-30 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 140.6 |
| e9418afb-cf27-3e53-9d9e-0f0e02ec7cbc | -10.3394 | -49.9547 | 2026-08-30 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 2824f8a9-36b8-3f19-b8c0-a83e3c7ff018 | -10.7647 | -50.6579 | 2026-08-30 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 126.8 |
| 7b1776d3-5d23-3dea-be1d-448450875bc6 | -9.0723 | -60.4148 | 2026-08-30 15:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.3 |
| d609c675-58f6-365b-aaf8-0bcfb30388e1 | -13.323 | -51.428 | 2026-08-30 15:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 79.2 |


[Clique aqui para ver as próximas entradas](README90.md)
