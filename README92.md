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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6d6b455b-2031-3fd7-852b-56345c66b705 | -11.0247 | -49.6656 | 2026-08-30 15:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 9a7b5b16-b566-3dfe-9043-3f6bf4e22d5b | -13.3611 | -51.4445 | 2026-08-30 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 56.3 |
| d02ce256-65ae-3394-8867-e9b28172ea5c | -12.2274 | -50.6007 | 2026-08-30 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 52f42dd4-4f8a-3af5-a2dd-381e53399b6b | -7.9169 | -61.3671 | 2026-08-30 15:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 09836a44-140c-3140-96b9-9a8c4472152b | -12.2083 | -50.603 | 2026-08-30 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 3da0f354-8f7a-3e4e-b05e-b8d5cb5a2aef | -10.9183 | -50.4925 | 2026-08-30 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 35770bb1-4c18-3ae4-b7a3-2fffbe5a1bf8 | -11.2446 | -45.3267 | 2026-08-30 15:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 31d91b96-6a3a-3262-9795-c10e06453a9d | -8.3679 | -57.6737 | 2026-08-30 15:20:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 0cebc958-3eb8-3706-bad4-8e2b22ed225b | -9.0723 | -60.4148 | 2026-08-30 15:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 9865872e-6ca1-3337-9e83-94d2e11bb679 | -9.1661 | -60.2945 | 2026-08-30 15:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 2f3cda08-4e94-34c5-be46-6aeadb36133c | -12.2277 | -50.5792 | 2026-08-30 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 2e06fea5-5426-3046-ae8a-be6d053ac9d2 | -11.1536 | -45.0636 | 2026-08-30 15:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.8 |
| ff0ab97f-5833-33b4-86f3-d78fc3f761ad | -8.7969 | -62.8506 | 2026-08-30 15:20:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 48e41457-d5c8-3d55-aad2-63ea9a1cf278 | -10.8798 | -50.5392 | 2026-08-30 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 2e5e9c1c-f114-3863-9941-7cf8bf9d3ed2 | -7.603 | -61.3415 | 2026-08-30 15:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| b7eca0fc-1bb0-3f11-abb1-bdf6ea53cf63 | -10.8249 | -45.3382 | 2026-08-30 15:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 142.6 |
| a1deeedb-94b0-3cdc-87a9-f997842ef13f | -11.6396 | -50.4553 | 2026-08-30 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| c21e7adb-273c-320f-a949-045584a8b928 | -12.3424 | -50.5655 | 2026-08-30 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 548014ce-5de8-3017-89ea-de8d344afecf | -3.8947 | -60.9399 | 2026-08-30 15:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 8691a5d0-fcea-330a-b011-b5806e394bb7 | -9.2396 | -60.4256 | 2026-08-30 15:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 836424ad-1499-3bf8-a664-7d4c87d96767 | -5.871 | -57.7715 | 2026-08-30 15:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| ab508794-a828-3581-a3ce-e456a2e6ad9a | -11.1634 | -50.5727 | 2026-08-30 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 5decf2e3-c87e-3748-850f-7513a2d5a343 | -10.9556 | -50.5311 | 2026-08-30 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| d66d0470-97d6-3a11-b3ac-cb6fb163208f | -13.3422 | -51.4256 | 2026-08-30 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 80.6 |
| da1dc34a-9b6a-3317-b78f-434ad8193ad6 | -12.9032 | -45.8382 | 2026-08-30 15:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 8419d1e7-873d-3416-83a3-624c60bdfb93 | -11.2128 | -53.9976 | 2026-08-30 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 0e103516-c8fb-3264-b561-8c8c19249ab7 | -11.6586 | -50.4532 | 2026-08-30 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 2c91c4a0-bb81-3ebd-ba09-88f84ce45f1a | -11.0057 | -49.6677 | 2026-08-30 15:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| bd79163f-ee59-3923-90d9-a43331dd10a0 | -12.2281 | -50.5578 | 2026-08-30 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| c37304e3-034a-3c27-a61e-73a4d5d5a5ae | -11.1441 | -50.5961 | 2026-08-30 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 47.5 |
| c2bf42b1-e250-3b3b-8f97-eadef8311347 | -11.2314 | -54.0164 | 2026-08-30 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 166.2 |
| 5f972f57-4da2-3ba4-ac99-95903638df3c | -9.2262 | -65.8784 | 2026-08-30 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 369.5 |
| 456f6ede-d72c-3b8d-87b5-92b23ece25b2 | -4.9605 | -55.8226 | 2026-08-30 15:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| bd77301e-73b9-3900-8e46-c2ec930503d9 | -5.8894 | -57.7708 | 2026-08-30 15:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| d01459b1-0c67-3bdb-8ffc-7f7434f234dd | -4.1516 | -60.6878 | 2026-08-30 15:20:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 208504b9-4ffb-3a62-a3ea-dacfe97f096f | -9.208 | -65.8044 | 2026-08-30 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 3511f3fa-72b2-3383-b7d0-c6269268eccd | -10.9749 | -50.5077 | 2026-08-30 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| d8607114-621b-3818-859e-bb9727baea5c | -9.0717 | -60.4918 | 2026-08-30 15:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 43.1 |
| ddad77c1-2f8b-3963-bb66-7d2863488087 | -11.2317 | -53.9958 | 2026-08-30 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 115.9 |
| 46ffb89d-597d-3b99-8647-e1ef257535a2 | -11.3431 | -45.1521 | 2026-08-30 15:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 127.0 |
| 0c2a7d20-844f-337b-8626-5608d6d65244 | -14.5035 | -52.1487 | 2026-08-30 15:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 9ff1e073-ab9b-3357-94d5-f54a13b12505 | -6.6198 | -53.3576 | 2026-08-30 15:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 38f15283-eb68-3358-af00-357ed600e7bd | -7.5272 | -44.3413 | 2026-08-30 15:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 131.8 |
| 43dfebde-6e2e-3857-a06b-5a412e10fd45 | -10.7867 | -45.3433 | 2026-08-30 15:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 181.1 |
| b9e19114-9b89-3dba-ba2b-2d7c5e25d00c | -9.8925 | -60.2945 | 2026-08-30 15:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 38c59a93-7c5e-3c86-9ab1-cdfeef08f3b6 | -3.0769 | -59.126 | 2026-08-30 15:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 83d26356-f9e4-39da-a3b4-48e05f0afca9 | -10.5782 | -50.4643 | 2026-08-30 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 92.5 |
| a034ac25-9d80-37f3-9b89-5464e3578cc6 | -9.1711 | -59.618 | 2026-08-30 15:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| e67a6beb-3965-3251-9769-dce4dbf651a4 | -11.2638 | -45.3241 | 2026-08-30 15:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 113.5 |
| ce49285e-3849-3595-baca-778e70ce7c48 | -14.4477 | -58.4709 | 2026-08-30 15:30:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 85616f1a-fe84-3180-9fad-07578babc705 | -9.9281 | -60.5242 | 2026-08-30 15:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 91e99d03-08c5-3385-8ec6-27c7327551d9 | -1.8779 | -55.1287 | 2026-08-30 15:30:00 | GOES-19 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 4032a119-5a2d-3a79-913e-ec6f6e2c19ad | -7.3479 | -55.1544 | 2026-08-30 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 85efe0f3-3246-3820-a04b-5cc8aff43626 | -5.9636 | -57.6704 | 2026-08-30 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| b4b0a007-f7b2-3198-9f2a-2a8fa5a74d70 | -14.2092 | -45.3207 | 2026-08-30 15:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 134.5 |
| 203c846c-e890-3adb-8df1-231d15dbf0b8 | -5.4875 | -57.1611 | 2026-08-30 15:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 8aedbfd2-ee60-3ec6-9f8b-eb6f556b6305 | -10.4794 | -64.5012 | 2026-08-30 15:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 2714d5b3-1b89-3ebe-b370-d01a345c8a8b | -7.1121 | -42.7963 | 2026-08-30 15:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 160.2 |
| ed186157-0578-36f7-90dd-2bb9e068363b | -11.1634 | -50.5727 | 2026-08-30 15:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 00be4dee-47ac-3702-95e2-53c76b0e7e09 | -6.695 | -58.7291 | 2026-08-30 15:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 70090568-f99d-31d3-99c7-b692ff2f39e8 | -11.3622 | -45.1494 | 2026-08-30 15:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 01af3a28-8f18-321b-bc20-0d8cc1222d6b | -3.1998 | -61.161 | 2026-08-30 15:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| a5432b55-ce3c-3314-8c1f-ce1c35e17d17 | -6.0 | -45.0889 | 2026-08-30 15:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 2d75588c-4c55-38ae-b983-aad8f5b5325e | -13.6422 | -51.856 | 2026-08-30 15:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 9586bcf3-41cd-3bec-9de4-6c972e77f999 | -11.0054 | -49.6893 | 2026-08-30 15:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 88.0 |
| a0d0fd27-e593-3b14-8745-aa670fe66a94 | -14.4842 | -52.1512 | 2026-08-30 15:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 220.5 |
| 5df8ac12-5273-3aca-a883-ab7373f7af7a | -9.2262 | -65.8784 | 2026-08-30 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 499.3 |
| 608d44b6-f276-3536-8e30-6ff8e9c50c53 | -10.8025 | -50.6539 | 2026-08-30 15:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 2064f2ff-e7b4-366f-9e20-26e997c1fa6d | -6.1294 | -57.6833 | 2026-08-30 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 558f2e1d-2fa4-35fd-82d6-0120e0f1eee6 | -9.0723 | -60.4148 | 2026-08-30 15:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 3bb35562-952c-381e-8348-310e00405c52 | -12.9216 | -45.8812 | 2026-08-30 15:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 4ecf4253-d930-3a0f-9f8b-ba268660e591 | -16.2735 | -42.5653 | 2026-08-30 15:30:00 | GOES-19 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 149.7 |
| f29b889b-fc93-3bc9-83b7-d658a7755d9d | -14.1649 | -52.8058 | 2026-08-30 15:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 184.9 |
| ad4a3844-4954-337b-ad1d-ed2903d51b33 | -13.4764 | -51.43 | 2026-08-30 15:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 7dea0bbe-c40d-38de-82c1-d9af93786abb | -14.4197 | -52.5413 | 2026-08-30 15:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 177.9 |
| cc8786c7-99bd-3267-a575-f9b3bb788c72 | -13.4187 | -51.4372 | 2026-08-30 15:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 213.5 |
| 39303055-e481-3b85-9757-beeb3fb874dc | -5.4876 | -57.1416 | 2026-08-30 15:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 164.6 |
| 48e90d96-64fa-3afc-bdda-94529e7f14d5 | -8.1345 | -45.4923 | 2026-08-30 15:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 8a0faee7-5bdb-349c-8787-7c9ca6e0c44a | -11.6586 | -50.4532 | 2026-08-30 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| a7081831-2af6-3b53-a965-5e676a814448 | -5.8788 | -46.1103 | 2026-08-30 15:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 5bbbce46-4fd6-3701-9366-7a837abb971e | -6.5234 | -51.4279 | 2026-08-30 15:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| d0c12ffa-5513-359c-a860-55b88c78fdbe | -10.7644 | -50.6792 | 2026-08-30 15:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 151.3 |
| 42cd7e1a-6b0a-3fad-9b30-f85f48424142 | -10.8249 | -45.3382 | 2026-08-30 15:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 144.2 |
| 2c1c9ca5-d6b8-3bde-8580-4e81f9f210a4 | -9.1661 | -60.2945 | 2026-08-30 15:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 6872be8f-fa8a-3de6-a23b-470dd05469e7 | -5.8894 | -57.7708 | 2026-08-30 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| f85a70d2-8004-3397-b9fc-79b3820fc646 | -5.982 | -57.6697 | 2026-08-30 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| d2c337f2-65ba-3835-8d65-0843947f2703 | -6.0541 | -57.9591 | 2026-08-30 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| a98ebe15-3134-363e-a50b-281c8c069429 | -10.9559 | -50.5098 | 2026-08-30 15:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| b539f9db-b48c-3467-ab01-809fd072066f | -11.0244 | -49.6872 | 2026-08-30 15:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 30cb275e-1d4d-3e49-b78f-f05092cf3548 | -6.9546 | -55.7147 | 2026-08-30 15:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| c5d9d1d0-d404-38ac-bb7f-84991ade1a91 | -8.1534 | -45.4904 | 2026-08-30 15:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 13fa202c-002f-387a-b415-283a916de1d2 | -4.1699 | -60.6874 | 2026-08-30 15:30:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 46.3 |
| eeb63735-c23e-3382-990e-95188cd1d4ed | -8.3679 | -57.6737 | 2026-08-30 15:30:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| a25bde01-250c-3998-afbb-819170da2ecc | -13.3995 | -51.4397 | 2026-08-30 15:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 18b52af0-daf4-3be4-be1f-bca3624f4083 | -6.0726 | -57.9583 | 2026-08-30 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 992ba821-2dc5-3b24-908e-75da5eb53f22 | -9.043 | -65.4175 | 2026-08-30 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| b619f3e7-dbf5-3e39-8af0-15aafc3955b7 | -11.3619 | -45.1724 | 2026-08-30 15:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 173.4 |
| b57bdec4-6823-3958-b728-68f6ca94e80b | -9.0429 | -65.4361 | 2026-08-30 15:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.8 |
| a761d0de-545e-3b43-a29b-f084fd5602cc | -10.7649 | -50.6366 | 2026-08-30 15:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 8e311f81-3355-33f6-9fa1-4639fd4000b7 | -7.9169 | -61.3671 | 2026-08-30 15:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |


[Clique aqui para ver as próximas entradas](README93.md)
