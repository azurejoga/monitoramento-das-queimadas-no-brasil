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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b839295f-e3e1-3c84-9c96-6b0912d6c48a | -8.62765 | -67.05685 | 2026-10-07 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7b231560-6f4c-3509-a05a-4a19a388cc16 | -8.5414 | -55.37875 | 2026-10-07 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dcf3871b-1ed6-3c49-a734-f80b19d3a4ac | -11.36688 | -46.69532 | 2026-10-07 05:06:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d6fc54da-f84d-3ecf-bdd4-09f832110300 | -9.05637 | -65.48808 | 2026-10-07 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f82919af-6cec-303d-ad75-b26b3cc6356a | -10.85151 | -50.6614 | 2026-10-07 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6c5dfd05-0c93-3d84-957d-c610652443cc | -13.00642 | -46.00137 | 2026-10-07 05:06:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 757b91c6-b286-3451-b5ec-ea07cde430df | -8.28035 | -50.26888 | 2026-10-07 05:06:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 857e6d7e-2954-3263-814a-19887f0bb6b3 | -12.16782 | -44.7093 | 2026-10-07 05:06:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 01f6865c-f620-3f5b-88a2-fb6732b77cd6 | -8.63328 | -67.05701 | 2026-10-07 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 63b2c3be-bddb-3958-90a8-53b726ba5a20 | -11.23901 | -44.87366 | 2026-10-07 05:06:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 5bca5566-203a-3739-8102-d0034f445c5a | -8.97764 | -65.44374 | 2026-10-07 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b34ae771-d930-3ed1-a76a-0efed892d365 | -11.23258 | -44.87261 | 2026-10-07 05:06:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 7970d466-15dc-3de2-8033-cc33ed0327ec | -12.17249 | -44.72729 | 2026-10-07 05:06:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6f5a52a2-d528-3234-9323-620059a719de | -10.49084 | -50.43711 | 2026-10-07 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a6dc96df-fd80-37b1-b800-d7857db5cc5b | -10.27916 | -60.54454 | 2026-10-07 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fbf29520-61f4-3656-9916-09f5c49d5ea8 | -7.7501 | -54.95078 | 2026-10-07 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 03c0ad00-ba28-3ff9-9011-42da6a063554 | -9.44176 | -67.09526 | 2026-10-07 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 22f9fe54-c721-341b-a53a-56cc38465a50 | -11.67642 | -43.62291 | 2026-10-07 05:06:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f71580e8-a172-395c-8f91-f817741945a2 | -9.03642 | -65.74524 | 2026-10-07 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 604e9405-8547-3e43-a78b-267d00eed688 | -9.13886 | -65.29693 | 2026-10-07 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6372902a-dd2e-33fe-a3cc-8e0b5894c676 | -10.97352 | -45.40767 | 2026-10-07 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2501903f-efa3-3071-b9d7-88565233ea81 | -9.11254 | -67.83266 | 2026-10-07 05:06:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 878243e7-e845-3835-bfbe-002b2f504667 | -8.97821 | -65.44057 | 2026-10-07 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| deafc33d-d6fd-37d7-98a4-e7cb8a8389cc | -11.07736 | -45.64438 | 2026-10-07 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c579309b-e850-3530-b404-8e4dd72f4333 | -8.74576 | -47.87831 | 2026-10-07 05:06:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5f1bcfe5-ce16-35f2-b9be-80cf7bb47833 | -9.14398 | -65.29782 | 2026-10-07 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9f323274-93be-31c1-99be-382650d5e57b | -11.74657 | -44.9411 | 2026-10-07 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d27604c1-8504-3839-82bd-b9eb48ceb488 | -7.59027 | -55.72574 | 2026-10-07 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 626a6f82-72c1-3cde-ba77-8c10a3acc091 | -9.54929 | -64.82047 | 2026-10-07 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 605f4559-5f59-32c8-b4fa-f7a0a8eba4f7 | -8.28468 | -50.26951 | 2026-10-07 05:06:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 0faf7748-9b0a-3124-9771-c9be31f23beb | -11.23875 | -44.86845 | 2026-10-07 05:06:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 400c198f-8ee0-3b9d-a1c3-4aff30639a2d | -11.23959 | -44.86842 | 2026-10-07 05:06:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 19.2 |
| fd00e0f5-a002-3232-89ca-ebd13207db59 | -13.63705 | -44.42153 | 2026-10-07 05:06:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b3d09215-3dd6-3ab8-ac27-f6385ac4d23b | -11.226 | -45.27475 | 2026-10-07 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9617c5a1-6752-3ad5-aa5d-a72be952319d | -11.05514 | -49.57286 | 2026-10-07 05:06:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e37e3b61-04f0-3c3a-9397-187a8cdefaf5 | -12.88587 | -61.71896 | 2026-10-07 05:08:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 28465af6-8c31-39ae-b3a4-708260b255da | -16.18832 | -45.35479 | 2026-10-07 05:08:00 | NOAA-21 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 9461a043-df15-386f-a1b9-4b4ac6ce5e16 | -16.19494 | -45.35562 | 2026-10-07 05:08:00 | NOAA-21 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e01798e3-f155-30e8-9d8b-dd39cc326a11 | -18.4195 | -45.1112 | 2026-10-07 05:08:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9dbe6e51-6fd5-3394-b60f-f374ad04d1dd | -14.36961 | -55.03345 | 2026-10-07 05:08:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| adb2bdac-b270-3e42-8d3d-13799b00df9e | 4.28145 | -60.14558 | 2026-10-07 05:38:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9e24bb7-6626-3f72-a815-bc415f6e6719 | 3.52935 | -51.27475 | 2026-10-07 05:38:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a4e0908-58f8-3b25-838d-6371e312e7ce | 3.51704 | -51.26436 | 2026-10-07 05:38:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 11c22d5e-22dc-387c-9e52-f2bd724c2a84 | 3.51755 | -51.26739 | 2026-10-07 05:38:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2bdb9d14-ca1c-3c1a-9570-b2b247a78b0c | 4.282 | -60.14906 | 2026-10-07 05:38:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64b369bd-049d-3492-b15f-4cc5b73c8f82 | 3.52884 | -51.27173 | 2026-10-07 05:38:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a787cdc-3db2-37df-be40-b55828721eb9 | 3.5119 | -51.26523 | 2026-10-07 05:38:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b1c1943d-39f7-34cf-8b9d-b9261be83328 | 3.52986 | -51.27778 | 2026-10-07 05:38:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b0ccf2e-7c32-3f23-8104-f56de00fc64e | 3.52319 | -51.26955 | 2026-10-07 05:38:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a818d1bb-55fb-38bb-ad7b-6875892e473b | 3.52371 | -51.27258 | 2026-10-07 05:38:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 177b2918-8c73-34a4-9962-ffafa340a154 | -3.73906 | -59.44368 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 91d6f0f4-f0e1-3bd3-80f4-773aaadf1324 | -2.97301 | -54.12905 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 50a1f33e-9135-3e80-8a80-646988bd1119 | -3.50439 | -54.66087 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1d6e8c7b-7e37-3e9d-bdc6-d053fc7c3790 | -3.01492 | -57.73702 | 2026-10-07 05:40:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1c474fb3-a8a9-3d41-a107-d606758c3201 | -3.11385 | -53.78081 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 97b9946b-8577-3f84-9f43-4a680cecdf0b | -3.18924 | -50.56831 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 3552c2c1-1ee6-347e-a716-c1c577722cf8 | -3.01189 | -54.12551 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 40f82b4d-b7ea-3864-82dd-1edd7c21e49c | -3.55186 | -59.48409 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 86cea66c-2f54-36b4-9041-dd5f1f7dfee9 | 0.94156 | -50.1978 | 2026-10-07 05:40:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9c81d7a4-10d4-3d3f-b6eb-69708b7c854e | 1.70624 | -55.63123 | 2026-10-07 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 193c81f7-cba4-3cb8-adfd-33f363597c6b | -1.12218 | -54.11567 | 2026-10-07 05:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c63bbb53-49c4-3305-b749-f46af9219b00 | -3.15627 | -50.44446 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 494f3719-11da-3ef8-b7d9-b1928a157df0 | -3.79575 | -58.29305 | 2026-10-07 05:40:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef329b90-eec5-3c87-ac37-4e07b7edd182 | -3.27645 | -53.8625 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df902567-f6a3-35d2-915c-d01ccd3adf10 | 2.4353 | -50.83633 | 2026-10-07 05:40:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9880acb9-5da5-3e93-b77d-a848345dc277 | 2.1235 | -50.83102 | 2026-10-07 05:40:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3e9423c1-98f4-3ae9-9161-7e7fe6613350 | -3.03037 | -53.90952 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ea54e6f1-e942-3f59-8202-f71ed4abbad7 | -2.95675 | -54.14172 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d0022484-dcba-3963-95e3-c1e2cf6a1c48 | -3.92789 | -56.06325 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6ea83ff-75bf-3ca1-82e5-cb92b78ea8ed | -3.52047 | -58.75461 | 2026-10-07 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16f3eb91-b15b-3789-a166-2d3eb951b3e5 | -3.54397 | -54.64541 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 940819a4-a244-3109-a106-6b99236ed24c | -3.2737 | -50.4144 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a8d727af-6a2f-38fd-9766-00322981e8ac | -2.10728 | -52.06491 | 2026-10-07 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f1568a97-e9ab-3abb-9334-aca28dea6383 | -3.17184 | -57.54666 | 2026-10-07 05:40:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 195d168a-47d0-35b4-bb61-3e8f1dcf1f57 | 2.44247 | -50.82769 | 2026-10-07 05:40:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 627a7985-9c71-380c-b216-65b680a8e241 | -2.95246 | -54.10628 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fbf45d8f-6964-3cb4-94d5-b79aeb15d36f | -3.26945 | -54.00875 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 715755ba-19e3-324a-af46-e73b27a20f3a | -3.58927 | -54.56233 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a8b10c74-9b0e-3958-a33d-eb976416f8d5 | -3.07879 | -54.26746 | 2026-10-07 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c5fd63a7-7064-35b0-9d3e-281b949314f6 | -3.28633 | -54.05066 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| abdae05b-d914-31ba-bdda-5509b36b984b | -1.50575 | -54.82857 | 2026-10-07 05:40:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c8a23108-f1ff-3f0a-828a-f6b61c467f27 | -3.64584 | -55.27829 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e31e9e7-c6e0-32e7-906d-98ecd2e350e7 | -3.67872 | -59.63255 | 2026-10-07 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c1b6baeb-332d-3c5f-8b0c-2247964da64c | -3.05956 | -54.20552 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7124b66d-7969-3c51-86cf-e2070b0da68d | -3.81103 | -51.04121 | 2026-10-07 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4f9f0e03-bfd0-3ec9-9372-a69cb61f59f3 | -2.93957 | -54.11781 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7bdeefd2-e5fe-39df-a955-6f5f0e9b9d2e | -3.48148 | -59.46605 | 2026-10-07 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6bd10e81-32e0-3059-a39c-b524ed04631f | -3.48255 | -55.43398 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e7728eea-19d1-3c8c-a18f-9a378164a86d | -2.91766 | -54.10452 | 2026-10-07 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3de9c1bb-a932-31d4-8551-3be78f784658 | -3.97286 | -55.82291 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a8d62835-b15f-3975-8fe5-85198c5a454d | -2.77301 | -54.0955 | 2026-10-07 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f0008b1b-5932-33d0-8bc7-95993f67eb55 | -3.52227 | -54.66593 | 2026-10-07 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 0602d969-bb2c-366c-9811-b8799853f62b | -2.98478 | -54.05089 | 2026-10-07 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 802f5c7a-fe9c-3aa4-b431-9ec3c0dfe01f | -3.73392 | -55.98043 | 2026-10-07 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e30cdc36-1c0a-3366-a66b-22a51e4acc27 | -2.85686 | -59.108 | 2026-10-07 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b0bc5dab-895d-321c-9008-7ac37b17bf4f | -4.13515 | -54.90641 | 2026-10-07 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5796aa4d-e3b8-3030-9b65-82439c7221cf | -2.70289 | -59.80065 | 2026-10-07 05:40:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d28fb4f4-9550-3a8f-ac1f-b018af31fdd0 | -3.28312 | -50.14464 | 2026-10-07 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| fc7482b1-e51e-33ff-9f83-6db49d719361 | -3.54062 | -50.09464 | 2026-10-07 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| aca7eece-c7a0-3336-8306-255368a12ab2 | -3.17554 | -58.63635 | 2026-10-07 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README96.md)
