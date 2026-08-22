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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5d2a1231-b068-3e27-bde1-600ee714b70f | -10.47445 | -45.08862 | 2026-08-22 04:27:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 452d0d5c-1184-3990-9542-4c74a26a292c | -12.77889 | -48.38998 | 2026-08-22 04:27:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4389f07b-0e63-3ae1-a910-05b2c4847464 | -11.59142 | -46.58154 | 2026-08-22 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ed27823e-a26b-36a0-8ae3-663854c12e93 | -12.01034 | -53.42819 | 2026-08-22 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f1d28922-62c5-324b-b558-9c3b8846170f | -12.01453 | -53.42895 | 2026-08-22 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7881fac-f17d-389d-8252-20de75838b17 | -6.93669 | -59.30556 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b945fe3f-9a04-361a-865b-4a9a7ceec85c | -6.78652 | -59.42803 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 1f22ca64-0f71-3281-8dcb-59ad38dd51a0 | -9.00196 | -50.74717 | 2026-08-22 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 28850b85-5496-3d67-8b12-5a90e7b7f4e2 | -12.79792 | -51.48132 | 2026-08-22 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9fba02f6-aabf-3d07-b89a-ab15a2955516 | -6.8118 | -59.41843 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 886aa8e3-a33e-3ff1-9d7d-b3a5852613a4 | -10.29512 | -50.39277 | 2026-08-22 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d3eec1ea-f395-38c3-971e-88369287d431 | -10.525 | -50.7699 | 2026-08-22 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 44cd901e-0053-3bcc-8edb-46f99342be78 | -7.54541 | -46.02072 | 2026-08-22 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aea0e37a-9e08-3b69-944a-51afc310cd69 | -7.23119 | -51.68803 | 2026-08-22 04:27:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f593b393-0fe4-3eda-a595-55942bcfcd1f | -11.84146 | -39.18465 | 2026-08-22 04:27:00 | NOAA-21 | CANDEAL | BAHIA | Brasil | 2906402 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4b13ab17-9c9a-3d26-9e02-6a5ed915ed4d | -12.7307 | -46.46265 | 2026-08-22 04:27:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 50bed995-349a-36d0-988e-0b83b3a473f4 | -11.59913 | -46.55347 | 2026-08-22 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 85d14767-dc34-3f98-9259-19847ca132a8 | -6.11115 | -53.07376 | 2026-08-22 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 097e5cca-dc7d-32aa-af69-402428d47765 | -11.16587 | -54.00708 | 2026-08-22 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 84decae7-e7f7-3450-bd1a-05cb49e223d4 | -10.80555 | -50.97989 | 2026-08-22 04:27:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 19.2 |
| e66c8261-c91b-314a-9935-60eb0ab23bf2 | -11.62854 | -46.51768 | 2026-08-22 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d0567d98-b20d-3c38-af6c-e1cc9566e602 | -14.00434 | -46.19713 | 2026-08-22 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 61dd1a59-0f61-3ee6-84f9-00ecb9e406cb | -11.16484 | -54.01651 | 2026-08-22 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 06a3fa43-7ac9-3524-af4a-6bdc121238bd | -8.53535 | -54.8138 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7d332c06-3198-3e8b-a7e0-69455d1b8e01 | -8.54015 | -55.32843 | 2026-08-22 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b7d3207-f7de-3990-ac68-f59094de042b | -6.80622 | -59.41125 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 5f35e6ac-3f93-3cf4-9b04-611455d87a34 | -6.80962 | -59.3934 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 43fba9be-3969-3444-bf7a-dd3f67b59178 | -8.52936 | -54.83325 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| eb85dcb3-ced1-32a6-b885-12d44d39cd9b | -6.75955 | -58.66273 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 93298e57-da35-3bd0-9600-833fa6be590d | -9.16594 | -59.45299 | 2026-08-22 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 445143b5-d5e2-3aa9-b351-2ca86cce6871 | -6.81454 | -59.42683 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 53f4a97a-60d7-3d9d-8e0f-421b6c42807c | -6.76597 | -58.66396 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 43788312-c99f-3fd1-a1fc-807c5b813286 | -11.10389 | -49.88874 | 2026-08-22 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 33ad8408-3afe-373a-9971-5b670d28363e | -11.44167 | -44.55774 | 2026-08-22 04:27:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 518d23dc-98c5-3b51-bed0-3a0fe1eaadbe | -6.8152 | -59.40054 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4198535e-a664-38dd-b72b-0f606523b6a3 | -11.16636 | -54.00773 | 2026-08-22 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 70cd5973-24b1-39dc-b52c-362af4da99d4 | -7.69808 | -46.15493 | 2026-08-22 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 67e974a9-70a2-3995-b502-72de5b5d7dc3 | -8.99529 | -50.7179 | 2026-08-22 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6f3c480e-0a33-3c33-a1a8-115ada24d602 | -9.43205 | -51.66092 | 2026-08-22 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 778ef4d2-a656-3322-a013-6a2391f4d2f1 | -8.53219 | -54.81688 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 7f04a022-04f7-3634-b293-5ab395eb9c86 | -14.14186 | -48.06938 | 2026-08-22 04:27:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c26c6868-e58b-3918-aa51-6be620a27e36 | -6.17158 | -55.4419 | 2026-08-22 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| acab0e52-bacf-3d6a-9e8d-3caaa62c4c15 | -11.44528 | -44.53296 | 2026-08-22 04:27:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bbd73965-e056-3d4a-a3c2-126b0eb2f7f4 | -6.09015 | -59.95602 | 2026-08-22 04:27:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5cbc9b5d-756c-3f11-9933-978b203e5eed | -6.69511 | -58.94576 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 46cc79a6-9c3b-3cc6-8bff-3c1e24970901 | -7.35249 | -55.6682 | 2026-08-22 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 788b972c-1544-3424-bf62-14eaa7e11e63 | -6.00283 | -57.80909 | 2026-08-22 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1126919c-b22c-36a4-abec-02d0a5d94c69 | -9.00495 | -50.75232 | 2026-08-22 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 2686eed7-4aa8-36d9-b91b-034b3cc9f2a5 | -8.99529 | -50.74123 | 2026-08-22 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c7c689e0-be2a-3c8e-b069-4b8606a58042 | -8.11031 | -50.04803 | 2026-08-22 04:27:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 72ced445-2a87-33b9-8cf3-6b3c78b34b27 | -10.5163 | -50.82055 | 2026-08-22 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4f8966b2-285b-34dd-a49f-7a8f907e1f1c | -10.96781 | -51.41076 | 2026-08-22 04:27:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| bd1fe898-91a4-324e-92cb-7f0f9d446b50 | -12.3618 | -46.45041 | 2026-08-22 04:27:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8539b0ee-0bb6-3212-9436-369602f37970 | -11.33708 | -45.02829 | 2026-08-22 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 03f70beb-9dd9-32ea-a37d-5e9c1dee40ed | -9.19304 | -59.45315 | 2026-08-22 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| efcb3555-4b28-3175-85d3-e6cbba0e13c7 | -8.5404 | -55.33344 | 2026-08-22 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6417fb25-9c64-31d4-b1cb-bb7a36d711e3 | -6.67632 | -58.75378 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bb4d1fa3-917d-3914-a031-0ec91d92e585 | -6.15391 | -53.7028 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b170ba5b-7bc0-323a-9460-b32f5882f01b | -6.81332 | -59.39563 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0ef40f5e-c6d5-3479-86e4-8e5e247f881a | -9.17999 | -59.44995 | 2026-08-22 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 3c3513d2-7c30-3f0a-9914-cac76a331098 | -12.2471 | -43.1832 | 2026-08-22 04:27:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 6c11c748-c2a1-38ac-920f-3f4d3c735991 | -9.10834 | -60.92112 | 2026-08-22 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 88c87b39-c25d-39d5-be6a-cff044389cd2 | -10.96405 | -51.41012 | 2026-08-22 04:27:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aa1dddc5-7ddd-3bf6-8d42-08eae8f39205 | -8.63461 | -54.69901 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ca93e9a2-cd2a-30ed-b710-d194410aaa6f | -6.43456 | -54.94801 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed698a77-a13c-31ac-a970-0daf5b85f3cd | -13.3771 | -41.34837 | 2026-08-22 04:27:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7141cba7-910a-304c-876c-10c4a8e51e72 | -6.77823 | -58.67365 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 192b2b5d-9e69-37e6-9342-708d44c242aa | -12.84291 | -48.45853 | 2026-08-22 04:27:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b275d013-ae65-3603-abc2-69953955bc1b | -8.45819 | -51.55692 | 2026-08-22 04:27:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 84ca6b3d-bf8d-35ef-9272-84ab402d9dfa | -7.1235 | -46.56907 | 2026-08-22 04:27:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8a24cf19-4519-38f6-9689-7b52ba8bd393 | -6.79048 | -59.42082 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| c7c2bdd2-f5e9-373e-8e79-53394a1e828c | -6.77276 | -58.66728 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f3c90d41-1ada-3626-8e98-43c7a372d6e5 | -9.21017 | -59.77212 | 2026-08-22 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7b6caa51-1870-3d9f-8e31-47b6928f1b4b | -11.0721 | -49.95203 | 2026-08-22 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d8083422-b20e-3673-962c-cf6f62d13259 | -6.15984 | -57.7415 | 2026-08-22 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6e8009ae-6a7a-34ea-be30-1026f3b65b23 | -11.60023 | -46.5463 | 2026-08-22 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b4bbbb53-a6cb-3aae-a063-924343a1acdc | -7.71573 | -46.15056 | 2026-08-22 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5d13c8c3-38f9-3636-bc47-0d954d2a863d | -8.52336 | -54.80976 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| b9fcb12d-5c89-3f14-9cae-3419e71bbfa7 | -8.53588 | -55.32951 | 2026-08-22 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4c3c5688-ded9-336e-a018-9597fd564cdd | -10.80114 | -50.98367 | 2026-08-22 04:27:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 23.5 |
| a9edabed-e871-390d-81c1-a38fed1c921d | -8.52752 | -54.82924 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| f67a6a63-3ead-3018-9f0b-41d3082f31f0 | -12.79197 | -48.45768 | 2026-08-22 04:27:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 677e3485-838a-3ea5-aef7-58d80009fdf7 | -8.59371 | -54.73981 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ce46e641-95f7-3118-acff-756d4a669363 | -12.75483 | -48.47709 | 2026-08-22 04:27:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 792b355f-3863-3990-a87b-b9d5cf96c0cc | -6.76732 | -58.66079 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 19.1 |
| d6f9e56b-a4ea-3ced-8c1b-7d44c3cf2718 | -9.44017 | -51.63679 | 2026-08-22 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 94a300f7-a4ee-3977-aab6-47b35f3154da | -8.59841 | -54.71321 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d571bfe4-6958-3501-8c39-a2ca6403173a | -6.67083 | -58.74726 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b9a57a9b-05b7-3b2c-8e6f-e0a017daa47b | -12.79546 | -48.39273 | 2026-08-22 04:27:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6a2944a0-13a9-3da5-a545-f9e8ecefdabd | -9.43801 | -51.62593 | 2026-08-22 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 962cb7db-c415-33a8-8829-b8c136a6465b | -9.44622 | -51.60117 | 2026-08-22 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 884efd0f-9cd2-3aff-badd-383139502d04 | -8.16111 | -46.71922 | 2026-08-22 04:27:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a375f579-a6a7-3646-8ae3-c7c5fd54bb2c | -9.15836 | -59.45731 | 2026-08-22 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 54323537-c14d-3dc9-90eb-503595a9d1c3 | -12.25946 | -43.17988 | 2026-08-22 04:27:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 4c99e4eb-d0ad-38cb-8118-7d935ce63677 | -6.79069 | -58.64224 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| d99a6400-1bc4-3aaf-b6bf-a2662b968b5e | -9.04602 | -60.4491 | 2026-08-22 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 78e165d5-c3bf-36c8-89af-c6cce8dc9dac | -8.99944 | -50.7495 | 2026-08-22 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e7269b71-5de7-3a94-ae34-8a26113523b5 | -13.38156 | -41.34895 | 2026-08-22 04:27:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7532b911-59e8-354b-8fb4-18a03f6accd3 | -12.77557 | -48.38944 | 2026-08-22 04:27:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| be6b99ee-bb5d-37f7-845c-1d7dc6e336f3 | -6.12256 | -59.8988 | 2026-08-22 04:27:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README23.md)
