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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0fd27611-dcfd-381a-a42e-7d446c9473dc | -15.15504 | -50.12305 | 2025-09-13 03:49:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8ba783ca-d9d5-35fd-92f7-c982349cb165 | -15.69505 | -50.5812 | 2025-09-13 03:49:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 62677bde-53b0-3d25-a52c-e78992ff9006 | -21.62484 | -46.80556 | 2025-09-13 03:49:00 | NPP-375D | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 406f8629-8b30-3503-9cfd-f4a5c4ed0354 | -15.69222 | -50.57476 | 2025-09-13 03:49:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 34300b98-1f1b-3a9e-abb3-c73f136cda17 | -23.61252 | -51.38196 | 2025-09-13 03:49:00 | NPP-375D | APUCARANA | PARANÁ | Brasil | 4101408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| e8c638f1-1435-3fe9-addc-515dd292aa1f | -20.64385 | -48.69561 | 2025-09-13 03:49:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a7285314-b51d-3144-aa15-83d717bddc3d | -15.50883 | -47.29792 | 2025-09-13 03:49:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 90dd8ddc-5457-30a7-95a4-5f3ff9dca268 | -16.41016 | -49.24501 | 2025-09-13 03:49:00 | NPP-375D | NERÓPOLIS | GOIÁS | Brasil | 5214507 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fe2e9b72-24ac-3b45-960a-28fca451e491 | -23.22978 | -51.00029 | 2025-09-13 03:49:00 | NPP-375D | IBIPORÃ | PARANÁ | Brasil | 4109807 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 44d7f267-4870-31a0-a608-6bfc69e3ac15 | -15.14338 | -48.31129 | 2025-09-13 03:49:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a7c44fba-615e-3d34-93a3-9370f6d252e1 | -15.23985 | -51.40186 | 2025-09-13 03:49:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 254086d1-0f74-3f41-9918-b155963a6f1d | -16.0614 | -50.01609 | 2025-09-13 03:49:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 17.6 |
| a289ddd9-4d50-34ec-a3e2-a68c5bab48bf | -16.28942 | -45.68615 | 2025-09-13 03:49:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 51456b44-615b-3396-b29d-14f24f97569a | -22.22555 | -48.60916 | 2025-09-13 03:49:00 | NPP-375D | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 9324862e-9990-3afb-9ce2-834edf1be674 | -15.60634 | -47.93181 | 2025-09-13 03:49:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 213727ae-9614-3778-a36f-7aa7181ef35d | -21.58842 | -48.41974 | 2025-09-13 03:49:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ca28b91f-8409-3b0f-acf8-2878aaba2425 | -21.58322 | -48.41828 | 2025-09-13 03:49:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 16.0 |
| a7b9a5bc-e287-36d3-bbde-9f50bf72d67e | -23.69923 | -51.79025 | 2025-09-13 03:49:00 | NPP-375D | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a56cf467-eb93-3618-b0d1-49470a7d8b92 | -22.65978 | -53.11514 | 2025-09-13 03:49:00 | NPP-375D | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 3498f74e-a4e5-3ffa-9a77-436ee8a989dd | -14.44541 | -47.31919 | 2025-09-13 03:49:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8f74b781-edbe-37b1-9735-3af8b6d74651 | -16.8516 | -41.53566 | 2025-09-13 03:49:00 | NPP-375D | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 819b90a4-e50e-3dd4-a9c0-158993d1b43f | -16.41009 | -49.03885 | 2025-09-13 03:49:00 | NPP-375D | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 15496df0-aec5-3830-891b-9c883b281b70 | -16.06499 | -49.99997 | 2025-09-13 03:49:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 656d556a-4d28-38e9-a93a-6951d7fc1fac | -23.45547 | -47.35128 | 2025-09-13 03:49:00 | NPP-375D | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 85019cb7-aba2-396a-8c13-97e4714c0592 | -15.53846 | -42.57001 | 2025-09-13 03:49:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d6879611-6e4d-3127-8e4e-87e6ce2f27ba | -9.5326 | -54.6075 | 2025-09-13 03:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 97.5 |
| 2a781aad-c054-3730-8335-d0efc19cc48d | -10.7477 | -50.5106 | 2025-09-13 03:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 136.8 |
| 9dd26eb1-2ace-31bf-9cd4-4e93694a64c9 | -21.5912 | -48.419 | 2025-09-13 03:50:00 | GOES-19 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 68.9 |
| b425b50a-62de-3b1e-b922-baac91d1fc1c | -9.5139 | -54.6089 | 2025-09-13 03:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 91.0 |
| efbd8766-3ea4-3dcc-aae4-3f1a505eae2d | -9.5322 | -54.648 | 2025-09-13 03:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 120.9 |
| 59ac725f-fd07-328b-ba39-64088e863840 | -11.1893 | -51.4401 | 2025-09-13 03:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 74.5 |
| d84b3213-dff6-3ce5-9169-ba7cac86f5a2 | -12.9595 | -47.9963 | 2025-09-13 03:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| e35dcf2e-350f-3766-8835-0773315c0b05 | -12.006 | -47.7505 | 2025-09-13 03:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 3bd0ef12-c3a9-3e06-8d8f-b9ea1d4df701 | -11.9869 | -47.7531 | 2025-09-13 03:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 6a27bf34-5792-352e-87d9-0640f45f7f95 | -9.247 | -59.4201 | 2025-09-13 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| fc110b5d-a422-32f0-b37f-8e3c463938f2 | -9.5324 | -54.6277 | 2025-09-13 03:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 302.4 |
| 20197ea5-fde1-30e1-a6e4-fa6c69c8c1d7 | -9.2472 | -59.4007 | 2025-09-13 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 9782395f-6671-3c70-92e5-efd10b44c038 | -9.5137 | -54.6292 | 2025-09-13 03:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 253.6 |
| b16d3e2d-82cc-314d-bf01-df1248f063d1 | -9.2656 | -59.4191 | 2025-09-13 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 159.1 |
| 42d1e179-9855-33c8-8673-ecfc79df4f35 | -9.5006 | -55.9588 | 2025-09-13 03:50:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 7a1b510c-bfd0-306f-b890-c296fed7e994 | -11.1706 | -51.4209 | 2025-09-13 03:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 6f85d499-1b40-3b75-b262-5def0b327c2a | -9.5004 | -55.9788 | 2025-09-13 03:50:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 91.0 |
| bbbf088b-9569-3088-8efa-1361b9871801 | -9.5135 | -54.6494 | 2025-09-13 03:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 106.3 |
| 98c66359-58f8-3977-9118-7dc2b0f6e6ea | -9.2658 | -59.3997 | 2025-09-13 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 115.8 |
| 74fd30a1-3b62-337c-b633-b8e4dcfbf37f | -9.2503 | -51.2472 | 2025-09-13 03:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 8b3400c9-0400-3ff2-867f-fac868ed47cc | -14.2905 | -46.0693 | 2025-09-13 03:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 54e86d42-2b0d-376c-bd35-11475e23cbef | -10.748 | -50.4892 | 2025-09-13 03:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 90.7 |
| c6eb3be7-768a-3759-8467-47d5a97916a3 | -9.2844 | -59.3986 | 2025-09-13 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.2 |
| ce692df8-bbde-36ea-bedc-1ebd596bb5f4 | -11.1896 | -51.419 | 2025-09-13 03:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 129.2 |
| 8edf43b7-298c-32b5-8872-1b225f100d08 | -9.2843 | -59.418 | 2025-09-13 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 921cf768-1656-3445-aafb-b734504d0dd1 | -12.9402 | -47.9991 | 2025-09-13 03:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 951f3125-4454-31eb-ba86-e197c66fe68e | -21.6187 | -46.8115 | 2025-09-13 03:50:00 | GOES-19 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 72.8 |
| dd9e5af3-ec7d-3953-9708-c962d4a5c12a | -9.5326 | -54.6075 | 2025-09-13 04:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 106.4 |
| 63085210-4a8a-3521-a326-e6a4d2688f8a | -9.5004 | -55.9788 | 2025-09-13 04:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 275ba2c3-82f9-36dd-804b-95a9140eca60 | -9.5137 | -54.6292 | 2025-09-13 04:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 231.3 |
| 9c1fa9b8-d57b-3247-a6d4-5977baea9c82 | -10.1611 | -64.7401 | 2025-09-13 04:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 49.2 |
| d4e61873-2f43-365d-af64-a2cda71b99fd | -11.1706 | -51.4209 | 2025-09-13 04:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 15a1261b-d784-3cd9-8fac-691734dbf160 | -11.1896 | -51.419 | 2025-09-13 04:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 110.1 |
| aaca9697-440a-304e-bd40-59c0ac0236aa | -15.7161 | -50.5763 | 2025-09-13 04:00:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 56.1 |
| da270610-2fdb-36f0-aea5-2b68ee2b02d7 | -21.6187 | -46.8115 | 2025-09-13 04:00:00 | GOES-19 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 62.3 |
| cfecf1c4-1d2d-3972-8d40-2fb0c7f08019 | -9.5006 | -55.9588 | 2025-09-13 04:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 2859e810-da40-398e-a3a2-a8743c332af4 | -9.5135 | -54.6494 | 2025-09-13 04:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| a9afc263-78b3-3713-a2c4-69b3740f94e0 | -9.5322 | -54.648 | 2025-09-13 04:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 42382abd-e496-3b71-84b6-7f237035a16b | -9.5139 | -54.6089 | 2025-09-13 04:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| e01829f8-3625-36a2-808b-0caee3965d53 | -11.1893 | -51.4401 | 2025-09-13 04:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 14f6370f-5078-3ee6-bbd2-4988488330a2 | -9.5324 | -54.6277 | 2025-09-13 04:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 372.9 |
| 2abdd515-72c3-3150-84a9-a5da8e553b87 | 0.69097 | -50.65158 | 2025-09-13 04:04:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 14a0c96b-bfb9-3d50-89db-fd67254072a6 | 0.69826 | -50.65928 | 2025-09-13 04:04:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c46d536a-a1f3-3042-a9db-a58362d6d4d3 | 0.69233 | -50.66026 | 2025-09-13 04:04:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4f17298f-3ae2-3895-938a-89df5cf5d68d | 0.69691 | -50.65061 | 2025-09-13 04:04:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 9.4 |
| b86593f3-7b68-372a-b08a-d41735f88639 | 0.693 | -50.66459 | 2025-09-13 04:04:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1dd6f014-8736-352f-9df8-440da549e559 | 0.69894 | -50.6636 | 2025-09-13 04:04:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 89e8715b-3fa6-37a6-8761-80cb8f9828a0 | 0.69165 | -50.65592 | 2025-09-13 04:04:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 98ecc9bd-6163-3569-b2ec-a2bfe6e4f4ae | 0.69759 | -50.65494 | 2025-09-13 04:04:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f540c429-5fa2-3bbb-9e60-566c0c2b77d3 | -6.8771 | -45.64267 | 2025-09-13 04:06:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 310b2810-e204-3d29-b786-460606a7ac2f | -3.21844 | -47.63098 | 2025-09-13 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| f1b1e648-2b9f-37f4-a8c4-73ac144aef74 | -5.71601 | -46.44984 | 2025-09-13 04:06:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9685fba8-13c5-3885-b075-f95f9e783b7a | -6.316 | -43.33674 | 2025-09-13 04:06:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4ad60962-ced0-317a-b60a-3f0cb89b66c8 | -3.22553 | -47.126 | 2025-09-13 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| f6f26cbc-4206-3004-b759-7535f19f622e | -6.29876 | -44.24652 | 2025-09-13 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 82994d39-6f7a-39a7-be63-a584871d3f24 | -6.90633 | -49.41473 | 2025-09-13 04:06:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f374c979-a447-3c9f-a6e4-1758ac953393 | -4.60586 | -48.79 | 2025-09-13 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8213ba28-b4a3-3c1a-92fd-9881723f34d9 | -7.14441 | -44.34861 | 2025-09-13 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ed3ca462-7599-31dd-9aaa-9237a249db6d | -6.88162 | -45.63888 | 2025-09-13 04:06:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e45df23d-652e-3fc6-83cd-75d6ffece5dc | -6.71997 | -44.02098 | 2025-09-13 04:06:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e25deb6e-f304-3346-8a20-ecc4e1ec9466 | -7.26181 | -44.42803 | 2025-09-13 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a0b86755-eb4f-3cfc-8ab1-add01983bab6 | -5.94962 | -42.78242 | 2025-09-13 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| fc1d771e-a3b0-3185-9cfd-87289ad63b32 | -6.07031 | -44.82059 | 2025-09-13 04:06:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a64d6d59-b2d7-3e91-8016-25365cc05a3f | -5.32554 | -45.7212 | 2025-09-13 04:06:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6f109199-b040-304d-950f-da7749bf6688 | -6.68221 | -44.16283 | 2025-09-13 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 51f5a962-b2f2-3797-8ccb-3af21d3ff363 | -6.8733 | -45.64212 | 2025-09-13 04:06:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 920872c5-3d88-376a-bb3a-4734fc64870d | -5.93713 | -43.22814 | 2025-09-13 04:06:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.8 |
| ecc487a5-e6f8-3bef-b3b2-583df9f9cf61 | -4.52488 | -43.83678 | 2025-09-13 04:06:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f4f4db3-249b-30d1-98a2-51177a53475b | -6.88198 | -45.63702 | 2025-09-13 04:06:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d6ae0fd9-6561-3e12-9cbe-dda3e489c62e | -7.85395 | -43.86719 | 2025-09-13 04:06:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 44b7ca7f-f2ec-3def-8b95-8c64bcc1fc0b | -7.56542 | -42.64692 | 2025-09-13 04:06:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8b7c1986-a935-3b61-a137-91a0b491040d | -7.21663 | -43.83957 | 2025-09-13 04:06:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6a2db4c7-4095-3968-a4c9-5b9758e50365 | -6.80008 | -38.73679 | 2025-09-13 04:06:00 | NOAA-20 | IPAUMIRIM | CEARÁ | Brasil | 2305704 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d3d05b30-acc4-3a92-b67a-17ede89378c6 | -7.43442 | -44.41404 | 2025-09-13 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8e782597-fb6d-360f-8388-831f6d353311 | -5.28499 | -40.95842 | 2025-09-13 04:06:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |


[Clique aqui para ver as próximas entradas](README40.md)
