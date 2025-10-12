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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b7191b47-9e26-326a-8475-b79130605c7d | -14.40317 | -47.97023 | 2025-10-12 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| b5f0e924-2e78-3905-b709-de539e2fa5bb | -15.01333 | -45.57341 | 2025-10-12 04:44:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 256e0c2f-cdf1-33c7-b700-f41ce9330d37 | -14.95218 | -45.57678 | 2025-10-12 04:44:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 036696c6-7ab9-354a-9ebe-19577ac8fb35 | -9.08215 | -48.02618 | 2025-10-12 04:44:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 85e352f7-3643-3a2b-ae38-3448f1341aa8 | -9.40238 | -45.74502 | 2025-10-12 04:44:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 25f32a4b-bb1d-3648-9074-d23acc76ceae | -9.83593 | -44.96126 | 2025-10-12 04:44:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 86e4ef9f-1277-348b-aa73-a0d055f839b1 | -11.49605 | -43.48863 | 2025-10-12 04:44:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c8959b2b-040f-3bfe-b7ff-54defa284419 | -14.70903 | -56.32613 | 2025-10-12 04:44:00 | NPP-375D | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 62aac92c-e797-337f-afc2-3df142b466a3 | -11.85544 | -56.86575 | 2025-10-12 04:44:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d8a5cc1d-750a-39bc-b395-06fcac3ca73c | -15.15082 | -56.8119 | 2025-10-12 04:44:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0e48d376-8530-3ac4-be30-dcb17ef85c9e | -10.14681 | -44.55439 | 2025-10-12 04:44:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0628fdee-5147-3e09-8254-ced0ed07d6f7 | -15.29471 | -46.1367 | 2025-10-12 04:44:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3f726862-da24-3efb-baf2-79b510933c05 | -15.23107 | -56.87479 | 2025-10-12 04:44:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dea5028c-8e4b-30f0-b7d7-2fffaaab7bd4 | -9.41014 | -45.74641 | 2025-10-12 04:44:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b92a61dc-5d96-3e7c-a5b1-fd0e6f5a7f42 | -9.07811 | -48.02947 | 2025-10-12 04:44:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| acda2dd5-2e16-3746-af18-b0a3c8895d48 | -13.98497 | -54.89479 | 2025-10-12 04:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 64a4e24b-b435-3128-9652-4df62eae67d9 | -9.07999 | -48.02654 | 2025-10-12 04:44:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4e21532c-5aca-3468-8eeb-48f736cb842a | -11.24933 | -61.17119 | 2025-10-12 04:44:00 | NPP-375D | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a1727643-c738-3c6c-9ef4-b13de113ef35 | -13.28653 | -47.98479 | 2025-10-12 04:44:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 008b5305-320d-3ce7-a712-6930bfe0455f | -13.46354 | -51.27407 | 2025-10-12 04:44:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 0919fc7a-c22b-363a-929e-41414f2bd8b3 | -13.46692 | -60.97388 | 2025-10-12 04:44:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a4d2da9e-1b08-37d0-b276-3b05deb5858d | -14.54034 | -45.58201 | 2025-10-12 04:44:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1498cf82-c429-3789-bfce-ef5a10ceade2 | -13.49499 | -43.03678 | 2025-10-12 04:44:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8331f1e7-2257-3e2f-b52f-5bafc6192f0a | -15.66251 | -43.90376 | 2025-10-12 04:44:00 | NPP-375D | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 86a8abd1-a16e-3ae9-b39c-f3e6a1064097 | -14.70524 | -47.43539 | 2025-10-12 04:44:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1164457a-b8c9-364c-9dad-d59852773aca | -13.45688 | -51.27297 | 2025-10-12 04:44:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 52b9907a-e05f-36cf-98e0-04480e751dc0 | -14.94204 | -45.58812 | 2025-10-12 04:44:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| ec999eaf-a6ba-313a-bffa-0d60b1342c34 | -14.55409 | -47.30999 | 2025-10-12 04:44:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ff0e4fe3-51e7-3000-9f73-d48d964f7895 | -14.9859 | -44.94366 | 2025-10-12 04:44:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 382e2c5f-76e1-34a7-b4b7-daada56fa053 | -14.94312 | -45.57978 | 2025-10-12 04:44:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 11498fe4-1748-3659-9a45-b8facecba63d | -13.29454 | -47.98425 | 2025-10-12 04:44:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 91f48ba0-2b90-3c26-872d-4442f0ead96d | -9.40625 | -45.74575 | 2025-10-12 04:44:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 794d5910-80b8-3557-ba81-24b64936f05a | -11.91526 | -44.18327 | 2025-10-12 04:44:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e01ff0da-7c74-3c4b-9350-17055506c695 | -9.41036 | -45.74833 | 2025-10-12 04:44:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cc49bfc8-cfdb-3fef-88dc-7710bb8b8ee8 | -9.41425 | -45.74898 | 2025-10-12 04:44:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1d8f4df4-b8d4-30d7-915e-90ec0535aab9 | -18.00702 | -52.3959 | 2025-10-12 04:46:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0323a240-1895-3731-bfe3-a69f21a54591 | -18.64431 | -43.14673 | 2025-10-12 04:46:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1c928c42-6d38-303b-a716-9cd5e989732c | -17.86893 | -45.02668 | 2025-10-12 04:46:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 7984700c-7b41-3fa8-a53b-c444d7102b09 | -17.81796 | -57.62904 | 2025-10-12 04:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 8b45c276-bf94-3bd0-9e13-4d6a01a8ddb9 | -17.82318 | -57.66927 | 2025-10-12 04:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 9bb94c6b-b7f3-3cf5-ad61-84a0d30ab124 | -17.40863 | -46.86756 | 2025-10-12 04:46:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c9a8422a-7bb9-3b0f-9338-45ed2367d265 | -19.82675 | -42.13544 | 2025-10-12 04:46:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 9d592622-1837-3e50-91e4-d45e59bba048 | -17.25298 | -52.2674 | 2025-10-12 04:46:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5923a076-33ce-3a7a-b379-396919bdc0b1 | -17.89796 | -57.66878 | 2025-10-12 04:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 58e29164-4af5-3c23-ad1c-3323e628d8f3 | -22.38679 | -50.00685 | 2025-10-12 04:46:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 67fb49d1-fb61-3a3c-870f-75fe58d25083 | -19.83165 | -42.14417 | 2025-10-12 04:46:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 473d5eee-52b6-3614-a61e-ecf83c56f64b | -15.45914 | -55.94572 | 2025-10-12 04:46:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bac7fc6d-0750-3e6e-9f20-9da87dd2e016 | -17.87351 | -45.02738 | 2025-10-12 04:46:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 14.7 |
| d463c5a9-4682-3c99-8b40-7f66b37a8695 | -17.83206 | -57.66727 | 2025-10-12 04:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 709510d9-47a0-3706-8cdd-f73f1cde83cc | -15.28414 | -57.08178 | 2025-10-12 04:46:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 221d8a2b-d8f0-3db0-9091-63d2bcd6fb6b | -17.54932 | -46.52179 | 2025-10-12 04:46:00 | NPP-375D | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 738d4161-d09b-3a17-a5b3-70a90e679ea7 | -22.33125 | -49.86766 | 2025-10-12 04:46:00 | NPP-375D | VERA CRUZ | SÃO PAULO | Brasil | 3556602 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 2122e178-01e3-3036-bf17-475dbf79bc14 | -18.95654 | -45.71966 | 2025-10-12 04:46:00 | NPP-375D | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 67c189eb-93c0-3b40-9a2b-e52563c8111b | -17.19497 | -46.96041 | 2025-10-12 04:46:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cbab18f6-725a-318e-a57c-15f15c629460 | -17.89651 | -57.67645 | 2025-10-12 04:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| c653fa5e-45ab-3d3a-940d-785dbbe216a1 | -19.03279 | -57.54022 | 2025-10-12 04:46:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 171ebd3f-23c1-30b1-a2f1-c43fe2fc9ceb | -17.87307 | -45.02499 | 2025-10-12 04:46:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 37acfbbe-4c92-31e9-b80e-cc5a70500e71 | -20.56463 | -54.63166 | 2025-10-12 04:46:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| eb157fc6-62d9-3cdb-b7c3-d39c56689431 | -16.11844 | -53.97406 | 2025-10-12 04:46:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7f24d22f-4b95-3191-b57a-e4ff173a2c32 | -19.77835 | -42.39491 | 2025-10-12 04:46:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 14f314de-9ef5-3d9f-9b5a-d476f0d16dfe | -15.71532 | -56.15477 | 2025-10-12 04:46:00 | NPP-375D | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3e92761d-e9e5-3d65-9156-347d7493c763 | -18.0076 | -52.39227 | 2025-10-12 04:46:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d2a0c83c-4bf5-3e94-8ca2-336d16e7926c | -18.00369 | -52.39533 | 2025-10-12 04:46:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dfd114d9-4489-3f54-89e3-3457eb3bd5a5 | -17.87249 | -45.02994 | 2025-10-12 04:46:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 4956fed6-7d1b-3f2b-975b-62b2aa5c07b6 | -17.19164 | -46.95451 | 2025-10-12 04:46:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cde55b94-a7c6-325c-aad2-c63851f2a1b2 | -17.40553 | -46.85983 | 2025-10-12 04:46:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ef0232fb-c2e5-34b9-b925-d3c0bbcbae8f | -17.18264 | -46.95192 | 2025-10-12 04:46:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 074a087c-f5ff-3994-8474-5ca6b62aefde | -17.55449 | -46.51463 | 2025-10-12 04:46:00 | NPP-375D | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ffe02708-429a-3a51-a74a-3a665aca8dd3 | -17.81933 | -57.62172 | 2025-10-12 04:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 69ffca71-0368-3639-98c4-d7e7817dfe9b | -17.86906 | -45.01934 | 2025-10-12 04:46:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 66dbaddf-44be-330c-822e-cb7e058235e4 | -17.19097 | -46.95969 | 2025-10-12 04:46:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 336f23f8-8564-37d8-86e9-fdf6cc7d1060 | -19.76609 | -42.4263 | 2025-10-12 04:46:00 | NPP-375D | PINGO D'ÁGUA | MINAS GERAIS | Brasil | 3150539 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| a2462041-ffaa-30a8-a785-440a29ab70d4 | -17.25631 | -52.26797 | 2025-10-12 04:46:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0166bf2c-9a7e-3d10-bec7-8201108785bf | -15.69598 | -56.151 | 2025-10-12 04:46:00 | NPP-375D | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a64b8211-bbe1-3477-912f-9a348bbec227 | -17.83685 | -57.66435 | 2025-10-12 04:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 8f31e21e-c6f0-35a7-af45-f8dc645e532c | -17.86955 | -45.02171 | 2025-10-12 04:46:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4db113ed-b542-33d4-9be8-71d5f88854d8 | -19.76418 | -42.42386 | 2025-10-12 04:46:00 | NPP-375D | PINGO D'ÁGUA | MINAS GERAIS | Brasil | 3150539 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 214f35e4-ada6-3425-a77c-d8d0a085d0ee | -17.95344 | -57.6214 | 2025-10-12 04:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 15bd8923-531a-3ca8-bdfd-50f0576e32a9 | -17.84165 | -57.66138 | 2025-10-12 04:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| a8256581-6e8b-331d-94ea-bb71c528bec9 | -17.82799 | -57.66628 | 2025-10-12 04:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| a9a06edb-d629-3b92-aec8-82d7a6d1020b | -17.94388 | -57.62732 | 2025-10-12 04:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 6ccc41d1-8261-30bb-a0c2-dd99e6e8c76f | -17.18003 | -46.94085 | 2025-10-12 04:46:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2c3eb5eb-e4fc-3c22-9d13-d0b28415707c | -15.85812 | -56.75191 | 2025-10-12 04:46:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b03ef6bc-c649-366b-a119-375d5b3c6aed | -16.75697 | -51.61956 | 2025-10-12 04:46:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cfbca6cf-d9c3-3f6f-b16a-7bead9b05514 | -15.46298 | -55.94646 | 2025-10-12 04:46:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 70253cfd-2897-31a3-9f49-1949e31716d9 | -17.82396 | -57.66511 | 2025-10-12 04:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| eb39a11b-c87d-3848-8305-8d6de7845264 | -17.94866 | -57.62434 | 2025-10-12 04:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| c6240174-1713-3fe9-8a5f-16955ce116d8 | -19.03974 | -57.54728 | 2025-10-12 04:46:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 6e57bd82-4c8a-38e7-89d2-05654bac4aef | -18.45531 | -47.15577 | 2025-10-12 04:46:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 31e45ffe-645b-3ac9-a046-a565e76659a6 | -22.29123 | -49.88871 | 2025-10-12 04:46:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b681b58c-5a59-3601-bf70-1b51e9f52bc7 | -17.17933 | -46.94613 | 2025-10-12 04:46:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7e59b4d3-bb59-3e71-94a9-6ac10137d53c | -17.81864 | -57.62542 | 2025-10-12 04:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 6c3e9300-4366-3533-9780-1ffe3c1e4436 | -15.46755 | -55.94915 | 2025-10-12 04:46:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c059da8f-1855-325e-9ad5-43f0be74df4a | -17.19394 | -46.95916 | 2025-10-12 04:46:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 46d6bec5-4e0e-34a1-abf3-635bde65245a | -17.95821 | -57.61849 | 2025-10-12 04:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 42d7a4d6-8a27-3423-bdfe-65c47368aec1 | -19.01983 | -57.54316 | 2025-10-12 04:46:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 540f297e-c35f-3ccd-a0f3-8906f47fff3c | -17.555 | -46.51076 | 2025-10-12 04:46:00 | NPP-375D | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dd50c289-6f2b-3415-9e4c-0380558cde7f | -17.25573 | -52.27158 | 2025-10-12 04:46:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc7933e9-cb40-3cfe-aede-58dbf9283ec8 | -17.82724 | -57.6703 | 2025-10-12 04:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| f748ce24-893b-3fb1-bbca-05d22fbf6a26 | -17.2524 | -52.27101 | 2025-10-12 04:46:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README36.md)
