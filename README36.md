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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 75ad7494-d5de-320f-94d0-259480c0ab9b | -3.31453 | -53.86312 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| a7e0dd82-78c8-3d07-afcb-d6d83005bed0 | -5.74231 | -46.17636 | 2024-12-01 04:23:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6909e5b2-36ff-3e98-bd31-5b7c68d1c151 | -5.73176 | -43.98101 | 2024-12-01 04:23:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7f692eeb-1a8c-37c1-8e07-266c8471c042 | -5.13634 | -46.19503 | 2024-12-01 04:23:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 91a85c9a-e6b5-3fbd-b05a-876f8216344e | -10.69772 | -44.97395 | 2024-12-01 04:23:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5d8e2347-9d16-34c9-b8f5-1b598a607145 | -3.68986 | -51.81766 | 2024-12-01 04:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 659159c8-6e11-3652-baf0-595e2d0dc8d1 | -3.25798 | -53.62867 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 66423615-9a09-3e8c-8aca-683e87d2bc06 | -10.76528 | -44.79499 | 2024-12-01 04:23:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cfb8de80-6d9f-353c-b48d-94d9b2fb7c1a | -3.48742 | -53.81186 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1952d89a-c9ab-3186-8712-aff838ab7707 | -3.75297 | -52.27069 | 2024-12-01 04:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 7a7886a3-6de6-32bc-9859-7275eace926b | -3.25323 | -53.92577 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9f0806c0-835e-3259-babe-befe8bcca054 | -4.3869 | -47.22872 | 2024-12-01 04:23:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 59106795-f53a-3663-9300-32a0354cb4ad | -4.4731 | -50.76469 | 2024-12-01 04:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d1514c69-9e0f-3e03-aa8b-08e66f0e78cc | -5.73122 | -43.98451 | 2024-12-01 04:23:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6faf9f9c-f140-3dc1-ad74-d6a441490a70 | -4.55914 | -45.71598 | 2024-12-01 04:23:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 09cf9405-5bf8-3f13-a22f-7859c7b8cbcb | -15.56895 | -47.85578 | 2024-12-01 04:23:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 02130e85-c9ae-3ad5-ba56-41200086db09 | -4.34577 | -50.77154 | 2024-12-01 04:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c1a30e19-8e20-3e23-8d98-3e39405c1434 | -4.59204 | -45.57276 | 2024-12-01 04:23:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2996ca9c-396b-395f-993d-26fbca495989 | -3.30214 | -53.83524 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e1b6728e-798f-33c9-9780-b757f4c3c086 | -3.26225 | -53.6364 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| dbd5d6cb-3654-3ccb-8861-ef84c458160a | -3.73148 | -51.30935 | 2024-12-01 04:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a6255129-85ce-3317-9bda-d90e79afb059 | -3.30763 | -53.83614 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a297bad-f4a3-33d3-a563-b15a646ea16e | -3.73069 | -51.31403 | 2024-12-01 04:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 95c8a737-5635-3dee-949d-8ac99dc36be8 | -6.71651 | -47.27144 | 2024-12-01 04:23:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8d3952e4-0013-3945-95f5-1c0f3e5d3d03 | -4.20822 | -48.12216 | 2024-12-01 04:23:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 335038b5-b9ea-372f-8efc-8c0604d79a45 | -7.46259 | -34.87497 | 2024-12-01 04:23:00 | NOAA-21 | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| add8c266-8463-3142-98be-5ab483fb2796 | -3.33711 | -53.28864 | 2024-12-01 04:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cdb4a37a-fbb1-3e55-b80a-6dcefde7f24d | -4.1889 | -50.68269 | 2024-12-01 04:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4fdd15c9-c201-38e1-b12f-ea86fa706491 | -3.34244 | -53.28931 | 2024-12-01 04:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 33917298-c450-3ce7-847f-8919613296bf | -10.66595 | -44.49213 | 2024-12-01 04:23:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 494d5313-a875-3f2d-8145-a7df09ebad87 | -4.56138 | -45.72356 | 2024-12-01 04:23:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a4101cf0-49b8-3697-aff9-d28645c65a5a | -3.91207 | -52.34069 | 2024-12-01 04:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b94861d-5098-3085-ae03-a40e2502c4e1 | -4.6184 | -46.47077 | 2024-12-01 04:23:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e382621-231b-380e-9e97-4513f341d3bf | -5.66847 | -46.8209 | 2024-12-01 04:23:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 60da4678-9549-3c95-81d3-0f890edfe447 | -6.08199 | -44.88025 | 2024-12-01 04:23:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5747458b-b6ce-316a-af70-ddff73d3961e | -3.71436 | -51.06977 | 2024-12-01 04:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2112bb91-ab0e-3750-a2b8-87cd5c8b3ad0 | -6.92484 | -43.54337 | 2024-12-01 04:23:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 17.7 |
| a9edbccf-4d12-3c1c-bdce-9d17a072c2c9 | -3.30839 | -53.83427 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ec30911-a673-37d1-8678-6da8cd218175 | -5.50568 | -42.87432 | 2024-12-01 04:23:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| a537366e-4f43-3b90-a9d8-949ead51ede2 | -4.17444 | -48.6206 | 2024-12-01 04:23:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d279dfd1-c8d8-3159-9923-10df0de09286 | -3.30844 | -53.86584 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 6bdbb45f-ce7f-3a17-9d5e-50c3306579dd | -6.92656 | -43.54317 | 2024-12-01 04:23:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 2a39d764-e927-3973-8301-6d5e21c30def | -6.92372 | -43.55059 | 2024-12-01 04:23:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fad429ee-1b2f-3a90-aea4-f6aed937240f | -3.29678 | -53.8361 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6eabed6b-edbc-3b17-9ab4-1b1ff5e7dfea | -5.31418 | -43.07339 | 2024-12-01 04:23:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e275b70e-6c69-3517-8e0d-c8b92d27711a | -10.66259 | -44.49161 | 2024-12-01 04:23:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b3fad231-138e-3325-96bf-ea5ae6e1ae40 | -8.83932 | -44.77041 | 2024-12-01 04:23:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 702a6ec8-11a5-3409-9647-4735373ab7b6 | -5.33096 | -45.43874 | 2024-12-01 04:23:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8802954e-f96a-3b64-bad3-0b671f378217 | -3.69316 | -51.34312 | 2024-12-01 04:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0555bf3c-eee1-3164-9885-c15ec4516ac4 | -5.61112 | -45.06356 | 2024-12-01 04:23:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| abdd806c-3130-34e2-87d2-ce850eb27819 | -3.24772 | -53.92476 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6a37179a-31ef-3f1d-8b45-fadd4ec3203d | -4.76137 | -50.99273 | 2024-12-01 04:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dff3cfc7-a23f-36ab-bb1f-fb49318936b1 | -3.26765 | -53.63743 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 34182614-690f-31a6-834a-f09ef37c2710 | -5.58148 | -43.61232 | 2024-12-01 04:23:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0771853a-4739-344e-8399-d5ca85bfa071 | -4.55579 | -45.71547 | 2024-12-01 04:23:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 524f86ed-b9fb-34a5-923b-e99d76ed0b69 | -3.24902 | -53.64863 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3804be8a-ef00-3130-8d86-448074c50552 | -4.41213 | -50.69889 | 2024-12-01 04:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 365b92c1-a081-334c-abb6-8cba8d5af789 | -4.18959 | -50.67849 | 2024-12-01 04:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 490e237b-d098-3b09-9846-e255ca0eae09 | -6.28942 | -43.84856 | 2024-12-01 04:23:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 690a716e-41bc-3953-a31d-9832d108a0ca | -10.42577 | -44.90633 | 2024-12-01 04:23:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f5921d9-1086-37dd-b2b2-d5e8beb6b489 | -4.00331 | -54.6188 | 2024-12-01 04:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1c76b663-7a5d-321a-aa51-65aa9e19e79f | -3.95214 | -49.95532 | 2024-12-01 04:23:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3629458f-816c-3997-9fc3-bf41bb546959 | -3.63847 | -54.44 | 2024-12-01 04:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9f7677dc-d241-3f19-84fd-0fb9050c938e | -8.93913 | -44.25245 | 2024-12-01 04:23:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b4bfcb15-7518-3846-a2b9-723188ef4079 | -4.6589 | -49.73471 | 2024-12-01 04:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 16a53de8-d24f-38c1-b74f-431c70974e57 | -3.81841 | -52.25506 | 2024-12-01 04:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 32e589e0-eb70-3884-ae33-3ebab0bd7658 | -6.86645 | -47.23659 | 2024-12-01 04:23:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 539d0b43-46ce-3ddb-b856-85bd13a5cbc6 | -4.202 | -50.68481 | 2024-12-01 04:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d7d948bb-220a-3e7c-ae63-484b18a41887 | -5.18871 | -43.95352 | 2024-12-01 04:23:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7cd74c9d-cb78-32e2-9387-5e054c344e84 | -6.56269 | -40.21152 | 2024-12-01 04:23:00 | NOAA-21 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 228b864c-2e3d-38df-8a80-d431ab7c0a22 | -4.45548 | -56.18076 | 2024-12-01 04:23:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2e13eb69-c907-38d5-af28-fd41e22b932c | -3.46489 | -53.87935 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 204c620e-0d5b-3860-bdc0-9e53e991d4c5 | -6.92994 | -43.54369 | 2024-12-01 04:23:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| e5dbef8a-6952-36a2-8af7-1049ccbe47d9 | -4.58542 | -50.96124 | 2024-12-01 04:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e85cbe3d-8925-3309-a190-bac2c375add8 | -4.41382 | -50.82492 | 2024-12-01 04:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f18cc98-bb63-3e7b-84ec-d9c73db068f7 | -4.26421 | -47.60921 | 2024-12-01 04:23:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d22f4416-38ea-30bb-8e64-1bb790a12f05 | -5.68581 | -46.95481 | 2024-12-01 04:23:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 74fdf25f-043e-3125-ae9d-9fbf80a426ee | -3.31335 | -53.8704 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| c53f8923-644f-3585-980b-ca147f8f1cdf | -5.62724 | -45.95371 | 2024-12-01 04:23:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 15f43e51-6d89-3b12-94ff-f4c97fb3ffe7 | -5.18622 | -43.88181 | 2024-12-01 04:23:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d429b830-0da0-3290-b9b0-6de910eede00 | -3.86941 | -51.01002 | 2024-12-01 04:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c1621e34-2b2a-37ba-a004-3284e8beedde | -3.66154 | -51.72452 | 2024-12-01 04:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d5224983-a006-3e0e-bf49-3400f28733dc | -4.84233 | -44.4768 | 2024-12-01 04:23:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a73018c-fa43-3d13-a23e-b4cca3b6f834 | -5.42366 | -45.10858 | 2024-12-01 04:23:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 25ac6896-819b-38d7-b5f3-5893ab87a8f7 | -3.21697 | -54.17871 | 2024-12-01 04:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| be3f64e3-59dd-3a6a-b7ca-cc87be02e152 | -6.92146 | -43.54285 | 2024-12-01 04:23:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 17.7 |
| f7571e92-10a6-36a6-9611-61380d24b8a6 | -3.76629 | -51.6179 | 2024-12-01 04:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ae85d73f-0165-3360-a6e6-d065537e0393 | -4.92226 | -48.20321 | 2024-12-01 04:23:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 966f17aa-9cdf-3bcf-83cf-a45dcbe221c6 | -4.72393 | -45.68758 | 2024-12-01 04:23:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 06414149-3b1e-304f-ba9b-db9636b81eda | -6.0905 | -43.54882 | 2024-12-01 04:23:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bbd1d3d9-89ba-3beb-a3e0-2c4007053fb8 | -17.0082 | -49.77974 | 2024-12-01 04:23:00 | NOAA-21 | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 82974857-0c36-3c2a-a6a3-e18f54bb14c2 | -4.55355 | -45.72962 | 2024-12-01 04:23:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f2d872d-0d84-3ba5-939d-34909c764c79 | -6.28888 | -43.85209 | 2024-12-01 04:23:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8b151e1c-ba59-3da7-96d9-4e05b92e82f3 | -3.4012 | -53.03262 | 2024-12-01 04:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2126925-2058-3935-8167-50d4c585265b | -5.91578 | -43.84486 | 2024-12-01 04:23:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dc25e863-7fa7-3fdc-b259-8ca7a351b0e0 | -6.86665 | -39.91485 | 2024-12-01 04:23:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c23f9fc1-287c-3366-824f-7af20b32f402 | -5.01862 | -47.11079 | 2024-12-01 04:23:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 633efc5a-aa93-3946-ac9a-f4b7fcc7e468 | -3.74059 | -51.83639 | 2024-12-01 04:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f333f48c-251a-3713-a2fb-1e44a8183977 | -4.08033 | -50.02665 | 2024-12-01 04:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fb61d7c7-5914-3a22-87d7-5445c3e314b2 | -5.14451 | -44.21641 | 2024-12-01 04:23:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |


[Clique aqui para ver as próximas entradas](README37.md)
