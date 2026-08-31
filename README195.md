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

## Dados Diários - Página 195

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dcae2d2e-04b8-3f0a-9e3d-9ae24ef476ef | -11.0747 | -51.5153 | 2026-08-31 19:20:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 89.0 |
| a90d3e66-d858-3c73-8580-ff94999c0559 | -19.0944 | -57.3849 | 2026-08-31 19:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.5 |
| 67c5b84e-1dd4-387a-a6cf-b98e48aa0005 | -10.2743 | -64.4907 | 2026-08-31 19:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 737088cd-8564-38f9-9ba1-4d1e0378c963 | -11.4972 | -45.084 | 2026-08-31 19:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 1187a506-ec26-3f9d-b2ae-10837cfea972 | -12.9054 | -59.8857 | 2026-08-31 19:20:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 999dcaaf-5fd0-358f-aded-c07fcf6d9b18 | -10.4634 | -46.5638 | 2026-08-31 19:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 144.2 |
| d1188d95-18f4-3025-8d63-b40baaa0e518 | -14.5623 | -52.0984 | 2026-08-31 19:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 132.8 |
| 25dfc8e0-3eba-3630-b440-ddef3a9591eb | -7.6991 | -55.3344 | 2026-08-31 19:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 649ae663-dfca-3ef8-bb05-79e71f0b32c1 | -9.1711 | -59.618 | 2026-08-31 19:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| d8771a3f-aed2-330e-9b1e-6135b49b92a9 | -12.9056 | -59.8661 | 2026-08-31 19:20:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 39967557-a854-3649-9335-0d9ababa14e7 | -10.7405 | -54.0606 | 2026-08-31 19:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 7b973864-bbe1-365f-b6fa-152ea86ace59 | -12.1113 | -45.0163 | 2026-08-31 19:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 52614662-dcfc-3798-a514-bb12963a9f66 | -14.444 | -53.4016 | 2026-08-31 19:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 79deb628-256d-3509-8ba5-eb58f55649ad | -9.1709 | -59.6374 | 2026-08-31 19:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 299336d6-ed9d-3373-a368-6807d31c0379 | -8.499 | -55.3051 | 2026-08-31 19:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| e6a015c5-7556-30fd-9b44-70be277b7eaa | -12.0921 | -45.0192 | 2026-08-31 19:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 7ef173ea-bc22-3384-8077-f9fec09987d8 | -8.5739 | -66.9754 | 2026-08-31 19:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| e3ece317-704f-3528-8e2b-921b57af111f | -4.5963 | -42.9266 | 2026-08-31 19:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| d97d274d-d5e9-3eed-ae31-892f7369336a | -11.1995 | -55.1008 | 2026-08-31 19:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 7a7d85e7-cabb-3b66-ad1d-b84b1239c6f2 | -7.4735 | -61.3846 | 2026-08-31 19:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 85.5 |
| f4bce56d-9430-3e4b-aa3f-90e884f5ef3f | -6.137 | -53.5259 | 2026-08-31 19:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| dcca2596-a1b2-3d34-9595-560b99b5a172 | -8.9295 | -62.3712 | 2026-08-31 19:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 7fb17d38-757c-37bd-8f88-2b83a9378bf5 | -7.905 | -44.2346 | 2026-08-31 19:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 96.9 |
| dd134054-ea2a-33f7-b133-8d97337de3d5 | -6.1618 | -52.6265 | 2026-08-31 19:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 6a4add8e-6e91-3373-9c1f-4c76c8c66239 | -19.1347 | -57.3589 | 2026-08-31 19:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 160.4 |
| cfbe4a5f-ac69-3b97-96ea-0e306042f9ab | -14.1459 | -52.7871 | 2026-08-31 19:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 76.5 |
| b1633b63-adbc-38ce-b1ea-8fb8f44c4da9 | -8.5177 | -55.3039 | 2026-08-31 19:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 670602de-64d3-3945-82dc-c8e9264f6790 | -9.9708 | -53.9419 | 2026-08-31 19:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 8c28d22b-e81d-3db7-9171-2aa89992b6e0 | -10.5719 | -57.495 | 2026-08-31 19:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 99.1 |
| ce19b38c-2c05-3c3e-843c-e2d00193e354 | -10.7591 | -54.0794 | 2026-08-31 19:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.7 |
| fba00a27-1542-3f5c-b0d8-f62c2c9132f7 | -9.6868 | -46.5433 | 2026-08-31 19:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 165.5 |
| 00be137b-4eb1-3f3a-8ddb-31c2f1b49eea | -8.8405 | -70.601 | 2026-08-31 19:20:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 7ac5d08d-4868-3422-93e4-655fe8a79cfc | -11.5009 | -60.5867 | 2026-08-31 19:20:00 | GOES-19 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 6fc11aea-528a-368d-bf58-1399fff7843c | -15.6333 | -56.4081 | 2026-08-31 19:20:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 75.3 |
| dcac6102-daf4-3c09-9098-ab99d73903db | -15.2475 | -53.8876 | 2026-08-31 19:20:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 153.6 |
| 2bd11dd4-6454-302a-aee1-08dce9936d94 | -9.4721 | -57.0156 | 2026-08-31 19:20:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 129.2 |
| 62fcf57e-1940-3282-a138-a0a8a4a11d78 | -3.6399 | -60.5466 | 2026-08-31 19:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 769da2f1-5c33-300f-add7-22a74f34dac3 | -6.8217 | -43.5271 | 2026-08-31 19:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 66.9 |
| f45eda08-b4a2-3ecd-b4b0-683f52f06f53 | -7.0293 | -55.6312 | 2026-08-31 19:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 0f2029c7-0cee-3b9a-8fa0-91a29d3560fc | -6.7648 | -59.4408 | 2026-08-31 19:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 111.9 |
| ef94d3cc-9f35-31a4-90a8-895570263cf5 | -7.0517 | -52.7187 | 2026-08-31 19:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 212.7 |
| 20450bb1-35ee-3987-84bd-e132ae4667f6 | -3.4002 | -61.3465 | 2026-08-31 19:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 405c86fe-f473-330b-a2f1-89c8f80ab7b8 | -6.8233 | -58.8786 | 2026-08-31 19:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 3803e0cd-d069-3331-a2f8-ffdb8235c36a | -17.3228 | -42.6878 | 2026-08-31 19:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 214.1 |
| d5b153af-d608-39b3-b024-e1848c66f497 | -6.3618 | -55.8632 | 2026-08-31 19:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 390cb189-e34d-3415-82d2-06b1775cb77e | -6.2537 | -55.4308 | 2026-08-31 19:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 4bcef445-4844-3583-8ca3-7f63af6e0869 | -10.1321 | -45.8825 | 2026-08-31 19:20:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 7364b1f9-0416-37ff-827d-bd6f3655fc34 | -6.1433 | -52.6275 | 2026-08-31 19:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 3f765844-d309-3193-9739-5009a7f6773c | -7.4803 | -63.7267 | 2026-08-31 19:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 0f69cb2f-4f55-3879-b45e-e7557c57f883 | -7.0292 | -55.6511 | 2026-08-31 19:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| a6af9895-ac88-310e-82cf-43429810cd2f | -8.5969 | -54.7755 | 2026-08-31 19:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 99.7 |
| b884fffb-b787-35b3-9095-594231f7d4ee | -2.7118 | -47.0649 | 2026-08-31 19:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 33c08a21-e5f6-3e60-97ec-39a92a023c92 | -6.8193 | -59.5734 | 2026-08-31 19:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 5002e297-39fe-3acc-8828-2bcfd38d308c | -14.2599 | -52.8782 | 2026-08-31 19:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 1d8ef73f-98cc-320a-b7ad-63fd1d14d1b9 | -10.9862 | -48.4088 | 2026-08-31 19:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 171.2 |
| b4ea24a8-4315-34e8-91b3-c6afa8649f4a | -6.8017 | -59.4394 | 2026-08-31 19:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| ea57774d-e950-30fb-9509-04253b78afa2 | -14.1456 | -52.8082 | 2026-08-31 19:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 20d7e523-556a-3877-9f03-41288854c81e | -8.3601 | -70.8458 | 2026-08-31 19:20:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 53.7 |
| da3b26ca-e114-3de4-b832-d030740a1586 | -4.7941 | -55.967 | 2026-08-31 19:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 36cc4b6c-7f27-38a1-a576-4a03efcd0c35 | -5.2547 | -55.9105 | 2026-08-31 19:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 2a67cddc-976d-3457-8876-28261e4b37c0 | -5.4876 | -57.1416 | 2026-08-31 19:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| f4554480-0dc1-3ed0-b2f7-344b7d0a25bf | -6.9367 | -55.636 | 2026-08-31 19:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 203.8 |
| 3d9e229f-b8b1-3fc7-a7a1-ed7cd8a95cbb | -3.1266 | -61.2 | 2026-08-31 19:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 57e8320f-7ac9-3bc6-89ea-128f5b9829d1 | -9.694 | -65.0958 | 2026-08-31 19:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 4d8a9fd3-ff7f-32b2-8893-53914219a74c | -8.7628 | -46.4642 | 2026-08-31 19:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 09d464c4-5bba-3fc0-8e52-2219e7940c97 | -3.0637 | -43.1229 | 2026-08-31 19:20:00 | GOES-19 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 208.8 |
| bdac8163-9b66-36c6-b347-3264519cd944 | -7.6264 | -57.615 | 2026-08-31 19:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| c90b0044-d245-3824-8af6-5e70ba624931 | -11.2478 | -45.1425 | 2026-08-31 19:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 61.8 |
| f913dcf7-9f7a-3d12-add6-3b8db5fe6f79 | -8.0443 | -61.7237 | 2026-08-31 19:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 1ee4d824-7adc-34c3-b73b-1c26a44a1417 | -14.9863 | -48.1304 | 2026-08-31 19:20:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 98e84468-efaf-317d-8791-6136c4d9fa9c | -5.9636 | -57.6704 | 2026-08-31 19:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 062e1cde-6b41-3ea5-83a6-8deff18bfa86 | -11.4828 | -58.5159 | 2026-08-31 19:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 6481f283-5f99-3dfa-afb7-7e3935507c56 | -3.4002 | -61.3276 | 2026-08-31 19:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 2f541443-0bb7-3096-ab40-1eae82b1b008 | -10.844 | -45.3356 | 2026-08-31 19:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 81c61cc2-6f2c-30fb-b72f-74599562ff1b | -15.8844 | -56.4819 | 2026-08-31 19:20:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 257597d5-3cd0-3b0c-a81e-e436ff9cd549 | -11.2294 | -45.099 | 2026-08-31 19:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 57.9 |
| b1c87741-8e7e-3efd-a115-08e48c7f8e24 | -5.8537 | -57.5576 | 2026-08-31 19:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| bddb5ff4-6f5c-354f-9dc6-540f8ee7f7b1 | -3.6398 | -60.5656 | 2026-08-31 19:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 121.5 |
| ebeac4f4-60a9-3496-b722-854fc9598981 | -19.1547 | -57.3562 | 2026-08-31 19:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 124.7 |
| f1318d85-fff2-3565-83c4-2cd0ae465276 | -3.3871 | -59.3883 | 2026-08-31 19:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 0a665f4a-363b-3be8-be78-97a773d43f31 | -6.4055 | -49.9228 | 2026-08-31 19:20:00 | GOES-19 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| f8baf742-c880-3f3b-b733-3f55c83f233a | -5.9451 | -57.6906 | 2026-08-31 19:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 125.8 |
| 5214df9e-1958-3d70-8928-f28e0a906ff6 | -10.9859 | -48.4308 | 2026-08-31 19:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 91.5 |
| f65f0232-2125-3ad4-9dfa-40375d0aab88 | -8.9481 | -62.3704 | 2026-08-31 19:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 0694814c-da65-3e23-8b39-bc272f608bc1 | -8.5971 | -54.7553 | 2026-08-31 19:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 3aa288a6-11d7-30d1-92dd-95667cde4f19 | -9.4908 | -57.0144 | 2026-08-31 19:20:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 24c7873b-824d-3ad1-a154-c82591b031d9 | -6.4054 | -49.9441 | 2026-08-31 19:20:00 | GOES-19 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 123.7 |
| 74239816-d1a7-313e-8e7c-3e223fd3d0c1 | -6.9365 | -55.6559 | 2026-08-31 19:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 1b8bc7bd-fd8e-35ac-80a5-4d776b08c371 | -11.0744 | -51.5365 | 2026-08-31 19:20:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 49331486-b8b7-3424-a89b-1e1f04e5e096 | -8.8706 | -66.7636 | 2026-08-31 19:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 260.5 |
| 41304127-c79b-357a-b87b-bb43269c7d31 | -10.1542 | -45.6755 | 2026-08-31 19:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 9af78fc6-2cca-3f59-9472-3254f5d9368b | -9.4153 | -45.6726 | 2026-08-31 19:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 7d8a4c69-1a64-3b75-80c2-9da4a6ea3c9e | -9.4719 | -57.0354 | 2026-08-31 19:20:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 111.3 |
| fd08094c-827b-3810-9ee7-46535d95eff9 | -8.8521 | -66.7641 | 2026-08-31 19:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 85a9b189-b06a-3b36-be96-542bf3fc6b0d | -8.6673 | -62.8369 | 2026-08-31 19:20:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 67.1 |
| d156ecbf-01f0-3fbb-b041-c38546d5363d | -7.917 | -61.3481 | 2026-08-31 19:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| ae1389c8-ee51-33d5-b00c-bee1fecccc86 | -3.3871 | -59.4075 | 2026-08-31 19:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 5a1647bd-ce66-3fb5-aed4-dca3b30ce6da | -11.5479 | -45.4676 | 2026-08-31 19:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 205.9 |
| 07a36a5b-9995-371a-95c4-7f768907e442 | -6.2106 | -53.5831 | 2026-08-31 19:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 2b6af62b-6f3c-370b-8381-91f8931bd2ba | -4.9787 | -55.8615 | 2026-08-31 19:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |


[Clique aqui para ver as próximas entradas](README196.md)
