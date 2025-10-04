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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 12e54578-d344-3dd0-890a-4864a42c176e | -19.57457 | -48.02306 | 2025-10-04 03:28:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| c5ff8f2c-7373-3b20-aa3c-0a06702d2596 | -21.12791 | -42.88098 | 2025-10-04 03:28:00 | NOAA-21 | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a7592ea7-2d3d-3d1e-a80d-da4a0708a3b0 | -20.06833 | -43.75579 | 2025-10-04 03:28:00 | NOAA-21 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c0698ced-f7e2-3a14-b2e0-f30ef7d62a59 | -20.78364 | -43.22218 | 2025-10-04 03:28:00 | NOAA-21 | PRESIDENTE BERNARDES | MINAS GERAIS | Brasil | 3153103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| b305af40-fb27-3cd4-b8af-45662fe4adb6 | -20.22437 | -44.1773 | 2025-10-04 03:28:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| a3ab8f14-5800-38e6-8b79-bbfb9dc12282 | -19.89675 | -43.65368 | 2025-10-04 03:28:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7c603715-30e1-321f-a263-0e8effbfaefb | -22.0776 | -43.09509 | 2025-10-04 03:28:00 | NOAA-21 | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9641f9b6-2c75-336d-b6cf-e88692ce3928 | -19.97006 | -43.70539 | 2025-10-04 03:28:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 08a6ee8b-6eb5-35c8-b569-b6f5402269c4 | -22.12503 | -42.91856 | 2025-10-04 03:28:00 | NOAA-21 | SÃO JOSÉ DO VALE DO RIO PRETO | RIO DE JANEIRO | Brasil | 3305158 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| a14e8dbc-3447-319e-9f2d-96239cd0400a | -21.19596 | -45.14146 | 2025-10-04 03:28:00 | NOAA-21 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 4eefdc09-62c8-3069-9a6d-b19c68afe872 | -19.68834 | -43.94733 | 2025-10-04 03:28:00 | NOAA-21 | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 88f30d4f-0385-316c-9400-7e1676c2579f | -19.97086 | -43.70164 | 2025-10-04 03:28:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 22ba5296-5433-3866-9ddd-60bd73a9376b | -20.47746 | -44.82663 | 2025-10-04 03:28:00 | NOAA-21 | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| e997de82-a9fe-3854-ac63-3b1516733eab | -19.77648 | -43.56367 | 2025-10-04 03:28:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b0b8112e-8432-3a72-88fb-ac188c7b8d06 | -19.57638 | -48.01551 | 2025-10-04 03:28:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| da1776b7-2bcd-3524-bef1-0c9035a6b16c | -21.33952 | -44.99389 | 2025-10-04 03:28:00 | NOAA-21 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 246ea7b9-3557-38a8-8f85-d16804811475 | -19.96848 | -43.71275 | 2025-10-04 03:28:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| aace93f5-baf0-31f7-a322-b8765bae8d5c | -21.59971 | -45.28521 | 2025-10-04 03:28:00 | NOAA-21 | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e01f3c12-4e48-32aa-85e0-ad0ad6caeb0c | -21.19496 | -45.14576 | 2025-10-04 03:28:00 | NOAA-21 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 2c5b2b11-6a5b-3ce5-8215-ce0690053b5e | -19.59422 | -44.62915 | 2025-10-04 03:28:00 | NOAA-21 | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 43711a23-98f2-3e61-b766-4c44d8e15b0a | -21.56006 | -45.27393 | 2025-10-04 03:28:00 | NOAA-21 | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f379ecfd-b9c5-3276-9bdb-b6b0b471d306 | -19.97614 | -43.7033 | 2025-10-04 03:28:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| b821e6a7-aaea-3e20-ba60-e22c7ae85e6d | -19.71157 | -44.12797 | 2025-10-04 03:28:00 | NOAA-21 | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c553fd86-3e75-3234-86fe-8a575a81abeb | -9.3464 | -54.5201 | 2025-10-04 03:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| f6e5066a-43ee-3dbf-8ec8-f70581295bde | -14.2316 | -46.1024 | 2025-10-04 03:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 40e07a4b-8cf3-3471-b382-5bc567a12524 | -5.1965 | -45.0768 | 2025-10-04 03:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 256.5 |
| 69d9f85d-1584-3377-bdb1-08a1b028d3b6 | -11.9339 | -46.3699 | 2025-10-04 03:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| bdaa910c-7861-3428-bd03-40bfd48b6c56 | -5.1967 | -45.0541 | 2025-10-04 03:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 202ade94-8186-3746-99f8-cce0a805a398 | -7.7301 | -46.3185 | 2025-10-04 03:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 2d6e0d60-6035-3503-a474-06206f889abc | -10.3343 | -50.3402 | 2025-10-04 03:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 178.5 |
| f6bde0b8-11cd-379f-bd37-6ca3672461c6 | -13.1164 | -47.8178 | 2025-10-04 03:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| d591fd5d-e866-35fa-be6b-dc842f122dc9 | -10.3346 | -50.3188 | 2025-10-04 03:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 106.6 |
| bdac365f-5647-367e-99e9-b3965a0de979 | -12.0314 | -45.1901 | 2025-10-04 03:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 276.6 |
| 7d069efc-398e-339e-921c-d6a6ee1501f0 | -4.4443 | -43.263 | 2025-10-04 03:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 6d8dd896-6997-3dcb-96ca-440bd68080ee | -12.0502 | -45.2103 | 2025-10-04 03:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 05b32807-c7ac-3218-a3a6-fcfa472ce504 | -4.954 | -45.0694 | 2025-10-04 03:30:00 | GOES-19 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 698a45f3-2ee0-30f4-82a8-524df23ad0fd | -14.6521 | -48.3188 | 2025-10-04 03:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 71.7 |
| e5069212-bbde-312c-adfa-bf6922ef410f | -6.0806 | -42.5118 | 2025-10-04 03:30:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 136.3 |
| 69daf9d7-ce67-358f-a343-1773830a9e48 | -5.1779 | -45.078 | 2025-10-04 03:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 06fa0273-d9db-33c9-bd80-7691521b2d16 | -4.4258 | -43.2408 | 2025-10-04 03:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 7373f917-e401-33cd-b77d-9235ec9664ab | -14.672 | -48.2933 | 2025-10-04 03:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 786e8488-6a2f-39ee-805b-cd222e03d182 | -11.9147 | -46.3726 | 2025-10-04 03:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 1a786368-df35-3811-a82b-146c4097a6c9 | -2.9013 | -50.7351 | 2025-10-04 03:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 521078d9-cb3e-336a-94cd-3e00076124a9 | -12.0507 | -45.1872 | 2025-10-04 03:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 101.1 |
| eb6d20f0-5bed-323e-b2a8-38169e880b7f | -14.2321 | -46.0794 | 2025-10-04 03:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 90.7 |
| fc1a41c8-d1f0-347a-a8bb-1f0b1abc015e | -14.251 | -46.0991 | 2025-10-04 03:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 134.2 |
| 7bf7af8c-b23f-3946-8a08-88504cba1007 | -9.3276 | -54.5215 | 2025-10-04 03:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 2c04e833-cbfc-3912-8124-f19b002fc8a5 | -17.7044 | -47.0821 | 2025-10-04 03:30:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 54.1 |
| d5dee12f-86e8-3c1e-9ee8-86d3be700f92 | -15.2205 | -56.8414 | 2025-10-04 03:30:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 8ba612f4-1381-3431-aa99-1ad6d1e87919 | -14.2515 | -46.076 | 2025-10-04 03:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 53cd2742-9b7c-3cbf-ab23-a3060d53a34f | -5.2152 | -45.0756 | 2025-10-04 03:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 8efca519-8565-3da9-ab6f-e824e3f8103b | -13.9387 | -48.1629 | 2025-10-04 03:30:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 6ac37ec8-bf76-31e0-bec9-e5b2ff82a0d8 | -14.6526 | -48.2964 | 2025-10-04 03:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 7ca8d967-dc93-36cf-bc11-95b75641e38a | -8.6322 | -54.9949 | 2025-10-04 03:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 38.2 |
| eb08553e-9f9c-3d86-acf9-c56c29f9e925 | -10.3154 | -50.3421 | 2025-10-04 03:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 5921b724-31f9-3b24-9527-d4c8e4e6c43f | -13.1357 | -47.8149 | 2025-10-04 03:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| bc860fda-ea94-3f49-82fa-f171c1586e3d | -4.4445 | -43.2397 | 2025-10-04 03:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 109.5 |
| a7f14b10-ad18-3c12-8b5f-94d007c59415 | -13.116 | -47.8401 | 2025-10-04 03:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 8f21b13c-ce67-3a12-9453-0f47df628aa5 | -12.031 | -45.2132 | 2025-10-04 03:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 272.4 |
| 1135f1b4-b6d7-39be-95f9-78c609efe58f | -15.6019 | -52.4888 | 2025-10-04 03:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 99.3 |
| b7369262-3b41-3fed-a5cc-509f2c43296e | -6.0618 | -42.5133 | 2025-10-04 03:30:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 134.3 |
| e82b4604-f607-3a0d-9a5b-051486dc2a1b | -6.0806 | -42.5118 | 2025-10-04 03:40:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 166.4 |
| 40598dd5-df23-3fb7-a918-8ddd090b0e04 | -10.3154 | -50.3421 | 2025-10-04 03:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 7976a126-7c93-36aa-a248-e72b33222fc1 | -8.6322 | -54.9949 | 2025-10-04 03:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 66be78cb-02ae-3771-8313-7a61bfd536e4 | -11.9147 | -46.3726 | 2025-10-04 03:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 194.6 |
| dacd173a-000b-3e13-98d3-b0800663e613 | -14.6725 | -48.2709 | 2025-10-04 03:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 76.7 |
| ce99c13a-d1b5-3815-b797-6503658b31af | -6.0618 | -42.5133 | 2025-10-04 03:40:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 134.8 |
| a58bf61e-aa7b-38f3-8baa-fe26d12366a6 | -4.632 | -43.1583 | 2025-10-04 03:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 9442926b-6b8d-3dd1-8a13-9b734eb2d546 | -4.6133 | -43.1594 | 2025-10-04 03:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 111.0 |
| f55bc41c-75ad-33ec-8155-9b88f1ae50b6 | -14.251 | -46.0991 | 2025-10-04 03:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 103.6 |
| d08d8347-c8dc-319b-a728-0f364eb59b79 | -14.672 | -48.2933 | 2025-10-04 03:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 207.3 |
| 9c95ddc0-db59-33f1-b72f-bdf0f04c7919 | -10.3346 | -50.3188 | 2025-10-04 03:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 79d20eae-4f34-3ebb-8158-da5a968cad7f | -9.3276 | -54.5215 | 2025-10-04 03:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| d56d0e74-7f14-3055-b164-c2f8c0c7ffc9 | -12.0314 | -45.1901 | 2025-10-04 03:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 311.3 |
| 441a1d1f-b160-3a0e-86b7-74fed4cff796 | -14.2321 | -46.0794 | 2025-10-04 03:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 55664d4a-3024-34f0-aa4b-1373a878219d | -10.3343 | -50.3402 | 2025-10-04 03:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 174.8 |
| abf30187-7a59-3bf4-a4b9-572f5ff92c51 | -5.1967 | -45.0541 | 2025-10-04 03:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 123.8 |
| ecebde29-efdd-3b7d-b391-a79c14e355bb | -13.1337 | -47.9267 | 2025-10-04 03:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| cddd278a-a837-3529-ab41-148717cd317c | -4.954 | -45.0694 | 2025-10-04 03:40:00 | GOES-19 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 1db6ef99-3d0e-3e64-bf3e-f782382612dc | -17.7044 | -47.0821 | 2025-10-04 03:40:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 65.5 |
| ed10dbc5-4f4c-3da9-a88c-f46d4ad66552 | -6.8774 | -47.2334 | 2025-10-04 03:40:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 9c156d88-0b1b-30ba-9a8e-bb9f4f7d7637 | -11.9143 | -46.3953 | 2025-10-04 03:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 186.5 |
| 141a229d-4427-3c24-97a7-73350fab6232 | -13.1144 | -47.9295 | 2025-10-04 03:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| f05dfce2-a694-3d9b-8c7a-10146b689479 | -12.031 | -45.2132 | 2025-10-04 03:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 409.4 |
| 95456e47-3c67-3643-a5c4-c4698d4ffdf3 | -11.9339 | -46.3699 | 2025-10-04 03:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 169.9 |
| fc241fb3-b937-3e75-8fc0-35a1ffae8c92 | -12.0507 | -45.1872 | 2025-10-04 03:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 2aacb24d-6d73-3824-986b-5c357f86f933 | -14.2515 | -46.076 | 2025-10-04 03:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 8a5fc997-96c1-33c1-bc33-7e4a1bc92bf2 | -7.7303 | -46.2961 | 2025-10-04 03:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 25610c9b-6f1f-36fd-867f-493c0c8eb745 | -13.1333 | -47.949 | 2025-10-04 03:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 80790b2c-92b2-3a4e-9350-9fad39f229e9 | -5.1965 | -45.0768 | 2025-10-04 03:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 201.8 |
| c5994631-2ac0-30e8-9c78-1c07e704c948 | -11.9335 | -46.3926 | 2025-10-04 03:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 25aff7be-f8b0-3f13-8296-dff15324305e | -7.7301 | -46.3185 | 2025-10-04 03:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 05a0f8bc-a0c2-3be1-a598-cafd588f8d6b | -14.2316 | -46.1024 | 2025-10-04 03:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 63.8 |
| b75378ab-b4d9-3401-ad60-16825424a14b | -14.6526 | -48.2964 | 2025-10-04 03:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 133.5 |
| 66b33a50-2d90-3d7a-a2a2-b9adc9750358 | -12.0502 | -45.2103 | 2025-10-04 03:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 19c4c2b9-201c-3a92-bf90-242cb100d9d7 | -4.14564 | -42.17272 | 2025-10-04 03:49:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e3f0d98c-a134-36ae-b80a-1671106e7815 | -2.68898 | -48.3961 | 2025-10-04 03:49:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ab90d9e3-2bb9-3c83-a93f-4f506656ddc5 | -3.34001 | -44.09692 | 2025-10-04 03:49:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 193a0244-8b23-36b0-b782-bbce219ca494 | -3.84302 | -41.56682 | 2025-10-04 03:49:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 484aa7d4-86da-3da4-9578-a59676552792 | -3.83749 | -44.55141 | 2025-10-04 03:49:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README18.md)
