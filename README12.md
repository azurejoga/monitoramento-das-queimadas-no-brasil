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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d8d8a8a9-5c98-3b49-95a3-9ab8224bfd4d | -18.54235 | -56.81684 | 2026-07-22 05:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 85100a8b-30d4-3f0b-89d4-e0fba7bb4051 | -18.54117 | -56.8156 | 2026-07-22 05:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 3b2c6ecd-d731-35ad-8434-e7a5646f91fe | -18.5351 | -56.80896 | 2026-07-22 05:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 6661c9f9-d233-3912-b90d-28546cf37a70 | -18.53579 | -56.81607 | 2026-07-22 05:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 3a30a87f-3074-35e3-8d29-4df75d779ef1 | -18.54067 | -56.82145 | 2026-07-22 05:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.1 |
| 1a718d80-24e6-3901-8831-2f90c3cb71b2 | -17.5748 | -47.4996 | 2026-07-22 06:00:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 373c1ee7-334c-35e4-bec6-447970354bfa | -17.57235 | -47.50833 | 2026-07-22 06:08:00 | AQUA_M-M | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 4f709043-3a7f-33f4-b5ee-c5191ec62dce | -17.57301 | -47.50084 | 2026-07-22 06:08:00 | AQUA_M-M | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 9eba91c8-3fa7-38cb-bee4-9be17b9cdc31 | -17.57609 | -47.48865 | 2026-07-22 06:08:00 | AQUA_M-M | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 41.8 |
| 25984d6c-7c56-35d0-b18d-fbf5cdd7d033 | -17.5748 | -47.4996 | 2026-07-22 06:10:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 14f02229-0913-3340-abb1-38471574b9f6 | -17.5748 | -47.4996 | 2026-07-22 06:20:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 63eeb365-b301-302c-9339-687758440f19 | -10.10094 | -68.17327 | 2026-07-22 06:25:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a3d715b8-79c5-3c84-bd7e-606705deafa6 | -10.02385 | -65.05037 | 2026-07-22 06:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 78df9f24-52c9-318c-a41f-794d9720900a | -10.0234 | -65.05379 | 2026-07-22 06:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7cef41ce-c703-3131-a3c9-bb2977dba86b | -17.5947 | -47.4956 | 2026-07-22 06:30:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 46.8 |
| de8b042a-a458-3cbf-8297-54bc0da038cd | -17.5748 | -47.4996 | 2026-07-22 06:30:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 13979e09-a00a-3f64-bfbe-a520d78c78aa | -22.4683 | -54.1871 | 2026-07-22 06:40:00 | GOES-19 | GLÓRIA DE DOURADOS | MATO GROSSO DO SUL | Brasil | 5004007 | 50 | 33 | nan | nan | nan | Mata Atlântica | 140.4 |
| 0a300bcc-6cf3-30ee-a3e7-1a995a7495eb | -17.3331 | -45.2681 | 2026-07-22 06:40:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 999374c6-a590-3a23-8f07-e1855b8973e0 | -19.6278 | -54.6139 | 2026-07-22 06:40:00 | GOES-19 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 489.3 |
| 32a76d16-79ee-3e15-ab43-25ead8e25e99 | -23.2494 | -50.6155 | 2026-07-22 06:40:00 | GOES-19 | CORNÉLIO PROCÓPIO | PARANÁ | Brasil | 4106407 | 41 | 33 | nan | nan | nan | Mata Atlântica | 176.7 |
| 59ffa4d8-6963-34c8-b8ef-814f9c8dd7ff | -17.3337 | -45.2443 | 2026-07-22 06:40:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 41.1 |
| b9f2eb8b-089b-3173-ab10-e22360bc2ded | -19.626 | -54.6996 | 2026-07-22 06:40:00 | GOES-19 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 4c295cb5-3d9a-3b46-b05a-1ef4d16d6f22 | -22.5301 | -54.1974 | 2026-07-22 06:40:00 | GOES-19 | JATEÍ | MATO GROSSO DO SUL | Brasil | 5005103 | 50 | 33 | nan | nan | nan | Mata Atlântica | 192.4 |
| ba9f5914-336f-396c-809f-4144b3e3cf55 | -22.3905 | -50.811 | 2026-07-22 06:40:00 | GOES-19 | JOÃO RAMALHO | SÃO PAULO | Brasil | 3525607 | 35 | 33 | nan | nan | nan | Cerrado | 87.8 |
| c3c16566-d9ba-3b3e-b9ef-eebc07a4e24a | -19.6269 | -54.6568 | 2026-07-22 06:40:00 | GOES-19 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 215.9 |
| ba3c155d-4a86-3336-902a-eeba201c60a8 | -22.4699 | -54.121 | 2026-07-22 06:40:00 | GOES-19 | GLÓRIA DE DOURADOS | MATO GROSSO DO SUL | Brasil | 5004007 | 50 | 33 | nan | nan | nan | Mata Atlântica | 553.5 |
| 870babfb-f207-3361-9d5f-52814d0ddd0c | -17.156 | -39.4621 | 2026-07-22 06:40:00 | GOES-19 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 263.9 |
| 015682b0-bea7-32d9-8f45-aa34bd6a85b2 | -22.3911 | -50.7881 | 2026-07-22 06:40:00 | GOES-19 | JOÃO RAMALHO | SÃO PAULO | Brasil | 3525607 | 35 | 33 | nan | nan | nan | Cerrado | 151.3 |
| 189b9857-b503-3a4e-aafa-1037b45b3fb4 | -23.2501 | -50.5924 | 2026-07-22 06:40:00 | GOES-19 | CORNÉLIO PROCÓPIO | PARANÁ | Brasil | 4106407 | 41 | 33 | nan | nan | nan | Mata Atlântica | 172.6 |
| 4c6391fa-2c6f-3e98-af7a-87e72be8f3b7 | -17.3343 | -45.2205 | 2026-07-22 06:40:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 144.8 |
| b48a2a8e-4265-3bb2-85cf-633d90bc7446 | -20.23 | -51.1943 | 2026-07-22 06:40:00 | GOES-19 | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Mata Atlântica | 114.7 |
| 79bdcc67-223a-36dd-a2d4-a2527a9085a8 | -18.5606 | -44.9418 | 2026-07-22 06:40:00 | GOES-19 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 148.3 |
| 2b28fd6b-a615-3431-863d-a5e8be0d1deb | -17.5748 | -47.4996 | 2026-07-22 06:40:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 45.3 |
| 119cabf8-e048-3a85-9e94-17fb3f7d0772 | -18.5586 | -45.0141 | 2026-07-22 06:40:00 | GOES-19 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 153.1 |
| effb6fd7-81a4-3255-aab2-a5642ccf8632 | -23.2488 | -50.6386 | 2026-07-22 06:40:00 | GOES-19 | CORNÉLIO PROCÓPIO | PARANÁ | Brasil | 4106407 | 41 | 33 | nan | nan | nan | Mata Atlântica | 179.2 |
| f51860e7-a623-305a-96ae-5e4f3c81ea26 | -18.5599 | -44.9659 | 2026-07-22 06:40:00 | GOES-19 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 102.6 |
| fd65ff62-b406-3e52-a1c7-258c74112136 | -19.6265 | -54.6782 | 2026-07-22 06:40:00 | GOES-19 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 162.0 |
| 7acbedbf-d511-3cd6-b2cc-4f938efa83ee | -19.6274 | -54.6353 | 2026-07-22 06:40:00 | GOES-19 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 255.3 |
| f5318d52-0244-3ac5-bb1e-9df0e8aeacff | -18.5592 | -44.99 | 2026-07-22 06:40:00 | GOES-19 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 196.3 |
| ad7dfa96-76b1-3ca7-b1e2-9759e64de907 | -12.533 | -48.2555 | 2026-07-22 11:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| ee7f9efe-27f0-33c8-a434-9aa858ff9b62 | -12.5334 | -48.2333 | 2026-07-22 11:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 6d0e072b-cc08-3fc1-abfb-b6ac5e2e2c75 | -6.0487 | -43.8712 | 2026-07-22 12:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 93.5 |
| afb87c04-ccca-3efc-b3ac-54a7a8c41b62 | -12.533 | -48.2555 | 2026-07-22 12:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 93.8 |
| ad93aa35-3c0c-3d62-9e72-81372287a754 | -6.0487 | -43.8712 | 2026-07-22 12:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 50dda5d8-76a1-3e2d-8558-dcd5b141cf61 | -12.5334 | -48.2333 | 2026-07-22 12:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 489ef292-5045-330e-8204-f36322658da8 | -11.61051 | -55.32647 | 2026-07-22 12:21:00 | TERRA_M-T | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| def74111-36ef-33cc-873d-153b86fa1468 | -12.3246 | -53.27933 | 2026-07-22 12:21:00 | TERRA_M-T | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e41ae22b-c5bb-377e-88ee-f0dd76dde078 | -10.59033 | -55.09882 | 2026-07-22 12:21:00 | TERRA_M-T | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fe5d08c9-23e6-3eee-90a2-61179df039b3 | -9.52394 | -47.14477 | 2026-07-22 12:21:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 9302cd10-98f5-369b-ac09-f15fd6755d85 | -10.42935 | -50.19747 | 2026-07-22 12:21:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 5412d7fe-1f0e-399c-9d11-71c9ee32f6a4 | -7.96356 | -47.27051 | 2026-07-22 12:21:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 92959550-a61a-3660-b856-5bc8790bc5fa | -12.31211 | -50.0468 | 2026-07-22 12:21:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 8cd1e713-da5c-3e5b-b709-1ac14380e554 | -10.42322 | -50.1902 | 2026-07-22 12:21:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 9b6adbea-90b4-3942-96fd-41fc14e13df8 | -10.6192 | -50.27808 | 2026-07-22 12:21:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| fbf4f429-99e5-35b5-a104-fa9282f0b8c1 | -10.62561 | -50.28543 | 2026-07-22 12:21:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 18.3 |
| dd954eba-fd5a-3ccf-a687-bd3f8930eb88 | -8.52638 | -54.7579 | 2026-07-22 12:21:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 10bfd4cc-b73e-3335-aca4-9bcc9c916f4d | -9.52853 | -47.10925 | 2026-07-22 12:21:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 33.3 |
| df02b482-270f-341d-bcde-f7ee2e065152 | -12.51866 | -48.24712 | 2026-07-22 12:21:00 | TERRA_M-T | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 143.1 |
| fc4dbcb4-7baa-3fa6-ad08-a9a2c0c6e245 | -10.82545 | -50.4402 | 2026-07-22 12:21:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 24.4 |
| c44e0f20-0a30-316c-b3b2-86e33a021c1d | -9.52502 | -47.13814 | 2026-07-22 12:21:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 98665354-058a-329c-9a9b-97e0b80d4e20 | -11.99013 | -50.5458 | 2026-07-22 12:21:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| d3ea7aa5-4b41-31b0-ac0e-7aa95a80055c | -11.78088 | -61.32358 | 2026-07-22 12:21:00 | TERRA_M-T | PRIMAVERA DE RONDÔNIA | RONDÔNIA | Brasil | 1101476 | 11 | 33 | nan | nan | nan | Amazônia | 194.3 |
| 11e1ba4d-c1ad-3289-9212-c3f1b6fd1724 | -9.52721 | -47.11604 | 2026-07-22 12:21:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 786a7b78-66c5-3df6-81da-f4cce782c67d | -12.53304 | -48.24865 | 2026-07-22 12:21:00 | TERRA_M-T | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 38c89a3e-c57a-32a8-8fc0-0334d72a35fb | -10.42106 | -50.20708 | 2026-07-22 12:21:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| bf013e4c-958a-34b3-8657-33cc1f3013a5 | -7.96141 | -47.26479 | 2026-07-22 12:21:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 170ee7a5-9cfc-3f4b-a5b8-3f6d2f9f7661 | -17.74122 | -52.75289 | 2026-07-22 12:23:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 9ea5f345-1e8a-3464-a589-ac888ca566e8 | -17.74289 | -52.73861 | 2026-07-22 12:23:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 1428c1b8-7134-35e1-a448-900851a6eb74 | -12.5138 | -48.2581 | 2026-07-22 12:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 8d559be8-3269-369d-bead-1f85ab6fa994 | -6.0487 | -43.8712 | 2026-07-22 12:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 8a51b212-567a-3b50-821b-a915e9ca0f4d | -12.533 | -48.2555 | 2026-07-22 12:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 8c9b0e0e-1d9c-38ac-92cf-0bb086fe38c5 | -12.5334 | -48.2333 | 2026-07-22 12:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| d0afbad9-db85-34f6-b69d-3c849076c60b | -12.533 | -48.2555 | 2026-07-22 12:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 931c5748-e6ea-3b0f-89f0-9591142e2e73 | -6.0487 | -43.8712 | 2026-07-22 12:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 204accaf-3ffd-3e96-9795-2af2d237278d | -12.5138 | -48.2581 | 2026-07-22 12:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 044f1a9b-61a0-3216-92b2-076573c2b3a7 | -6.0487 | -43.8712 | 2026-07-22 12:50:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 145.6 |
| b65d0e46-e5d5-3832-94eb-7be77bee51de | -12.5138 | -48.2581 | 2026-07-22 12:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 14d52dc9-dfbe-376b-aa06-78c7cc35639c | -12.533 | -48.2555 | 2026-07-22 12:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 131.1 |
| a9dd9235-a199-3078-8b8c-722b19c948e5 | -12.5334 | -48.2333 | 2026-07-22 12:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 130.0 |
| 721c7692-11d7-31b8-ad2f-b0f8e160336d | -12.5138 | -48.2581 | 2026-07-22 13:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 112.6 |
| ec9b4ced-cb59-35b0-8b35-1fefb4cb961f | -12.533 | -48.2555 | 2026-07-22 13:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 165.7 |
| db176ca5-7ea3-32aa-aed8-3214767e87a0 | -12.5334 | -48.2333 | 2026-07-22 13:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 120.4 |
| bf9968ad-349a-33cf-ac97-a52405b61291 | -6.0487 | -43.8712 | 2026-07-22 13:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 120.8 |
| fd8c9e49-b536-36d8-8094-5dece268fe54 | -6.03 | -43.8727 | 2026-07-22 13:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 334dd305-d6d3-3828-884b-fd608b5e43fa | -12.5138 | -48.2581 | 2026-07-22 13:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 106.4 |
| b9428401-ed52-3a16-af2c-33d0a26d31e5 | -12.5334 | -48.2333 | 2026-07-22 13:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 152.9 |
| 0ff1020a-6ef1-3f86-99c9-399f49c1a5c3 | -17.0609 | -45.043 | 2026-07-22 13:10:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 94.5 |
| f4686629-6354-3acc-9746-3ab1ef9dc01a | -10.634 | -46.5877 | 2026-07-22 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| fcdd43f1-524f-383c-9bbb-0edba79404e6 | -6.0487 | -43.8712 | 2026-07-22 13:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 93d7b3ba-f636-333a-aead-79e06c031e72 | -12.533 | -48.2555 | 2026-07-22 13:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 176.6 |
| ba14c4f7-2f00-3439-8bb6-dbb2c3871ea3 | -12.533 | -48.2555 | 2026-07-22 13:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 187.9 |
| e7bfdbb5-0a58-3e1f-9878-889e045636bf | -12.5138 | -48.2581 | 2026-07-22 13:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 139.9 |
| 4a4e3c8c-0b14-3522-a597-d051a6960504 | -12.5334 | -48.2333 | 2026-07-22 13:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 142.1 |
| bdc429d9-01ef-33c0-9f30-a32b9048f83d | -6.0487 | -43.8712 | 2026-07-22 13:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 141.4 |
| ab40c6ca-3a10-3a7c-a731-786fbcfa8918 | -12.3321 | -50.0073 | 2026-07-22 13:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 9c74960b-775c-3b9d-a586-fb5e851f8612 | -13.3169 | -54.3221 | 2026-07-22 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 3d384446-d26e-33e8-87a2-8f4f522384f6 | -12.5334 | -48.2333 | 2026-07-22 13:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 126.5 |
| a372f766-2eb2-3828-a35b-a69d2af6329a | -12.5138 | -48.2581 | 2026-07-22 13:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 165.9 |
| e95c7f05-d55f-3e0b-98d8-3b93c7b526b1 | -6.0487 | -43.8712 | 2026-07-22 13:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 156.7 |
| ed598d87-f55b-31c5-898d-482bbad19d87 | -12.3321 | -50.0073 | 2026-07-22 13:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |


[Clique aqui para ver as próximas entradas](README13.md)
