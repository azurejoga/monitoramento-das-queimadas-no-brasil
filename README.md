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
| 550af704-0ee9-3352-9947-405f91e963c0 | -5.6105 | -36.7969 | 2026-02-01 00:00:00 | GOES-19 | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 76.1 |
| f462fb88-364a-3d85-b7b7-90b9fe6d3a84 | -5.6105 | -36.7969 | 2026-02-01 00:20:00 | GOES-19 | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 71.9 |
| ce97d529-0310-3ca7-9d65-a50920a49588 | 3.25802 | -61.02805 | 2026-02-01 01:32:00 | TERRA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 17609745-09bb-315b-bf58-2f3bbad4483b | -9.23514 | -36.88905 | 2026-02-01 03:04:00 | NPP-375D | IATI | PERNAMBUCO | Brasil | 2606507 | 26 | 33 | nan | nan | nan | Caatinga | 7.1 |
| c1974025-c9eb-33d0-8eee-a78bc7a46f40 | -9.24159 | -36.88987 | 2026-02-01 03:04:00 | NPP-375D | IATI | PERNAMBUCO | Brasil | 2606507 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| baaf3d3c-0b2e-3c4b-ac7f-b49bb03ea863 | -12.05398 | -38.01517 | 2026-02-01 03:06:00 | NPP-375D | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| c6cda87a-2e85-3e9f-ad7a-c233428b6911 | -12.04745 | -38.01405 | 2026-02-01 03:06:00 | NPP-375D | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 373f10b2-60e2-34c4-9164-c69f6e65e290 | -5.24644 | -37.50116 | 2026-02-01 03:23:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 82913977-4aa7-3e51-9d80-2a9bbad33ce1 | -5.35858 | -38.59249 | 2026-02-01 03:23:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 048d87d0-7c7e-3959-bfe9-36b01b4760c8 | -6.23446 | -35.54472 | 2026-02-01 03:23:00 | NOAA-20 | SERRINHA | RIO GRANDE DO NORTE | Brasil | 2413508 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 87b9377b-264a-337b-80e1-400adfcafa5b | -8.92324 | -36.50864 | 2026-02-01 03:25:00 | NOAA-20 | GARANHUNS | PERNAMBUCO | Brasil | 2606002 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 88d7d9e4-ff33-3861-9889-9969ff667361 | -10.14033 | -36.20761 | 2026-02-01 03:25:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 8255830e-8bc1-320f-8a6a-58b3be69d1f9 | -9.2364 | -36.88938 | 2026-02-01 03:25:00 | NOAA-20 | IATI | PERNAMBUCO | Brasil | 2606507 | 26 | 33 | nan | nan | nan | Caatinga | 7.8 |
| a7c8f385-ff73-36d0-809e-69238cb5344a | -8.97767 | -35.56511 | 2026-02-01 03:25:00 | NOAA-20 | JUNDIÁ | ALAGOAS | Brasil | 2703908 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f5746dda-a7c7-3d04-96c9-ccdb2d5e5665 | -9.47471 | -35.90962 | 2026-02-01 03:25:00 | NOAA-20 | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| af6d6fa6-c505-34ba-a9b9-da491b4eee73 | -8.86632 | -36.89392 | 2026-02-01 03:25:00 | NOAA-20 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| b4a3d819-1cf3-3f93-8d9f-3449f7cef31d | -9.31805 | -35.79092 | 2026-02-01 03:25:00 | NOAA-20 | MESSIAS | ALAGOAS | Brasil | 2705200 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 50bec562-7f5c-3af8-9fb3-294631a92321 | -9.23707 | -36.88554 | 2026-02-01 03:25:00 | NOAA-20 | IATI | PERNAMBUCO | Brasil | 2606507 | 26 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 89aed488-49c1-3b04-9b8e-7d0eb6f38cce | -10.76853 | -37.14368 | 2026-02-01 03:25:00 | NOAA-20 | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b058a25a-afdf-3dec-adbe-437988830e63 | -9.54578 | -35.8244 | 2026-02-01 03:25:00 | NOAA-20 | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 32.2 |
| 67296d65-212f-3b35-8f7a-3973f3b7722a | -11.31135 | -37.8676 | 2026-02-01 03:25:00 | NOAA-20 | TOMAR DO GERU | SERGIPE | Brasil | 2807501 | 28 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d5bd22d3-f929-3044-81aa-9e3e999e5ddf | -12.04761 | -38.01301 | 2026-02-01 03:25:00 | NOAA-20 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bef91fbe-67ac-3708-9952-b463c56af0dd | -9.47861 | -35.9104 | 2026-02-01 03:25:00 | NOAA-20 | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9b676a2b-ea41-359e-b8c9-6b90b3cd84aa | -9.54493 | -35.8294 | 2026-02-01 03:25:00 | NOAA-20 | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| a3701c7a-2581-30a9-9bbf-2b356408feb6 | -12.05192 | -38.01374 | 2026-02-01 03:25:00 | NOAA-20 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| a3696a75-d0b8-3130-988c-655ddde4021d | -11.04347 | -38.35387 | 2026-02-01 03:25:00 | NOAA-20 | RIBEIRA DO AMPARO | BAHIA | Brasil | 2926509 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| f0d58d67-dad7-3332-9852-62505182cc03 | -22.89573 | -43.65703 | 2026-02-01 03:29:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 41d7b2af-7741-3455-bd64-7dd07bed8156 | -22.89504 | -43.66027 | 2026-02-01 03:29:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 21ded9f3-e121-3d1d-b133-d112e1c720a4 | -9.5544 | -35.8115 | 2026-02-01 03:30:00 | GOES-19 | SATUBA | ALAGOAS | Brasil | 2708907 | 27 | 33 | nan | nan | nan | Mata Atlântica | 75.2 |
| e3098993-0063-325d-9704-f2c5d67cbef0 | -9.8666 | -36.6203 | 2026-02-01 03:40:00 | GOES-19 | FEIRA GRANDE | ALAGOAS | Brasil | 2702603 | 27 | 33 | nan | nan | nan | Mata Atlântica | 88.9 |
| 48b888c4-6b3e-3fb1-b900-78ca276dcf82 | -4.25918 | -48.83415 | 2026-02-01 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c5efdd1e-3ec8-3d0f-bbb2-06f29a23e719 | -5.56849 | -46.32785 | 2026-02-01 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5145e88c-1e74-3cb4-afba-902f66f6293a | -4.09928 | -47.73647 | 2026-02-01 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f82a1cc6-cdb0-395f-822e-07570cb2c268 | -4.73293 | -48.95749 | 2026-02-01 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e026456-83c0-34eb-8aa0-bb4c90e64978 | -5.89136 | -35.61232 | 2026-02-01 04:14:00 | NOAA-21 | SÃO PEDRO | RIO GRANDE DO NORTE | Brasil | 2412708 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0c2bf508-d4d3-395f-b8fc-998be9e8ff8d | -5.1688 | -39.89433 | 2026-02-01 04:14:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 520179d8-468a-3b35-8a14-ffc2fd2217d7 | -2.42863 | -49.03088 | 2026-02-01 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c34160f5-2947-389d-99eb-eb6a220f2ab8 | -5.24953 | -37.49894 | 2026-02-01 04:14:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 122ebdfd-77bd-3584-9a3d-965542999bac | -5.35951 | -38.59094 | 2026-02-01 04:14:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 227d3db9-cb84-312b-b480-49c308adf598 | -6.36153 | -39.08532 | 2026-02-01 04:14:00 | NOAA-21 | ORÓS | CEARÁ | Brasil | 2309508 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bc07ea90-8e92-307b-b600-48cbb30d652f | -2.26198 | -47.86877 | 2026-02-01 04:14:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1b94fd5c-e90c-31af-8f33-db5ca548788c | -2.44646 | -47.07983 | 2026-02-01 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 809ed061-8d37-3b50-8781-c9ac1af25f87 | -3.01519 | -43.21314 | 2026-02-01 04:14:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4bc2a81d-8d28-3b18-98cc-3b17c50dcd72 | -2.02811 | -47.8948 | 2026-02-01 04:14:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4bd5f73b-6784-34ee-9fbd-994ad5f28922 | -4.09933 | -47.28715 | 2026-02-01 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 01254a0a-1eeb-3d4a-abec-819bccca2252 | -4.47594 | -40.42724 | 2026-02-01 04:14:00 | NOAA-21 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3be4ce3e-8ce0-3175-8a07-eef891b67fa7 | -4.09959 | -47.29017 | 2026-02-01 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e4b3499-753b-3807-8c09-5268fd2ab8b6 | -6.23444 | -35.5446 | 2026-02-01 04:14:00 | NOAA-21 | SERRINHA | RIO GRANDE DO NORTE | Brasil | 2413508 | 24 | 33 | nan | nan | nan | Caatinga | 2.2 |
| df68aecd-8243-3a66-9e35-a911c52fa30b | -5.37569 | -43.0715 | 2026-02-01 04:14:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 16a80cac-38e3-3aab-87a5-865480e175db | -5.74435 | -39.77412 | 2026-02-01 04:14:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 262f7a66-27d4-3d66-8210-e2c965b36a0f | -4.09568 | -47.28957 | 2026-02-01 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17178d69-37a2-3047-a968-21b53f77950a | -5.98624 | -45.73929 | 2026-02-01 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 814ec4bc-ff5b-3171-9285-7b37ad940ece | -3.71656 | -42.34515 | 2026-02-01 04:14:00 | NOAA-21 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 67972e9c-084f-39a2-b295-7156daa35279 | -5.65045 | -44.07008 | 2026-02-01 04:14:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9a004193-9972-301f-948d-c8b1b7c16e73 | -4.30629 | -39.15166 | 2026-02-01 04:14:00 | NOAA-21 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 39e4c141-4646-3c54-8d74-c871abb7df1b | -1.50816 | -47.33045 | 2026-02-01 04:14:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9049768c-9782-3b6b-aa90-b9772a9fb27d | -2.95671 | -40.49435 | 2026-02-01 04:14:00 | NOAA-21 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 95cc5880-df44-35e8-91cd-3e2b7d23e1e1 | -3.88731 | -42.51656 | 2026-02-01 04:14:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fd368e46-5aea-3620-8820-71c1bce32a22 | -5.07839 | -42.05544 | 2026-02-01 04:14:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7aa9e7f2-774c-3958-b917-c0b4f49532b7 | -3.26598 | -42.54832 | 2026-02-01 04:14:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b78bc932-9781-3151-b717-ea0b2f0b52c0 | -4.39633 | -48.11993 | 2026-02-01 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c7490bba-cdbb-3a74-8798-9f30367ac6d7 | -5.98504 | -45.73979 | 2026-02-01 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d19c5128-ed10-382e-95cc-9727a2e46899 | -5.37845 | -43.07545 | 2026-02-01 04:14:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a9f05b08-6a42-325e-b854-ecb1c62a55df | -2.42413 | -49.03022 | 2026-02-01 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cd3254d4-e9ea-3cfa-a347-d939da3d8083 | -5.36073 | -38.59293 | 2026-02-01 04:14:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 759b170d-0951-3f95-b148-c35e5c1ca407 | -5.37899 | -43.07201 | 2026-02-01 04:14:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a23dcc4c-24cc-31db-b9d8-9bb2719039f1 | -4.14855 | -44.18447 | 2026-02-01 04:14:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f7377772-c9aa-3ead-bd83-b24809623f95 | -5.39706 | -46.53282 | 2026-02-01 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5ad02a0b-23fb-31bd-9305-022e0b775b62 | -2.26259 | -47.86495 | 2026-02-01 04:14:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 527ea9ea-923b-3150-848e-216aeac0aa01 | -12.05062 | -38.01358 | 2026-02-01 04:16:00 | NOAA-21 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| e22a0ba9-13c9-3a60-9e32-2b6ece8eafbe | -10.42438 | -44.81337 | 2026-02-01 04:16:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5d4df922-b779-33c1-9c27-4afdcf625eb4 | -8.43246 | -48.04582 | 2026-02-01 04:16:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a37a684e-b9ca-3e23-a540-3c4e84281614 | -9.23761 | -36.88497 | 2026-02-01 04:16:00 | NOAA-21 | IATI | PERNAMBUCO | Brasil | 2606507 | 26 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 5d534413-a286-3f19-aa6f-a026ad59f89a | -9.31922 | -35.79233 | 2026-02-01 04:16:00 | NOAA-21 | MESSIAS | ALAGOAS | Brasil | 2705200 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 7ea59bcd-3f0c-3f5f-81c9-e38701d8b02c | -12.05504 | -38.01428 | 2026-02-01 04:16:00 | NOAA-21 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 827cda2a-1879-3b02-86b2-073e47866e67 | -10.47073 | -40.55197 | 2026-02-01 04:16:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 7e92e3ba-74a7-30fa-b575-a4d2f6421126 | -9.40944 | -44.53709 | 2026-02-01 04:16:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b9d40d9b-8cd2-3124-8c6b-3f0e4540be58 | -7.00546 | -45.85435 | 2026-02-01 04:16:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 07101ef3-723f-371e-9b88-be039f3bbb67 | -7.90368 | -50.37349 | 2026-02-01 04:16:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b7f7ef00-0c23-3b9d-93c6-3aeeff9fe947 | -7.86125 | -45.97357 | 2026-02-01 04:16:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a111c592-4e5d-32c3-8912-ac6053b6aa91 | -11.04465 | -38.354 | 2026-02-01 04:16:00 | NOAA-21 | RIBEIRA DO AMPARO | BAHIA | Brasil | 2926509 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0dbcc127-6094-3677-b4c7-3d543424d728 | -7.86472 | -45.97413 | 2026-02-01 04:16:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 96732e87-2690-3e6e-82db-0ccdb63569dd | -8.72658 | -48.32867 | 2026-02-01 04:16:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f2f3a168-d9a1-3d90-b79f-bcb0aeb2ef41 | -10.77035 | -37.14162 | 2026-02-01 04:16:00 | NOAA-21 | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 4aa2440a-8d04-3130-bb8b-6b14597ad26d | -8.43058 | -48.04295 | 2026-02-01 04:16:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c8bdb631-7ecd-3aa1-87e8-d79140662347 | -9.23694 | -36.88982 | 2026-02-01 04:16:00 | NOAA-21 | IATI | PERNAMBUCO | Brasil | 2606507 | 26 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 9ea6ff2f-7946-3292-8ec0-2a352ff345dd | -8.43138 | -48.03814 | 2026-02-01 04:16:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e6c6f603-cb6d-30de-826e-8b4eb713fb73 | -11.31166 | -37.86707 | 2026-02-01 04:16:00 | NOAA-21 | TOMAR DO GERU | SERGIPE | Brasil | 2807501 | 28 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 80e7d047-c4e7-3424-8c62-0dd04416f16d | -8.43329 | -48.041 | 2026-02-01 04:16:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9c61bebf-584f-3c49-9693-7cb24b3fbe0d | -18.81248 | -51.60129 | 2026-02-01 04:18:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| adfc184c-3c09-300e-bdd5-6853599769b5 | -23.55682 | -49.23604 | 2026-02-01 04:21:00 | NOAA-21 | TAQUARITUBA | SÃO PAULO | Brasil | 3553807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7c848dbf-52ff-36b0-9e6a-3795ad9318e0 | -26.01963 | -52.70221 | 2026-02-01 04:21:00 | NOAA-21 | PATO BRANCO | PARANÁ | Brasil | 4118501 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| ea9aa5d4-5e2a-3892-8b44-2da3233b9fe5 | -23.37566 | -46.02827 | 2026-02-01 04:21:00 | NOAA-21 | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5d6d3a9c-59d7-3c43-bfcf-442f0997b977 | -21.51789 | -49.13251 | 2026-02-01 04:21:00 | NOAA-21 | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| bdb17246-05d3-3c1f-bd97-6843cb3744c9 | -21.15797 | -46.92522 | 2026-02-01 04:21:00 | NOAA-21 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 94796765-0fee-327a-8991-671cdb5ca8ac | -23.5575 | -49.23206 | 2026-02-01 04:21:00 | NOAA-21 | TAQUARITUBA | SÃO PAULO | Brasil | 3553807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| da2acc49-8c3c-3a93-8d6c-9bfaa3fc86d7 | -26.0158 | -52.70142 | 2026-02-01 04:21:00 | NOAA-21 | PATO BRANCO | PARANÁ | Brasil | 4118501 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 63c6053d-c21a-3ad6-a382-4b7df9ad4f8a | -24.12664 | -46.70902 | 2026-02-01 04:21:00 | NOAA-21 | MONGAGUÁ | SÃO PAULO | Brasil | 3531100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6c09890e-d055-3a2e-8f1f-70be4dc7c302 | -20.2323 | -50.9584 | 2026-02-01 04:21:00 | NOAA-21 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 60856b97-f629-3260-9248-9e67c013b56b | -23.51453 | -46.57576 | 2026-02-01 04:21:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |


[Clique aqui para ver as próximas entradas](README2.md)
