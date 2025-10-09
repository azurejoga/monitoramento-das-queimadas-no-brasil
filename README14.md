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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 04508990-492b-381c-841f-2e8914c39981 | -14.41824 | -43.97484 | 2025-10-09 03:32:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 8e7b577a-e00f-330d-971e-e06c13385597 | -17.60161 | -47.1832 | 2025-10-09 03:32:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ab928fd-4c86-3ef9-b3d6-a1579ddf9352 | -17.63302 | -47.20174 | 2025-10-09 03:32:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 53937ee1-37f0-3b96-98a2-5dffb9fdcc80 | -16.75274 | -43.96886 | 2025-10-09 03:32:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| d73501f1-1090-3dcc-ba59-5b0c6dc4f54a | -18.65004 | -43.91415 | 2025-10-09 03:32:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f522eef6-0ad8-36ef-b7df-86ac21afef50 | -16.37285 | -42.30537 | 2025-10-09 03:32:00 | NOAA-21 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| a41b5f8a-7b53-3260-b549-bd8b47d8e673 | -18.04908 | -44.96368 | 2025-10-09 03:32:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d8799208-9a20-3080-8463-092d2b4a0725 | -17.46053 | -43.38307 | 2025-10-09 03:32:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c8d7b5aa-b660-38bf-9243-17c95446faa5 | -11.75148 | -45.13793 | 2025-10-09 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7e268261-f8ee-32a0-be90-a0e02786c953 | -15.31087 | -46.15219 | 2025-10-09 03:32:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1ad461bc-4fa1-39d6-b6a6-61083106c707 | -18.02886 | -45.0051 | 2025-10-09 03:32:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1ccdde36-54f0-344b-bc59-93fa823c6771 | -16.27141 | -47.13712 | 2025-10-09 03:32:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7ae9a905-5f46-314c-ad19-5a0fde3f919f | -18.08551 | -44.44452 | 2025-10-09 03:32:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7345d810-576f-344f-8c0b-98111c28ff64 | -15.31712 | -43.85666 | 2025-10-09 03:32:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ee0806b7-1d50-3f3e-8e65-418ecf581cd6 | -13.80353 | -45.84536 | 2025-10-09 03:32:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1496f75e-6e2d-3c95-af7c-813a0719ffde | -14.97414 | -46.2938 | 2025-10-09 03:32:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ad4c2d67-f344-34b7-bcdf-41eea1180986 | -17.0797 | -43.37042 | 2025-10-09 03:32:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0d75394a-c140-363f-9904-6e3ec386f9fc | -15.39066 | -48.05238 | 2025-10-09 03:32:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2ee32b14-b408-3212-b425-05f7d6e93642 | -17.89507 | -44.26115 | 2025-10-09 03:32:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ef8e728a-69d2-3555-905b-056aca69617e | -15.47522 | -47.9645 | 2025-10-09 03:32:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8956702c-fc5d-3f7a-9cce-ae8d0f163c3f | -17.37658 | -46.8927 | 2025-10-09 03:32:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9241c6ac-2bc9-3588-8c5a-5eeb660d8896 | -16.69949 | -45.00504 | 2025-10-09 03:32:00 | NOAA-21 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 314ab7bf-7ebc-31f1-9e8e-0fc97f3c3695 | -14.94819 | -46.78416 | 2025-10-09 03:32:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 447f5ca9-af78-38d8-8e0b-d145e3db4cd3 | -18.41678 | -45.23036 | 2025-10-09 03:32:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f0cb54b3-3508-3bf3-b1b9-a5e074da859b | -15.29834 | -46.15806 | 2025-10-09 03:32:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| baa24edf-7194-3891-bb2d-1d0e03ee58c6 | -17.45607 | -43.37926 | 2025-10-09 03:32:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5aeb1ff4-2500-3318-8024-b46b37cb063d | -16.69864 | -45.00904 | 2025-10-09 03:32:00 | NOAA-21 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b51aebb3-3821-3772-b2b9-02c8e767d4a1 | -18.41975 | -45.24363 | 2025-10-09 03:32:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 052dd0da-e9c1-3d65-9475-b4027340668c | -17.37668 | -45.08307 | 2025-10-09 03:32:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| db08f19b-4ea0-3dc4-9f8e-d683ec4aff1c | -16.74745 | -43.96777 | 2025-10-09 03:32:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| de38f4ee-4d7c-3617-b3c6-12b3be1a6735 | -11.77354 | -45.05152 | 2025-10-09 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 88c04cf2-f74f-34d5-926b-136a34778ae0 | -15.39373 | -48.03875 | 2025-10-09 03:32:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a8eab4bb-1f99-3fb0-a849-aaa985d6285e | -13.78798 | -45.85714 | 2025-10-09 03:32:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e35266ca-1798-37e3-b9b7-68cbf314b70b | -18.05068 | -44.95604 | 2025-10-09 03:32:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e363c97f-e9c5-3f36-a726-7c96948b983a | -14.41044 | -43.98502 | 2025-10-09 03:32:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0598e5d4-b42b-3330-91a4-a53678e402ad | -13.37368 | -47.21574 | 2025-10-09 03:32:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 15.4 |
| d8009498-1ce6-3876-a925-440d29b67e1a | -13.79205 | -45.86884 | 2025-10-09 03:32:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4d943a78-d729-3e5e-86b3-aa3394d28566 | -17.3853 | -46.88292 | 2025-10-09 03:32:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bc16a1d5-5e41-3b3c-9edb-120be94df841 | -11.77213 | -45.15337 | 2025-10-09 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6db1758f-dc2f-345b-ac6d-f054d1cd1cbc | -13.3942 | -42.69959 | 2025-10-09 03:32:00 | NOAA-21 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ddc26343-0019-3450-ab14-46f30453819d | -11.87442 | -44.93206 | 2025-10-09 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ed3c792f-274b-332c-9f3d-780645511114 | -11.66997 | -43.89682 | 2025-10-09 03:32:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd34fb69-f805-3f90-acea-83b4d52a9c13 | -16.2 | -43.65941 | 2025-10-09 03:32:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 393e4dc3-2fcb-31c8-bbf4-06a26c2abaa4 | -16.37794 | -46.3822 | 2025-10-09 03:32:00 | NOAA-21 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 806dc568-1bd6-3209-b2b1-43cd06b2b64c | -15.47678 | -47.95768 | 2025-10-09 03:32:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 460c6997-f9f0-384f-8db5-16c3b166431f | -16.62497 | -46.76655 | 2025-10-09 03:32:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 709b2552-7dfc-3eab-90ca-f6899be922f4 | -10.85601 | -44.62419 | 2025-10-09 03:32:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 7dacfdbc-71d3-3bf1-8825-66f590f2473e | -11.80161 | -45.03993 | 2025-10-09 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8ec02ca3-96d8-3700-9a3a-2bc26da59b11 | -18.39615 | -45.2455 | 2025-10-09 03:32:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 98e85f55-2952-3274-9ffa-ac4a03e110bb | -17.95631 | -44.41729 | 2025-10-09 03:32:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d1b81b0b-290e-327c-8a41-9e85a403f76f | -17.98556 | -44.96549 | 2025-10-09 03:32:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0ab2de06-b105-3dc4-8fa5-868e5f28f9ee | -15.52431 | -41.85105 | 2025-10-09 03:32:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 6c66eb35-487b-3626-ae0c-86e38dd8be44 | -11.4685 | -43.48091 | 2025-10-09 03:32:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 12336308-3a02-34f5-bb07-06804fdade2f | -14.78943 | -46.09803 | 2025-10-09 03:32:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3daba3ff-725c-30b8-a73b-04f4d65cd411 | -14.42451 | -43.97222 | 2025-10-09 03:32:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 88c248e6-0e4e-34b1-99ea-39fa6cc40017 | -18.39996 | -45.2548 | 2025-10-09 03:32:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5b817934-a271-3021-94d2-d0092746d745 | -16.75002 | -43.9755 | 2025-10-09 03:32:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 076f0861-4649-3421-a366-3e4ee08fc301 | -15.47592 | -47.96059 | 2025-10-09 03:32:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4e0f89df-d759-3565-b778-8b60f039d3ad | -13.27042 | -42.50189 | 2025-10-09 03:32:00 | NOAA-21 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 25868df0-9274-30e8-927a-1fe25684f93a | -17.95174 | -44.99036 | 2025-10-09 03:32:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 28fc7aca-56c6-3826-900d-c6869ef45a68 | -16.75205 | -43.97229 | 2025-10-09 03:32:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 1854f217-d5ba-3351-b9b0-d1c3fd4db8c4 | -17.98468 | -44.96957 | 2025-10-09 03:32:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c96e32ca-73d9-333a-85e1-7f0be4a2201e | -16.19974 | -42.68152 | 2025-10-09 03:32:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c3c1fd4a-78f8-3b42-9b07-18a216395da0 | -12.2314 | -43.78745 | 2025-10-09 03:32:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 69ca8f13-8f51-3ac7-96f9-e510d5c9b123 | -14.41672 | -43.98239 | 2025-10-09 03:32:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 2bd1b3e0-b541-3018-b3ca-a483f550d054 | -11.87002 | -44.92219 | 2025-10-09 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c730477b-88a8-3bc9-989e-914c4336d349 | -15.29197 | -46.15752 | 2025-10-09 03:32:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| debdcdcb-9ada-319c-91e6-ac1f669cd3ee | -15.47441 | -47.96739 | 2025-10-09 03:32:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| aee104c5-fb12-3d95-a3f9-1c4fb64037fd | -17.89632 | -44.25946 | 2025-10-09 03:32:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c339b48d-447c-3e78-b860-747753905e93 | -16.39568 | -46.36015 | 2025-10-09 03:32:00 | NOAA-21 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ba2d3678-b268-3c99-aec8-02b97b316715 | -17.9792 | -44.96832 | 2025-10-09 03:32:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| cb13d850-7bc2-3911-867e-c2f6aca741ea | -14.96309 | -42.85179 | 2025-10-09 03:32:00 | NOAA-21 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0daf8273-1a62-3a5d-a013-7a97fc270475 | -17.65195 | -44.43153 | 2025-10-09 03:32:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f128bc91-a66c-34cf-bba5-1ac0b266ffbe | -18.05454 | -44.96494 | 2025-10-09 03:32:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 73061652-6c98-3404-9333-c28cbd5ffa42 | -17.39136 | -46.88501 | 2025-10-09 03:32:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5cc46cb4-0057-355d-ae54-77f475aa799a | -18.06703 | -44.47905 | 2025-10-09 03:32:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1bdc4a17-cd13-3b86-a775-0e6a67693064 | -18.06822 | -44.4216 | 2025-10-09 03:32:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0733b117-a1b0-387c-b327-4eaa66d83da9 | -14.44037 | -47.50356 | 2025-10-09 03:32:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 051db80a-0a47-32ea-9493-3eb127e174a9 | -16.28689 | -47.12845 | 2025-10-09 03:32:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2ba24072-bc93-3c6b-af1a-8dd72a64a4c3 | -17.95243 | -44.98577 | 2025-10-09 03:32:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f4e61db9-059e-3013-a66a-809002c7ed1d | -18.29365 | -45.43425 | 2025-10-09 03:32:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ad7213f2-62bf-33a2-8d36-b91fd195afc7 | -13.03441 | -43.90162 | 2025-10-09 03:32:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3e3e62d7-354b-3740-bbf0-1f1186781d3e | -18.02967 | -45.00125 | 2025-10-09 03:32:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3996c76b-777b-3d87-9f24-55e88100471e | -18.03694 | -44.99404 | 2025-10-09 03:32:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cfe8a22c-107f-3a75-9f9d-9e03941dfdda | -15.29865 | -46.17835 | 2025-10-09 03:32:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f96388ff-5872-3133-be8a-a457da4aca15 | -18.03963 | -44.9541 | 2025-10-09 03:32:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0e06b72f-0f35-3594-8598-ec485d67a9dd | -13.78283 | -45.85064 | 2025-10-09 03:32:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| db22deaa-d283-3509-9dbd-3dd22ed4c99e | -17.5295 | -46.75185 | 2025-10-09 03:32:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 735d10b5-efe1-38ed-8787-d111cb777358 | -18.05563 | -44.43678 | 2025-10-09 03:32:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b32b5a18-d304-3371-8483-5a8d0cd3fb97 | -16.70302 | -47.59917 | 2025-10-09 03:32:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7eadab22-5138-3a75-9efd-d39c659c2794 | -18.42057 | -45.23975 | 2025-10-09 03:32:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ab34fb90-68ef-31ca-82fa-ebb7469d3983 | -12.42654 | -45.71302 | 2025-10-09 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 88a1747a-1880-3d35-8b74-7f8c69f3ea8f | -15.29776 | -46.19139 | 2025-10-09 03:32:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c4520f97-acdf-3107-933e-3cc91d1dc664 | -17.96039 | -45.00404 | 2025-10-09 03:32:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7275572a-5a66-3e04-9bf3-dba67bd58841 | -13.82572 | -45.80174 | 2025-10-09 03:32:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bac9c75b-672e-3eaa-8f60-5e09e51b6cd9 | -11.79282 | -45.14706 | 2025-10-09 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4f9a94e0-c665-3f6e-a7d5-20adfd5d0a14 | -17.39253 | -46.87975 | 2025-10-09 03:32:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0bb7df1b-3f1f-342b-aaec-a4990ae1b919 | -17.95793 | -44.98694 | 2025-10-09 03:32:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c50478ca-7418-34aa-8f0c-9344c80790eb | -15.39904 | -48.04726 | 2025-10-09 03:32:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1945f1bb-11a9-3818-abf7-f785bb952f5d | -18.41134 | -45.22869 | 2025-10-09 03:32:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |


[Clique aqui para ver as próximas entradas](README15.md)
