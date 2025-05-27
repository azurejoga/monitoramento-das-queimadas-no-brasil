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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cb58c614-ff02-3aa7-8ad7-d03dc5dc2215 | -7.1837 | -43.1189 | 2025-05-27 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 74.6 |
| 20aad7a0-c195-3e51-a565-a2840d34a1d6 | -7.2028 | -43.0936 | 2025-05-27 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 59.8 |
| 5190dc21-4f57-398b-a466-2e1d7aa3f0dd | -13.1498 | -56.8054 | 2025-05-27 00:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 3ffdc295-fa58-3618-ae23-faf887f4ffc2 | -7.2214 | -43.1153 | 2025-05-27 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 193.7 |
| 2251c2de-0a83-32ae-9fe6-85609e818a4d | -21.2774 | -48.6091 | 2025-05-27 00:00:00 | GOES-19 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 81.8 |
| ca938110-4731-3374-b3dc-e25286cb39e8 | -7.2025 | -43.1171 | 2025-05-27 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 233.6 |
| e0d62670-1f85-341e-8fe3-e803cec8daf6 | -7.2028 | -43.0936 | 2025-05-27 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 84.4 |
| 764f2d31-ad5a-3ca4-aa63-2738743f35d6 | -7.2403 | -43.1134 | 2025-05-27 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 72.8 |
| bcb59104-fbe3-3742-9c91-6872b91911ab | -10.8213 | -56.9604 | 2025-05-27 00:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 52.0 |
| e3e081ba-46c9-3a2d-af52-02a7bbf9a4e8 | -7.2025 | -43.1171 | 2025-05-27 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 291.0 |
| dfc705e5-6ed5-3430-9702-080f119dfde7 | -7.2214 | -43.1153 | 2025-05-27 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 130.3 |
| 5a131096-5425-37b6-bfd5-52a9c68f4942 | -13.1498 | -56.8054 | 2025-05-27 00:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 96.0 |
| e1c2429e-6e75-3317-8d23-92d2dd8bd7bf | -7.2025 | -43.1171 | 2025-05-27 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 87.6 |
| cc5b361d-9e74-36d8-8e66-6bfc02a31126 | -13.1498 | -56.8054 | 2025-05-27 00:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 750ea416-6466-3144-ab41-aff890ed8d2c | -7.2214 | -43.1153 | 2025-05-27 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 57.7 |
| 43722b1d-8543-360f-9c97-18adb6b94450 | -7.1837 | -43.1189 | 2025-05-27 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 79.8 |
| d155f8d8-8548-311d-a466-18c72421c1f2 | -7.2025 | -43.1171 | 2025-05-27 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 213.2 |
| 30044a8e-e76d-3ed8-8af4-413758e15d66 | -7.2028 | -43.0936 | 2025-05-27 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 88.9 |
| 6fbf6b18-e3ca-3902-ad72-063dbf43bca3 | -13.1498 | -56.8054 | 2025-05-27 00:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| d0ea7675-4b97-3815-a4f9-0442b73e1a0d | -7.184 | -43.0954 | 2025-05-27 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 38.8 |
| d30217ed-2583-3f87-85ec-08722a8615f9 | -7.2023 | -43.1406 | 2025-05-27 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 56.6 |
| 70fe60c2-9bea-3a31-b3a4-03d6a93d2248 | -7.2214 | -43.1153 | 2025-05-27 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 122.1 |
| 42512577-6877-398b-aa9d-4b7794e596a0 | -7.2214 | -43.1153 | 2025-05-27 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 103.6 |
| ad800d99-8465-37ea-bfd8-033e3dfca7e4 | -13.1498 | -56.8054 | 2025-05-27 00:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 73.8 |
| ba624ae0-b062-3d5e-8dd2-8b6b6c5c8085 | -7.2025 | -43.1171 | 2025-05-27 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 99.2 |
| 81c5e1b5-0058-3275-8b41-d3ee875a7821 | -7.1837 | -43.1189 | 2025-05-27 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 75.8 |
| c1f887e5-1083-3427-9a8f-8a500c97f642 | -13.1498 | -56.8054 | 2025-05-27 00:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 810280b6-6cc8-317b-ada5-8b10f11b84e9 | -18.8484 | -53.6035 | 2025-05-27 00:50:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 45.3 |
| 651f9cdb-1730-3c40-abbe-485562e0eb51 | -7.2214 | -43.1153 | 2025-05-27 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 115.6 |
| 264a4d2a-7f9f-32a2-85f5-3be62893843a | -7.2025 | -43.1171 | 2025-05-27 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 195.9 |
| 4b039b91-f73c-3b45-ad0c-aa920cf3849d | -7.2028 | -43.0936 | 2025-05-27 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 91.5 |
| 79e023c9-5ee6-362f-961b-6136fefdadc4 | -7.1837 | -43.1189 | 2025-05-27 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 62.6 |
| 5ada9d64-14a4-3dbe-bf5d-6c12de14a4a0 | -7.2214 | -43.1153 | 2025-05-27 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 102.5 |
| 0e46a742-1147-39b0-b0f7-61bf92a8be94 | -13.1498 | -56.8054 | 2025-05-27 01:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 5e13f569-e88a-3126-9032-369160f4c7f5 | -7.2028 | -43.0936 | 2025-05-27 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 80.5 |
| a630ab00-679d-3dfd-8865-43bb80acd7c0 | -7.2025 | -43.1171 | 2025-05-27 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 213.3 |
| 7aa8950c-72b9-373a-b645-ee77840370f8 | -7.2025 | -43.1171 | 2025-05-27 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 154.6 |
| 274a5576-4814-3a27-9b37-814b95a4c146 | -7.2214 | -43.1153 | 2025-05-27 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 78.4 |
| f689b34b-93b8-39e6-831a-ff91b51d50d9 | -19.4239 | -54.774 | 2025-05-27 01:10:00 | GOES-19 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 3f9da080-8efa-3864-8e06-a5a64d47b274 | -19.444 | -54.7708 | 2025-05-27 01:10:00 | GOES-19 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 69.8 |
| aece8918-58eb-3130-85d2-f7ce0a6fae7b | -13.1498 | -56.8054 | 2025-05-27 01:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 5c31dc2a-a077-3e96-8259-9c5a4b7d4058 | -18.8484 | -53.6035 | 2025-05-27 01:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 2ac90993-3e81-3bc3-93c5-7ee7dc248e9f | -23.10498 | -49.26637 | 2025-05-27 01:11:00 | TERRA_M-M | MANDURI | SÃO PAULO | Brasil | 3528601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.7 |
| feb629f1-1d4c-3a09-8b2e-f218e27fb01a | -21.2668 | -48.60481 | 2025-05-27 01:13:00 | TERRA_M-M | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |
| d63d4037-47ad-3ea9-a191-f4541ab36e4f | -16.32355 | -53.80259 | 2025-05-27 01:13:00 | TERRA_M-M | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| ad0bcd4a-5a3d-3810-98ac-b9444304002f | -18.85291 | -53.62342 | 2025-05-27 01:13:00 | TERRA_M-M | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 20.4 |
| e283b920-5bee-37fc-b6bd-8e006f30fc8f | -18.8321 | -53.60706 | 2025-05-27 01:13:00 | TERRA_M-M | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 6e9a97f5-c5e4-3505-917c-b9b604713391 | -21.26983 | -48.62217 | 2025-05-27 01:13:00 | TERRA_M-M | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 23.8 |
| e3d9aacc-b0d1-3ee5-acdf-29a0c6017881 | -18.84251 | -53.61525 | 2025-05-27 01:13:00 | TERRA_M-M | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 28.9 |
| ab99cf08-4f33-3f1b-ab9b-a4e1791bd3b9 | -18.85151 | -53.61382 | 2025-05-27 01:13:00 | TERRA_M-M | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 6.8 |
| b9df0556-f0bf-3142-a98b-f6beedebd47d | -17.53192 | -52.12532 | 2025-05-27 01:13:00 | TERRA_M-M | PEROLÂNDIA | GOIÁS | Brasil | 5216452 | 52 | 33 | nan | nan | nan | Cerrado | 14.7 |
| ac290fa6-4554-3b15-bdd6-002eb817742d | -18.40914 | -55.58064 | 2025-05-27 01:13:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.7 |
| fa230148-f367-33fe-a81e-02ea6bba198c | -18.8411 | -53.6056 | 2025-05-27 01:13:00 | TERRA_M-M | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 7fcf6d11-29af-3e76-8191-4f2fc3c8a60e | -18.8397 | -53.59595 | 2025-05-27 01:13:00 | TERRA_M-M | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 91bd8932-3061-38fb-8df1-29adef2c6d9d | -18.84391 | -53.62489 | 2025-05-27 01:13:00 | TERRA_M-M | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 40ea89d2-1e5f-3a0f-888a-084ddefbd43c | -14.01764 | -55.14112 | 2025-05-27 01:15:00 | TERRA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| c8facde1-a226-3d19-a37d-b2dadd4b453a | -14.04602 | -55.14021 | 2025-05-27 01:15:00 | TERRA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| e5eaf8ff-83c2-3259-b87b-90a00e465b06 | -11.40489 | -52.95909 | 2025-05-27 01:15:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 7b83cc2b-d1a8-3f46-94c0-221463a65500 | -12.11372 | -54.66384 | 2025-05-27 01:15:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 34b982aa-95ae-3781-a3be-bf65b6e085cc | -11.62737 | -54.93245 | 2025-05-27 01:15:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7a445aef-bf7d-3060-85c5-e1c055a75dcf | -13.14481 | -56.81576 | 2025-05-27 01:15:00 | TERRA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 25fce2c0-147b-30a0-a85a-57ce023aaac8 | -11.5661 | -47.4494 | 2025-05-27 01:15:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 48.4 |
| d4715598-9c91-3ec9-856c-d35fc2959283 | -11.81551 | -55.08544 | 2025-05-27 01:15:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7cdc5965-2317-3de9-858f-dda5976edfd9 | -14.03581 | -55.1324 | 2025-05-27 01:15:00 | TERRA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 7c9e76d7-75b7-38d1-9d83-f374ce641940 | -13.15326 | -56.79945 | 2025-05-27 01:15:00 | TERRA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 0f4b3d1f-6ebb-3fcc-b2fa-59c5c0269950 | -13.1545 | -56.80854 | 2025-05-27 01:15:00 | TERRA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 0f135305-15a9-382c-8dc4-92821e65a4ca | -11.82454 | -55.08409 | 2025-05-27 01:15:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1ecd0ce5-0f74-3eaa-ba95-929e4d148ede | -12.03168 | -51.59306 | 2025-05-27 01:15:00 | TERRA_M-M | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 0052a6b9-9790-35cc-bff4-6d0b3781943f | -11.40302 | -52.94697 | 2025-05-27 01:15:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| c1b75805-66cc-30a6-aea2-f1b015140b4d | -14.0447 | -55.13101 | 2025-05-27 01:15:00 | TERRA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 87706b70-46c1-375b-aceb-f0c3d8055573 | -14.70155 | -56.14374 | 2025-05-27 01:15:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8aedf60e-7e9b-31bd-8af0-2885b6740e7f | -14.02824 | -55.14298 | 2025-05-27 01:15:00 | TERRA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 36256b94-7313-3507-80b5-0b122136ae49 | -11.87115 | -52.25888 | 2025-05-27 01:15:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 9298067f-d6a5-331d-a8f9-cd3e7b5021f0 | -13.14356 | -56.80667 | 2025-05-27 01:15:00 | TERRA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 77f26026-31d3-36eb-b0e9-1b763898ab38 | -14.02692 | -55.13375 | 2025-05-27 01:15:00 | TERRA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 019e2c81-5fb4-396a-b073-d20218b55f7b | -11.81414 | -55.07602 | 2025-05-27 01:15:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 15.0 |
| bf2268e7-63c6-345d-b980-1664f821eee6 | -12.03405 | -51.60792 | 2025-05-27 01:15:00 | TERRA_M-M | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 13fb0f46-a6c7-3dcf-9cfd-0e6ed79deeea | -12.82516 | -47.38482 | 2025-05-27 01:15:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 52381d4e-c102-3557-801a-1e0cee8aeaf5 | -13.15573 | -56.81763 | 2025-05-27 01:15:00 | TERRA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| ff87b9e0-4adf-39f5-9c1c-dfc3bb8b39a0 | -12.08892 | -57.37669 | 2025-05-27 01:15:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 2ff06c90-2182-3a84-afab-3d31b25e8752 | -14.01503 | -55.12265 | 2025-05-27 01:15:00 | TERRA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| c6b40ae5-fa66-3e32-9fd6-b51a99e0feb3 | -12.65903 | -52.44125 | 2025-05-27 01:15:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 975e5d9b-12bc-3821-a1b7-4d52524c5a4c | -11.82317 | -55.07466 | 2025-05-27 01:15:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 496fda44-8af9-3c81-a904-cd6bd4f59136 | -14.01634 | -55.13189 | 2025-05-27 01:15:00 | TERRA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 60522ded-1def-37fa-a565-85bf92ef8667 | -12.1243 | -54.67215 | 2025-05-27 01:15:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 8676a8f3-231b-354d-a0fd-b6454c2c7af4 | -11.62875 | -54.942 | 2025-05-27 01:15:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 16.3 |
| e17bb7fe-ca73-35ed-810d-02902ff6767b | -8.7547 | -49.7419 | 2025-05-27 01:17:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 28.4 |
| aee5ee1e-348b-3e08-a995-de0051ee0d2e | -8.42741 | -46.65268 | 2025-05-27 01:17:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 504bdf2f-aa79-3a8b-a7b3-b36808ee6184 | -7.91593 | -63.59032 | 2025-05-27 01:17:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 33.9 |
| d8b6d250-7bca-3784-bf47-a5a99eb91d32 | -8.75861 | -49.76542 | 2025-05-27 01:17:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 97260268-f786-3fcd-81f0-fb4665fed1b5 | -8.74874 | -49.74872 | 2025-05-27 01:17:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 7ddf5aa2-0f64-362c-ba3f-af767d61cc64 | -10.8152 | -54.02695 | 2025-05-27 01:17:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| fab16812-f8e9-3d8a-9a77-7a8cceac8f67 | -8.31423 | -55.11515 | 2025-05-27 01:17:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| dcd070e9-0425-3b99-9a80-b61e51147bcb | -11.1404 | -53.93001 | 2025-05-27 01:17:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 742e5313-768f-3bc9-a0ec-18a6e56b2b62 | -10.29735 | -57.14067 | 2025-05-27 01:17:00 | TERRA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| bfb771ea-09a6-3e1e-8eaa-ef8f3cce031f | -10.83348 | -56.9539 | 2025-05-27 01:17:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 9f579f63-e6f6-3ad6-a3b0-c42338c3010c | -10.82942 | -54.02934 | 2025-05-27 01:17:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 1a1e3a32-0564-3174-b30b-e81821fc143b | -9.15004 | -49.65135 | 2025-05-27 01:17:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 1031ffc0-cf88-3d6e-b02e-619b1d52fb8b | -10.81984 | -54.0308 | 2025-05-27 01:17:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 10c1c144-d338-3f09-be18-8ecc6a9dc7d9 | -10.33649 | -57.49194 | 2025-05-27 01:17:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |


[Clique aqui para ver as próximas entradas](README2.md)
