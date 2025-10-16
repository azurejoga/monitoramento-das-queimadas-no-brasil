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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b6f78930-1ada-3158-b326-5f0d699f32bd | -6.06428 | -44.31501 | 2025-10-16 05:08:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 121c9896-1b50-39e7-b859-62f51449c92a | -7.93791 | -44.12527 | 2025-10-16 05:08:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b10d6191-7d75-3b39-b7ee-7e90f3348bf6 | -6.74808 | -44.37485 | 2025-10-16 05:08:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0200f91c-14b7-3f27-ab24-88bc409ff43b | -8.46897 | -44.19806 | 2025-10-16 05:08:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 071ce9db-9805-3e31-ad2c-5843d5c6744c | -9.68057 | -44.50293 | 2025-10-16 05:08:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c6ca7b82-a3d7-3570-b763-c3539565e1aa | -8.45014 | -44.18855 | 2025-10-16 05:08:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d5154720-7bf4-3818-a153-8d58ed827aed | -9.22393 | -48.60307 | 2025-10-16 05:08:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| b77da8e1-438a-3e75-bf14-238e69865f90 | -11.33365 | -55.06139 | 2025-10-16 05:08:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 04ac0fac-f8bc-325f-b4eb-b9340c6731d3 | -11.60091 | -48.55302 | 2025-10-16 05:08:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 98d5a368-d370-30f3-a28f-51510eb96b50 | -10.88683 | -47.93118 | 2025-10-16 05:08:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2680a55a-62dd-3cff-8511-ad1a33b54a72 | -10.03296 | -43.83302 | 2025-10-16 05:08:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ff8d8044-e467-3502-89e4-e7b4c322decc | -5.8773 | -43.85578 | 2025-10-16 05:08:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3ad0bc14-e480-3638-966c-fbd2e1c7c197 | -6.83379 | -44.64595 | 2025-10-16 05:08:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7620db99-28b1-3e7a-a05b-93f034cc533b | -7.00586 | -43.74616 | 2025-10-16 05:08:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| a23b2b1c-be0b-3785-b9a6-d97022169285 | -7.35525 | -43.85544 | 2025-10-16 05:08:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0f662097-bdda-3e88-afe1-ebee4d8f98e9 | -6.12918 | -44.29079 | 2025-10-16 05:08:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 51595579-6f7c-30f7-942d-905e76389a29 | -9.68364 | -44.53021 | 2025-10-16 05:08:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d3e1df6a-d397-38e4-877a-409deb38b393 | -8.39241 | -46.25719 | 2025-10-16 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8a2ba775-f2a2-3e16-91f8-21a7d6198c59 | -7.16951 | -42.51144 | 2025-10-16 05:08:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 80d42c66-ab71-3f85-80d9-6f07d06cc241 | -10.14284 | -44.54452 | 2025-10-16 05:08:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bf9b9700-4855-35d5-9ee2-b0034c28afaa | -6.21888 | -47.04047 | 2025-10-16 05:08:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 798496de-dc41-3aac-98ab-90c665af30eb | -6.95233 | -47.74625 | 2025-10-16 05:08:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 88e03871-2a1b-39af-83a9-381747c944e3 | -9.69398 | -44.50624 | 2025-10-16 05:08:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d236b45d-4488-3f15-a1e9-71ba0ac48609 | -9.69078 | -44.53246 | 2025-10-16 05:08:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1fad40a7-67af-3d54-aa3c-075dd3bf9c84 | -11.43138 | -44.13201 | 2025-10-16 05:08:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 85bfe68a-0f4b-390c-9bfe-b8cd700e31da | -8.27173 | -43.36238 | 2025-10-16 05:08:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f3a39e7b-e79d-309e-90f0-0923f09aacbe | -8.46905 | -46.24733 | 2025-10-16 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a4d3bd9e-1afe-3528-82fc-fd75ee3f30e6 | -7.61412 | -46.47937 | 2025-10-16 05:08:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| afc3a539-106f-3eca-ac5f-9bd307f5dff2 | -6.321 | -46.32063 | 2025-10-16 05:08:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1af36e5d-56ab-332e-b9f8-d225bf29000a | -6.19889 | -44.10904 | 2025-10-16 05:08:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de543bfb-b39f-32b0-8102-bc76e138d35c | -4.67317 | -49.33516 | 2025-10-16 05:08:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 35dba6bb-690e-3208-acb1-9784cde5511a | -7.53526 | -44.28063 | 2025-10-16 05:08:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c4794d39-e7f4-3f7d-9fcb-77affb4530e9 | -4.619 | -49.5531 | 2025-10-16 05:08:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 72e8db49-89ae-3174-8ca1-449f7cb94e71 | -6.32599 | -46.32503 | 2025-10-16 05:08:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c8defffa-7cab-3aaf-909e-628ff3c35dd4 | -7.47338 | -42.76169 | 2025-10-16 05:08:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 362a8bf2-cf04-3c4f-944f-310fe49623fc | -6.70859 | -44.38316 | 2025-10-16 05:08:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| db3c2a14-7c0a-32b5-a001-efa246437986 | -11.54765 | -49.92042 | 2025-10-16 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8f8a7bae-a7fb-3455-af0b-44ac76b08a6c | -7.66185 | -42.38658 | 2025-10-16 05:08:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ac4b134f-726a-3b81-9a57-df4c78eda37b | -8.45805 | -44.17866 | 2025-10-16 05:08:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 12.6 |
| eb0fc196-1f7d-3c75-a65b-603bea6304d6 | -10.64627 | -45.24858 | 2025-10-16 05:08:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5e6b7001-f580-34b1-bfab-e720eed3ec9c | -6.26541 | -42.89891 | 2025-10-16 05:08:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eb81ed11-d36b-3215-9f8a-abd294fd4461 | -6.82767 | -44.6447 | 2025-10-16 05:08:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83eb9ee5-777e-3674-813f-b21309fd9251 | -10.12486 | -44.58409 | 2025-10-16 05:08:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| fe763e41-2630-3afa-bf26-ecdd80d3c468 | -7.46616 | -42.6699 | 2025-10-16 05:08:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6262efc6-5385-3e8d-b75f-444b58b01c71 | -8.20057 | -43.97602 | 2025-10-16 05:08:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f6b53f12-c3eb-34c0-b504-ed3ba6725650 | -5.34917 | -43.75232 | 2025-10-16 05:08:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cf52cc0a-fa48-3df5-94a7-705ae8a5b21c | -10.12859 | -44.55336 | 2025-10-16 05:08:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e3aeca48-e9cb-332e-98a2-b3e1ffc0e94b | -5.87287 | -43.88837 | 2025-10-16 05:08:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a92cfee2-1802-314f-82be-94368b6e0d94 | -7.61576 | -46.47737 | 2025-10-16 05:08:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4c4a6277-33bb-3e58-a099-7a49a136c4b0 | -8.45126 | -44.18149 | 2025-10-16 05:08:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 094518b6-d0e1-3eef-b552-266215042a39 | -7.11681 | -44.72125 | 2025-10-16 05:08:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0d4bb575-009c-38d2-97e9-7080a8cff449 | -7.20476 | -45.48499 | 2025-10-16 05:08:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3905ed93-4bde-3637-8035-dbd7fd87cd95 | -8.4506 | -44.18675 | 2025-10-16 05:08:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 5d722d87-0bb8-3d21-93aa-568d0a37ab4e | -6.12431 | -44.29573 | 2025-10-16 05:08:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f1666362-e1fd-370e-b7c8-26a48f6a7443 | -8.24593 | -44.03314 | 2025-10-16 05:08:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f38a379b-8c8c-3449-b0a0-11f9eae0c0bd | -6.24547 | -44.01532 | 2025-10-16 05:08:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e5e0bf7d-cfd1-3cc9-ab84-65083f0de1c0 | -9.71982 | -44.50974 | 2025-10-16 05:08:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e9f659e8-ff3f-3bb0-b3b9-0b2712c17cd6 | -5.88155 | -43.87253 | 2025-10-16 05:08:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d619f15a-d1a1-3b4d-bece-0869f02e7e5d | -10.80806 | -43.94534 | 2025-10-16 05:08:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c9a520f5-8a56-376c-8c65-8e6234d82aa7 | -11.43468 | -44.16294 | 2025-10-16 05:08:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 85d7e861-158b-3739-af4d-0455fcfb9cdd | -8.23991 | -44.03195 | 2025-10-16 05:08:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6fe9a639-9a0b-36ba-b9a3-c8caccefca49 | -9.49556 | -46.55449 | 2025-10-16 05:08:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f3e18ed2-5296-363b-8f2f-0d4502b6258f | -9.23127 | -48.59513 | 2025-10-16 05:08:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 395a78fd-cd60-359f-b023-e94e3b659dde | -5.68556 | -45.09732 | 2025-10-16 05:08:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| c8c16c4b-bdc3-3151-8192-da76d02453c0 | -5.86645 | -43.88079 | 2025-10-16 05:08:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bc221023-340b-3825-8b45-e533844b45b2 | -5.74056 | -44.98593 | 2025-10-16 05:08:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1dfa30a7-6e86-3b3f-a999-ba0fcfb36eee | -10.12024 | -44.56802 | 2025-10-16 05:08:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 621fe994-0cea-385b-8d34-442988bc62b3 | -7.40387 | -44.74984 | 2025-10-16 05:08:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aa3db637-eb4b-3ab7-9e9e-45b9e7c91128 | -4.91698 | -45.98142 | 2025-10-16 05:08:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1f5debe3-cc90-3fb2-8bfd-8340e59975f5 | -11.45955 | -44.1842 | 2025-10-16 05:08:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 738437ec-e305-3a6c-bde1-8463348f13a6 | -10.12296 | -52.34604 | 2025-10-16 05:08:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2171019-aab5-3c54-ac86-70e7ca9afa86 | -11.59543 | -48.55537 | 2025-10-16 05:08:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f981309e-4921-31e7-a0fb-e31569b11cfe | -10.52798 | -44.50767 | 2025-10-16 05:08:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3f8701ea-725d-33bc-9b7d-a2aca454872e | -5.42124 | -44.23767 | 2025-10-16 05:08:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ec1899b4-ffbd-3c77-88b6-e9319794dbc9 | -8.45911 | -46.19134 | 2025-10-16 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a907795d-3ae1-34d8-b034-7391193e3367 | -12.67215 | -43.43353 | 2025-10-16 05:08:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| a046cb29-7529-3fae-bce8-8844eac66d81 | -7.05758 | -45.05906 | 2025-10-16 05:08:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 10693544-153d-3509-8f1e-9ed16ee1b032 | -8.06116 | -45.42316 | 2025-10-16 05:08:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5eb1288f-61c8-3079-9e9a-2e2a57afd60c | -11.59581 | -48.55234 | 2025-10-16 05:08:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4b44931c-308b-3b9c-a935-45bd7ed670e7 | -7.47416 | -42.75546 | 2025-10-16 05:08:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 1f502aff-aedf-3b5e-8ef6-a4a53ffb809c | -5.87441 | -43.87707 | 2025-10-16 05:08:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f570ffbc-4eff-3597-87ba-50540451bbf6 | -10.87937 | -48.80517 | 2025-10-16 05:08:00 | NPP-375D | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| f33a6aaf-77a1-37ff-b541-f36f600d7d7d | -8.1985 | -47.00899 | 2025-10-16 05:08:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ed45ae5c-4f0c-332f-84c8-6f3d7cf54824 | -7.00743 | -43.74077 | 2025-10-16 05:08:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| bfc79946-2d4f-3a73-b164-ebd3a337257f | -5.47442 | -42.92668 | 2025-10-16 05:08:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 5d181a7b-eebe-3c61-b652-adf76ddd60f5 | -5.46684 | -42.93168 | 2025-10-16 05:08:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ae068a07-7cd0-3110-86cc-30f1742ef812 | -7.97033 | -44.12915 | 2025-10-16 05:08:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 818176ab-4547-3a87-8987-23865c2195c5 | -5.91987 | -45.434 | 2025-10-16 05:08:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6b7177c4-277d-3c59-b77d-ed8b77c4d717 | -9.68754 | -44.50518 | 2025-10-16 05:08:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7112e3b2-1ae7-3cae-9ac9-996b75cb1d86 | -8.06757 | -45.42079 | 2025-10-16 05:08:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 65e15db2-896e-3446-9220-9483f59b5177 | -5.65919 | -45.96147 | 2025-10-16 05:08:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2f693b59-2a7d-340a-acca-3a92b2964fa3 | -11.43001 | -44.14408 | 2025-10-16 05:08:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fa87a10e-041f-3590-8184-c4f01cae5965 | -6.71547 | -44.37955 | 2025-10-16 05:08:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a2741eec-c0d5-32da-8957-ff6aeb3fcdaf | -8.46957 | -44.19333 | 2025-10-16 05:08:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 19.6 |
| dede57b3-c170-3889-b440-72c0c78fedec | -5.87845 | -43.89524 | 2025-10-16 05:08:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 47c1026e-4ebb-3b7e-a0be-60dc618ce240 | -5.38372 | -48.91289 | 2025-10-16 05:08:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4c53bf05-f79e-361c-a6e4-13a4654899af | -6.19493 | -52.73203 | 2025-10-16 05:08:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 06d03306-634f-32e3-9192-4c69f9fcb7f1 | -9.15675 | -46.87186 | 2025-10-16 05:08:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f85bea95-e218-3859-a4c4-f71eea6a34ec | -7.61022 | -46.4766 | 2025-10-16 05:08:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 593003b2-0ea6-30c3-92c4-a5571840ffc9 | -7.39927 | -44.75037 | 2025-10-16 05:08:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README74.md)
