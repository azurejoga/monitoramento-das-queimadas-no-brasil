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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d1e22927-2b53-3abc-b2e0-5c4b1cfa419e | -8.90725 | -62.44014 | 2025-08-25 04:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a6c715a8-3867-31d8-8d34-423d17a3b132 | -6.8221 | -58.95216 | 2025-08-25 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f7bc0a44-508a-342c-b073-d6a59c056ec1 | -9.19584 | -59.45725 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a7b70de5-afda-3ae1-8b19-6fc6c5f4d475 | -8.06337 | -49.68796 | 2025-08-25 04:42:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 3278ec34-ab40-3761-a07c-ab256a1d3b35 | -11.86337 | -45.11906 | 2025-08-25 04:42:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 05433a63-7502-3817-9b50-f4530760c1a8 | -11.61979 | -46.24069 | 2025-08-25 04:42:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 32d46699-4a4d-397b-b064-b69c393043ec | -9.15767 | -59.51205 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d6ce3498-b430-3582-bc71-c55a8113af6d | -9.16612 | -59.46611 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5640a179-9e80-3234-9c5d-427b3179e28c | -8.54473 | -48.85897 | 2025-08-25 04:42:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d568e477-654e-3ea8-9584-8b366da7701c | -13.40316 | -51.78942 | 2025-08-25 04:42:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2a9c0a62-fa09-3900-ab80-bed969fde1e9 | -9.1687 | -59.45208 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 6a31eca5-b7b9-389f-b0ff-af69435857ea | -9.20256 | -59.5169 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dab52d73-660d-37a0-bbbe-1e6d9d1cc2e3 | -8.06115 | -49.68046 | 2025-08-25 04:42:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c8e98539-68e5-36be-9593-ec21a27c2d4b | -9.20561 | -59.44111 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ad7761d9-3629-3b5e-badd-bc7b1bfc19d0 | -9.54833 | -48.13755 | 2025-08-25 04:42:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 68b3edf1-de54-3d3b-8c97-879635135c9a | -9.70802 | -54.98877 | 2025-08-25 04:42:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b3b234e2-4dc2-39b7-a881-f0fd9ad35f27 | -10.71646 | -47.3311 | 2025-08-25 04:42:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a6e8b457-7c95-31ae-b6d1-b762777e77bc | -10.26068 | -59.10342 | 2025-08-25 04:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a8bc265-3c64-3a44-9100-13710677a422 | -11.18301 | -55.02231 | 2025-08-25 04:42:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 588af7fd-e2ff-3e9c-bfd3-80048fea0849 | -6.68555 | -58.8618 | 2025-08-25 04:42:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5708d444-348c-3059-904e-86eee15bc02c | -13.05457 | -46.31596 | 2025-08-25 04:42:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 51884ed9-b77f-323e-822e-bc41c0dbc5e6 | -8.06225 | -49.6735 | 2025-08-25 04:42:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4a340ae-33a8-3544-9732-d340784c139b | -9.22107 | -60.93486 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 19fe9a82-c0f6-3430-8ff6-0b44486ce262 | -13.50678 | -46.89725 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e0928725-4032-333e-b563-1c54936a792c | -11.6327 | -46.23276 | 2025-08-25 04:42:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f16dc120-13a9-3a59-bb59-e54065ca1ba2 | -11.17258 | -55.03614 | 2025-08-25 04:42:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb726c73-b7db-39a2-b8c1-8730f09a2037 | -12.75522 | -48.11478 | 2025-08-25 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| be4a28b0-9ff4-39bd-8ba6-ddccff04e192 | -9.18993 | -59.61394 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2f7b541-8f2d-3153-8c83-77518804eb52 | -6.79575 | -58.62901 | 2025-08-25 04:42:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4ac31548-11ec-3402-8acc-b849a6a41913 | -11.18379 | -55.03551 | 2025-08-25 04:42:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a818f7e-da76-3551-8704-738007ad0e88 | -8.80339 | -45.47265 | 2025-08-25 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e428f33f-b36a-36e4-a6a8-9b512c8ad1d3 | -11.14784 | -44.79993 | 2025-08-25 04:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f96d4010-9202-3ee9-bd8c-c57e9073708a | -6.83369 | -58.95053 | 2025-08-25 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5aca4446-4d0e-3982-b4ac-c8074787d49c | -12.74766 | -48.14177 | 2025-08-25 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cf49a22d-19c5-3438-b10c-e2e4834f6edc | -9.192 | -59.47836 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 74ec8f02-2949-3909-880c-e4aaf45c7021 | -13.4992 | -46.89603 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4efe8ad3-2c92-3a24-b7f5-71692cecdf7b | -13.43714 | -46.90056 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 38bfba9c-215f-310e-8edd-d7166c1f5f55 | -9.19967 | -59.49813 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7953b797-7349-3c98-9efc-3327d4e324fd | -10.72127 | -47.12029 | 2025-08-25 04:42:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 02843d8e-d00d-3259-8e96-1310ad2bad39 | -13.47885 | -47.01264 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a88576b2-ace9-3716-a0da-faf4c3a65f4d | -8.58677 | -62.63503 | 2025-08-25 04:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6940d859-fd0b-3287-b112-383ee716df6f | -9.20443 | -59.4409 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b2e79eb9-40fb-37f8-90b6-4032a5c4fc80 | -8.6082 | -62.59665 | 2025-08-25 04:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 633ada42-31da-3178-bd9e-330718324d65 | -9.20111 | -59.49468 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 869838c6-e0ab-3131-a86a-47e5669bb37f | -8.12787 | -47.13199 | 2025-08-25 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6023d01e-3ab3-32bd-b9ae-7aa7be5648cc | -9.52299 | -60.52933 | 2025-08-25 04:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 60d7de80-7f60-3f37-97d0-5f69e5778ffd | -9.13873 | -60.73595 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ffeee2de-0c52-3271-b63e-d3a18e39a84a | -13.44291 | -47.02202 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 19e0eed0-9fbd-3740-be3c-870281dac490 | -6.82822 | -58.94958 | 2025-08-25 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 16a8d66a-5d15-37e4-b025-5d609d0b278c | -11.18693 | -55.02302 | 2025-08-25 04:42:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5774794e-7ae6-30fc-a6fc-3386c2245d16 | -12.98623 | -45.2283 | 2025-08-25 04:42:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 377efa54-9ebd-3dd5-9728-6fb09da98898 | -9.60943 | -55.34688 | 2025-08-25 04:42:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d993d05b-9ad7-33f7-a5fb-841831bccd33 | -10.45476 | -59.13245 | 2025-08-25 04:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 73719dad-44c8-3ce7-abeb-04ebd89a19db | -8.86902 | -62.42655 | 2025-08-25 04:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d0dda977-74a0-3ae5-be60-a354b07ae0a0 | -7.84582 | -49.99635 | 2025-08-25 04:42:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 626411c9-7269-3285-991f-dba8241d669a | -9.18307 | -59.62021 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 80144b74-5f49-3c72-9cd2-353a2fe31c4b | -11.33787 | -47.8502 | 2025-08-25 04:42:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e9ab2942-5a36-3c9d-bfe2-00c859f876d8 | -10.60007 | -54.88742 | 2025-08-25 04:42:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e5ed5f91-cf82-356d-a16c-4b1cbb637be0 | -9.26096 | -59.78506 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7cc3dee8-dea4-3df9-ac6d-7feba622ec94 | -8.10501 | -62.87307 | 2025-08-25 04:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 34994ace-bf60-3046-914e-1c3eefe9109f | -8.60272 | -62.58942 | 2025-08-25 04:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ded99926-5fb4-3bb7-a9c0-af6b2d45157a | -9.25368 | -59.63765 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 00387e27-a844-3355-aa6c-cf9a7daab4dc | -13.45592 | -46.87795 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ad488a09-8a92-37a9-b1d6-49b2cb38babc | -9.20404 | -60.92688 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8af2f174-2ba9-391b-99ab-669a0a7dc459 | -13.80927 | -45.88306 | 2025-08-25 04:42:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 66bb8f38-ecb8-391a-ab39-191a76a04fa7 | -9.19823 | -59.45042 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d20bd58e-2240-3ab7-b138-3e97a6db2e50 | -11.39401 | -50.68264 | 2025-08-25 04:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ecf54c42-d593-3a2d-a889-4f88257a1c12 | -9.1741 | -59.60757 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 15fda2dc-b392-3471-9f44-ec8f44c7a5a0 | -9.51915 | -60.52212 | 2025-08-25 04:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1b6fc5a5-aa01-30c2-9502-5220d4274fa4 | -8.11918 | -62.87667 | 2025-08-25 04:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e5e87e7b-a43d-3185-9ab0-a5128e4db14f | -8.61951 | -62.62836 | 2025-08-25 04:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70a9a826-2ca5-30a7-83b1-0fee71c8197f | -8.29355 | -46.36072 | 2025-08-25 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 759b7895-f333-3f10-a1ea-3c3c15b00824 | -9.18361 | -60.79053 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 9746d2e8-feb6-3055-99cd-aece21a3ed6a | -10.41903 | -64.44014 | 2025-08-25 04:42:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e0a70ca3-c191-3d68-80d1-44db5cc9e9d3 | -9.19341 | -60.78888 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| ce5ff7eb-4100-38a9-96f2-578ea06954a2 | -9.95906 | -60.18653 | 2025-08-25 04:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 65a768d5-c069-3fc4-86f2-dd4630022a7a | -9.51569 | -60.50864 | 2025-08-25 04:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 73b5e0d0-a1ad-3699-9c1c-96cc4b23ae19 | -11.63794 | -46.22355 | 2025-08-25 04:42:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f784011f-2067-3e93-8c8e-02fa16d0230b | -10.25358 | -59.11245 | 2025-08-25 04:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 793ddcd3-42a3-34f2-bb73-cc523b418ad4 | -8.54638 | -48.84833 | 2025-08-25 04:42:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9664bcfb-f087-3fa5-bfda-8768a2efa0e7 | -11.10285 | -44.78534 | 2025-08-25 04:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f022d408-6ff4-3c04-9970-9e2fcb7fbd92 | -12.74758 | -48.1176 | 2025-08-25 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6159f33a-3ffb-34e1-a538-39a44d69b191 | -9.22316 | -59.71046 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e01d0484-d4dc-3538-b279-b78c228a248a | -9.19414 | -59.44236 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7408fdb7-0725-3aee-a5eb-00721699cb28 | -9.64425 | -59.63704 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 56eab558-2b7a-3041-a520-33be19791e9d | -9.19361 | -59.43866 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18c93ae3-f790-3bc6-ae81-49c2d3540983 | -8.07109 | -49.66063 | 2025-08-25 04:42:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9507199b-9f64-3d5d-ba6d-1b75ab96e4b9 | -9.15091 | -59.51813 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 53129b4f-1a19-3a0d-953c-a8a04e92f3e1 | -6.82696 | -58.95763 | 2025-08-25 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 55b043b4-6dc4-325b-abfc-e2f3a7f4373c | -10.05161 | -59.36094 | 2025-08-25 04:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6777b886-8c06-3ddb-8e1a-c02e198b6922 | -10.53666 | -46.76141 | 2025-08-25 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cd5e0bc9-7c45-3f37-b6b2-89eb865f50e5 | -9.16248 | -59.51659 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 466d9d69-9a54-3de9-9513-97f0a013c080 | -9.15654 | -59.45705 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 344938e9-65f7-3771-bc8f-c89c3a1d4959 | -7.64942 | -63.524 | 2025-08-25 04:42:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3af6d856-46e1-3d19-9139-95506f46eded | -10.8191 | -46.4373 | 2025-08-25 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 407a81f0-b283-3447-98b6-96104d97d6f5 | -10.36949 | -46.45991 | 2025-08-25 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 88092fdc-a00f-341c-9f6f-40a2a484d35e | -8.60627 | -62.58894 | 2025-08-25 04:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2e3daecd-e3b3-3c94-bcef-aca282955c2e | -11.27087 | -44.96941 | 2025-08-25 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 28560bad-a105-38b1-b551-34ec2622446e | -9.16117 | -59.5237 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 26ed571c-db2a-3f6d-8b98-f41a09d7c0c5 | -13.50613 | -46.90187 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README44.md)
