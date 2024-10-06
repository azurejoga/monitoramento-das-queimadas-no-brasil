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

## Dados Diários - Página 101

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e7985239-0979-3992-b45a-10c81b8bebb1 | -2.81273 | -58.36312 | 2024-10-06 05:10:00 | NOAA-21 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dd54e732-80e0-390d-b63b-5e48eae0f113 | -2.62459 | -59.37503 | 2024-10-06 05:10:00 | NOAA-21 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5953ac5a-bb62-3f83-928d-1fc9cd1ba1f5 | -2.62104 | -59.37447 | 2024-10-06 05:10:00 | NOAA-21 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4851ff97-947e-3624-ba47-159a05e6815d | -3.52809 | -59.39682 | 2024-10-06 05:10:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 2eb70847-c579-3090-8ad0-f7d7dd86365f | -4.28959 | -60.01583 | 2024-10-06 05:10:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 399e17b0-1dee-3e78-87d8-712595485f89 | -4.28893 | -60.01996 | 2024-10-06 05:10:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ba16e341-630c-383d-baec-2623e4910e23 | -4.28599 | -60.01526 | 2024-10-06 05:10:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e8ecd1c9-cabb-3077-92f7-3a3ccd8870ca | -4.28534 | -60.01939 | 2024-10-06 05:10:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5236da9f-d0ef-31de-8360-3e67b6e431aa | -4.2824 | -60.01469 | 2024-10-06 05:10:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bd816b4a-03a4-3a2e-a8b9-803219906022 | -4.28174 | -60.01883 | 2024-10-06 05:10:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 20056571-6af7-3f48-8406-71905aba2ebb | -4.22573 | -59.95504 | 2024-10-06 05:10:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0ce3be98-ad9b-3949-9223-4fee691b91bf | -3.88945 | -59.7257 | 2024-10-06 05:10:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| beb2fe14-9a5d-3667-bc78-8298e05256fd | -3.86583 | -58.56827 | 2024-10-06 05:10:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 28c53b4f-c3f4-3623-9628-42c282c946b5 | -5.49796 | -60.4618 | 2024-10-06 05:10:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7f705cc2-c1e5-37d5-8f2e-521cc0e5399c | -3.03384 | -61.68413 | 2024-10-06 05:10:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8155c247-c7c6-3b0a-ada4-ef71aab2f299 | -11.67247 | -45.24791 | 2024-10-06 05:12:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9a725032-ea17-3845-b9fe-f3768b5f2a64 | -11.66558 | -45.2471 | 2024-10-06 05:12:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6156db57-62ae-33aa-a8bb-07c2dd8e8f7e | -10.61294 | -45.1898 | 2024-10-06 05:12:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b65a1082-2e3f-3e8b-8f8c-b7c43c241a1e | -10.48585 | -45.18554 | 2024-10-06 05:12:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 7a7a68ef-9803-3a34-989d-788667296265 | -10.48512 | -45.19181 | 2024-10-06 05:12:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 8098eb89-d919-39f8-b68a-c52da67bfa84 | -11.33506 | -45.54741 | 2024-10-06 05:12:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1f9598d7-18e4-3b63-8f59-fc41187ab7f6 | -9.36499 | -64.33373 | 2024-10-06 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| bb39ccb4-08ab-32b4-9570-f61c4bd9ff6d | -9.36214 | -64.32454 | 2024-10-06 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b56c9c55-9404-3732-83d0-95af00400727 | -9.36139 | -64.32876 | 2024-10-06 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d667900c-4e00-34ac-8a64-92508206da06 | -9.3089 | -65.38571 | 2024-10-06 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a3c05f5d-d14f-3def-a1b8-11a59a27eb63 | -9.30514 | -65.37983 | 2024-10-06 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4741e3fd-8528-3831-a1c5-59e717b8676e | -9.30424 | -65.38484 | 2024-10-06 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d748d04f-ebcb-3f69-936a-d32881ca0f22 | -9.2946 | -65.33158 | 2024-10-06 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 067ecfec-8639-3d92-828d-45148102c28c | -9.29122 | -65.33399 | 2024-10-06 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 07951d60-d29b-39ba-ba0d-a507d591a052 | -9.28385 | -65.4175 | 2024-10-06 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9034059-53c2-3f5a-910c-0d667cd77b26 | -9.26653 | -65.36526 | 2024-10-06 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 83ba9e73-2943-3327-a2f9-36868973ece8 | -8.65566 | -64.29558 | 2024-10-06 05:12:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c57c8130-1ccc-3a2f-acef-be6f40533d44 | -9.50734 | -65.59867 | 2024-10-06 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f582d77e-320f-3373-aecc-7e42980841a0 | -9.47234 | -64.72837 | 2024-10-06 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1587bddd-8514-3a8d-bd6c-9b10e7e69de5 | -9.36817 | -65.51582 | 2024-10-06 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9221a87e-061f-3dac-84bb-9fc78291a9ba | -9.36554 | -65.51244 | 2024-10-06 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 899c48e5-2480-3296-9b31-21258f9a62c7 | -10.41642 | -64.86997 | 2024-10-06 05:12:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b8d4468-b1cf-3db9-bc51-7a09f5c413ff | -9.9533 | -65.24444 | 2024-10-06 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e60b7a5f-b396-324a-b68f-b0cf6c1467ba | -9.95293 | -65.24679 | 2024-10-06 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 27595cf9-40d1-3d7f-b3ea-7080b83fae56 | -9.95247 | -65.2492 | 2024-10-06 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5a2b0cdc-17fc-35cf-9e69-27550207c625 | -9.68916 | -64.62717 | 2024-10-06 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 28.0 |
| f959999e-9993-38de-8718-7f075b3e5115 | -9.68839 | -64.63158 | 2024-10-06 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 1707bfb4-925a-3b29-ad10-9692ece69fed | -9.68475 | -64.62638 | 2024-10-06 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 24.2 |
| ddb7daa1-41f7-3d86-8d00-0a8facd27987 | -9.68398 | -64.63079 | 2024-10-06 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 9350cf0f-f5e9-3ba7-a4d9-e21d7a7fcd80 | -9.68034 | -64.6256 | 2024-10-06 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 0f856098-45d0-3785-8bf1-55900d08b38b | -9.50642 | -65.60381 | 2024-10-06 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 44e473e3-eb3b-3e05-8260-fd09839304b7 | -9.3761 | -65.47027 | 2024-10-06 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 36d160b7-e0a3-3d25-b7e5-cf37ad88249f | -9.36933 | -65.51829 | 2024-10-06 05:12:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 85007d2e-93a1-3cde-99e5-b4cc5532d71c | -13.09857 | -46.38205 | 2024-10-06 05:12:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 37bf068c-3a1b-3ca3-b4e7-2703d6e4e8e8 | -13.09795 | -46.38771 | 2024-10-06 05:12:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 65815814-6a04-3e83-984b-4f926f4ca6e8 | -13.09659 | -46.33959 | 2024-10-06 05:12:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5eebf251-0006-3e21-8537-a13151748537 | -13.09617 | -46.34342 | 2024-10-06 05:12:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e6af88d1-a7c2-3b2e-bfde-fb5fe35cb121 | -13.09569 | -46.34771 | 2024-10-06 05:12:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 9b045fa0-fbf6-36a0-922a-1681573fc05a | -13.09512 | -46.35297 | 2024-10-06 05:12:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 42897d7b-a654-328f-bc13-acc662c595eb | -12.51484 | -45.29956 | 2024-10-06 05:12:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 21669c43-6d8a-3364-8711-c8e1e1ef6c77 | -8.54796 | -67.12483 | 2024-10-06 05:12:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| dc8b9db0-e0f0-3423-996a-fc2b94f329f8 | -8.54734 | -67.12819 | 2024-10-06 05:12:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1e9c1e63-d3ec-3964-8b38-45c19fef3508 | -8.54672 | -67.13155 | 2024-10-06 05:12:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1d9eae7a-fcc3-3e45-89b5-03c105a69e6f | -9.07445 | -67.66431 | 2024-10-06 05:12:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01b84857-e995-302c-83d0-de86094cd084 | -10.52968 | -67.73898 | 2024-10-06 05:12:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 88f4e6d1-bb73-31ef-bd93-3bffa8f7b55b | -10.52904 | -67.74241 | 2024-10-06 05:12:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 61892a26-69b4-3405-bab2-9a0c2846fce1 | -10.28659 | -68.03053 | 2024-10-06 05:12:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f82da12a-7d3b-3473-a137-339ed56e13d2 | -10.10383 | -68.06432 | 2024-10-06 05:12:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 00a4af56-d84c-343d-8e0e-ce52cbfd8ace | -10.10313 | -68.06799 | 2024-10-06 05:12:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 827cc3b7-66a6-343d-8949-4149a9049bb8 | -10.10221 | -68.2844 | 2024-10-06 05:12:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 54125af4-0e4f-3ad7-b46e-f03b16e13eb7 | -10.05669 | -68.37118 | 2024-10-06 05:12:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 59009db1-7adb-3ecd-97ad-20efe6a4dedb | -10.05594 | -68.37507 | 2024-10-06 05:12:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 145b6f73-d94b-3fe5-b4ac-f326637a99eb | -9.71702 | -67.73198 | 2024-10-06 05:12:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00b1a869-f40a-34be-8ba3-8e00b42bf854 | -12.50793 | -45.29858 | 2024-10-06 05:12:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 884d31e7-c66e-3df1-b403-18be1c2d4d8c | -9.71633 | -67.73561 | 2024-10-06 05:12:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b6ff2525-5130-3bf4-bceb-89651ed6bbbc | -9.7152 | -67.73365 | 2024-10-06 05:12:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8e998d39-e904-359c-8ea4-e33f7b7740e3 | -9.7116 | -67.73096 | 2024-10-06 05:12:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 22b4201a-ce45-3cd8-a8e5-b1a80c5d8cb1 | -9.7109 | -67.73459 | 2024-10-06 05:12:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1146e76c-38ba-3d7f-aa1c-4cd194665f65 | -12.51463 | -45.29801 | 2024-10-06 05:12:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1e0da6b0-8111-3e45-a0cd-22730211c5b0 | -12.50772 | -45.29698 | 2024-10-06 05:12:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5a99ce8e-ece0-397a-8740-5ef867aa924e | -14.09042 | -45.49812 | 2024-10-06 05:12:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3f453bfd-ae0e-3507-8303-33788b2d7614 | -14.08973 | -45.50472 | 2024-10-06 05:12:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 48c7ea7c-f5cc-3515-9289-5f348dcadcfa | -14.08905 | -45.51115 | 2024-10-06 05:12:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| a22f0f38-1d09-3e26-a38d-fd50d7f2444d | -14.08836 | -45.51767 | 2024-10-06 05:12:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 0eab41d9-bd38-3b1c-a088-7f4dddd49f1c | -14.08767 | -45.5242 | 2024-10-06 05:12:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| dfe6d749-58b9-3656-ad2a-98b85a96a17d | -14.08416 | -45.49062 | 2024-10-06 05:12:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| eb16d964-da61-3106-a5b6-30eca245fa32 | -14.08346 | -45.49729 | 2024-10-06 05:12:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f435fd46-35d9-35ce-8662-4073868c3653 | -14.08005 | -45.52975 | 2024-10-06 05:12:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d8a9122d-4abf-3617-973e-e33b32860aa3 | -13.58272 | -48.14326 | 2024-10-06 05:12:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0f4c2dbc-843d-31c1-a476-5e8e9e663794 | -9.34506 | -46.5346 | 2024-10-06 05:12:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 684f25b9-b1e4-3bc7-ae99-6b34f1f37f10 | -9.34384 | -46.54449 | 2024-10-06 05:12:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| bc036883-1744-3f54-8551-702e76b47891 | -9.33703 | -46.54864 | 2024-10-06 05:12:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 5f32bcd2-3391-3818-9407-e026b777c5d0 | -9.33644 | -46.55342 | 2024-10-06 05:12:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 1ab226b1-f59b-3f5d-bc31-bde83775afed | -9.33584 | -46.55828 | 2024-10-06 05:12:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 8894d359-3842-3ced-a1c3-0cde78b0b848 | -8.6187 | -46.49922 | 2024-10-06 05:12:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b292d8c7-3d07-3086-ad48-5716e01e2ac8 | -8.61313 | -46.49384 | 2024-10-06 05:12:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b0c27095-1ffb-35a5-bf97-c7d1f083f5cb | -8.45257 | -46.43039 | 2024-10-06 05:12:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c18ae59d-13a0-3bbc-ac62-f27c0331af9d | -8.45195 | -46.4351 | 2024-10-06 05:12:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c03c6381-effc-30dc-a624-d2f03d157445 | -9.34444 | -46.53962 | 2024-10-06 05:12:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| f61988bb-3026-3093-a335-6aa1e3417bcc | -9.34324 | -46.5493 | 2024-10-06 05:12:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0b6a16e5-8182-3725-92fc-e833d8c366ca | -9.34265 | -46.5541 | 2024-10-06 05:12:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0fb1a233-2648-3a80-b088-3508f763db74 | -9.33824 | -46.53885 | 2024-10-06 05:12:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 247eecc3-737c-3f09-9b86-3bbbd06d2dfb | -9.33763 | -46.54379 | 2024-10-06 05:12:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c1ab26f8-3418-3106-8fd2-cc7ba33ccc2b | -8.61252 | -46.49865 | 2024-10-06 05:12:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8fef97c6-cc1e-37d5-ad78-9daaa3742136 | -8.39677 | -46.28726 | 2024-10-06 05:12:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |


[Clique aqui para ver as próximas entradas](README102.md)
