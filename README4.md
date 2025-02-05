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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 14cb0b39-cae1-3659-9aeb-02813eb50aed | -12.53805 | -48.32776 | 2025-02-05 04:31:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5e96b39c-b267-3042-9d74-08592247ee2f | -10.94813 | -40.73812 | 2025-02-05 04:31:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 08d9a6cf-8d7b-306e-9770-bbaf1a7e71f2 | -7.05403 | -44.37984 | 2025-02-05 04:31:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1f2da2df-4206-346f-ad38-7b076c6b2768 | -12.64915 | -43.81431 | 2025-02-05 04:31:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a063e88-d1ed-32c8-b8c5-69a71c2b3ba2 | -7.04393 | -44.39667 | 2025-02-05 04:31:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 369c4e00-02e4-3eca-8365-b9d4f6694aae | -12.5386 | -48.32417 | 2025-02-05 04:31:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae9dfbe2-e813-327a-ab11-f20a053ac664 | -7.04262 | -44.40551 | 2025-02-05 04:31:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c75b4a33-bf89-3a52-81ed-0f215700d4c9 | -7.04633 | -44.40597 | 2025-02-05 04:31:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d42fa404-f092-372c-b530-98f19efd6e73 | -11.0256 | -45.0526 | 2025-02-05 04:31:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 84c68f8a-769d-323a-a310-2370041adf98 | -11.02495 | -45.05719 | 2025-02-05 04:31:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a5162a92-5864-3a7f-8f6d-b20a1427f269 | -9.47359 | -35.93495 | 2025-02-05 04:31:00 | NOAA-20 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 5c3353b7-2d2d-3690-a233-84418b76cb49 | -12.64863 | -43.81813 | 2025-02-05 04:31:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 87043e49-e000-33ef-9444-0e5553a2b59b | -11.45568 | -40.71272 | 2025-02-05 04:31:00 | NOAA-20 | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b9187f71-874c-3892-aab9-785cce4f3d49 | -12.54139 | -48.32829 | 2025-02-05 04:31:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5648c676-45a9-3da6-9db9-aebd1210deff | -7.04831 | -44.39272 | 2025-02-05 04:31:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| adb6d012-e905-3bc4-993c-4ff13e57d786 | -7.05269 | -44.38881 | 2025-02-05 04:31:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e4de5d5-4ed7-3f2a-b857-136f82f8aae3 | -17.82027 | -45.31993 | 2025-02-05 04:33:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 64199c4a-979a-376b-b85f-8e116257367a | -15.75173 | -42.64919 | 2025-02-05 04:33:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 30c02dc4-61a9-3526-bb27-bdad2c0b0149 | -20.76247 | -46.7697 | 2025-02-05 04:33:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e3504489-5636-38f1-b8f8-3fadffe88213 | -16.86879 | -40.69985 | 2025-02-05 04:33:00 | NOAA-20 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| fbdf19da-2ef3-30e2-a0b7-5e8e069de84f | -17.7134 | -43.45105 | 2025-02-05 04:33:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 84de95ad-8fad-3b9f-8134-4d8c3f85e6a4 | -15.75434 | -42.64793 | 2025-02-05 04:33:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5303b39c-af20-326a-b028-eb2116fdcdb6 | -17.66709 | -54.16586 | 2025-02-05 04:33:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 246e29e2-861e-361d-a45e-1195c87daad2 | -16.68237 | -43.88522 | 2025-02-05 04:33:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7e087a10-56a6-3061-bc6a-f18ab370f70d | -22.20153 | -56.317 | 2025-02-05 04:36:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 54866fb1-7562-376a-b797-93a601a477a0 | -22.89968 | -43.75031 | 2025-02-05 04:36:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 0db827ec-4c75-3426-ad99-f8aa1bd5ec85 | -22.89927 | -43.75146 | 2025-02-05 04:36:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 6524bc1e-d491-3156-99ce-9cdaf695b46a | -22.67577 | -42.85473 | 2025-02-05 04:36:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d77caf4c-bb29-3100-a965-fcd0205b114c | -27.08613 | -50.51133 | 2025-02-05 04:36:00 | NOAA-20 | SANTA CECÍLIA | SANTA CATARINA | Brasil | 4215505 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 56bfa34f-160c-38f6-ac19-49aaa65fdecc | -29.75912 | -54.76414 | 2025-02-05 04:38:00 | NOAA-20 | SÃO VICENTE DO SUL | RIO GRANDE DO SUL | Brasil | 4319802 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| a701bd7d-0cb6-3ae5-a0b3-a08f05ad11e7 | -28.58654 | -49.44133 | 2025-02-05 04:38:00 | NOAA-20 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d8d4d79a-ecb9-3fe0-a041-f3235d694114 | -27.96878 | -51.63689 | 2025-02-05 04:38:00 | NOAA-20 | LAGOA VERMELHA | RIO GRANDE DO SUL | Brasil | 4311304 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 913bf9c0-3b26-3a51-930f-60dc9c30264e | -29.88647 | -52.21751 | 2025-02-05 04:38:00 | NOAA-20 | RIO PARDO | RIO GRANDE DO SUL | Brasil | 4315701 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 816ac5e8-31b1-3ace-8287-7afa6bdb2e0a | -29.39017 | -52.03104 | 2025-02-05 04:38:00 | NOAA-20 | ARROIO DO MEIO | RIO GRANDE DO SUL | Brasil | 4301008 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| fdcdd8d5-a4fa-3096-a9c1-8824ba64f4dc | -29.75578 | -54.76341 | 2025-02-05 04:38:00 | NOAA-20 | SÃO VICENTE DO SUL | RIO GRANDE DO SUL | Brasil | 4319802 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 76d4f4a4-649d-3771-8284-b347d2e96152 | -30.5153 | -52.05354 | 2025-02-05 04:38:00 | NOAA-20 | DOM FELICIANO | RIO GRANDE DO SUL | Brasil | 4306502 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| afb3261e-200e-3d5f-afdd-4a732acf79a2 | -29.89117 | -51.23447 | 2025-02-05 04:38:00 | NOAA-20 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 2.1 |
| 69c2ea90-692d-396b-90f9-ec0d4aa87125 | -29.95237 | -51.61782 | 2025-02-05 04:38:00 | NOAA-20 | CHARQUEADAS | RIO GRANDE DO SUL | Brasil | 4305355 | 43 | 33 | nan | nan | nan | Pampa | 1.7 |
| 46e421b3-2600-3f08-aed8-382ac7123a91 | -6.41278 | -35.64157 | 2025-02-05 04:42:00 | AQUA_M-M | LAGOA D'ANTA | RIO GRANDE DO NORTE | Brasil | 2406205 | 24 | 33 | nan | nan | nan | Caatinga | 31.6 |
| 04ac78b4-a548-394a-b7f6-bc1d5e69e7b0 | -6.41132 | -35.65102 | 2025-02-05 04:42:00 | AQUA_M-M | LAGOA D'ANTA | RIO GRANDE DO NORTE | Brasil | 2406205 | 24 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 3021a6a1-0e12-3c17-a2fd-564de0698375 | -8.7347 | -64.0788 | 2025-02-05 05:10:00 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 54ea1be6-6e12-3e2d-a140-9e2b9c7b3247 | -8.7347 | -64.0788 | 2025-02-05 05:20:00 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 46.7 |
| d10d3139-23ef-3825-bb72-70b7913faa26 | 3.59033 | -61.42989 | 2025-02-05 05:20:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| db0787fd-fb13-3844-823b-5fa1f3fba812 | 3.69388 | -60.61609 | 2025-02-05 05:20:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c5cb4cd-4cf7-3eb6-a01a-4847aebb8c7b | 3.58608 | -61.42627 | 2025-02-05 05:20:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ae5ecadb-094a-31d9-8ddb-67d8e9bdd93f | 3.58789 | -61.42727 | 2025-02-05 05:20:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 668d77bf-9af3-3813-ab18-2bbc368a6150 | 4.22855 | -59.83978 | 2025-02-05 05:20:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb7893b8-d3cc-3bfa-ba82-23b7ceb76840 | 3.59149 | -61.4267 | 2025-02-05 05:20:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e9f22d2d-87d1-3830-b55c-0ceb9a10f7d0 | 2.009 | -61.38197 | 2025-02-05 05:20:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 89066fcd-c92f-3d54-8763-bdf46c3f884e | 3.58969 | -61.42574 | 2025-02-05 05:20:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ff080d72-ccd2-32cd-9eb8-5bd36a060a1a | -9.13553 | -67.10896 | 2025-02-05 05:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82d9e4fd-bbf7-336d-a0e9-95fb3fa92dd2 | 1.38591 | -60.80499 | 2025-02-05 05:22:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6e5348ea-4eb9-3705-96fe-e3f7758026ca | -2.97622 | -50.58974 | 2025-02-05 05:22:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c9c43d78-8779-3635-841b-9e7df59a4580 | -9.13483 | -67.11304 | 2025-02-05 05:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b2c3d9d-3f41-3a90-b75f-304c7cfa3ab3 | -2.97518 | -50.58815 | 2025-02-05 05:22:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c5faf370-6bb0-370d-b3d4-2ef31c4e3c4f | -8.99771 | -63.81453 | 2025-02-05 05:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 61a73dba-1b29-3454-8ad5-934d9cf7d7ec | -8.73229 | -64.07762 | 2025-02-05 05:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| daaa7a5f-e407-3bce-a724-94a3d3f8c324 | -11.97523 | -63.84323 | 2025-02-05 05:22:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2ee70681-9c40-3c10-b4bc-f2617d43e8b8 | -8.72306 | -64.08884 | 2025-02-05 05:22:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 8cc62973-346f-3aaf-8fde-2cb605b2c717 | -8.72871 | -64.07703 | 2025-02-05 05:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 37d10bcc-e7af-3bd5-9d40-15a3bbe9f77c | -8.72566 | -64.0813 | 2025-02-05 05:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 8fc069da-006e-349e-a585-9f74e6beadb2 | -2.9747 | -50.59148 | 2025-02-05 05:22:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b2212db6-7169-3212-9124-4b6231313c3a | -8.72375 | -64.08471 | 2025-02-05 05:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 458bd1c4-db1c-38a2-9c98-3ce7f5344810 | -9.13126 | -67.10822 | 2025-02-05 05:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 55f27ba7-1898-3f1c-b6e4-96f9046fee74 | -11.97305 | -63.83503 | 2025-02-05 05:22:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 41d5d5b0-83ef-3e56-abd2-71d73693efff | -9.71388 | -64.54083 | 2025-02-05 05:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d77ee3d8-600b-38f1-a0f5-24de0ff4a4bb | -8.725 | -64.08543 | 2025-02-05 05:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 908cbe2b-d6e6-34dc-b75c-bbf0bfd772a7 | -8.72017 | -64.08413 | 2025-02-05 05:22:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| de9fe00b-b95d-3906-aea3-fda7d9e57635 | -8.72802 | -64.08117 | 2025-02-05 05:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5b56cfef-b114-3f14-876a-eccf86f8a3b9 | -8.72444 | -64.08059 | 2025-02-05 05:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 80957517-b325-3d61-8cb4-8f67fda014e3 | -8.72141 | -64.08485 | 2025-02-05 05:22:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| d3d4fc8a-27bc-31ab-88b2-d85813b56b9e | -8.72733 | -64.08529 | 2025-02-05 05:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 61c52301-eb78-3625-b58a-424693e3e68d | -12.36576 | -63.88456 | 2025-02-05 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 203f4fc6-8433-3611-9df5-032ef19d6b6a | -16.10883 | -60.04737 | 2025-02-05 05:25:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a41a7a5f-b3c0-3e8d-811f-51c75f0e5baf | -12.15017 | -63.80572 | 2025-02-05 05:25:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eeb0bb09-884c-3100-9c41-2fb6beb716ae | -16.1077 | -58.22262 | 2025-02-05 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 4963ea07-fd04-3b5a-a866-e0f499918c54 | -16.10132 | -60.07514 | 2025-02-05 05:25:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d2ad2844-def5-366b-a589-948a0feca75b | -12.20774 | -64.03528 | 2025-02-05 05:25:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b6e716d-66f4-3399-975f-08c3fe7803b2 | -17.747 | -56.31299 | 2025-02-05 05:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 1a713699-e119-388a-8dd7-65a3794bbfa0 | -12.40558 | -63.98523 | 2025-02-05 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dd3cdd8b-ee8f-3963-9f17-cafe1399db91 | -12.14675 | -63.80515 | 2025-02-05 05:25:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 785875f9-5826-3cbd-842d-b71bcead4c3d | -16.02604 | -59.8395 | 2025-02-05 05:25:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a500fd3a-4427-3f4a-b453-21eca118ee95 | -12.16827 | -64.01675 | 2025-02-05 05:25:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d6819143-4834-3472-be29-47e07f5e9977 | -14.5287 | -59.74697 | 2025-02-05 05:25:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6e4db6a6-8355-3e3a-b788-38a4271587f6 | -15.04686 | -59.89077 | 2025-02-05 05:25:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4724ab73-e214-30ba-a529-d2dec847ea0f | -28.07944 | -53.00298 | 2025-02-05 05:27:00 | NOAA-21 | CHAPADA | RIO GRANDE DO SUL | Brasil | 4305306 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e5736a25-7151-314e-ba74-bf9ee4b013d5 | -28.07979 | -52.99767 | 2025-02-05 05:27:00 | NOAA-21 | ALMIRANTE TAMANDARÉ DO SUL | RIO GRANDE DO SUL | Brasil | 4300471 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| b0be2111-1743-34b7-9b6b-70b646bca076 | -21.07579 | -56.39345 | 2025-02-05 05:27:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b2f2a51c-2680-3763-966c-15832ed5a0e9 | -28.07834 | -53.00256 | 2025-02-05 05:27:00 | NOAA-21 | ALMIRANTE TAMANDARÉ DO SUL | RIO GRANDE DO SUL | Brasil | 4300471 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| b54e120e-1106-3ad0-b7a9-9d2726b46acd | -28.07866 | -52.99717 | 2025-02-05 05:27:00 | NOAA-21 | ALMIRANTE TAMANDARÉ DO SUL | RIO GRANDE DO SUL | Brasil | 4300471 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 0625946b-c968-38ed-b018-db37521d6e59 | 2.00905 | -61.37867 | 2025-02-05 05:46:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed23d278-6b35-3cb5-8f53-ebf0f9cbb98b | 4.12156 | -59.89068 | 2025-02-05 05:46:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6cb8fc9d-34d2-3a5a-8f30-2ef9a5e236b8 | 3.59307 | -61.42689 | 2025-02-05 05:46:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c07edbd-06df-3930-a849-08306450dd38 | 3.58941 | -61.42747 | 2025-02-05 05:46:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 63ce34bd-3ce1-3d5c-8ad4-63eba8133fe5 | 2.01003 | -61.37997 | 2025-02-05 05:46:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 55952c06-3346-37d6-b8cb-2f9cf4cd60c3 | -8.99718 | -63.81232 | 2025-02-05 05:50:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 76655767-f25c-32e4-9c74-f9fb5f7fc9e6 | -11.9672 | -63.67704 | 2025-02-05 05:50:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b0494966-ef79-30b0-8bc6-984efcc13554 | -12.40496 | -63.98607 | 2025-02-05 05:50:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5e04d149-4074-3b62-b59d-7156c18fdfb9 | -12.14794 | -63.80553 | 2025-02-05 05:50:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa01bce5-e763-367d-a52d-2fe73e5b8f7c | -9.13342 | -67.1085 | 2025-02-05 05:50:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README5.md)
