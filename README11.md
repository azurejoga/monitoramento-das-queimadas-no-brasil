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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 892e9ad2-60fd-325c-8791-f05b8861df07 | -9.4058 | -60.5904 | 2026-08-19 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 48.2 |
| ca973da2-e3db-36e3-a4a3-2a8aefed5f1e | -5.9994 | -57.8639 | 2026-08-19 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 133.7 |
| 4af1965a-5a8c-351b-b310-19e65be54c5d | -9.3873 | -60.5721 | 2026-08-19 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| aed7dfa6-dd3e-3106-b6ac-66cdac22adc1 | -19.7446 | -57.9217 | 2026-08-19 01:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.4 |
| cfd16d7f-5718-3af4-89cd-f62f36f5690a | -6.0912 | -57.9187 | 2026-08-19 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 125.8 |
| aae0c5c9-7907-3bf7-8e2d-eabb1f1ee7b8 | -9.406 | -60.5711 | 2026-08-19 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 35ed874e-f579-35dc-8539-58384faf8b28 | -5.4317 | -48.4212 | 2026-08-19 01:10:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 6579a1ca-2c2e-3099-8a7c-052223cb8b05 | -6.0913 | -57.8992 | 2026-08-19 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| e14832c8-3e6c-3255-825e-bfa4c3c75a3e | -14.0352 | -53.7017 | 2026-08-19 01:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 89.7 |
| ca07be98-8a4f-3bab-adcc-c4a17fb199a7 | -5.9198 | -43.6264 | 2026-08-19 01:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 219.4 |
| 5f9ed726-ace1-36c3-8cb6-6141d9813367 | -9.4257 | -60.416 | 2026-08-19 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 8829d525-490b-34d4-8e73-b672f2c73178 | -5.9995 | -57.8444 | 2026-08-19 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 01c15ec8-3f6d-30f3-b430-1a9b0abcb8cf | -8.55 | -54.78 | 2026-08-19 01:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a6f1146-a91b-3df8-846f-fe4cc08d9753 | -8.57 | -54.73 | 2026-08-19 01:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86351990-aa55-354a-bc94-2236b3e2db9e | -5.91 | -43.61 | 2026-08-19 01:15:00 | MSG-03 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2709835a-1a7f-3a01-b2a3-51ac2d6b0c4e | -8.54 | -54.72 | 2026-08-19 01:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70c6f4b6-aac9-384a-afa1-08472360ce3b | -9.4061 | -60.5518 | 2026-08-19 01:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 23f0a3a6-10e7-3fbe-9319-32e9f9b0b9cc | -5.9995 | -57.8444 | 2026-08-19 01:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 209c9860-9f52-3e3e-8069-01e4459bd0a6 | -19.7639 | -57.9607 | 2026-08-19 01:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 118.3 |
| 57f583fb-8659-355a-9c48-52ee50f433df | -6.6938 | -58.942 | 2026-08-19 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 106.8 |
| 92a8cb43-0e56-35e9-8e86-e0ad2ca54468 | -6.0178 | -57.8631 | 2026-08-19 01:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| c0157094-8532-35af-bcab-e93a4ecc9eb5 | -19.7438 | -57.9633 | 2026-08-19 01:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.4 |
| f5d2632e-6cb7-3fe1-b39e-bcdfca1d540b | -7.0577 | -59.8331 | 2026-08-19 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 2d60f232-84c1-3643-9372-706dc0e44128 | -5.9198 | -43.6264 | 2026-08-19 01:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 274.7 |
| a2e290ec-65aa-364f-b554-2e178ecde4f8 | -9.3875 | -60.5528 | 2026-08-19 01:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 7f297918-60c3-352c-8653-3df84afaaa6b | -6.8593 | -59.0318 | 2026-08-19 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 38e70324-dfd9-3209-a75d-61174ac3e048 | -6.7123 | -58.9412 | 2026-08-19 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 862a8f3f-57e1-318b-ba40-25aedbd996ee | -6.0912 | -57.9187 | 2026-08-19 01:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 115.8 |
| b1b21302-b7b2-383e-8e0d-dba918663520 | -9.4257 | -60.416 | 2026-08-19 01:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 30c1ab2f-084e-3a06-909d-288c131ac3d7 | -7.5487 | -55.5829 | 2026-08-19 01:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| b1a5627f-b1f2-3881-b4f2-dca50048fc68 | -9.3873 | -60.5721 | 2026-08-19 01:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 69.4 |
| fecab1b0-41b8-3669-b5bb-de63bb34a694 | -5.4319 | -48.3996 | 2026-08-19 01:20:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| ed3e2cac-92f8-3c9d-b3f3-b3d9def7dc58 | -5.9011 | -43.6279 | 2026-08-19 01:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| fb84fecf-46ac-3268-9fe2-33ff408db84d | -9.0865 | -50.7979 | 2026-08-19 01:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 4dbca8f2-7442-3565-ac15-38fceb61dded | -5.4317 | -48.4212 | 2026-08-19 01:20:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 118.6 |
| a7553468-7e12-30e3-a425-812babf36fea | -7.5301 | -55.5839 | 2026-08-19 01:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| c055f9cb-184d-3811-9246-fdfefb139bcb | -5.92 | -43.6032 | 2026-08-19 01:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 930bea6f-f0c8-3e0a-9bac-d6df1a1f71f8 | -5.9994 | -57.8639 | 2026-08-19 01:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 142.5 |
| 7d191703-5a76-3bd1-a79c-a01ada55d2ad | -19.7442 | -57.9425 | 2026-08-19 01:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 156.8 |
| c12feb83-db95-37cb-9cc1-040ab1463193 | -6.3496 | -54.9068 | 2026-08-19 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| a04bd13a-7534-372a-89d5-a449492543b6 | -19.7643 | -57.9399 | 2026-08-19 01:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.8 |
| 0f2249bb-602f-3e60-8912-a9e423444043 | -6.0913 | -57.8992 | 2026-08-19 01:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 42.8 |
| dd676da0-1d1b-32a2-b42d-dec5ab7bc273 | -9.406 | -60.5711 | 2026-08-19 01:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 6d6e6c65-20be-32ec-ba73-aaad7f6adf6e | -6.0728 | -57.9194 | 2026-08-19 01:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| c9975609-482b-362b-ade1-5e05902b2424 | -19.7241 | -57.9452 | 2026-08-19 01:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.5 |
| f0a0461d-24a6-3666-8825-c27a3898650a | -9.4256 | -60.4353 | 2026-08-19 01:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 7bf840fa-a686-3a7a-a3b8-c5298ddeef6e | -6.7486 | -59.0364 | 2026-08-19 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 59624dfc-43b6-3424-a873-663bac4203de | -16.2623 | -57.665298 | 2026-08-19 01:23:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 07fc7520-8233-3fc6-b5ec-20f0ed3eb39f | -9.2037 | -60.785301 | 2026-08-19 01:23:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 375a29b6-0dcb-3659-add0-8da0db2f3100 | -15.1948 | -48.219501 | 2026-08-19 01:23:00 | METOP-C | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 35d64dd6-580c-3380-97d6-843e4b007dc4 | -6.8405 | -56.457802 | 2026-08-19 01:23:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6159660a-4345-3dbe-b1f1-40a3bb85fdb6 | -9.2863 | -56.8946 | 2026-08-19 01:23:00 | METOP-C | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e2b36c6c-3e64-3660-b544-48e767bab77a | -8.5069 | -54.867001 | 2026-08-19 01:23:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e98ee3b0-7e54-3c2e-98f9-02078c14d879 | -15.3154 | -56.443199 | 2026-08-19 01:23:00 | METOP-C | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8ed0e639-0870-34b3-8501-3b490a16fbbb | -9.1187 | -61.610199 | 2026-08-19 01:23:00 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c95801ac-3a7d-3349-b013-03853f86e124 | -19.749201 | -57.9436 | 2026-08-19 01:23:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a0350d19-e10f-387f-b0bf-a49039ff27a9 | -8.5664 | -54.728001 | 2026-08-19 01:23:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| acd92992-87b2-3c98-bac4-587b1afcd09b | -6.8904 | -59.0299 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 986d0991-240f-3cf3-aacc-19f6f1837a11 | -9.424 | -60.434601 | 2026-08-19 01:23:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fd3f9dad-42d6-3b69-a4d2-5f1f1264feaa | -6.141 | -57.882401 | 2026-08-19 01:23:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e393a6fb-81e7-39bd-a583-13d846b70922 | -15.886 | -55.562199 | 2026-08-19 01:23:00 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 49e1c34d-4d8c-3297-95d4-be7d8bbe6c87 | -7.0542 | -59.837898 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 503a2e25-d562-3c1f-942d-b9bdfc05bdfc | -8.225 | -55.026501 | 2026-08-19 01:23:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba0949db-f74b-3de6-b79b-a467c78650fc | -12.9445 | -56.6395 | 2026-08-19 01:23:00 | METOP-C | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e1358996-6bb0-309f-a7e2-17ca762d388d | -19.739401 | -57.9459 | 2026-08-19 01:23:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 479a0071-f173-31ea-ae18-ac96834ded7d | -6.6845 | -59.076401 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 70b92a37-b5d7-39aa-ba8b-be352c8a561d | -15.5832 | -49.828899 | 2026-08-19 01:23:00 | METOP-C | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1a5c5b43-0ffc-3271-8c56-d0e1013b3888 | -15.3188 | -56.457802 | 2026-08-19 01:23:00 | METOP-C | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e8dd2618-956e-3b0b-9ab6-71d39d1ac687 | -7.4618 | -59.9991 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7201f8d1-81c5-37c1-b2e8-5e67bb8154b3 | -6.3533 | -54.9235 | 2026-08-19 01:23:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17a984ac-5c6f-35a0-a5aa-3e3a42ba9d50 | -6.7369 | -59.0354 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7776b026-3128-3ad6-ba9b-f188b50dfcbe | -6.9074 | -62.904598 | 2026-08-19 01:23:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1b080ce4-0a5e-36ca-8a36-c420f603a28e | -6.7644 | -59.470699 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 66eff242-ad61-398e-a7d8-446b8b5f5a24 | -9.4275 | -60.4039 | 2026-08-19 01:23:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 00d4ceeb-e696-3116-8b87-1361e9afa307 | -15.2782 | -56.506001 | 2026-08-19 01:23:00 | METOP-C | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3307c4ba-3b33-3333-88cb-c542ce9e8ebb | -6.8562 | -59.015701 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 76dc62a7-eb19-3fd1-88e7-79abdf3e4af8 | -21.4522 | -48.519299 | 2026-08-19 01:23:00 | METOP-C | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| db484db0-2185-378a-91eb-12e2cbbb88d5 | -6.0016 | -57.8596 | 2026-08-19 01:23:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 290883d9-6bc2-369c-9f40-c0fe965ef4b4 | -8.9615 | -60.529999 | 2026-08-19 01:23:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e95ea797-ce4f-3590-a264-c14940732503 | -4.2865 | -60.8587 | 2026-08-19 01:23:00 | METOP-C | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e68de238-b6e7-3eb5-9bd0-8cb775550dbe | -6.1225 | -57.713902 | 2026-08-19 01:23:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e727965-701d-3831-8f9e-95c004bae3ea | -6.8936 | -59.043701 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a573edd2-267e-3715-a2a4-ca856af958b1 | -5.4469 | -48.4384 | 2026-08-19 01:23:00 | METOP-C | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 926cf18b-2a2d-3549-bd7d-120be277ba24 | -15.5929 | -49.826199 | 2026-08-19 01:23:00 | METOP-C | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6f40a3d1-a1d1-3d2b-8e4e-2c054d6131cd | -6.8004 | -59.4482 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7ff05ece-5ebf-32d9-8da5-2dfbae86d47f | -6.7612 | -59.457001 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f1bf3e36-afaa-33cb-87ee-d6492cc05afd | -6.7484 | -59.040199 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3103d4bb-fb73-3d10-bc57-f8682c6e88cf | -9.4306 | -60.418098 | 2026-08-19 01:23:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d22f459a-e43b-3b8c-9f7b-c300ff2ade6a | -8.5588 | -54.782101 | 2026-08-19 01:23:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fcd74cbd-a118-3414-9187-a821b781b486 | -6.8433 | -59.004101 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 62e0b2aa-3986-3e6a-b21d-28c6bdf6ad13 | -9.3987 | -60.598202 | 2026-08-19 01:23:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| adc6eda5-0427-3be8-a7cd-719e3782feba | -29.137501 | -50.385601 | 2026-08-19 01:23:00 | METOP-C | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cd771169-9541-3334-a922-bc789995af1d | -10.1965 | -54.248199 | 2026-08-19 01:23:00 | METOP-C | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5fc31744-712c-3945-b729-dc07646e49ac | -14.3368 | -51.9533 | 2026-08-19 01:23:00 | METOP-C | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1256570e-f64f-3dc8-a5e3-a31fbaedf0db | -6.8134 | -59.459702 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b3ae29b5-1e1a-36bd-92cb-2b0d6b263bcd | -11.206 | -54.021198 | 2026-08-19 01:23:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7c69b347-7649-388a-a87c-b0ec3199987b | -9.0822 | -50.794498 | 2026-08-19 01:23:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91de8535-98e5-357e-ad84-428aa047c6a5 | -8.5346 | -54.766899 | 2026-08-19 01:23:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc865c37-aa06-32f9-8441-bd9cc7d41466 | -5.5016 | -60.127899 | 2026-08-19 01:23:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0dc163d2-322c-33fb-8220-649c766fd3d2 | -23.0492 | -50.3158 | 2026-08-19 01:23:00 | METOP-C | ANDIRÁ | PARANÁ | Brasil | 4101101 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |


[Clique aqui para ver as próximas entradas](README12.md)
