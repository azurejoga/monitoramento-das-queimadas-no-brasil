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
| f85ee2e3-2748-3edb-acb8-aaadfbec2f2b | 1.1075 | -60.513699 | 2026-08-01 00:56:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 2c644ba4-0de4-3989-95b8-61d71e81a8c3 | -7.2947 | -55.312302 | 2026-08-01 00:56:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a78f2e71-3905-3fcd-9f3b-db0cb84cec94 | -14.0766 | -46.264801 | 2026-08-01 00:56:00 | METOP-C | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9a87d029-051d-3299-8fc1-321f9d4f53f2 | -8.1659 | -55.442299 | 2026-08-01 00:56:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bdec619e-2bf3-30e6-b5e0-0c38e65fc7e8 | -6.7596 | -41.004601 | 2026-08-01 00:56:00 | METOP-C | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a0cf0da6-c82b-3945-a0b5-559930be4e31 | -4.3711 | -47.761002 | 2026-08-01 00:56:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f220f5e6-5470-323f-9f8a-05b558602b98 | -11.4284 | -50.6075 | 2026-08-01 01:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 65532c95-17d2-3e72-a2de-7c0c642487a8 | -11.2404 | -54.833 | 2026-08-01 01:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| b5f0685f-cade-3223-a080-fe4476e1b41f | -1.6591 | -54.4543 | 2026-08-01 01:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| b4124567-d612-3097-a47a-309dc10a4afb | -14.073 | -46.2669 | 2026-08-01 01:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 62.8 |
| dbb19aaa-3a94-3d29-826d-b71162b2484d | -14.0735 | -46.2439 | 2026-08-01 01:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 2788e9d4-eb55-3ba0-bc1a-e6979cdf8259 | -2.8932 | -48.0171 | 2026-08-01 01:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 2437e165-38b2-3b61-8e5e-f534448153f5 | -11.2588 | -54.8721 | 2026-08-01 01:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 131.3 |
| cf6334d7-d00c-300b-aab4-9e461bd43cf3 | -11.2402 | -54.8534 | 2026-08-01 01:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 404.2 |
| 19736c5f-6074-338f-a53e-d06d2468ed11 | -11.2399 | -54.8737 | 2026-08-01 01:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 353.8 |
| 63cd7dd5-2dc5-352d-b98c-a77699d9e7b9 | -6.5699 | -55.156 | 2026-08-01 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 09efa1fe-5a5e-3c5d-9a9b-305e684974e3 | -11.2591 | -54.8517 | 2026-08-01 01:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 150.4 |
| a6a492aa-c996-39b0-a0a8-5888ffeac25e | -6.7555 | -41.0103 | 2026-08-01 01:00:00 | GOES-19 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 87.2 |
| 2db4c910-d7cc-3331-8683-a70f85972130 | -14.0929 | -46.2407 | 2026-08-01 01:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 55.1 |
| e7d65096-8b89-3d88-968d-f3e617ae1688 | -9.4765 | -40.3613 | 2026-08-01 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 58.7 |
| 9fb80cd9-2b65-387c-9ee0-85eb1a83a5ca | -11.2402 | -54.8534 | 2026-08-01 01:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 246.3 |
| 444dbba5-55eb-3d53-9849-dc98c8a34d9a | -1.6591 | -54.4543 | 2026-08-01 01:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| e212909d-2ec1-31a5-adcc-7bb4bf009c17 | -11.2591 | -54.8517 | 2026-08-01 01:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 221.4 |
| ac28b0df-eb55-3af3-9713-8e88cd11a0f5 | -11.2399 | -54.8737 | 2026-08-01 01:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 218.5 |
| 1dfdc9b2-41c4-3d1b-bd56-5b34407772a6 | -11.2588 | -54.8721 | 2026-08-01 01:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 198.9 |
| 6491211f-541e-3c27-aafc-d5c1f150772d | -14.0735 | -46.2439 | 2026-08-01 01:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 60df3d49-4280-323a-8648-199f9464d586 | -14.073 | -46.2669 | 2026-08-01 01:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 7890af9e-0598-3b79-a437-36e6d20c9f52 | -11.4284 | -50.6075 | 2026-08-01 01:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 6da32f2c-34b9-3c6d-9828-7cf910c609cf | -11.25 | -54.85 | 2026-08-01 01:15:00 | MSG-03 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c00409e8-d603-38d5-a726-d08c60114132 | -11.25 | -54.91 | 2026-08-01 01:15:00 | MSG-03 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2e136195-4d2f-34cc-bca7-fe4c69c66b5f | -11.2402 | -54.8534 | 2026-08-01 01:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 218.7 |
| 4bc1a23d-c52d-33a1-aa15-77530a05bc0c | -11.2588 | -54.8721 | 2026-08-01 01:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 130.3 |
| c2385c15-67e3-35e9-a80b-ebdb660f66ac | -14.073 | -46.2669 | 2026-08-01 01:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 1908ae13-0c3a-3525-b675-841bfdba79d6 | -11.2399 | -54.8737 | 2026-08-01 01:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 191.1 |
| fbbd63a6-2632-393d-9bb8-26cb565db5c3 | -14.0735 | -46.2439 | 2026-08-01 01:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 0ba7f0d8-c666-3c69-aae9-67e8d0c2e904 | -11.2591 | -54.8517 | 2026-08-01 01:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 148.1 |
| 7b263e7f-0ff0-35ff-a5d1-2f39bab94d8a | -1.6591 | -54.4543 | 2026-08-01 01:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 757d6df6-b937-3f5c-b1cb-5b48de8e64f3 | -9.4765 | -40.3613 | 2026-08-01 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 46.7 |
| 7cd19e34-8d7d-3773-9a28-c79b2ee3e400 | -11.2588 | -54.8721 | 2026-08-01 01:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 121.1 |
| b4786341-1365-359f-a7ee-31e2dcd9641e | -11.2591 | -54.8517 | 2026-08-01 01:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 137.8 |
| a657ed8b-791b-33d1-873f-8af924e92f0c | -11.2402 | -54.8534 | 2026-08-01 01:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 175.6 |
| 00a4c25f-0e5d-38f2-a1bf-2989d18a4ab5 | -14.073 | -46.2669 | 2026-08-01 01:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 88460f8e-35ac-3356-9964-8a733fb27ed1 | -11.2399 | -54.8737 | 2026-08-01 01:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 154.5 |
| ef561efc-bf63-3e3a-9afc-91781eb0780e | -14.0735 | -46.2439 | 2026-08-01 01:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 73.7 |
| fff40a06-4861-330e-b363-e98691268d23 | -18.5346 | -47.3935 | 2026-08-01 01:40:00 | GOES-19 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 2df53400-3d89-3469-bbb8-6b8f5968a330 | -14.0925 | -46.2637 | 2026-08-01 01:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 139.2 |
| ba468dc4-62e0-344f-a10b-5b0aba6ddbdd | -14.0929 | -46.2407 | 2026-08-01 01:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 10789eb7-f1be-3cc9-85de-cb4777dc382e | -11.2399 | -54.8737 | 2026-08-01 01:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 1ded9176-6955-3e3f-8c62-2bfcf5b3f7eb | -2.8932 | -48.0171 | 2026-08-01 01:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 33.0 |
| 9b8a0295-4ea2-3cc7-a631-4127c0d678da | -11.2591 | -54.8517 | 2026-08-01 01:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 146.3 |
| cd0a5d55-6891-3954-abcf-677aa4e3c69d | -14.073 | -46.2669 | 2026-08-01 01:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 370.5 |
| 1fb8c340-6df3-3370-8747-cbba78982686 | -14.0735 | -46.2439 | 2026-08-01 01:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 099ea340-ca43-3220-aa9c-cc27a08b6bb4 | -14.0725 | -46.2899 | 2026-08-01 01:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 85.8 |
| dc3d1d40-1bc1-35a9-8703-00d4cb25c1f1 | -11.2402 | -54.8534 | 2026-08-01 01:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 143.3 |
| 54f3f048-2ed9-3b3e-9149-e16aa62d3b59 | -18.5352 | -47.3703 | 2026-08-01 01:40:00 | GOES-19 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 152d99d0-d3f8-3aae-bca6-708e4153a5a5 | -11.2588 | -54.8721 | 2026-08-01 01:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 107.6 |
| f66af81e-4607-3a72-bc58-c2a8b36fb0f2 | -11.2402 | -54.8534 | 2026-08-01 01:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 289.0 |
| 4357f32e-dded-344e-8a6c-f2b788be60dc | -14.0925 | -46.2637 | 2026-08-01 01:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 206.7 |
| e31413c6-75f4-3ab4-929c-ef097cb3b2c9 | -11.2588 | -54.8721 | 2026-08-01 01:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 103.7 |
| aed3e108-fb1f-32bd-bdd8-b695b13c5196 | -11.2399 | -54.8737 | 2026-08-01 01:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 188.6 |
| 45ff5f38-bc59-351a-94fe-1c4f11be4570 | -14.073 | -46.2669 | 2026-08-01 01:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 201.8 |
| d00a3b3d-5cbc-31fd-b6c3-5c8952ba9cdb | -11.2404 | -54.833 | 2026-08-01 01:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 58be9cdf-d6bb-34e3-8c59-b1898b165f1d | -14.092 | -46.2866 | 2026-08-01 01:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 3269e49c-c966-3e95-861e-2fe899b34f93 | -14.0929 | -46.2407 | 2026-08-01 01:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 74.5 |
| e7392d3f-2020-377b-a806-2e4449f9f19e | -14.0735 | -46.2439 | 2026-08-01 01:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 74.3 |
| b95ba12a-02f6-387f-91fa-80d6c9ddd846 | -14.0725 | -46.2899 | 2026-08-01 01:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 4613e8f2-2dab-3413-b804-5bb5c118e678 | -6.5699 | -55.156 | 2026-08-01 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| b5206274-0abe-3787-b51a-58c74ee62f21 | -11.2591 | -54.8517 | 2026-08-01 01:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 155.8 |
| 2349a420-7407-3755-8c16-8887ef117fab | -14.0725 | -46.2899 | 2026-08-01 02:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 320.3 |
| 60016aaa-6f75-3132-ae1a-e32cabefacd7 | -11.2402 | -54.8534 | 2026-08-01 02:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 278.4 |
| 1d220611-5127-3774-9ce5-e86ba0339415 | -14.092 | -46.2866 | 2026-08-01 02:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 227.8 |
| a33b4917-d260-3493-b0d4-dbf04c3203b1 | -11.2404 | -54.833 | 2026-08-01 02:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 73a386a0-840b-3e4a-9a89-165807105560 | -11.2399 | -54.8737 | 2026-08-01 02:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 143.0 |
| ce990408-428b-3e4d-8e82-051234eee25a | -20.528 | -51.4475 | 2026-08-01 02:00:00 | GOES-19 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 64.1 |
| d25e25af-b76a-3ca0-939a-5b86dfa02bcf | -14.0929 | -46.2407 | 2026-08-01 02:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 4d8d5c2c-b23a-380e-9780-4329748186af | -11.2588 | -54.8721 | 2026-08-01 02:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 183.9 |
| 33f0235d-9dff-3130-a33a-7f45fec5912f | -14.073 | -46.2669 | 2026-08-01 02:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 310.6 |
| f286a69e-db1a-3159-ad32-0f1a58496de9 | -11.2593 | -54.8313 | 2026-08-01 02:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 55.9 |
| b24e8974-3d04-3048-bf8d-a9b67a9c8aba | -20.5286 | -51.4252 | 2026-08-01 02:00:00 | GOES-19 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 84.4 |
| 8424a6d7-37df-3deb-a9e8-38a8d0123981 | -14.0925 | -46.2637 | 2026-08-01 02:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 213.3 |
| bffc5cac-b117-3031-b210-672836f28f29 | -11.2591 | -54.8517 | 2026-08-01 02:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 415.6 |
| 65d29152-d3bd-3b09-8fb6-4e6cd492f1bb | -14.0735 | -46.2439 | 2026-08-01 02:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 3bcb814d-072c-3ce8-b7a3-48be0c3027cb | -14.073 | -46.2669 | 2026-08-01 02:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 143.7 |
| 62227238-f51d-3b27-a197-a97b84209d0b | -14.092 | -46.2866 | 2026-08-01 02:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 125.6 |
| c0aa266c-1a5f-3bb1-9c27-e5362c8bd3ae | -11.2402 | -54.8534 | 2026-08-01 02:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 460.0 |
| 11be9116-4142-34f4-b768-1d806826f6c7 | -11.2593 | -54.8313 | 2026-08-01 02:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 06a2f63f-8065-340c-a694-5b4ebbf029fa | -14.0929 | -46.2407 | 2026-08-01 02:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 1119ab6f-6201-3128-b9bb-0d3c4c709239 | -14.0725 | -46.2899 | 2026-08-01 02:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 9e12e960-71c5-3e71-bde0-2e7b39835919 | -14.0735 | -46.2439 | 2026-08-01 02:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 75.0 |
| b8713b29-2c12-330f-a0b5-4657cc0490bf | -14.0925 | -46.2637 | 2026-08-01 02:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 130.9 |
| 80613483-4a3a-3ee2-a7b2-08e9da447511 | -11.2404 | -54.833 | 2026-08-01 02:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 26dace90-e56a-3a4b-a39e-467a13d39699 | -11.2588 | -54.8721 | 2026-08-01 02:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 127.8 |
| eac47143-b79d-3c07-98f6-c8d67caf9566 | -11.2399 | -54.8737 | 2026-08-01 02:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 218.7 |
| 8f569e63-4a56-358c-bafd-434cc9840628 | -11.2591 | -54.8517 | 2026-08-01 02:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 273.0 |
| ad2ca2e3-74a7-3cdc-86a9-79f69abf75c4 | -14.08 | -46.26 | 2026-08-01 02:15:00 | MSG-03 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 86af5037-9a08-3dd2-8ec1-0b047e8f4222 | -14.06 | -46.3 | 2026-08-01 02:15:00 | MSG-03 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2d482bc0-3526-38d0-8b6c-2e861bc2c317 | -11.25 | -54.85 | 2026-08-01 02:15:00 | MSG-03 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b383c631-c5db-3704-840e-14ba9f0b59e4 | -14.09 | -46.31 | 2026-08-01 02:15:00 | MSG-03 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4847c7c0-25c7-3028-ade3-06631e1dc23b | -14.0929 | -46.2407 | 2026-08-01 02:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 0d31fbae-53af-3c25-b040-9786ebb75676 | -14.0735 | -46.2439 | 2026-08-01 02:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 78.7 |


[Clique aqui para ver as próximas entradas](README5.md)
