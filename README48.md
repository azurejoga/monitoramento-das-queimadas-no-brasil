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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 19065cb8-d925-34e1-8f1c-cdc6e0b2d55c | -23.13204 | -47.00253 | 2025-10-07 04:12:00 | NOAA-21 | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4fd43ab5-4dbc-3e13-b133-bcd39847bbd1 | -22.5347 | -43.58154 | 2025-10-07 04:12:00 | NOAA-21 | ENGENHEIRO PAULO DE FRONTIN | RIO DE JANEIRO | Brasil | 3301801 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c15a4441-e81e-3a78-ae94-3697f56d3701 | -21.44892 | -43.907 | 2025-10-07 04:12:00 | NOAA-21 | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 376676c3-1048-3df7-a9b8-080555c9ab42 | -23.37834 | -47.19704 | 2025-10-07 04:12:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e0d503be-e38d-3f7d-abfa-b57d69ef137b | -22.54515 | -44.9877 | 2025-10-07 04:12:00 | NOAA-21 | CRUZEIRO | SÃO PAULO | Brasil | 3513405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 7797e394-a49e-3ad3-a632-fa6e2d4ec3fc | -21.06921 | -44.68156 | 2025-10-07 04:12:00 | NOAA-21 | BOM SUCESSO | MINAS GERAIS | Brasil | 3108008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9ceffb18-55e2-35d2-962e-c1765052ab96 | -20.82337 | -42.48249 | 2025-10-07 04:12:00 | NOAA-21 | MIRADOURO | MINAS GERAIS | Brasil | 3142106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 42d8713e-a9d1-3f88-a687-eb3916277c13 | -22.53071 | -43.58513 | 2025-10-07 04:12:00 | NOAA-21 | ENGENHEIRO PAULO DE FRONTIN | RIO DE JANEIRO | Brasil | 3301801 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1898f5c0-e2b9-3e22-802e-4e7c413c21ac | -21.95631 | -44.88133 | 2025-10-07 04:12:00 | NOAA-21 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c87ea697-9be6-32ed-824a-f3488d02f536 | -23.31627 | -45.75729 | 2025-10-07 04:12:00 | NOAA-21 | JAMBEIRO | SÃO PAULO | Brasil | 3524907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| fcdf28f2-c107-36e8-b453-3cf24c79b4af | -20.75015 | -43.46998 | 2025-10-07 04:12:00 | NOAA-21 | LAMIM | MINAS GERAIS | Brasil | 3137908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 47cfedd0-2bfb-39d8-b8d4-1d0659f36230 | -21.90288 | -44.87572 | 2025-10-07 04:12:00 | NOAA-21 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 424be647-b661-31e5-997b-d171dd60f9ec | -21.80147 | -46.15784 | 2025-10-07 04:12:00 | NOAA-21 | CAMPESTRE | MINAS GERAIS | Brasil | 3111002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| cb7e1ef0-6608-3c59-8a6d-3cb9dc30e39d | -21.4959 | -45.28201 | 2025-10-07 04:12:00 | NOAA-21 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 29a073ee-bdd7-3da2-8a3d-4d67a5a71158 | -20.86652 | -43.44165 | 2025-10-07 04:12:00 | NOAA-21 | RIO ESPERA | MINAS GERAIS | Brasil | 3155207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9df9893d-2fb9-31b1-b217-6c43225186a4 | -21.09532 | -44.17834 | 2025-10-07 04:12:00 | NOAA-21 | TIRADENTES | MINAS GERAIS | Brasil | 3168804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3bdea6cd-9d70-3f69-8a03-9861a4118f1b | -20.83039 | -43.61492 | 2025-10-07 04:12:00 | NOAA-21 | SANTANA DOS MONTES | MINAS GERAIS | Brasil | 3159100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c5be78c0-f06c-336c-bd6b-dcdb73b3b660 | -23.27921 | -45.51604 | 2025-10-07 04:12:00 | NOAA-21 | REDENÇÃO DA SERRA | SÃO PAULO | Brasil | 3542305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7fab1166-7b7d-36ef-a7e4-9ab0ae7554f5 | -21.86485 | -42.88357 | 2025-10-07 04:12:00 | NOAA-21 | MAR DE ESPANHA | MINAS GERAIS | Brasil | 3139805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8bcb739a-8c92-38df-9aac-d624c80b9708 | -22.09279 | -44.79093 | 2025-10-07 04:12:00 | NOAA-21 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 3f9b9e6b-332f-383d-be05-34175bc4d437 | -22.16241 | -49.38491 | 2025-10-07 04:12:00 | NOAA-21 | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5559ad65-be1e-3406-afe0-8f398dae0c33 | -23.31156 | -46.94373 | 2025-10-07 04:12:00 | NOAA-21 | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2fad2538-fc7b-30bb-87d8-3fb73530b182 | -23.39538 | -47.012 | 2025-10-07 04:12:00 | NOAA-21 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 32636e1c-d7f5-3bc7-8cbf-f7eae736b08a | -21.08213 | -46.9083 | 2025-10-07 04:12:00 | NOAA-21 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e42563f4-f707-3a5c-be57-fed388907b27 | -21.5988 | -45.27718 | 2025-10-07 04:12:00 | NOAA-21 | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2448d46d-3a04-3c75-b531-333d77fe2fee | -22.32178 | -47.13546 | 2025-10-07 04:12:00 | NOAA-21 | CONCHAL | SÃO PAULO | Brasil | 3512209 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cc9190e6-5200-3460-9767-661c3583db4e | -20.82623 | -42.48744 | 2025-10-07 04:12:00 | NOAA-21 | MIRADOURO | MINAS GERAIS | Brasil | 3142106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| e0f59231-82d4-3c0e-8c06-c1109a3ee237 | -22.01472 | -49.55359 | 2025-10-07 04:12:00 | NOAA-21 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 84bab539-6d0d-39e6-94a4-9113db89b9f5 | -21.18779 | -45.61432 | 2025-10-07 04:12:00 | NOAA-21 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e9269ef9-5d38-3afd-83b6-03e70a38686a | -21.90891 | -44.88058 | 2025-10-07 04:12:00 | NOAA-21 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 330f5da3-df88-30f0-9414-46a429cdc60f | -22.01119 | -49.72357 | 2025-10-07 04:12:00 | NOAA-21 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 38c2da21-0631-3b3f-8625-0a96abf609ad | -22.17726 | -49.38821 | 2025-10-07 04:12:00 | NOAA-21 | AVAÍ | SÃO PAULO | Brasil | 3504305 | 35 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 0e7509bc-4c9d-37c5-bee2-c23be8ce7aa1 | -22.11477 | -45.00046 | 2025-10-07 04:12:00 | NOAA-21 | POUSO ALTO | MINAS GERAIS | Brasil | 3152600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| bfcf6c33-6b18-3a77-8d8b-b7c9a36b21a8 | -22.1142 | -45.00416 | 2025-10-07 04:12:00 | NOAA-21 | SÃO LOURENÇO | MINAS GERAIS | Brasil | 3163706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| fb1cff93-cd30-3789-93d8-c6f2d349abdf | -22.00452 | -49.71693 | 2025-10-07 04:12:00 | NOAA-21 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| 78375fc2-6089-3419-984c-efbf2791affb | -22.015 | -49.72431 | 2025-10-07 04:12:00 | NOAA-21 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 26468bc9-aa08-3043-bdaf-a5202b028298 | -22.02591 | -49.72352 | 2025-10-07 04:12:00 | NOAA-21 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 81a715d0-f562-331f-9a21-0af9a16964c9 | -20.98202 | -45.58119 | 2025-10-07 04:12:00 | NOAA-21 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e522814-5ce8-3fe7-81bd-5f6d4d287b1d | -21.0794 | -46.90368 | 2025-10-07 04:12:00 | NOAA-21 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 54006eb7-69e1-3a05-82d3-ecb27e2ed111 | -21.30419 | -45.94884 | 2025-10-07 04:12:00 | NOAA-21 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8f91ba7a-33af-39df-be08-94fb949ba4d7 | -21.1314 | -42.9499 | 2025-10-07 04:12:00 | NOAA-21 | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 147f43a4-a51d-3299-9f00-77d9fd4ba80e | -22.52225 | -43.57146 | 2025-10-07 04:12:00 | NOAA-21 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 2b3b0e77-0001-373b-b0c0-cb56b3a45624 | -21.44835 | -43.91078 | 2025-10-07 04:12:00 | NOAA-21 | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3c196888-7dba-3f72-9cdb-18f75c5876ba | -21.4926 | -45.28142 | 2025-10-07 04:12:00 | NOAA-21 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| abde0a55-ad51-3da1-8ec2-6c8c20db2088 | -22.02352 | -49.72079 | 2025-10-07 04:12:00 | NOAA-21 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| a90bebb2-60eb-3dc2-abd6-172f552ae6df | -22.81431 | -42.9672 | 2025-10-07 04:12:00 | NOAA-21 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b222f602-1375-3ade-a265-07cbf55ab7e0 | -21.8036 | -43.86739 | 2025-10-07 04:12:00 | NOAA-21 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 3deba25b-3153-3114-ac49-41ae8f53453c | -21.19168 | -45.61124 | 2025-10-07 04:12:00 | NOAA-21 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7a22adef-c653-36ca-8e14-87cabe4afa4a | -21.62465 | -44.00204 | 2025-10-07 04:12:00 | NOAA-21 | SANTANA DO GARAMBÉU | MINAS GERAIS | Brasil | 3158706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| aa35e12f-0d1d-3b2a-8265-0736d0c2c524 | -21.52502 | -45.59114 | 2025-10-07 04:12:00 | NOAA-21 | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6873254f-dedb-3954-9ce7-41b3489b4624 | -21.77201 | -47.77972 | 2025-10-07 04:12:00 | NOAA-21 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0f99c41b-7938-3adf-b689-71dd3ce483f0 | -22.00648 | -49.72778 | 2025-10-07 04:12:00 | NOAA-21 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 4f7b22f2-b0ad-3c92-9644-798ebb01878d | -23.1514 | -46.57097 | 2025-10-07 04:12:00 | NOAA-21 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 08cca142-c375-34c0-97f8-b8bfb952256e | -23.33366 | -46.78933 | 2025-10-07 04:12:00 | NOAA-21 | FRANCO DA ROCHA | SÃO PAULO | Brasil | 3516408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9b6679ad-17cc-30d1-bfad-2a5769690bcd | -23.23344 | -47.34771 | 2025-10-07 04:12:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0f2f755d-fe94-3241-9564-00988348663e | -20.03526 | -48.2379 | 2025-10-07 04:12:00 | NOAA-21 | MIGUELÓPOLIS | SÃO PAULO | Brasil | 3529708 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8b20c64c-e715-3270-9b80-cdcb4116e613 | -21.62521 | -43.99826 | 2025-10-07 04:12:00 | NOAA-21 | SANTANA DO GARAMBÉU | MINAS GERAIS | Brasil | 3158706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| ef6f29cc-e0de-3a62-9536-f06add193c3c | -22.97784 | -47.60778 | 2025-10-07 04:12:00 | NOAA-21 | MOMBUCA | SÃO PAULO | Brasil | 3530904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 913f0af2-8f73-313b-ad63-bae487900b16 | -10.4288 | -50.3305 | 2025-10-07 04:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 6369125d-7068-3100-bd5d-70d75142ac33 | -5.5127 | -43.0512 | 2025-10-07 04:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 70b0057f-f4e8-35b7-8009-ad9957026efe | -10.4291 | -50.3091 | 2025-10-07 04:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 168.5 |
| b52c7dda-743d-3fe6-8886-4c134951b457 | -4.6689 | -45.829 | 2025-10-07 04:20:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 15da19d0-eede-37ca-938b-150e47785b2a | -10.8921 | -51.0269 | 2025-10-07 04:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 5d6eadfb-c7fd-31a7-a918-2a097c0fde31 | -4.7061 | -45.8269 | 2025-10-07 04:20:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 66.9 |
| b231ca0b-241b-36eb-a299-2262daecc4e5 | -10.4102 | -50.311 | 2025-10-07 04:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 35e2a56e-126b-3fee-a40d-a8c8670323d1 | -8.5398 | -46.2181 | 2025-10-07 04:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 707b4de3-99ed-3c97-80ac-08a7c7390d9a | -10.8731 | -51.0289 | 2025-10-07 04:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 11d64e9c-0d80-3211-bacb-4e12588f4a87 | -3.0827 | -47.0088 | 2025-10-07 04:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 217784e9-dbfa-3274-a4ee-4a82ae82de17 | -10.4105 | -50.2897 | 2025-10-07 04:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 0270d1f5-e72c-3ab2-b57b-aad0c1b8f4be | -5.494 | -43.0526 | 2025-10-07 04:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 561cf1e4-4e76-3ce5-a435-534efa42f558 | -13.5072 | -43.6594 | 2025-10-07 04:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 5e1213b3-c401-3170-9b9a-4c3807b10a0f | -13.541 | -42.9835 | 2025-10-07 04:20:00 | GOES-19 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 133.3 |
| c345befc-0530-3f83-a4c6-23f6a5dd7e7f | -8.5395 | -46.2406 | 2025-10-07 04:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 5d5d9514-b2cb-3f31-960e-764f97a8d4b3 | -4.6875 | -45.828 | 2025-10-07 04:20:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 136.4 |
| c3c796aa-5880-3f08-a2e7-91389fb0363d | -22.5468 | -44.4405 | 2025-10-07 04:20:00 | GOES-19 | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 70.3 |
| 2e3d1e7d-da0b-3c00-b316-fbceaced12c9 | -3.1013 | -47.0082 | 2025-10-07 04:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| e55b82a9-ee71-318f-ad6f-6acea5118025 | -5.4937 | -43.0761 | 2025-10-07 04:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 84.7 |
| c2c0c8b1-f00e-38ac-8ac3-485ea6889674 | -11.0259 | -50.928 | 2025-10-07 04:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 52.2 |
| dd8484b0-6d27-39e8-b238-304617754d6d | -4.6873 | -45.8504 | 2025-10-07 04:30:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 110.8 |
| 491c8ad8-1b65-3ba4-971b-4e227a3af060 | -10.4102 | -50.311 | 2025-10-07 04:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 179.5 |
| cdd40fbf-764b-338e-95e6-1db7b0ad3c0a | -3.0826 | -47.0308 | 2025-10-07 04:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 31335fec-04ce-3a5b-890d-3968db60bd20 | -10.3916 | -50.2916 | 2025-10-07 04:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 130.0 |
| fb56b4c1-c0ab-34fa-84cc-0cb380352eae | -10.3913 | -50.313 | 2025-10-07 04:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 2e5e354c-61e2-32e2-adff-abcea278b44e | -10.4291 | -50.3091 | 2025-10-07 04:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 158.2 |
| 0a8f7c49-060b-3b2a-a887-0fec838f5c8e | -3.1012 | -47.0301 | 2025-10-07 04:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| e17b367c-8079-36d7-a248-bc6f8b820391 | -3.0827 | -47.0088 | 2025-10-07 04:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 2b719320-8da5-374d-a0a7-690b314ca5d3 | -3.1013 | -47.0082 | 2025-10-07 04:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| ffd33246-7554-3266-8436-b873b15a1d00 | -10.4105 | -50.2897 | 2025-10-07 04:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 906bc459-3438-3e69-b4f3-037895c2342f | -4.6875 | -45.828 | 2025-10-07 04:30:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 99.8 |
| b32925b6-408b-3add-b3a2-2eeb81bff343 | -10.4288 | -50.3305 | 2025-10-07 04:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 158.7 |
| 43e9d754-35b6-35de-aaa4-a119c1d0047b | -3.87869 | -41.54824 | 2025-10-07 04:34:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 550b2e34-dce1-3b12-ad7f-aa11baa6c0e9 | 0.7517 | -51.58102 | 2025-10-07 04:34:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e4afdaf5-a417-33e9-b873-d3929dd069b6 | -3.22028 | -50.79865 | 2025-10-07 04:34:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 048d15c3-a269-336e-a58f-ffe0bde0cfc2 | -2.26903 | -47.19291 | 2025-10-07 04:34:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c7ab5e1b-4b76-375d-af26-598b7faa7b7c | -5.20355 | -37.62633 | 2025-10-07 04:34:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 854f5bd2-b86e-3796-b78b-c04fec6d1132 | -4.06591 | -44.51041 | 2025-10-07 04:34:00 | NPP-375D | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| a885b9f9-fecd-366a-883a-b1edf8452223 | -3.14215 | -50.44732 | 2025-10-07 04:34:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 49e467af-648f-3308-9064-115b22e3ef8f | -3.20023 | -51.01964 | 2025-10-07 04:34:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5c450e46-9638-3415-82ba-d090dea4f4fe | -4.45155 | -43.22619 | 2025-10-07 04:34:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 28.8 |
| ce74c034-9147-3a37-a121-9758fd0c6180 | -2.88726 | -50.73294 | 2025-10-07 04:34:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README49.md)
