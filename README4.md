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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1bac32de-84cb-39ab-87a7-a60fcf2116f8 | -8.6032 | -40.1834 | 2025-10-19 00:50:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 76.3 |
| 8b9d9d8f-ac94-3d41-a790-c0044e301bed | -10.2422 | -44.8866 | 2025-10-19 00:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 76.3 |
| a1fe40fc-a396-3c9e-bbbc-b4d59d6c3569 | -11.6489 | -44.0854 | 2025-10-19 00:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 8fa27558-8ac8-3731-a7e0-9d8479da15d6 | -8.6032 | -40.1834 | 2025-10-19 01:00:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 75.1 |
| f87654ad-8304-320f-962a-6e24c09dd2f7 | -10.5522 | -43.3761 | 2025-10-19 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 6b48827d-ee62-3f07-ad47-393d74738c27 | -11.6489 | -44.0854 | 2025-10-19 01:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 0c0b7728-b2a0-391a-a08a-67b44c20025d | -2.6841 | -49.5427 | 2025-10-19 01:00:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| f68f0eff-f9c3-33cd-b30c-ad1ac8705177 | -8.4345 | -44.1324 | 2025-10-19 01:00:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 8b3b4ef7-d2a8-3bdd-9814-d0c8884f8a9d | -2.9127 | -52.735 | 2025-10-19 01:00:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 33f80f54-2b32-3372-9463-9483edb75f59 | -4.9766 | -56.2764 | 2025-10-19 01:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 0701b8cc-b56f-3513-8c81-e2e11081574a | -2.684 | -49.5639 | 2025-10-19 01:00:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 42e6ecd5-cf56-393b-9d32-0bf3204d523a | -7.6237 | -60.9403 | 2025-10-19 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 82dddf67-b41e-3142-aad8-e88f88b53eaf | -10.2422 | -44.8866 | 2025-10-19 01:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 1139a3fe-7a58-3ed9-91bd-4cdeefd27c2a | -17.4587 | -40.0547 | 2025-10-19 01:00:00 | GOES-19 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 141.4 |
| 6170f370-2f45-385a-b254-e8b00579534e | -17.4377 | -40.0863 | 2025-10-19 01:00:00 | GOES-19 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 255.1 |
| 3dd77a99-e024-3ee5-9977-f832853f7ee9 | -17.4579 | -40.0808 | 2025-10-19 01:00:00 | GOES-19 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 81.8 |
| f6c1c5a7-8b33-3f37-a432-537cb6383fcf | -7.6238 | -60.9212 | 2025-10-19 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 81.8 |
| b5ded0cd-8cbf-3311-a12b-d3bfbf26d35a | -14.4759 | -45.5751 | 2025-10-19 01:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 464abc08-475e-3fe3-a1c1-b0c24c4b3d1f | -10.8671 | -43.9428 | 2025-10-19 01:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 289af664-eab6-3fcf-9388-a5a208492b29 | -10.8891 | -46.0814 | 2025-10-19 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 1700ecc6-1688-396a-baec-8164e237aa02 | -8.6219 | -40.2058 | 2025-10-19 01:00:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 79.7 |
| 6c4b78b4-951b-3f9b-ba67-d03181b8f52d | -10.5518 | -43.3998 | 2025-10-19 01:00:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 84e317a2-315a-3abb-a40b-fb9fe26c46d0 | -8.6223 | -40.1809 | 2025-10-19 01:00:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 131.0 |
| d4c11ac0-0d1f-3c96-931d-f03de0215536 | -2.9128 | -52.7146 | 2025-10-19 01:00:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 02f962cd-a02d-3e24-9cf0-a380fb4bd494 | -8.4342 | -44.1556 | 2025-10-19 01:00:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 83.0 |
| c2adbca8-fd5b-3240-b8bc-81dc74c9d0c3 | -17.4392 | -40.0342 | 2025-10-19 01:00:00 | GOES-19 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 88.4 |
| f6b60229-0119-3e0f-a365-62bb1f883929 | -10.5714 | -43.3734 | 2025-10-19 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 09c43397-ba03-34c0-af92-525c1cefd62b | -5.3086 | -45.0695 | 2025-10-19 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 2622b80c-3d16-352c-84e3-78d312c9b654 | -17.4385 | -40.0602 | 2025-10-19 01:00:00 | GOES-19 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 493.7 |
| a8c9e108-c02d-3e56-8520-de38644fb712 | -2.7026 | -49.5422 | 2025-10-19 01:00:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| afdba02e-eaf7-3afe-b4c3-2f6590967a4e | -2.6841 | -49.5427 | 2025-10-19 01:10:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| fce3da68-b0cb-3bea-9fed-89a24ad1c0a0 | -10.5714 | -43.3734 | 2025-10-19 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 62.1 |
| f8961b7f-7c53-3834-88ee-bd911dd9abf7 | -14.3157 | -51.8542 | 2025-10-19 01:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 05640c14-843b-3569-bd6e-54e83ac6cfc5 | -11.6489 | -44.0854 | 2025-10-19 01:10:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 11099b92-ca65-3910-b96c-aee28602f714 | -4.9766 | -56.2764 | 2025-10-19 01:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 05e76a61-16c1-3831-937a-45c48af58a95 | -8.4342 | -44.1556 | 2025-10-19 01:10:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 81fe573d-efb3-353e-988b-674daa5ec15d | -8.6029 | -40.2083 | 2025-10-19 01:10:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 64.6 |
| 64168a96-2e3c-3a58-846e-f6d506766782 | -5.6472 | -44.7964 | 2025-10-19 01:10:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 3eb9b246-19e9-381d-9174-dc9c9c56c890 | -5.3105 | -44.8423 | 2025-10-19 01:10:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 87aa110e-e4a4-39e8-9d70-6b2c3f799d92 | -10.5518 | -43.3998 | 2025-10-19 01:10:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 71.6 |
| c2ca09a6-0755-3dcc-b9c2-9ecded430c37 | -5.3291 | -44.8411 | 2025-10-19 01:10:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| fcf53336-f8e6-3d40-a958-dff182cb8eb3 | -2.7025 | -49.5634 | 2025-10-19 01:10:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 91c4bfbc-512d-34e2-928c-2dca4ae204af | -5.1017 | -47.79 | 2025-10-19 01:10:00 | GOES-19 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 57.1 |
| b3cf0df0-794f-3df3-b03e-d86ea1e708d9 | -2.9127 | -52.735 | 2025-10-19 01:10:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 101.8 |
| 0e979aca-350a-3afa-938f-b8faa4c7eb55 | -8.6219 | -40.2058 | 2025-10-19 01:10:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 82.3 |
| 804d54ce-fe1a-3af2-aeae-90031cbd834e | -10.8863 | -43.9401 | 2025-10-19 01:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 6ea53fc6-3745-34e3-b9fb-382d99378dda | -8.6032 | -40.1834 | 2025-10-19 01:10:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 85.9 |
| b078eadf-e534-35ca-9780-796d9843ab38 | -10.5522 | -43.3761 | 2025-10-19 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 86.2 |
| b4ea404a-52a9-352b-96be-735e315d5783 | -8.6223 | -40.1809 | 2025-10-19 01:10:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 103.6 |
| 9ae4484d-0475-3920-9509-546f95842735 | -2.9128 | -52.7146 | 2025-10-19 01:10:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 8be34a86-da9d-3097-a413-778b3b1d1271 | -10.8671 | -43.9428 | 2025-10-19 01:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 6d48bf6d-9325-30ee-b3d3-870716c75538 | -8.4345 | -44.1324 | 2025-10-19 01:10:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 70.3 |
| dfc27b68-c0bf-36a1-9407-967438d43fec | -2.7026 | -49.5422 | 2025-10-19 01:10:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 0854d467-b1ae-3d67-a59c-44b17086d3e6 | -5.3086 | -45.0695 | 2025-10-19 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 497110ca-c2cb-3e77-a571-a63307156371 | -2.9311 | -52.7346 | 2025-10-19 01:10:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 42eec1da-272b-38c3-a342-4894af36d809 | -10.8891 | -46.0814 | 2025-10-19 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.3 |
| f8103ffe-d129-3e16-af2f-87ce66d3537c | -17.8586 | -40.1002 | 2025-10-19 01:20:00 | GOES-19 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 79.9 |
| a382680c-6740-3953-a8a2-15f38d297636 | -14.4578 | -51.4506 | 2025-10-19 01:20:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 9650513d-4eae-395d-ab74-ae2e8f1af9ed | -8.6029 | -40.2083 | 2025-10-19 01:20:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 73.6 |
| e4f2862c-2290-35c3-aa90-6ca01c90d4ca | -4.9766 | -56.2764 | 2025-10-19 01:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| f84b939a-79a7-3612-8350-92eb5053057a | -14.4574 | -51.4721 | 2025-10-19 01:20:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 159.7 |
| 10ef61dd-0a93-3d35-ad00-0a2bf6b9ba7b | -2.9128 | -52.7146 | 2025-10-19 01:20:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 97.9 |
| a50e880a-84d5-3445-8183-e46054d4a67d | -2.6841 | -49.5427 | 2025-10-19 01:20:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 5182ac70-11e7-3b3d-9617-b8fe4af21939 | -14.4767 | -51.4694 | 2025-10-19 01:20:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 76.5 |
| d8a7be86-7c19-3eac-b316-8a1a27990c00 | -11.6489 | -44.0854 | 2025-10-19 01:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 681fc563-d149-3a37-bdff-7260d37c9ea2 | -10.8671 | -43.9428 | 2025-10-19 01:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 9e6d43c2-804c-3e44-9ba4-ee515887cdc2 | -10.5522 | -43.3761 | 2025-10-19 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 7ec57985-346d-3714-a423-fac89beec848 | -5.3086 | -45.0695 | 2025-10-19 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 57.0 |
| c593cd2d-9d5e-38d0-97cb-1de63ea9cfa1 | -17.8789 | -40.0946 | 2025-10-19 01:20:00 | GOES-19 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 88.8 |
| e30aa0b6-07f1-33a4-8fb0-ab94900e26dc | -6.522 | -41.6616 | 2025-10-19 01:20:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 36.0 |
| a5e02b54-09bb-341d-8c0b-36804ead5a67 | -2.9127 | -52.735 | 2025-10-19 01:20:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 106.9 |
| 396bac54-5516-36c7-a726-d90beb2cbd9a | -8.6223 | -40.1809 | 2025-10-19 01:20:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 82.8 |
| 96fff5ad-bf96-31c7-af35-5060314fb65c | -5.6472 | -44.7964 | 2025-10-19 01:20:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 0be3f640-6afb-33dd-94de-afd4d9e9689d | -11.6297 | -44.0884 | 2025-10-19 01:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 56.3 |
| e159e47b-f5f9-337d-b025-11bb2bd500ba | -14.4764 | -51.4909 | 2025-10-19 01:20:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 71.9 |
| e9d7a9d1-2319-3a58-b779-e734926256f6 | -10.8891 | -46.0814 | 2025-10-19 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 2c8b1dd6-14ec-306b-aad4-a6cbf06ce2b8 | -14.438 | -51.4747 | 2025-10-19 01:20:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 7238959f-2d64-32a1-96f3-770ad5e15ed5 | -2.7026 | -49.5422 | 2025-10-19 01:20:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 5e37ac0b-53e0-34b5-b449-78e238bd53ee | -14.457 | -51.4935 | 2025-10-19 01:20:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 598b86e6-9e72-3f25-a69f-15ba7b63e006 | -8.6032 | -40.1834 | 2025-10-19 01:20:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 107.7 |
| 290e2bf7-3562-36a6-af87-9d02d81f8453 | -5.3105 | -44.8423 | 2025-10-19 01:20:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| b3fdd3db-3c63-31fd-9820-a97344297650 | -11.6301 | -44.0649 | 2025-10-19 01:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 48.5 |
| d46e7d50-383a-367b-aa7d-6db772f25101 | -10.8891 | -46.0814 | 2025-10-19 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.3 |
| fd15e7c1-f522-3a62-b4af-f196f58a6678 | -8.6223 | -40.1809 | 2025-10-19 01:30:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 103.3 |
| d2d7ee04-7fab-3844-998c-bdd59f579be3 | -8.6032 | -40.1834 | 2025-10-19 01:30:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 72.2 |
| dc50d10d-ff87-34d2-9e98-d8c10ae737a1 | -2.9127 | -52.735 | 2025-10-19 01:30:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 78ff457a-9282-352d-b288-56b761e07d31 | -17.8586 | -40.1002 | 2025-10-19 01:30:00 | GOES-19 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 74.4 |
| ad821bb2-1983-3d36-9ff7-bf1482b8d51c | -10.5522 | -43.3761 | 2025-10-19 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 74.3 |
| f6100972-e9a3-3370-a569-cb514e75a900 | -5.1017 | -47.79 | 2025-10-19 01:30:00 | GOES-19 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 06b8165d-d378-36c7-892b-c667e8330acc | -6.522 | -41.6616 | 2025-10-19 01:30:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 67.5 |
| c65006c2-cafa-3bbb-b588-1377806cbeed | -11.6297 | -44.0884 | 2025-10-19 01:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 97a4fc52-227e-3782-92c3-237ae35da70b | -5.3086 | -45.0695 | 2025-10-19 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 71ca8a24-ea86-307b-a855-df49db836fff | -10.5518 | -43.3998 | 2025-10-19 01:30:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 4756033e-d600-3897-9958-7edd0c31ac2a | -14.4949 | -45.5949 | 2025-10-19 01:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 5611b85a-2032-3eb0-99b1-2b02d6dfee54 | -11.6489 | -44.0854 | 2025-10-19 01:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 316cd70d-e659-3e0f-b602-79f008e29510 | -2.9128 | -52.7146 | 2025-10-19 01:30:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 114.9 |
| 62cebaa1-06bb-33ff-9f78-26e3b6706ab9 | -14.4759 | -45.5751 | 2025-10-19 01:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 6aa9a3a5-479c-3a18-a9fc-c914188176e7 | -7.6238 | -60.9212 | 2025-10-19 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 169c06f5-45d8-3865-93e6-6f1b5fd5a892 | -6.5409 | -41.6599 | 2025-10-19 01:30:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 36.4 |
| 5ac5e2aa-16de-347d-88dc-a5b0f2f502cf | -5.3291 | -44.8411 | 2025-10-19 01:30:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 57.0 |


[Clique aqui para ver as próximas entradas](README5.md)
