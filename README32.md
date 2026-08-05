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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 32e55305-48a4-3e29-beb7-4a83f5d09f05 | -12.575 | -46.9555 | 2026-08-05 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 167.2 |
| d71069bb-6bc6-3299-84d6-5c180458b7ca | -10.6184 | -46.3646 | 2026-08-05 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 48.8 |
| e402538b-d714-3af0-8963-8a671f502962 | -11.3111 | -44.7873 | 2026-08-05 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 06fc6c40-f91f-3bdb-a915-e578cf8d1d43 | -13.2604 | -54.2662 | 2026-08-05 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 95.4 |
| bd6edc38-576c-3648-a2d9-d9f8331f29d4 | -12.5754 | -46.9329 | 2026-08-05 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 168.2 |
| 0ccfe749-4af2-38f2-8375-a8e45c809ffe | -14.2687 | -45.2636 | 2026-08-05 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 5bdbd674-749c-3b18-9ea8-d99b209dd788 | -14.2682 | -45.287 | 2026-08-05 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 184.7 |
| dbb61ee4-ac13-3b5c-b925-03a37f15fc01 | -12.5942 | -46.9527 | 2026-08-05 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 7aca35d6-6a33-3f02-a102-a649e365075f | -14.3865 | -53.3877 | 2026-08-05 14:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 7b56c928-8458-3ae0-b3d6-14e6a12aee8b | -12.4386 | -50.5109 | 2026-08-05 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 153.8 |
| 185416b2-c2e0-384a-8ed7-be088aaedfdb | -6.5514 | -55.1569 | 2026-08-05 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 2998574b-6a78-3db9-ade8-eb9226307703 | -7.2187 | -43.3499 | 2026-08-05 14:30:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 102.3 |
| 02836a3f-b14f-309b-aeae-ee40eb5401a3 | -10.9192 | -50.4283 | 2026-08-05 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 218.9 |
| 3b797b5c-a00b-3e00-b05c-733de5b6d6cf | -12.4383 | -50.5324 | 2026-08-05 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 113.5 |
| a9688726-2391-3ed1-9758-3b69d1118fb5 | -14.2487 | -45.2904 | 2026-08-05 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 67947cdc-83a8-3300-9521-a38bfae96fa9 | -14.3579 | -47.5144 | 2026-08-05 14:30:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 75.7 |
| da8bfd90-1d94-3d33-b7d8-e3ddccc8390a | -12.5947 | -46.9301 | 2026-08-05 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| a9f1685d-a29d-3130-9815-bc2e8dcca094 | -11.292 | -44.7901 | 2026-08-05 14:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 8231be44-afe1-31c3-ae4c-ee2d5bc7f54c | -6.8904 | -42.4152 | 2026-08-05 14:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 115.6 |
| 8c87cc32-fdce-3cf0-a672-0f65e821f311 | -6.9879 | -42.1201 | 2026-08-05 14:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 102.2 |
| 49b0c1db-28ba-34c2-8888-e86c4f9432dd | -14.2687 | -45.2636 | 2026-08-05 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 3fda4ac4-17d5-339b-b2ad-fc6d419d49bd | -7.2293 | -45.7801 | 2026-08-05 14:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| e6c87cc2-32c3-3b17-9ac0-a116c4192ae2 | -7.4913 | -45.8468 | 2026-08-05 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 19369199-44ea-35e2-a08e-e87dacea81c3 | -14.1969 | -54.4309 | 2026-08-05 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 82.6 |
| ab9a1943-3d4e-3862-b41b-80d8246066c6 | -14.1972 | -54.4102 | 2026-08-05 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 16e1d0e4-b31d-35c8-b015-ac1f61f40a3a | -10.4681 | -50.2196 | 2026-08-05 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 5260be59-769e-300f-bbcd-46f82e00b829 | -6.8904 | -42.4152 | 2026-08-05 14:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 89.3 |
| f35eebcf-abda-3115-926b-4d0b4c647cf7 | -7.4913 | -45.8468 | 2026-08-05 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| e532c737-9a7d-33fe-8343-cb002eb24cfd | -14.0337 | -46.2964 | 2026-08-05 14:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 119.1 |
| cecb1f7c-cf0a-3dd2-af57-f1cc6056681b | -14.2687 | -45.2636 | 2026-08-05 14:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 81.5 |
| b7e91c3d-73a6-3728-b7b5-a6f71f246ced | -6.5329 | -55.1578 | 2026-08-05 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 4353d915-b308-36fe-a3ef-4bffeedae207 | -14.1969 | -54.4309 | 2026-08-05 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 9a97737d-cd75-35d7-bd6c-6e0ac7677c62 | -7.2293 | -45.7801 | 2026-08-05 14:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 191eb555-e871-38f7-8022-298fc24878e8 | -14.1776 | -54.4331 | 2026-08-05 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 992a4296-04d4-342c-a860-4048d97ef849 | -12.5951 | -46.9075 | 2026-08-05 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 41f69201-8653-386f-8304-a5f10cf1967d | -14.3579 | -47.5144 | 2026-08-05 14:40:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 6f40f793-0892-3567-8a48-3a400e5fcd4e | -6.5514 | -55.1569 | 2026-08-05 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 220c82d1-4938-3769-8afc-f6fe6d20e001 | -12.4386 | -50.5109 | 2026-08-05 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 9a3d9f4e-3736-31bf-9f6b-d95112027b9f | -14.3672 | -53.3901 | 2026-08-05 14:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 91.3 |
| f8656114-674f-3dcb-a69d-b14edb181410 | -12.4598 | -50.3794 | 2026-08-05 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 93.7 |
| facfe689-44e0-3226-b4ff-8f873b7204ae | -14.3865 | -53.3877 | 2026-08-05 14:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 899f9da3-f823-3dc3-9992-4b648f90ae3a | -7.2187 | -43.3499 | 2026-08-05 14:40:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 93.3 |
| 7c97d61b-445b-3b8d-9707-825d3596f762 | -10.9192 | -50.4283 | 2026-08-05 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 159.7 |
| 7d3f7f47-f1cd-3503-b508-0c9b012cd5e7 | -12.5947 | -46.9301 | 2026-08-05 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 144.5 |
| 21ce783a-3c4a-336c-b8af-93262d230da5 | -8.3494 | -46.394 | 2026-08-05 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 94b9e8ad-d892-3f88-8ee7-ecdd567aa7b5 | -12.4386 | -50.5109 | 2026-08-05 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 167.1 |
| dd7fa681-8dc4-35fe-a7e6-1b64fd321503 | -8.3494 | -46.394 | 2026-08-05 14:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 9a9a645a-b3f3-3d4e-8329-8a16059f928d | -14.1966 | -54.4517 | 2026-08-05 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 71.1 |
| a400ba0f-cce9-3aba-a2ca-fc329ad5bd82 | -13.2604 | -54.2662 | 2026-08-05 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 79a06f51-2a83-3321-9b40-2a329f230390 | -7.2187 | -43.3499 | 2026-08-05 14:50:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 82.9 |
| acca7feb-d2c5-3290-b1cc-03265a934bb8 | -7.6288 | -45.3145 | 2026-08-05 14:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 74.4 |
| a0f582f7-356f-3064-82d8-8bd9be866b0f | -14.2687 | -45.2636 | 2026-08-05 14:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 8bd24259-2eba-30f5-a8cf-55ee8ed768c2 | -12.5942 | -46.9527 | 2026-08-05 14:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 2a5ebaa0-ee13-349c-b480-2e6eaebc564a | -11.2206 | -54.9161 | 2026-08-05 14:50:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 116.1 |
| 45b783c5-4335-38fc-ae58-0c8b9b133ecd | -6.8904 | -42.4152 | 2026-08-05 14:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 86.8 |
| bd53a17e-c91d-319e-8b6f-6c1b98f11e1e | -14.3865 | -53.3877 | 2026-08-05 14:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 2b2fec27-21f7-34d6-924b-3f652e21bcf6 | -6.5514 | -55.1569 | 2026-08-05 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| cd0ca731-dc93-308f-ad7f-d32710c1233a | -7.4913 | -45.8468 | 2026-08-05 14:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 0cef1847-aa89-321e-817d-21861dc60d7b | -11.3107 | -44.8105 | 2026-08-05 14:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 60.9 |
| fbef1ff5-5341-3e4e-95f2-a6f91df7ada2 | -14.1969 | -54.4309 | 2026-08-05 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 77.4 |
| c8e077b9-0b33-39b5-8a84-1d7f999d322e | -7.2293 | -45.7801 | 2026-08-05 14:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 92.3 |
| b442d5ba-643f-358d-be9b-39f6be5982d9 | -14.1776 | -54.4331 | 2026-08-05 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 101.4 |
| a42a23ac-3249-3fe9-bf73-cdfb0c838a71 | -10.9192 | -50.4283 | 2026-08-05 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 141.1 |
| 6ca2bd79-805d-3a97-9208-9abe62084dc0 | -14.1972 | -54.4102 | 2026-08-05 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 4c566044-9cd4-3801-9ffd-f9c3885fd650 | -14.1966 | -54.4517 | 2026-08-05 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 318.7 |
| ee82ae80-0f87-3963-bab4-1bdab86e915c | -10.8121 | -65.091 | 2026-08-05 15:00:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 71d75d6c-86ff-365c-8f03-662007b042ff | -11.2206 | -54.9161 | 2026-08-05 15:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| a740e4b6-00b8-33c2-9c73-b2cf7d57c9f8 | -14.3865 | -53.3877 | 2026-08-05 15:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 1e7d8a82-9567-392f-8a10-1cc4bc22c12a | -7.2187 | -43.3499 | 2026-08-05 15:00:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 87.5 |
| 80251c6f-c94c-3b1e-9d9f-00d42cf328e8 | -14.1969 | -54.4309 | 2026-08-05 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 191.9 |
| f2699f04-240e-36f7-9e94-5a62ec1e8414 | -6.5514 | -55.1569 | 2026-08-05 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 96.6 |
| caad5807-69b9-345e-8475-92b5e28bc41a | -7.4913 | -45.8468 | 2026-08-05 15:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 6c4a8c36-d967-3a5a-91b0-52c918dfb9b9 | -12.4386 | -50.5109 | 2026-08-05 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 556c835e-1429-3da3-8e0d-a1511450335e | -7.2296 | -45.7575 | 2026-08-05 15:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 0880c67b-16d5-3ed6-aab2-bf78e81da6ff | -14.1776 | -54.4331 | 2026-08-05 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 134.3 |
| b7d02702-7132-3856-8d4f-d1b3e0599c6d | -14.3579 | -47.5144 | 2026-08-05 15:00:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 205.4 |
| 019726d0-8889-37af-bc29-ebbb26ddf7ba | -12.5947 | -46.9301 | 2026-08-05 15:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 226.8 |
| a38fe20a-5cc9-3209-a1aa-735868197d0f | -12.6139 | -46.9273 | 2026-08-05 15:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| ae4860a0-5887-3aef-a343-3d3d6dfea325 | -8.3494 | -46.394 | 2026-08-05 15:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| d5b95c95-bca2-3428-9046-8cdc5679f04d | -10.4678 | -50.241 | 2026-08-05 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 45c0fdaf-f019-3bcf-8eea-693bbeb74027 | -6.8904 | -42.4152 | 2026-08-05 15:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 91.6 |
| 2e9e558f-7fbd-34ce-a1af-f988b8dbe5ae | -14.5046 | -52.0847 | 2026-08-05 15:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 31752329-da0c-36a7-b13a-5d6b78aa2672 | -7.2293 | -45.7801 | 2026-08-05 15:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 7ab9d262-99d1-316b-81a4-ee1affd8fe09 | -11.3111 | -44.7873 | 2026-08-05 15:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 448efa99-a7e9-3efc-ac4c-8b020371f310 | -6.5329 | -55.1578 | 2026-08-05 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 6e06234c-9310-369b-9321-239fffa45592 | -10.9192 | -50.4283 | 2026-08-05 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 159.9 |
| e35e3758-1489-35f7-88d7-a3621fa456dc | -7.2293 | -45.7801 | 2026-08-05 15:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 88357f77-cd2d-3302-ac9c-b1a198b88c74 | -14.3516 | -53.1612 | 2026-08-05 15:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 10fb75c8-99ba-3454-af28-3754c912c69a | -10.9192 | -50.4283 | 2026-08-05 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 165.3 |
| b8bffb9b-ac3a-312b-90c2-4871909c03de | -12.4789 | -50.377 | 2026-08-05 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 104.6 |
| cde0eb0a-cc05-36bd-8e7b-8df480bbe24f | -14.1776 | -54.4331 | 2026-08-05 15:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 75de14b4-e91d-39bf-8445-e29c71ca6f81 | -10.8121 | -65.091 | 2026-08-05 15:10:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 562d8031-c7f4-3059-9f23-6ec1e5c3ad3b | -14.1966 | -54.4517 | 2026-08-05 15:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 63e33448-fec7-39a7-b951-af5f126f8474 | -7.2187 | -43.3499 | 2026-08-05 15:10:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 89.7 |
| 1de16661-ebca-3565-977b-ccd97329a6ad | -6.8904 | -42.4152 | 2026-08-05 15:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 105.7 |
| 73a30e41-c795-34cf-91eb-244ca4476fea | -12.4386 | -50.5109 | 2026-08-05 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 85208928-bc6e-3ea9-b21b-26d909c5a3bb | -6.5512 | -55.1769 | 2026-08-05 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| b4108302-5dfd-3af4-aced-f7ac785fef8d | -6.5329 | -55.1578 | 2026-08-05 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 51a2bc2f-cbb2-3007-a937-8480b91b8d3a | -14.1969 | -54.4309 | 2026-08-05 15:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 124.0 |
| ee4f85c8-6d18-35cf-a4fc-b19587bd3482 | -6.5514 | -55.1569 | 2026-08-05 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 91.4 |


[Clique aqui para ver as próximas entradas](README33.md)
