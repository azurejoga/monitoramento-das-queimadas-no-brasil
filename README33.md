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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e3ec5a50-2fd6-3375-9f90-3e944fcba1b6 | -15.36491 | -52.67486 | 2026-08-30 04:17:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 34202477-24b9-3aed-a9cd-4fa697f73dc0 | -16.33572 | -43.44294 | 2026-08-30 04:17:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1a5b4628-a409-30b8-b224-b9ff1390ec04 | -19.15475 | -44.85505 | 2026-08-30 04:17:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1f05c925-04d2-3b0b-9f36-27cab809ffff | -15.13381 | -50.63147 | 2026-08-30 04:17:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| e702d370-d246-346c-848d-04971fc8dbc1 | -14.93542 | -56.34411 | 2026-08-30 04:17:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 99f100e7-d828-3bf7-b5ac-867bf30bc7bb | -14.42983 | -52.56053 | 2026-08-30 04:17:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2bb7db9b-bb3e-32dd-9a1e-dca05d751228 | -14.76828 | -48.73717 | 2026-08-30 04:17:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2d843fc9-1c74-3abb-ab36-dae5560f1a1c | -16.36289 | -51.0088 | 2026-08-30 04:17:00 | NPP-375D | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 007f4724-0841-341b-968f-33ef7eea081d | -17.27835 | -46.00998 | 2026-08-30 04:17:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d6314618-4060-342c-9625-17f1f0e11c0c | -24.28905 | -49.59652 | 2026-08-30 04:17:00 | NPP-375D | JAGUARIAÍVA | PARANÁ | Brasil | 4112009 | 41 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a4da8631-47a4-3589-bdc7-3ce36d297806 | -18.46072 | -44.90297 | 2026-08-30 04:17:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 96023974-da60-3694-b42e-4d3b67d24e40 | -16.35327 | -51.00445 | 2026-08-30 04:17:00 | NPP-375D | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e83c1692-1a95-37ff-8018-f5af8c29a7a1 | -16.36227 | -51.01192 | 2026-08-30 04:17:00 | NPP-375D | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 20.4 |
| d85f8116-48dc-301a-8f52-b43991f6b0f7 | -16.3488 | -51.0006 | 2026-08-30 04:17:00 | NPP-375D | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8998054e-3311-386a-95c9-5a8a7b490e10 | -19.00962 | -47.32365 | 2026-08-30 04:17:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9eef1e9e-9046-3fa0-b1d1-dfcb860c5984 | -14.16271 | -52.81326 | 2026-08-30 04:17:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6448943b-1eab-39ab-9938-5c32740175f0 | -15.36407 | -52.67892 | 2026-08-30 04:17:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8c51f672-9efe-3a9a-8d61-baf128df735c | -17.28926 | -46.01221 | 2026-08-30 04:17:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f6c3acb0-b1ca-391c-8845-0278e12d511b | -20.51389 | -49.0509 | 2026-08-30 04:17:00 | NPP-375D | ALTAIR | SÃO PAULO | Brasil | 3500907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a47bd4ba-758e-3bdb-ae29-4b078d2ca158 | -19.74203 | -48.9712 | 2026-08-30 04:17:00 | NPP-375D | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 95bf2348-5fe0-3aac-81f3-ba47788e4755 | -14.16644 | -52.81132 | 2026-08-30 04:17:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3dcdebb8-b68b-343f-b0b8-2202577feec1 | -14.2435 | -54.64878 | 2026-08-30 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6831765c-6238-3d21-961d-5a04674dc99f | -16.54796 | -49.38552 | 2026-08-30 04:17:00 | NPP-375D | GOIANIRA | GOIÁS | Brasil | 5208806 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5c40ed95-0971-3634-830e-383b8ff91a6b | -14.40612 | -52.55901 | 2026-08-30 04:17:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3a7b228d-52ee-3a52-a020-edcd0ae35f18 | -16.34229 | -50.98077 | 2026-08-30 04:17:00 | NPP-375D | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 205be490-f72c-3f84-9c4e-7874563a17fd | -17.35916 | -39.41162 | 2026-08-30 04:17:00 | NPP-375D | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7592a704-1c9d-3a1e-908f-2af8a97ae896 | -14.03396 | -54.01574 | 2026-08-30 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8ac476b4-b193-3c2f-af62-03c6a6c2a4ba | -16.1418 | -43.04904 | 2026-08-30 04:17:00 | NPP-375D | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d618b675-a9b3-3f89-8fd8-cbbe7b2b957e | -14.76102 | -48.74301 | 2026-08-30 04:17:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e17c4d1b-2eb1-3dd4-882d-19f6fdec0cd0 | -20.55844 | -47.59494 | 2026-08-30 04:17:00 | NPP-375D | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bc05107a-36b0-3690-9967-fc4eb5cc3d73 | -14.67674 | -48.05651 | 2026-08-30 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 71c1ff11-081d-362b-905e-19391fe33f47 | -17.42036 | -42.63137 | 2026-08-30 04:17:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 6245864d-94b6-3086-bffd-5c1f741bc817 | -14.76379 | -48.73642 | 2026-08-30 04:17:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f8addb59-d58c-3e0b-bc7f-e56b01f10553 | -13.39736 | -51.76713 | 2026-08-30 04:17:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 2b5460c5-f6c7-3230-a126-6e85f2e01ba3 | -18.11214 | -42.87598 | 2026-08-30 04:17:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8ca4a726-d4ae-3a38-830d-0acb8306a5fe | -15.1394 | -50.62962 | 2026-08-30 04:17:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8bda8280-930d-3663-9bbf-4898650b24dc | -14.67752 | -48.05243 | 2026-08-30 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e620bed8-b6e1-3728-89a5-1810b785bd39 | -15.13882 | -50.6326 | 2026-08-30 04:17:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 7a7f5bcf-8ad9-3708-a803-7e1e57983563 | -14.76297 | -48.74067 | 2026-08-30 04:17:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a6df4924-9678-3974-8bbd-8db271c12fdf | -17.27665 | -46.04108 | 2026-08-30 04:17:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fd25d2f2-6463-3672-be69-38efff44c8ea | -14.7626 | -48.73448 | 2026-08-30 04:17:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8c60aec1-6c0c-32bf-862b-f2b116d044e5 | -14.14414 | -52.81419 | 2026-08-30 04:17:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9628a6af-bc3e-3862-a6c7-b0946c88963c | -19.1541 | -44.85896 | 2026-08-30 04:17:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 484f2e3a-5c06-357e-8bfb-464f92ef9c99 | -17.28563 | -46.01143 | 2026-08-30 04:17:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f1a703d3-5085-34af-a68e-d1cc74f8e327 | -16.1424 | -43.04539 | 2026-08-30 04:17:00 | NPP-375D | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 20271cec-6e95-37cb-b615-e1b9e3f9601d | -23.21017 | -46.98109 | 2026-08-30 04:19:00 | NPP-375D | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f1d0eb75-3e67-3864-bbf6-3335e4dfc81c | -22.51454 | -46.02808 | 2026-08-30 04:19:00 | NPP-375D | ESTIVA | MINAS GERAIS | Brasil | 3124500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5e3b933e-e172-3368-869e-7881a562923e | -22.90794 | -43.43195 | 2026-08-30 04:19:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| c620ff6a-d054-39a5-bebb-94e2fdb6e902 | -23.2367 | -45.79355 | 2026-08-30 04:19:00 | NPP-375D | SÃO JOSÉ DOS CAMPOS | SÃO PAULO | Brasil | 3549904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f764fc81-55cb-3335-8006-2d590ec7ce4f | -23.03597 | -46.59103 | 2026-08-30 04:19:00 | NPP-375D | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ed01fdc1-6ae5-385e-9d5d-3e8ca7c7ab19 | -23.82503 | -48.72009 | 2026-08-30 04:19:00 | NPP-375D | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e236dac-6621-377b-ab26-7c6ebec0ed75 | -21.17414 | -50.47073 | 2026-08-30 04:19:00 | NPP-375D | ARAÇATUBA | SÃO PAULO | Brasil | 3502804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 976d0cc0-702c-3f39-aff0-d528da47aa6a | -21.17563 | -50.47298 | 2026-08-30 04:19:00 | NPP-375D | ARAÇATUBA | SÃO PAULO | Brasil | 3502804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 20c06080-db09-37de-917a-9c93037996e9 | -22.51385 | -46.03212 | 2026-08-30 04:19:00 | NPP-375D | ESTIVA | MINAS GERAIS | Brasil | 3124500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 54681ee8-ea70-3339-9980-a0ef3190f7f8 | -23.2975 | -45.62201 | 2026-08-30 04:19:00 | NPP-375D | REDENÇÃO DA SERRA | SÃO PAULO | Brasil | 3542305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c35e0b18-9645-3105-935b-9c2f159a773d | -22.2732 | -44.86108 | 2026-08-30 04:19:00 | NPP-375D | ITAMONTE | MINAS GERAIS | Brasil | 3133006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a14b7757-6bdf-3c3f-b4db-e4c779b54dc0 | -22.65237 | -47.66948 | 2026-08-30 04:19:00 | NPP-375D | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 07ad239a-58a3-3fbd-99bf-366dd9f496e7 | -22.9046 | -43.43134 | 2026-08-30 04:19:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| cb4bf818-36e1-34ad-9224-1eab8c23a7cc | -22.12628 | -47.05173 | 2026-08-30 04:19:00 | NPP-375D | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 139b45c8-eafa-3161-941f-295ff1276bc6 | -23.20663 | -46.98038 | 2026-08-30 04:19:00 | NPP-375D | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d7771e2d-4a7a-3682-8ebe-372bfd55de67 | -22.60589 | -46.25443 | 2026-08-30 04:19:00 | NPP-375D | MUNHOZ | MINAS GERAIS | Brasil | 3143807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 916c19de-9cd7-353e-b439-1068e11923bd | -22.92836 | -44.85327 | 2026-08-30 04:19:00 | NPP-375D | CUNHA | SÃO PAULO | Brasil | 3513603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 252ae916-1598-3e8d-a938-810bb808a7ed | -23.48138 | -47.29163 | 2026-08-30 04:19:00 | NPP-375D | ALUMÍNIO | SÃO PAULO | Brasil | 3501152 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ae971b31-4a09-3376-b8e2-9708dfc26a0b | -22.27257 | -44.8649 | 2026-08-30 04:19:00 | NPP-375D | ITAMONTE | MINAS GERAIS | Brasil | 3133006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| c2e8bcda-daae-3d90-84b7-f1702d2d467f | -9.0615 | -65.4169 | 2026-08-30 04:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 86e87879-581b-3a41-8963-33fc075c0c86 | -5.4876 | -57.1416 | 2026-08-30 04:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 49c204ba-2209-3f46-9285-8361852bb065 | -4.9604 | -55.8424 | 2026-08-30 04:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 3449c8a4-4205-3011-8acb-6a2935f63ce2 | -9.8927 | -60.2752 | 2026-08-30 04:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 5e896d11-fccd-3683-b7ed-62993fb3afae | -5.8894 | -57.7708 | 2026-08-30 04:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 7f1708e4-99cf-30ac-819f-8726ec5da915 | -1.3224 | -47.56483 | 2026-08-30 04:29:00 | NOAA-20 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3b3ec1b0-03d8-3460-bacc-e0061871094f | 1.12524 | -50.89468 | 2026-08-30 04:29:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 43fdd6d9-6642-36f4-8e4f-f56a9d934c21 | 1.95892 | -50.99065 | 2026-08-30 04:29:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a08209c8-b9a0-369b-a10b-6d87906dfe69 | 2.23834 | -50.7543 | 2026-08-30 04:29:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f8d3172e-5702-38a7-8a0f-f1c72d888f22 | 2.24264 | -50.75683 | 2026-08-30 04:29:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ca3345e6-d18b-3504-8d41-83ed30b5a04f | 0.01431 | -51.11026 | 2026-08-30 04:29:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec70bfa6-995d-3d2c-98de-53a37729f37a | 2.19111 | -50.7132 | 2026-08-30 04:29:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f00947fa-7650-3d97-b998-6e03d5fe1274 | 2.25211 | -50.75648 | 2026-08-30 04:29:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ded1e3de-3538-38cb-aa61-2716cbd71c94 | 2.5189 | -50.85487 | 2026-08-30 04:29:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ec4a86e4-74a9-317c-9059-e11a7b4ba047 | 2.2339 | -50.75823 | 2026-08-30 04:29:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 46bda573-a2ed-3793-a62d-f75f447e0ef8 | 2.52332 | -50.85418 | 2026-08-30 04:29:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8bf28bc1-90d5-3ee6-bee9-0c7acdd5f9aa | -1.32301 | -47.56105 | 2026-08-30 04:29:00 | NOAA-20 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 72c64668-fb88-35a6-8863-d0ac700fb449 | 2.23898 | -50.75855 | 2026-08-30 04:29:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 35200427-3b0e-3b60-99cf-0112eefb24ad | 1.96379 | -50.98687 | 2026-08-30 04:29:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4448e967-ce40-3ed1-864f-4393e5d1226c | 2.51824 | -50.85054 | 2026-08-30 04:29:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0b2332fe-5762-34b2-bae2-78d3c42ae513 | 1.96004 | -50.99188 | 2026-08-30 04:29:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c3c7598-4c6e-38d2-b057-76f71b953178 | 1.97286 | -50.99286 | 2026-08-30 04:29:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d03161b-ab50-3f0e-945c-cb3640a31af4 | -1.33165 | -47.95793 | 2026-08-30 04:29:00 | NOAA-20 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c27117be-713c-3a83-b90e-1fab6c0c0ec9 | 2.23827 | -50.75754 | 2026-08-30 04:29:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9a92ca07-61c7-3421-aaeb-a3dfe27b6e11 | 2.16983 | -50.69082 | 2026-08-30 04:29:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 71f8634d-f820-38e7-803b-5a0be29ac4a9 | 2.19547 | -50.71252 | 2026-08-30 04:29:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ac0d38bd-8190-3ee8-9f88-96273ee51d9a | -4.9604 | -55.8424 | 2026-08-30 04:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |
| a53c4088-4942-34cc-8762-1a99e9545fc5 | -5.4876 | -57.1416 | 2026-08-30 04:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 7a5797be-0f77-3fca-9576-ed8872de1f84 | -9.8927 | -60.2752 | 2026-08-30 04:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 6b3ef921-dbfd-3e89-92a9-de936fbb2ea4 | -5.8894 | -57.7708 | 2026-08-30 04:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 8df6d4a3-8365-3b42-83ce-80744e0872ed | -5.63923 | -44.97639 | 2026-08-30 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2b4e2eee-48cf-3b43-a1cd-0dc7cce0fa7b | -6.87448 | -41.65981 | 2026-08-30 04:32:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 78396156-5078-31b6-a6f4-886c1f796446 | -6.82598 | -42.87684 | 2026-08-30 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 83136c08-6530-39dd-89cd-3e060823f3a0 | -5.99603 | -45.08655 | 2026-08-30 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e4df9f6-1aed-3b02-84b3-745eabea03a0 | -7.99455 | -46.50357 | 2026-08-30 04:32:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f8deeb92-6b0e-3b26-a9b2-385d8fe14951 | -6.07292 | -57.89219 | 2026-08-30 04:32:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README34.md)
