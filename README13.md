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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 73722522-e0d7-3d4d-9113-1a8a37c8790f | -7.09056 | -44.56348 | 2025-08-22 03:55:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aa62de26-80fc-3a44-82c3-4028a213a4a2 | -5.93699 | -42.55933 | 2025-08-22 03:55:00 | NPP-375D | ÁGUA BRANCA | PIAUÍ | Brasil | 2200202 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a0cc66db-1d4d-3a8d-a523-4196276198b1 | -7.09439 | -44.56647 | 2025-08-22 03:55:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bf6c842b-67e0-3d87-bd4b-caa55dd663c4 | -7.95333 | -42.63699 | 2025-08-22 03:55:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| be2d2879-0428-31a4-be54-4d1e0ffe10d6 | -6.03119 | -44.36572 | 2025-08-22 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5b8de0e5-f319-3660-b7bf-e343f352f96d | -5.24615 | -37.69352 | 2025-08-22 03:55:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0d909eee-67ed-35a7-8206-80805c5eb7e5 | -7.09493 | -44.56421 | 2025-08-22 03:55:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dee2ebc1-5ff6-3f60-97b4-93d6b7e9147d | -6.49012 | -43.4495 | 2025-08-22 03:55:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d1ee88c0-3c49-3df9-bc52-959b9fe75e63 | -7.02453 | -44.63383 | 2025-08-22 03:55:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 80ff39d2-ffee-333a-a40d-15764e524667 | -6.42724 | -39.56282 | 2025-08-22 03:55:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 80c6da68-c6da-3dc1-88d6-b7a5c6551494 | -7.25152 | -44.70119 | 2025-08-22 03:55:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e23cf984-2ea5-30a3-8ede-59422a6cd2c4 | -2.4747 | -47.76957 | 2025-08-22 03:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 9d66841c-b652-35ba-83da-e3bbb3374384 | -7.4804 | -44.93365 | 2025-08-22 03:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cd7bc3aa-a040-300e-94c0-8a9e031b3986 | -3.81659 | -41.55623 | 2025-08-22 03:55:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b1843a14-7b7d-3262-9aba-19d0bd70f920 | -6.29481 | -43.8955 | 2025-08-22 03:55:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c85ba2c1-cf3d-333b-b55f-2b0e4f3ec0b5 | -6.49364 | -43.45362 | 2025-08-22 03:55:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7e3cbbf3-ac7b-3307-a861-522f707dce6c | -7.03034 | -44.62632 | 2025-08-22 03:55:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c32ef541-bfcd-3219-83fe-871aeedd2107 | -6.58199 | -44.4591 | 2025-08-22 03:55:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c63ea301-e79d-3794-b61d-319fde698aa2 | -4.14398 | -46.46049 | 2025-08-22 03:55:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9678fdce-9ed9-3346-8ce0-6d121fca26db | -7.05307 | -37.23612 | 2025-08-22 03:55:00 | NPP-375D | QUIXABA | PARAÍBA | Brasil | 2512606 | 25 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 5a63676c-0db5-39bf-8868-f637bb899ad2 | -6.02164 | -42.82133 | 2025-08-22 03:55:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 9a78c993-9eeb-3d21-9d2c-39bf20837765 | -6.03557 | -44.36649 | 2025-08-22 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1d9b53cf-ab28-370a-a129-bf15c2024b51 | -6.20837 | -43.56263 | 2025-08-22 03:55:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3033ecdd-4297-375c-b0a9-ec7ceb4c8e3d | -6.29835 | -43.90032 | 2025-08-22 03:55:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3b5742ef-9a01-3522-bb35-25b093b0e90d | -0.7498 | -47.75195 | 2025-08-22 03:55:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c58080f-1571-3117-bba0-eeb91b92415a | -6.4362 | -44.52448 | 2025-08-22 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3e1637fb-7485-3077-92ff-f051fbdced41 | -6.08296 | -44.13454 | 2025-08-22 03:55:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3e7d4f57-2cd3-3f1c-865c-9a91035b0780 | -3.45649 | -39.59585 | 2025-08-22 03:55:00 | NPP-375D | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f14aa54f-2395-3558-96e6-afa04bb47885 | -7.04046 | -44.62001 | 2025-08-22 03:55:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3340eb4e-631a-3b37-aa67-925e518e6eac | -5.14359 | -45.17419 | 2025-08-22 03:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 04765a3b-71cc-3020-9b8e-feeef9d216e5 | -3.81654 | -41.57755 | 2025-08-22 03:55:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1fa36f0d-f729-3b98-ab80-30d51382d27a | -6.06058 | -44.10915 | 2025-08-22 03:55:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cfaf6491-a0dd-3439-97e4-38c4ecc0d186 | -6.51131 | -44.58348 | 2025-08-22 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 2c3578bf-7860-3a10-83b3-7daa26c264af | -5.78155 | -43.60606 | 2025-08-22 03:55:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d8b106af-fb7a-3b5e-91bf-f1f48f821c8d | -5.46214 | -46.47329 | 2025-08-22 03:55:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d2e944ba-5821-3ffc-a8e7-942db2ee8578 | -4.39624 | -44.08571 | 2025-08-22 03:55:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 64d2d4f7-6c8e-3b06-9eea-c95ce97b8c6f | -7.26692 | -43.67143 | 2025-08-22 03:55:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2cb556b8-364e-3817-b120-1eed4e32d6ad | -6.41598 | -35.0294 | 2025-08-22 03:55:00 | NPP-375D | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| d0116059-d48e-3415-a58b-905dfee29426 | -3.99103 | -47.89015 | 2025-08-22 03:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 43a5fd9b-cd42-3b69-ab7b-27ab9a66e30e | -7.65121 | -45.2447 | 2025-08-22 03:55:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 064e8666-8474-31d4-8956-4e1d828292ae | -7.25079 | -44.70551 | 2025-08-22 03:55:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7b5405b3-8558-3ede-a738-12aa6b87276c | -4.65451 | -41.41259 | 2025-08-22 03:55:00 | NPP-375D | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 4af37238-b96d-30b8-8e1c-482c7a418446 | -6.35208 | -43.37907 | 2025-08-22 03:55:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0aa4795c-fda3-3167-9412-b9952a5cbd10 | -7.65313 | -46.22808 | 2025-08-22 03:55:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 947e1c2c-0156-33fe-a923-41cf5d8e1e82 | -6.07449 | -43.45219 | 2025-08-22 03:55:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4bef51b6-e19c-324f-b728-0b55d99d2efb | -6.4285 | -44.67978 | 2025-08-22 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4dfab003-c60a-3260-b716-f46b290c7fb9 | -3.17215 | -49.47778 | 2025-08-22 03:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84bee3df-e9b7-3c4b-b6b1-6ed5263c0f3f | -7.21521 | -35.03407 | 2025-08-22 03:55:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 416ab629-a7ac-3a2a-bf1f-b312f5906dfc | -3.23105 | -46.78905 | 2025-08-22 03:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ae2221ea-ade9-38a7-ad72-314e52f69467 | -7.15779 | -44.66982 | 2025-08-22 03:55:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a5382d21-c4f7-3d91-941f-f6841d350d44 | -5.87434 | -42.40767 | 2025-08-22 03:55:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| eed48b3f-758d-30c7-8236-510aa8f42cff | -6.41373 | -35.33262 | 2025-08-22 03:55:00 | NPP-375D | NOVA CRUZ | RIO GRANDE DO NORTE | Brasil | 2408300 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a9366ac2-15f6-358d-a370-f4310a94699e | -6.29341 | -43.69953 | 2025-08-22 03:55:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 095bb820-8410-3eac-af4d-1f22e7ecfb9e | -7.37469 | -35.11312 | 2025-08-22 03:55:00 | NPP-375D | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a0c0106c-6016-35c7-936f-62d088c325dc | -4.07643 | -46.92681 | 2025-08-22 03:55:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34354184-4c6c-3359-8936-28f4035477ea | -7.21973 | -35.03204 | 2025-08-22 03:55:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 212c7cfa-c0e3-3202-a2a4-aa55802880bc | -7.85238 | -45.19717 | 2025-08-22 03:55:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 115dd020-0b5d-3b3c-ac10-8e7a6b6ff455 | -7.94717 | -42.65773 | 2025-08-22 03:55:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 00b12930-4471-3fb6-860b-4024b4d3f339 | -5.37627 | -41.21932 | 2025-08-22 03:55:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 5475b0da-086f-3d01-9c6c-1fee15f487e0 | -7.25892 | -39.67228 | 2025-08-22 03:55:00 | NPP-375D | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 0cfd6661-7708-3d8d-a6c9-1101898e1358 | -5.25223 | -44.45448 | 2025-08-22 03:55:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7577949d-8f3a-307f-956e-45e2ba6f125e | -6.48883 | -42.85728 | 2025-08-22 03:55:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7e75094f-6469-321d-8237-a9568762cc6f | -3.47858 | -39.14867 | 2025-08-22 03:55:00 | NPP-375D | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a3f7b08f-647b-3668-8d0c-f9aa624bb69f | -3.3901 | -47.61521 | 2025-08-22 03:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49369aa7-3783-3278-9b0d-b6a4891bceab | -4.31158 | -48.10184 | 2025-08-22 03:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 83e09275-79cc-370d-a7ef-b053e78b6023 | -7.37104 | -35.11258 | 2025-08-22 03:55:00 | NPP-375D | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9aa39520-ab42-3a81-8fca-bac8deeae254 | -3.62791 | -43.54437 | 2025-08-22 03:55:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 351f16c2-4c8f-36c8-8e53-66812b342192 | -3.98533 | -47.88886 | 2025-08-22 03:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a9ffd7f0-12e3-3dc0-ad14-6a848d4bfaa5 | -7.09078 | -44.5614 | 2025-08-22 03:55:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c2582ac6-c079-3198-97cb-895ad2416835 | -5.79598 | -45.07071 | 2025-08-22 03:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7d19c37f-6eb3-37b2-afcf-036c880e04c2 | -6.03924 | -44.37156 | 2025-08-22 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a6a01aa6-12ac-33c3-bacb-5628694b25dc | -5.78092 | -43.60978 | 2025-08-22 03:55:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7cdc518e-1015-398e-955f-4d95b00514ef | -4.40506 | -44.08726 | 2025-08-22 03:55:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0fc108e8-b88d-3cec-949f-485fd162ec04 | -6.11426 | -44.37814 | 2025-08-22 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 62f37e02-e424-3912-bf05-7c23ed3285a0 | -6.43835 | -44.5116 | 2025-08-22 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cdf9f04e-bc9a-30a4-8f8b-7007b62c190b | -5.38384 | -41.2191 | 2025-08-22 03:55:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 79187d7c-149d-3917-9e17-48c566526549 | -6.49596 | -43.43972 | 2025-08-22 03:55:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8cb664eb-c32d-32d3-b6ae-e2d73961cf75 | -3.42472 | -43.33544 | 2025-08-22 03:55:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a730f3c6-50d9-3680-a18c-836ebe2ce3c4 | -7.16218 | -44.67057 | 2025-08-22 03:55:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aa89aeff-25ec-36cd-bdb4-4b3ea7f489cc | -3.42833 | -43.34007 | 2025-08-22 03:55:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fdd309a6-2ea9-39ee-8834-3e9c83278ab7 | -2.92029 | -48.30363 | 2025-08-22 03:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0e262cc-b370-33a7-a0e4-b8e5144fead7 | -2.91605 | -48.30317 | 2025-08-22 03:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ee5677c2-e1c9-37e7-ba20-b2538114c6b3 | -3.81806 | -41.56834 | 2025-08-22 03:55:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 5d478850-af32-3c45-a4d3-f8078e85b1d9 | -6.42109 | -44.66932 | 2025-08-22 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0e6c3621-99f4-3739-8154-9c0ed18812c5 | -6.82562 | -44.23647 | 2025-08-22 03:55:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a4e6748d-21d9-3370-a226-bda3f4045729 | -6.41966 | -44.67787 | 2025-08-22 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 81032948-c00c-3d95-aeb6-e3f0305b055d | -2.69229 | -48.20596 | 2025-08-22 03:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3651895c-9eeb-3caf-bb14-5b9a0b5c33d4 | -7.17172 | -44.66762 | 2025-08-22 03:55:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5e75d818-0668-331c-8d9a-6ddbd7017766 | -5.37991 | -41.21991 | 2025-08-22 03:55:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 52b25731-a693-3391-9dd0-7bc81503532f | -7.62182 | -46.24895 | 2025-08-22 03:55:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f572a7a4-7f9b-38c4-81cc-591b5c484e96 | -3.35785 | -43.16865 | 2025-08-22 03:55:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 20c61fc9-de47-3af7-9e35-f318cf939acb | -5.464 | -46.47399 | 2025-08-22 03:55:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d42ee18-23fc-3da1-88ff-130339643c34 | -6.4591 | -44.56995 | 2025-08-22 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0ee6b841-bea5-3d28-b4a0-1428ceba4938 | -5.14272 | -45.1792 | 2025-08-22 03:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 05addf45-6ef6-317d-b877-09c6bb83a20f | -2.4541 | -47.74858 | 2025-08-22 03:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bd786352-088f-31eb-8764-ef58168fb71d | -7.72286 | -44.08958 | 2025-08-22 03:55:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9bd59e4c-24a0-3a6b-869d-13a903627ea1 | -7.24125 | -44.78823 | 2025-08-22 03:55:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 98f1a7e7-d7e8-3143-ba56-f81c481b69d6 | -2.45989 | -47.74986 | 2025-08-22 03:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d51c5b88-49ae-3ef8-9927-0a2b1610c2d5 | -7.47057 | -44.44864 | 2025-08-22 03:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c4fbfe5f-50d2-3004-8a94-9caa4886cbdb | -6.0319 | -44.36149 | 2025-08-22 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README14.md)
