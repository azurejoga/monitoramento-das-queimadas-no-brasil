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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c7a3828b-b7f8-388a-81eb-621991627c92 | -2.6388 | -46.7597 | 2026-09-07 02:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| ddb6d7ef-1d1c-3043-98fd-5bb5a321b63f | -13.3198 | -45.2409 | 2026-09-07 02:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 133.3 |
| a5f6f32d-38dc-3030-b2d5-1cda96a9cd18 | -2.8839 | -50.4428 | 2026-09-07 02:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 680cc6d6-6a10-3ec6-8034-66d03ba736d2 | -2.8655 | -50.4434 | 2026-09-07 02:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 713100d9-7f06-3d8f-af91-2752148aac25 | -3.1461 | -60.6696 | 2026-09-07 02:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 82.7 |
| a5c06978-264f-3460-932c-fc5c1db2fa05 | -13.3203 | -45.2177 | 2026-09-07 02:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 171.7 |
| ede1d500-7f20-3e24-9256-e918a71180ad | -2.6387 | -46.7817 | 2026-09-07 02:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 113.3 |
| 43cad42f-1f90-35bc-a11b-9f317fc4b327 | -13.3203 | -45.2177 | 2026-09-07 02:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 129.6 |
| 95db9dea-6f81-3222-b7a2-52e121976a9e | -13.3009 | -45.2209 | 2026-09-07 02:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 9dd9ff69-dce5-358b-99e0-d166496ab852 | -9.7328 | -43.4168 | 2026-09-07 02:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 184.6 |
| 0b76cf77-5299-3e9e-bd19-918dc9a4851a | -13.3004 | -45.2442 | 2026-09-07 02:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 12f47c01-c101-372e-ba78-37e1731aff2a | -9.7522 | -43.3907 | 2026-09-07 02:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 289.6 |
| 5ec52dcb-66b4-33e2-a45a-4f6bd8b13951 | -13.3198 | -45.2409 | 2026-09-07 02:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 124.6 |
| 80d34ef4-5cf1-3b94-ba20-a5199e5f348e | -6.0002 | -57.7079 | 2026-09-07 02:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 91d8b5da-bc48-371f-a2e7-b3f1e5cd8e97 | -3.1461 | -60.6696 | 2026-09-07 02:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 69.0 |
| b6129f8b-f920-3dca-8571-211f124a0951 | -9.7519 | -43.4143 | 2026-09-07 02:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 357.1 |
| 6a14d26e-c5b4-3036-849d-0de181dd1e04 | -2.6388 | -46.7597 | 2026-09-07 02:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 8f85b736-bdee-3ede-ac96-0cca612177a9 | -10.753 | -45.0724 | 2026-09-07 02:50:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 0c9c1291-277a-3191-8f7a-8bff3c2e5683 | -8.7437 | -62.4359 | 2026-09-07 02:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 9d1fd871-75d5-32cc-9985-c4c2110f3b77 | -2.6387 | -46.7817 | 2026-09-07 02:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 131.3 |
| 88f38930-3f43-3ad5-bc45-1e7936580240 | -9.4968 | -40.2839 | 2026-09-07 02:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 71.2 |
| 1b372821-7b11-36b4-b34c-6a469f489f3f | -13.2287 | -61.7355 | 2026-09-07 02:50:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 60.4 |
| b85ba8b5-3119-3609-856e-30ec4ff66e46 | -10.734 | -45.075 | 2026-09-07 02:50:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 105.1 |
| d42c0272-45b7-351e-b83b-7c84f1737cb5 | -2.8839 | -50.4428 | 2026-09-07 02:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 53575b68-b92f-3112-9e44-832b5b09f8d3 | -2.8655 | -50.4434 | 2026-09-07 02:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 79780a12-7389-37b1-a793-6ac785c4cd52 | -6.0004 | -57.6884 | 2026-09-07 02:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| cbba07ea-c2ec-313f-9e21-ce52d739cc68 | -9.7332 | -43.3932 | 2026-09-07 02:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 143.9 |
| a8b59deb-5312-3a67-a7d2-7c5a15e58cd2 | -15.9331 | -41.9772 | 2026-09-07 02:50:00 | GOES-19 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 5cbb0e35-27c6-3141-b34c-7952f30efeb8 | -13.2477 | -61.7342 | 2026-09-07 02:50:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 44baeb5c-aee6-3b8f-8432-85cdd6625c4b | -3.1462 | -60.6506 | 2026-09-07 02:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 22f28494-3468-3d40-b0f4-6c739d4e4c7f | -9.7325 | -43.4403 | 2026-09-07 03:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 9dbc14ad-22a7-3759-9e24-9d4475e8f711 | -2.8839 | -50.4428 | 2026-09-07 03:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| de5a7f37-e719-3f12-935b-9370912b5d5f | -13.3203 | -45.2177 | 2026-09-07 03:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 142.3 |
| fb1acd39-ffb3-330b-90a7-e00169f246a3 | -2.8655 | -50.4434 | 2026-09-07 03:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 530b0c24-54c5-3de2-ac27-e2f78d8f6145 | -3.1462 | -60.6506 | 2026-09-07 03:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 97b9ce0a-2b73-3843-af81-56facc959cf2 | -2.6387 | -46.7817 | 2026-09-07 03:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 6b3445f7-d682-3cb0-816f-ea08db839c1e | -3.1461 | -60.6696 | 2026-09-07 03:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 19116750-7006-3cb1-a225-09b48deeb120 | -13.3004 | -45.2442 | 2026-09-07 03:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 8744615b-f83d-3999-8ac7-1c418262f284 | -2.6203 | -46.7602 | 2026-09-07 03:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 27ed2f4f-c7d6-3a13-8bb3-156bf377bf77 | -15.9331 | -41.9772 | 2026-09-07 03:00:00 | GOES-19 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 53fd0b01-07c2-3f3f-84ee-807e01d828be | -10.7527 | -45.0954 | 2026-09-07 03:00:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 167.8 |
| 1a8688e1-29d5-3634-8caa-384cc3980301 | -10.7336 | -45.098 | 2026-09-07 03:00:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 174.1 |
| 0ee7587a-2083-357a-84a0-65b81f01113b | -2.6388 | -46.7597 | 2026-09-07 03:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| ab2b0489-4c34-3c42-b2b9-30e745b867ea | -9.4968 | -40.2839 | 2026-09-07 03:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 88.1 |
| 2b09fe2c-261a-3509-b285-824df0b98ce4 | -10.734 | -45.075 | 2026-09-07 03:00:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 331.7 |
| edea6e18-1ba3-335c-9346-fdf254f51ffb | -9.7332 | -43.3932 | 2026-09-07 03:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 119.4 |
| bb09e4b3-6ab9-34eb-a2f2-f2ffe21dafb6 | -13.3009 | -45.2209 | 2026-09-07 03:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 3943c61a-1352-30a4-accb-193971231cff | -9.7522 | -43.3907 | 2026-09-07 03:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 132.9 |
| f6c488ff-4930-3fbb-89c2-40c75fe7b231 | -13.3198 | -45.2409 | 2026-09-07 03:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 138.3 |
| 274806bf-0884-3bc0-833b-40c3fc3a2ddb | -10.753 | -45.0724 | 2026-09-07 03:00:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 332.0 |
| 3945cbcc-6b37-36b9-bfbb-ba531c661134 | -9.7328 | -43.4168 | 2026-09-07 03:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 210.7 |
| ed89f198-930f-34aa-a3a3-3149755bc043 | -9.7519 | -43.4143 | 2026-09-07 03:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 190.6 |
| 14eb1c8f-2988-3a0d-bdb4-177fd4fb1c5b | -2.6202 | -46.7822 | 2026-09-07 03:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| e4469790-6bd1-32d1-958d-d3ff25cad83f | -13.3009 | -45.2209 | 2026-09-07 03:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 178.8 |
| 922d5b93-b12b-3017-90af-c0d512e4a13f | -9.7522 | -43.3907 | 2026-09-07 03:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 157.7 |
| c94b3ef0-298f-3262-b336-ec03830bfea1 | -3.1462 | -60.6506 | 2026-09-07 03:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 78.4 |
| a3ad7c5f-8c50-37dc-a99d-091cccb28377 | -2.8655 | -50.4434 | 2026-09-07 03:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 24e2d39c-e8a8-3123-a5a7-766f4292171a | -2.6202 | -46.7822 | 2026-09-07 03:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 083b4724-5fea-353a-9490-b04f36c3880e | -9.7332 | -43.3932 | 2026-09-07 03:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 114.2 |
| 5efe0258-e053-34d2-8c2c-fa4798378152 | -10.753 | -45.0724 | 2026-09-07 03:10:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 1569ce42-f5d1-355f-901b-5bcea2ea812c | -2.6388 | -46.7597 | 2026-09-07 03:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 0a1a3540-c375-307f-88f4-2d2d9f6dfbf9 | -9.7519 | -43.4143 | 2026-09-07 03:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 184.6 |
| 2100f2c3-4503-394c-b6af-2401d1127371 | -13.2284 | -61.7743 | 2026-09-07 03:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 72.4 |
| e48ed742-707d-3a42-959c-29f1652a99d4 | -13.3203 | -45.2177 | 2026-09-07 03:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 195.3 |
| 7a797445-0359-392c-8a7e-bb69c1952bc1 | -9.7328 | -43.4168 | 2026-09-07 03:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 274.9 |
| 697e6399-0486-3d22-bfb3-2396cebdadff | -9.7325 | -43.4403 | 2026-09-07 03:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 67672a09-c797-3c23-8a2e-1180d8ec04a4 | -13.3198 | -45.2409 | 2026-09-07 03:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 170.0 |
| d9bce2be-c517-31b7-a7b2-9483e44d501d | -8.7622 | -62.4351 | 2026-09-07 03:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 53.9 |
| b4adcb4d-58dc-3ff3-a0c8-6533f2fad19b | -2.6387 | -46.7817 | 2026-09-07 03:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 5debfaef-cef9-3da1-a1a7-3ee15c48ce6c | -8.7437 | -62.4359 | 2026-09-07 03:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 42.4 |
| b053860f-6010-38c4-ba3a-f30f1222eea9 | -2.8839 | -50.4428 | 2026-09-07 03:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 103.8 |
| 50493a0a-d933-3e9f-a683-51f1bd00f6ed | -15.9331 | -41.9772 | 2026-09-07 03:10:00 | GOES-19 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 5562b422-fff6-3ff5-985d-c02ce76a1daa | -3.1461 | -60.6696 | 2026-09-07 03:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 96981fa6-7a53-34e3-a6ee-5c2ba46e9fec | -13.2094 | -61.7755 | 2026-09-07 03:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 855576b7-7b32-3739-864a-ca217781cf44 | -13.3004 | -45.2442 | 2026-09-07 03:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 155.0 |
| 3ad08757-05db-3d6c-b170-0a74232f4f17 | -13.2287 | -61.7355 | 2026-09-07 03:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 45.6 |
| ba38ae11-bd0b-34ab-9a87-59a22d0b5046 | -10.734 | -45.075 | 2026-09-07 03:10:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 469754f4-f659-30b8-b1cb-7941b415f586 | -9.71 | -43.42 | 2026-09-07 03:15:00 | MSG-03 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 7b497198-d52d-3d82-abca-5bee8e435f90 | -10.75 | -45.07 | 2026-09-07 03:15:00 | MSG-03 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 11956315-cef1-3ae3-a5b1-c1eb694610be | -9.74 | -43.43 | 2026-09-07 03:15:00 | MSG-03 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1b970a79-61e8-334e-8d7b-3157a96cf561 | -2.6203 | -46.7602 | 2026-09-07 03:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 95be78e9-47e1-3acd-b368-394c1427b0d9 | -10.734 | -45.075 | 2026-09-07 03:20:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 125.8 |
| d5c258d7-c0a4-3bfd-9e3f-6851de04225e | -3.1461 | -60.6696 | 2026-09-07 03:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 32d9c3b2-881b-306c-b33b-f3a80827a4a6 | -2.6202 | -46.7822 | 2026-09-07 03:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| d898e33c-7333-3227-8c40-efe9c646123d | -2.6388 | -46.7597 | 2026-09-07 03:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 76c5716b-9d1c-3116-9b1e-732fefad6356 | -15.9331 | -41.9772 | 2026-09-07 03:20:00 | GOES-19 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 70ee001a-89f9-3ff0-9904-fabdd740af77 | -10.753 | -45.0724 | 2026-09-07 03:20:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 010f42a6-6f5e-3477-9faa-ac20bc1e3e69 | -13.3198 | -45.2409 | 2026-09-07 03:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 204.8 |
| f4d53865-a6e7-36d5-9416-9ea46fb5e514 | -2.8655 | -50.4434 | 2026-09-07 03:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 95e49997-ba00-339e-8289-2348fba3018f | -13.3203 | -45.2177 | 2026-09-07 03:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 226.3 |
| 91ced0cc-96d4-3a27-b57c-6d94ed10b043 | -11.4998 | -49.6326 | 2026-09-07 03:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 9fac7a74-2cd3-35a5-9539-a6211ad67584 | -11.5188 | -49.6304 | 2026-09-07 03:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 95.7 |
| b2124986-f301-394b-9089-f93dd8c6b552 | -13.3009 | -45.2209 | 2026-09-07 03:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 208.6 |
| a706c9c7-f79e-3859-8316-4c1dee6c3743 | -11.5191 | -49.6087 | 2026-09-07 03:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 114.1 |
| a734e0f4-b256-348e-87ed-db2ab4e4762b | -2.6387 | -46.7817 | 2026-09-07 03:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| c788308f-3242-3907-9d15-c4659499f93b | -2.8839 | -50.4428 | 2026-09-07 03:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 925c479a-631c-3fcc-9017-38ed19de8d95 | -13.2287 | -61.7355 | 2026-09-07 03:20:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 46.7 |
| c8d2e3b2-b64b-3fac-b495-aea06b2ac10c | -13.2477 | -61.7342 | 2026-09-07 03:20:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 64861e1e-f2ac-33d8-b727-b46faa4397ca | -13.2284 | -61.7743 | 2026-09-07 03:20:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 52.4 |
| ff9de382-5845-34ae-bf65-3f8cae673a23 | -3.1462 | -60.6506 | 2026-09-07 03:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 69.7 |


[Clique aqui para ver as próximas entradas](README9.md)
