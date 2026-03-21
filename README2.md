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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 52738db1-f09d-3361-9af2-f2436a921f30 | -21.81821 | -48.70303 | 2026-03-21 04:19:00 | NOAA-21 | TABATINGA | SÃO PAULO | Brasil | 3552700 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 27a145ec-d1dd-321e-b56e-707b7335412c | -23.40781 | -46.4206 | 2026-03-21 04:19:00 | NOAA-21 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 896e904c-ab0d-3b94-99dc-d1169a71a48e | -23.59638 | -46.43015 | 2026-03-21 04:19:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5dfcf79a-b0ea-3076-9c4a-1162fb2e8f22 | -21.82161 | -48.70372 | 2026-03-21 04:19:00 | NOAA-21 | TABATINGA | SÃO PAULO | Brasil | 3552700 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a804985-780d-3a8c-b49d-681ca0a82cbd | -23.45344 | -46.69988 | 2026-03-21 04:19:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 93c48a57-74b1-38a5-a325-941ddd9fa511 | -23.04204 | -47.85987 | 2026-03-21 04:19:00 | NOAA-21 | LARANJAL PAULISTA | SÃO PAULO | Brasil | 3526407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ba749cea-65b3-3863-abdb-54673758a57c | -27.72621 | -49.90584 | 2026-03-21 04:19:00 | NOAA-21 | BOCAINA DO SUL | SANTA CATARINA | Brasil | 4202438 | 42 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| ea3d5931-8f82-38c8-aa95-6f6d5a25177b | -15.28337 | -43.0624 | 2026-03-21 04:19:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 0.5 |
| b714007c-a2da-3d58-8631-1b80c4d997ed | -20.63112 | -51.69676 | 2026-03-21 04:19:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1fb26597-303e-3f8f-9094-fe53eed89e8f | -23.57767 | -46.50846 | 2026-03-21 04:19:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 1ae877f1-a542-34a1-97e8-f9feaf095c93 | -23.46969 | -48.90452 | 2026-03-21 04:19:00 | NOAA-21 | PARANAPANEMA | SÃO PAULO | Brasil | 3535804 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 32f43b5d-93bf-3fc2-a111-0e6cb65f9968 | -23.59305 | -46.42957 | 2026-03-21 04:19:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| c7921f9a-7736-30b2-9b50-ee562bec98dd | -15.28681 | -43.06293 | 2026-03-21 04:19:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 310f2106-174d-33ce-8937-deb61cd5a3dd | -20.62646 | -51.69953 | 2026-03-21 04:19:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| afeb96e3-3bb5-33bd-9753-1b428d061ff9 | -15.28737 | -43.05906 | 2026-03-21 04:19:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 2.7 |
| aa2f0320-5900-35b1-9171-ee88f532145d | -21.82093 | -48.70767 | 2026-03-21 04:19:00 | NOAA-21 | TABATINGA | SÃO PAULO | Brasil | 3552700 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 368fe09c-b2c5-3226-9d23-0be7cc292a72 | -23.39314 | -51.12927 | 2026-03-21 04:19:00 | NOAA-21 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 64ad3049-be2d-3cff-bf79-249379ce3e1e | -31.14474 | -53.62423 | 2026-03-21 04:21:00 | NOAA-21 | BAGÉ | RIO GRANDE DO SUL | Brasil | 4301602 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 4b91f16e-20fe-3b25-a797-86f7fecee291 | 2.1226 | -61.22302 | 2026-03-21 04:44:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 289b75e8-520d-3ff6-aad4-8ec37e987e5e | 3.23579 | -60.13131 | 2026-03-21 04:44:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ba3c1aa3-f2cc-3fa7-8dbe-99c6f87831d0 | 3.23542 | -60.12558 | 2026-03-21 04:44:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e9afd047-bb18-3ad0-9422-3002deed0887 | 3.56369 | -60.16322 | 2026-03-21 04:44:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ccea52a7-1516-3976-a42d-808b1fe8b6f5 | 3.23628 | -60.13158 | 2026-03-21 04:44:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9da3b3c2-d611-3e3f-9738-09b7423589e4 | -6.44547 | -40.9811 | 2026-03-21 04:46:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e65b2889-5a40-3553-b437-8fbf9a8d1947 | -6.44504 | -40.9841 | 2026-03-21 04:46:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0733fb9a-965c-3764-a644-0d39df6b3b1e | -8.43314 | -44.04184 | 2026-03-21 04:46:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e8c1e245-639c-3eed-a69c-52d7860b0936 | -8.4337 | -44.03783 | 2026-03-21 04:46:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f425ee90-4d2b-3eff-9260-32092b00840e | -8.43257 | -44.04585 | 2026-03-21 04:46:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3a24aadd-0096-332c-a0e0-38c38556c614 | -8.42944 | -44.03722 | 2026-03-21 04:46:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ec09583-6238-34ee-847d-28b10c6c86ba | -8.42887 | -44.04124 | 2026-03-21 04:46:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ab79693f-d9be-3b04-8742-da5c5bd2007f | -23.39112 | -51.12716 | 2026-03-21 04:49:00 | NPP-375D | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ec2df0a3-6e9a-3bc6-bfdc-3f3d385a6a6b | -14.11894 | -43.42285 | 2026-03-21 04:49:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1f3049e2-a07b-31d5-96bc-d4b3d26b5802 | -14.12444 | -43.41815 | 2026-03-21 04:49:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 00de4a85-0673-3c15-b11f-f56752d7bc83 | -15.28472 | -43.06656 | 2026-03-21 04:49:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 0ad3d14b-a5b7-39b8-ab9b-277dfc6f06fc | -14.11962 | -43.41747 | 2026-03-21 04:49:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ae703b7c-8494-3221-aeb2-3bbad274d570 | -23.46641 | -48.90484 | 2026-03-21 04:49:00 | NPP-375D | PARANAPANEMA | SÃO PAULO | Brasil | 3535804 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c3f4d40d-f326-31d6-ab9f-1fb51197e638 | -23.59454 | -46.43002 | 2026-03-21 04:49:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| e1249b95-dfa3-3e8e-bbf2-2f01f0e1b0df | -15.28546 | -43.06065 | 2026-03-21 04:49:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 587d5584-be33-3e80-825f-e3cc4cd4719b | -23.47026 | -48.90546 | 2026-03-21 04:49:00 | NPP-375D | PARANAPANEMA | SÃO PAULO | Brasil | 3535804 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c9081dd1-71e5-36dd-b993-0f1e37635849 | -25.13806 | -50.8573 | 2026-03-21 04:49:00 | NPP-375D | GUAMIRANGA | PARANÁ | Brasil | 4108957 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ba96c1d5-cf9d-3885-9a3b-542bcb34e415 | -14.12927 | -43.41883 | 2026-03-21 04:49:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 42bf987c-bda8-39bd-bacd-1b8bec808aaa | -15.28347 | -43.06675 | 2026-03-21 04:49:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 07c1d86e-ac61-3129-88b6-f715c0d9ee97 | -21.3852 | -55.86156 | 2026-03-21 04:49:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d73fbbac-0855-36d1-a497-4c340fe592fe | -21.38321 | -55.86354 | 2026-03-21 04:49:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2c88900a-d558-3da2-a363-b1890e6477d1 | -21.82185 | -48.70835 | 2026-03-21 04:49:00 | NPP-375D | TABATINGA | SÃO PAULO | Brasil | 3552700 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 094dcc22-113d-36bb-9b85-678ed0275627 | -14.12376 | -43.42353 | 2026-03-21 04:49:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 20f483e4-9ada-3626-99dd-fc6788cf3b51 | -21.81802 | -48.70785 | 2026-03-21 04:49:00 | NPP-375D | TABATINGA | SÃO PAULO | Brasil | 3552700 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7b83e4e9-575a-31f7-b5ac-5591473d148e | -15.28417 | -43.06083 | 2026-03-21 04:49:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 04f0f631-4d83-34df-add5-f346080f41d5 | -28.91481 | -55.96341 | 2026-03-21 04:51:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 84c16b42-f93d-3489-989e-2f4da3bcc059 | 2.59845 | -61.30203 | 2026-03-21 05:04:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fc57bbde-fe37-3b16-8494-3a7b695d926b | 2.5937 | -61.30274 | 2026-03-21 05:04:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c336217-395b-3262-878c-9c555404facc | 2.12451 | -61.21994 | 2026-03-21 05:04:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 15ee080c-6021-34e7-a956-27d0bf53b017 | 2.11983 | -61.2207 | 2026-03-21 05:04:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c3c422c7-6acb-3059-99b0-0c88464d1654 | 3.36231 | -60.17567 | 2026-03-21 05:04:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad40f614-e938-329e-b54b-06eff88cb38b | 2.24968 | -60.2878 | 2026-03-21 05:04:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 007e01ae-887f-3b0b-a729-c6ccd974bb93 | 1.99447 | -60.55952 | 2026-03-21 05:04:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ca9c58bb-6002-38c7-b3bb-3cdc92040ef1 | 3.33762 | -60.19285 | 2026-03-21 05:04:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8a03eed1-5fe5-3300-9c7e-e975a7b90d9b | 3.2385 | -60.34218 | 2026-03-21 05:04:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 92fe9ada-b06d-3925-967a-b7f95d5750b4 | 1.91977 | -60.56847 | 2026-03-21 05:04:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 297e5644-d364-3465-9dae-f583b5f4dcbc | 3.33317 | -60.19352 | 2026-03-21 05:04:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e803314f-01a4-3d70-8dc3-de18d0944a74 | 2.05369 | -61.81397 | 2026-03-21 05:04:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 57d1899f-4bde-31f9-bb7e-dc13cd7e74f5 | 2.78485 | -60.31707 | 2026-03-21 05:04:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d520d2d2-51b7-317f-b22e-e44c5431b82b | 3.32113 | -60.20433 | 2026-03-21 05:04:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 863a8394-4203-3bd1-9da9-9f768a693c27 | 1.80932 | -60.67022 | 2026-03-21 05:04:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 914276bc-c47d-3ed0-a80f-d39509205240 | 2.59779 | -61.30244 | 2026-03-21 05:04:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b7a58ee5-9737-30df-8265-125db92f7c8a | 3.23328 | -60.1262 | 2026-03-21 05:04:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d25faa2a-aa17-38f1-a922-6d372d4130ea | 3.32493 | -60.19926 | 2026-03-21 05:04:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1235e6a7-10fc-3c8e-8489-522f608263ac | 3.23769 | -60.12548 | 2026-03-21 05:04:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 306b92b2-b1fa-334c-b19c-14788991077a | 1.97795 | -60.57117 | 2026-03-21 05:04:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c11f666-89c6-31a4-a6dd-e68ef703d12e | 3.23393 | -60.13049 | 2026-03-21 05:04:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d89bfe72-5472-368c-82c1-785a5f4da6f0 | 3.56335 | -60.16755 | 2026-03-21 05:04:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f4b231b3-7bac-3300-b4b1-79a1ba11d19a | 2.05859 | -61.81331 | 2026-03-21 05:04:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 07257d8e-7018-37cc-a9fb-5146df165541 | 3.3712 | -60.17434 | 2026-03-21 05:04:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 48a66811-124d-328b-a0aa-26c06e3d773a | 3.33696 | -60.18845 | 2026-03-21 05:04:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5373b1c7-6437-3e11-8d55-c0365512ca49 | 3.56402 | -60.17196 | 2026-03-21 05:04:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e2eb036b-297a-3515-8d27-c87b9c3c913a | 2.25409 | -60.2872 | 2026-03-21 05:04:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79e06814-02ec-38fd-b8e2-a8d16620b3a0 | 3.32938 | -60.1986 | 2026-03-21 05:04:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f7eb73f-7e7e-37a9-bae8-b78d55c86944 | 1.67041 | -60.50094 | 2026-03-21 05:04:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 03dfd128-5c78-3580-95ad-6ad83ae9531d | 1.55652 | -60.66934 | 2026-03-21 05:04:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 524fd756-e13a-308a-aadd-9d8ff91427d7 | 2.73352 | -60.45064 | 2026-03-21 05:04:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 239af5ac-12e0-3f73-9d71-9afb8b470693 | 3.23835 | -60.12978 | 2026-03-21 05:04:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 90b26202-de8a-335d-aa36-4106b221975c | 2.05288 | -61.80857 | 2026-03-21 05:04:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 91804e7c-3590-3262-a3f1-faeb6a1af220 | 3.36675 | -60.175 | 2026-03-21 05:04:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91f2c205-994d-30ed-a997-5094f648be0a | 3.3414 | -60.18778 | 2026-03-21 05:04:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d2d6a62e-ee05-3d2f-b69d-ca981ba061c2 | 3.56269 | -60.16315 | 2026-03-21 05:04:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aef4dce0-022f-3c2f-9d0f-1f86488866f9 | -8.43208 | -44.04452 | 2026-03-21 05:06:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d1f50ac5-ee6c-368e-a09b-e2e882f74088 | -8.43282 | -44.03889 | 2026-03-21 05:06:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 261a4e6d-5037-387e-8d49-3f3a2ebac258 | -8.43221 | -44.03705 | 2026-03-21 05:06:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4af24fbb-14f9-3088-a202-9a0d7526bb73 | -8.4315 | -44.04271 | 2026-03-21 05:06:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ae97e09e-e4c7-3b3e-9da4-48c25aba20d4 | -15.12259 | -59.34351 | 2026-03-21 05:08:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 715d2575-287d-30cf-b3b9-ec6866c8abdf | -21.38491 | -55.85991 | 2026-03-21 05:10:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bc3c2d3b-7bd3-3a38-a312-6eeecaf22689 | -23.59414 | -46.43334 | 2026-03-21 05:10:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 042365f6-a2c3-30f7-a9a5-34d655514169 | -21.81776 | -48.70935 | 2026-03-21 05:10:00 | NOAA-20 | TABATINGA | SÃO PAULO | Brasil | 3552700 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 62a952bf-1b30-3459-9b54-711a83739dfd | -21.81815 | -48.70522 | 2026-03-21 05:10:00 | NOAA-20 | TABATINGA | SÃO PAULO | Brasil | 3552700 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| eb81806b-1d55-364d-afe0-16b51c8c3abe | -25.43562 | -52.87959 | 2026-03-21 05:12:00 | NOAA-20 | QUEDAS DO IGUAÇU | PARANÁ | Brasil | 4120903 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 2b725f4a-22a9-3995-ab53-94f3a1859943 | -28.91274 | -55.96305 | 2026-03-21 05:12:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| b4cafef5-d681-3d1f-b5f2-8cdacdda1d5a | 2.05338 | -61.80658 | 2026-03-21 05:55:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e686ff9f-145d-3985-929f-e070a4a78d15 | 3.32492 | -60.1977 | 2026-03-21 05:55:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43ca06d8-fdb2-3a98-86ce-f656f203ce0e | 3.31697 | -60.20327 | 2026-03-21 05:55:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7562ea61-909a-3e09-8c29-47f025c7840d | 3.32128 | -60.20255 | 2026-03-21 05:55:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README3.md)
