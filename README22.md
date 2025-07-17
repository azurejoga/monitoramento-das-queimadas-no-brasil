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
| 06fede6f-2a40-3c9b-81d3-0a55f3b8b0c4 | -12.59113 | -44.79533 | 2025-07-17 04:46:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a2ccbf4e-3e4a-3798-ac2f-2cce4d9a66ac | -11.91934 | -49.38293 | 2025-07-17 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aeca0bd7-edb7-3043-b131-dc295d86e549 | -11.84919 | -46.75273 | 2025-07-17 04:46:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c3d2ccb5-6036-3481-9dca-dcde2ac59f93 | -7.34585 | -44.20164 | 2025-07-17 04:46:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5ea77505-739f-38f6-aa1a-93fdb2241ae9 | -9.38124 | -48.55211 | 2025-07-17 04:46:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 15b65d61-4417-3f1e-b94e-cf8cede4abe9 | -7.09379 | -49.16903 | 2025-07-17 04:46:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bb25f268-cc82-3743-8b6f-abf549cce0f8 | -8.87607 | -50.15064 | 2025-07-17 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5658220-762f-31f0-ba33-76992c7254b5 | -11.94942 | -48.42035 | 2025-07-17 04:46:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 85530a15-e0b4-365b-8443-40b147b370e0 | -6.43672 | -45.32433 | 2025-07-17 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1797cd0d-c8ab-34a3-bc6c-84ed4c2252d5 | -11.50543 | -48.95558 | 2025-07-17 04:46:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e94132de-28ba-33c9-aee8-20fbc54550f8 | -6.13907 | -47.31704 | 2025-07-17 04:46:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 3bf516f6-bb5b-3d50-8fc8-081cf33cca57 | -10.10554 | -40.92075 | 2025-07-17 04:46:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0bab4322-8e71-3d4d-9494-b7a95befaa51 | -9.46324 | -63.15145 | 2025-07-17 04:46:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6dcaeb10-f73e-3e22-a9a1-34f8809cffb1 | -10.65779 | -49.36296 | 2025-07-17 04:46:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6caa5a1d-bff3-3943-a3b8-31d14332940d | -8.11318 | -43.1473 | 2025-07-17 04:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 0456c543-8484-33fe-9d31-617736fa4ef5 | -8.10263 | -43.1488 | 2025-07-17 04:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| c78186df-160f-3a3a-83b4-0675b3bd8e22 | -6.33967 | -43.7496 | 2025-07-17 04:46:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 90b40641-3c77-31e6-be84-1518d1d6999a | -9.88627 | -47.81404 | 2025-07-17 04:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8e4daf37-e4ed-33d0-b893-b74efbcb3546 | -6.85514 | -44.77291 | 2025-07-17 04:46:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3c45014c-848b-31bd-9cef-c7756fe6644b | -10.96657 | -49.25149 | 2025-07-17 04:46:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 55f4dd2f-0e65-38b0-9446-91b65842c57e | -11.07939 | -44.53386 | 2025-07-17 04:46:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 048a5d35-70b7-3204-8f2f-520efb421e09 | -8.38097 | -46.90046 | 2025-07-17 04:46:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3b33205d-dc23-3df3-bec8-2f9de61a003e | -9.06231 | -47.89624 | 2025-07-17 04:46:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d75f206d-c3d5-36f1-99a7-47c12dd8ffaa | -11.07865 | -44.53454 | 2025-07-17 04:46:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 726c43c6-9567-301a-9683-f4b8dbcc8f01 | -8.05935 | -50.10818 | 2025-07-17 04:46:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 94a668f5-5a26-3713-9135-9d4e22289bc5 | -6.44564 | -42.67614 | 2025-07-17 04:46:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 54dd4da6-8eb4-3729-a3a1-03e44c22e81f | -5.79171 | -45.09214 | 2025-07-17 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 34d7fa36-2355-39c8-89d9-bcfa73916735 | -7.14706 | -43.18481 | 2025-07-17 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 744a0a1e-cb96-3eac-b10b-3e86d896786f | -7.21221 | -45.3312 | 2025-07-17 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4cfad5b3-a59e-3d83-9316-af7dd63094bf | -6.46784 | -45.34442 | 2025-07-17 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e76feeb9-d3cd-319b-b4d7-a6b5bd995b53 | -6.99959 | -43.74662 | 2025-07-17 04:46:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 4576301e-c859-319f-b542-a31ec87ff5e0 | -6.84914 | -42.74898 | 2025-07-17 04:46:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| aab61294-d5b3-3b0d-b1c3-f8be3d19bc6a | -6.99404 | -43.7512 | 2025-07-17 04:46:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f0073b39-487d-3321-9458-5adcd49d3d2b | -11.46021 | -45.09786 | 2025-07-17 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fdf1facb-d8a9-3e81-aa97-1654de7f5800 | -12.10421 | -48.19628 | 2025-07-17 04:46:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a655e2c-d874-393f-9991-c1452fe32b6e | -7.1872 | -43.11716 | 2025-07-17 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 6ad82248-20f5-3a28-a7ff-870203d27086 | -9.01675 | -59.5398 | 2025-07-17 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b23ca592-38b4-3544-9f19-b2786aa9d254 | -8.75167 | -46.59148 | 2025-07-17 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8c2c00a8-e78e-3dab-8cb1-13295ed7301a | -6.97942 | -42.8099 | 2025-07-17 04:46:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| cb914f8c-8631-3966-b284-6ad5ab3dd403 | -8.75671 | -46.58488 | 2025-07-17 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3f53d036-3cc9-3b8b-81d4-3b2a96acc3f3 | -8.75267 | -46.58425 | 2025-07-17 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 0c3e07a7-dc5a-3c91-9d1b-4ddc41f5ca49 | -8.88711 | -50.15548 | 2025-07-17 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8883a694-0c39-3b0d-929c-35a57108fc48 | -9.92085 | -50.84612 | 2025-07-17 04:46:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 87e5c752-cb0a-3965-b324-9dd8443b5ddf | -6.98122 | -43.73915 | 2025-07-17 04:46:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e4f8a038-c279-3a54-aba4-43cf2870e954 | -8.384 | -46.90226 | 2025-07-17 04:46:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1597dd51-2d7b-30c8-8498-123bb0948189 | -9.16274 | -59.71268 | 2025-07-17 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bbc4f713-b20c-375f-81ad-45181d777a8a | -6.67707 | -43.03479 | 2025-07-17 04:46:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b9ea64c2-0959-3445-a330-d1189ed7ed04 | -6.67668 | -43.03767 | 2025-07-17 04:46:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d6e5c0f5-b547-3e60-8d67-68af64af9e12 | -11.94951 | -48.42215 | 2025-07-17 04:46:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e2fcb25d-4980-35b9-9675-c716236853b8 | -7.59374 | -46.33788 | 2025-07-17 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| da401eea-8b23-3764-8f7e-8426f84bc7de | -5.79793 | -45.10943 | 2025-07-17 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a648677d-2659-389d-b435-d181d9bdd76e | -4.45158 | -48.99669 | 2025-07-17 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f9e8c0fe-a283-3613-8392-6b2522169e1c | -5.66252 | -43.71979 | 2025-07-17 04:46:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| d7574148-b24b-30b4-88d1-ec63f015b43c | -11.80514 | -46.66804 | 2025-07-17 04:46:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a7cc8c62-1fac-371b-82aa-6f979ce52128 | -10.32861 | -49.9086 | 2025-07-17 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9618a3c3-bf92-3d38-bf18-e2110b881e2b | -7.59737 | -46.31326 | 2025-07-17 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0e5a763e-bcb9-3816-a8a0-e98c7a925ed4 | -6.45934 | -45.34306 | 2025-07-17 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e6add8f0-79f0-303e-94be-661eddf6c4eb | -7.89185 | -55.42179 | 2025-07-17 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7153a124-45f5-3ee7-b778-63a4f3ec2254 | -6.82712 | -44.84065 | 2025-07-17 04:46:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 704f74a4-843e-3768-9926-3f92c566aa5c | -10.32591 | -49.90902 | 2025-07-17 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3ed7a5d1-3d2d-366d-a6ec-5d56bd0d7bd0 | -7.20357 | -45.33007 | 2025-07-17 04:46:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| db7fb187-0541-3d14-b7ef-4528abde57af | -6.84363 | -42.75109 | 2025-07-17 04:46:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 862c44ef-51c1-373e-8b41-049219bfbf18 | -10.96888 | -46.4725 | 2025-07-17 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 991f3a9c-d73e-3da1-92e5-941d7aceaeef | -11.11059 | -48.86841 | 2025-07-17 04:46:00 | NOAA-21 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0575b0e4-7c6d-398b-b2de-1aa3169fbc15 | -11.95016 | -48.41747 | 2025-07-17 04:46:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fd88b0c4-e9c3-3a9b-b24b-294587e0e27e | -8.54186 | -47.85365 | 2025-07-17 04:46:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 12c8cff0-f759-3867-bd5e-9c5b36dbde5d | -10.97256 | -46.47701 | 2025-07-17 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| c1aea5c7-2732-305d-b923-7990b2d6ec77 | -11.66947 | -43.77006 | 2025-07-17 04:46:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 526e9ac8-46cd-3178-827e-6c90f43d3ede | -7.20789 | -45.33063 | 2025-07-17 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a66a2745-a5a4-38b0-ab65-25a6cb54fb1c | -8.87551 | -50.15429 | 2025-07-17 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b94d6424-4fd3-3d65-acb9-7bbb6a7f6ded | -9.49542 | -40.39937 | 2025-07-17 04:46:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 76bd0e65-e432-3f3e-ac8e-fca02890d843 | -8.71281 | -50.0541 | 2025-07-17 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 55fad1e9-83f2-366a-8f39-db9a0b909f0e | -5.91801 | -43.47421 | 2025-07-17 04:46:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6cce115f-d6f7-34aa-bf4a-0fb20393ba79 | -6.73256 | -44.32998 | 2025-07-17 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| bbf0bb2d-300f-34c5-b74d-3c106492b632 | -6.71949 | -44.32306 | 2025-07-17 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fb1a2370-645b-3295-82c8-81e4ca08ea72 | -6.7149 | -44.32248 | 2025-07-17 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9f56be91-7867-38e0-9e0a-cd1da95edc73 | -9.41054 | -48.40267 | 2025-07-17 04:46:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e3d58dd2-b7ae-3386-baab-52eb6f9f94b5 | -11.94874 | -48.42503 | 2025-07-17 04:46:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 54cb88a4-4a42-347c-a337-e4249c4f48fd | -7.73064 | -50.76622 | 2025-07-17 04:46:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12ec01c3-0d0e-3269-b482-5b635365c532 | -7.34049 | -44.20585 | 2025-07-17 04:46:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4bf2a0ab-2380-32f6-93af-8fa6a57bc333 | -6.73973 | -47.42197 | 2025-07-17 04:46:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 08e77cd9-0432-3c67-b82c-faa59fc69e17 | -6.42937 | -45.31516 | 2025-07-17 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 74ec1a34-d906-3537-9dfa-bf76ab126c9e | -9.02602 | -61.22383 | 2025-07-17 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a57f8925-3cdd-3f1f-ae6e-b25d7fa9a397 | -6.1223 | -44.07324 | 2025-07-17 04:46:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cbe437d9-6c01-37fa-8115-1f88c3673ba7 | -11.24126 | -49.50285 | 2025-07-17 04:46:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ad189136-8f0e-37ac-9973-82b1b16c9013 | -11.50907 | -48.95612 | 2025-07-17 04:46:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a95e79fa-5953-3913-8852-8305da052ba3 | -11.33187 | -51.43879 | 2025-07-17 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 078fd83b-95b8-3616-b741-9ef13ef31cdc | -9.02064 | -61.22286 | 2025-07-17 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 545aa29a-20b4-3669-8e74-696c9f1f8002 | -8.8634 | -46.85705 | 2025-07-17 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a0ddb772-6cbd-3a46-afb6-6a3958ff9438 | -12.09839 | -48.19272 | 2025-07-17 04:46:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a04233a-c1a5-3a49-91ec-7148cfe6a5da | -6.81796 | -43.78782 | 2025-07-17 04:46:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d05ecf58-37cc-3196-a203-aee2e8343286 | -6.98052 | -43.7444 | 2025-07-17 04:46:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b43c123e-a3bc-3f62-8973-2b7071c8ea31 | -7.21652 | -45.33181 | 2025-07-17 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6bfce197-8028-3efe-9221-a8e24d9b09a1 | -10.59108 | -55.57691 | 2025-07-17 04:46:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3af85c6e-0080-3f46-ae28-1fa2bd2e0197 | -10.90018 | -49.21287 | 2025-07-17 04:46:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 15fc454a-3387-3766-a4fa-8fe5d62f93e9 | -4.74272 | -48.02187 | 2025-07-17 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d0b6cb8-c35c-36be-9fe1-f8d5743652f1 | -7.8956 | -55.42238 | 2025-07-17 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c007cdc3-5ce7-3e2c-82bc-fc2d94c69e6b | -12.02893 | -47.78223 | 2025-07-17 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 831e1a46-d238-31db-8e74-2420f2fadd70 | -11.66435 | -43.76943 | 2025-07-17 04:46:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 89806c86-6f89-3f8f-bbc9-6f6d643768f5 | -8.09756 | -43.14807 | 2025-07-17 04:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |


[Clique aqui para ver as próximas entradas](README23.md)
